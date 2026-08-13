#!/usr/bin/env python3
"""Pull the last N uploads for a set of channels and score each against that
channel's OWN median views. Raw views compare channel sizes; the outlier
multiple compares a video to what that channel normally does, which is the only
way to read a 500K channel and a 20K channel on the same page.

Writes one CSV per channel plus a combined CSV, into ../data/.

    python3 competitor-pull.py @indydevdan @DavidOndrej ...
"""
import csv
import json
import os
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude" / "skills" / "yt-analytics"))

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKEN = Path.home() / ".claude" / "analytics" / "yt_token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
OUT = Path(__file__).resolve().parent.parent / "data"
SHORTS_MAX_SECONDS = 180


def client():
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not creds.valid and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def duration_seconds(iso):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", str(iso or ""))
    if not m:
        return 0
    h, mi, s = (int(g or 0) for g in m.groups())
    return h * 3600 + mi * 60 + s


def fmt_dur(sec):
    return f"{sec // 60}:{sec % 60:02d}"


def resolve(yt, handle):
    """Handle -> (channel_id, title, subs, uploads_playlist)."""
    h = handle.lstrip("@")
    r = yt.channels().list(part="id,snippet,statistics,contentDetails",
                           forHandle=h).execute()
    items = r.get("items") or []
    if not items:
        # fall back to search when the handle does not resolve directly
        s = yt.search().list(part="snippet", q=h, type="channel",
                             maxResults=1).execute().get("items") or []
        if not s:
            return None
        cid = s[0]["snippet"]["channelId"]
        r = yt.channels().list(part="id,snippet,statistics,contentDetails",
                               id=cid).execute()
        items = r.get("items") or []
        if not items:
            return None
    c = items[0]
    return (c["id"], c["snippet"]["title"],
            int(c["statistics"].get("subscriberCount", 0) or 0),
            c["contentDetails"]["relatedPlaylists"]["uploads"])


def recent_uploads(yt, playlist, limit=30):
    ids, token = [], None
    while len(ids) < limit:
        r = yt.playlistItems().list(part="contentDetails", playlistId=playlist,
                                    maxResults=50, pageToken=token).execute()
        ids += [i["contentDetails"]["videoId"] for i in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token:
            break
    ids = ids[:limit]
    out = []
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,statistics,contentDetails",
                             id=",".join(ids[i:i + 50])).execute()
        for v in r.get("items", []):
            sec = duration_seconds(v["contentDetails"]["duration"])
            st = v.get("statistics", {})
            pub = v["snippet"]["publishedAt"]
            age = (datetime.now(timezone.utc)
                   - datetime.fromisoformat(pub.replace("Z", "+00:00"))).days
            out.append({
                "id": v["id"],
                "date": pub[:10],
                "age_days": age,
                "title": v["snippet"]["title"],
                "dur": fmt_dur(sec),
                "seconds": sec,
                "is_short": 0 < sec <= SHORTS_MAX_SECONDS,
                "views": int(st.get("viewCount", 0) or 0),
                "likes": int(st.get("likeCount", 0) or 0),
                "comments": int(st.get("commentCount", 0) or 0),
                "thumb": v["snippet"]["thumbnails"].get("high", {}).get("url", ""),
            })
    # keep upload order, newest first
    order = {v: i for i, v in enumerate(ids)}
    out.sort(key=lambda r: order[r["id"]])
    return out


FIELDS = ["date", "age_days", "title", "dur", "seconds", "is_short", "views",
          "outlier", "likes", "comments", "engagement_pct", "id", "thumb"]


def score(rows):
    """Outlier vs the channel's own long-form median. Shorts are scored against
    the shorts median separately - mixing them makes every long-form look dead
    on a channel that posts shorts."""
    longs = [r["views"] for r in rows if not r["is_short"]]
    shorts = [r["views"] for r in rows if r["is_short"]]
    lmed = statistics.median(longs) if longs else 0
    smed = statistics.median(shorts) if shorts else 0
    for r in rows:
        med = smed if r["is_short"] else lmed
        r["outlier"] = round(r["views"] / med, 2) if med else 0
        r["engagement_pct"] = (round((r["likes"] + r["comments"]) / r["views"] * 100, 2)
                               if r["views"] else 0)
    return lmed, smed


def main():
    handles = sys.argv[1:]
    if not handles:
        print("usage: competitor-pull.py @handle [@handle ...]", file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    yt = client()
    stamp = datetime.now().strftime("%Y-%m-%d")
    summary, combined = [], []

    for h in handles:
        info = resolve(yt, h)
        if not info:
            print(f"!! could not resolve {h}", file=sys.stderr)
            continue
        cid, title, subs, playlist = info
        rows = recent_uploads(yt, playlist, 30)
        lmed, smed = score(rows)
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        path = OUT / f"{stamp}-{slug}-last30.csv"
        with path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        for r in rows:
            combined.append({**{k: r.get(k) for k in FIELDS},
                             "channel": title, "subs": subs})
        longs = [r for r in rows if not r["is_short"]]
        summary.append({
            "handle": h, "channel": title, "subs": subs,
            "videos": len(rows), "longform": len(longs),
            "shorts": len(rows) - len(longs),
            "longform_median_views": int(lmed), "shorts_median_views": int(smed),
            "best": max(rows, key=lambda r: r["outlier"])["title"] if rows else "",
            "best_outlier": max((r["outlier"] for r in rows), default=0),
            "csv": path.name,
        })
        print(f"{title:28s} {subs:>9,} subs  {len(rows)} vids  "
              f"long med {int(lmed):,}  short med {int(smed):,}", file=sys.stderr)

    comb = OUT / f"{stamp}-competitors-combined.csv"
    with comb.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["channel", "subs"] + FIELDS,
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(combined)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
