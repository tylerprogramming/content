# Master Recording Plan - Three Standalone Courses

**Compiled:** 2026-08-04 (rebuilt after all three outlines were expanded)
**Covers:** Claude Code (~3:00, 28 lessons), Cowork (~2:24, 21 modules + 2 capstones), Build AI Agents (~2:20, 20 lessons)
**Purpose:** one plan Tyler films from. Each course table classifies every section as RECORD NEW or REUSE straight from that section's reuse note. Then a batch-film shot list, a reuse pull-list, and a demo-asset staging list.

**How the classification was made:** the label comes from each lesson's reuse note. A section is REUSE only when the note points to a real shot package with a timestamp or a "direct from / full build / near-complete" clip that covers the section's main content. A section is RECORD NEW when the note says "new footage," "new demo-assets," "net-new," "structure only," cites only another outline, or reuses prior material only as framing / energy / a beat (ambiguous coverage, so treated as new per the plan rule).

**What changed in this rebuild:** the Claude Code course grew from 24 to 28 lessons (now ~3:00). The surfaces lesson (L20) became a real teardown of terminal / Desktop / web / phone / cloud with teleport. A dedicated Claude in Chrome lesson (L21) was added. A two-lesson deploy-to-production block was added before the wrap: the production checklist (L26) and ship-it-live (L27). A closing "Your skills and agents library" wrap (L28) is now the last lesson. All four new Claude Code lessons are RECORD NEW. Cowork gained one module, M21 "Build your own Cowork skill (no code)," also RECORD NEW. Build AI Agents is unchanged.

**Sources reused most:** package 003 (Claude Code beginners), 040 (skills run my business), 001 (build a skill), 023 (Cowork full course), 038 (build first agent), 046 (Arcade build agent).

---

## COURSE 1 - CLAUDE CODE

