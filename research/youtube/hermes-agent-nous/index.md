# Research: Hermes Agent (Nous Research)

**Date:** 2026-08-25
**For:** New long-form video
**Angle Tyler flagged:** "Not as talked about, and it's amazing." Runs as terminal TUI or desktop app.

---

## 1. What Hermes Agent is

Open-source, self-hosted AI agent by **Nous Research**. MIT licensed. Released **Feb 25, 2026**. Current build ~v0.20.5.

The one-line pitch: it is NOT a coding copilot chained to an IDE and NOT a chatbot wrapper. It runs as an **always-on background process on infrastructure you control**, remembers everything across sessions, and writes its own reusable skills as it works, so it gets faster and cheaper the second time it hits a task.

Repo: `github.com/NousResearch/hermes-agent` (~236k stars, ~47k forks as of research date).
Install (mac/Linux/WSL2): `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`

### Core features
- **Self-improving loop** - the headline. Solves a hard task, auto-writes a "skill" document describing the solution pattern, then loads that skill next time instead of reasoning from scratch. Accumulates domain expertise on your codebase/workflow over weeks.
- **Persistent memory** - SQLite DB indexed by FTS5 holding every session; full-text search + LLM summarization across past conversations. This is the thing competitors can't do.
- **Built-in cron** - natural-language scheduling for reports, backups, briefings, audits; runs unattended through the gateway.
- **Messaging gateways** - one agent, one memory, reachable from Telegram, Discord, Slack, WhatsApp, Signal, Email, and CLI. (Live voice in Discord voice channels too.)
- **Subagents** - isolated subagents with their own conversations, terminals, and Python RPC scripts for parallel workstreams.
- **Tooling** - 40+ tools, MCP integration, web search (Firecrawl), browser automation, vision, image gen, TTS.
- **Skills Hub** - compatible with the `agentskills.io` open standard (same skills idea as Claude Code).

### Deployment / models
- **Surfaces:** terminal TUI (multiline edit, slash-command autocomplete, streaming output), native desktop app (macOS 12+, Windows 10/11, Linux), messaging gateways.
- **Sandbox backends:** local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox.
- **Model-agnostic:** Nous Portal (300+ models), OpenRouter, OpenAI, NVIDIA NIM, Bedrock, **Ollama for 100% local**, any OpenAI-compatible endpoint. Switch with `hermes model`.
- **Runs on a $5 VPS** up to GPU clusters or serverless with hibernation.
- Paid tiers (Free / Plus / Super / Ultra) exist only for hosted model credits via Nous Portal; the agent itself is free + self-hostable.
- Migrates from OpenClaw in one command: `hermes claw migrate` (settings, memories, skills, API keys).

### Why it fits Tyler's channel
It rhymes with Claude Code (skills, memory, cron/scheduling, MCP) but is model-agnostic, self-hosted, and always-on. Perfect "here's the open-source cousin of the tool you already love, and it does the automation piece Claude Code doesn't" angle. Ties straight into Tyler's existing automation/scheduling content.

---

## 2. YouTube landscape

Two searches run (files in `~/content/research/`): title-matched last 45 days (3 videos) and broad "Hermes Agent" last 120 days (20 videos). Real view counts pulled per video.

### Top performers (broad, by views)

