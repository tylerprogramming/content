#!/usr/bin/env python3
"""Load YouTube Library posts into Attend as DRAFTS for the-ai-agency.

usage: /opt/scripts/.venv/bin/python load_posts.py posts.json [--dry-run]
Drafts are never published by attend-posts (it only sends status='scheduled'); Tyler
approves each one on the Attend posts calendar. Idempotent: skips a title that already
exists for this community in draft/scheduled/published.
"""
import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, "/root/attend/worker")
import db  # noqa: E402

COMMUNITY = "d00bf9c7-41b7-43de-bceb-980917b9528b"   # the-ai-agency
CUSTOMER = "f769d47f-b4d4-4171-903a-e6a429ba3872"
LABEL = "20a2b534818c404aaf9b682699f767e0"           # 💬 Discussion (community default)
BATCH = "youtube-library-2026-10"
TZ = ZoneInfo("America/New_York")

posts = json.load(open(sys.argv[1]))
dry = "--dry-run" in sys.argv
existing = {r["title"] for r in db.select("scheduled_posts", select="title",
            community_id=f"eq.{COMMUNITY}", status="in.(draft,scheduled,published)")}

rows = []
for p in posts:
    if p["title"] in existing:
        print("skip (exists):", p["title"])
        continue
    when = datetime.fromisoformat(p["date"] + "T09:00:00").replace(tzinfo=TZ)
    rows.append({
        "customer_id": CUSTOMER, "community_id": COMMUNITY,
        "title": p["title"], "body": p["body"], "label_id": LABEL,
        "scheduled_for": when.isoformat(), "status": "draft",
        "email_members": False, "media": [], "plan_batch": BATCH,
    })
for r in rows:
    print(("DRY " if dry else "") + f"{r['scheduled_for'][:16]}  {r['title']}  ({len(r['body'])} chars)")
if rows and not dry:
    out = db.insert("scheduled_posts", rows)
    print("inserted", len(out) if isinstance(out, list) else out)
