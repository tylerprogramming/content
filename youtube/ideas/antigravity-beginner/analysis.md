# Source Video Analysis

## Source
Transcript: `~/content/transcripts/transcript_cCIiRnlyipE.txt`
Video: [Jack Roberts - AntiGravity Hidden Systems](https://youtu.be/cCIiRnlyipE)

## Structure Breakdown

| Segment | Timestamps | Duration | Purpose |
|---|---|---|---|
| Hook | 0:00 - 0:28 | 28s | Bold claim + credibility flex. "Game-changing if you know how to use it." |
| RAPS Framework Intro | 0:28 - 1:17 | 49s | Introduces 4-step framework. Formula One metaphor. |
| R — Rules | 1:17 - 7:06 | 5m 49s | Longest section. Global rules, workspace rules, gemini.md, workflows, audit.md. Builds product design doc live. |
| A — Armory (MCPs) | 7:06 - 14:00 | 6m 54s | MCP servers deep dive. Context7, Firecrawl, Supabase, Notion, Pinecone demos. |
| App Check-in | 14:00 - 18:15 | 4m 15s | Reviews built app, shows task list, discusses MCP limit (~50), settings walkthrough. |
| P — Parallel Agents | 18:15 - 24:07 | 5m 52s | Agent Manager, 4 archetypes, universal inbox, audit workflow demo. |
| S — Serverless | 24:07 - 28:19 | 4m 12s | Modal deployment, screenshot bot demo, Supabase MCP auto-creates table. |
| CTA | 28:19 - 28:34 | 15s | Quick redirect to next video. |

## What Works Well

- **Formula One metaphor** — Used throughout to frame each section. Effective recurring device.
- **RAPS acronym** — Memorable, gives viewers a framework to organize knowledge.
- **Live demos throughout** — Firecrawl scraping a coffee website, Notion page creation, Modal scheduling. Not hypothetical.
- **Practical MCP recommendations** — Names specific 5-6 MCPs to install. Actionable.
- **Agent archetypes** — Design Lead / Builder / Nerd / Researcher. Easy mental model for parallel agents.
- **Settings walkthrough** — Shows the actual AntiGravity settings panel (review policy, terminal, agent).
- **Nested tool usage** — Shows Firecrawl MCP being used inside an agent to enrich Notion content. Power-user move.

## Weaknesses / Opportunities for Differentiation

1. **28 minutes is long** — A beginner who just wants to get started will bounce. There's a gap for a fast, focused tutorial.
2. **Never actually shows setup/install** — Assumes you already have AntiGravity. Skips download, sign-in, first-run.
3. **Rules section is 6 minutes of talking** — Heavy on concept, light on showing what to actually type.
4. **No "build from zero" moment** — The app (Reddit scraper) is already partially built when he starts. Viewer never sees the empty folder → working app journey.
5. **MCP section is overwhelming** — 5 MCPs in 7 minutes. A beginner doesn't need Pinecone and Firecrawl on day one.
6. **Parallel agents are advanced** — Presented as step 3 of a beginner-adjacent video, but most viewers won't use this for weeks.
7. **Serverless (Modal) is very technical** — Requires API keys, cloud accounts, deployment concepts. Not beginner material.
8. **"Hidden systems" title but content is fairly standard** — Opportunity to actually show things that aren't obvious.
9. **No discussion of what AntiGravity IS** — Never explains it's a VS Code fork, what Gemini 3 is, or why it matters vs. Cursor.
10. **No mention of Plan Mode vs Fast Mode** — Key beginner concept skipped entirely.

## Target Audience

Mid-level. Assumes familiarity with AI tools, some technical vocabulary (MCP, API keys, serverless, Supabase). Secondary: Jack's existing Skool community members learning his RAPS system.

## Our Differentiation

Our beginner tutorial fills the exact gaps Jack left:
- **Actually show the install and setup** — Download → open → first project
- **Empty folder to working app** — The full zero-to-hero journey in one shot
- **10-15 minutes, not 28** — Fast, dense, no filler
- **One concept at a time** — Build the app first, THEN briefly show rules and Manager View as "next steps"
- **No MCP setup required** — Keep it simple. MCPs are a future video.
- **Show Plan Mode and the task list** — The artifact system is the key differentiator from other tools and it's beginner-friendly

---

## AntiGravity Research (Full Reference)

### What Is AntiGravity?

Google AntiGravity is an **agent-first AI IDE** developed by Google. Announced **November 18, 2025** alongside Gemini 3. Heavily modified VS Code fork.

- **Website:** antigravity.google/download
- **Pricing:** Free public preview (Pro ~$20/month expected later 2026)
- **Platforms:** macOS, Windows, 64-bit Linux
- **Benchmark:** 76.2% on SWE-bench Verified

### Architecture

Two primary views:
1. **Editor View** — Traditional IDE with agent sidebar
2. **Manager View** — Multi-agent orchestration control center (`Ctrl/Cmd + Shift + M`)

### Core Features

**Multi-Model Support:** Gemini 3 Pro, Deep Think, Flash + Claude Sonnet 4.5 + GPT-OSS

**Rules System (3 Tiers):**
1. Global Rules (`~/.gemini/GEMINI.md`) — Apply everywhere
2. Workspace Rules (`.agent/rules/`) — Per workspace/client
3. Project Rules — Within project folders

**How to create rules:** Click `...` top-right → Customizations → Rules → `+ Global` or `+ Workspace`

**Workflows:** Reusable instruction sets via `@workflow`. Stored at `~/.gemini/antigravity/global_workflows/` (global) or `.agent/workflows/` (workspace).

**Skills System:** On-demand knowledge packages. Structure: SKILL.md + scripts/ + references/ + assets/

**MCP Servers:** Context7, Firecrawl, Supabase, Notion, Pinecone. Keep under ~50.

**Parallel Agents:** Multiple agents simultaneously. Agent archetypes: Design Lead, Builder, Nerd (QC), Researcher.

**Artifacts:** Task Lists, Implementation Plans, Screenshots, Browser Recordings.

**Plan vs Fast Mode:** Plan creates artifacts before acting. Fast executes immediately.

**Terminal Policies:** Off (never auto-execute), Auto (agent decides), Turbo (always auto-execute).

**Settings path:** AntiGravity → Settings → AntiGravity Settings → Review Policy, Terminal, Browser, Agent.

### Competitive Landscape

| Feature | AntiGravity | Cursor | Windsurf | Claude Code |
|---------|------------|--------|----------|-------------|
| **Type** | VS Code fork (agent-first) | VS Code fork | VS Code fork | CLI/Terminal |
| **Parallel Agents** | Yes | No | No | No |
| **MCP Support** | Built-in | Yes | Partial | Yes (native) |
| **Pricing** | Free preview | $20/mo | $15/mo | API usage |
| **Best For** | Task delegation | Hands-on coding | Large codebases | Terminal power users |

### About Jack Roberts

- Founded Glaido. Built/sold startup with 60k customers (Top-100 UK Startups).
- 7-figure AI automation business. "AI Automations by Jack" on Skool.
- Teaches RAPS framework: Rules → Armory → Parallel agents → Serverless.

### Sources

- [Google Developers Blog - AntiGravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)
- [AntiGravity Wikipedia](https://en.wikipedia.org/wiki/Google_Antigravity)
- [The New Stack - Hands-On Review](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/)
- [Codecademy - IDE Comparison](https://www.codecademy.com/article/agentic-ide-comparison-cursor-vs-windsurf-vs-antigravity)
- [Visual Studio Magazine - VS Code Forks](https://visualstudiomagazine.com/articles/2026/01/26/what-a-difference-a-vs-code-fork-makes-antigravity-cursor-and-windsurf-compared.aspx)
- [Google Codelabs - Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)
- [AIFire - 2026 Guide](https://www.aifire.co/p/google-antigravity-the-2026-guide-to-the-best-ai-ide)
- [LeaveIt2AI - Review](https://leaveit2ai.com/ai-tools/code-development/antigravity)
- [AntiGravity Codes - MCPs & Rules](https://antigravity.codes/)
- [Jack Roberts](https://jackroberts.ai/)
- [BayTech - 2026 Guide](https://www.baytechconsulting.com/blog/google-antigravity-ai-ide-2026)
- [Toolworthy - Review](https://www.toolworthy.ai/tool/google-antigravity)
- [Index.dev - Agentic IDE](https://www.index.dev/blog/google-antigravity-agentic-ide)
- [Medium - Getting Started](https://medium.com/google-cloud/tutorial-getting-started-with-google-antigravity-b5cc74c103c2)
- [Tony Reviews Things - Skills](https://www.tonyreviewsthings.com/google-antigravity-skills-mcp-agentic-ide/)
- [KDnuggets - AI-First Dev](https://www.kdnuggets.com/google-antigravity-ai-first-development-with-this-new-ide)
- [Google Cloud Blog - Data Integration](https://cloud.google.com/blog/products/data-analytics/connect-google-antigravity-ide-to-googles-data-cloud-services)
- [Geeky Gadgets - Guide](https://www.geeky-gadgets.com/google-antigravity-guide/)
- [HumAI - IDE Comparison](https://www.humai.blog/best-ai-coding-ide-2025-cursor-vs-antigravity-vs-claude-code-vs-windsurf-the-complete-comparison/)
- [freeCodeCamp - Flutter + AntiGravity](https://www.freecodecamp.org/news/build-an-ai-powered-flutter-app-with-google-antigravity/)
- [Codecademy - Setup Guide](https://www.codecademy.com/article/how-to-set-up-and-use-google-antigravity)
- [Mete Atamel - Rules & Workflows](https://atamel.dev/posts/2025/11-25_customize_antigravity_rules_workflows/)
- [GitHub - Workspace Template](https://github.com/study8677/antigravity-workspace-template)
