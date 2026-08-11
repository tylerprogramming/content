# Arcade.dev — Verified Research (2026-08-11)

Live-docs research backing the 047 course + `project/` code. Each section is sourced. **No fabricated APIs** — anything unconfirmed is flagged.

---

## MODULE 3 — Build your own custom tool / MCP server  ✅ researched

**Headline:** The old **Arcade TDK** (`arcade_tdk` / `arcade serve` worker) is **superseded by `arcade-mcp`** (GA 2025-10-17). Current framework = `arcade-mcp`: an `MCPApp` object + `@app.tool` decorator. This powers Arcade's prebuilt tools and is open-source.

### Install
```
uv tool install arcade-mcp        # primary (README uses uv exclusively)
```
- CLI/package: **`arcade-mcp`** (provides the `arcade` CLI)
- Import module: **`arcade_mcp_server`** (e.g. `from arcade_mcp_server import MCPApp`)
- ⚠️ exact `pip install arcade-mcp` line not verbatim-confirmed (README shows only `uv`).

### Scaffold
```
arcade new my_server
cd my_server/src/my_server
```
Creates `pyproject.toml`, `.env.example`, `server.py` (with example tools). Nested layout: `my_server/src/my_server/`. ⚠️ full file tree not published.

### Define a tool (minimal)
```python
from typing import Annotated
from arcade_mcp_server import MCPApp

app = MCPApp(name="my_server", version="1.0.0")

@app.tool
def greet(name: Annotated[str, "Name to greet"]) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(transport="stdio")
```

### OAuth-protected tool
```python
from typing import Annotated
import httpx
from arcade_mcp_server import Context, MCPApp
from arcade_mcp_server.auth import Google  # built-in providers in arcade_mcp_server.auth

app = MCPApp(name="auth_example", version="1.0.0")

@app.tool(requires_auth=Google(scopes=["https://www.googleapis.com/auth/calendar.readonly"]))
async def list_calendars(context: Context) -> dict:
    """List the user's calendars."""
    token = context.get_auth_token_or_empty()
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient() as client:
        r = await client.get("https://www.googleapis.com/calendar/v3/users/me/calendarList", headers=headers)
        r.raise_for_status()
        return r.json()
```

### Custom OAuth provider + secrets
```python
from arcade_mcp_server.auth import OAuth2
@app.tool(requires_auth=OAuth2(id="your-oauth-provider-id", scopes=["scope1"]))
async def custom_tool(context: Context) -> dict: ...

@app.tool(requires_secrets=["API_KEY"])
async def with_secret(context: Context) -> dict:
    key = context.get_secret("API_KEY")
    ...
```
- Params typed `Annotated[type, "desc"]` (string = LLM-facing description); docstring = tool description.
- `context` injected automatically when auth/secrets needed; hidden from the LLM.
- Token: `context.get_auth_token_or_empty()`. Secret: `context.get_secret("NAME")`.
- Use **`@app.tool`** for arcade-mcp (the standalone `@tool` is the legacy TDK form).

### Run locally
```
uv run server.py            # stdio (default)
uv run server.py http       # HTTP+SSE, docs at http://127.0.0.1:8000/docs
arcade configure claude     # wire into Claude Desktop/Code
```

### Deploy
```
arcade login
arcade deploy -e src/my_server/server.py
```
- Run from the dir with `pyproject.toml`. **No `worker.toml`** (that was the old TDK model).
- Entrypoint must call `MCPApp.run()`.
- Deploy validates, health-checks, uploads/discovers secrets, packages, and stands up a **cloud-hosted MCP server** on Arcade Cloud, registered to your tool catalog.
- Call it via: (1) an **MCP Gateway** (pick tools → MCP endpoint URL for clients), or (2) **Arcade clients/SDK** directly.
- Ops: `arcade server logs/list/status`, `arcade dashboard`.
- ⚠️ explicit hosted MCP URL string format not printed in docs (surfaced via dashboard/gateway).

