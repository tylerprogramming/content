#!/usr/bin/env python3
"""
ledger.py - the content ledger. One row per piece of content on any platform.

Store: ~/content/system/ledger/ledger.jsonl  (one JSON object per line, append-friendly, git-diffable)
Views: ledger.py status | list | add | set | sync-youtube | export

Written by skills (yt-package, yt-upload, social-copy, Blotato scheduling) and bots, not by hand.
Stages: idea -> packaged -> filmed -> editing -> scheduled -> live  (also: parked, superseded)

Usage:
  ledger.py add --kind long --platform youtube --title "..." --path youtube/videos/064-x --stage packaged
  ledger.py set 064 --stage filmed --record-date 2026-10-28
  ledger.py set 064 --stage scheduled --publish-at 2026-11-02T13:15:00-04:00 --external-id dQw4w9WgXcQ
  ledger.py add --kind post --platform linkedin --title "..." --parent 064 --publish-at ... --external-id <blotato postId>
  ledger.py sync-youtube            # match live videos by id/title, update views
  ledger.py status                  # dashboard text
  ledger.py list --stage packaged   # filter
  ledger.py export                  # write ledger.csv + tracker-generated.md
"""
import argparse, csv, json, os, re, sys, uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(os.environ.get("CONTENT_ROOT", Path.home() / "content"))
DIR = ROOT / "system" / "ledger"
FILE = DIR / "ledger.jsonl"
STAGES = ["idea", "packaged", "filmed", "editing", "scheduled", "live", "parked", "superseded"]
KINDS = ["long", "short", "reel", "carousel", "post", "thread", "pin", "email", "skool", "community"]
PLATFORMS = ["youtube", "tiktok", "instagram", "linkedin", "x", "pinterest", "skool", "email", "youtube-community", "threads", "bluesky"]
FIELDS = ["id", "kind", "platform", "title", "path", "stage", "parent", "record_date", "publish_at",
          "external_id", "url", "views", "views_7d", "views_28d", "likes", "comments", "ctr", "notes",
          "created_at", "updated_at", "source"]


def now():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def load():
    if not FILE.exists():
        return []
    rows = []
    for line in FILE.read_text().splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def save(rows):
    DIR.mkdir(parents=True, exist_ok=True)
    tmp = FILE.with_suffix(".tmp")
    with tmp.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(FILE)


def find(rows, key):
    """Match by id, external_id, or NNN video number prefix."""
    for r in rows:
        if r["id"] == key or r.get("external_id") == key:
            return r
    m = re.fullmatch(r"\d{3}", key)
    if m:
        hits = [r for r in rows if r["kind"] == "long" and (r.get("path") or "").split("/")[-1].startswith(key + "-")]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            sys.exit(f"ambiguous: {key} matches {[h['id'] for h in hits]}")
    return None


def new_id(kind, path=None, platform=None):
    if kind == "long" and path:
        m = re.match(r"(\d{3})-", Path(path).name)
        if m:
            return f"v{m.group(1)}"
    return f"{kind[:1]}{platform[:2] if platform else 'xx'}-{uuid.uuid4().hex[:6]}"


def cmd_add(a):
    rows = load()
    rid = a.id or new_id(a.kind, a.path, a.platform)
    if find(rows, rid):
        sys.exit(f"exists: {rid} (use set)")
    r = {k: None for k in FIELDS}
    r.update(id=rid, kind=a.kind, platform=a.platform, title=a.title, path=a.path, stage=a.stage,
             parent=a.parent, record_date=a.record_date, publish_at=a.publish_at, external_id=a.external_id,
             url=a.url, notes=a.notes, created_at=now(), updated_at=now(), source=a.source or "cli")
    rows.append(r)
    save(rows)
    print(json.dumps(r))


def cmd_set(a):
    rows = load()
    r = find(rows, a.key)
    if not r:
        sys.exit(f"not found: {a.key}")
    for k in ["stage", "title", "path", "parent", "record_date", "publish_at", "external_id", "url", "notes", "platform", "kind"]:
        v = getattr(a, k, None)
        if v is not None:
            r[k] = v
    if a.append_note:
        r["notes"] = ((r.get("notes") or "") + " | " + a.append_note).strip(" |")
    r["updated_at"] = now()
    save(rows)
    print(json.dumps(r))