| Section | NEW / REUSE | Source package + timestamp | Notes / demo assets |
|---|---|---|---|
| INTRO (cold open + mental model) | REUSE | 003 [0:00-0:35], 040 [0:00-0:35], all-features sec 0 | Mental-model diagram may need a fresh beat over reused cold open. |
| L1 Install, setup, first launch | RECORD NEW | new footage | Throwaway repo to open; run `claude "explain this codebase"`. |
| L2 Basics: chat, edit, run (REPL) | REUSE | 003 [2:30-3:45] | Throwaway repo with a small bug/feature (Project 1). |
| L3 Context management | REUSE | 003 [2:30-3:45], [5:00-6:15]; all-features 10, 18 | `/rewind` summarize-from-here beat is new, film that slice. |
| L4 CLAUDE.md and memory | REUSE | 003 [1:00-2:30], [11:45-12:45] | Run `/init` on a real repo, cut to 3 rules. |
| L5 Skills part 1 (plain skill, live) | REUSE | 001 [1:30-10:00] near-complete, 040 [1:30-2:45], [11:30-13:30] | commit-summary skill (Project 2). |
| L6 Skills part 2 (bundled script) | REUSE | 001 [1:30-10:00], 011, 012 | Codebase-map Python-script visualizer run is fresh capture; flag. |
| L7 Skills part 3 (personal workflow) | REUSE | 040 (full), 044, 042, 011 | Morning-brief / standup / hook drafter skill (Project 4). |
| L8 Headless mode | RECORD NEW | new footage | Real one-liner pipe + a `-p --output-format json` script. |
| L9 Routines / schedule | RECORD NEW | 024 framing only, research/scheduling docs | `/schedule` demo is fresh; needs a repo to schedule against. |
| L10 MCP part 1 (first live tool) | REUSE | 046 [0:45-2:30], 003 [8:45-9:45] | GitHub or Sentry over HTTP (Project 5). |
| L11 MCP part 2 (multi + troubleshoot) | REUSE | 045, 046 | 2nd/3rd server + break-and-fix is partly fresh; flag. Need GitHub+Sentry+ClickUp connected. |
| L12 Subagents (+ custom agents) | REUSE | 003 [9:45-10:45] | Writing the custom `.claude/agents/` file is fresh; flag. |
| L13 Plan, checkpoints, rewind | RECORD NEW | new footage | Plan a non-trivial change, then `/rewind` (Project 7). |
| L14 Hooks (three examples) | REUSE | 003 [7:45-8:45], research/claude-code-hooks | 3-hook build is partly fresh; need a `.env` protected file (Project 8). |
| L15 Permissions, auto mode, allowlist | REUSE | 003 [3:45-5:00] | Auto-mode + `/fewer-permission-prompts` deep dive partly fresh; flag. |
| L16 Models, thinking, effort | REUSE | 003 [5:00-6:15], 041 | Same prompt on Haiku vs Opus / ultrathink. |
| L17 Image input and web search | RECORD NEW | new footage | Screenshot of a broken UI to paste; a query that forces web search. |
| L18 Git and GitHub (commits, PRs, worktrees) | REUSE | 003 [10:45-11:45] nearly whole lesson | Commit + PR + a `claude -w` worktree. |
| L19 Refactor and feature project | RECORD NEW | 019, build-anything (structure/energy only) | Fresh end-to-end run. Need a messy script/app/tool to refactor (Project 10). |
| L20 Surfaces (terminal/Desktop/web/phone/cloud + teleport) | RECORD NEW | new footage; 005-remote-control | Expanded lesson. Same project across surfaces; `--cloud` then `--teleport` a session back. Needs Desktop app + web + phone signed in. |
| L21 Claude in Chrome (drive a real browser) | RECORD NEW | new footage; all-features sec 15 + demo #11 | NEW lesson, doubles as a standalone video. Non-prod/staging site + test account + a reproducible bug. |
| L22 Agent SDK (tiny agent) | RECORD NEW | 038 structure only, different stack | ~25-line Python/TS build (Project 11). Needs API-key auth; load `claude-api` skill. |
| L23 Common mistakes and troubleshooting | RECORD NEW | doc corrections + own brand, no footage | Break a setup on purpose, diagnose with `claude doctor` / `--safe-mode`. |
| L24 Power-user workflows | RECORD NEW | 022, 042, 043 (mindset/energy only) | Chained live demo is fresh (background agent + `/goal`). |
| L25 CAPSTONE: multi-part build | RECORD NEW | 040, 042 (structure only) | Fresh full build: skill + headless script + routine + MCP + hooks (Project 12). |
| L26 Production checklist (secrets, errors, logging, config) | RECORD NEW | new footage on real code; L14/L15 callbacks | NEW lesson. Take the capstone system or the SDK agent and do one production-readiness pass, shown as diffs. Needs real code with a secret to move to env. |
| L27 Ship it live (running on its own) | RECORD NEW | new footage; all-features demo #5, sec 18 | NEW lesson, doubles as a standalone video. Deploy ONE thing: a small app/tool to a real host with a live URL, OR a skill/agent on a schedule (Project 13). Needs a host account + a deployable app; verify first live run + one alert. |
| L28 Your skills and agents library (what you keep) | RECORD NEW | 040, 042 (framing only); all-features 4, 6, 16 | NEW wrap lesson. Live inventory (`/skills`, `/agents`, `/context`) + organize personal vs project scope + `/plugin`. Only framing reused, so film the walkthrough. |
| OUTRO | REUSE | 040 [13:30-end], 003 [12:45-13:30] | Recap + single action. |

**Claude Code: 15 RECORD NEW, 15 REUSE.**

---

## COURSE 2 - COWORK

