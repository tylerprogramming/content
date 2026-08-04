# Claude Mega Course - Outline (Claude Code + Claude Cowork + AI Agents)

**Type:** Course OUTLINE (structure only, not a script)
**Compiled:** 2026-08-04
**Target runtime:** ~3 hours (180 min, three parts + intro/outro)
**Audience:** Business owners, creators, and technical-curious people who already use Claude Chat and want the full system. Two on-ramps in one course: the no-code path (Cowork, agents) and the builder path (Claude Code). Tyler is a software engineer, so the promise is "I build the hard version at a Fortune 500, here is the version anyone can start with today."
**Voice/rules:** no em dashes, no money amounts in titles, no hype words, drafts before sends, show real runs, admit limits. Honest over impressive.

**Format note (say this early):** film it MODULE BY MODULE, each with its own screen recording, stitched with chapter cards. Do not attempt one pass. Chapters go in the description. Viewers can jump to any part.

**Accuracy note:** every feature named below is confirmed in `research/youtube/2026-08-02-all-claude-code-features.md` (Claude Code v2.1.x, mid-2026). Custom slash commands and skills are now the same thing. The `/agents` wizard was removed (ask Claude or edit `.claude/agents/` directly). Cowork rollout details (scheduled-task-in-background, Chrome availability) change, so state what is live on filming day.

---

## The running timeline (sums to 3:00:00)

| Time | Section |
|---|---|
| 0:00 | INTRO |
| 0:08 | PART 1 - Claude Code |
| 1:13 | PART 2 - Claude Cowork |
| 2:00 | PART 3 - AI Agents |
| 2:52 | OUTRO |
| 3:00 | END |

---

# INTRO (0:00 - 0:08) ~8 min

**By the end of this intro you can:** say exactly which Claude surface to reach for and what you will have built by the end of the course.

### 0.1 Who this is for and what you will build (0:00, 3 min)
Cold open with a result on screen, not a channel intro. One line on who is teaching (software engineer by day, runs a channel and community, uses all of this daily). Lay out the three real deliverables: a working Claude Code setup with your own skill, a Cowork employee that runs a scheduled task, and an AI agent you built with no code. Promise every step on camera, nothing faked.
- **Reuse:** cold-open + "software engineer by day" framing from `021-claude-cowork-clearly-explained/script.md` (sec 1) and `023-.../script.md` INTRO.

### 0.2 The mental model: Chat vs Code vs Cowork vs Agents (0:03, 5 min)
The spine of the whole course. Chat = a conversation (words back, you still do the work). Cowork = an employee (describe the outcome, finished files come back, no code). Claude Code = the engineer (builds custom tools and automations, terminal-first). Agents = a goal + tools + a loop that runs the steps on its own. Same engine underneath (Cowork and Code share it), different surfaces. Draw the one diagram viewers should hold the whole time.
- **Reuse:** "brain vs hands" analogy from `021/script.md` (sec 5); "Chat = conversation, Cowork = employee" from `023/script.md` INTRO; the "one engine, many surfaces" idea from the all-features doc sec 0.

---

# PART 1 - CLAUDE CODE (0:08 - 1:13) ~65 min

**By the end of Part 1 you can:** install Claude Code, drive it to edit and run real code, give it a CLAUDE.md and memory, build and run your own skill, connect a live tool over MCP, plan/checkpoint/subagent your way through a big change safely, and ship one real project end to end.

### 1.1 Install and first launch (0:08, 5 min)
Native install (`curl -fsSL https://claude.ai/install.sh | bash`, PowerShell, or Homebrew). `cd your-project && claude` to open the REPL. Sign in, run `claude doctor` to confirm setup. Tour the interface: prompt box, activity, the mode selector.
- **Task:** install it, open a real folder, run `claude "explain this codebase"`.
- **Reuse:** none direct; new, but keep the "don't let the name scare you, not writing code first" framing from `038/script.md` [1:30-2:30].

### 1.2 The basics - chat, edit, run (0:13, 6 min)
The core loop everything else builds on: ask a question, let it edit files, let it run a command. Show it reading files, making an edit with an inline diff, running the test/build, and reporting back. Introduce `/clear`, `/context`, and image input (paste a screenshot of a broken UI, get a fix).
- **Task:** have Claude add a small feature or fix a bug in a throwaway repo, then run it.
- **Reuse:** new footage; the "70 percent right, you give one correction" habit from `023/script.md` M2 applies verbatim as the working rhythm.

