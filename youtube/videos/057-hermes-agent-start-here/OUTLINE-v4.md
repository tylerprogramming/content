# 057 Outline v4 (30 min course) — drafted 2026-09-14

Supersedes the v3 13-min script structure. Built from `STATE.md`, `analysis.md`, the Tina breakdown, and what is actually running on the Mac Studio tonight. Approve or edit this table before anything else gets written.

**Title (pick one before filming; working title breaks rule #2):**
1. Set Up Hermes Agent in 30 Minutes (Claude Code Users Start Here)
2. How to Run an AI Agent That Never Forgets (Hermes Setup)
3. Turn Any Computer Into a 24/7 AI Agent (Hermes)

**Spine:** Tina's order, half the explainer, and it ends on three named bots shipping a real PR and pinging Slack. She ends on a Pomodoro widget in Discord.

**Rule for every section:** viewer copy-paste steps (COMPANION.md) + live demo with expected output written down + one line of why.

## Section table

| # | Section | Time | Viewer instruction | Live demo (verified state) |
|---|---|---|---|---|
| 0 | Cold open: proof | 0:00-0:40 | none | Phone: this morning's Attend card (8am, `ok` 09-14) and Coder's verdict card in Slack. Desktop Bots tab: Coder, Researcher, Packager. No camera until 0:25. |
| 1 | What it is, why both | 0:40-2:00 | none | Diagram: CC = session you open / Hermes = process that stays running. Three things a session tool cannot do: remembers, runs while you are away, reaches your phone. Say the one cost: host must be awake. |
| 2 | Host | 2:00-2:30 | pick a machine that stays on | "Mac Studio, on all day. Laptop works, VPS works." No hardware tour. |
| 3 | Install + first hi | 2:30-5:00 | desktop download, or the curl one-liner; pick a model | FRESH instance. Composer model picker, Nous Portal key, `hi`. Filler while it installs: same install on a VPS. |
| 4 | Memory tier 1 | 5:00-8:30 | tell it about yourself, then open the files | FRESH: paste the about-me line (channel name, CC daily, no em dashes). Then `Given what you now know about me, what would you not bother explaining to me?` Open `~/.hermes/memories/` in Finder: USER.md, MEMORY.md (two files, verified tonight). Edit a line live. Contrast with ChatGPT memory you cannot open. |
| 5 | Memory tier 2 + the caps | 8:30-11:30 | none, it is on by default | CUT TO MATURE, say the seam. New session: `Based on everything you know about how I work, draft the outline for my next video. Don't ask me any questions first.` Show it reading status.md + the package, returning a numbered section table. Then the "oh, that is why" beat: caps 2,200 / 1,375 chars because tier 1 loads every session; tier 2 is searched on demand. Context meter showing memory's share. |
| 6 | Memory controls | 11:30-13:30 | two config lines, no accounts | `hermes config set memory.write_approval true` → `/memory pending`. `hermes config get auxiliary.background_review` → enabled, ollama-launch, gemma4:e4b (verified tonight): background review runs on a free local model. Honcho/Obsidian named in one line, not built. |
| 7 | Skills | 13:30-17:00 | run a task, then "make this a skill" | Capabilities → Skills. Past chat (title-check on last 10 uploads) → `Make this into a skill for checking my titles.` → open SKILL.md → new chat `/title-check`. Then the CC-user beat: `claude-to-hermes-skill-porting`, port one yt-skill from `~/.claude/skills` live. Honest line: four jarvis skills for one project, "it drifts, curate." |
| 8 | Cron | 17:00-20:30 | one job, plain English, deliver to a chat app | Routines pane: Attend 8am and YouTube 9pm with weeks of `ok`. Then `hermes -p coder cron run "coder: morning repo check"` → Slack card lands (last run `ok` 09-14 21:05). Three parts of a job: schedule, prompt, delivery. Gotchas: fresh session per run, pre-flight check. Keys via `hermes config set`, never the chat. |
| 9 | Local and free | 20:30-23:00 | Ollama, tool-capable model, context length | Settings → Providers → Local Models, or `ollama launch hermes`. Point at `qwen3.8:27b-q8_0`. Tool test offline: list files, read README, name the project. "The background review you saw earlier was already local." |
| 10 | Bots: the payoff | 23:00-29:00 | `hermes profile create`, a SOUL.md, describe it | Create a 4th bot from nothing on camera (delete the pre-built one first). Roster shows avatars + descriptions. Then in Researcher's Bot Chat: `@packager build the package for video 058 from the research you have. When it's done, @coder opens a PR on tylerprogramming/content and posts the link to Slack.` Three surfaces: Bots tab handoff → GitHub PR → Slack ping on the phone. Say the limit out loud: desktop is where you talk to a bot, Slack is where bots talk to you (`@coder` in Slack needs its own app). |
| 11 | Where it fits + CTA | 29:00-30:00 | none | "I run both. Claude Code is the specialist in the repo. This never closes." Pay off the cold open: everything you saw is what ran this morning, not a demo. Companion doc in the free community, one link. |

## Changes from v3 you need to know about

1. Section 5's "outline" demo is real now: this outline is the artifact. Screenshot the session before it scrolls off.
2. Roster is 3 bots, not 2. `packager` (skill `yt-package`) exists and STATE.md does not list it. Fix STATE.md before the Researcher bot answers questions from it.
3. Local model in STATE.md is `qwen3.8:latest`; the installed tags are `qwen3.8:27b-q8_0` and `gemma4:e4b`. Script must use the real tag.
4. v3's Telegram montage (7am brief, comment drafts, competitor watch) is gone. Those crons do not exist. The cold open uses the Slack cards that actually fired.
5. Section 10 handoff: `message_agent` reply landing is still "sent, not eyeballed" in STATE.md. Verify the PR and the Slack ping land end to end before this beat goes in the script. If it does not land, the ending is Coder's live PR review posting to Slack (verified), and the three-bot chain is cut, not faked.
6. Pokemon and Jarvis stay out. Jarvis survives only as the one-line curation beat in section 7.

## Deliverables after approval

`script.md` v4, `SHOTLIST.md` v4, `COMPANION.md`, `FILMING-CARD.md`, `STATE.md` refresh. Then ClickUp `86e31d3j9` comment + status.md row + commit.