| Section | NEW / REUSE | Source package + timestamp | Notes / demo assets |
|---|---|---|---|
| INTRO (cold open + who-for) | REUSE | 021 sec 1, 023 INTRO first-30s | Keep intro short. |
| M1 What Cowork is + mental model | REUSE | 021 secs 4-5, 030, 023 INTRO | Brain-vs-hands, one diagram. |
| M2 Install + folder/permission model | REUSE | 023 Module 1 | about-me interview (Project 1). |
| M3 Core loop | REUSE | 023 Module 2 closing beat | The 70-percent-then-one-correction rhythm. |
| M4 Organize a messy folder | REUSE | 023 Module 2 Demo 2A | Assets staged: 023 demo-assets/messy-client-folder. |
| M5 Receipts/screenshots/notes to sheet | REUSE | 023 Module 2 Demo 2B | Assets staged: 023 demo-assets/receipts. Add screenshots + typed notes as variants. |
| M6 Batch-rename and sort a media pile | RECORD NEW | new demo-assets/media-pile, mirrors M4 | Stage a chaotic mixed-filename folder; plan-first dry run. |
| M7 Clean and merge messy data | RECORD NEW | new demo-assets/dirty-data | Two messy CSVs; can seed one from 023 analytics CSVs. |
| M8 Summarize a stack of PDFs | RECORD NEW | new demo-assets/pdf-stack | 4-6 public sample PDFs with a buried date/clause. |
| M9 Draft documents from source files | RECORD NEW | transcripts/ inputs only (no footage) | Pick a non-sensitive transcript as source. |
| M10 Generate a deliverable (proposal/one-pager) | RECORD NEW | new demo-assets/proposal-inputs | Scope notes, placeholder pricing, past proposal, brand note. No real prices on camera. |
| M11 Research to recommendations | REUSE | 023 Module 4 Demo 4A/4B | Assets staged: 023 demo-assets/analytics. |
| M12 A weekly report | REUSE | 023 Module 4 analytics + report format | Format seeds the M17 routine and the M21 skill. |
| M13 Memory: train it on you and your voice | REUSE | 023 Module 3 (+ Demo 3) | CLAUDE.md build, then re-run an earlier task (Project 11). |
| M14.1 How connectors work + boundary | REUSE | 023 Module 5 | The ask-first / revoke line. |
| M14.2 Gmail connect and read | REUSE | 023 Module 5 Demo 5A setup half | Blur sensitive subjects. |
| M14.3 Drive cross-reference | REUSE | 023 Module 5 Demo 5B | Two sources at once. |
| M14.4 Notion connector | RECORD NEW | new short demo | Need a Notion workspace/database with sample tasks or a page. |
| M14.5 Custom MCP connector | RECORD NEW | arcade outline Module 2 (outline only, no footage) | Need a public MCP/Gateway URL + OAuth (Project 12). |
| M15 Inbox triage with drafts | REUSE | 023 Module 5 Demo 5A payoff half | Draft only, send nothing. |
| M16 Calendar and meeting prep | RECORD NEW | arcade outline example #5 (outline only) | Need a real upcoming event + related emails/files. |
| M17 Scheduled tasks and routines (17.1-17.4) | REUSE | 023 Module 8 | Reuse the M12 weekly report on a timer; CSVs staged. |
| M18 Creator / small business / student | REUSE | maps to M4/M5/M7/M8/M9/M10/M12/M15 | No new core footage; recombines existing demos. |
| M19 Common mistakes + troubleshooting | RECORD NEW | net-new module | Talking-head checklist; strong standalone short. |
| M20 Cowork vs Code vs Chat | REUSE | 023 Module 9 | The decision rule. |
| M21 Build your own Cowork skill (no code) | RECORD NEW | new footage; callbacks to M12/M13/M17/M20 | NEW module. Save the M12 weekly report as a named no-code skill, run it by name, correct once, keep it (Project 16). Reuses M12 inputs; no new asset needed. State current Cowork saved-skill behavior on filming day. |
| CAPSTONE A - personal: inputs to a decision | RECORD NEW | combines M5+M7+M13, receipts seed | Fresh end-to-end run; pick a real personal job (Project 17). |
| CAPSTONE B - business: repeatable operation | RECORD NEW | structure mirrors 023 Mods 3/4/8 | Fresh run + schedule. Need competitor transcripts + analytics + notes + a Drive doc (Project 18). |
| OUTRO + 7-day plan | REUSE | 023 Module 10 + OUTRO | Keep CTA tight. |

