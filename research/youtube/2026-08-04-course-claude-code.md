# Claude Code - Standalone Course (Outline)

**Type:** Course OUTLINE (structure only, not a script)
**Compiled:** 2026-08-04 (expanded from the ~87 min v1 to a full 2+ hour course; then widened again to cover all three surfaces properly, Claude in Chrome, and a closing library wrap; then a two-lesson "deploy to production" block was added before the wrap so the course ends with something actually running live)
**Target runtime:** ~3:00:00 (180 min), intro + 28 lessons + outro
**Audience:** Anyone who already uses Claude in the browser and wants the terminal-first, buildable version. Beginners welcome, but this goes deep enough for someone who has poked at Claude Code and wants the whole picture. Tyler is a software engineer by day (Pfizer, ex-IBM/Chase); the promise is "I build the heavy version at a Fortune 500, here is the version you can start today, and the honest limits of each piece."
**Voice/rules:** no em dashes, no money amounts in titles, no hype words, always draft before send, show real runs on camera, admit limits out loud. Honest over impressive. Not a growth-strategy channel; this is about Claude and AI automation.

**Format note (say this early, to yourself not the viewer):** film it LESSON BY LESSON, each with its own screen recording, stitched with chapter cards. Do not attempt one pass. Chapters go in the description so viewers can jump to any lesson. At 2+ hours, chapter navigation is not optional, it is the whole reason the video is watchable.

**Accuracy note:** every feature named below is confirmed in `research/youtube/2026-08-02-all-claude-code-features.md` (Claude Code v2.1.x, mid-2026). Two things people still get wrong, so say them plainly: (1) custom slash commands and skills are the SAME thing now (a `.claude/commands/deploy.md` and a `.claude/skills/deploy/SKILL.md` both create `/deploy`); (2) the `/agents` creation wizard was removed in v2.1.198 (ask Claude to write the file, or edit `.claude/agents/` directly). State whatever is live on filming day for anything in active rollout (Chrome, Desktop-on-Linux, background subagents).

**This is a complete course, not part one of anything.** It has its own cold open, its own capstone, and its own outro. It expands Part 1 of the mega-course outline (`2026-08-04-claude-mega-course-outline.md`) into a full standalone. Cowork and agents are only referenced at the very end as "where to go next."

**What changed from v1 (why this is now 2+ hours):** the extra 52 minutes are DEPTH, not padding. Skills went from one live build to three full walkthroughs (a plain skill, a skill with a bundled script, and a personal-workflow automation). MCP went from one connection to two lessons (first tool, then multiple servers with local-vs-remote and a real troubleshooting pass). New standalone lessons were added for context management, scheduling/routines, a real refactor project, a tiny Agent SDK build, common mistakes/troubleshooting, and power-user workflows. The capstone became a larger multi-part build.

**What changed again (the +13 minutes on top of that):** the surfaces lesson stopped being a flyby and became a real lesson on running Claude Code across the terminal, the Desktop app, and the web app (plus phone and cloud), including `--teleport` and steering background agents. A dedicated Claude in Chrome lesson was added (it doubles as a strong standalone video). And a closing "Your skills and agents library" wrap lesson was added so the course ends with the student holding a real, keepable library of the skills and agents they built along the way, not a pile of throwaway demos.

**What changed once more (the +28 minutes to reach three hours):** a two-lesson "deploy to production" block was added right before the library wrap, because a course that ends at "it works on my machine" leaves out the part that actually matters. The first lesson is the unglamorous production checklist (real secrets and env handling, error handling, logging, config). The second is the payoff: the student takes ONE thing they built and ships it so it is genuinely running live and unattended, either a small app or tool on a real host with a live URL, or a skill/agent on a schedule that fires on its own, then verifies the live run and wires basic monitoring. It is kept honest the whole way: real costs, real keys, what can break, how you roll back. The library wrap still closes the course.

---

## By the end of this course you can...

- Install Claude Code and drive the REPL to read, edit, and run real code
- Manage context deliberately with `/context`, `/clear`, `/compact`, and rewind-summarize so long sessions stay sharp
- Give it a CLAUDE.md and let auto memory make it better at your repo over time
- Build three real skills: a plain one, one that runs a bundled script, and one that automates a workflow you actually do
- Run it headless (`-p`), pipe it into other tools, and put it on a schedule as a routine
- Connect multiple live tools over MCP, query real data, and troubleshoot a broken connection
- Delegate noisy work to subagents (and write your own) to keep your main context clean
- Plan big changes before they run, and rewind if you do not like the result
- Enforce guardrails with several real hooks and run long tasks safely under auto mode with a tuned allowlist
- Pick the right model, effort, and thinking level for the job
- Use image input and web search, commit and open PRs through git/GitHub, and run parallel work in worktrees
- Refactor real code and add a feature end to end, and build a tiny agent with the Claude Agent SDK
- Run the same engine across the terminal, the Desktop app, and the web app, start a session on one surface and continue it on another with `--teleport`, and steer background agents while they run
- Let Claude drive a real browser with Claude in Chrome to reproduce a bug or automate a repetitive web task, safely
- Avoid the common mistakes, diagnose a broken setup, and chain the power-user moves
- Ship one real multi-part project from an empty folder to working and committed
- Run a production-readiness pass on real code (secrets in env not hardcoded, error handling, logging, config) and then deploy ONE real thing so it is genuinely running live and unattended, either an app on a real host with a live URL or a skill/agent on a schedule, with a run log, a cheap alert, and an honest rollback plan
- Walk away with a real, reusable library of the skills and agents you built in this course, organized and ready to run forever

---

## The running timeline (sums to 3:00:00 / 180 min)

| Time | Lesson |
|---|---|
| 0:00 | INTRO |
| 0:06 | 1 - Install, setup, and first launch |
| 0:10 | 2 - The basics: chat, edit, run (the REPL) |
| 0:15 | 3 - Context management (the skill that keeps sessions sharp) |
| 0:20 | 4 - CLAUDE.md and memory |
| 0:26 | 5 - Skills part 1: build your first skill live |
| 0:32 | 6 - Skills part 2: a skill that runs a bundled script |
| 0:38 | 7 - Skills part 3: automate a workflow you actually do |
| 0:43 | 8 - Headless mode (scripting Claude Code) |
| 0:48 | 9 - Routines: put Claude Code on a schedule |
| 0:52 | 10 - MCP part 1: connect your first live tool |
| 0:58 | 11 - MCP part 2: multiple servers, local vs remote, troubleshooting |
| 1:04 | 12 - Subagents: Explore, custom agents, when to delegate |
| 1:10 | 13 - Plan mode, checkpoints, and rewind |
| 1:16 | 14 - Hooks: format-on-edit, block .env, notify |
| 1:22 | 15 - Permissions, auto mode, and the allowlist deep dive |
| 1:28 | 16 - Models, thinking, and effort |
| 1:32 | 17 - Image input and web search |
| 1:36 | 18 - Git and GitHub: commits, PRs, worktrees |
| 1:41 | 19 - A real refactor and feature project |
| 1:47 | 20 - Surfaces: terminal, Desktop, web, phone, and cloud (with teleport) |
| 1:53 | 21 - Claude in Chrome: let Claude drive a real browser |
| 1:59 | 22 - The Claude Agent SDK: build a tiny agent |
| 2:04 | 23 - Common mistakes and troubleshooting |
| 2:09 | 24 - Power-user workflows |
| 2:14 | 25 - CAPSTONE: a real multi-part build, end to end |
| 2:23 | 26 - The production checklist: secrets, errors, logging, config |
| 2:35 | 27 - Ship it live: put it in the world, running on its own |
| 2:51 | 28 - Your skills and agents library (what you keep) |
| 2:56 | OUTRO |
| 3:00 | END |

---

# INTRO (0:00 - 0:06) ~6 min