def cmd_list(a):
    rows = load()
    out = [r for r in rows
           if (not a.stage or r["stage"] == a.stage)
           and (not a.kind or r["kind"] == a.kind)
           and (not a.platform or r["platform"] == a.platform)
           and (not a.parent or r.get("parent") == a.parent)]
    if a.json:
        print(json.dumps(out, indent=1))
        return
    for r in out:
        print(f"{r['id']:<14} {r['stage']:<10} {r['kind']:<8} {r['platform']:<12} {(r.get('publish_at') or r.get('record_date') or '')[:10]:<10} {r['title'][:70]}")
    print(f"-- {len(out)} rows")


def _dt(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def cmd_status(a):
    rows = load()
    today = datetime.now(timezone.utc).astimezone()
    wk_ago, wk_ahead, mo_ago = today - timedelta(days=7), today + timedelta(days=7), today - timedelta(days=30)
    longs = [r for r in rows if r["kind"] == "long"]
    by = lambda st: [r for r in longs if r["stage"] == st]
    live_week = [r for r in rows if r["stage"] == "live" and (_dt(r.get("publish_at")) or today - timedelta(days=999)) >= wk_ago]
    sched = sorted([r for r in rows if r["stage"] == "scheduled" and _dt(r.get("publish_at")) and _dt(r["publish_at"]) <= wk_ahead], key=lambda r: r["publish_at"])
    stale = [r for r in by("packaged") if (_dt(r.get("created_at")) or today) < mo_ago]

    print(f"CONTENT STATUS  {today:%a %Y-%m-%d}   ({len(rows)} rows, {len(longs)} long-form)\n")
    print("Long-form pipeline: " + "  ".join(f"{st} {len(by(st))}" for st in ["idea", "packaged", "filmed", "editing", "scheduled", "live", "parked", "superseded"]))
    print()
    print(f"Published last 7 days ({len(live_week)}):")
    for r in sorted(live_week, key=lambda r: r["publish_at"] or "", reverse=True):
        print(f"  {r['publish_at'][:10]}  {r['platform']:<10} {r['kind']:<8} {r['title'][:60]}  {('views ' + str(r['views'])) if r.get('views') is not None else ''}")
    print(f"\nScheduled next 7 days ({len(sched)}):")
    for r in sched:
        print(f"  {r['publish_at'][:16]}  {r['platform']:<10} {r['kind']:<8} {r['title'][:60]}")
    print(f"\nIn flight (filmed/editing):")
    for r in by("filmed") + by("editing"):
        print(f"  {r['id']:<6} {r['stage']:<8} {r['title'][:60]}  recorded {r.get('record_date') or '?'}")
    print(f"\nFilm queue (packaged, {len(by('packaged'))}), oldest first:")
    for r in sorted(by("packaged"), key=lambda r: r.get("created_at") or ""):
        flag = "  STALE >30d" if r in stale else ""
        print(f"  {r['id']:<6} {r['title'][:60]}  {r.get('path','')}{flag}")
    # per-platform counts last 30d
    plat = {}
    for r in rows:
        d = _dt(r.get("publish_at"))
        if r["stage"] == "live" and d and d >= mo_ago:
            plat[r["platform"]] = plat.get(r["platform"], 0) + 1
    print("\nLive last 30 days by platform: " + (", ".join(f"{k} {v}" for k, v in sorted(plat.items())) or "none recorded"))


def cmd_sync_youtube(a):
    """Pull the channel's uploads and update views; create rows for live videos we don't have."""
    sys.path.insert(0, str(Path.home() / ".claude" / "skills" / "yt-analytics"))
    try:
        import yt_analytics as ya
        from googleapiclient.discovery import build
    except ImportError as e:
        sys.exit(f"yt-analytics deps missing: {e}")
    creds = ya.authenticate()
    yt = build("youtube", "v3", credentials=creds)
    ch = yt.channels().list(part="id", mine=True).execute()["items"][0]["id"]
    vids = ya.get_recent_videos(yt, ch, max_results=a.max, shorts_only=False) + ya.get_recent_videos(yt, ch, max_results=a.max, shorts_only=True)
    rows = load()
    by_ext = {r.get("external_id"): r for r in rows if r.get("external_id")}
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    by_title = {norm(r["title"]): r for r in rows if r["platform"] == "youtube"}
    added = updated = 0
    for v in vids:
        r = by_ext.get(v["id"]) or by_title.get(norm(v["title"]))
        if not r:
            r = {k: None for k in FIELDS}
            r.update(id=f"yt-{v['id']}", kind="short" if v["isShort"] else "long", platform="youtube", title=v["title"],
                     stage="live", created_at=now(), source="sync-youtube")
            rows.append(r); added += 1
        r.update(external_id=v["id"], url=f"https://youtu.be/{v['id']}", stage="live", publish_at=v["publishedAt"],
                 views=v["views"], likes=v["likes"], comments=v["comments"], updated_at=now())
        if r["kind"] == "long" and v["isShort"]:
            r["kind"] = "short"
        updated += 1
    save(rows)
    print(f"youtube sync: {updated} updated, {added} added (channel {ch})")


def cmd_export(a):
    rows = load()
    with (DIR / "ledger.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in FIELDS})
    # generated inventory
    L = ["# Content Tracker (generated)", "", f"Generated {now()[:16]} from `system/ledger/ledger.jsonl` by `ledger.py export`. Do not edit; edit the ledger.", ""]
    for st in ["live", "scheduled", "editing", "filmed", "packaged", "idea", "parked", "superseded"]:
        sub = [r for r in rows if r["kind"] == "long" and r["stage"] == st]
        if not sub:
            continue
        L += [f"## {st} ({len(sub)})", "", "| id | title | folder | date | url | views |", "|---|---|---|---|---|---|"]
        for r in sorted(sub, key=lambda r: r.get("publish_at") or r.get("record_date") or r.get("created_at") or "", reverse=True):
            L.append(f"| {r['id']} | {r['title']} | `{r.get('path') or ''}` | {(r.get('publish_at') or r.get('record_date') or '')[:10]} | {r.get('url') or ''} | {r.get('views') if r.get('views') is not None else ''} |")
        L.append("")
    other = [r for r in rows if r["kind"] != "long"]
    if other:
        L += [f"## Other content ({len(other)})", "", "| id | kind | platform | title | parent | date | stage |", "|---|---|---|---|---|---|---|"]
        for r in sorted(other, key=lambda r: r.get("publish_at") or "", reverse=True):
            L.append(f"| {r['id']} | {r['kind']} | {r['platform']} | {r['title'][:60]} | {r.get('parent') or ''} | {(r.get('publish_at') or '')[:10]} | {r['stage']} |")
    (ROOT / "system" / "tracker-generated.md").write_text("\n".join(L) + "\n")
    print(f"wrote {DIR/'ledger.csv'} and {ROOT/'system'/'tracker-generated.md'} ({len(rows)} rows)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("add"); x.add_argument("--id"); x.add_argument("--kind", required=True, choices=KINDS); x.add_argument("--platform", required=True, choices=PLATFORMS)
    x.add_argument("--title", required=True); x.add_argument("--path"); x.add_argument("--stage", default="idea", choices=STAGES); x.add_argument("--parent")
    x.add_argument("--record-date"); x.add_argument("--publish-at"); x.add_argument("--external-id"); x.add_argument("--url"); x.add_argument("--notes"); x.add_argument("--source")
    x.set_defaults(fn=cmd_add)
    x = sp.add_parser("set"); x.add_argument("key"); x.add_argument("--stage", choices=STAGES); x.add_argument("--title"); x.add_argument("--path"); x.add_argument("--parent")
    x.add_argument("--kind", choices=KINDS); x.add_argument("--platform", choices=PLATFORMS)
    x.add_argument("--record-date"); x.add_argument("--publish-at"); x.add_argument("--external-id"); x.add_argument("--url"); x.add_argument("--notes"); x.add_argument("--append-note")
    x.set_defaults(fn=cmd_set)
    x = sp.add_parser("list"); x.add_argument("--stage"); x.add_argument("--kind"); x.add_argument("--platform"); x.add_argument("--parent"); x.add_argument("--json", action="store_true"); x.set_defaults(fn=cmd_list)
    x = sp.add_parser("status"); x.set_defaults(fn=cmd_status)
    x = sp.add_parser("sync-youtube"); x.add_argument("--max", type=int, default=200); x.set_defaults(fn=cmd_sync_youtube)
    x = sp.add_parser("export"); x.set_defaults(fn=cmd_export)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
