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

## MODULE 1 — WHAT ARCADE ACTUALLY IS (the concepts, fast) [~5-6 min]

[NOTE: the ONLY lecture in the course. Keep it tight and concrete. Build a simple diagram on screen as you name each layer: tool → MCP server → gateway (one URL) → engine.]

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
> TO WRITE. Beats: why (prebuilt is great until your thing is custom) → `uv tool install arcade-mcp` → `arcade new` → write a tool (`@app.tool`, no-auth + secret + OAuth) → `uv run server.py http` test → `arcade login` + `arcade deploy` → add to the gateway → call it from Claude Code. Free tier hosts one server.

## MODULE 4 — SAME TOOLS IN LANGCHAIN  [~10 min]  (project/03-langchain)
> TO WRITE. Beats: the 2026 truth (langchain-arcade deprecated) → `uv run 03-langchain/agent.py` → authorize once → it uses Gmail. Point out: same tools, a framework.

## MODULE 5 — SAME TOOLS IN CREWAI  [~10 min]  (project/04-crewai)
> TO WRITE. Beats: crewai-arcade also deprecated → same arcadepy pattern → `uv run 04-crewai/main.py`. The payoff line: learn the SDK once, use it anywhere. Optional on-camera model swap (OpenAI → Claude, one env var).

## MODULE 6 — RUN IT 24/7 ON A SERVER  [~10-12 min]  (project/05-scheduled-agent + deploy)
> TO WRITE. The Morning Planner (ClickUp → plan → write calendar blocks). Beats: `--discover` → dry run → `--apply` into the "AI Plan" calendar → schedule it LOCALLY with cron → then SSH into a Hostinger VPS and set up the same cron/systemd there so it runs without your laptop. This is the "24/7 on your own server" payoff from the roadmap.

## MODULE 7 — WRAP + FREE STUFF  [~2-3 min]
> TO WRITE. Recap the 5 builds. Point to the free blueprint + setup pack + community. CTA.
