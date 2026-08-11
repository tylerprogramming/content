# 047 — The Full Arcade.dev Course (~1 hour)

**Lane:** arcade.dev series capstone. The comprehensive one that ties the whole arc together.
**Status:** BUILDING (2026-08-11). Research in flight (Arcade custom-tool/deploy, LangChain, CrewAI, arcadepy + concepts + latest). Code project scaffolded at `project/`; code fills in once research lands.
**Target runtime:** 55-65 min. Chaptered, modular, project-based.

**Working title:** How to Build AI Agents in 2026 (The Right Way) — options in `titles.md`.
**Code repo:** https://github.com/tylerprogramming/arcade-course (the runnable project + INSTALL — see `CODE.md`; no longer mirrored in this repo).
**LLM:** OpenAI `gpt-5.4-mini` for filming/testing (viewer's own credits); one env var (`LLM_PROVIDER`) flips to Claude. Model-agnostic is a teaching beat.
**Hook:** value-forward, see `hooks.md` (Hook 1).

## The value (the spine — say it in the hook, deliver it in the build)
By the end, the viewer can build real AI agents connected to anything they use, with **no auth headaches**, and it's **simpler than they expect**. They leave with **agents they actually use**, a **free blueprint**, and a **setup pack** to install them.

## Free downloads (lead magnets)
- **Blueprint** — `blueprint-build-ai-agents.md` (one-page system + the 5 builds). Offer as a shareable page/PDF.
- **Setup Pack** — `project/INSTALL.md` (install the agents in ~10 min, copy-paste, uv-based).
- **The code** — the runnable `project/` folder.

## Thesis
One video that takes you from "what is Arcade" to a real, working project: your apps in Claude Code, your OWN custom MCP server, the same tools driving a LangChain agent AND a CrewAI crew, and a scheduled agent running on a VPS with access to your stuff. The through-line: Arcade handles auth, so the SAME tools work everywhere — Claude Code, your own code, any framework.

## What the viewer walks away with
- A clear mental model of Arcade (tools, toolkits, gateways / MCP servers, auth, workers).
- Their apps connected to Claude Code (recap of 045/046).
- A **custom MCP server / tool they built and deployed** with Arcade.
- The same tools running inside **LangChain** and **CrewAI**.
- A **scheduled agent on a VPS** (the Morning Planner: ClickUp → plan → write Calendar blocks), hosted on Hostinger.
- The full **project repo** (`project/`) they can open in an IDE and run.

## Modules (chapters)

| # | Module | ~Time | What's shown / built |
|---|---|---|---|
| 0 | Cold open + what you'll build | 0:00-3:00 | Montage of the finished pieces (Claude Code, custom tool, LangChain agent, CrewAI crew, scheduled planner writing to a calendar). Promise the whole project. |
| 1 | What Arcade actually is (concepts) | 3:00-9:00 | The problem (tools + auth, auth is the hard part). Concepts: tools, toolkits, gateways / MCP servers, engine, workers, auth/OAuth. One-line: a runtime that handles auth so tools work everywhere. |
| 2 | Use Arcade in Claude Code | 9:00-17:00 | Fast recap of 045/046: build a gateway (Gmail + Calendar), `claude mcp add`, authorize once, use it. The "using an MCP server" baseline. |
| 3 | Build your OWN MCP server / custom tool | 17:00-31:00 | Tool SDK: scaffold a toolkit, write a custom tool (function + auth requirement), run locally, test, **deploy** it with Arcade so it's a hosted tool with a URL, add it to a gateway, call it from Claude Code. |
| 4 | Use Arcade tools in LangChain | 31:00-42:00 | `langchain-arcade`: load tools, build a LangGraph agent, handle the per-user authorize flow in code, run it with Claude. Same tools, a framework. |
| 5 | Use Arcade tools in CrewAI | 42:00-52:00 | `crewai-arcade`: wire tools into a crew, authorize, run a task with Claude. Same tools, another framework — the point: framework-agnostic. |
| 6 | The scheduled agent on a VPS | 52:00-62:00 | The Morning Planner (ClickUp → Claude plans → writes Calendar time-blocks) as a standalone `arcadepy` script. Auth carries over (no tokens in code). Cron it on a **Hostinger VPS** so it runs every morning. Safe pattern: writes to a wipeable "AI Plan" calendar. See `blueprint` (046 package). |
| 7 | Wrap + resources | 62:00-64:00 | Recap, the project repo, where next, CTA. |

## The project repo (`project/`)
```
project/
  README.md              overview + setup + run-order
  .env.example           ARCADE_API_KEY, ANTHROPIC_API_KEY, etc. (real .env is gitignored)
  requirements.txt       pinned deps (filled from research)
  01-claude-code/        gateway + `claude mcp add` notes
  02-custom-tool/        a custom Arcade toolkit + deploy config
  03-langchain/          langchain-arcade agent
  04-crewai/             crewai-arcade crew
  05-scheduled-agent/    the Morning Planner + cron/systemd unit
  deploy/                VPS (Hostinger) setup notes
```

## Prerequisites (state on screen in Module 0)
- Python 3.11+
- An Arcade account + API key
- An Anthropic API key (Claude)
- A Google account (Calendar + Gmail)
- A ClickUp account (for the planner)
- Optional: a Hostinger VPS (for Module 6 hosting)

## Filming approach
- Chaptered, so each module can be filmed and edited as a unit; assemble into one long-form + break modules into standalone shorts/clips later.
- Everything real: real gateway, real deploy, real agents, real runs. Draft/safe mode on anything that writes.
- No keys/tokens on screen: env vars, gitignored `.env`, and Arcade holds the OAuth.
- Disclosure: if sponsored/partner with Arcade (and/or Hostinger for the VPS), say so on camera + in the description. Do not blur two sponsors — call each out plainly where it appears.

## Research: DONE (2026-08-11) — see `research-arcade-2026.md`
All code in `project/` is written against verified, current Arcade docs. Key findings:
- Module 3: custom server = **`arcade-mcp`** (`MCPApp`/`@app.tool`/`arcade deploy`). TDK is dead.
- Module 4: **`langchain-arcade` deprecated** → `arcadepy` + `StructuredTool` + `create_agent`. Code: `03-langchain/agent.py`.
- Module 5: **`crewai-arcade` deprecated** → `arcadepy` + pasted `ArcadeTool` wrapper. Code: `04-crewai/main.py`.
- Module 6: `arcadepy` authorize/execute → the Morning Planner. Code: `05-scheduled-agent/morning_planner.py` + `deploy/` (Hostinger VPS cron/systemd).
- Module 1: concepts glossary + gateway URL `https://api.arcade.dev/mcp/{slug}`. Code: `01-claude-code/README.md`.
- Teaching spine: both frameworks deprecated their Arcade packages and converged on the SDK — learn `arcadepy` once, use it anywhere.

## Confirm on film day (small, flagged in code + research doc)
- Exact ClickUp task-tool name/inputs (planner has a `--discover` mode).
- `GoogleCalendar.ListEvents` params + `CreateEvent` `calendar_id` arg.
- `pip install arcade-mcp` line (README shows `uv` only); current pricing numbers.

## Still to build (next passes)
- The module-by-module **script** (`script.md`) and **filming-guide.md** for the ~1hr shoot.
- `titles.md` / `hooks.md` / `description.md` / `tags.txt` (run /yt-seo after the script).
- Test-run each `project/` module end to end before filming (real accounts, safe mode).
