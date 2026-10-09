# Description

OpenAI's new Agents API runs on your own Mac, not just in a hosted sandbox. Every guide I found uses OpenAI's cloud container, which bills at $0.03 to $1.92 per 20-minute session on top of tokens. The docs say the environment can be a laptop, so in this video I run the Codex harness against a folder on my Mac in three steps: create a session with a self-hosted environment, run `codex exec-server` on the machine, and send it work. Their loop, my files, no container bill.

Then I show what it costs, the two limits I would want to know before building on it (US-only data residency, no zero data retention even when self-hosted), and I run the same task on the local agent I already have on this Mac for zero, so you can see where each one fits. I have been a software engineer for eight years and I run both; this is the comparison I wanted and could not find.

## Chapters
00:00 - [UPDATE] A file lands on my Mac from OpenAI's cloud
00:35 - [UPDATE] What the Agents API actually is
02:00 - [UPDATE] Step 0: two keys and one install
03:15 - [UPDATE] Step 1: create a session pointed at your Mac
05:00 - [UPDATE] Step 2: codex exec-server
06:30 - [UPDATE] Step 3: send it real work
08:45 - [UPDATE] What it costs, and the two limits
10:15 - [UPDATE] Same task, local, for zero
11:30 - [UPDATE] Which one to reach for

## Links
Scripts from this video (create_session.py, send.py, stream.py): [UPDATE - Skool link]
Set up the local agent (the other half of this): [UPDATE - 057 link]
Agents API launch post: https://openai.com/index/introducing-the-agents-api/
Self-hosted sandboxes doc: https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted
Pricing (Containers): https://developers.openai.com/api/docs/pricing
Codex harness source: https://github.com/openai/codex
