# Analysis — Hermes Agent (Start Here)

## Source transcript analysis

### Primary reference: Tina Huang, "Hermes Agent Fundamentals In 29 Minutes" (313,962 views)

**Structure:**
| Time | Segment | Purpose |
|---|---|---|
| 0:00-0:44 | Hook + outline | "Setting it up right is the difference." Shows her multi-agent system + Obsidian second brain running. |
| 0:44-2:55 | Hardware choices | 4 options: dedicated local (Mac Studio), VPS ($5-6), old laptop, personal PC + Docker. |
| 2:55-7:45 | Install + first run | Desktop app vs terminal; pick a model; tell it about yourself; where memory lives (.hermes folder). |
| 7:45-15:47 | 5 major features | Tools, integrations/MCP, skills (the famous one), cron jobs. |
| 15:47-23:00 | Memory deep dive | 4 tiers: core files, session search (SQLite), Honcho plugin, Obsidian second brain. |
| 23:00-25:40 | Open-source local models | Ollama / llama.cpp, Qwen local driver, free + private. |
| 25:40-29:40 | Multi-agent payoff | Discord-driven parallel builds, compound board orchestration. |

**What works:** immediate proof (systems running in the hook), "everything is easy, just ask Hermes to set it up" repeated as a through-line, concrete file paths shown on screen, honest about cost. Ease framing throughout ("cookie for anybody").

**Weaknesses / our opening:** it is 29 minutes and assumes zero prior agent knowledge, so it spends a long time on hardware and 4 tiers of memory. It has **no Claude Code framing at all** - it treats Hermes as a first agent, not as the complement to a coding agent the viewer already runs. It also predates the v0.20 update (voice, desktop platform, new CLI commands). Our differentiation: **half the length, aimed at people who already use Claude Code, three features not five, and current.**

**Audience:** Tina's is for general AI-curious beginners. Ours is narrower and warmer - existing Claude Code / builder users - which is exactly Tyler's lane and authority.

### Secondary references
- **Greg Isenberg, "Hermes Agent Desktop: Full Setup + Real Use Cases" (160,530):** desktop-first, use-case heavy. Confirms the setup+use-case format travels. `transcript_hermes_greg.txt`
- **Nate Herk, "Zero to Personal AI Assistant (1 Hour Course)" (349,120):** the biggest on the topic, long-course framing. `transcript_gb5TlGw6Uks.txt`

---

## Web research

### What Hermes Agent is
Open-source, self-hosted, MIT-licensed AI agent by Nous Research. Released Feb 25, 2026. ~236k GitHub stars, ~47k forks. Not a coding copilot, not a chatbot wrapper - an always-on background process you control.

### Core mechanics
- **Self-improving learning loop (headline):** solves a task, auto-writes a reusable markdown skill file, reloads it next time. No YAML/manual config; handled internally.
- **Persistent memory:** `.hermes` folder with plain-markdown core files (user / memory / soul) as tier one; every session written to a SQLite FTS5 DB with LLM summarization as tier two (session search). Optional tier three (Honcho user-modeling plugin) and tier four (Obsidian second brain).
- **Built-in cron:** natural-language scheduling, runs unattended through the gateway.
- **Gateways:** one agent + one memory across Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI. Live voice in Discord voice channels.
- **Subagents:** isolated subagents with own conversations, terminals, Python RPC. Native "compound board" orchestration.
- **Tooling:** 40+ tools, MCP integration, web search (Firecrawl), browser automation, vision, image gen, TTS.
- **Skills Hub:** compatible with the `agentskills.io` open standard (same skills concept as Claude Code).

