# Creator Breakdown: Tina Huang, "Hermes Agent Fundamentals In 29 Minutes"

- **Video:** https://youtube.com/watch?v=5_N84t1rUU0 (313,962 views, 29:40, uploaded 2026-07-20)
- **Transcript:** `~/content/transcripts/transcript_5_N84t1rUU0.txt`
- **Broken down:** 2026-09-12, for video 057
- **Her setup at filming:** Mac Studio M4 64GB on 24/7; local Qwen 3.6 35B via llama.cpp; Discord as the multi-agent surface; Obsidian as the memory viewer/vault

## Her structure

| # | Beat | Time | What she does on screen |
|---|---|---|---|
| 1 | Hook | 0:00-0:44 | Shows her multi-agent Discord + Obsidian second brain already running. "Setting it up right is the difference." Outline of the video. |
| 2 | Hardware | 0:44-2:55 | Four options: dedicated local (Mac Studio), VPS ($5-6), old laptop, personal PC + Docker. Links prior videos, does not go deep. |
| 3 | Install | 2:55-4:30 | **Desktop app, not terminal** (she says most tutorials go terminal, so she does the app). Model picker, Add provider, promises local later. |
| 4 | First hi | 4:27 | Says hi. "Your first interaction." |
| 5 | Tell it about yourself | 5:16-5:58 | Asks Claude to write her bio, pastes it, "please remember this." Points at *running memory*. |
| 6 | Where memory lives | 5:58-7:12 | **Cuts to her mature Mac Studio and says so.** Finder → `~/.hermes` → opens in Obsidian → `user.md`, `memory.md`. "Human readable." |
| 7 | Settings tour | 7:12-7:38 | Quick scroll: model, personalities, appearance, workspace, safety, memory. "I leave it default." |
| 8 | Tools | 7:38-9:25 | Skills-and-tools panel → Tools tab. Live task: "search the web for latest AI chip developments." |
| 9 | Messaging | 9:25-10:21 | "Help me connect to Telegram." Shows the messaging pane. |
| 10 | MCP | 10:21-11:13 | "Help me connect to the Notebook LM MCP." Names it, skips the detail, "maybe a next video." |
| 11 | Skills | 11:13-14:19 | Shows a **past** chat (business idea research + scoring) → "make this into a skill for evaluating business ideas" → shows the SKILL.md description + how-to-use → new chat `/business-idea-evaluator` on a fresh idea → 9.2/10 → saves to Obsidian via the obsidian skill. |
| 12 | Cron | 14:19-15:56 | Her 11pm daily brief. "Recurring things in life." |
| 13 | Memory deep dive | 15:56-18:35 | Tier 1 files, tier 2 session search. Demo: new session, "Remind me, what were we talking about earlier about business ideas?" → session_search tool → recall. |
| 14 | Memory tiers 3-4 | 18:35-23:03 | Honcho (external user-modeling plugin, paid credits, `hermes honcho status`), then Obsidian vault as project memory. ~4.5 min. |
| 15 | Local models | 23:03-25:40 | "Everything you just saw was local." Ollama launch tab has Hermes. Prefers llama.cpp for control + speed, 30 min setup with Hermes helping. |
| 16 | **Payoff: multi-agent Discord** | 25:40-29:40 | `@Hermes draft the spec for a Pomodoro app that saves to Obsidian` → PRD → "queue it" → build lands in #builds → runs the app → Obsidian shows the entry. Then two more `@Hermes bot` specs in parallel. "Isn't that mind-blowing." |

## Her rhythm (the reusable part)

**Tell → show a real past example → do a new one live.** She never demos on empty state. The skills beat works because she points at a conversation that already happened, then repeats the move fresh. Steal this for every feature.

**Say the seam.** She openly cuts from the fresh install to her real machine and names it. Turns a continuity problem into credibility.

**Ease framing throughout.** "Easy cookie," "just ask Hermes to help you set it up." Every hard step is delegated to the agent on camera.

**Ends on the build, not the recap.** The last four minutes are the most impressive thing in the video, and she saves it.

## What works
- Immediate proof in the hook (systems already running)
- Desktop-first lowers the barrier; she says why
- Concrete file paths on screen (Finder, the .md files)
- Honest about cost, honest about "I'm not going deep here"
- The Pomodoro build is a real artifact she then uses

