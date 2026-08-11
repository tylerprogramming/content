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

## Setup (uv — the modern standard)

Deps live in `pyproject.toml`, locked in `uv.lock`, on **Python 3.12** (pinned in `.python-version`). uv installs that Python for you — into its own managed dir, shared across projects, never touching your system Python.

1. **Install uv** once: `brew install uv` (or `pip3 install uv`, or the installer at https://docs.astral.sh/uv).
2. **Create the env + install everything** (uv fetches Python 3.12 automatically):
   ```
   uv sync
   ```
3. **Install the custom-server CLI** for module 2 (a separate global tool):
   ```
   uv tool install arcade-mcp
   ```
4. **Secrets**: copy `.env.example` to `.env` and fill it in. **Never commit `.env`** (gitignored).
   ```
   cp .env.example .env
   ```
5. **Run** anything through uv — no manual activate needed:
   ```
   uv run 05-scheduled-agent/morning_planner.py --discover
   uv run 03-langchain/email_agent.py
   uv run 04-crewai/main.py
   ```

> **pip fallback** (if you don't want uv): `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` — but you'll need Python 3.11+ installed yourself.

## Accounts you'll need
- Arcade (API key) · Anthropic (Claude API key) · Google (Calendar + Gmail) · ClickUp · optional Hostinger VPS.

## Safety rules baked into this project
- Anything that **writes** (calendar events, emails) runs in **draft / safe mode** or into a **wipeable "AI Plan" calendar** until you trust it.
- **No tokens in code.** Arcade holds the per-user OAuth; your `.env` only holds API keys, and `.env` is gitignored.

> Code in each module folder is filled in from **verified, current Arcade docs** (2026). This README's setup will be finalized with exact package versions once research is complete.
