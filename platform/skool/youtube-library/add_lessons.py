#!/usr/bin/env python3
"""Add new videos to the YouTube Library course as finished lessons (video + brief + guide PDF + links).

usage (on the box, in a dir holding the json + guide PDFs):
  /opt/scripts/.venv/bin/python add_lessons.py briefs-06-10.json [--apply]
JSON is keyed by YouTube id, in the order lessons should be created (Skool has no reorder API).
Idempotent: a lesson whose title already exists is skipped.
"""
import json, os, sys, urllib.request
from pathlib import Path
os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api import SkoolClient
from skool_api.endpoints import classroom as cls
from skool_api.richtext import md_to_v2, validate_v2, flatten_v2

G = "291a78f5b31f45a7982cc512bae3c9df"
COURSE, SLUG = "31b0709529e1440ea64abf80d6621741", "d8e99302"
P = str(Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json")
ck = {c["name"]: c["value"] for c in json.loads(Path(P).read_text())}
client = SkoolClient(cookies_path=P, group_slug="the-ai-agency", group_uuid=G)
spec = json.loads(Path(sys.argv[1]).read_text())
APPLY = "--apply" in sys.argv


def thumb(vid):
    for q in ("maxresdefault", "hqdefault"):
        u = f"https://img.youtube.com/vi/{vid}/{q}.jpg"
        try:
            with urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=10) as r:
                if r.status == 200:
                    return u
        except Exception:
            pass
    raise SystemExit(f"no thumbnail for {vid}")


sys.path.insert(0, str(Path(__file__).parent))
from live_gate import require_live          # noqa: E402
from dup_gate import classroom_videos, library_titles   # noqa: E402
require_live(list(spec), Path(__file__).parent)   # nothing goes in the course unless it's public on the channel

# DUPLICATE GUARD (by YouTube id, against the LIVE course, not the json or titles).
if len(set(spec)) != len(spec):
    sys.exit("BLOCKED: the same video id appears twice in the json.")
lessons = classroom_videos()
have = library_titles()
todo = {}
for vid, s in spec.items():
    in_lib = [l for c, l in lessons.get(vid, []) if c == "YouTube Library"]
    if in_lib:
        print(f"ALREADY IN COURSE, skipped: {vid} is lesson {in_lib[0]!r}"); continue
    if s["title"] in have:
        sys.exit(f"BLOCKED: title {s['title']!r} is already used by a different lesson. Rename it. Nothing was written.")
    others = [f"{c} > {l}" for c, l in lessons.get(vid, [])]
    if others:
        print(f"note: {vid} is also a lesson in {others} (fine, the Library is the archive)")
    todo[vid] = s

for vid, s in todo.items():
    assert len(s["title"]) <= 50, f"title too long ({len(s['title'])}): {s['title']}"
    assert "\u2014" not in s["brief"] + s["title"]
    v2 = md_to_v2(s["brief"]); assert not validate_v2(v2), validate_v2(v2)
    assert Path(s["guide"]).exists(), s["guide"]
    url = f"https://www.youtube.com/watch?v={vid}"
    if not APPLY:
        print(f"DRY {s['title']!r} ({len(s['title'])} chars) | {url} | brief {len(flatten_v2(v2))} chars | guide + {len(s['links'])} links")
        continue
    # re-read right before writing: another run may have added it since the check above
    if [l for c, l in classroom_videos().get(vid, []) if c == "YouTube Library"]:
        print(f"ALREADY IN COURSE (added since start), skipped: {vid}"); continue
    m = cls.create_module(ck, G, COURSE, s["title"], v2, state=2)
    fid = cls.upload_file(ck, s["guide"], G, content_type="application/pdf")
    res = [{"title": "Step-by-step guide (PDF)", "file_id": fid}] + [{"title": t, "link": u} for t, u in s["links"]]
    cls.update_unit(ck, m["id"], video_link=url, video_thumbnail=thumb(vid), resources=res)
    print("created", m["id"], s["title"])

if APPLY:
    print("\nCOURSE NOW:")
    for ch in client.get_course_modules(SLUG):
        u = cls.get_unit(ck, ch["course"]["id"])
        rs = u.get("resources"); rs = json.loads(rs) if isinstance(rs, str) else (rs or [])
        print(f"  {ch['course']['state']} {u.get('title')!r} | {u.get('video_link')} | brief {len(flatten_v2(u.get('desc') or ''))} | resources {[r.get('title') for r in rs]}")
