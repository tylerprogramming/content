# Runsheet — 047 How to Build AI Agents in 2026 (The Right Way)

Format: PROJECT-BASED COURSE, filmed module-by-module (assemble into one ~1hr long-form; each module also stands alone as a clip). Voice: Tyler to a friend. Short sentences. No hype words. No em dashes. Open fast.
LLM: OpenAI `gpt-5.4-mini` on screen (one env flip to Claude). Model-agnostic is a teaching beat.
Everything real: real gateway, real accounts, real deploys, real runs. Draft/safe mode on anything that writes. No keys/tokens on screen (env vars, gitignored `.env`).
[DISCLOSURE: if sponsored/partner with Arcade (and Hostinger for the VPS), say so on camera + in the description. Call each out where it appears; don't blur them.]

> STATUS: Modules 0-2 drafted. Modules 3-7 to write next. Cold open (Module 0) is filmed LAST (needs the module footage for the montage).

---

## MODULE 0 — COLD OPEN + ROADMAP  [film last]

### The hook (result-first)
[SHOW: fast cuts of the payoff — Claude Code pulling Gmail; a terminal printing "Deployed"; a LangChain agent answering; a CrewAI crew running; a calendar at 6:31 AM filling itself with time-blocks.]

"By the end of this, you'll have real AI agents running on your own accounts. Your email, your calendar, your tasks, anything you want to connect. And you'll build them without ever touching an auth token or storing a password. That was always the hard part. It isn't anymore. You'll leave with agents you actually use, plus a free blueprint and a setup pack so you can run them yourself. Let me show you how simple it got."

### The roadmap (say exactly what we're doing + the 24/7 payoff)
[SHOW: Tyler to camera, or a simple 5-step list building on screen.]

"Here's exactly what we're doing. First, I connect my real accounts to an AI, my email, my calendar, my tasks, in one setup, with no auth headaches. Then I build my own tool from scratch and put it online. Then I take those same tools and drop them into two different agent frameworks, LangChain and CrewAI. And to finish, I put an agent on a server so it runs on its own, every single day.

By the end of this, you'll have your own AI agents running 24/7 on your own server. Let's start."

[NOTE: this is the promise. Keep it under ~25 seconds. It's the map for the whole video, so say it plainly and move.]

---

## MODULE 1 — WHAT ARCADE ACTUALLY IS (the concepts, fast) [~5-6 min]  [FILM LAST, with the hook]

[NOTE: talking-head, so record it LAST (after the demos), same as the cold open. The ONLY lecture in the course. Keep it tight and concrete. Build a simple diagram on screen as you name each layer: tool → MCP server → gateway (one URL) → engine.]

[SHOW: Tyler to camera.]

"Before we build anything, give me sixty seconds on how this works, because it's the whole trick of the video.

A real agent needs two things. Tools, and permission to use them. The tools are the easy part. The permission is where everyone gets stuck. Letting an AI into your real Gmail means OAuth, tokens, scopes, refreshing them, keeping them safe. I spent eight years building exactly this at IBM and Chase. It's the part that eats the afternoon, every time.

The whole job of the tool we're using, Arcade, is to take that off your plate."

[SHOW: arcade.dev homepage, tagline "ship agents, not auth infrastructure."]

"Four words and you've got it.

[SHOW: each term appears and stacks into a little diagram as you say it.]

A **tool** is one action. Read an email. Create a calendar event.
A bunch of tools for one app is an **MCP server**. Gmail is one. Calendar is another.
A **gateway** is the tools you pick, bundled behind one URL. Think of it like a front desk with a single address: your agent talks to that one URL, and the gateway figures out which tool to run.
And underneath it all, the **engine** runs the logins and holds your tokens, per user, so you never store one.

So the whole flow is just this: pick your tools, get a URL, and the auth is handled for you.

And here's why that matters. That same setup works in Claude Code, in the Claude desktop app, on the web, in your own Python, inside LangChain or CrewAI, and on a server running while you sleep. You connect once. You use it everywhere. That one idea is the entire course.

Alright. Enough talking. Let's connect some apps."

[NOTE: don't quote a hard tool count on camera unless you re-checked it that day, "thousands" is safe. The deeper gateway detail (routing, auth modes, when you DON'T need one — your Python agents skip it) lives in Module 2 where you actually build the gateway. Keep Module 1 to the four words + the payoff line.]

---

## MODULE 2 — CONNECT YOUR APPS TO CLAUDE CODE  [~8 min]  (project/01-claude-code)

[NOTE: quickest win, and the foundation. Real gateway, real auth.]

### Build the gateway
[SHOW: Arcade dashboard → MCP Gateways → Create MCP Gateway.]

"Step one, I build a gateway. In the Arcade dashboard I hit create, I give it a slug, and I pick the tools I want. For this whole course I'll add Gmail, Google Calendar, and ClickUp. I save it, and it hands me a URL."

[NOTE: set the gateway's auth mode to "Arcade Auth" (NOT "Arcade Headers") — Headers mode is incompatible with Claude Desktop, and we connect Desktop later this module.]

[SHOW: the generated URL, of the form https://api.arcade.dev/mcp/<slug>. Copy it.]

"That URL is my toolbox. Copy it."

### Add it to Claude Code
[SHOW: terminal. Type it live.]

```
claude mcp add arcade --transport http "https://api.arcade.dev/mcp/<your-slug>"
claude mcp list
```

"One command. Add an MCP server called arcade, HTTP transport, here's the URL. Verify it's connected. Done."

### Use it (and the auth moment)
[SHOW: ask Claude Code something real and read-only first.]

> "What's on my calendar today, and which unread emails actually need a reply?"

[SHOW: the first tool call triggers the real Google consent screen. Approve it live.]

"Watch this. First time it touches my Google account, Arcade sends me to Google's real consent screen. I approve it once. And that's the only auth I will ever do. The token isn't in a file, it isn't in my code, Arcade holds it. From here on, it just works."

[SHOW: back in the terminal, the calendar summary + the emails that matter come through.]

"There's my day, and the emails that need me. Real inbox, real calendar, and I never handled a token. That's the foundation. Everything else in this video is just pointing more things at that same connection."

### Same URL, the other Claude apps (Desktop + Web)
[SHOW: Claude Desktop, then claude.ai — add the SAME gateway URL as a custom connector.]

"And this isn't a Claude Code trick. It's just a URL. Let me add the exact same gateway to the Claude desktop app, and to Claude on the web."

[STEPS — verified vs live docs 2026-08 (Arcade + Anthropic). The menu is "Connectors" (not Integrations/Extensions).]

**Claude Desktop:**
1. Avatar (bottom-left corner) → Settings (or Cmd+,)
2. Open the **Connectors** tab → **Add custom connector**
3. Name it "Arcade", paste `https://api.arcade.dev/mcp/<slug>` → **Add**
4. Click **Connect** → approve in the browser (the Arcade Auth sign-in)
> Remote HTTP works directly here — no `mcp-remote`, no JSON config file (the JSON `claude_desktop_config.json` only supports LOCAL servers). Optional: **Configure** to toggle individual tools.

**Claude.ai web:**
1. **Customize → Connectors → Add custom connector**
2. Paste the same URL → **Add** → **Connect** → approve
> Free plan = one custom connector. On Team/Enterprise an Owner adds it first (Organization settings → Connectors → Add → Custom → Web), then each member clicks Connect.

"Same tools, now in three Claude surfaces, and I only connected once. That's the whole point of a gateway. And in a minute we'll point Python at that same URL too."

[NOTE: `arcade configure claude` exists but sets up a LOCAL server — do NOT use it for the hosted gateway; use the Connectors UI above. Minor: the button reads "Add custom connector" (Anthropic) / "Add custom Connector" (Arcade doc) — same button.]

[NOTE: pre-clear the OAuth once before filming so the on-camera approve is smooth, or show the real first-time approve if it's quick. Keep any write action (drafting/sending) in draft mode.]

---

## MODULE 3 — BUILD YOUR OWN TOOL / MCP SERVER  [~12 min]  (project/02-custom-tool)

[NOTE: the "you could build anything" module. Build ONE small real tool live, deploy it, call it from Claude Code. Framework is `arcade-mcp` (the CURRENT SDK; the old TDK is dead). Reference tool: `project/02-custom-tool/server.py`. PRE-TEST the deploy before filming — it can be slow, and you want it warm.]

### Why build your own [~1 min]
[SHOW: Tyler to camera, or the Arcade tool catalog.]

"So far we've used tools Arcade already built, and there are thousands of them. They cover most of what you'll want. But eventually you hit the thing that's yours. An internal API. A niche service. Your own product. When that happens, you build the tool yourself, and Arcade still handles the hosting and the auth. Let me show you how little there is to it."

### Install + scaffold [~2 min]
[SHOW: terminal.]

"One thing to install, once."
```
uv tool install arcade-mcp
```
"That gives me the arcade command. Now I scaffold a new server."
```
arcade new my_server
cd my_server/src/my_server
```
[SHOW: open server.py — it ships with example tools.]

"That's a full project. A pyproject file, an env file for secrets, and this server file. The server file is the whole thing."

### Write a tool [~3 min]
[SHOW: write/paste a small tool in server.py. Keep it readable on screen.]

"A tool is just a Python function with a decorator. Here's one that takes a GitHub repo and returns its star count."
```python
from typing import Annotated
import httpx
from arcade_mcp_server import MCPApp

app = MCPApp(name="my_server", version="1.0.0")

@app.tool
async def github_repo_stars(
    repo: Annotated[str, "owner/name, e.g. 'ArcadeAI/arcade-mcp'"],
) -> Annotated[int, "The repo's current star count"]:
    """Return how many stars a public GitHub repository has."""
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.github.com/repos/{repo}")
        r.raise_for_status()
        return int(r.json()["stargazers_count"])

if __name__ == "__main__":
    app.run(transport="stdio")
```
"That's the whole tool. The decorator makes it a tool. The little Annotated notes and the docstring are what the AI reads to know how to use it. If it needed a login, like Gmail, you'd add one line, `requires_auth`, and Arcade runs the OAuth. If it needed an API key, `requires_secrets`, and Arcade stores it. This one's a public API, so we're done."

### Test it locally [~2 min]
[SHOW: run it in HTTP mode.]
```
uv run server.py http
```
[SHOW: open http://127.0.0.1:8000/docs, run the tool with a repo name, see the star count.]

"Arcade gives me a local test page. I type a repo, run the tool, there's the star count. It works. Now let's put it online."

### Deploy it [~2 min]
[SHOW: cd back to the project root, the folder with pyproject.toml.]
```
cd ../..
arcade login
arcade deploy -e src/my_server/server.py
```
"Log in once, then deploy. Arcade packages my server, checks it, and stands it up as a hosted MCP server in the cloud. On the free plan you get one hosted server, which is all we need. And now my tool shows up in my Arcade catalog, right next to Gmail and Calendar."

[NOTE: deploy runs from the folder that has pyproject.toml (`my_server/`), entrypoint `-e src/my_server/server.py`. Confirm it appears in the dashboard before moving on.]

### Use your tool from Claude Code [~2 min]
[SHOW: add the new tool to your gateway in the dashboard (the same gateway from Module 2), then Claude Code.]

"Last step. I add my new tool to my gateway, the same one from module two. Now Claude Code can use it."
[SHOW: ask Claude Code.]

> "How many stars does the ArcadeAI arcade-mcp repo have? Use my github tool."

[SHOW: Claude Code calls your tool, returns the number.]

"There it is. That number came from a tool I wrote ten minutes ago, running in the cloud, called by Claude Code. That's your own MCP server. Anything you can write as a function, you can hand to an agent this way, and you never touched the hosting or the auth."

[NOTE: if the live deploy is slow or flaky, cut to a pre-deployed version. Never fake the output.]

## MODULE 4 — SAME TOOLS IN LANGCHAIN  [~10 min]  (project/03-langchain)
> TO WRITE. Beats: the 2026 truth (langchain-arcade deprecated) → `uv run 03-langchain/agent.py` → authorize once → it uses Gmail. Point out: same tools, a framework.

## MODULE 5 — SAME TOOLS IN CREWAI  [~10 min]  (project/04-crewai)
> TO WRITE. Beats: crewai-arcade also deprecated → same arcadepy pattern → `uv run 04-crewai/main.py`. The payoff line: learn the SDK once, use it anywhere. Optional on-camera model swap (OpenAI → Claude, one env var).

## MODULE 6 — RUN IT 24/7 ON A SERVER  [~10-12 min]  (project/05-scheduled-agent + deploy)
> TO WRITE. The Morning Planner (ClickUp → plan → write calendar blocks). Beats: `--discover` → dry run → `--apply` into the "AI Plan" calendar → schedule it LOCALLY with cron → then SSH into a Hostinger VPS and set up the same cron/systemd there so it runs without your laptop. This is the "24/7 on your own server" payoff from the roadmap.

## MODULE 7 — WRAP + FREE STUFF  [~2-3 min]
> TO WRITE. Recap the 5 builds. Point to the free blueprint + setup pack + community. CTA.
