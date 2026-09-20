# Description

Written against the delivered cut (`056 - deepseek harness - FINAL.mp4`, 17:32).
Chapters are from a local whisper-large-v3-turbo pass on the final render, not the
pre-production script — every timestamp below is a real moment in the video.
Every link was checked for a 200 on 2026-09-12.

---

## SHIP THIS

**Title:** DeepSeek Harness: The Open-Source Claude Code (Full Setup + Claude as a Sub-Agent)
**A/B challenger:** I Tested DeepSeek Harness Honestly (It Doesn't Replace Claude Code)

DeepSeek Harness hit 200,000 GitHub stars in about two weeks, and half of YouTube is calling it the end of Claude Code. It isn't. But it is the most interesting thing to happen to agents this year, and this is the honest setup: install it in one command, run any model including free local ones, and make it run Claude Code for you as a sub-agent.

I start with the thing nobody explains: what a "harness" actually is. A model on its own can't read a file, use a tool, or remember anything. The harness is the code wrapped around it — the loop, the tools, the context, the permissions, the interface. Claude Code is a harness. Codex is a harness. Cursor is a harness. The difference here is that every single one of those pieces is a plugin, all 165 of them, including the sidebar and the settings page.

Then I build the whole thing on camera: install from the quick start, connect a model through OpenRouter, then switch to 100% free and local with Ollama. I show Trajectory, which prints every step the agent took — the prompt, the context, the skill, the tool call, the result. I turn on Creator mode and watch it write its own calculator plugin and overlay it on its own UI. And I enable the Claude Code sub-agent plugin so Harness delegates the long-running work to Claude Code on your existing subscription, no API key.

Straight answer at the end: it does not replace Claude Code today. What it does is let you build a harness shaped exactly the way you work, and put it on a VPS so it's always running.

Developer preview, and I'm honest about the rough edges — including the one that broke mid-recording.

CHAPTERS
0:00 - The hype, and the honest answer
0:24 - What a "harness" actually is
1:12 - Claude Code, Codex and Cursor are harnesses too
1:39 - Installing it with one command
2:29 - Skip the desktop version (it's third party)
2:52 - Sessions and workspaces
3:12 - Connecting a model with OpenRouter
4:31 - Running it 100% free and local with Ollama
5:58 - Trajectory: see every step the agent takes
6:24 - Demo: build a Flask to-do app
7:34 - Reading the full trajectory
8:25 - Creator mode: it builds its own tools
9:01 - Everything is a plugin (all 165 of them)
9:55 - The calculator it wrote for itself
10:35 - Turning plugins off and back on
11:25 - Claude Code as a sub-agent
13:03 - Delegating a real task to Claude Code
14:09 - Watching the sub-agent write the code
15:09 - Composio's plugin list (and the one to avoid)
16:24 - The verdict: does it replace Claude Code?
17:18 - Files and wrap-up

LINKS
- DeepSeek Harness on GitHub: https://github.com/deepseek-ai/deepseek-harness
- DeepSeek Harness site (quick start): https://deepseek.com/harness/en/
- OpenRouter (the paid route, ~$10 of credits): https://openrouter.ai
- Ollama (the free local route): https://ollama.com
- Claude Code (needed for the sub-agent section): https://claude.com/claude-code
- Composio's DeepSeek Harness plugin roundup: https://composio.dev/content/best-deepseek-harness-plugins

Every command, the Ollama provider settings, and the Claude Code sub-agent config are in my free community:
https://www.skool.com/the-ai-agency

---

## Notes for upload

- Tags live in `tags.txt`, not in the description.
- No sponsorship or affiliate relationship with DeepSeek, OpenRouter, Ollama or Composio.
  Nothing in this video is paid, so no disclosure is required.
- The Composio link is the article shown on screen at 15:09. He recommends against the
  number-two plugin on that list on camera, so the link is included as reference, not
  endorsement.
- OpenRouter is `openrouter.ai`. He says ".com or .ai, I'm sorry" on camera and corrects
  himself; the description carries the correct one.