**By the end of this intro you can:** say what Claude Code actually is, why it is different from Claude in the browser, and exactly what you will have built by the end.

### 0.1 Cold open: who this is for and what you will build (0:00, 3 min)
Open with a result on screen, not a channel intro. Show Claude Code doing something real in your actual setup (planning or editing a live file), then cut to camera. One line on who is teaching: software engineer for years, builds the production version of this at a Fortune 500, runs a channel and community, uses this every single day. Lay out the promise: by the end you will have installed Claude Code, built three skills, connected multiple live tools, refactored real code, built a tiny agent, run it across the terminal, the Desktop app, and the web, let Claude drive a browser, shipped one real multi-part project, and deployed one real thing so it is running live and unattended, all on camera, nothing faked. Say the bigger promise plainly, because it is the reason to sit through two and a half hours: by the end you will have a folder of skills and agents you actually use every day, not a pile of demos you delete after the video. Everything you build in this course, you keep. Say the honesty rule up front: every limit gets stated out loud, because that is what makes the wins trustworthy. Because this is long, tell them how to use it: chapters in the description, each lesson is self-contained, jump to what you need.
- **Reuse:** cold-open energy and "I've been using Claude Code every day for months" framing from `003/script.md` [0:00-0:35]; the "none of this is code, you do not need to be an engineer, I am one and I am telling you that" beat from `040/script.md` [0:00-0:35].

### 0.2 The mental model: one engine, many surfaces (0:03, 3 min)
The spine of the whole course. Claude Code is an agentic coding tool: it reads your codebase, edits files, runs commands, and integrates with your dev tools. The same engine runs across five surfaces (Terminal, VS Code, JetBrains, Desktop, Web) and your CLAUDE.md, skills, and MCP servers work across all of them. Draw the one diagram viewers should hold the whole time: one brain, many surfaces. Contrast with Claude in the browser in a sentence: chat gives you words back and you still do the work; Claude Code does the work in your files and terminal. Preview install so they can follow along.
- **Reuse:** "one engine, many surfaces" from all-features doc sec 0; "brain vs hands" analogy exists in `021/script.md` sec 5 if you want a beat.

---

# LESSON 1 - Install, setup, and first launch (0:06 - 0:10) ~4 min

**What it covers:** get it running on any machine and confirm the setup is healthy. Native install (`curl -fsSL https://claude.ai/install.sh | bash` on macOS/Linux/WSL, `irm https://claude.ai/install.ps1 | iex` on Windows PowerShell, or `brew install --cask claude-code`). `cd your-project && claude` to open the REPL. Sign in. Run `claude doctor` (alias `/checkup`) to confirm everything is wired. Quick tour of the interface: prompt box, activity area, the mode selector at the bottom, the context meter.
- **Hands-on task:** install it, open a real folder, run `claude "explain this codebase"` and read what comes back.
- **Reuse:** new footage. Keep the "do not let the name scare you, you are not writing code first" framing.

---

# LESSON 2 - The basics: chat, edit, run (the REPL) (0:10 - 0:15) ~5 min

**What it covers:** the core loop everything else builds on. Ask a question, let it edit a file (show the inline diff), let it run a command (test or build), and read the report back. This is interactive mode, the REPL, and it is the default way to work; everything else in the course is a variation on it. Name the "70 percent right, you give one correction" rhythm and call it the working habit for the whole course. Point out the mode selector at the bottom and that Shift+Tab cycles permission modes (foreshadow, do not teach yet). Keep this lesson pure on the loop; context management gets its own lesson next.
- **Hands-on task (PROJECT 1):** in a throwaway repo, have Claude add a small feature or fix a bug, then run it and confirm it works. Give it one correction on purpose so beginners see steering is normal, not failure.
- **Reuse:** the core chat/edit/run demo and green context meter glimpse from `003/script.md` [2:30-3:45]; the "70 percent then one correction" framing is your own recurring line.

---

# LESSON 3 - Context management: the skill that keeps sessions sharp (0:15 - 0:20) ~5 min

**What it covers:** the invisible thing that decides whether a long session stays smart or turns to mush, pulled out of the basics because it deserves real time. The context window holds your CLAUDE.md, loaded skills, MCP tools, and the whole conversation; when it fills, quality drifts (context rot). The moves: `/context` to see what is loaded as a colored grid (memory, skills, MCP tools, conversation) and spot what is eating the window; `/clear` (aliases `/reset`, `/new`) to start a fresh context when you switch tasks; `/compact` to summarize the conversation and reclaim room when you are mid-task and cannot clear. Then the advanced move most people miss: `/rewind` -> "summarize from here" / "summarize up to here" to compress a verbose stretch (a long debugging back-and-forth) without losing your original instructions. Say the honest heuristic on camera: when a session starts repeating itself or forgetting what you said two prompts ago, that is the window, not the model; clear or compact and move on.
- **Hands-on task:** open `/context` on a real session, read the grid out loud, then run one big search, watch the grid grow, and `/clear` to reset it. Then trigger a summarize-from-here on a verbose stretch.
- **Reuse:** context-window / context-rot explanation and the green meter from `003/script.md` [2:30-3:45]; the `/clear` basics from `003` [5:00-6:15]; all-features doc secs 10 (summarize-from-here) and 18 (`/context`, `/compact`).

---

# LESSON 4 - CLAUDE.md and memory (0:20 - 0:26) ~6 min

**What it covers:** the single biggest lever on quality. `/init` generates a starting CLAUDE.md by analyzing your codebase. What belongs in it: build and test commands, conventions, "always do X" rules. The scope hierarchy in one breath (user `~/.claude/CLAUDE.md` for all projects, project `./CLAUDE.md` committed for the team, local `CLAUDE.local.md` gitignored). Show one power move: `@path` imports (`@docs/git-instructions.md` inlines a file) and `.claude/rules/` with `paths:` frontmatter so heavy instructions only load when Claude touches matching files. Then auto memory: on by default, Claude saves its own learnings to `~/.claude/projects/<project>/memory/MEMORY.md` and reloads them every session, so you see "Saved N memories" / "Recalled N memories" and it gets better at your repo without you writing anything. The `#` shortcut ("remember we use pnpm not npm") versus "add this to CLAUDE.md" (edits the file). `/memory` to view and toggle, `/context` to confirm what actually loaded.
- **Hands-on task:** run `/init`, then cut the generated CLAUDE.md down to three real rules and prove it changes Claude's behavior on the next prompt.
- **Reuse:** CLAUDE.md-as-instruction-manual framing and the "ask Claude to help you write it" beat from `003/script.md` [1:00-2:30]; the auto + manual memory split from `003` [11:45-12:45]; all-features doc sec 2 for the facts.

---

# LESSON 5 - Skills part 1: build your first skill live (0:26 - 0:32) ~6 min

**What it covers:** kill the scary part first. A skill is a folder with one text file, `SKILL.md`: a plain-English description at the top (how Claude decides to use it) plus instructions below. Slash commands and skills are the same thing now, so "custom command" and "skill" mean one idea: a text file that becomes a command. Show a real SKILL.md, point at the description line, then walk the useful frontmatter without going down the rabbit hole (`description`, `allowed-tools`, `user-invocable`, `disable-model-invocation`, `argument-hint`). Then build a brand new one live in about two minutes, invoke it by name, and iterate once by adding a rule and re-running so viewers see the output change. Keep this one a PLAIN skill (instructions only) so the next lesson can level it up with a script.
- **Hands-on task (PROJECT 2):** create `~/.claude/skills/commit-summary/SKILL.md` that takes a git diff and drafts a commit message, using `` !`git diff HEAD` `` to inject the diff. Save it, run it, then add a rule ("group changes by area, flag risks") and re-run.
- **Reuse:** the live 2-minute build and "a skill is a folder with one text file" from `040/script.md` [1:30-2:45] and [11:30-13:30]; the full SKILL.md structure and iterating from `001/script.md` [1:30-10:00] (near-complete footage); all-features doc secs 3-4.

