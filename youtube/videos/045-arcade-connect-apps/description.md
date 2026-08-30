# YouTube Description: 045 Arcade Connect Apps

> **Use the `## SEO-Optimized Version` at the bottom of this file.** Title locked
> 2026-08-13 in `titles.md`: **Turn Claude Code Into A Real Assistant In 7 Minutes
> (No Code)**. Tags live in `tags.txt` (YouTube tags field, not the description).
>
> **Rewritten 2026-08-16 against the delivered cut** (`~/Movies/Camtasia/045 -
> arcade.dev/045 - arcade.dev - FINAL.mp4`, 12:00.6). The previous version was
> written pre-production and did not match what was shot — it promised **GitHub**,
> which never appears, and its chapters were placeholders. Chapters below are timed
> off the final render.

---

Claude Code is great in the terminal, but out of the box it cannot touch your real apps. In this video I connect it to Gmail, Google Calendar, Google Drive, Google Docs, Slack and ClickUp using arcade.dev, an MCP runtime that holds the per-user OAuth for you. There is no server to build, no tokens to hardcode and no scopes to fight. You pick the tools you want, paste one command into Claude Code, authorize once, and it starts taking real actions in your real accounts.

I build it twice on purpose. First a simple gateway with three Gmail tools, so you can see the shape of the thing. Then a multi-tool gateway with 65 tools across five apps, wired into Claude Code. Then one prompt: summarize the partnership thread in my Gmail, write it up as a Google Doc, file that in a named Drive folder, and post the summary to Slack. It does all five steps. Then I add ClickUp to the gateway live, and hit the one mistake everybody makes. If you add a tool after the gateway exists, you have to re-authenticate before it can use it.

The part that actually matters is the auth. Anything Google-related makes you refresh your connection every seven days unless you are a production-ready app, which means you cannot just let an agent run unattended. arcade.dev holds that layer, so you can add people to a project or stand up your own sign-in provider and never handle a token yourself.

CHAPTERS
0:00 - What one MCP server just did
0:23 - "Can't I just use plugins or connectors?"
1:04 - Creating your first MCP gateway
1:41 - Picking only the tools you need
2:18 - Choosing who can connect
2:33 - Connecting the gateway to Claude Code
3:05 - Authenticating and the first test
4:06 - Building a smarter multi-tool gateway
5:16 - Adding it to Claude Code
5:56 - Turning off the servers you don't want it using
6:20 - Test: read my email and my calendar
6:58 - The five-step demo prompt
7:33 - The 7-day re-auth problem this solves
8:18 - Watching all five steps run
8:52 - The mistake I made: re-authenticate after adding a tool
9:24 - Checking the results in Drive
9:52 - Connecting from anywhere, and adding ClickUp
10:47 - Per-user auth and adding your team
11:34 - Free resources and wrap-up

LINKS
- arcade.dev: https://www.arcade.dev/
- Claude Code + Arcade docs: https://docs.arcade.dev/en/get-started/mcp-clients/claude-code
- Free community, with this whole walkthrough in the classroom: https://www.skool.com/the-ai-agency

---

[No disclosure needed — Arcade is not sponsored, confirmed 2026-08-13.]

---

## SEO-Optimized Version

One MCP server, six apps. I connect Claude Code to Gmail, Google Calendar, Google Drive, Google Docs, Slack and ClickUp with a single MCP gateway from arcade.dev, then give it one prompt and watch it run a five-step workflow across four of them. No code, no server to build, and no OAuth to fight.

Out of the box Claude Code cannot touch your real accounts. This is the piece of plumbing that fixes that. I build the gateway twice. First a simple one with three Gmail tools so the shape is obvious, then a multi-tool gateway carrying 65 tools across five apps, wiring each one into Claude Code with a single paste. Then the real test: summarize a partnership thread in Gmail, write it up as a Google Doc, save that into a named Drive folder, and post the summary to a Slack channel. Five steps, one prompt.

The reason this beats wiring it yourself is the auth. Anything Google-related expires every seven days unless you are a production-ready app, so an agent you want running unattended will just stop. arcade.dev holds the auth and governance layer, so you add people to a project or bring your own sign-in provider and never touch a token. I also add ClickUp to a live gateway at the end and hit the gotcha nobody documents: add a tool after the gateway exists and you have to re-authenticate before Claude Code can use it.

CHAPTERS
0:00 - What one MCP server just did
0:23 - "Can't I just use plugins or connectors?"
1:04 - Creating your first MCP gateway
1:41 - Picking only the tools you need
2:18 - Choosing who can connect
2:33 - Connecting the gateway to Claude Code
3:05 - Authenticating and the first test
4:06 - Building a smarter multi-tool gateway
5:16 - Adding it to Claude Code
5:56 - Turning off the servers you don't want it using
6:20 - Test: read my email and my calendar
6:58 - The five-step demo prompt
7:33 - The 7-day re-auth problem this solves
8:18 - Watching all five steps run
8:52 - The mistake I made: re-authenticate after adding a tool
9:24 - Checking the results in Drive
9:52 - Connecting from anywhere, and adding ClickUp
10:47 - Per-user auth and adding your team
11:34 - Free resources and wrap-up

Everything here, plus the exact prompt I used, is in my free community:
https://www.skool.com/the-ai-agency
