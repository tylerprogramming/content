#!/usr/bin/env python3
"""READ-ONLY classroom audit dump for the-ai-agency. Writes /tmp/aiagency-classroom-raw.json."""
import json, sys
from pathlib import Path
from skool_api import SkoolClient
sys.path.insert(0, str(Path.home() / ".claude/skills/skool-shared/lib"))
from env import load_env

env = load_env()
name = env["SKOOL_NAME"]
c = SkoolClient(cookies_path=str(Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json"),
                group_slug=name, group_uuid=env.get("SKOOL_GROUP_ID", ""))
out = []
for rc in c.get_courses():
    slug = rc.get("name")
    entry = {"course": rc, "children": []}
    if slug:
        try:
            entry["children"] = c.get_course_modules(slug)
        except Exception as e:
            entry["error"] = repr(e)
    out.append(entry)
    print(rc.get("metadata", {}).get("title"), len(entry["children"]), file=sys.stderr)
Path("/tmp/aiagency-classroom-raw.json").write_text(json.dumps(out, ensure_ascii=False))
print("ok", len(out))
