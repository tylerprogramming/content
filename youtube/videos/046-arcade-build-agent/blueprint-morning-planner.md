# Blueprint — The Morning Planner Agent

> An agent that reads your ClickUp tasks each morning and time-blocks your calendar around your meetings and work hours. It doesn't just tell you the plan — it **writes** it into your calendar. This is the "takes an action" upgrade over a draft-only agent, and a strong featured example for 046.

**Spec**
- **Agent:** Morning Planner
- **Runs:** daily, ~6:30am (before you sit down)
- **Stack:** Claude (Opus 4.8) + Arcade gateway (ClickUp + Google Calendar)
- **Host:** an always-on box — a Hostinger VPS — so it runs whether or not your laptop is open
- **Mode:** proposes → you approve → writes (safe by default)

## The flow (what happens each morning)

1. **Pull tasks** — reads today's due + high-priority open tasks from **ClickUp** (Arcade ClickUp tool).
2. **Read the day** — reads your **Google Calendar**: fixed meetings + your defined work hours (Arcade Calendar tool).
3. **Plan** — **Claude** fits the tasks into the open slots, around the meetings, by priority and rough duration. No double-booking, respects work hours.
4. **Write the blocks** — creates the time blocks on your calendar. *This is the action.* Writes to a separate "AI Plan" calendar (or as tentative) so it's easy to wipe until you trust it.
5. **Brief you** — drops the plan in Slack or email so it's waiting before the day starts.

## The stack (how it's wired)

- **Arcade gateway** — ClickUp + Google Calendar (+ optional Slack) behind one URL. Arcade holds the per-user OAuth; **no tokens in your code.**
- **Claude (Opus 4.8)** — does the planning: which task, which slot, how long.
- **A small script** — about a page of Python, the agent loop. The same Arcade tools work in your own code, not just Claude Code.
- **A schedule** — cron fires it every morning.

## Where it runs

- Local cron works, but your machine has to be on for it to fire.
- So it lives on a small always-on box (a **Hostinger VPS**) and runs every morning regardless. That is what makes "it ran before I sat down" actually true, not a demo claim.

## Keep it safe (it touches your real calendar)

- **Propose first.** It writes to a separate "AI Plan" calendar (or tentative events). You glance, you keep or clear. Promote to your main calendar once you trust it.
- **Arcade holds the auth**, and every run is logged, so you can see what it did.
- **Start narrow:** two tools, one job. Add the Slack/email brief once it has earned it.

## Make it yours

- Swap ClickUp for whatever task list you live in.
- Add a "protect deep work" rule (no task blocks before 11, or guard a focus window).
- Have it sweep unfinished blocks to tomorrow each evening.
- Add a Slack ping so the plan lands where you already look.

## Build it (high level)

1. Arcade → build a gateway with ClickUp + Google Calendar. Copy the URL.
2. Authorize once (ClickUp + Google consent screens). Arcade stores + refreshes the tokens.
3. Write the agent loop: pull tasks → read calendar → ask Claude to plan → create the blocks.
4. Put it on cron on the Hostinger VPS (~6:30am).
5. Run in propose-mode until you trust it, then let it write to your main calendar.

> ⚠️ **Fact-check before scripting the code** (shared with 046 Part 2 + 049): exact Arcade Python client usage, executing a Gateway tool from code with carried-over auth, the Claude call, and the ClickUp/Calendar tool signatures. Design so no keys/tokens ever appear on screen (env var, gitignored .env).

Built with Claude Code + Arcade. Blueprint by Tyler Reed (@TylerReedAI).
