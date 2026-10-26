#!/usr/bin/env python3
"""Put the written lesson bodies under the 5 YouTube Library video lessons (the-ai-agency).

usage: /opt/scripts/.venv/bin/python push_lesson_bodies.py bodies.json [--apply]
bodies.json: {"<lesson unit id>": "<markdown body>"}. Validates every [v2] body and
rejects em dashes before any write; reads each lesson back after writing.
"""
import json, os, sys
from pathlib import Path
os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api.endpoints import classroom as cls
from skool_api.richtext import md_to_v2, validate_v2, flatten_v2

P = Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json"
ck = {c["name"]: c["value"] for c in json.loads(P.read_text())}
bodies = json.loads(Path(sys.argv[1]).read_text())
APPLY = "--apply" in sys.argv

prepared = {}
for uid, md in bodies.items():
    assert "\u2014" not in md, f"em dash in {uid}"
    v2 = md_to_v2(md)
    errs = validate_v2(v2)
    assert not errs, (uid, errs)
    prepared[uid] = v2
    before = cls.get_unit(ck, uid)
    print(f"{uid} {before.get('title')!r}: {len(before.get('desc') or '')} -> {len(v2)} chars, video={before.get('video_link')}")

if not APPLY:
    print("[dry run] all bodies valid"); sys.exit()

for uid, v2 in prepared.items():
    cls.update_unit(ck, uid, desc=v2)
    back = cls.get_unit(ck, uid)
    flat = flatten_v2(back.get("desc") or "")
    ok = back.get("desc") == v2
    print(f"{'OK ' if ok else 'MISMATCH '}{back.get('title')!r} desc={len(back.get('desc') or '')} video={back.get('video_link')} | {flat[:90]!r}")
