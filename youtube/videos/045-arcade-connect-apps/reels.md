# Reels — 045: Give Claude Code Access to Your Real Apps (Arcade)

4 short-form scripts, cut from the 045 footage or filmed quick. Each is ~30-45s.
Platforms: TikTok, Instagram Reels, YouTube Shorts, LinkedIn (value post).
Voice: Tyler talking to a friend. Short sentences. No em dashes. No hype words. IG max 5 hashtags.
Video: https://youtube.com/watch?v=REPLACE_045_URL

---

## Reel 1 — "Add any MCP server in one line" (the easy add, post first)

**Spoken (word for word):**
"People overcomplicate this. You can give Claude Code a whole new set of tools with one line. Watch. `claude mcp add`, a name, the transport, and a URL. Enter. Now Claude Code can reach that tool. That's it. It's not a plugin you build, it's not a config file you babysit. One line, and Claude Code can do something it couldn't do a second ago."

[SHOW: terminal. Type `claude mcp add arcade --transport http "<url>"` live, then `claude mcp list` showing it connected.]

**TikTok:**
You can add a whole toolset to Claude Code with one line. claude mcp add, a name, the URL, enter. Done. No plugin to build, no config to babysit.
#claudecode #mcp #ai #aiagents #claudeai

**Instagram Reels:**
Adding an MCP server to Claude Code is one line. Not a plugin you build, not a config you babysit. One command and it can reach new tools. Full walkthrough on my channel.
#claudecode #mcp #ai #aiagents #claudeai

**YouTube Shorts:**
How to add any MCP server to Claude Code (one line).
#shorts #claudecode #ai

**LinkedIn:** (value post, Tyler voice)
People think adding tools to an AI agent is a project. It is one line.

`claude mcp add`, a name, the transport, and a URL. Enter. Now Claude Code can reach a tool it could not touch a second ago.

That is the whole idea behind MCP. It is a standard way to hand an agent a new capability without wiring up a custom integration each time.

The hard part was never the wiring. It was the auth behind it, and that is the part I let something else handle.

So if you have been putting this off, it is smaller than you think. What tool would you connect first?

---

## Reel 2 — "A simple MCP server, no code" (demystify, post second)

**Spoken (word for word):**
"Everyone says build an MCP server like it's a weekend. Here's the simple version. On arcade.dev I pick the tools I want, Gmail, Calendar, Slack, whatever. I get one URL back. That URL is the server. I didn't write any code. I chose the tools, I got a URL, I handed it to Claude Code. That's a working MCP server."

[SHOW: arcade.dev gateway builder, selecting Gmail + Calendar, then the generated Gateway URL.]

**TikTok:**
You don't have to code an MCP server. Pick your tools on arcade.dev, get one URL back, hand it to Claude Code. That URL is the server. No code.
#claudecode #mcp #ai #aiagents #arcade

**Instagram Reels:**
A "simple MCP server," no code: pick your tools, get one URL, hand it to Claude Code. That is the server. Full breakdown on my channel.
#claudecode #mcp #ai #aiagents #arcade

**YouTube Shorts:**
The simplest MCP server (no code, just a URL).
#shorts #claudecode #ai

**LinkedIn:** (value post, Tyler voice)
"Build an MCP server" sounds like a weekend. Here is the version that took a minute.

I picked the tools I wanted. I got one URL back. I handed that URL to Claude Code. That is a working server, and I did not write any code.

The point is not that coding one is bad. The point is that for most people, the goal is the capability, not the plumbing. If you can skip the plumbing and get to the capability, do that first.

You can always go deeper later, once you know it is worth it.

---

## Reel 3 — "A 1-minute email and calendar setup" (the payoff)

**Spoken (word for word):**
"This took about a minute to set up. Claude Code, connected to my real Gmail and my real calendar. I ask it for my day. It reads the calendar, pulls the emails that actually need a reply, and drafts them. In draft mode, so nothing sends without me. That's a morning brief, running on my actual accounts, and the setup was one URL and one command."

[SHOW: terminal. Prompt "what does my day look like and which emails need a reply?" then the day summary + drafts appearing. Then Gmail drafts folder.]

**TikTok:**
One minute of setup: Claude Code on my real Gmail and calendar. I ask for my day, it summarizes the calendar and drafts the emails that need a reply. Drafts only, nothing sends.
#claudecode #ai #aiagents #productivity #claudeai

**Instagram Reels:**
A 1-minute setup: Claude Code reads my real calendar and inbox, gives me the day, and drafts the emails that need a reply. Drafts only. Full video on my channel.
#claudecode #ai #aiagents #productivity #claudeai

**YouTube Shorts:**
A 1-minute email + calendar assistant in Claude Code.
#shorts #claudecode #ai

**LinkedIn:** (value post, Tyler voice)
About a minute of setup, and now Claude Code reads my real calendar and my real inbox.

I ask what my day looks like. It gives me the schedule, pulls the emails that actually need me, and drafts the replies. In draft mode, so nothing goes out without me reading it.

That is the pattern I would tell anyone to start with. Let it read and draft. You approve. You are not handing over the send button, you are handing over the boring first pass.

The work does not disappear. You just stop starting from a blank screen every morning.

---

## Reel 4 — "I never touched an OAuth token" (the honest hook)

**Spoken (word for word):**
"Here's the part I care about as an engineer. I connected Claude Code to my real Gmail, and I never touched an OAuth token. When it first used the tool, it sent me to Google's real consent screen. I approved it. That's it. The token gets stored and refreshed for me. I never pasted it, it's not in a config file, it's not in my repo. That's the difference between a demo and something I'd actually run."

[SHOW: the Google OAuth consent screen appearing, approving it, then the tool working. Cut to a config file that does NOT contain a token.]

**TikTok:**
I connected Claude Code to my real Gmail and never touched an OAuth token. It sent me to Google's real consent screen, I approved once, done. No token in a config file. That is the difference from a demo.
#claudecode #ai #aiagents #oauth #claudeai

**Instagram Reels:**
I gave Claude Code my real Gmail and never touched an OAuth token. Approve once on Google's real screen, and it handles the rest. That is what makes it real, not a demo. Full video on my channel.
#claudecode #ai #aiagents #security #claudeai

**YouTube Shorts:**
I connected my real Gmail to Claude Code and never touched a token.
#shorts #claudecode #ai

**LinkedIn:** (value post, Tyler voice)
The part I care about as an engineer: I connected Claude Code to my real Gmail and never touched an OAuth token.

The first time it used the tool, it sent me to Google's actual consent screen. I approved it. The token is stored and refreshed for me. I never pasted it, it is not in a config file, it is not in my repo.

I have built these integrations at big companies. The auth is the part that eats the afternoon, and it is the part most demos quietly skip.

That is the line between something you show once and something you actually run. Handle the auth like it matters, and the rest gets boring in the best way.

---

## Post order
1 (one-line add) → 3 (1-min email/calendar payoff) → 2 (simple MCP server) → 4 (no OAuth token).
Reason: open with the quick win, then the payoff, then demystify, then the credibility beat.

## Notes
- Fill the video URL once 045 is live.
- No em dashes, no hype words, IG capped at 5 hashtags. Verified.
- LinkedIn posts are standalone value (they teach without needing the video), link optional in first comment.
