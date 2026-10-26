#!/usr/bin/env python3
"""Create the YouTube Library course (DRAFT) in the-ai-agency with 5 video-link lessons.

usage: /opt/scripts/.venv/bin/python create_youtube_library.py [--dry-run]
Idempotent: if a course with TITLE already exists it is reused and existing lesson
titles are skipped. Course is created with state=1 (draft); Tyler publishes in the UI.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
from skool_api import SkoolClient                      # noqa: E402
from skool_api.endpoints import classroom as cls       # noqa: E402
from skool_api.richtext import md_to_v2                # noqa: E402

GROUP_ID = "291a78f5b31f45a7982cc512bae3c9df"
COOKIES = str(Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json")
TITLE = "YouTube Library"
DESC = "Every YouTube video in one place."
VIDEOS = [  # newest first = creation order. Skool lesson titles: max 50 chars (422 "Title is too long")
    ("MzwYKfSxToU", "Set Up Hermes Agent in 30 Minutes"),
    ("3xprBcuJKDA", "DeepSeek Harness: Full Setup"),
    ("WvxPxQ_XlcQ", "Build an AI Agent in 5 Steps (Claude Code)"),
    ("1KsadAvYE8k", "Give Claude the Keys to Every App You Own"),
    ("uEUP4iHJO1Q", "Claude Code + MCP for Non-Technical Beginners"),
]
assert all(len(t) <= 50 for _, t in VIDEOS)
DRY = "--dry-run" in sys.argv


def thumb(vid):
    for q in ("maxresdefault", "hqdefault"):
        u = f"https://img.youtube.com/vi/{vid}/{q}.jpg"
        try:
            with urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=10) as r:
                if r.status == 200:
                    return u
        except Exception:
            pass
    return f"https://img.youtube.com/vi/{VIDEOS[0][0]}/hqdefault.jpg"


client = SkoolClient(cookies_path=COOKIES, group_slug="the-ai-agency", group_uuid=GROUP_ID)
cookies = {c["name"]: c["value"] for c in json.loads(Path(COOKIES).read_text())}

existing = next((c for c in client.get_courses() if (c.get("metadata") or {}).get("title") == TITLE), None)
if existing:
    course_id = existing["id"]
    print(f"course exists: {course_id} state={existing.get('state')}")
    have = {(ch.get("course", {}).get("metadata") or {}).get("title") for ch in client.get_course_modules(existing["name"])}
elif DRY:
    course_id, have = "(new)", set()
    print(f"DRY would create course {TITLE!r} state=1 (draft), desc={DESC!r}")
else:
    r = cls.create_course(cookies, GROUP_ID, TITLE, desc=DESC, state=1)
    course_id = r["id"]
    have = set()
    print(f"created course {course_id} state={r.get('state')} name={r.get('name')}")

for vid, title in VIDEOS:
    url = f"https://www.youtube.com/watch?v={vid}"
    if title in have:
        print(f"skip (exists): {title}")
        continue
    th = thumb(vid)
    if DRY:
        print(f"DRY lesson: {title} | {url} | {th}")
        continue
    m = cls.create_module(cookies, GROUP_ID, course_id, title, md_to_v2(url), state=2)
    cls.update_unit(cookies, m["id"], video_link=url, video_thumbnail=th)
    back = cls.get_unit(cookies, m["id"])
    print(f"lesson {m['id']}: {title} | video_link={back.get('video_link') or back.get('videoLink')}")

print("course_id", course_id)
