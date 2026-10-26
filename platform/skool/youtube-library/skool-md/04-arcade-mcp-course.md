## In this lesson
You'll connect your apps (ClickUp, Gmail, Google Calendar, Slack) once through Arcade.dev and use them in Claude Code, the Claude desktop app, your own Python agents (LangChain and CrewAI), and agents that run on a schedule.
You'll also build your own MCP server without writing code, deploy it so it runs 24/7, and set up a morning briefing that runs every day at 7am. No passwords or tokens stored in a file.

## Good to know
- Time: 2 to 3 hours if you do every module. Steps 1 to 3 alone take about 20 minutes.
- Cost: Arcade is free to sign up. The Python agents need an OpenAI or Anthropic API key (paid per use). A Hostinger VPS is about $7 to $8 a month, and only if you want it running 24/7.
- Level: Beginner for steps 1, 2 and 8 (no code). Steps 3 to 7 use the terminal, but Claude writes the code and the course repo has it all.
- Honest caveat: Claude Routines don't run exactly at 7am. Mine finish a few minutes after.

## What you need
- Arcade account (sign in with Google), free: https://www.arcade.dev/
- Claude Code: https://claude.com/claude-code
- Claude desktop app (for steps 2 and 8)
- The free course code: https://github.com/tylerprogramming/arcade-course (runs on uv, a Python tool step 5 installs)
- An OpenAI key (https://platform.openai.com) or an Anthropic key (https://console.anthropic.com), for steps 5 to 7
- Accounts for the apps you connect. I used ClickUp, Gmail, Google Calendar, Slack and GitHub.
- Optional: a Hostinger VPS: https://www.hostinger.com

**1. Make your first MCP gateway and add it to Claude Code (0:56)**
A gateway is just a bundle of tools from the apps you pick. In the Arcade dashboard, go to MCP Gateways, click Create MCP Gateway, name it (mine was ClickUp Assistant), search for ClickUp and tick it, choose "members of this project", then click Create. Pick Claude Code and copy the command Arcade gives you. Paste it in your terminal. The course repo writes it like this:
```
claude mcp add arcade --transport http "https://api.arcade.dev/mcp/<your-slug>"
```
Open Claude Code, switch to auto mode (Shift + Tab), then type:
```
/mcp
```
Pick your gateway and press Enter to authenticate. A browser window opens on Arcade. Click allow. Then try it:
> For my ClickUp assistant, can you get me all my in progress tasks?
Writing works too. I asked it to add a comment to a task and it showed up in ClickUp.

**2. Use the same gateway in the Claude desktop app (7:27)**
In Arcade, open your gateway, click Connect, choose Claude desktop and copy the URL. In the Claude app go to Settings > Connectors > Add custom connector. Paste the URL, click Add, then Connect, and allow it on Arcade. You can set each tool to always allow or needs approval. Same tools, and you only connected once.

**3. Build your own MCP server without writing code (11:21)**
For a tool that's yours, like your own product. I asked Claude Code to do the install and setup for me. The two commands are:
```
uv tool install arcade-mcp
arcade new my_server
```
It comes with example tools (greet, whisper secret, star a repo). Run it on your computer from the my_server/src/my_server folder:
```
uv run server.py
```
Ask Claude for the command to add this local server to Claude Code, exit Claude Code, paste it, open Claude again and type /mcp to see my_server and its tools. Test it:
> Use the greet tool from my_server with the name Tyler
When it said there was no Arcade API key, I logged in from inside Claude Code (the ! runs a terminal command):
```
!arcade login
```

**4. Deploy your server so it runs 24/7 (18:03)**
Running it locally means your computer has to stay on. From the top folder of the project (the one with pyproject.toml), run:
```
arcade deploy -e src/my_server/server.py
```
When it says the deployment is successful, it shows up in the Arcade dashboard under Servers (not MCP Gateways). Make a new gateway with just the tool you want (I picked star a repo), add it to Claude Code like step 1, and authenticate in /mcp. Disable the old local my_server in /mcp so Claude uses the hosted one.

**5. Get the code and your keys ready (24:32)**
In the Arcade dashboard, make an API key (Dashboard > API Keys). Then install uv and set up the course code:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/tylerprogramming/arcade-course.git
cd arcade-course
uv sync
cp .env.example .env
```
Open .env and fill in ARCADE_API_KEY, OPENAI_API_KEY (or set LLM_PROVIDER=anthropic and add ANTHROPIC_API_KEY), and ARCADE_USER_ID (your email).

**6. Run the same tools in LangChain and CrewAI (29:45)**
The LangChain email agent chats with you and can read and send Gmail:
```
uv run 03-langchain/email_agent.py
```
I asked: What are the last three unread emails? Then the email and Slack agent, which gets the whole Slack server:
```
uv run 03-langchain/email_slack_agent.py
```
Can you summarize all emails from the last 24 hours and send a message in Slack to the #ai channel?
The CrewAI version (34:16) runs on its own and lists your email address and three latest subjects:
```
uv run 04-crewai/main.py
```

**7. Build the morning planner and schedule it (38:19)**
It reads today's ClickUp tasks and your Google Calendar and blocks out your day. First see your real tool names, then do a dry run that writes nothing, then let it write:
```
uv run 05-scheduled-agent/morning_planner.py --discover
uv run 05-scheduled-agent/morning_planner.py
uv run 05-scheduled-agent/morning_planner.py --apply
```
To schedule it, I didn't write the cron job myself. I asked Claude Code:
> Can you schedule the morning_planner.py with --apply on it every morning at 6 a.m. on my computer?
For 24/7 without your computer on (44:17), get a Hostinger KVM VPS, open its terminal, run Claude Code there and set up the same agent. The repo's deploy/README.md has the cron steps.

**8. Schedule a morning briefing with Claude Routines, no code (46:17)**
In the Claude app go to Code > Routines and describe it:
> I want to know all my tasks from ClickUp, what's on my calendar and a summary of my emails from the last 24 hours at 7 a.m. every morning.
Click Draft routine, then Create. In Arcade, make a gateway called Morning Assistant with Gmail, Google Calendar and ClickUp. Add it in Claude under Settings > Connectors > Add custom connector, connect and allow. Edit the routine (pencil icon), remove the other connectors, add Morning Assistant, save, then click Run now to test. Turn on push notifications to get the summary on your phone.

## Files and links
- Course code, all modules: https://github.com/tylerprogramming/arcade-course
- Copy-paste setup guide: https://github.com/tylerprogramming/arcade-course/blob/main/INSTALL.md
- VPS and cron guide: https://github.com/tylerprogramming/arcade-course/blob/main/deploy/README.md
- Arcade: https://www.arcade.dev/
- Arcade MCP gateways: https://api.arcade.dev/dashboard/mcp-gateways
- Add Arcade to Claude Code, Desktop and Web: https://docs.arcade.dev/en/get-started/mcp-clients
- Claude custom connectors: https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp

## If it breaks
- Gateway says "needs authentication": type /mcp, pick it, press Enter and allow it on Arcade.
- Claude uses the wrong ClickUp connection: name the gateway in your prompt ("for my ClickUp assistant").
- Custom server says no Arcade API key configured: run !arcade login inside Claude Code.
- Can't find your deployed server: it's under Servers in the dashboard, not MCP Gateways.
- Starring a repo failed because the Arcade GitHub connection wasn't allowed to star: add GitHub to the same gateway, save, then re-authenticate in /mcp.
- Old guides tell you to install langchain-arcade or crewai-arcade: don't. Install LangChain or CrewAI on their own plus the Arcade SDK. The repo already does this.
- The CrewAI agent errored on an empty page token with the OpenAI model: I pasted the error into Claude and it fixed it.
- The 6am job didn't run: your Mac was asleep. It runs when it wakes up, or keep it from sleeping, or use a VPS.
- Routine set to always allow: lock down tools that delete or trash things before you leave it running.

## Next
Build an AI Agent in 5 Steps (Claude Code)