**Cowork: 12 RECORD NEW, 17 REUSE.**

---

## COURSE 3 - BUILD AI AGENTS

| Section | NEW / REUSE | Source package + timestamp | Notes / demo assets |
|---|---|---|---|
| INTRO (cold open) | REUSE | 046 [0:00-0:15], 038 cold open | Result-first: finished morning-brief on screen. |
| L1 What an agent actually is | REUSE | 038 [0:20-1:30] | Add the new "model in a loop" line over reused footage. |
| L2 When to build (or not) | RECORD NEW | new; rhymes with mega-course 2.8 | Label one weekly task script/prompt/agent (Project 1). Talking head. |
| L3 The agent loop in detail | RECORD NEW | new footage | Diagram + narration reused later over L8/L9 runs. Talking head. |
| L4 Tools, MCP, and the auth problem | REUSE | 046 [0:15-2:30], arcade outline Mods 1-2 | Two-tool Gateway (Gmail+Calendar) + OAuth (Project 2). Disclosure if sponsored. |
| L5 Tool design | RECORD NEW | new footage | Point at the connected Gateway tools; write a one-line brief. Talking head. |
| L6 Memory: short vs long-term | RECORD NEW | new footage | Write a tight memory file (name, voice, 2 rules) (Project 3). |
| L7 Self-verification and evals | RECORD NEW | new footage | Live on the research agent; write 3 evals (normal/edge/refuse) (Project 4). |
| L8 Agent 1: research-brief, no code | REUSE | 038 [1:30-8:00] full live build | Copy-pack exists. Narrate the L3 loop over it. |
| L9 Agent 2: morning-brief, end to end | REUSE | 046 [2:30-8:00] full | Exactly that agent + prompt. Cut a timed short from it. Real inbox+calendar (blur). |
| L10 Agent 3: inbox triage | RECORD NEW | 038 [8:00-9:15] framing beat only | Full live triage run is fresh. Gmail tool. |
| L11 Agent 4: research assistant + artifact | RECORD NEW | builds on L8+L7, now its own build | Add save-to-doc via Drive/Docs tool (Project 8). |
| L12 Agent 5: repo triage to ClickUp | RECORD NEW | arcade outline walkthrough 3 (outline only) | Need a repo with issues/PRs + ClickUp MCP fallback (Project 9). |
| L13 Agent 6: content-repurposing | RECORD NEW | new footage | Real transcript source; drafts saved not posted (Project 10). Voice file from L6. |
| L14 Agent 7: support / FAQ | RECORD NEW | new footage | Need a FAQ/help-doc source of truth; prove refuse-out-of-scope (Project 11). |
| L15 Agent 8: scheduled monitoring | RECORD NEW | 040 [6:30-9:30] as example only | Fresh build. Pick something to watch; run twice to prove the diff (Project 12). |
| L16 Frameworks (Pydantic AI, LangGraph, Agent SDK) | RECORD NEW | new footage | Rebuild the L8 agent, same instructions/tool. Python/TS env; load `claude-api` skill (Project 13). |
| L17 Multi-agent and orchestration | RECORD NEW | new footage | Uses L11/L13 research-write-check chain as the example. Talking head + demo. |
| L18 Where agents fail + safety | REUSE | 038 [9:15-10:30], 046 [8:00-9:00] | Failure stories tie to L7/L10/L11. |
| L19 Deploy, schedule, monitor, cost | RECORD NEW | 023 Mod 8 discipline + 040 [6:30-9:30]; cost is new | Schedule an agent, run log, per-run cost + one guardrail (Project 14). |
| L20 Running an agent as a paid service | RECORD NEW | 046 [8:00-9:00] governance; scoping/pricing/maintaining new | One-page scope for a real agent (Project 15). Talking head. |
| OUTRO | REUSE | 038 [10:30-12:15], 046 CTA | Recap + single action. |

