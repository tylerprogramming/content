# Arcade.dev Course — Project

The hands-on project for the full Arcade.dev course (video 047). Open this folder in your IDE and work through it in order. Each module is self-contained.

> One idea ties it together: **Arcade handles auth, so the same connected tools work everywhere** — in Claude Code, in your own Python, and inside any agent framework.

## What you'll build

| Module | Folder | What |
|---|---|---|
| 1 | `01-claude-code/` | Connect your apps to Claude Code (gateway + `claude mcp add`). |
| 2 | `02-custom-tool/` | Build and deploy your **own** custom Arcade tool / MCP server. |
| 3 | `03-langchain/` | Drive the same tools from a **LangChain / LangGraph** agent. |
| 4 | `04-crewai/` | Drive the same tools from a **CrewAI** crew. |
| 5 | `05-scheduled-agent/` | The **Morning Planner**: ClickUp → Claude plans → writes Calendar time-blocks. Runs on a schedule on a VPS. |
| — | `deploy/` | Host the scheduled agent on a Hostinger VPS (cron / systemd). |

## Setup

1. **Python 3.11+**. Create a venv:
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```
2. **Install deps** (pinned versions land after research):
   ```
   pip install -r requirements.txt
   ```
3. **Secrets**: copy `.env.example` to `.env` and fill it in. **Never commit `.env`** (it's gitignored).
   ```
   cp .env.example .env
   ```

## Accounts you'll need
- Arcade (API key) · Anthropic (Claude API key) · Google (Calendar + Gmail) · ClickUp · optional Hostinger VPS.

## Safety rules baked into this project
- Anything that **writes** (calendar events, emails) runs in **draft / safe mode** or into a **wipeable "AI Plan" calendar** until you trust it.
- **No tokens in code.** Arcade holds the per-user OAuth; your `.env` only holds API keys, and `.env` is gitignored.

> Code in each module folder is filled in from **verified, current Arcade docs** (2026). This README's setup will be finalized with exact package versions once research is complete.
