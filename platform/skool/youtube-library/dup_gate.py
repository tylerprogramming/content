#!/usr/bin/env python3
"""Duplicate guard for the YouTube Library (runs ON the box, reads live state every time).

A video is a DUPLICATE if its YouTube id already appears in:
  - a lesson in the YouTube Library course            -> no new lesson
  - an Attend post that is scheduled/published/failed -> no new post
  - a post already in The AI Agency feed (community_posts, includes posts Tyler wrote by hand)
Drafts that mention the video are not duplicates; they get cancelled when the real post is scheduled.
Lessons for the same video in OTHER courses are reported as a warning only (the Library is the archive).

CLI (preflight, read-only):  /opt/scripts/.venv/bin/python dup_gate.py <id-or-url> [...]
  exit 0 = nothing exists yet for any of them; exit 1 = at least one is already there.
"""
import json, os, re, sys
from pathlib import Path

os.environ.setdefault("SKOOL_NAME", "the-ai-agency")
sys.path.insert(0, "/root/attend/worker")

GROUP = "291a78f5b31f45a7982cc512bae3c9df"
LIBRARY_SLUG = "d8e99302"
COMMUNITY = "d00bf9c7-41b7-43de-bceb-980917b9528b"
COOKIES = str(Path.home() / ".claude/skills/skool-shared/data/skool_cookies.json")
BLOCKING_POST_STATUS = ("scheduled", "published", "failed")
_ID = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([\w-]{11})")


def video_id(s: str) -> str | None:
    if not s:
        return None
    m = _ID.search(s)
    if m:
        return m.group(1)
    s = s.strip()
    return s if re.fullmatch(r"[\w-]{11}", s) else None


def _walk(nodes, course_title, out):
    for ch in nodes or []:
        node = ch.get("course", ch)
        md = node.get("metadata") or {}
        vid = video_id(md.get("videoLink") or md.get("video_link") or "")
        if vid:
            out.setdefault(vid, []).append((course_title, md.get("title")))
        _walk(ch.get("children"), course_title, out)


def classroom_videos():
    """{video_id: [(course title, lesson title), ...]} across EVERY course in the group."""
    from skool_api import SkoolClient
    c = SkoolClient(cookies_path=COOKIES, group_slug="the-ai-agency", group_uuid=GROUP)
    out = {}
    for course in c.get_courses():
        title = (course.get("metadata") or {}).get("title")
        _walk(c.get_course_modules(course["name"]), title, out)
    return out


def library_titles():
    from skool_api import SkoolClient
    c = SkoolClient(cookies_path=COOKIES, group_slug="the-ai-agency", group_uuid=GROUP)
    return {(ch["course"].get("metadata") or {}).get("title") for ch in c.get_course_modules(LIBRARY_SLUG)}


def post_hits(vid: str):
    """Attend posts (any status) and feed posts that mention this video id."""
    import db
    sched = db.select("scheduled_posts", select="id,title,status,scheduled_for",
                      community_id=f"eq.{COMMUNITY}", body=f"ilike.*{vid}*")
    feed = db.select("community_posts", select="title,posted_at,url",
                     community_id=f"eq.{COMMUNITY}", body=f"ilike.*{vid}*")
    return sched, feed


def report(ids):
    """Per video: in_library, other_courses, blocking posts, drafts, feed posts."""
    lessons = classroom_videos()
    rows = []
    for vid in ids:
        where = lessons.get(vid, [])
        sched, feed = post_hits(vid)
        rows.append({
            "id": vid,
            "in_library": [l for c, l in where if c == "YouTube Library"],
            "other_courses": [f"{c} > {l}" for c, l in where if c != "YouTube Library"],
            "posts_blocking": [(p["status"], p["scheduled_for"][:16], p["title"]) for p in sched if p["status"] in BLOCKING_POST_STATUS],
            "drafts": [(p["id"], p["title"]) for p in sched if p["status"] == "draft"],
            "feed": [(p["title"], (p.get("posted_at") or "")[:10]) for p in feed],
        })
    return rows


def lesson_exists(vid: str, lessons=None):
    lessons = classroom_videos() if lessons is None else lessons
    return [l for c, l in lessons.get(vid, []) if c == "YouTube Library"]


if __name__ == "__main__":
    ids = [video_id(a) for a in sys.argv[1:]]
    if not ids or None in ids:
        sys.exit(__doc__)
    dup = False
    for r in report(ids):
        exists = bool(r["in_library"] or r["posts_blocking"] or r["feed"])
        dup |= exists
        print(("ALREADY THERE " if exists else "NEW           ") + r["id"])
        for k in ("in_library", "posts_blocking", "feed", "drafts", "other_courses"):
            if r[k]:
                print(f"    {k}: {r[k]}")
    sys.exit(1 if dup else 0)
