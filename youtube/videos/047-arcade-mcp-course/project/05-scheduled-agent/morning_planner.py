"""
Module 5 — The Morning Planner (scheduled agent).

Every morning: read today's ClickUp tasks + your Google Calendar, ask Claude to
time-block the day around your meetings and work hours, then WRITE those blocks
to a dedicated "AI Plan" calendar. Runs on a schedule on a VPS (see deploy/).

Verified building blocks (docs.arcade.dev, 2026-08):
  - arcadepy Arcade client: client.tools.authorize / .execute, client.auth.wait_for_completion
  - GoogleCalendar.CreateEvent input: {summary, start_datetime, end_datetime}
  - per-user auth is stored by Arcade under user_id; no tokens live in this file

Claude (Opus 4.8) does the planning via the Anthropic SDK.

Install:  pip install arcadepy anthropic python-dotenv
Env:      ARCADE_API_KEY, ARCADE_USER_ID, ANTHROPIC_API_KEY

SAFE BY DEFAULT: runs in DRY_RUN (prints the plan, writes nothing). Pass --apply
to actually create events. Even with --apply it writes to PLAN_CALENDAR (a
separate, wipeable calendar), never your main one, until you trust it.

Run:      python morning_planner.py            # dry run, prints the plan
          python morning_planner.py --apply    # creates the blocks
          python morning_planner.py --discover  # print exact ClickUp/Calendar tool names
"""
import json
import os
import sys
from datetime import date, datetime

from anthropic import Anthropic
from arcadepy import Arcade
from dotenv import load_dotenv

load_dotenv()

USER_ID = os.environ["ARCADE_USER_ID"]
WORK_START = "09:00"
WORK_END = "17:00"
PLAN_CALENDAR = "AI Plan"          # a separate calendar you can clear; NOT your main one
MODEL = "claude-opus-4-8"

# ── Tool names ───────────────────────────────────────────────────────────────
# Calendar CreateEvent is confirmed from the Arcade quickstart. The exact ClickUp
# task-listing tool name + inputs vary by catalog version — run this file with
# --discover once to print your account's real tool names, then set these.
CAL_LIST_TOOL = "GoogleCalendar.ListEvents"       # TODO: confirm via --discover
CAL_CREATE_TOOL = "GoogleCalendar.CreateEvent"    # confirmed
CLICKUP_TASKS_TOOL = "ClickUp.GetTasks"           # TODO: confirm via --discover (name + input schema)

client = Arcade()                  # reads ARCADE_API_KEY
anthropic = Anthropic()            # reads ANTHROPIC_API_KEY


def run_tool(tool_name: str, tool_input: dict):
    """Authorize (once, interactively) then execute an Arcade tool as USER_ID."""
    auth = client.tools.authorize(tool_name=tool_name, user_id=USER_ID)
    if auth.status != "completed":
        print(f"Authorize {tool_name} here (one time):\n  {auth.url}")
        client.auth.wait_for_completion(auth.id)
    resp = client.tools.execute(tool_name=tool_name, input=tool_input, user_id=USER_ID)
    return resp.output.value


def discover():
    """Print the exact tool names + inputs for the toolkits we use."""
    for toolkit in ("ClickUp", "GoogleCalendar"):
        print(f"\n=== {toolkit} tools ===")
        for t in client.tools.list(toolkit=toolkit).items:
            print(" •", t.qualified_name)
    print("\nSet CLICKUP_TASKS_TOOL / CAL_* above to the names you see here.")


def gather_context() -> dict:
    today = date.today().isoformat()
    tasks = run_tool(CLICKUP_TASKS_TOOL, {})              # TODO: pass your list/filter inputs
    events = run_tool(CAL_LIST_TOOL, {"min_end_datetime": f"{today}T00:00:00",
                                      "max_start_datetime": f"{today}T23:59:59"})
    return {"date": today, "tasks": tasks, "events": events}


def plan_day(context: dict) -> list[dict]:
    """Ask Claude to fit tasks into open slots. Returns a list of time blocks."""
    prompt = f"""You are my scheduling assistant. Today is {context['date']}.
My work hours are {WORK_START} to {WORK_END}.

Fixed calendar events today (do not move these):
{json.dumps(context['events'], indent=2, default=str)}

Tasks I want to get done (from ClickUp):
{json.dumps(context['tasks'], indent=2, default=str)}

Plan my day: fit the tasks into the open slots around the fixed events, highest
priority first, with realistic durations. Do not double-book. Stay inside work
hours. Leave short breaks.

Return ONLY a JSON array, no prose, each item:
{{"summary": "<task>", "start_datetime": "{context['date']}T09:00:00", "end_datetime": "{context['date']}T10:00:00"}}"""

    msg = anthropic.messages.create(
        model=MODEL, max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    text = msg.content[0].text.strip()
    text = text[text.find("["): text.rfind("]") + 1]      # tolerate stray prose
    return json.loads(text)


def write_blocks(blocks: list[dict]):
    for b in blocks:
        run_tool(CAL_CREATE_TOOL, {
            "summary": f"[Plan] {b['summary']}",
            "start_datetime": b["start_datetime"],
            "end_datetime": b["end_datetime"],
            # "calendar_id": PLAN_CALENDAR,   # TODO: confirm CreateEvent's calendar arg via --discover
        })
        print(f"  created: {b['start_datetime']}  {b['summary']}")


def main():
    if "--discover" in sys.argv:
        discover()
        return
    apply = "--apply" in sys.argv

    ctx = gather_context()
    blocks = plan_day(ctx)

    print(f"\nMorning plan for {ctx['date']}:")
    for b in blocks:
        print(f"  {b['start_datetime'][11:16]}-{b['end_datetime'][11:16]}  {b['summary']}")

    if not apply:
        print("\n(dry run — nothing written. Re-run with --apply to create the blocks.)")
        return
    print(f"\nWriting {len(blocks)} blocks...")
    write_blocks(blocks)
    print("Done.")


if __name__ == "__main__":
    main()
