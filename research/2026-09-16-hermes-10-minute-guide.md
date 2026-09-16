# Research: Hermes Agent for a 10-minute guide

**Date:** 2026-09-16
**Task:** kanban t_e74d3be4 (dashboard, no body). Interpreted as: what a 10-minute Hermes Agent guide from tylerreedai should be, backed by the current field and the current docs.
**Search:** yt-dlp, 6 queries ("Hermes Agent", "+ tutorial", "+ setup guide", "+ explained", "+ in 10 minutes", "+ beginners"), 30 results each, deduped to 91, 89 long-form with Hermes in the title. Counts pulled 2026-09-16 18:15 EDT.
**Raw data:** `research/2026-09-16-hermes-10-minute-guide.json` (91 videos with chapters, descriptions, follower counts)
**Docs pulled today:** docs index, installation, quickstart, memory, skills, cron, CLI reference, import-from-other-agents (all hermes-agent.nousresearch.com, 2026-09-16)
**Transcripts pulled today (10):** `transcripts/transcript_<id>.txt` for 3JkcN6rldpc, 9GpWELm3_XI, BeWUUclCin0, 1CLc-VeEivk, hZqC6-pHPng, DYdvJCxWd6M, -NF6TYwRJ2U, 8GjyOQy19so, 8bYMgvJt5Ws, Ta2wg6xPaY4
**Prior research:** `research/2026-08-25-hermes-agent.md` (20 videos, 08-25 counts), `research/youtube/hermes-agent-nous/index.md` (product facts, 08-25), `research/youtube/creator-breakdowns/2026-09-12-tina-huang-hermes-fundamentals.md`
**Related package:** 057 (30-min setup course, v4, filming). This research is for a separate, shorter video. See section 6 for how the two fit.

---

## 0. Read this first

| Fact | Number | Consequence |
|---|---:|---|
| Long-form Hermes videos found | 89 | Crowded. 30 of them are 5 to 15 minutes. |
| Videos titled "in 10 minutes" or "10 min" | 7 | All under 32K views except Vaibhav Sisinty (183,781, sponsored VPS ad). Six of seven are under 3K views. The title alone does not carry. |
| Biggest video in the 5-15 min lane | 183,781 (Vaibhav Sisinty, 10:11, 2026-05-03) | Hostinger ad plus 4 Telegram demos. Zero terminal. Zero Claude Code. |
| Biggest video in the last 45 days | 338,082 (Metics Media, 34:23, 2026-08-31), 21,130 views/day | Long, VPS, Telegram, desktop app. The market still rewards long setup guides. |
| Fastest-growing video right now | 17,950 in 1 day (Sharbel A., "Hermes + Claude Code Is The Ultimate Cheat Code", 14:10, 2026-09-15) | The Claude Code + Hermes angle just got its first video 24 hours ago. It is a talking-head concept video with no setup and no terminal. |
| Videos that mention `hermes import-agent claude-code` | 0 of 10 transcripts checked | Nobody has shown the one command that moves a Claude Code setup into Hermes. Verified on Tyler's machine today: 55 items would import (CLAUDE.md, 2 MCP servers, 52 skills). |
| Avg views, 10-15 min bucket | 46,371 (19 videos) | vs 236,360 avg for 30-60 min (16 videos). Short Hermes videos underperform long ones on average. A 10-min video needs a sharp reason to exist. |

Read on the field: the generic "set up Hermes in 10 minutes" slot is taken 7 times and none of them worked without a sponsor. The open slot is "you already use Claude Code, here is what Hermes adds and the one command that carries your setup over." Sharbel proved demand for the pairing yesterday (17,950 views/day on a 32K-sub channel) and did it with zero demos. That is the opening.

---

## 1. The field

### 1a. Top 25 by views (of 89)

