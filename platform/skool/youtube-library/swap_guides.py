#!/usr/bin/env python3
"""Replace the guide PDF on existing lessons, keeping their links. usage: swap_guides.py map.json [--apply]
map.json: {"<lesson unit id>": "<guide.pdf>"}"""
import json, os, sys
from pathlib import Path
os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api.endpoints import classroom as cls
G = "291a78f5b31f45a7982cc512bae3c9df"
ck = {c["name"]: c["value"] for c in json.loads((Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json").read_text())}
for uid, pdf in json.loads(Path(sys.argv[1]).read_text()).items():
    u = cls.get_unit(ck, uid)
    rs = u.get("resources"); rs = json.loads(rs) if isinstance(rs, str) else (rs or [])
    links = [{"title": r["title"], "link": r["link"]} for r in rs if r.get("link")]
    print(u.get("title"), "| keeps", len(links), "links")
    if "--apply" not in sys.argv:
        continue
    fid = cls.upload_file(ck, pdf, G, content_type="application/pdf")
    cls.update_unit(ck, uid, resources=[{"title": "Step-by-step guide (PDF)", "file_id": fid}] + links)
    back = cls.get_unit(ck, uid).get("resources"); back = json.loads(back) if isinstance(back, str) else back
    print("   now:", [(r.get("title"), r.get("file_id", "")[:8] or r.get("link")) for r in back])
