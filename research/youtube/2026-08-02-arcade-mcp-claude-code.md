# Video Concepts: Simple Arcade MCP Servers + Claude Code

**Topic:** How to connect Arcade's prebuilt MCP tools (Gmail, Slack, Calendar, GitHub...) to Claude Code and build a useful "7-minute app / agent" without wrestling with auth.

## What Arcade actually is (say this simply on camera)
- **An MCP runtime for real agents** - the tagline is "Ship agents, not auth infrastructure."
- **7,500+ prebuilt tools across 81 MCP servers** (Gmail, Google Calendar/Docs/Sheets/Drive, Slack, Teams, Discord, GitHub, Linear, Jira, Asana, Postgres, MongoDB...).
- **The whole point: it handles the auth.** Normally connecting Claude to your Gmail means fighting OAuth, tokens, and scopes. Arcade does per-user OAuth for you - you click "authorize" once per tool and it manages the tokens. That's the "simple" in "simple MCP servers."
- Not just chat - the agent takes **real actions as you** (send the email, post the Slack, create the issue), with an audit trail.

## The connection (the easy part - this is the demo backbone)
1. Make an Arcade account, build a **Gateway**, pick the tools you want.
2. One command in Claude Code:
   ```
   claude mcp add arcade --transport http "<YOUR_ARCADE_GATEWAY_URL>"
   ```
3. Verify: `claude mcp list` / `claude mcp get arcade`
4. First time you use a tool, it pops an **OAuth authorize** for that account. Done.

That's it - no server to build, no code. You're plugging in prebuilt MCP servers.

## The "7-minute app" framing (Arcade's ethos, and your angle)
Arcade's pitch is you go from nothing to a working, production-shaped agent **in a single sitting** - connect Gmail or Slack "in one line." Frame the whole video around that: **you don't build apps anymore, you assemble an agent from tools in ~7 minutes.** Put a timer on screen.

---

## Title options
1. **Give Claude Code Access to Your Real Apps in 7 Minutes (Arcade MCP)**
2. **The Easiest Way to Connect Gmail and Slack to Claude Code**
3. **I Gave Claude Code My Gmail - Safely - with One MCP Server**
4. **Build a Real AI Agent in 7 Minutes: Claude Code + Arcade**
5. **MCP Servers Made Simple (Claude Code + Arcade)**

Recommended: #1 or #4 - both promise the outcome + the time, and match Arcade's own "7-minute" ethos.

## Structure (~8-10 min)
1. **Hook (get right into it):** "Claude Code is great, but it can't touch your real apps. I connected my Gmail, Calendar, and Slack in about 7 minutes, no code, no OAuth headaches. Here's how."
2. **What Arcade is (30s):** the MCP runtime that handles the auth so you don't. 7,500 prebuilt tools.
3. **Connect it (the simple part, on screen):** build a gateway, pick tools, `claude mcp add arcade ...`, authorize. Start the 7-min timer here.
4. **Demo 1 - the morning brief:** Calendar + Gmail -> "what's my day look like and what needs a reply?"
5. **Demo 2 - take an action:** "draft replies to the two that matter" or "post my standup to Slack" or "summarize the open issues in my repo and file the top one in ClickUp."
6. **Why it's not sketchy (your dev angle):** real per-user OAuth, tokens never hardcoded, every action logged. You've built integrations at Fortune 500s - this is the part that actually matters for real use.
7. **The bigger idea:** stop building apps, start assembling agents from tools. Stop the timer.
8. **CTA.**

## Demo / "7-minute app" ideas (pick 1-2)
- **Morning brief agent** - Gmail + Calendar -> daily summary + which emails need replies. (Most relatable.)
- **Inbox triage + draft** - reads unread, drafts replies in your voice, you approve.
- **Slack standup poster** - "post yesterday's wins to #standup."
- **Repo triage** - GitHub -> summarize open issues/PRs, file the top one to ClickUp (via Arcade if available, or Tyler's existing ClickUp MCP).
- **Meeting prep** - before a calendar event, pull the attendee's last emails and a one-page brief.

## Positioning / honesty (per your voice)
- You're a software engineer (8 yrs, Fortune 500) - lean into *why the auth layer is the hard part* and why offloading it matters. That's your credible wedge, not "look how easy."
- No hype words. Show the real thing working, admit the limits (it's a product, has a paid tier, tools vary in polish).
- **Disclosure:** you worked with Arcade before - if this is sponsored/partner again, say so on camera and in the description.

## For continuity
- Couldn't find last year's Arcade video package in this repo - if you have the link/title, I'll pull the old angle so this one builds on it instead of repeating.

## Sources
- Arcade: https://www.arcade.dev/
- Claude Code + Arcade docs: https://docs.arcade.dev/en/get-started/mcp-clients/claude-code
- Arcade MCP framework: https://www.arcade.dev/mcp/
- arcade-mcp (GitHub): https://github.com/ArcadeAI/arcade-mcp