| Views | Dur | Date | Channel | Title |
|------:|-----|------|---------|-------|
| 349,120 | 58:22 | 05-10 | Nate Herk / AI Automation | Hermes Agent: Zero to Personal AI Assistant (1 Hour Course) |
| 313,962 | 29:40 | 07-20 | Tina Huang | Hermes Agent Fundamentals In 29 Minutes |
| 195,894 | 4:53 | 05-23 | CodeHead | Hermes Agent Explained In 5 Minutes |
| 194,153 | 15:18 | 05-22 | Alex Finn | 6 Hermes Agent use cases I promise will change your life |
| 189,716 | 29:11 | 05-28 | zSecurity | I Built an AI Hacking Team with Hermes Agent (And YOU can too) |
| 160,530 | 43:48 | 06-06 | Greg Isenberg | Hermes Agent Desktop: Full Setup + Real Use Cases |
| 159,626 | 44:14 | 05-26 | Alex Finn | Hermes Agent is the greatest AI tool ever made. Here's how to set it up |
| 158,368 | 47:00 | 05-06 | David Ondrej | 100 hours of Hermes Agent lessons in 46 minutes |
| 150,074 | 9:29 | 06-15 | Metics Media | OpenClaw vs Hermes Agent (Don't choose WRONG!) |
| 133,182 | 25:35 | 06-17 | Jack Roberts | Every Level of Hermes Agent Explained |
| 127,185 | 9:54 | 05-10 | WorldofAI | Hermes Agent NEW Desktop App - The 24/7 Self-Evolving AI Agent! |
| 124,719 | 33:48 | 05-28 | Metics Media | Hermes Agent Tutorial for Beginners (Full Step-by-Step Setup) |
| 121,236 | 19:04 | 06-05 | Jack Roberts | Hermes Agent + Ollama = 100% Private OS |
| 116,279 | 3:02:47 | 07-10 | Samin Yasar | HERMES AGENT FULL COURSE 3 HOURS: Build & Sell |
| 104,669 | 8:48 | 05-25 | WorldofAI | Hermes Agent + DeepSeek V4 (FREE) = GOD TIER |

### Read on the field
- **NOT under-discussed at the top.** Big channels (Tina Huang 314k, Nate Herk 349k, David Ondrej, Greg Isenberg) already covered it in the May-June launch wave. The "nobody's talking about this" framing will not survive contact - drop it. The real opening is that Tyler's specific audience (Claude Code / builder) has NOT been served a Claude-Code-native take.
- **Two-wave shape:** heavy May-June launch spike, thinner July, almost nothing recent. That's an opening - a fresh, current take on a tool that's had major updates (Grok 4.5, Kimi K3, parallel tool calls, 60x faster Firecrawl search per Jack Roberts' July video) has low recent competition.
- **Formats that won:** (a) "in N minutes" fast explainers (CodeHead 196k in 5 min), (b) use-case listicles (Alex Finn "6 use cases" 194k), (c) full setup courses, (d) tool-vs-tool (OpenClaw comparison 150k), (e) local/private angle (Ollama = 100% Private, DeepSeek FREE = GOD TIER both 100k+).
- **Recurring winning modifiers in titles:** "Private / 100% local", "FREE", "self-evolving / 24-7", "use cases", "vs OpenClaw", model pairings (+Ollama, +DeepSeek, +MiniMax).

### Thumbnail patterns (from actual images)
- The Hermes **brand mark** - a black-and-white anime girl with headphones + Nous "N" - appears in nearly every thumbnail. Strong recognition device; put it on screen.
- Face + 2-3 word bold overlay, extreme contrast. Palettes: orange/black (Alex Finn), yellow/black (CodeHead), blue accent (Tina Huang "It's So EASY").
- Pointing at the logo or the terminal screen. Arrows onto the two logos for the "vs" video.
- Terminal screenshot as backdrop for the "easy/setup" angle sells the "you run this yourself" idea.

---

## 3. Video ideas (Tyler's lane: Claude Code / builder audience)

Formula = specific number + specific outcome + specific tool. No money in titles, no em dashes.

**Long-form**
1. **"I Replaced My Claude Code Cron Jobs With This Free Open-Source Agent"** - Hermes' built-in scheduler + always-on gateway vs the Claude Code scheduling setup Tyler already teaches. Native to his audience, nobody's done the Claude-Code-user framing.
2. **"Hermes Agent vs Claude Code: The One Thing Claude Can't Do"** - honest builder comparison, memory + always-on ops as the wedge. Tool-vs-tool is proven (150k on the OpenClaw comparison), and Tyler has the Claude Code authority to make it credible.
3. **"I Ran an AI Agent 100% Local With Ollama (No API Keys, No Cloud)"** - the private/local angle over-indexed hard (Ollama 121k, DeepSeek 105k). Hermes + Ollama, self-hosted on a cheap VPS, memory that never leaves your machine.
4. **"This Agent Writes Its Own Skills While It Works"** - deep-dive on the self-improving loop, mapped to the skills concept his audience knows from Claude Code. The most genuinely novel mechanic; underexplained in existing videos.
5. **"I Gave One Agent Telegram, Slack, and My Terminal - Same Brain Everywhere"** - the unified-memory-across-gateways demo. Very demo-able, visually distinct from the setup-tutorial pack everyone else made.

**Shorts** (zero Shorts in the search window = wide open)
1. "The AI agent that remembers everything you told it last week" - memory hook, 30s.
2. "Run a private AI agent for the price of a coffee a month" - $5 VPS + Ollama, no money figure in title if repurposed.
3. "Claude Code can't do this one thing. This free agent can." - the cron/always-on wedge in 40s.
4. "One command migrates your whole agent off OpenClaw" - `hermes claw migrate` quick tip.
5. "Your AI agent, now living in your Telegram" - gateway demo clip.

---

## 3b. LOCKED SLATE (2026-08-25)

Tyler picked: How I Use It Daily + 100% Local/Private, and liked the "Full Setup + Real Use Cases" format and the "in X minutes" format.

**Video 1 - FLAGSHIP.** "How I Actually Use Hermes Agent Every Day (Full Setup + 5 Real Workflows)"
- Merges Greg Isenberg's "Full Setup + Real Use Cases" (161k) with Tyler's personal-workflow angle, framed for Claude Code builders.
- Best references: Greg Isenberg `EJm8Ka-gVOc` (setup+use cases), Nate Herk `gb5TlGw6Uks` (zero-to-assistant, 349k), Alex Finn `AQHlyGA2cZM` (6 use cases, 194k).

**Video 2 - 100% Local/Private.** "I Ran a 100% Private AI Agent With Ollama (No Cloud, No API Keys)"
- Best reference: Jack Roberts `RoBD7Lc-0MI` (Hermes + Ollama = 100% Private OS, 121k).

**Video 3 - Fast explainer (entry point).** "Hermes Agent Explained in 10 Minutes (Claude Code Users Start Here)"
- Time-boxed format (Fundamentals 314k, Explained in 5 Min 196k). Feeds 1 and 2.

## 4. Recommendation

Lead with idea #1 or #2 - the **Claude-Code-user framing** is the gap none of the big launch-wave videos filled. Keep the "underrated" angle out of the title (it's been covered by huge channels); instead position it as the open-source, self-hosted, always-on complement to Claude Code, which is exactly Tyler's authority and audience.

Next step: `/transcribe` the top 2 references (Tina Huang `5_N84t1rUU0`, Jack Roberts updates `sJt1sQO87sc`) to feed `/yt-package`.

---

## Sources
- github.com/NousResearch/hermes-agent
- hermes-agent.nousresearch.com
- YouTube search data: `~/content/research/2026-08-25-hermes-agent.json` + `-thumbnails/`