### Deployment / models
- Surfaces: terminal TUI, desktop app (macOS 12+, Win 10/11, Linux), messaging gateways.
- Sandbox backends: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox.
- Model-agnostic: Nous Portal (300+ models), OpenRouter, OpenAI, NVIDIA NIM, Bedrock, **Ollama for 100% local**, any OpenAI-compatible endpoint. Switch with `hermes model`.
- Runs on a $5 VPS up to GPU clusters or serverless with hibernation.
- Install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` (mac/Linux/WSL2); PowerShell one-liner on Windows.
- Migrates from OpenClaw: `hermes claw migrate`.

### Recent updates (timeliness hook)
- **Latest: v0.20.5 (Aug 19, 2026)** - patch on top of the v0.20 "Herald Release."
- **v0.20 "Herald":** real-time conversational voice (streaming TTS, barge-in, on-device wake words), A2A v1.0, a full desktop platform (versioned artifact cards, sandboxed live preview, a plugin SDK with Kanban as the first plugin, floating panes / multi-window).
- **New CLI power-user commands (very Claude-Code-adjacent):** `!command` to run shell instantly, `/init` to generate or update an `AGENTS.md`, `/diff` for staged/session changes, `/context` for context-window breakdown, `/focus` for reduced output, `Ctrl+S` to stash a half-written prompt.
- **Web dashboard admin panel:** MCP catalog toggles, credential + webhook/hook management, gateway controls without SSH.

### Competitive landscape
- **vs Claude Code:** Hermes = autonomous always-on ops agent; Claude Code = interactive in-repo coding specialist. They rarely compete for the same task. Hermes wins on persistent memory + always-on + model-agnostic + voice; Claude Code wins on raw coding and a zero-infra managed experience (included in Claude Pro/Max). One 18-task test: Hermes 14, Claude Code 4 (Claude took the pure-coding tasks; Hermes won by remembering prior sessions).
- **vs OpenClaw:** Hermes positioned as the successor; one-command migration exists. "OpenClaw vs Hermes" comparisons pulled 150k.

### YouTube demand / gap
- Head term passes the demand gate (big channels covered it in the May-June launch wave; coverage thinned after June).
- **Gap:** nobody has done the Claude-Code-user framing, and nobody has covered the fresh v0.20 update in a short beginner setup. Zero Shorts in the search window.

---

## Sources
- https://github.com/NousResearch/hermes-agent
- https://hermes-agent.nousresearch.com/
- https://the-agent-report.com/2026/08/hermes-agent-v020-herald-release-august-2026/
- https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.16.2
- https://fast.io/resources/hermes-agent-vs-claude-code/
- https://pub.towardsai.net/i-tested-hermes-agent-vs-claude-code-vs-openclaw-on-18-real-tasks-the-10-week-old-one-cheats-by-0f2881a10213
- https://www.mindstudio.ai/blog/what-is-hermes-agent-openclaw-alternative
- Local research brief: `~/content/research/youtube/hermes-agent-nous/index.md`
- YouTube search data: `~/content/research/2026-08-25-hermes-agent.json` + `-thumbnails/`

---

## Memory model — verified against the docs 2026-08-31

Source: `hermes-agent.nousresearch.com/docs/user-guide/features/memory`. Not yet confirmed on a
running install, so **check the folder on camera before narrating the file count.**

### The actual model (two tiers, and the caps are what explain it)

| | What | Where | Limit |
|---|---|---|---|
| **Tier 1** | `MEMORY.md` (agent's own notes) + `USER.md` (user profile) | `~/.hermes/memories/` | **2,200 chars (~800 tok)** and **1,375 chars (~500 tok)** |
| **Tier 2** | Every session, full-text searchable, LLM-summarized | `~/.hermes/state.db` (SQLite FTS5) | unbounded |

**Why the caps exist, and why this is the beat:** tier 1 loads as a **frozen snapshot into the
system prompt at session start** — every session, every time. So it must stay small or you pay for
your whole history on every message. That reframes the cap from a limitation into the architecture:
**a tiny always-loaded profile plus an unlimited on-demand archive.** Nobody in the competitor set
explains this.

### Corrections to the earlier script
- Path is **`~/.hermes/memories/`** (plural), files are **UPPERCASE**. Script said `memory/user.md`.
- **Two** core memory files, not three. Tina names a third (`SOUL.md`) as the persona file; the memory
  docs describe only two bounded stores. Verify in the folder.
- The `memory` tool has three actions: **add / replace / remove**. There is **no read action** — the
  content auto-injects into context.

### Zero-friction alternatives to Honcho (what to show instead)

Both are first-party, both are config lines, neither needs an account:

1. **`background_review`** — a post-turn self-improvement fork that saves discoveries to memory and
   skills automatically. Can be pointed at a cheaper model.
```yaml
auxiliary:
  background_review:
    enabled: true
    provider: openrouter
    model: google/gemini-3-flash-preview
    extra_tools: []
```
2. **`write_approval`** — stage every memory write for human approval instead of writing straight
   through. Review the queue with **`/memory pending`** (and `/skills pending` for skills).
```yaml
memory:
  write_approval: false   # true = stage all writes for approval
skills:
  write_approval: false
```

`write_approval` is the better demo of the two: it is visual (a queue you can show), it is a
one-line change, and "memory with a code review step" is the engineer read. **Use these as tier 3
instead of Honcho** — Honcho is a third-party signup with credits, which is friction in a
start-here video and dates the video if it changes.