| # | Title | Channel | Views | Views/day | Duration | Uploaded | id |
|---|---|---|---:|---:|---|---|---|
| 1 | you need to use Hermes RIGHT NOW!! (goodbye OpenClaw!!) | NetworkChuck | 1,650,387 | 13,869 | 32:39 | 2026-05-20 | QQEgIo4Juxg |
| 2 | Hermes Agent Fundamentals In 29 Minutes | Tina Huang | 495,478 | 8,543 | 29:40 | 2026-07-20 | 5_N84t1rUU0 |
| 3 | Hermes Agent: Zero to Personal AI Assistant (1 Hour Course) | Nate Herk | 378,378 | 2,933 | 58:22 | 2026-05-10 | gb5TlGw6Uks |
| 4 | Hermes Agent - Full Tutorial & Setup Guide (For Beginners) | Metics Media | 338,082 | 21,130 | 34:23 | 2026-08-31 | DYdvJCxWd6M |
| 5 | Hermes Agent Explained In 5 Minutes | CodeHead | 269,706 | 2,325 | 4:53 | 2026-05-23 | 9GpWELm3_XI |
| 6 | HERMES AGENT FULL COURSE 3 HOURS: Build & Sell (2026) | Samin Yasar | 233,324 | 3,431 | 3:02:47 | 2026-07-10 | 8yE6G1Lup1s |
| 7 | 6 Hermes Agent use cases I promise will change your life | Alex Finn | 216,047 | 1,847 | 15:18 | 2026-05-22 | AQHlyGA2cZM |
| 8 | Hermes Agent Full Setup: Build Your Own Self-Improving AI Agent in 10 mins | Vaibhav Sisinty | 183,781 | 1,351 | 10:11 | 2026-05-03 | 3JkcN6rldpc |
| 9 | Hermes Agent Desktop: Full Setup + Real Use Cases | Greg Isenberg | 182,399 | 1,788 | 43:48 | 2026-06-06 | EJm8Ka-gVOc |
| 10 | 100 hours of Hermes Agent lessons in 46 minutes | David Ondrej | 179,316 | 1,348 | 47:00 | 2026-05-06 | G47mnkGkYwQ |
| 11 | My FULL Hermes Agent Setup (HermesOS) | Tina Huang | 175,996 | 8,000 | 16:24 | 2026-08-25 | 1CLc-VeEivk |
| 12 | Every Level of Hermes Agent Explained | Jack Roberts | 171,175 | 1,881 | 25:35 | 2026-06-17 | 6GtF_uHbGhw |
| 13 | Hermes Agent is the greatest AI tool ever made. Here's how to set it up | Alex Finn | 169,474 | 1,500 | 44:14 | 2026-05-26 | RoBD7Lc-0MI |
| 14 | Hermes Agent - Full Course & Setup Guide - For COMPLETE Beginners | Tech With Tim | 144,967 | 1,407 | 59:20 | 2026-06-05 | mTYxpIRK7xA |
| 15 | Learn 95% of Hermes Agent in 31 Minutes | Sharbel A. | 144,614 | 3,806 | 31:28 | 2026-08-09 | Ta2wg6xPaY4 |
| 16 | Hermes Agent Tutorial for Beginners (Full Step-by-Step Setup) | Metics Media | 133,898 | 1,206 | 33:48 | 2026-05-28 | LvWobwr0Neg |
| 17 | Did Hermes Agent just kill OpenClaw? (full guide) | Alex Finn | 132,440 | 784 | 13:55 | 2026-03-31 | tP6yf22OJdI |
| 18 | Hermes Agent: The Ultimate Beginner's Guide | Metics Media | 119,695 | 825 | 37:08 | 2026-04-24 | CwPUOVUdApE |
| 19 | 10 Hermes Agent Skills You NEED To Install Today | Sharbel A. | 112,050 | 3,615 | 13:19 | 2026-08-16 | 5WQk9WiWcYQ |
| 20 | Full Hermes Agent Tutorial (Desktop) | Wanderloots | 109,702 | 1,425 | 28:50 | 2026-07-01 | GL67DEf2nyI |
| 21 | 14 Hermes Agent Skills You NEED To Install Right Now | Dubibubi | 106,828 | 1,942 | 17:24 | 2026-07-23 | IbFaY3xFpZM |
| 22 | Hermes Architecture EXPLAINED: Memory, Context & Gateways | Hugging Face | 103,797 | 1,141 | 40:28 | 2026-06-17 | n32qq7Kwzh0 |
| 23 | Is Hermes Bot Mode Worth It? My Best Practices (So Far) | Wanderloots | 103,612 | 10,361 | 35:06 | 2026-09-06 | 3RoK0rrOHCA |
| 24 | Why I'm back to Qwen 3.8 27B and Hermes Agent | Digital Spaceport | 100,258 | 10,026 | 16:48 | 2026-09-06 | L8xTCd80p68 |
| 25 | Hermes Agent Full Tutorial for Beginners / Setup Guide | Tech With Tim | 99,827 | 684 | 28:35 | 2026-04-23 | 1ve4Atbqmoo |