## Weaknesses / our openings
- **No Claude Code framing.** Treats Hermes as a first agent. Our audience already has one.
- **Recall demo only proves storage.** "Remind me what we discussed" = a database lookup. Producing work from memory with zero context proves it is load-bearing.
- **4.5 min on Honcho + Obsidian.** Third-party signup with credits in a "fundamentals" video. Config lines (`write_approval`, `background_review`) do the job with no accounts.
- **Never explains WHY memory files are capped.** The always-loaded-vs-searched-on-demand architecture is the "oh, that's why" beat nobody in the set has.
- **Discord payoff is a widget.** A real PR on GitHub plus a Slack ping beats a Pomodoro timer.
- **One profile.** She never shows the "Applies to" per-bot settings or a roster of named bots.
- **Predates v0.20.** No Bot Mode, no desktop Bots tab, no `/journey` memory graph, no voice.
- **Panel names have changed.** Her "Skills and Tools" is now **Capabilities** (tabs: Capabilities / Skills / Tools). Say the current name once on camera.

## What we do instead (video 057)

| Her beat | Our beat | Our exact prompt / click |
|---|---|---|
| 1 Hook: Discord + Obsidian running | Phone: Slack cards (8am Attend, Coder verdict). Desktop: Bots tab, 4 bots | clips, no typing |
| 2 Hardware, 4 options | 30s: "Mac Studio, on all day. Laptop works, VPS works." | none |
| 3 Install via desktop | Same, desktop first | Download → open → composer model picker → Nous Portal |
| 4 hi | Same | `hi` |
| 5 Claude writes bio → paste | Same move; natural for Claude Code users | In Claude Code: `Write a short paragraph about me I can hand to a new AI assistant.` Paste + `Please remember this.` Then: `Given what you now know about me, what would you not bother explaining to me?` |
| 6 Cut to mature, Obsidian | Same cut, say the seam, own editor | `open ~/.hermes/memories/` → USER.md, MEMORY.md. Count on camera. Edit a line live. |
| 7 Settings scroll | 20s: Model, Memory & Context (the caps), **Applies to** chips | Cmd+, |
| 8 Tools tab, AI chips search | **Capabilities** → Tools tab | `Search the web for what changed in Hermes Agent's latest release and give me the three things a Claude Code user would care about.` |
| 9 "connect to Telegram" | Settings → Messaging: Slack connected; point at Telegram **Create with QR** | none |
| 10 MCP one-liner | Same skip | none |
| 11 Past chat → make a skill → run it | Identical shape, our data | `Look at my last 10 uploads and day-1 view medians. Which title pattern is winning? 5 new title ideas, scored 1-10.` → `Make this into a skill for checking my titles.` → new chat `/title-check` |
| 12 Her 11pm brief | Our 8am Attend + 9pm YouTube (weeks of `ok`), then create Coder's live | Routines pane → New; `hermes cron list` |
| 13 "Remind me what we discussed" | **Produce, don't recall** | `Based on everything you know about how I work, draft the outline for my next video. Don't ask me anything first.` Then `/journey` |
| 14 Honcho + Obsidian | Two config lines, no accounts | `hermes config set memory.write_approval true` → `/memory pending`; `hermes config get auxiliary.background_review` (gemma4:e4b) |
| 15 Local Qwen, llama.cpp | Same claim: whole video on qwen3.8 / gemma4 via Ollama | `ollama launch hermes` or Settings → Providers → Local Models |
| 16 Discord Pomodoro build | **Bots tab: Researcher → Packager → Coder → real PR → Slack ping** | In Researcher's Bot Chat: `@packager build the package for video 057 from the research you have. When it's done, @coder opens a PR with it on tylerprogramming/content and posts the link to Slack.` |

## Possible extras (not in her video, available to us)
- `/journey` memory graph with the playback scrubber
- Context meter → token breakdown, pointing at memory's share (pays off the caps beat)
- Git review pane (Cmd+G) scoped to "Last turn," then **Ask Hermes to open PR**
- Profile export: right-click Coder → Export → `.tar.gz` with skills, SOUL, memory, crons, keys stripped. "Here's my Coder. Import it."
- Curator: `hermes curator status` for the "it drifts" honesty line
- Live Subagents frame during a `delegate_task` fan-out