**Build AI Agents: 15 RECORD NEW, 7 REUSE.**

---

## SYNTHESIS 1 - RECORD FRESH: master shot list (batch by setup)

Film these in three camera setups. Talking-head-only lessons are grouped so they shoot back to back without changing the rig. 42 fresh sections total.

### SETUP A - Claude Code terminal (15 fresh sections)
Sit in the terminal / repo for the whole block. A few of these leave the terminal (Desktop/web/phone, the browser, a deploy host), flagged inline, so stage those before the block.

Build/demo lessons:
- CC L1 - install + first launch (throwaway repo)
- CC L8 - headless: a pipe one-liner + a `-p --output-format json` script
- CC L9 - routines: schedule one job with `/schedule`
- CC L13 - plan mode, checkpoints, `/rewind` a non-trivial change
- CC L17 - paste a broken-UI screenshot + force a live web search
- CC L19 - refactor + feature project end to end on a real repo
- CC L20 - surfaces: same project across terminal / Desktop / web / phone, then `--cloud` and `--teleport` a session back (needs Desktop app + web + phone signed in)
- CC L21 - Claude in Chrome: reproduce a bug or automate a browser chore on a non-prod site (needs a browser + staging site + test account; doubles as a standalone video)
- CC L22 - Agent SDK: ~25-line Python/TS agent
- CC L25 - CAPSTONE: skill + headless script + routine + MCP + hooks, empty folder to committed
- CC L26 - production checklist: one production-readiness pass on real code (secrets to env, error handling, run log, config), shown as diffs
- CC L27 - ship it live: deploy one thing to a real host with a live URL, or put a skill/agent on a schedule; verify the first live run + one alert (needs a host account + a deployable app; doubles as a standalone video)

Terminal talking-head / diagnostics (can batch):
- CC L23 - common mistakes + break-and-fix diagnostics
- CC L24 - power-user workflows: background agent + `/goal` chained live
- CC L28 - skills and agents library: live inventory (`/skills`, `/agents`, `/context`) + organize personal vs project scope + `/plugin`

Also flag (classified REUSE but each needs a short fresh slice on this same setup): CC L3 summarize-from-here, CC L6 bundled-script visualizer run, CC L11 second/third server + break-and-fix, CC L12 writing the custom agent file, CC L14 the three-hook build, CC L15 auto-mode + allowlist run.

### SETUP B - Agent builds (15 fresh sections)
Arcade Gateway + Claude Code (and a code editor for the framework lesson).

Talking-head block (no screen build, shoot together):
- AG L2 - when to build (or not)
- AG L3 - the agent loop in detail (with diagram)
- AG L5 - tool design
- AG L17 - multi-agent and orchestration (add the research-write-check demo)
- AG L20 - running an agent as a paid service

Live agent builds:
- AG L6 - write the memory file
- AG L7 - self-verification + 3 evals on the research agent
- AG L10 - inbox triage agent
- AG L11 - research assistant that saves an artifact
- AG L12 - repo triage to a ClickUp task
- AG L13 - content-repurposing agent
- AG L14 - customer-support / FAQ agent
- AG L15 - scheduled monitoring agent (run twice)
- AG L19 - deploy + schedule + cost control
- AG L16 - frameworks: rebuild the research agent in Pydantic AI / LangGraph / Agent SDK (needs code editor + Python/TS env)

### SETUP C - Cowork desktop (12 fresh sections)
Desktop app pointed at the dedicated folder.