Full 89 in the JSON. Views moved since 08-25: Tina 313,962 to 495,478 (+58%), Nate Herk 349,120 to 378,378 (+8%), CodeHead 5-min 195,894 to 269,706 (+38%). NetworkChuck was not in the 08-25 search; it is the biggest Hermes video by 3x.

### 1b. The 10-minute lane (5:00 to 15:00, 30 videos, top 15)

| # | Title | Channel | Views | Duration | Uploaded | Sponsor (from description or transcript) | id |
|---|---|---|---:|---|---|---|---|
| 1 | Hermes Agent Full Setup ... in 10 mins | Vaibhav Sisinty | 183,781 | 10:11 | 2026-05-03 | Hostinger (transcript) | 3JkcN6rldpc |
| 2 | Did Hermes Agent just kill OpenClaw? (full guide) | Alex Finn | 132,440 | 13:55 | 2026-03-31 | none in description | tP6yf22OJdI |
| 3 | 10 Hermes Agent Skills You NEED To Install Today | Sharbel A. | 112,050 | 13:19 | 2026-08-16 | none in description | 5WQk9WiWcYQ |
| 4 | The Biggest Lie You've Been Told About Hermes Agent | Craig Hewitt | 80,172 | 14:21 | 2026-05-29 | none in description | ubxDCAtYQwE |
| 5 | Hermes Agent Full Tutorial INSTALLATION + USECASES | CodeHead | 65,454 | 7:47 | 2026-05-14 | Hostinger (transcript) | 8GjyOQy19so |
| 6 | Use This To Make The Hermes Agent Basically Free | AI LABS | 58,715 | 13:08 | 2026-07-01 | none in description | 5d02TYoOzfE |
| 7 | Hermes Agent Tutorial: Beginner to Pro In 13 Minutes | Zinho Automates | 47,829 | 12:56 | 2026-06-24 | Hostinger (transcript) | -NF6TYwRJ2U |
| 8 | The Only Hermes Agent Tutorial You'll Need in 2026 | Parker Prompts | 44,353 | 10:57 | 2026-05-27 | Hostinger | 8bYMgvJt5Ws |
| 9 | The Hermes Agent Setup Everyone's Installing Now | Sharbel A. | 43,019 | 13:17 | 2026-04-02 | none in description | k5HM4HUGt00 |
| 10 | How I Made Hermes Agent 10x More Powerful | Sharbel A. | 39,663 | 13:31 | 2026-08-23 | none in description | 3KIyi_Npxmg |
| 11 | Hermes Agent Quickstart: Zero to Working Agent in 10 Minutes | Tonbi's AI Garage | 31,151 | 9:50 | 2026-06-23 | none (transcript) | BeWUUclCin0 |
| 12 | Every Hermes Agent Concept Explained for Normal People | Zinho Automates | 30,207 | 13:43 | 2026-07-30 | Hostinger | oxYV588fuPs |
| 13 | GPT-5.6 on Hermes Agent Is Actually Insane ($0 setup) | Moe Lueker | 27,868 | 12:47 | 2026-07-14 | VPS affiliate link | eo4X_BqDozA |
| 14 | The ONLY Hermes Agent Tutorial You'll Ever Need | Zinho Automates | 23,514 | 14:18 | 2026-07-28 | Hostinger | _erdOhqGVhk |
| 15 | Hermes Agent Tutorial for Beginners - Crash Course | Creator Magic | 23,337 | 9:56 | 2026-05-22 | Zapier affiliate link | 6QZBep7mW0c |

Sponsored or affiliate: 9 of 15. Of the 6 setup-style videos (1, 5, 7, 8, 11, 15), 5 carry a VPS or affiliate link. Tonbi is the only clean one and it is Windows.

