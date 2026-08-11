# Build AI Agents in 2026 — The Blueprint

> The free download for the course. One page: the pattern, the five things you build, and the rules that keep it safe. Pairs with the Setup Pack (`project/INSTALL.md`) and the code.

## The one idea
**Connect your accounts once. Use that connection everywhere.** Through Arcade, the same connected tools work in Claude Code, in your own Python, inside LangChain or CrewAI, and in an agent that runs on a schedule. You never store a password or an auth token.

## The pattern (every agent is these 3 steps)
1. **Connect** — pick your tools in an Arcade gateway, get one URL. Arcade runs the OAuth and holds the tokens.
2. **Give an agent the tools** — a goal + the connected tools + plain instructions. Same tools, any surface.
3. **Let it act** — in safe mode first (drafts, or a wipeable calendar). You approve, then loosen the leash.

## What you build in this course
| Build | What it proves |
|---|---|
| **Claude Code on your apps** | Use prebuilt tools with one command (`claude mcp add`). |
| **Your own tool / MCP server** | Build + deploy a custom tool with `arcade-mcp` (free tier hosts one). |
| **LangChain agent** | The same tools, driving a LangGraph agent. |
| **CrewAI crew** | The same tools again, another framework. |
| **Morning Planner (scheduled)** | Reads your ClickUp tasks + calendar, blocks your day, runs on a VPS every morning. |

## The rule that makes it safe
- **Draft before send, always** — anything that writes starts reversible.
- **Arcade holds the auth**, not your code. Every run is logged.
- **Start narrow** — two tools, one job. Add more once it earns it.

## The 2026 reality (why most tutorials are wrong now)
- The old `langchain-arcade` and `crewai-arcade` packages are **deprecated**. Both frameworks now just wrap the **Arcade SDK** (`arcadepy`). Learn the SDK once, use it anywhere.
- Custom tools/servers use **`arcade-mcp`** (`MCPApp` + `@app.tool` + `arcade deploy`), not the old TDK.
- It's model-agnostic too: swap OpenAI for Claude with one setting, the tools don't change.

## Get building
- **Setup Pack** (install the agents in ~10 min): `INSTALL.md`
- **The code** (every module, runnable): the project folder
- Free community + walkthrough: [funnel link]

Blueprint by Tyler Reed · @TylerReedAI · built with Claude Code + Arcade