### Pricing / tier
- **Hobby (Free):** 1 Arcade-hosted MCP server, 1,000 std + 50 pro executions/mo, 100 auth challenges/mo → **you can deploy one custom hosted server free.**
- **Growth ($25/mo):** usage-based; hosted servers ~$0.05/server-hour; unlimited self-hosted workers.
- ⚠️ pricing from secondary summaries — confirm on live pricing page.

### 2026 changelog highlights
- 2026-01-16 — arcade-mcp: Ed25519, dep fixes.
- 2026-01-09 — expiring API keys; **Arcade Evals** for arcade-mcp; docs overhaul; Windows compat.
- 2025-12-12 — **OAuth added to arcade-mcp servers**; CLI multi-org/project.
- 2025-11-07 — `arcade deploy` supports arcade-mcp.
- 2025-10-17 — **arcade-mcp GA; TDK superseded; Projects & MCP Gateways GA.** (pivotal)

### Sources
- github.com/ArcadeAI/arcade-mcp (README)
- docs.arcade.dev/home/build-tools/create-a-tool-with-auth
- docs.arcade.dev/home/build-tools/tool-context
- docs.arcade.dev/home/serve-tools/arcade-deploy
- docs.arcade.dev/en/references/changelog
- arcade.dev/blog/introducing-arcade-deploy-instant-hosting-for-your-custom-ai-tools

---

## MODULE 4 — LangChain integration  ✅ researched

**Headline:** `langchain-arcade` is **DEPRECATED** (PyPI v2.0.1, 2026-02-04: "no longer maintained"). No more `ArcadeToolManager`/`ToolManager`. Current pattern (docs last-updated 2026-07-27): load tools via `arcadepy.AsyncArcade`, wrap each as a LangChain `StructuredTool`, run in a LangChain 1.0 agent via `create_agent`. Auth = per-tool `tools.authorize` → LangGraph `interrupt` → `auth.wait_for_completion` → `Command(resume=...)`.

- Install: `pip install arcadepy langchain langchain-anthropic langgraph python-dotenv`
- Imports: `from langchain.agents import create_agent` (NOT `create_react_agent`), `from langgraph.types import Command, interrupt`, `from langchain_core.tools import StructuredTool`.
- Tool ids: fully-qualified, e.g. `Gmail_ListEmails`; fetch via `client.tools.get(name=...)` or `client.tools.list(toolkit=...)`.
- Claude swap: `from langchain_anthropic import ChatAnthropic; ChatAnthropic(model="claude-opus-4-8", api_key=...)`.
- **Working file:** `project/03-langchain/agent.py` (from the doc example, adapted to Claude).
- Sources: docs.arcade.dev/home/langchain/use-arcade-tools · /home/langchain/user-auth-interrupts · pypi.org/pypi/langchain-arcade/json

## MODULE 5 — CrewAI integration  ✅ researched

**Headline:** `crewai-arcade` is **DEPRECATED** (PyPI v2.0.1, 2026-02-23). No `ArcadeToolManager`/`CrewAIToolManager`. Current pattern (docs 2026-07-27): install plain CrewAI + arcadepy, paste an `ArcadeTool(BaseTool)` wrapper + `get_arcade_tools()` helper. Auth handled inside `ArcadeTool._auth_tool()` (authorize → print url → `wait_for_completion`).

- Install: `pip install 'crewai[tools]' arcadepy python-dotenv` (Python ≥3.10). Do NOT `pip install crewai-arcade`.
- Imports: `from crewai import Agent, Crew, LLM, Task` · `from crewai.tools import BaseTool` · `from arcadepy import Arcade`.
- Claude: `LLM(model="anthropic/claude-opus-4-8", max_tokens=4096)` (max_tokens REQUIRED for Anthropic; use the native `LLM` class to avoid LiteLLM grabbing OPENAI_API_KEY).
- **Working file:** `project/04-crewai/main.py` (Arcade wiring verbatim from docs; LLM/runner adapted).
- Sources: docs.arcade.dev/en/home/crewai/use-arcade-tools · docs.crewai.com/en/concepts/llms · pypi.org/project/crewai-arcade