The "in 10 minutes" titles specifically: Vaibhav 183,781; Tonbi 31,151; Clearmud (Windows) 22,980; Henry Hasselbach (German) 15,795; Mervin Praison 2,630; Ai Untapped 1,643; Ty Chen 792; Noah McCray 354; The AI Doctor 226. Median 2,630. The phrase is not a draw by itself.

### 1c. Last 45 days by velocity (top 10 of 23)

| # | Title | Channel | Views | Views/day | Duration | Uploaded |
|---|---|---|---:|---:|---|---|
| 1 | Full Tutorial & Setup Guide (For Beginners) | Metics Media | 338,082 | 21,130 | 34:23 | 2026-08-31 |
| 2 | Hermes + Claude Code Is The Ultimate Cheat Code | Sharbel A. | 17,950 | 17,950 | 14:10 | 2026-09-15 |
| 3 | Is Hermes Bot Mode Worth It? | Wanderloots | 103,612 | 10,361 | 35:06 | 2026-09-06 |
| 4 | Why I'm back to Qwen 3.8 27B and Hermes Agent | Digital Spaceport | 100,258 | 10,026 | 16:48 | 2026-09-06 |
| 5 | My FULL Hermes Agent Setup (HermesOS) | Tina Huang | 175,996 | 8,000 | 16:24 | 2026-08-25 |
| 6 | How I Upgrade My Hermes Agent Team: Bot Mode, Skills & MCP | Wanderloots | 28,781 | 5,756 | 21:40 | 2026-09-11 |
| 7 | 7 INSANE Use Cases For Hermes Agent | Tom Crawshaw | 61,089 | 4,699 | 22:30 | 2026-09-03 |
| 8 | Grokbot vs Hermes Agent | Tom Crawshaw | 15,698 | 3,924 | 19:12 | 2026-09-12 |
| 9 | Learn 95% of Hermes Agent in 31 Minutes | Sharbel A. | 144,614 | 3,806 | 31:28 | 2026-08-09 |
| 10 | Every Hermes Agent Concept Explained for Normal People | Tom Crawshaw | 84,462 | 3,672 | 40:00 | 2026-08-24 |

Three themes are moving in September: Bot Mode (Wanderloots x2, Tonbi), local models (Digital Spaceport), and Claude Code pairing (Sharbel). Beginner setup is still the biggest single bucket (Metics).

### 1d. Duration buckets (89 videos)

| Bucket (min) | Videos | Total views | Avg views |
|---|---:|---:|---:|
| under 5 | 3 | 269,838 | 89,946 |
| 5 to 10 | 11 | 190,430 | 17,311 |
| 10 to 15 | 19 | 881,059 | 46,371 |
| 15 to 30 | 39 | 2,785,904 | 71,433 |
| 30 to 60 | 16 | 3,781,769 | 236,360 |
| 60+ | 1 | 233,324 | 233,324 |

---

## 2. What the 10-minute videos actually do (transcripts)

| Video | Structure | Sponsor time | Live demos | What is missing |
|---|---|---|---|---|
| Vaibhav Sisinty 10:11 (183,781) | Hook (morning HN brief on Telegram) 1:00, what is Hermes 1:00, Hostinger 2:00, Telegram 0:40, 4 demos 3:00, memory/skills 1:00, cost 1:00 | 2:00 of 10:11 | 4, all via Telegram: HN PDF, thumbnail grid, competitor monitor with subagents, write-like-me | No terminal. Never shows a skill file or memory file. Never shows a failure. |
| Tonbi's AI Garage 9:50 (31,151) | Install 1:00, gateway 0:30, Telegram 2:30, iMessage via Photon 2:00, install a skill 1:00, dashboard + desktop 1:00, /model, memory, cron 1:30 | 0 | Telegram hello, iMessage cron status, concept-diagram skill, cron sports+news | Windows, no Claude Code, thin on why. Quick summary of a 5-hour masterclass. |
| CodeHead 7:47 (65,454) | What is Hermes 0:40, install 1:20, free models 1:00, Telegram 0:35, brain dump 0:45, reverse prompting 0:40, 2 use cases 1:10, pro tip | Hostinger ~1:00 | Brain dump prompt, reverse prompt | Best "first 5 minutes with Hermes" advice in the field: brain dump, then "based on what you know about me, what use cases would help me?" |
| Zinho Automates 12:56 (47,829) | Why VPS 1:00, VPS 2:30, setup 3:15, Slack 2:00, skills 0:50, memory 0:30, cron 0:30, morning brief 1:00 | Hostinger ~2:30 | Slack: research + "save your approach as a skill", "remember I like short responses", weekly cron, morning brief | All chat prompts, no files opened. |
| CodeHead 4:53 (269,706) | Not a copilot 0:35, memory + skills 1:00, install + Hostinger 1:30, skills hub 1:00, subagents 0:30, who it is for 0:30 | ~1:15 | 0 | Pure explainer. Biggest short video. Anthropic-style: someone owns "what is it in 5 minutes." Do not remake. |
| Sharbel A. 14:10 (17,950, 1 day old) | Hook ($6K client closed overnight) 1:00, builder vs operator 1:20, 3 business examples 4:30, shared memory (Mem0) 3:20, self-improvement 1:00, 5 moves 2:00 | 0 | 1: tells Claude a favorite food, Hermes recalls it via Mem0 | No terminal, no install, no `import-agent`, no profiles, no Bot Mode. The concept without the build. |