---

# LESSON 6 - Skills part 2: a skill that runs a bundled script (0:32 - 0:38) ~6 min

**What it covers:** the moment skills stop being "fancy prompts" and start doing things a prompt alone cannot. A skill directory can bundle a real script (Python, node, shell) plus reference docs that load only when referenced, and the SKILL.md tells Claude when and how to run it. This is the highest-value skill demo because the payoff is visual. Explain `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PROJECT_DIR}` for resolving bundled paths, and that the body only loads on use so a big reference doc costs almost no context until needed. Build the classic: a codebase-visualizer skill where the SKILL.md instructs Claude to run a bundled Python script that walks the repo and writes an interactive HTML tree, then opens it in the browser. Show the folder layout (`SKILL.md` + `scripts/visualize.py`), run it by name, and open the HTML result on camera. Honest note: a bundled script is code you own, so keep it small and readable, and let `allowed-tools` scope what the skill can run.
- **Hands-on task (PROJECT 3):** create `~/.claude/skills/codebase-map/` with a `SKILL.md` and a `scripts/` file; ask "map this codebase," watch Claude run the script, and open the generated HTML.
- **Reuse:** "skills can do things a prompt alone can't" is all-features Most Demo-Worthy #3 (bundled-script visualizer); the folder-with-reference-file upgrade path from `001/script.md` [1:30-10:00]; `011-3-skills-and-build` and `012-skills-full-course` for deeper skill material; all-features doc sec 4 (supporting files, `${CLAUDE_SKILL_DIR}`).

---

# LESSON 7 - Skills part 3: automate a workflow you actually do (0:38 - 0:43) ~5 min

