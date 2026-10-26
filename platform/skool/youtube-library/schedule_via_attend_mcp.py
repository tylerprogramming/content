#!/usr/bin/env python3
"""Schedule the 5 YouTube Library posts through the Attend MCP server (real MCP stdio client).

Same server Hermes registered as `attend`: ssh -> /root/attend/mcp/server.py.
1. list current queue (scheduled_posts tool)
2. schedule_post x5 at 9am ET, label Discussion, email_members False
3. cancel_scheduled_post on the 5 matching drafts
usage: python schedule_via_attend_mcp.py [--apply]
"""
import asyncio, json, sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

APPLY = "--apply" in sys.argv
CMD = "cd /root/attend/mcp && set -a && . ./.env && set +a && exec /opt/scripts/.venv/bin/python server.py"
import os
ON_VPS = os.path.exists("/root/attend/mcp/server.py")
PARAMS = (StdioServerParameters(command="bash", args=["-c", CMD]) if ON_VPS
          else StdioServerParameters(command="ssh", args=["-o", "BatchMode=yes", "attend", CMD]))
COMMUNITY = "the-ai-agency"
# DST ends 2026-11-01: EDT (-04:00) before, EST (-05:00) after. 9am ET either way.
# Batches: pass --batch 2 for videos 6-10. Each batch = (video id -> ISO time with offset).
BATCHES = {
    "1": {"3xprBcuJKDA": "2026-10-27T09:00:00-04:00", "MzwYKfSxToU": "2026-10-28T09:00:00-04:00",
          "WvxPxQ_XlcQ": "2026-10-29T09:00:00-04:00", "uEUP4iHJO1Q": "2026-10-30T09:00:00-04:00",
          "1KsadAvYE8k": "2026-11-03T09:00:00-05:00"},
    "2": {"-dEeg0WnJxs": "2026-11-04T09:00:00-05:00", "GJQCUcx4roA": "2026-11-05T09:00:00-05:00",
          "cdvi2ooarDc": "2026-11-06T09:00:00-05:00", "J5lkE_jBEko": "2026-11-10T09:00:00-05:00",
          "WJabXRVe8JQ": "2026-11-11T09:00:00-05:00"},
}
WHEN = BATCHES[sys.argv[sys.argv.index("--batch") + 1] if "--batch" in sys.argv else "1"]
posts = [p for p in json.loads(Path(__file__).with_name("posts.json").read_text()) if p["video"] in WHEN]
assert len(posts) == len(WHEN), f"posts.json has {len(posts)} posts for {len(WHEN)} videos in this batch"
sys.path.insert(0, str(Path(__file__).parent))
from live_gate import require_live          # noqa: E402
from dup_gate import post_hits, BLOCKING_POST_STATUS   # noqa: E402
require_live(list(WHEN), Path(__file__).parent)   # no post about a video that isn't public on the channel

# DUPLICATE GUARD (by YouTube id in the post BODY, against live Attend + the live feed).
# One post per video, ever. A video that already has a scheduled/published/failed post, or that
# already appears in a feed post (including ones Tyler wrote by hand), gets no new post.
for p in posts:
    if p["video"] not in p["body"]:
        sys.exit(f"BLOCKED: post {p['title']!r} doesn't contain its video id {p['video']}; the dup guard can't track it.")
SKIP, DRAFTS = set(), {}
for p in posts:
    sched, feed = post_hits(p["video"])
    blocking = [x for x in sched if x["status"] in BLOCKING_POST_STATUS]
    if blocking or feed:
        why = blocking[0]["status"] + " " + blocking[0]["title"] if blocking else "already in the feed: " + feed[0]["title"]
        print(f"ALREADY POSTED, skipped: {p['video']} ({why})"); SKIP.add(p["video"])
    DRAFTS[p["video"]] = [x["id"] for x in sched if x["status"] == "draft"]


def data(res):
    sc = getattr(res, "structured_content", None)
    if isinstance(sc, dict) and set(sc) == {"result"}:
        return sc["result"]
    if sc is not None:
        return sc
    txt = "".join(c.text for c in res.content if getattr(c, "type", "") == "text")
    try:
        return json.loads(txt)
    except Exception:
        return txt


async def main():
    async with stdio_client(PARAMS) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = {t.name for t in (await s.list_tools()).tools}
            print("tools:", len(tools), "schedule_post" in tools, "cancel_scheduled_post" in tools)
            queue = data(await s.call_tool("scheduled_posts", {"community": COMMUNITY, "limit": 50}))
            print("queue now:", [(q["status"], q["publishes"], q["title"]) for q in queue])
            for p in posts:
                if p["video"] in SKIP:
                    continue
                args = {"title": p["title"], "body": p["body"], "when": WHEN[p["video"]],
                        "community": COMMUNITY, "label": "20a2b534818c404aaf9b682699f767e0", "email_members": False}
                if not APPLY:
                    pv = data(await s.call_tool("preview_post", {k: args[k] for k in ("title", "body", "community")} | {"label": "20a2b534818c404aaf9b682699f767e0"}))
                    print("DRY", WHEN[p["video"]], p["title"], "->", {k: pv.get(k) for k in ("would_reach", "category", "characters")} if isinstance(pv, dict) else pv)
                    continue
                # re-check right before writing: another run may have scheduled it since start
                if [x for x in post_hits(p["video"])[0] if x["status"] in BLOCKING_POST_STATUS]:
                    print("ALREADY POSTED (since start), skipped:", p["video"]); continue
                print("schedule_post:", data(await s.call_tool("schedule_post", args)))
                for pid in DRAFTS.get(p["video"], []):
                    print("cancel draft:", data(await s.call_tool("cancel_scheduled_post", {"post_id": pid, "community": COMMUNITY})))
            if APPLY:
                after = data(await s.call_tool("scheduled_posts", {"community": COMMUNITY, "limit": 50}))
                print("queue after:")
                for q in after:
                    print(" ", q["status"], q["publishes"], q["category"], q["title"], "| problem:", q["problem"])

asyncio.run(main())
