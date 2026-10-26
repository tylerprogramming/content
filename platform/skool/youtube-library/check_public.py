#!/usr/bin/env python3
"""Gate: a video may become a lesson or a post ONLY if it is live on Tyler's channel.

Live = on HIS channel, privacyStatus == "public", no future publishAt, uploadStatus "processed".
Unlisted, private, scheduled (premiere/publishAt in the future) or someone else's video -> NOT live.

usage: python check_public.py <id-or-url> [...]        exit 0 only if every video is live
       python check_public.py --json <id> [...]       machine-readable
Uses the YouTube Data API with ~/.claude/analytics/yt_token.json (same token as yt-analytics).
"""
import json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN = Path.home() / ".claude/analytics/yt_token.json"


def vid_of(s):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", s)
    return m.group(1) if m else s.strip()


def check(ids):
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid and creds.refresh_token:
        creds.refresh(Request())
    yt = build("youtube", "v3", credentials=creds, cache_discovery=False)
    mine = {c["id"] for c in yt.channels().list(part="id", mine=True).execute().get("items", [])}
    found = {}
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,status", id=",".join(ids[i:i + 50])).execute()
        for v in r.get("items", []):
            found[v["id"]] = v
    now = datetime.now(timezone.utc)
    out = []
    for vid in ids:
        v = found.get(vid)
        if not v:
            out.append({"id": vid, "live": False, "why": "not found (deleted, or private on another channel)"}); continue
        st, sn = v["status"], v["snippet"]
        why = []
        if sn["channelId"] not in mine:
            why.append(f"not your channel ({sn.get('channelTitle')})")
        if st.get("privacyStatus") != "public":
            why.append(f"privacy is {st.get('privacyStatus')}")
        pa = st.get("publishAt")
        if pa and datetime.fromisoformat(pa.replace("Z", "+00:00")) > now:
            why.append(f"scheduled to publish {pa}")
        if st.get("uploadStatus") not in (None, "processed"):
            why.append(f"upload status {st.get('uploadStatus')}")
        out.append({"id": vid, "title": sn["title"], "published": sn.get("publishedAt"),
                    "privacy": st.get("privacyStatus"), "live": not why, "why": "; ".join(why) or "public on your channel"})
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        sys.exit(__doc__)
    res = check([vid_of(a) for a in args])
    if "--json" in sys.argv:
        print(json.dumps(res, indent=1))
    else:
        for r in res:
            print(("LIVE    " if r["live"] else "BLOCKED ") + r["id"], "|", r.get("title", "?"), "|", r["why"])
    sys.exit(0 if all(r["live"] for r in res) else 1)