Desktop demos:
- CW M6 - batch-rename and sort a media pile
- CW M7 - clean and merge two messy CSVs
- CW M8 - summarize a stack of PDFs
- CW M9 - draft a document from source files
- CW M10 - assemble a proposal / one-pager
- CW M14.4 - Notion connector demo
- CW M14.5 - custom MCP connector by URL
- CW M16 - calendar + meeting prep one-pager
- CW M21 - build your own Cowork skill (no code): save the M12 report as a named skill, run it by name, correct once
- CW CAPSTONE A - personal: inputs to a decision
- CW CAPSTONE B - business: repeatable operation, then schedule it

Desktop talking-head (batch):
- CW M19 - common mistakes, permission gotchas, troubleshooting

---

## SYNTHESIS 2 - REUSE: pull from existing, per course

### Claude Code
- **003** (beginner concepts) - the workhorse: [0:00-0:35] cold open, [1:00-2:30] CLAUDE.md, [2:30-3:45] chat/edit/run + context meter, [3:45-5:00] permissions, [5:00-6:15] `/clear` + `/model`, [7:45-8:45] hooks, [8:45-9:45] MCP, [9:45-10:45] subagents, [10:45-11:45] git/PR/worktrees, [11:45-12:45] memory, [12:45-13:30] outro
- **040** (skills run my business) - [0:00-0:35] cold open, [1:30-2:45] + [11:30-13:30] live skill build, full for L7, [13:30-end] outro; framing only for L25 capstone and L28 library wrap
- **001** (build a skill) - [1:30-10:00] SKILL.md structure/build (near-complete)
- **046** [0:45-2:30] MCP connect (L10); **045** multi-connection (L11)
- **021** sec 5 brain-vs-hands beat (intro); **041** model lineup (L16); **044 / 042 / 011 / 012** skill support (L5-L7)

### Cowork
- **023** (Cowork full course) - primary reuse: INTRO (cold open), Module 1 (M2), Module 2 Demo 2A (M4) + Demo 2B (M5) + closing beat (M3), Module 3 (M13), Module 4 Demo 4A/4B (M11, M12), Module 5 Demo 5A/5B (M14.1-3, M15), Module 8 (M17), Module 9 (M20), Module 10 + OUTRO
- **021** secs 4-5 and **030** (M1)
- Staged demo assets inside 023: `demo-assets/messy-client-folder` (M4), `demo-assets/receipts` (M5, Capstone A), `demo-assets/analytics` CSVs (M11, M12, M17)

### Build AI Agents
- **038** (build first agent) - cold open (INTRO), [0:20-1:30] what-is-an-agent (L1), [1:30-8:00] first agent full build (L8), [9:15-10:30] limits/safety (L18), [10:30-12:15] outro
- **046** (Arcade build agent) - [0:00-0:15] cold open (INTRO), [0:15-2:30] tools + auth + Gateway (L4), [2:30-8:00] morning-brief agent (L9), [8:00-9:00] safety/governance (L18, L20), CTA (outro)

---

## SYNTHESIS 3 - DEMO ASSETS TO STAGE before filming

Everything below is referenced by the outlines but does not exist yet (or needs setup). Group by course.

### Cowork
- `demo-assets/media-pile/` - a chaotic folder: `IMG_4821.jpg`, `Screenshot 2026-*.png`, `Untitled.pdf`, random screen recordings, mixed names (M6)
- `demo-assets/dirty-data/` - two intentionally messy CSVs (a contacts list + a signups list): different column names, inconsistent casing, duplicate rows, mismatched date formats; seed one from the 023 analytics CSVs (M7)
- `demo-assets/pdf-stack/` - 4-6 public sample PDFs (contracts, reports, a whitepaper, a lease or policy) with a renewal date/clause buried deep (M8)
- `demo-assets/proposal-inputs/` - scattered pieces: scope notes, a pricing sheet with placeholder numbers, a past proposal, a logo/brand note (M10)
- A non-sensitive source transcript selected from `transcripts/` for the drafting demo (M9)
- A Notion workspace/database with sample tasks, plus a page to summarize (M14.4)
- A public MCP/Gateway URL with OAuth for the custom connector demo (M14.5)
- A real upcoming calendar event with related emails and files, for meeting prep (M16)
- The M12 weekly-report inputs on hand at filming so the M21 build-your-own-skill demo saves a task viewers already watched (M21; no new asset, reuses the analytics CSVs)
- Capstone A: a month of receipts + bank-statement screenshots + a notes file (extend the receipts set)
- Capstone B: competitor transcripts + analytics exports + notes + a Drive doc reachable via connector