### 1.3 CLAUDE.md and memory (0:19, 7 min)
The single biggest lever on quality. `/init` to generate a starting CLAUDE.md. What belongs in it (build/test commands, conventions, "always do X"). The scope hierarchy (user vs project vs local) in one sentence. Auto memory: Claude saves its own learnings and reloads them each session ("Saved N memories"). The `#` shortcut and `/memory`. `/context` to confirm what actually loaded.
- **Task:** run `/init`, then tighten the CLAUDE.md to three real rules and prove it changes behavior.
- **Reuse:** the CLAUDE.md-as-employee-handbook framing from `023/script.md` M3 (works the same in Code); all-features doc sec 2 for the facts.

### 1.4 Slash commands and skills - build one live (0:26, 9 min)
Kill the scary part first: a skill is a folder with one `SKILL.md` (plain-English description + instructions). Slash commands and skills are the same thing now. Show a real SKILL.md, point at the description line, then build a brand new one live in ~2 minutes and run it by name.
- **Task (PROJECT 1):** create `~/.claude/skills/<name>/SKILL.md` for a genuinely useful small task (e.g. summarize a git diff into a commit message, or draft a caption), save, run it.
- **Reuse:** the live 2-minute skill build from `040/script.md` [11:30-13:30] and "what a skill actually is" [1:30-2:45]; `012-skills-full-course` for deeper skill material if a segment needs padding. All-features doc secs 3-4.