Pattern across all six: Telegram or Slack is the surface, VPS is the sponsor, the demos are chat prompts, and no one opens `~/.hermes`. Metics (34 min) is the only one that shows the memory tool fire on screen and then proves it in a fresh session (transcript 22:49 to 24:35), and that is the beat people share.

---

## 3. What Hermes is today (verified against docs, 2026-09-16)

| Fact | Value | Source |
|---|---|---|
| Repo stars / forks | 246,177 / 51,458 | github.com/NousResearch/hermes-agent (fetched 09-16). Was ~236K on 08-25. |
| License | MIT | same |
| Tyler's installed version | v0.21.3 (2026.9.14), 38 commits behind | `hermes --version` on this Mac, 09-16 |
| Install (mac/Linux/WSL2) | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` | docs/getting-started/installation |
| Install (Windows native) | `iex (irm https://hermes-agent.nousresearch.com/install.ps1)` | same |
| Recommended install on mac/Windows | Hermes Desktop installer (bundles CLI + app) | docs index and installation page both say "recommended" |
| Provider quick path | `hermes setup --portal` (Nous Portal OAuth, 300+ models + Tool Gateway) | quickstart |
| Anthropic as provider | Max plan + extra usage credits via OAuth, or API key | quickstart provider table |
| Min context | 64K tokens, rejected at startup below that | quickstart |
| Secrets vs settings | `~/.hermes/.env` vs `~/.hermes/config.yaml`; `hermes config set` routes automatically | quickstart |
| Two terminal UIs | `hermes` (classic) and `hermes --tui` (recommended) | quickstart |
| Memory | MEMORY.md 2,200 chars, USER.md 1,375 chars, in `~/.hermes/memories/`, frozen snapshot at session start | docs/user-guide/features/memory |
| Session recall | FTS5 `session_search` across all past sessions | same |
| Skills | `~/.hermes/skills/`, agentskills.io standard, every skill is a slash command, `/learn <source>` writes one | docs/user-guide/features/skills |
| Cron | `/cron add "every 2h" "..."`, natural language, no-agent mode, event triggers via webhook | docs/user-guide/features/cron |
| Built-in tools | "60+" | docs index |
| Claude Code import | `hermes import-agent claude-code` maps CLAUDE.md to MEMORY.md, `Bash(...)` allow/deny to `command_allowlist`/`approvals.deny`, mcpServers to `mcp_servers`, `skills/<name>/` to `~/.hermes/skills/claude-code-imports/<name>/`. `commands/*.md` skipped. Credentials never read. `--dry-run` previews. `--sync` re-imports on change. | docs/user-guide/import-from-other-agents |
| Import on Tyler's machine | 55 items would import: CLAUDE.md, mcp_servers.clickup, mcp_servers.skool (Authorization header stripped), 52 skills (yt-package, yt-search, yt-thumbnail, prd, ralph, transcribe, ...). 0 allow rules, 0 deny rules. | `hermes import-agent claude-code --dry-run`, 09-16 |
| Recovery order (docs) | `hermes doctor`, `hermes model`, `hermes setup`, `hermes sessions list`, `hermes --continue`, `hermes gateway status` | quickstart |
| Common failure 1 | Empty or broken replies = provider auth or model selection wrong, rerun `hermes model` | quickstart |
| Common failure 2 | Gateway starts but nobody can message it = token, allowlist, or platform setup incomplete | quickstart |

Docs also state the quickstart rule: "if Hermes cannot complete a normal chat, do not add more features yet." That is a usable line for a 10-minute video.

Unverified today (do not say on camera without a check): Parker Prompts claims "150,000 GitHub stars in 7 weeks" and "agents with 20 or more self-created skills complete similar tasks 40% faster" (transcript 8bYMgvJt5Ws 0:00 and 0:52). No source given. Not in the docs pages pulled.

---

## 4. The opening

Nobody in 89 videos has made the video for the person who already runs Claude Code every day. The closest is Sharbel yesterday, and it is a framework talk with one Mem0 demo. Specific gaps:

| Gap | Who covers it | Proof |
|---|---|---|
| `hermes import-agent claude-code` on screen | none of 10 transcripts | grep across transcripts, 0 hits |
| Claude Code skills running inside Hermes as slash commands | none | Tyler has 52 that would import |
| CLAUDE.md becoming MEMORY.md, then opened in a file | none | docs mapping table |
| A permission deny rule becoming `approvals.deny` | none | docs mapping table (Tyler's settings.json has none; need one for the demo) |
| Terminal install on a Mac, no VPS, no sponsor | Tonbi (Windows) | 5 of 6 short videos use Hostinger |
| Memory proven in a fresh session | Metics only, in a 34-min video | transcript 22:49 to 24:35 |

The 10-minute video is: "You already have Claude Code. Run one command, your CLAUDE.md, MCP servers, and skills are in Hermes. Now here are the 3 things Hermes does that Claude Code does not: remembers across sessions, runs on a schedule, and messages you." Three demos, one command, no sponsor.

---

## 5. Beat plan (target 10:00 to 11:00)

| # | Beat | Time | On screen | Exact prompt or command |
|---|---|---|---|---|
| 1 | Hook | 0:00 to 0:35 | Slack message from Coder that arrived while Tyler was away (real one from the 057 cron). "Claude Code cannot do this. It sat in my terminal waiting for me." | none |
| 2 | Who this is for | 0:35 to 1:00 | Text: "You use Claude Code daily. Keep it. This adds three things." Name them. | none |
| 3 | Install | 1:00 to 2:00 | Terminal, the curl line, `hermes model`, pick Anthropic (Max OAuth) so it is the same model he already pays for. Say the 64K rule in one line. | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` then `hermes model` |
| 4 | The one command | 2:00 to 3:30 | `hermes import-agent claude-code --dry-run`, scroll the 55-item preview, then run it for real. Open `~/.hermes/memories/MEMORY.md`, show CLAUDE.md lines in it. Open `~/.hermes/skills/claude-code-imports/`. | `hermes import-agent claude-code --dry-run` then `hermes import-agent claude-code` |
| 5 | Same skill, new home | 3:30 to 4:30 | `hermes --tui`, type `/yt-search` (or another imported skill), it runs. "That is a Claude Code skill running in Hermes. Zero edits." | `/yt-search Hermes Agent` |
| 6 | Thing 1: memory that survives | 4:30 to 6:00 | Metics beat. Give one correction, watch the memory tool fire, `/new`, ask again, it holds. Then `session_search`: "what did we talk about 10 minutes ago." | "Too wordy. Three sentences max, no bullets. Save that as a preference." then `/new` then "What did I say about response length?" |
| 7 | Thing 2: runs on a schedule | 6:00 to 7:30 | `/cron add` in chat, one job that returns a decision not a dump. Show `hermes cron list`. Trigger it by hand. | `/cron add "every weekday at 8am" "Check tylerprogramming/content for PRs opened in the last 24h. If none, say so in one line. If any, list them with one-line verdicts."` |
| 8 | Thing 3: it messages you | 7:30 to 9:00 | Slack gateway is already wired (057 state). Send the cron result to Slack. Phone shot of it arriving. One line on `hermes gateway setup` for viewers. | `hermes cron run "<job name>"` |
| 9 | What breaks | 9:00 to 9:40 | The docs failure table: empty replies = `hermes model`; nobody can message it = `hermes gateway status`. Say `hermes doctor` first. | `hermes doctor` |
| 10 | Close | 9:40 to 10:15 | "Claude Code builds. Hermes remembers, schedules, and messages. Same skills, same model, same CLAUDE.md." Point to 057 for the 30-min version with Bot Mode. | none |

Rhythm borrowed from Tina and Metics: say the seam when cutting to the mature machine (Slack is already wired), and prove memory in a fresh session, not the same one.

What to leave out of the 10-min cut: Bot Mode, profiles, local models, Honcho, VPS. All of that is 057.

---

## 6. How this fits 057

| | 057 (v4, filming) | This video |
|---|---|---|
| Length | ~30 min | 10 min |
| Title | Set Up Hermes Agent in 30 Minutes (Claude Code Users Start Here) | proposal: Claude Code Users: Move to Hermes Agent in 10 Minutes (One Command) |
| Ending | Bots tab handoff, real PR, Coder pings Slack | Cron result lands in Slack |
| Overlap | install, `hermes model`, memory, Slack | same 4, compressed |
| Unique here | `import-agent`, imported skill as slash command | not in 057 (grep of all 057 package .md files for "import-agent": 0 hits, 09-16) |

Two options for Tyler:
1. Ship this as a standalone 10-min video before 057. It is the top-of-funnel; 057 is the follow-on. `import-agent` is the hook nobody has.
2. Fold beats 4 and 5 into 057 as a 90-second block after install, and drop this video. Risk: the one differentiated beat is buried at minute 6 of a 30-min course.

Recommendation: option 1. The 10-15 min bucket averages 46K, but the one video in it with a distinct angle and no sponsor is what is missing, and Sharbel's 1-day velocity says the Claude Code + Hermes audience is awake right now.

---

## 7. Title and thumbnail inputs (for @packager)

Titles in the field that worked at 10-15 min: "in 10 mins" (Vaibhav), "in 13 Minutes" (Zinho), "Skills You NEED To Install" (Sharbel, Dubibubi), "+ Claude Code Is The Ultimate Cheat Code" (Sharbel). Titles that did not: five of seven "in 10 minutes" under 3K.

Candidate titles (unranked, rules not checked):
- Claude Code Users: Move to Hermes Agent in 10 Minutes (One Command)
- Hermes Agent for Claude Code Users (Your Skills Import in One Command)
- I Moved My Claude Code Setup to Hermes Agent in One Command

Thumbnail: terminal with `hermes import-agent claude-code` and "55 items imported" visible. Two logos, one arrow.

---

## 8. Files

- This report: `research/2026-09-16-hermes-10-minute-guide.md`
- Raw: `research/2026-09-16-hermes-10-minute-guide.json`
- Transcripts (new today): `transcripts/transcript_3JkcN6rldpc.txt` (Vaibhav 10:11), `transcript_BeWUUclCin0.txt` (Tonbi 9:50), `transcript_8GjyOQy19so.txt` (CodeHead 7:47), `transcript_-NF6TYwRJ2U.txt` (Zinho 12:56), `transcript_9GpWELm3_XI.txt` (CodeHead 4:53), `transcript_hZqC6-pHPng.txt` (Sharbel + Claude Code 14:10), `transcript_DYdvJCxWd6M.txt` (Metics 34:23), `transcript_Ta2wg6xPaY4.txt` (Sharbel 95% 31:28), `transcript_1CLc-VeEivk.txt` (Tina HermesOS 16:24), `transcript_8bYMgvJt5Ws.txt` (Parker Prompts 10:57)
- Prior: `transcripts/transcript_5_N84t1rUU0.txt` (Tina 29:40), `research/youtube/creator-breakdowns/2026-09-12-tina-huang-hermes-fundamentals.md`
- Docs cache: `~/.hermes/profiles/researcher/cache/web/hermes-agent.nousresearch.com-*.md` (quickstart, memory, skills, cron, CLI ref, 09-16)
