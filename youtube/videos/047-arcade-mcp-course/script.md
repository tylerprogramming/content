# Runsheet — 047 How to Build AI Agents in 2026 (The Right Way)

Format: PROJECT-BASED COURSE, filmed module-by-module (assemble into one ~1hr long-form; each module also stands alone as a clip). Voice: Tyler to a friend. Short sentences. No hype words. No em dashes. Open fast.
LLM: OpenAI `gpt-5.4-mini` on screen (one env flip to Claude). Model-agnostic is a teaching beat.
Everything real: real gateway, real accounts, real deploys, real runs. Draft/safe mode on anything that writes. No keys/tokens on screen (env vars, gitignored `.env`).
[DISCLOSURE: if sponsored/partner with Arcade (and Hostinger for the VPS), say so on camera + in the description. Call each out where it appears; don't blur them.]

> STATUS: Modules 0-2 drafted. Modules 3-7 to write next. Cold open (Module 0) is filmed LAST (needs the module footage for the montage).

---

## MODULE 0 — COLD OPEN + ROADMAP  [film last]

### The hook (modeled on Sabrina Ramonov's top-tutorial structure)
[SHOW: open on Tyler to camera for the "two types" line, then fast cuts of the payoff — Claude Code pulling Gmail; a terminal printing "Deployed"; a LangChain agent answering; a CrewAI crew running; a calendar filling itself with time-blocks at 6:31 AM.]

"There are two types of people trying to build AI agents right now. The ones still reading about it, and the ones who actually connected AI to their real apps and let it start doing the work. And the gap between them isn't coding. It's one thing: giving the AI permission to touch your accounts without doing something reckless with your passwords. That's the wall everyone hits.

So in this video I hand you the way past it, and by the end you'll have real agents running on your email, your calendar, your tasks, even one running on a server every morning while you sleep. You don't need to be an engineer for any of it.

I've spent eight years building exactly these integrations, at IBM, at Chase, now at Pfizer, so trust me: this used to be the hard part, and it isn't anymore. Let's build."

[NOTE: beats — pattern-interrupt hook → the ONE problem (auth) → ① DELIVERABLE ("by the end you'll have...") → ② objection pre-empt ("you don't need to be an engineer") → ③ credibility (IBM/Chase/Pfizer, delayed to HERE on purpose so the hook earns attention first — her tutorial move) → ④ hard cut ("Let's build"). Into the content by ~1:00.]

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

"A tool is just a Python function with a decorator. Here's one that takes a GitHub repo and returns its star count. No login needed, it just hits GitHub's public API."
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
"That's the whole tool. The decorator makes it a tool. The little Annotated notes and the docstring are what the AI reads to know how to use it. This one's a public API, so no login. But if it DID need one, like Gmail, you'd add one line, `requires_auth`, and Arcade runs the OAuth. If it needed an API key, `requires_secrets`, and Arcade stores it."

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

## MODULE 4 — SAME TOOLS IN LANGCHAIN  [~10 min]  (03-langchain/email_agent.py + email_slack_agent.py)

[NOTE: the "not just Claude" module. Same Arcade tools, now driving a LangChain/LangGraph agent in code. Lead with the 2026 truth (langchain-arcade is deprecated). Run from ~/arcade-course. PRE-TEST agent.py before filming and pre-authorize Gmail so the run is smooth.]

### The 2026 truth [~1.5 min]
[SHOW: Tyler to camera, or a quick shot of the deprecated PyPI page.]

"Claude Code is great, but you're not always inside Claude. Sometimes you're building your own agent, in your own code, with a framework like LangChain. So let me show you the same tools running there.

And I have to say this up front, because it'll save you hours. If you google how to use Arcade with LangChain, you'll find a package called langchain-arcade. Don't use it. It got deprecated. Same story with the CrewAI one, which we'll see next. The way that actually works now is to use the Arcade SDK directly and wrap the tools yourself. It's a little setup code, and I've already written it for you in the project. Let me walk through it."

### The code [~3 min]
[SHOW: open 03-langchain/email_agent.py, scroll to the key parts.]

"Here's the whole idea. I load the Arcade tools I want by name, Gmail list emails, Gmail send. I wrap each one so LangChain understands it. Then I hand them to a normal LangChain agent. The one interesting part is authorization: the first time the agent wants a tool I haven't approved, it pauses, gives me a link, I approve, and it continues. Arcade holds the token after that.

And notice the model up here. It's OpenAI by default, but it's one line to switch to Claude. The agent doesn't care, the tools don't change. That's the point, this is model-agnostic and framework-agnostic."

### Run it [~4 min]
[SHOW: terminal in ~/arcade-course.]
```
uv run 03-langchain/email_agent.py
```
[SHOW: it says the agent is ready. Type a request.]

> "Summarize my three most recent unread emails."

[SHOW: if Gmail isn't authorized yet it prints a link — click, approve, return. If you authorized Gmail earlier (Module 2), it runs straight through.]

"If I'd never connected Gmail, it'd hand me a link right here, I approve once, done. Since I already authorized it back in Claude Code, same account, same user, it just runs. Watch."

[SHOW: the agent calls the Gmail tool, returns the summary.]

"There it is. A LangChain agent, using my real Gmail, through the exact same Arcade connection I set up at the start. No new auth, no tokens in my code. I built the agent, Arcade handled the access."

### Level up: add Slack, same code [~2 min]
[SHOW: open email_slack_agent.py beside email_agent.py — highlight the ONLY difference: Slack was added.]

"Now watch how easy it is to give this agent a new power. This is the same file. The one thing I changed is that I added Slack. That's the whole thing about Arcade: any tool in their catalog drops into my agent just by naming it. I don't build the integration, I name it, and I approve it once. Let me run this one."
```
uv run 03-langchain/email_slack_agent.py
```
> "Summarize my unread emails, then post the summary to my #standup channel on Slack."

[SHOW: approve Slack once if needed, then it reads Gmail and posts to Slack.]

"Read my email, wrote a summary, posted it to Slack, one agent. And to add Slack I wrote zero integration code. I named the tool and approved it. More power is just more tools."

[NOTE: use a scratch Slack channel, pre-authorize Slack before filming. Keep any email send in draft; don't actually send on camera. If create_agent/tool-wrapping errors on the day, that's why we pre-test — never debug on camera, cut to a working take.]

## MODULE 5 — SAME TOOLS IN CREWAI  [~8-10 min]  (04-crewai/main.py)

[NOTE: the "it's not just LangChain" module — proves framework-agnostic. Faster than Module 4 (viewers get the pattern now). Run from ~/arcade-course. VERIFIED working with gpt-5.4-mini. Pre-authorize Gmail.]

### The hook [~1 min]
[SHOW: Tyler to camera.]

"So we did LangChain. But maybe you don't use LangChain. Maybe you're a CrewAI person, or your team is. So let me prove the whole point of this video: the tools don't care what framework you're in. I'm going to hand the exact same Gmail tools to a completely different framework, CrewAI, and I want you to notice how little actually changes.

Same warning as before, by the way: there's an old crewai-arcade package too, and it's also deprecated. So we do it the current way, straight through the SDK."

### The code [~3 min]
[SHOW: open 04-crewai/main.py, next to the LangChain file if you can.]

"Put this next to the LangChain one. The Arcade part is basically identical. I load the tools, I wrap them, I handle the one-time auth inside the wrapper. The only thing that's really different is the CrewAI shape around it: I define an agent, give it a task, put it in a crew. That's CrewAI's world, not Arcade's. The Arcade half didn't move.

That's the real lesson of these two modules. You learn Arcade's SDK once, and the framework is just the wrapper you put around it."

### Run it [~3 min]
[SHOW: terminal in ~/arcade-course.]
```
uv run 04-crewai/main.py
```
[SHOW: it calls Gmail.WhoAmI and Gmail.ListEmails, then prints my email + three recent subject lines.]

"And there it is. A CrewAI agent, using my real Gmail, through the same Arcade connection from the very beginning. It looked me up, pulled my recent emails, listed the subjects. Same tools, same auth, different framework, and almost no new code."

### Optional flex: swap the model [~1 min]
[SHOW: open .env, change LLM_PROVIDER from openai to anthropic, re-run.]

"One more thing if you want it. This ran on OpenAI. I change one setting, the provider, to Claude, and run it again. Same tools, same agent. Arcade doesn't care what model you use either. Model-agnostic, framework-agnostic. That's the whole point."

[NOTE: the model swap is a nice flex but adds time and needs an ANTHROPIC_API_KEY in .env; skip if the module runs long. Keep any send in draft.]

## MODULE 6 — RUN IT 24/7 ON A SERVER: the Morning Planner  [~12 min]  (05-scheduled-agent + deploy)

[NOTE: the finale + the roadmap payoff. This one makes it an AGENT — it runs on its own, on a server, every morning. It also TAKES AN ACTION (writes your calendar), not just reads. Run from ~/arcade-course.
⚠️ LEAST-tested path: needs ClickUp AND Google Calendar authorized (two new consents) plus the plan step. PRE-RUN a full dry-run before filming and pre-clear both auths. Writes go to a wipeable calendar with a [Plan] tag — keep it safe.]

### The hook [~1 min]
[SHOW: Tyler to camera, then the result: a calendar filling with time-blocks, early-morning timestamp.]

"Everything so far ran when I ran it. But a real agent runs when I'm not there. So for the finale, I'm building the one I actually use. Every morning, before I'm even up, it reads my to-do list and my calendar, plans my day, and writes the time-blocks straight into my calendar. And it does it on a server, so my laptop doesn't even have to be on. Let me show you."

### What it does [~1 min]
[SHOW: morning_planner.py, or a simple 4-step graphic.]

"Here's the whole job. It reads today's tasks from ClickUp. It reads my calendar to see what's already booked. It hands both to the model and asks it to fit the tasks into the open slots around my meetings. Then it writes those blocks back to my calendar. Read, plan, act. This is the first agent in the video that actually does something, instead of just telling me something."

### See the real tool names [~1 min]
```
uv run 05-scheduled-agent/morning_planner.py --discover
```
"Quick honesty step. This prints the exact tool names my Arcade account has for ClickUp and Calendar, so I'm wiring real ones, not guessing."

### Dry run — plan, don't write [~3 min]
```
uv run 05-scheduled-agent/morning_planner.py
```
[SHOW: first run authorizes ClickUp, then Google Calendar — click through both once. Then it prints the plan.]

"First time, it asks me to connect ClickUp and my calendar, same one-time approval as always. Then, and this matters, it runs in safe mode by default. It prints the plan it WANTS to make and writes nothing. So I can look first. There's my day, blocked out around my meetings."

### Apply it [~2 min]
```
uv run 05-scheduled-agent/morning_planner.py --apply
```
[SHOW: open Google Calendar — the [Plan] blocks appear.]

"Now I let it write. And there they are, in my actual calendar, tagged Plan so I know the agent made them. It's writing to a calendar I can wipe in one click until I fully trust it. That's the rule for anything that takes an action: safe first, trust later."

### Schedule it locally [~2 min]
[SHOW: crontab.]

"It works when I run it. Let's make it run on its own. Simplest way, on my machine, is cron."
```
crontab -e
# 6:30am daily (uses the project's venv python):
30 6 * * * cd ~/arcade-course && ~/arcade-course/.venv/bin/python 05-scheduled-agent/morning_planner.py --apply
```
"Now it fires every morning at six thirty. But there's a catch: my laptop has to be awake for cron to run. So let's do it the real way, on a server."

### Run it 24/7 on a Hostinger VPS [~2-3 min]
[SHOW: SSH into the VPS. Steps from deploy/README.md.]

"I've got a small Hostinger VPS. I copy the project up, install it the same way, authorize once, and set the exact same schedule there. The server never sleeps, so it runs every single morning whether my laptop's open or not."
```
# from your Mac: copy the project up
scp -r ~/arcade-course root@YOUR_VPS_IP:~/arcade-course
ssh root@YOUR_VPS_IP
cd ~/arcade-course && curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run 05-scheduled-agent/morning_planner.py     # click the auth links once
crontab -e                                         # add the same 6:30am line (VPS paths)
```
"And that's it. The plan and the blocks are waiting for me every morning, made by an agent running on a server, on my real accounts, and I never stored a token anywhere."

[DISCLOSURE: if Hostinger is a partner, say so here, plainly.]

### Close the build [~30s]
"So that's the whole thing. My apps in Claude Code, in the desktop app, and on the web. A tool I built myself. The same tools in LangChain and CrewAI. And now an agent running on a server around the clock. One connection at the start powered every bit of it."

[NOTE: tighten the VPS section in the edit. The key beat is 'local cron needs the laptop on, the server doesn't.' If the live VPS is slow, pre-set it up and show the result (crontab -l + a real run log).]

## MODULE 7 — WRAP + FREE STUFF  [~2-3 min]
> TO WRITE. Recap the 5 builds. Point to the free blueprint + setup pack + community. CTA.