### 1.5 MCP - connect a real tool (0:35, 7 min)
What MCP is in one line (connect Claude to external tools/data instead of copy-pasting). Add one server live: `claude mcp add --transport http <name> <url>`, `claude mcp list` to see health, run a tool, do the one-time OAuth. Then ask a real question against live data.
- **Task (PROJECT 2):** connect one tool (GitHub, Sentry, or Tyler's ClickUp) and ask it something real ("what are the most common errors in the last 24 hours?" / "summarize my open issues").
- **Reuse:** the one-gateway framing and `claude mcp add ... --transport http` flow from `2026-08-02-arcade-mcp-course-outline.md` (Modules 1-2) and `046-arcade-build-agent/script.md`; all-features doc sec 5.

### 1.6 Subagents, plan mode, and checkpoints (0:42, 9 min)
Three moves that make big changes safe. Plan mode (Shift+Tab or `/plan`): Claude researches and proposes without editing, you approve. Subagents (Explore for read-only search) keep noisy work out of your main context; show the `/context` grid before/after. Checkpoints/`/rewind` (or double-Esc): a session-level undo. State the honest limits of rewind on camera (does not undo bash `rm`/`mv`, not a git replacement).
- **Task:** plan a non-trivial change, let it run, then `/rewind` to snap it back.
- **Reuse:** new footage; all-features doc secs 6, 8, 10 and the "plan + rewind together" demo (Most Demo-Worthy #1).

### 1.7 Hooks (0:51, 5 min)
Deterministic guardrails: a shell command that always runs at a lifecycle event, instead of hoping the model does it. Two concrete demos: PostToolUse auto-format after every edit, PreToolUse block edits to a protected file (`.env`). Keep it to the two that land; `/hooks` to browse.
- **Task:** add a PostToolUse prettier/format hook to the demo repo and watch it fire.
- **Reuse:** new; all-features doc sec 7 (example JSON is ready to show).

### 1.8 Permissions, auto mode, and safety (0:56, 5 min)
The permission modes (Manual/default, acceptEdits, plan, auto) cycled with Shift+Tab. Auto mode as the 2026 flagship: a separate classifier approves safe actions and blocks dangerous ones (`curl | bash`, force push, secret exfiltration, `rm -rf` on unresolved variables) so you get long autonomous runs without blanket bypass. `/permissions` and `/fewer-permission-prompts`. Deny rules always win.
- **Task:** turn on auto mode for a longer task and watch it run with fewer prompts.
- **Reuse:** new; all-features doc sec 11 (auto mode is the headline). Frame safety honestly, not as magic.

### 1.9 PROJECT - build something real, end to end (1:01, 12 min)
Tie it all together on one real deliverable. Suggested: build a small working tool (a CLI utility, a landing page, or a script Tyler actually needs) using the full chain: CLAUDE.md set, plan mode to design, auto mode to execute, a hook enforcing format, an MCP tool for real data, checkpoints as the safety net, then Claude commits it with a message. Show the finished thing running.
- **Task (PROJECT 3):** ship one real artifact from empty folder to working + committed.
- **Reuse:** structure mirrors the "run my business" system in `040/script.md`; pick a project Tyler genuinely wants so the footage is reusable as a standalone video.

---

# PART 2 - CLAUDE COWORK (1:13 - 2:00) ~47 min

**By the end of Part 2 you can:** install Cowork, set up its folder and permission boundary, turn messy inputs into finished files, give it memory so it knows your voice, connect Gmail/Drive/a custom MCP, and put a real task on a schedule.

### 2.1 What Cowork is and the mental model (1:13, 4 min)
Cowork = Claude with hands: it reaches into your folders, reads and creates files, and does the task instead of describing it. Same engine as Claude Code, made usable with no code. Desktop app only, not the browser. The "new employee on day one" frame. One honest heads-up: big tasks burn more usage.
- **Reuse:** heavy reuse from `021/script.md` (secs 4-5) and `030-claude-cowork-explained`; `023/script.md` INTRO.

### 2.2 Setup and the folder/permission model (1:17, 6 min)
Get it right once. Paid plan + desktop app from claude.ai/download (NOT the website, the #1 confusion). Open the Cowork tab. Create ONE dedicated folder, framed as a memory folder that everything reads from and adds to. Point Cowork at it; that folder is the safety boundary (it can only touch folders you give it). Tour the three areas (chat, activity panel, settings/connectors/scheduled tasks). First task: create an about-me.md by having it interview you.
- **Task:** install, make the memory folder, run the about-me interview.
- **Reuse:** direct from `023/script.md` Module 1 (steps + the "first brick of memory" beat).

### 2.3 Real tasks - organize files, notes to spreadsheet, research (1:23, 8 min)
The core loop (inputs in the folder, describe the outcome, review, give one correction). Two demos: organize a messy client folder into clean renamed subfolders + a summary; and turn raw inputs (receipt photos or meeting notes) into a structured spreadsheet plus a summary that flags something you did not ask for (a duplicate subscription).
- **Task (PROJECT 4):** drop 5-6 receipt photos or a pile of notes and get back a clean spreadsheet + summary.
- **Reuse:** direct from `023/script.md` Module 2 (both demos, plus the "feedback not redo" habit). Demo assets exist in `023-.../demo-assets/`.

### 2.4 Memory for Cowork (1:31, 5 min)
Turn the about-me into a real CLAUDE.md instructions file (have Cowork interview you to write it). It reads it on every task. Plus the memory it builds from your corrections (voice, preferences). Prove it with a before/after report that comes out formatted your way without being told, and an email draft already in your voice. The one rule: correct, do not redo.
- **Task:** build your CLAUDE.md, then ask for a report and watch it match your format unprompted.
- **Reuse:** direct from `023/script.md` Module 3.

### 2.5 Connectors - Gmail, Drive, custom MCP (1:36, 8 min)
Settings > Connectors > add > approve permissions. The boundary line viewers need: it asks first, you approve, you can revoke. Demo Gmail inbox triage (48 hours, sorted, drafts in your voice) and two sources at once (Drive scripts + a local analytics file in one prompt). Then show adding a custom connector (remote MCP URL) so it is not limited to the built-in list. Honest note: connectors are strongest at read/draft; you stay the one who hits send.
- **Task (PROJECT 5 setup):** connect Gmail and run a triage; add one custom connector by URL.
- **Reuse:** `023/script.md` Module 5 (Gmail + Drive demos); custom-connector flow from `2026-08-02-arcade-mcp-course-outline.md` Module 2 (Cowork = Settings > Connectors > add custom > paste URL > authorize).

### 2.6 Scheduled tasks and routines (1:44, 6 min)
The payoff: a job Cowork runs on its own using your folders, memory, connectors, and skills. Show a real prior output (a morning brief or Monday report), then build one live: prove it manually first, create the task, describe it in plain language, set the schedule, confirm it has access to what it needs, let the first run fire, correct. HONEST beat: whether it runs fully in the background or needs the app open depends on your setup and the rollout, so test before you rely on it.
- **Task (PROJECT 6):** schedule a Monday analytics report to the folder.
- **Reuse:** direct from `023/script.md` Module 8 (including the honesty caveat, which is the brand).

### 2.7 PROJECT - a real research task, folder to decision (1:50, 6 min)
Pull the part together on one useful job: hand Cowork a pile of raw material (competitor transcripts, exports, notes) and get back a ranked opportunities spreadsheet or a weekly report with three recommendations at the top. Data vs analysis: it tells you what to DO, not just what happened.
- **Task:** gap analysis or weekly report from real inputs.
- **Reuse:** direct from `023/script.md` Module 4 (both demos + the "inputs in, specific question, follow up deeper" pattern).

### 2.8 Cowork vs Code vs Chat - when to use which (1:56, 4 min)
The decision rule, stated plainly. Chat = a quick answer. Cowork = an outcome you would hand an assistant (organize, analyze, draft, triage), desktop, files + apps, no code. Code = building custom tools and automations, terminal, scriptable. The real system: Cowork runs recurring operations, Code builds the machinery, you graduate your most-repeated Cowork tasks into Code skills.
- **Reuse:** `023/script.md` Module 9; the surface-by-surface framing in `arcade-mcp-course-outline.md` Module 6.

---

# PART 3 - AI AGENTS (2:00 - 2:52) ~52 min

**By the end of Part 3 you can:** explain what an agent actually is, build your first one with no code, give it tools over MCP, understand the loop/memory/self-check, ship a real agent end to end, name where agents fail, and run one on a schedule.

### 3.1 What an agent actually is (2:00, 5 min)
Kill the intimidation. An agent is three things: a goal (something you want done), a tool it is allowed to use (search the web, read a file, hit an API), and you telling it what to do in plain English. A chatbot talks back; an agent has a job and goes and does it, figuring out the steps itself. Earned authority once: Tyler built the heavy production version at Fortune 500s, and you do not need any of it to start.
- **Reuse:** direct from `038/script.md` [0:20-1:30] (the three-part graphic is the anchor for the whole part).

### 3.2 Build your first agent, no code (2:05, 10 min)
Build ONE real agent live: a research agent (topic in, real web research, one-page brief with sources out). Make a folder, write ONE plain-English instructions file (who it is, what to do, "if unsure say so, do not make things up"), give it the one tool it needs (web search), run it on a real topic, then nudge it (it gets you 80-90 percent, you steer the rest). No frameworks, no code.
- **Task (PROJECT 7):** build and run the research-brief agent.
- **Reuse:** direct from `038/script.md` [1:30-8:00], the full live build. Copy-pack already exists for this agent.

### 3.3 Tools and MCP for agents (2:15, 7 min)
Agents are only as capable as their tools. The wall everyone hits is auth (OAuth, tokens, scopes), not the tools. Show connecting real tools to an agent: either built-in (web search, file read) or a runtime like Arcade that handles per-user OAuth so you get Gmail/Calendar/Slack/GitHub without wiring anything. Same MCP idea as Part 1, now aimed at giving an agent hands.
- **Task:** give the agent one connected tool (calendar or email, in draft/safe mode).
- **Reuse:** `046-arcade-build-agent/script.md` [0:15-2:30] (the "tools + auth, auth is the hard part" framing and the Arcade one-line setup); all-features doc sec 5.

### 3.4 The agent loop, memory, and self-verification (2:22, 7 min)
What is happening under the hood, explained plainly. The loop: pick an action, use a tool, read the result, decide the next step, repeat until the goal holds (`/goal` sets a completion condition). Memory so it carries context across runs. Self-verification: have the agent check its own work before declaring done (the honest version of "reliable"). Keep it conceptual and visual, not a lecture.
- **Task:** add a "check your work against the sources before finishing" instruction and watch it self-correct.
- **Reuse:** new; all-features doc secs 6 (agent loop / subagents) and 18 (`/goal`). Reinforces the "nudge" rhythm from `038`.

### 3.5 PROJECT - a real agent, end to end (2:29, 11 min)
Build a genuinely useful agent start to finish, with a visible timer for the reusable-short cut: a morning brief agent that reads today's Calendar + unread Gmail, summarizes the day, flags the emails that need a reply, and drafts those replies in draft/safe mode. Show the real run, the real output, and one nudge.
- **Task (PROJECT 8):** build and run the morning-brief agent.
- **Reuse:** direct from `046-arcade-build-agent/script.md` (this is exactly that agent, 7-minute build) - shoot once, cut the short from it.

### 3.6 Where agents fail and keeping them safe (2:40, 6 min)
The trust beat, do not skip. Agents are not perfect: weak sources, missed nuance, confident wrong answers. Not set-it-and-forget-it, you still steer. Safety: default to drafts, keep actions reversible, per-user OAuth so tokens are never hardcoded, every action logged, and the classifier/permission guardrails from Part 1. What to never let an agent do unattended.
- **Reuse:** direct from `038/script.md` [9:15-10:30] (honest limitations) and the safety/governance beat in `arcade-mcp-course-outline.md` Module 6.

### 3.7 Ship it - run your agent on a schedule (2:46, 6 min)
From "I ran it once" to "it runs without me." Put the agent on a schedule: Routines (scheduled cloud agents, cron/event triggers, run even when your machine is off, created with `/schedule`) or a Cowork scheduled task / local cron. Same rule as Cowork: prove it manually, schedule it, verify the first real run before you rely on it.
- **Task:** schedule the morning-brief agent to run daily and verify the first fire.
- **Reuse:** all-features doc sec 18 (Routines); the scheduled-task discipline from `023/script.md` Module 8; the comment/email monitors in `040/script.md` [6:30-9:30] as a real "runs while I'm not here" example.

---

# OUTRO (2:52 - 3:00) ~8 min

### Recap (2:52, 3 min)
Zoom out: you installed and drove Claude Code, built a skill, connected a tool, and shipped a project; you set up Cowork with memory, connectors, and a scheduled task; you built two agents and put one on a schedule. That is not a feature list, it is a working system. Reinforce the mental model one last time (Chat / Cowork / Code / Agents).

### What to build next and resources (2:55, 5 min)
One clear action: pick ONE task you do every week and hand it to whichever surface fits, this week. Not the whole system, one task. Point to the starter prompt pack, the copy-paste agent, the CLAUDE.md files, and the community/newsletter (free.tylerai.dev/youtube). Comment prompt: what is the first thing you will automate. Tease the deeper single-topic courses (Cowork full course, skills course, Arcade agent build) for anyone who wants to go further on one part.
- **Reuse:** outro + CTA structure from `023/script.md` OUTRO and `040/script.md` recap; keep it under 2 minutes of actual CTA.

---

# The hands-on projects (8 across the course)

1. **Build a live skill in Claude Code** (Part 1.4) - a real `SKILL.md` you run by name (commit-message summarizer, caption drafter).
2. **Connect an MCP tool and query it** (Part 1.5) - GitHub / Sentry / ClickUp, ask it something real against live data.
3. **Claude Code capstone** (Part 1.9) - ship one real artifact from empty folder to working + committed, using plan mode, auto mode, a hook, an MCP tool, and checkpoints.
4. **Cowork: raw inputs to spreadsheet** (Part 2.3) - receipt photos or notes into a clean spreadsheet + a summary that flags something.
5. **Cowork research project** (Part 2.7) - a pile of material into a ranked opportunities sheet or a weekly report with recommendations.
6. **Cowork scheduled task** (Part 2.6) - a Monday report that runs on its own.
7. **Your first agent, no code** (Part 3.2) - the research-brief agent (topic in, sourced one-pager out).
8. **Morning-brief agent, shipped on a schedule** (Parts 3.5 + 3.7) - Calendar + Gmail summary with drafted replies, running daily.

---

# Reusable-footage map (so Tyler does not re-shoot everything)

| Module | Reuse from |
|---|---|
| Intro mental model | 021 sec 5, 023 intro, all-features sec 0 |
| P1 skills (build one live) | 040 [11:30-13:30], 012-skills-full-course |
| P1 MCP | arcade-mcp-course-outline Mod 1-2, 046 [0:45-2:30] |
| P1 plan/rewind/subagents/hooks/auto | all-features secs 6-11 (new footage, doc has demos) |
| P1 capstone / "runs my business" | 040 full |
| P2 setup + memory folder | 023 Modules 1, 3; 021; 030 |
| P2 files / spreadsheet | 023 Module 2 (+ demo-assets) |
| P2 research project | 023 Module 4 |
| P2 connectors + custom MCP | 023 Module 5; arcade-mcp Mod 2 |
| P2 scheduled tasks | 023 Module 8 |
| P2 vs Chat/Code | 023 Module 9; arcade-mcp Mod 6 |
| P3 what-is-an-agent + first agent + limits | 038 full |
| P3 tools/auth + morning brief agent | 046 full |
| P3 schedule / runs-while-away | all-features sec 18; 040 [6:30-9:30] |

# Sources
- `research/youtube/2026-08-02-all-claude-code-features.md` (feature accuracy, v2.1.x)
- `research/youtube/2026-08-02-arcade-mcp-course-outline.md` (one-gateway MCP across surfaces)
- Packages: `youtube/videos/021-claude-cowork-clearly-explained`, `023-claude-cowork-full-course`, `030-claude-cowork-explained`, `012-skills-full-course`, `040-claude-code-skills-run-my-business`, `038-build-first-ai-agent`, `046-arcade-build-agent`