**What it covers:** the point of the whole skills arc, turn a repeated real chore into one command. This is where beginners feel the "oh, this is for me" click, so pick something genuinely useful and non-code so it lands for everyone: a morning-brief skill that reads a folder or a couple of files and drafts your day, or a content-hook drafter, or a "prep my standup" skill. Teach the two upgrades that make a workflow skill feel like magic: `` !`command` `` to pull live context in (today's date, recent files, a git log) before Claude even reads the skill, and `context: fork` to run heavier skills in an isolated subagent so they do not clog your main window. Reinforce that a workflow skill is a first-class thing you build once and reuse forever, and that this is exactly how Tyler's own channel system is built (dozens of skills, each one a chore he stopped doing by hand).
- **Hands-on task (PROJECT 4):** build a real personal-workflow skill (morning brief, standup prep, or hook drafter) that uses `` !`command` `` to inject live context, run it, and iterate once.
- **Reuse:** the "runs my business, each skill is a chore I automated" framing from `040/script.md` (full) and `042-content-pipeline-11-skills`; the morning-routine build in `044-claude-code-skills-morning-routine/script.md`; `011-3-skills-and-build` for the multi-skill build energy; all-features doc sec 4 (dynamic context injection, `context: fork`).

---

# LESSON 8 - Headless mode: scripting Claude Code (0:43 - 0:48) ~5 min

**What it covers:** the feature that makes Claude Code a Unix citizen, and the one most people have never seen. `claude -p "query"` runs a query, prints the result, and exits, non-interactive, built for scripts and CI. Because it reads stdin and writes stdout, you can pipe into it and chain it. Show `--output-format json` (machine-readable result with cost, usage, and model fields) and mention `--json-schema` to constrain the output shape for downstream tools. Note the guardrails for automation: `--max-turns` and `--max-budget-usd` cap agentic work in `-p` mode, and `claude setup-token` gives you a long-lived token for CI. Show one pipe and one script-file example so they see the range.
- **Hands-on task:** run a real one-liner (`tail -200 app.log | claude -p "summarize any anomalies"` or `git diff main --name-only | claude -p "review these changed files for risks"`), then wrap a `-p` call with `--output-format json` inside a two-line shell script and run it.
- **Reuse:** new footage; all-features doc sec 1 has both example commands ready to show; `022-write-loops-not-prompts` for the scripting mindset.

---

# LESSON 9 - Routines: put Claude Code on a schedule (0:48 - 0:52) ~4 min

**What it covers:** the natural next step after headless, run Claude Code when you are not there. Routines are scheduled cloud agents (cron, GitHub events, or API triggers) that run on Anthropic infrastructure even when your machine is off; create them with `/schedule`. Desktop scheduled tasks are the local flavor (they run on your machine instead). Frame the honest split: a routine in the cloud is great for "every morning, review yesterday's errors and open issues"; a Desktop scheduled task is great for "every evening, run this local script against my files." Combine with Lesson 8: the thing you scheduled is often just a headless `-p` command or a skill you already built. Keep it tight, this is a capability tour plus one real schedule, not a deep dive.
- **Hands-on task:** schedule one real routine with `/schedule` (a daily "summarize my open GitHub issues" or a local nightly cleanup) and confirm it is registered.
- **Reuse:** the scheduling material in `research/youtube/scheduling-tasks-with-claude-code/` (index.md + report.md); the routines-as-content-system framing from `024-claude-routines-content-system/script.txt`; all-features doc sec 18 (Routines, `/schedule`).

---

# LESSON 10 - MCP part 1: connect your first live tool (0:52 - 0:58) ~6 min

**What it covers:** MCP in one line, then one clean live connection. It is an open standard for connecting Claude Code to external tools and data (GitHub, Sentry, Postgres, Notion, Slack, your own servers) so instead of pasting data from another tool into chat, Claude reads and acts on that system directly. Add one remote HTTP server live: `claude mcp add --transport http <name> <url>`, then `claude mcp list` to see health (Connected / Needs auth / Failed), do the one-time OAuth via `/mcp`, and ask a real question. Show the payoff clearly: the tool's data appears in chat with no copy-paste. Keep scopes to one sentence here (local default; project and user covered next lesson). This lesson is the "it works, here is why it matters" version; the next one goes wide and breaks something on purpose.
- **Hands-on task (PROJECT 5):** connect one real tool (GitHub or Sentry) over HTTP and ask it something real, e.g. "summarize my open issues" or "what are the most common errors in the last 24 hours?"
- **Reuse:** the "skills teach Claude how, MCP gives Claude access" line from `003/script.md` [8:45-9:45]; the `claude mcp add ... --transport http` flow from `2026-08-02-arcade-mcp-course-outline.md` (Modules 1-2) and `046/script.md`; all-features doc sec 5.

---

# LESSON 11 - MCP part 2: multiple servers, local vs remote, troubleshooting (0:58 - 1:04) ~6 min

**What it covers:** the depth people actually need once one server works. Connect a SECOND and THIRD server so viewers see a real multi-tool setup (GitHub for code, Sentry for errors, and Tyler's ClickUp for tasks), then ask a question that spans two of them ("cross-reference my top Sentry errors against open GitHub issues"). Teach local vs remote head-on: remote HTTP (`--transport http`, recommended for cloud services, OAuth) versus local stdio (`--transport stdio -- npx -y some-mcp-server`, runs a process on your machine, note the `--` separator and `--env` for keys). Cover scopes properly now: `local` (default, private), `project` (shared via `.mcp.json` committed to the repo, so your team gets the same servers), `user` (all your projects), and precedence. Then troubleshoot a broken connection on camera, the part every tutorial skips: `claude mcp list` shows Failed or Needs auth, use `claude mcp get <name>` to inspect, re-run OAuth with `claude mcp login <name>`, check the transport and URL, and use `--bare` / `--safe-mode` to rule out other config. Honest note: MCP tool calls that run past two minutes auto-move to a background task so the session stays usable.
- **Hands-on task (PROJECT 6):** connect a second and third server, run one cross-server question, commit a `.mcp.json` at project scope, then deliberately break one (bad URL or expired auth), see it go Failed in `claude mcp list`, and fix it.
- **Reuse:** the one-gateway / multi-connection framing from `2026-08-02-arcade-mcp-course-outline.md` (Modules 1-2) and `045-arcade-connect-apps`/`046/script.md`; all-features doc sec 5 (transports, scopes, `claude mcp login`, auto-background).

---

# LESSON 12 - Subagents: Explore, custom agents, and when to delegate (1:04 - 1:10) ~6 min

**What it covers:** how to keep big work from wrecking your context, plus writing your own. A subagent runs in its own context window with its own system prompt and tool restrictions; the main agent delegates via the Task tool and gets back only a summary, so noisy work (searching, log reading, big file dumps) never pollutes your main session. The built-ins: Explore (fast, read-only, search and codebase understanding), Plan (read-only research during plan mode), general-purpose (full tools), plus you can route cheap work to Haiku. Show the `/context` grid before and after delegating a search to Explore so the payoff is visible. Then WRITE a custom agent: they live in `.claude/agents/` as markdown + frontmatter (`name`, `description`, `tools`, `model`, `permissionMode`); the `/agents` wizard was removed, so ask Claude to write the file (show a `code-improver` agent restricted to Read/Grep/Glob). Teach the judgment call out loud, "when to delegate": delegate self-contained, noisy, read-heavy work (searches, log triage, "go understand X and report back"); do NOT delegate the main thread of a task you are actively steering, because the summary loses nuance. As of Week 27 subagents run in the background by default; state whatever is live on filming day.
- **Hands-on task:** delegate a search to Explore ("find everywhere we handle auth and report back"), open `/context` to show the main window stayed clean, then have Claude write a custom `.claude/agents/` file and invoke it.
- **Reuse:** the "separate Claude instances, each its own context window, clean slate" explanation from `003/script.md` [9:45-10:45]; all-features doc sec 6 (built-ins, custom agent frontmatter, foreground vs background).

---

# LESSON 13 - Plan mode, checkpoints, and rewind (1:10 - 1:16) ~6 min

**What it covers:** the two moves that make ambitious changes safe, shown together. Plan mode (Shift+Tab cycles default to acceptEdits to plan, or prefix a prompt with `/plan`): Claude researches and proposes a plan without editing anything, you approve or refine. For anything non-trivial, planning first is the single biggest quality win. Then checkpoints: Claude auto-snapshots your code before each prompt, and `/rewind` (or double-Esc on an empty prompt) opens a menu of every prompt, letting you restore code, conversation, or both. State the honest limits on camera: rewind does NOT undo files changed by bash commands (`rm`, `mv`, `cp`), does not restore background-subagent edits, does not track other-session changes, and skips symlinks. It is local undo, not a replacement for git. Mention `opusplan` (Opus to plan, Sonnet to execute). Note that "summarize from here" (taught in Lesson 3) lives in this same menu.
- **Hands-on task (PROJECT 7):** plan a non-trivial change, let it run, then `/rewind` to snap the code back and show it actually reverted.
- **Reuse:** new footage; the "plan + rewind together, the safety net is the story" demo (all-features Most Demo-Worthy #1); all-features doc secs 8 and 10.

---

# LESSON 14 - Hooks: format-on-edit, block .env, notify (1:16 - 1:22) ~6 min

**What it covers:** deterministic guardrails, shown with three real hooks instead of one. A hook is a shell command Claude Code runs at a fixed lifecycle event, so the thing always happens instead of you hoping the model chooses it, and it uses zero AI tokens. Configured in a `hooks` block in `settings.json`; browse them read-only with `/hooks`. Build all three on camera: (1) a PostToolUse `Edit|Write` hook that auto-formats every edit (the ready-to-show prettier JSON from the doc); (2) a PreToolUse hook that BLOCKS edits to a protected file like `.env` (exit 2 with a message, so Claude is told why and stops); (3) a Stop or Notification hook that fires a desktop notification / sound when a long run finishes so you can walk away. Explain how hooks talk back (exit 0 proceeds, exit 2 blocks and feeds stderr to Claude) and that matchers filter by tool name (`Edit|Write`, `Bash`, `mcp__github__.*`) while the `if` field filters by arguments (`Bash(git *)`). Mention the other hook types exist (http, prompt, agent) without touring all of them, and preview that a `prompt` or `agent` hook can even "run the tests before allowing Stop."
- **Hands-on task (PROJECT 8):** add all three hooks to the demo repo. Make an edit and watch the formatter fire, try to edit `.env` and watch it get blocked, then finish a task and get the notification.
- **Reuse:** the "hooks are deterministic, they always run, they never hallucinate, use them for formatting/logging/validation" framing from `003/script.md` [7:45-8:45]; the hooks research in `research/youtube/claude-code-hooks/` (report.md); the hooks angle notes in `011-3-skills-and-build/hooks.md` style docs; all-features doc sec 7 (example JSON ready to show, full lifecycle list).

---

# LESSON 15 - Permissions, auto mode, and the allowlist deep dive (1:22 - 1:28) ~6 min

**What it covers:** how to go faster without going reckless, with the allowlist taught properly. The permission modes cycled with Shift+Tab: Manual (default, reads only, for sensitive work), acceptEdits (reads plus edits you review after), plan, and auto. Auto mode is the 2026 flagship and deserves the beat: a separate classifier model reviews each risky action before it runs, blocking escalations, `curl | bash`, force push, prod deploys, `rm -rf` on unresolved variables, and secret exfiltration, while letting safe work through (local edits, dependency installs, read-only HTTP, pushes to your branches). It falls back to prompting after repeated blocks. This is how you get long autonomous runs without blanket bypass. Then the manual controls, in depth: permission rules are `allow` / `ask` / `deny` with real syntax (`Bash(git log *)`, `Edit(*.ts)`, `Agent(model:opus)`); `/permissions` manages them; `/fewer-permission-prompts` scans your transcripts and proposes an allowlist you can accept. Explain precedence out loud (deny always wins, even over hook-allow and bypass) and where rules live (`.claude/settings.json` committed vs `.claude/settings.local.json` personal). Protected paths (`.git`, `.claude`, shell rc files, `.mcp.json`, `.npmrc`) are never auto-approved except in bypass. Say the honest line: `bypassPermissions` is for isolated containers only, not your laptop.
- **Hands-on task (PROJECT 9):** turn on auto mode for a longer task and watch it run with far fewer prompts, then run `/fewer-permission-prompts`, read the proposed allowlist out loud, and accept a couple of safe rules into `.claude/settings.json`.
- **Reuse:** the "pre-approve the safe stuff, Claude works faster and you still control anything risky" beat from `003/script.md` [3:45-5:00]; all-features doc sec 11 (auto mode is the headline, permission-rule syntax, precedence). Frame safety honestly, not as magic.

---

# LESSON 16 - Models, thinking, and effort (1:28 - 1:32) ~4 min

**What it covers:** the three dials that change cost and quality, kept practical. Model selection via `/model` (picker or `/model sonnet` directly; Enter saves as default, `s` for session only) or the `--model` flag. The aliases that matter: `sonnet`, `opus`, `haiku`, `fable`, plus `sonnet[1m]`/`opus[1m]` for 1M-token context and `opusplan`. One line on the mid-2026 lineup: Sonnet 5 is the default, Opus 5 for hard work, Fable 5 for long autonomous sessions, Haiku for cheap fast work. Effort levels (`/effort`: low, medium, high, xhigh, max) control adaptive reasoning, how much the model thinks per step; default is high. Then `ultrathink`: type it anywhere in a prompt for deeper reasoning on that one turn without changing your setting (and note that "think hard" and similar phrases are NOT special keywords, a common myth). Mention `/fast` for lower latency and `--fallback-model` for overload.
- **Hands-on task:** run the same non-trivial prompt on Haiku and then Opus, or with and without `ultrathink`, and compare the result quality and cost from `/usage`.
- **Reuse:** the `/model` mid-session switching from `003/script.md` [5:00-6:15]; `041-claude-opus-5` for lineup framing; all-features doc sec 12. Correct the "magic thinking words" myth explicitly, it fits the honest-teacher brand.

---

# LESSON 17 - Image input and web search (1:32 - 1:36) ~4 min

**What it covers:** two built-in inputs people forget Claude Code has. Image input: paste or drag a screenshot (a broken UI, an error, a design mockup, a diagram) into the prompt and Claude reads it, which is the fastest path for "here is the broken screen, fix it" and design-to-code. Web search: the built-in WebSearch tool means Claude searches the live web when a task needs current info (session cap defaults to 200 searches). Web fetch: WebFetch pulls a URL, converts it to markdown, and reads it, great for "read these docs and implement against them." Mention `/deep-research` as the bundled skill that fans out searches and returns a cited report.
- **Hands-on task:** paste a screenshot of a broken or ugly UI and have Claude fix it, then ask a question that forces a live web search and watch it pull current info.
- **Reuse:** new footage; `009-claude-design` and `018-claude-design-5-landing-pages` for design-to-code energy; all-features doc sec 13.

---

# LESSON 18 - Git and GitHub: commits, PRs, worktrees (1:36 - 1:41) ~5 min

**What it covers:** Claude Code as a git-native teammate. In session it stages changes, writes commit messages, creates branches, and opens PRs directly ("commit my changes with a descriptive message," "open a PR against main"). It uses the `gh` CLI for GitHub when available. `/install-github-app` sets up automated PR review and issue triage in CI, and `/code-review [--fix] [--comment] [target]` reviews a diff for real bugs and cleanup; `/diff` opens an interactive diff viewer. Then worktrees as the power move: `claude -w feature-auth` runs parallel sessions in isolated git worktrees so multiple Claudes work on different branches with no interference. The non-negotiable rule to say out loud: always work in a branch, because git is your real undo button (rewind is not).
- **Hands-on task:** let Claude make a change, commit it with its own message, and open a PR; then create a second worktree with `claude -w` and run a parallel task on another branch.
- **Reuse:** the "always work in a Git branch, Claude commits for you, worktrees for parallel sessions" material from `003/script.md` [10:45-11:45] (nearly the whole lesson); all-features doc sec 14.

---

# LESSON 19 - A real refactor and feature project (1:41 - 1:47) ~6 min

**What it covers:** the first big walkthrough, an honest end-to-end on EXISTING code, which is what most viewers actually do all day (not greenfield). Take a small real repo (a messy script, a tiny app, or one of Tyler's channel tools) and do two things back to back: a refactor and a feature add. Show the real professional rhythm: (1) plan mode to have Claude read the code and propose the refactor before touching anything (L13), (2) let it execute under acceptEdits and review the diffs, (3) run the tests / the app to confirm nothing broke, (4) THEN add a new feature on top, (5) commit each step on a branch (L18). This is where you narrate the "70 percent then one correction" habit on real stakes, show a checkpoint save the day when a change goes sideways, and demonstrate reading diffs critically instead of rubber-stamping. The point to land: Claude Code is at its best improving code that already exists, and the discipline (plan, review, test, commit) is what separates a clean refactor from a mess.
- **Hands-on task (PROJECT 10):** refactor a real function/module and then add one feature to it, planning first, reviewing every diff, running it, and committing each step on a branch.
- **Reuse:** structure and stakes from `019-claude-design-rebuild-stripe` (rebuild/refactor energy) and `build-anything-claude-code`; the plan-review-test-commit discipline is your own; all-features doc secs 8, 10, 14.

---

# LESSON 20 - Surfaces: terminal, Desktop, web, phone, and cloud (with teleport) (1:47 - 1:53) ~6 min

**What it covers:** the same engine everywhere, so you are never locked to the terminal, taught as a real lesson instead of a flyby. Walk the three surfaces you will actually live in, and what each one is best for.

- **Terminal (and IDE).** The default and the fastest place to steer: full REPL, every slash command, hooks, worktrees. The VS Code / Cursor extension and the JetBrains plugin are the same engine with inline diffs, @-mentions, and plan review in the editor. Best for: focused, hands-on work where you are driving prompt by prompt.
- **Desktop app** (macOS/Windows, Linux beta). A window instead of a terminal: visual diffs, multiple sessions side by side, an in-app browser, and scheduled tasks that run locally on your machine. `/desktop` (alias `/app`) hands your current terminal session straight to it. Best for: running several sessions at once and watching them, and local scheduled tasks.
- **Web app** (claude.ai/code). No local setup at all: run long and parallel tasks in the browser, on Anthropic's machines, against repos you do not even have cloned locally. Best for: kicking off long autonomous work and checking on it from anywhere.

Then the move that ties them together, cloud and remote sessions with teleport, because this is the "wait, it can do that?" beat. `claude --cloud "fix the login bug"` starts a session in the cloud from your terminal and hands it off; you can watch and steer that same session from the web app or the phone (Claude app on iOS/Android, with push notifications when it finishes, and `claude remote-control` to continue a local session from any browser). When you want it back on your machine, `claude --teleport` pulls the cloud/web session down into your local terminal so you can finish it hands-on. Start in the terminal, continue on the web or your phone, pull it back to the terminal, one session the whole way.

Cover steering background agents here too, since it is the same "watch work you are not driving" muscle: `/tasks` and `claude agents` show every running session (running / blocked on you / done), and you can jump into one to answer a question or redirect it, on any surface. One line on Slack so they know it exists (`@Claude` a bug, get a PR back). The point to land, said out loud: your CLAUDE.md, skills, and MCP config follow you across all of them, so the library you built earlier in this course works everywhere you open Claude Code.
- **Hands-on task:** start a session on ONE surface and continue it on ANOTHER. Concretely: kick off a real task with `claude --cloud "..."` (or hand a terminal session to Desktop with `/desktop`), open that same session in the web app or the phone and steer it a step, then run `claude --teleport` to pull it back into your terminal and finish it. Confirm your skills and CLAUDE.md are right there on every surface.
- **Reuse:** new footage; `005-claude-code-remote-control` for the cross-surface / remote framing; all-features doc sec 15 (five surfaces, `--cloud`, `--teleport`, mobile, remote-control) and secs 9/6 (agent view, background sessions). State whatever is live on filming day (Chrome GA, Desktop-on-Linux beta, teleport).

---

# LESSON 21 - Claude in Chrome: let Claude drive a real browser (1:53 - 1:59) ~6 min

**What it covers:** the surface people do not expect, Claude driving an actual browser. With Claude in Chrome (`claude --chrome`, GA in 2026, backed by the Claude-in-Chrome extension and computer use) Claude opens a real Chrome tab, clicks, types, navigates, and reads the page's console and network, so it can operate a live web app the same way you would. This is different from web fetch (which just reads a URL as text): here Claude is actually using the browser.

Land what it is for with a real demo, not a toy. Two strong options: (1) reproduce and verify a bug, hand Claude a repro path ("go to the staging site, log in with the test account, add an item to the cart, and tell me why the total is wrong"), let it walk the steps in the browser, read the console and network as it goes, find the cause, and after you approve a fix, drive the same steps again to verify it is gone; or (2) automate a repetitive browser chore (pull the same three numbers off a dashboard every morning, fill a recurring form, check a set of pages for a broken element). Show it clicking through on camera.

Teach the safety model honestly, because this one touches live sites: Claude asks before it acts, and you grant permission per site in the extension; it should read freely but pause before anything that writes or is destructive (submitting, deleting, purchasing, sending). Say the rule out loud, do not point it at production and walk away, avoid destructive clicks, use a test account and a staging environment, and keep an eye on it the way you would a new intern with your logged-in browser. Then when to reach for it: a bug that only shows up in the running UI, a task that has no API, or a repetitive click-path you are tired of doing by hand. When there is a clean API or MCP server, prefer that; Chrome is for when the browser IS the interface.
- **Note:** this lesson doubles as a strong standalone video ("I let Claude use my browser") so shoot the demo clean enough to cut on its own.
- **Hands-on task:** point Claude in Chrome at a real (non-production) site and have it do one useful thing end to end: reproduce a known bug and confirm the fix, or automate one repetitive browser task. Grant site permission, watch it ask before it acts, and stop it before any destructive click.
- **Reuse:** new footage; all-features doc sec 15 (Claude in Chrome, computer use) and Most Demo-Worthy #11; state whatever is live on filming day (Chrome GA, computer-use scope). Frame the safety model honestly, not as magic.

---

# LESSON 22 - The Claude Agent SDK: build a tiny agent (1:59 - 2:04) ~5 min

**What it covers:** where Claude Code stops being an app and becomes a library you build ON. The Claude Agent SDK is the same tools, agent loop, and context management that power Claude Code, available in Python and TypeScript so you can build your own agent in your own process. Say the distinction cleanly so nobody gets lost: the CLI is the interactive terminal app for daily use; the Agent SDK is for building production agents with full control over orchestration, tools, and permissions, and it loads the same `.claude/` skills, commands, memory, subagents, hooks, and MCP config you already built in this course. Do not confuse it with the Client SDK (raw Anthropic API, you write the tool loop yourself) or Managed Agents (hosted). Install (`npm i @anthropic-ai/claude-agent-sdk` or `pip install claude-agent-sdk`) and note it needs API-key auth, not a claude.ai login. Build a genuinely tiny agent live (about 20-30 lines): give it a task, let it loop with a tool or two, print the result. Honest note: this is the on-ramp to production, not a full agent-engineering course; keep it to "here is how little code it takes to reuse the same engine in your own program." Also mention the escape hatch, you can drive the same loop from any language by running the CLI as a subprocess with `-p --output-format json`.
- **Hands-on task (PROJECT 11):** write a ~25-line Agent SDK script (Python or TS) that runs a small task end to end, and run it.
- **Reuse:** the first-agent build energy from `038-build-first-ai-agent/script.md` (structure only, that one is a different agent stack); all-features doc sec 17 (Agent SDK vs Client SDK vs Managed Agents, install, subprocess escape hatch). Load the `claude-api` skill before filming to confirm current model ids and SDK details.

---

# LESSON 23 - Common mistakes and troubleshooting (2:04 - 2:09) ~5 min

**What it covers:** the honest lesson that saves people hours, mistakes Tyler sees constantly plus how to diagnose a broken setup. Walk the top mistakes out loud, each with the fix: (1) treating it like chat, dumping a giant vague prompt instead of planning first; (2) never writing a CLAUDE.md, then wondering why it ignores your conventions; (3) letting one session run forever until context rot sets in, instead of `/clear` between tasks; (4) believing "magic thinking words" work (they do not; `ultrathink` is the real one); (5) thinking `/rewind` undoes everything (it does not touch bash `rm`/`mv`, background-subagent edits, or other sessions, so branch in git); (6) reaching for `bypassPermissions` on a real machine instead of auto mode; (7) expecting the `/agents` wizard that was removed (edit the file). Then the diagnostic toolkit: `claude doctor` / `/checkup` for a full setup check, `claude mcp list` for server health, `/context` when it is "acting dumb" (usually a full window), `/status` and `/usage` for what is going on, and the debugging flags `--safe-mode` (disable all customizations) and `--bare` (skip auto-discovery) to isolate whether YOUR config is the problem. Show one real failure and fix it on camera.
- **Hands-on task:** deliberately break something (a bad hook, a full context window, or a failed MCP server), then diagnose and fix it using `claude doctor`, `/context`, and `--safe-mode`.
- **Reuse:** the accuracy corrections (skills=commands, `/agents` removed, thinking-word myth, rewind limits) from the all-features doc note block and secs 6, 10, 11, 12; your honest-teacher brand carries this whole lesson.

---

# LESSON 24 - Power-user workflows (2:09 - 2:14) ~5 min

**What it covers:** the "now that you know the pieces, here is how pros chain them" lesson, a fast tour of high-leverage moves that only make sense once the basics are down. Hit the ones with the best payoff-per-second: background agents (`claude --bg "investigate the flaky test"`) plus the agent view (`claude agents`) to run and watch parallel work on one screen; `/goal` to set a completion condition and let Claude keep working across turns until it holds; `/loop` to repeat a prompt on an interval; a custom status line (`/statusline`) and output styles (a Proactive style for more autonomous behavior); plugins (`/plugin`) to package skills, subagents, hooks, and MCP servers together and share them with a team; the advisor tool (`--advisor opus`) to escalate hard calls to a stronger model; and `/focus` / session recap to stay oriented in a long session. The thread to pull: every one of these is a force multiplier on things you already learned, not a new concept to fear. Show two or three chained live rather than listing all of them.
- **Hands-on task (PROJECT combo):** kick off a background agent while you keep working in the foreground, watch both in `claude agents`, and set a `/goal` on one task so it runs to a defined finish.
- **Reuse:** the "write loops not prompts" mindset from `022-write-loops-not-prompts/script.md`; the multi-skill/multi-agent pipeline energy from `042-content-pipeline-11-skills` and `043-jarvis-that-learns`; all-features doc secs 9 (background agents), 16 (status line, output styles, plugins), 18 (`/goal`, advisor, `/focus`).

---

# LESSON 25 - CAPSTONE: a real multi-part build, end to end (2:14 - 2:23) ~9 min

**What it covers:** tie the whole course together on one real, multi-part deliverable, from an empty folder to working and committed, using the full chain in order. Make it bigger than v1: not one artifact but a small SYSTEM with two or three connected parts, so the capstone earns its length and shows the pieces working together. Good candidate for Tyler: a mini content-ops helper, e.g. (a) a skill that drafts a post from a transcript, (b) a headless script that runs it over a folder, and (c) a routine that fires it on a schedule, with an MCP tool pulling real data and hooks keeping it clean. The sequence, each step calling back to a lesson: set a tight CLAUDE.md (L4), plan the whole build in plan mode (L13), execute under auto mode with a format hook enforcing style (L14, L15), build the skill and give it a bundled helper if needed (L5-L7), wire in one MCP tool for real data (L10-L11), lean on checkpoints as the safety net (L13), schedule the finished piece as a routine (L9), and finish with Claude committing it through git on a branch and opening a PR (L18). Show the finished system running end to end. Narrate the "70 percent then one correction" rhythm the whole way so beginners see steering is normal, and keep the project genuinely useful so the footage doubles as a standalone video.
- **Hands-on task (PROJECT 12, the capstone):** ship one real multi-part system (skill + headless script + routine, with an MCP tool and hooks) from empty folder to working, committed on a branch, and scheduled, exercising CLAUDE.md, plan mode, auto mode, skills, MCP, checkpoints, and git.
- **Reuse:** structure mirrors the real "runs my business" system in `040/script.md` (full) and the multi-skill pipeline in `042-content-pipeline-11-skills` without re-teaching the individual pieces; keep the project genuinely useful so it stands alone.

---

# LESSON 26 - The production checklist: secrets, errors, logging, config (2:23 - 2:35) ~12 min

**What it covers:** the gap between "it ran once on my machine" and "it can run without me watching it," taught as the boring pass nobody films but everybody needs. Take something real you already built in this course (the capstone system, a skill's bundled script, or the Agent SDK agent) and walk four things on camera, each shown as a diff on that code:
1. **Secrets and env.** Never hardcode a key or token. Pull them from environment variables, keep a gitignored `.env` locally and set the real values in the host's env settings in production. Reinforce the block-`.env` hook from L14 so a key never gets committed by accident, and that auto mode blocks secret exfiltration (L15). Say the honest line: a leaked key is a real incident, so treat keys like keys.
2. **Error handling.** The happy path is not enough. Have Claude add real try/except (or try/catch), sensible exit codes, and a clear message when something upstream is down, so a failed run tells you WHY instead of dying silent.
3. **Logging.** A run should leave a trail. Write a timestamped line per run (started, what it did, succeeded or failed) to a file or to stdout the host captures, so you can answer "did it run last night, and what happened."
4. **Config.** Pull the things you will want to change (the schedule, folder paths, thresholds, the model) out of the code into a small config file or env vars, so tuning it later is not surgery on your logic.

The framing to land: this is the unglamorous part that separates a demo from something you trust to run alone, and Claude Code is good at it. Ask Claude for a "production-readiness pass" and then read its changes critically instead of rubber-stamping, because this is the code that runs when you are not there.
- **Hands-on task:** take one thing you built earlier and have Claude do a single production-readiness pass: move every secret to env vars, add error handling and a run log, and pull config out of the code. Review every diff.
- **Reuse:** the block-`.env` hook from `003/script.md` [7:45-8:45] and L14; the auto-mode secret/exfil protection from L15; all-features doc secs 7 (hooks) and 11 (auto mode blocks secret exfiltration); the "boring but load-bearing" framing is your own honest-teacher brand.

---

# LESSON 27 - Ship it live: put it in the world, running on its own (2:35 - 2:51) ~16 min

**What it covers:** the payoff of the whole course, take ONE real thing and make it genuinely RUN LIVE, unattended, then prove it runs and keep an eye on it. Two paths; demo one end to end and describe the other so viewers pick the one that fits what they built.

- **Path A, deploy a small app or tool to a real host.** Something Claude Code built (a small web app, an API, a tool with a URL) goes to Railway, Vercel, Fly, or Cloudflare. The rhythm: let Claude add the deploy config the host expects, set the real env vars in the host's dashboard (the keys from L26, never in git), push, and get a live URL you can open on your phone. Honest notes said out loud: this costs real money (name the free tier and exactly where it ends), the keys are real (rotate them if they ever leak), and things break (a build that passes locally can fail in the host's environment, so read the deploy log instead of guessing).
- **Path B, ship a skill or agent that runs on a schedule.** The thing you built runs on its own on a timer: a Routine in the cloud (`/schedule`, runs on Anthropic infrastructure even when your laptop is closed, L9), or a Desktop scheduled task / a plain cron job that fires a headless `claude -p` command or a skill you already built (L8, L9). Best for "every morning, do X and save or send the result." Honest note: a cloud routine and a local cron behave differently, a job that needs a local file has to run where that file lives, so know which one you picked and why.

Then, whichever path you took, the two things people skip:
- **Verify it actually runs live.** Open the URL, or trigger and wait out the first real scheduled run, and confirm it did the thing, not just that it deployed. Deployed is not the same as working.
- **Basic monitoring.** Keep the run log from L26 that the host or the routine writes to, and wire ONE cheap alert so a failure reaches you: a Slack or email line from a headless `claude -p` step (the "Slack me if you see anomalies" pattern), or a notification. You do not need an observability stack, you need to find out it broke without staring at it.

Close on the honest operations reality: know your costs, keep your keys out of git, know what can break, and know how you would roll back (redeploy the last good version, or turn the schedule off). Say it plainly, shipping is not the finish line, it is the start of owning something that runs.
- **Note:** this doubles as a strong standalone video ("I deployed what Claude Code built and left it running"), so shoot the live demo clean enough to cut on its own.
- **Hands-on task (PROJECT 13):** deploy ONE real thing so it is genuinely running in the world, either a small app or tool on a real host with a live URL and real env vars, or a skill/agent on a schedule that fires on its own. Verify the first live run, add a run log and one cheap alert, and write down what it costs, what could break, and how you would roll it back.
- **Reuse:** new footage; the headless `-p` alert pattern is all-features Most Demo-Worthy #5 ("Slack me if you see anomalies"); routines from L9 and all-features doc sec 18; secrets and env handling carried over from L26. State the current host free tiers and the current routine cloud-vs-local behavior on filming day.

---

# LESSON 28 - Your skills and agents library: what you keep (2:51 - 2:56) ~5 min

**What it covers:** the payoff of the whole course, said out loud, you are not leaving with a video you watched, you are leaving with a working toolkit you built. This lesson exists to make the promise real: everything you made along the way (the three skills, the custom agent, the hooks, the MCP setup, the routine) was a real, reusable thing, not a throwaway demo, and now you collect it into one library you can run forever.

Walk it on camera. First, take inventory: `/skills` lists what you have, `/agents` (or opening `.claude/agents/`) shows your agents, and `/context` proves what actually loads. Then organize it so it lasts:
- **Personal library, used everywhere:** `~/.claude/skills/<name>/SKILL.md` for skills and `~/.claude/agents/<name>.md` for agents live at the user scope, so they follow you into every project and every surface (terminal, Desktop, web, the SDK).
- **Project library, shared with a team:** `.claude/skills/` and `.claude/agents/` committed to a repo, so anyone who clones it gets the same commands, plus a `CLAUDE.md`, a committed `.mcp.json`, and `.claude/settings.json` hooks. Mention `/plugin` as the way to bundle skills, agents, hooks, and MCP servers into one shareable package when you want to hand the whole kit to someone.

Then the honest promise about keeping it alive: this library is never finished, and that is the point. The rule to say plainly, every task you do twice becomes the next skill. When you catch yourself doing something by hand a second time, that is the signal to spend five minutes turning it into a skill or an agent, exactly the way you built the three in this course. That is how Tyler's own channel system grew from zero to dozens of skills, one automated chore at a time. Close the loop with the intro promise, out loud: you were told you would leave with a folder of skills and agents you actually use every day, and here it is, open on screen, yours to keep and keep growing.
- **Hands-on task:** open `~/.claude/skills/` and `~/.claude/agents/` and confirm every skill and agent you built in this course is sitting there. Tidy the names, make sure the personal ones live at the user scope so they follow you, and pick ONE more chore from this week to turn into the next skill before you close the course.
- **Reuse:** the "each skill is a chore I stopped doing by hand, this runs my whole business" framing from `040/script.md` (full) and `042-content-pipeline-11-skills`; the "every task you do twice becomes a skill" line is your own recurring beat; all-features doc secs 4 (skill locations), 6 (agent locations), 16 (plugins). No re-teaching of the pieces, this is the collect-and-keep lesson.

---

# OUTRO (2:56 - 3:00) ~4 min

### Recap and where to go next (2:56, 4 min)
Zoom out: you installed and drove Claude Code, learned to manage context, gave it a CLAUDE.md and memory, built three real skills (including one with a bundled script and one that automates a chore you actually do), ran it headless and on a schedule, connected multiple live tools over MCP and troubleshot one, delegated to subagents and wrote your own, planned and rewound changes, added real hooks, ran under auto mode with a tuned allowlist, tuned model and effort, used images and web search, refactored real code and shipped a feature, built a tiny agent with the SDK, ran the same engine across the terminal, Desktop, web, and phone and teleported a session between them, let Claude drive a real browser in Chrome, learned the common mistakes and the power-user moves, shipped a real multi-part system, ran a production-readiness pass and deployed one real thing so it is running live and unattended, and collected everything into one keepable library. That is not a feature list, it is a working practice. Say the promise landed, out loud: you came in to watch a course and you are leaving with a folder of skills and agents you actually use every day, and it keeps growing every time you automate the next chore. Reinforce the mental model one last time: one engine, many surfaces, your config and your library follow you. Then one clear action, not the whole system: pick ONE task you do every week and turn it into the next skill in that library this week. Point to the starter skills, the CLAUDE.md examples, and the community/newsletter (free.tylerai.dev/youtube). Comment prompt: what is the first thing you will build a skill for. Tease the deeper single-topic courses (the skills full course, the MCP/agent build, Cowork for the no-code path) for anyone who wants to go further, framed as optional next steps, not a cliffhanger.
- **Reuse:** recap-then-single-action structure from `040/script.md` [13:30-end] and `003/script.md` [12:45-13:30]; keep actual CTA under about 90 seconds.

---

# The hands-on projects (13 build-something projects across the course)

1. **Fix a bug / add a feature and run it** (Lesson 2) - the core chat/edit/run loop in a throwaway repo, ending in the "70 percent then one correction" habit.
2. **Skill #1, a plain skill built live** (Lesson 5) - `~/.claude/skills/commit-summary/SKILL.md` that drafts a commit message from `` !`git diff HEAD` ``, then iterate once.
3. **Skill #2, a skill with a bundled script** (Lesson 6) - `~/.claude/skills/codebase-map/` with a Python script that generates an interactive HTML map; run it and open the result.
4. **Skill #3, automate a workflow you actually do** (Lesson 7) - a morning-brief / standup-prep / hook-drafter skill that injects live context with `` !`command` ``.
5. **Connect an MCP tool and query it** (Lesson 10) - one remote HTTP server (GitHub or Sentry), asking a real question against live data.
6. **Multi-server MCP + troubleshoot** (Lesson 11) - a second and third server, one cross-server question, a committed `.mcp.json`, then break one and fix it.
7. **Plan then rewind a change** (Lesson 13) - plan a non-trivial change, run it, `/rewind` to snap it back.
8. **A hooks bundle** (Lesson 14) - format-on-edit, block-`.env`, and a finish notification, all firing live.
9. **Run a task under auto mode + build an allowlist** (Lesson 15) - a longer task with far fewer prompts, plus accepting `/fewer-permission-prompts` rules.
10. **Refactor real code and add a feature** (Lesson 19) - plan, execute, review diffs, test, and commit each step on a branch.
11. **Build a tiny Agent SDK agent** (Lesson 22) - a ~25-line Python/TS script that reuses the same engine in your own process.
12. **Capstone: a real multi-part system** (Lesson 25) - skill + headless script + routine, with an MCP tool and hooks, from empty folder to working, committed on a branch, and scheduled.
13. **Deploy one real thing so it runs live** (Lesson 27) - take something you built and ship it unattended: either a small app/tool to a real host (Railway/Vercel/Fly/Cloudflare) with a live URL and real env vars, or a skill/agent on a schedule; verify the first live run, add a run log and one cheap alert, and write down the costs, the failure modes, and the rollback plan.

Smaller in-lesson tasks (not counted as the 13 projects but shot on camera): install + first prompt (L1), read the `/context` grid and clear it (L3), `/init` and tighten CLAUDE.md to three rules (L4), a headless one-liner + a `-p` script (L8), schedule one routine (L9), delegate to Explore and write a custom agent (L12), compare models / `ultrathink` (L16), screenshot-to-fix and a live web search (L17), a git commit + PR + a second worktree (L18), start a session on one surface and continue it on another with `--teleport` (L20), let Claude in Chrome reproduce a bug or automate a browser chore (L21), diagnose and fix a broken setup (L23), a background agent + `/goal` combo (L24), run a production-readiness pass on real code (L26), collect your skills and agents into one keepable library (L28).

---

# Reusable-footage map (so Tyler does not re-shoot everything)

| Lesson | Reuse from |
|---|---|
| Intro (cold open + mental model) | 003 [0:00-0:35], 040 [0:00-0:35], all-features sec 0 |
| 2 basics (chat/edit/run) | 003 [2:30-3:45]; "70 percent then one correction" is your own line |
| 3 context management | 003 [2:30-3:45], [5:00-6:15]; all-features secs 10, 18 |
| 4 CLAUDE.md + memory | 003 [1:00-2:30], [11:45-12:45]; all-features sec 2 |
| 5 skill #1 (plain, live) | 001 [1:30-10:00] (near-complete), 040 [1:30-2:45] + [11:30-13:30] |
| 6 skill #2 (bundled script) | all-features demo #3; 011-3-skills-and-build, 012-skills-full-course; all-features sec 4 |
| 7 skill #3 (personal workflow) | 040 (full), 042-content-pipeline-11-skills, 044-morning-routine, 011-3-skills-and-build |
| 8 headless | new footage; all-features sec 1; 022-write-loops-not-prompts |
| 9 routines/schedule | research/scheduling-tasks-with-claude-code; 024-claude-routines-content-system; all-features sec 18 |
| 10 MCP part 1 | 003 [8:45-9:45], arcade-mcp-course-outline Mod 1-2, 046 [0:45-2:30] |
| 11 MCP part 2 (multi + troubleshoot) | arcade-mcp-course-outline Mod 1-2, 045-arcade-connect-apps, 046; all-features sec 5 |
| 12 subagents (+ custom agents) | 003 [9:45-10:45]; all-features sec 6 |
| 13 plan/checkpoint/rewind | new footage; all-features secs 8, 10 |
| 14 hooks (three examples) | 003 [7:45-8:45]; research/claude-code-hooks; all-features sec 7 |
| 15 permissions + auto mode + allowlist | 003 [3:45-5:00]; all-features sec 11 |
| 16 models/thinking/effort | 003 [5:00-6:15]; 041-claude-opus-5; all-features sec 12 |
| 17 image input + web search | new footage; 009/018 design packages; all-features sec 13 |
| 18 git + PRs + worktrees | 003 [10:45-11:45]; all-features sec 14 |
| 19 refactor + feature project | 019-rebuild-stripe, build-anything-claude-code; all-features secs 8,10,14 |
| 20 surfaces (terminal/Desktop/web/phone/cloud + teleport) | new footage; 005-claude-code-remote-control; all-features sec 15 (+ secs 6,9) |
| 21 Claude in Chrome | new footage; all-features sec 15 + demo #11; doubles as a standalone video |
| 22 Agent SDK | 038-build-first-ai-agent (structure only); all-features sec 17; load `claude-api` skill |
| 23 mistakes + troubleshooting | all-features note block + secs 6,10,11,12; your own brand |
| 24 power-user workflows | 022-write-loops-not-prompts, 042, 043-jarvis-that-learns; all-features secs 9,16,18 |
| 25 capstone | 040 (full), 042 (multi-skill); structure only |
| 26 production checklist (secrets/errors/logging/config) | new footage on real code; L14/L15 callbacks; all-features secs 7, 11 |
| 27 ship it live (deploy app or schedule agent) | new footage; all-features demo #5 (`-p` alert), sec 18 (routines); doubles as a standalone video |
| 28 skills + agents library (what you keep) | 040 (full), 042-content-pipeline-11-skills; "every task you do twice becomes a skill" is your own line; all-features secs 4,6,16 |
| Outro | 040 [13:30-end], 003 [12:45-13:30] |

# Sources
- `research/youtube/2026-08-02-all-claude-code-features.md` (feature accuracy, v2.1.x, mid-2026)
- `research/youtube/2026-08-04-claude-mega-course-outline.md` (this expands its Part 1 into a standalone)
- `research/youtube/2026-08-02-arcade-mcp-course-outline.md` (one-gateway MCP framing)
- `research/youtube/scheduling-tasks-with-claude-code/` and `research/youtube/claude-code-hooks/` (routines + hooks research)
- Packages: `youtube/videos/001-build-claude-code-skill`, `003-claude-code-beginner-concepts`, `005-claude-code-remote-control`, `011-3-skills-and-build`, `012-skills-full-course`, `019-claude-design-rebuild-stripe`, `022-write-loops-not-prompts`, `024-claude-routines-content-system`, `038-build-first-ai-agent`, `040-claude-code-skills-run-my-business`, `041-claude-opus-5`, `042-content-pipeline-11-skills`, `043-jarvis-that-learns`, `044-claude-code-skills-morning-routine`, `045-arcade-connect-apps`, `046-arcade-build-agent`, `build-anything-claude-code`