### Claude Code
- A small throwaway/real repo with a bug or small feature to add (L2)
- A messy script / tiny app / channel tool to refactor and extend (L19)
- A protected `.env` file in the demo repo for the block-edit hook (L14)
- MCP accounts connected: GitHub + Sentry + ClickUp (ClickUp already exists; set up Sentry account and GitHub app) (L10, L11)
- A repo with open issues for the scheduled "summarize open GitHub issues" routine (L9)
- API-key auth configured for the Agent SDK build, separate from the claude.ai login (L21)
- A screenshot of a broken/ugly UI to paste (L17)
- Desktop app + web app + phone (Claude iOS/Android) all signed in to the same account so a session can teleport across surfaces (L20)
- A non-production / staging site with a test account and a reproducible bug (or a repetitive browser chore) for Claude in Chrome (L21)
- A deliberately broken setup (bad hook, failed MCP server, or full context) to diagnose on camera (L23)
- A deployable app/tool built earlier in the course, plus a host account (Railway / Vercel / Fly / Cloudflare) with real env vars set, and one cheap alert channel (Slack or email) for the ship-it-live run (L27)
- The capstone system or the SDK agent with a real hardcoded secret to move to env, for the production-readiness pass shown as diffs (L26)

### Build AI Agents
- Arcade Gateway with Gmail + Calendar tools, OAuth cleared - foundational (L4, L9)
- A Drive/Docs tool in the Gateway (L11 save-artifact, L13 repurpose source, L14 FAQ source)
- GitHub in the Arcade catalog + the ClickUp MCP fallback connector, and a repo with issues/PRs (L12)
- A memory file template (name, reply voice, two standing rules) (L6, reused L13/L15)
- A FAQ / help-doc source of truth (product docs or a help folder) (L14)
- Three eval test cases: normal, edge, should-refuse (L7)
- Something worth monitoring (competitor uploads, a news keyword, channel stats, or a folder) (L15)
- A Python/TS environment with Pydantic AI, LangGraph, and the Claude Agent SDK installed (L16)
- A real transcript/doc/video as the repurposing source (from `transcripts/`) (L13)
- Real inbox + calendar with sensitive fields blurred, for the live morning-brief and triage runs (L9, L10)

---

## Fresh recording vs reuse - per course

- **Claude Code:** ~98 min of new-lesson runtime across 15 fresh sections, roughly 4.5 to 5 hours of fresh filming (the deploy block and library wrap pushed this course to 3 hours and added the most new load); ~82 min reusable across 15 sections, mostly from 003, 040, 001.
- **Cowork:** ~61 min of new-lesson runtime across 12 fresh sections, roughly 3 to 3.5 hours of fresh filming; ~83 min reusable across 17 sections, nearly all from 023.
- **Build AI Agents:** ~92 min of new-lesson runtime across 15 fresh sections, roughly 4 to 4.5 hours of fresh filming (still the most net-new course per section); ~40 min reusable across 7 sections from 038 and 046.

---

## Totals

| Course | RECORD NEW | REUSE | Sections |
|---|---|---|---|
| Claude Code | 15 | 15 | 30 |
| Cowork | 12 | 17 | 29 |
| Build AI Agents | 15 | 7 | 22 |
| **Total** | **42** | **39** | **81** |

**Total fresh sections to film across all three courses: 42.**
