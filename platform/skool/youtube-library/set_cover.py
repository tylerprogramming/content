#!/usr/bin/env python3
"""Upload a cover PNG and set it on a course (and optionally the course desc). Verifies via get_courses."""
import json, os, sys, requests
from pathlib import Path
os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api import SkoolClient
from skool_api._http import API2, headers
from skool_api.endpoints import classroom as cls

G = "291a78f5b31f45a7982cc512bae3c9df"
COURSE = "31b0709529e1440ea64abf80d6621741"
P = str(Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json")
ck = {c["name"]: c["value"] for c in json.loads(Path(P).read_text())}
png, desc = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)

file_id, url = cls.upload_file(ck, png, G, file_name="youtube-library-cover.png", content_type="image/png", inline_image=True)
print("uploaded", file_id, url)
cls.update_unit(ck, COURSE, cover_image=url, cover_image_file=file_id)
if desc:
    r = requests.put(f"{API2}/courses/{COURSE}", cookies=ck, headers=headers("/-/classroom"), json={"desc": desc}, timeout=30)
    print("desc PUT", r.status_code)
c = SkoolClient(cookies_path=P, group_slug="the-ai-agency", group_uuid=G)
x = next(x for x in c.get_courses() if x["id"] == COURSE)
m = x["metadata"]
print("state", x["state"], "| title", m.get("title"), "| desc", m.get("desc"), "| cover", m.get("coverImage"), "| file", m.get("coverImageFile"))
print("HEAD cover", requests.head(m.get("coverImage") or "", timeout=20).status_code if m.get("coverImage") else None)
