#!/usr/bin/env python3
"""Make each YouTube Library lesson brief: short desc + resources (guide PDF + key links).

usage (on the box, from a dir holding briefs json + the guide PDFs):
  /opt/scripts/.venv/bin/python apply_briefs.py briefs-01-05.json [--apply]
Backs up each lesson's current desc/resources to backup-<uid>.json first.
"""
import json, os, sys
from pathlib import Path
os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api.endpoints import classroom as cls
from skool_api.richtext import md_to_v2, validate_v2, flatten_v2

G = "291a78f5b31f45a7982cc512bae3c9df"
ck = {c["name"]: c["value"] for c in json.loads((Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json").read_text())}
spec = json.loads(Path(sys.argv[1]).read_text())
APPLY = "--apply" in sys.argv

for uid, s in spec.items():
    assert "\u2014" not in s["brief"]
    v2 = md_to_v2(s["brief"]); assert not validate_v2(v2), validate_v2(v2)
    assert Path(s["guide"]).exists(), s["guide"]
    cur = cls.get_unit(ck, uid)
    print(f"{cur.get('title')!r}: desc {len(cur.get('desc') or '')} -> {len(v2)} chars; resources -> guide + {len(s['links'])} links")
    if not APPLY:
        continue
    Path(f"backup-{uid}.json").write_text(json.dumps(cur))
    fid = cls.upload_file(ck, s["guide"], G, content_type="application/pdf")
    res = [{"title": "Step-by-step guide (PDF)", "file_id": fid}] + [{"title": t, "link": u} for t, u in s["links"]]
    cls.update_unit(ck, uid, desc=v2, resources=res)
    back = cls.get_unit(ck, uid)
    rs = back.get("resources")
    rs = json.loads(rs) if isinstance(rs, str) else (rs or [])
    print("   OK" if flatten_v2(back.get("desc") or "") == flatten_v2(v2) else "   DESC MISMATCH",
          "| video", back.get("video_link"), "| resources:", [(r.get("title"), r.get("file_name") or r.get("link")) for r in rs])
if not APPLY:
    print("[dry run]")