> **Teaching point (both frameworks):** LangChain and CrewAI both deprecated their Arcade packages and converged on the same shape — use `arcadepy` and wrap its `authorize`/`execute` for the framework. Learn the SDK once, use it anywhere.

## MODULE 1 + 6 — arcadepy client, concepts, gateways, latest  ✅ researched

### arcadepy (Module 6 scheduled agent)
```python
from arcadepy import Arcade            # or AsyncArcade
client = Arcade()                      # reads ARCADE_API_KEY
auth = client.tools.authorize(tool_name="GoogleCalendar.CreateEvent", user_id="you@example.com")
if auth.status != "completed":
    print(auth.url); client.auth.wait_for_completion(auth.id)
resp = client.tools.execute(tool_name="GoogleCalendar.CreateEvent",
    input={"summary": "Sync", "start_datetime": "2026-08-20T15:30:00", "end_datetime": "2026-08-20T16:30:00"},
    user_id="you@example.com")
print(resp.output.value)               # tool output on resp.output.value
```
- Methods confirmed: `client.tools.authorize`, `client.tools.execute`, `client.auth.wait_for_completion`. Per-user tokens stored by Arcade under `user_id`; none in your code.
- **Working file:** `project/05-scheduled-agent/morning_planner.py`.
- ⚠️ Exact **ClickUp** task-tool name + inputs NOT confirmed — the planner has a `--discover` mode that lists a toolkit's real tool names; confirm before filming. `GoogleCalendar.CreateEvent` input `{summary,start_datetime,end_datetime}` IS confirmed; `ListEvents` + a `calendar_id` arg are flagged TODO.

### Concepts (Module 1 glossary — from docs)
- **Tool** — a function an agent can call to take an action (API/fs/db).
- **MCP Server** — a themed collection of tools + the process that serves them (what older docs called a "Toolkit").
- **Toolkit** — a named provider bundle (Gmail, Calendar, Slack, Linear, Excel…). 7,000+ integrations.
- **MCP Gateway** — connect multiple MCP servers to your agent/IDE behind one URL; routes + enforces policy.
- **Engine** — the hosted (or self-hostable) runtime between agent and external systems; routes calls, runs OAuth, stores tokens.
- **Worker** — the deployed process running an MCP server's code.
- **Auth/OAuth provider** — the service users sign in with (Google, GitHub, Slack…).

### Gateways (Module 1)
- MCP URL pattern CONFIRMED: `https://api.arcade.dev/mcp/{gateway-slug}` — what Claude Code connects to.
- Create in dashboard: api.arcade.dev/dashboard/mcp-gateways → Create → name+slug+tools+auth-mode → copy URL.
- Auth modes: Arcade Auth (internal) · User Source/OIDC (production) · Arcade Headers (API-key fallback).
- ⚠️ Programmatic gateway creation via API NOT documented (dashboard only).

### Latest 2026
- **$60M Series A (2026-06-15)**; positioning = "the secure action layer behind every production AI agent" (governs what an agent may do, as whom, fully audited).
- Joined Linux Foundation's Agentic AI Foundation (Gold). Arcade tools in LangChain LangSmith **Fleet**.
- Changelog highlights: `Arcade.ListApps` builtin (2026-07-17); stateless MCP tools/list+call; OAuth RFC 9207; new toolkits (Power BI, Postman, Fireflies, Nimble…).

### Sources
- docs.arcade.dev/en/home/quickstart · /get-started/quickstarts/call-tool-agent · /home/glossary · /guides/mcp-gateways · /references/changelog
- github.com/ArcadeAI/arcade-py · businesswire (Series A) · langchain.com/blog (Fleet)

---

## ⚠️ Confirm-on-film-day (unresolved from live docs)
- Exact `pip install arcade-mcp` line (README shows only `uv tool install`).
- Exact ClickUp task-tool name + input schema (use planner `--discover`).
- `GoogleCalendar.ListEvents` param names + `CreateEvent` `calendar_id` arg.
- Current Arcade pricing numbers (secondary sources only).
- Programmatic gateway creation (dashboard-only as far as docs show).
