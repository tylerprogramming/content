"""Shared gate used by add_lessons.py and schedule_via_attend_mcp.py (both run on the box).

The YouTube token lives on the Mac, so the live check runs there first:
    python check_public.py --json <ids...> > public_check.json
and that file travels to the box with the script. This module refuses any video that is
not marked live in it, and refuses a stale file (older than MAX_AGE_MIN), so a video that
was public yesterday but got set private today can't slip through on an old check.
"""
import json, os, sys, time
from pathlib import Path

MAX_AGE_MIN = 60


def require_live(video_ids, here: Path):
    f = here / "public_check.json"
    if not f.exists():
        sys.exit("BLOCKED: no public_check.json. Run check_public.py --json on the Mac first.")
    age = (time.time() - f.stat().st_mtime) / 60
    if age > MAX_AGE_MIN:
        sys.exit(f"BLOCKED: public_check.json is {age:.0f} min old (max {MAX_AGE_MIN}). Re-run check_public.py.")
    res = {r["id"]: r for r in json.loads(f.read_text())}
    bad = [(v, res.get(v, {}).get("why", "not checked")) for v in video_ids if not res.get(v, {}).get("live")]
    if bad:
        for v, why in bad:
            print(f"BLOCKED {v}: {why}")
        sys.exit("Not live on the channel yet: no lesson, no post. Nothing was written.")
    print(f"live check ok: {len(video_ids)} video(s) public on the channel ({age:.0f} min old)")
