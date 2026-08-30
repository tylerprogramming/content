# 053 - How we build the agents (the tech, on screen)

The whole video rests on one true, simple claim: **an agent = an instruction file + a set of
tools.** In Claude Code that maps to two real things:

- **The instruction file** = a Claude Code **Agent Skill** (`SKILL.md` in a folder) or a **slash
  command** (`.claude/commands/name.md`). Plain markdown. Says the job in English.
- **The tools** = **MCP servers** for the apps (Gmail, Google Calendar, ClickUp). Connected once
  with `claude mcp add`. This is the exact "connect your apps" layer from the Arcade video (045) -
  we reuse it, we do not re-explain it.

Nothing here is new for Tyler: these are his real skills, his real MCP connections, and his real
JARVIS scheduling. The video shows how they are made, it does not stage them.

## The stack (name it once, plainly)
| Layer | What it is | On screen |
|---|---|---|
| Instructions | a `SKILL.md` / slash-command markdown file | write it live, ~15-20 lines |
| Tools | MCP servers: Gmail, Google Calendar, ClickUp | `claude mcp add ...`, then `/mcp` shows connected |
| Memory / voice | a `CLAUDE.md` or style file the agent reads | the content agent uses it to sound like Tyler |
| Autopilot | cron / a scheduled routine that runs the command | the briefing fires at 6am |
| A team | Claude Code subagents (background Task) | one goes to research while the main keeps working |

## Per-agent build

**1. Morning briefing** - skill that calls Gmail (read last 24h) + Google Calendar (today) +
ClickUp (open tasks), then writes a 3-part briefing to a file. Runs on a **cron/routine at 6am**.
(This is essentially Tyler's real JARVIS morning agent - show the actual one.)

**2. Inbox triage** - skill that reads Gmail, applies four labels (Action/Waiting/FYI/Promo), and
**drafts** replies to the Action ones. Technical honesty beat: the **Gmail connector is draft-only** -
it creates drafts, it cannot send. That is the "on a leash" agent, and the limit is real, not a choice.

**3. Content pipeline** - skill that edits `status.md` (filesystem), moves the matching **ClickUp**
task (MCP), and drafts social copy using the **voice/style file**. Pure ops, chained in one run.

**4. Calendar** - skill that queries **Google Calendar** for a free block and creates the event in
the right timezone. Smallest agent, one tool.

**Subagent pattern** - from the main agent, spawn a **background subagent** (Claude Code Task) to go
research a topic and return only the report, while the main agent keeps working. Show both windows.

## The one-time setup we show (fast, not a tutorial detour)
1. `claude mcp add` the three apps (Gmail, Calendar, ClickUp) - or point at the Arcade gateway from 045.
2. `/mcp` to confirm they are connected and authorized.
Then every agent is just a markdown file that is allowed to use those tools.

## Scheduling (the autopilot piece)
- Simplest on-camera version: a **cron** entry (or a `launchd` job on the Mac) that runs the briefing
  command each morning.
- Or a **Claude routine** (claude.ai/code/routines) for the hosted version.
- Honest limit to state: schedules run **on a clock, not on events** - no real-time triggers yet.

## Why this reuses everything Tyler already has
- MCP app-connection = the Arcade 045 material.
- Skills = his existing `~/.claude/skills/` library (yt-*, transcribe, etc.).
- Scheduled agents writing reports to disk = JARVIS, already running daily.
So the build is real end to end, and the "steal my setup" folder at the end is literally these files.
