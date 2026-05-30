# Claude Routines + Claude Code — 30-Min Tutorial Plan

**Target runtime:** 28-30 minutes
**Angle:** Routines (cloud) + Claude Code (local) as a complete automation stack for creators/solopreneurs — business outcomes, not just technical demos
**Differentiation:** Nobody in the top 12 competitor videos frames Routines alongside Claude Code local with a business lens. Most just say "kills n8n."

---

## Reference Sources

- **Structure model:** Dan Martell — `~/content/transcripts/transcript_XRU-CjzYt_o.txt` (numbered 6-point structure, shock hook, personal authority, demo → business value → lead magnet → CTA)
- **Content cues:** Nick Saraev — `~/content/transcripts/transcript_j3aXJNu9804.txt` (routine build walkthrough, API triggers, n8n comparison, 3 demos)
- **Tone model:** Tyler's AntiGravity video + existing scripts — confident but not arrogant, credentials as facts, short sentences, "right?" and "okay" as checkpoints, teaches technical terms simply
- **Thumbnail reference:** `~/content/youtube/claude-routines-content-system/reference-thumbnails/nick-saraev.webp`

---

## Tyler's Existing Routines (already running)

1. **Morning inbox digest** — Gmail + Slack, 5 AM trigger, categorizes and drafts replies
2. **Apify competitor monitor** — Scrapes TikTok hashtag, posts digest to Slack
3. **Content pipeline helper** — (TBD — the carousel-routine repo is attached and ready)

---

## Structure (30 min)

### [0:00 - 1:00] HOOK
- Pattern interrupt: "Everybody's saying Claude Routines killed n8n. That's not the story."
- Authority drop: "I've built AI automations for Fortune 500 companies — JPMorgan, Pfizer. I run 22+ Claude Code skills that publish 30+ pieces of content every week. So when Routines dropped, I was in it day one, running them with Slack, Gmail, and Apify."
- Promise: "In this video I'll show you what Routines actually are, 3 real ones I run in my business, how to build your own live, then when to use Claude Code on your machine instead. By the end you'll know exactly where Routines win, where Claude Code wins, and how to use both."
- Curiosity gap: "Stick around — I'll show you a loop in Claude Code watching a process in real time. That's the piece nobody's talking about."

### [1:00 - 3:00] POINT 1: What Routines Actually Are
- Cloud container vs local machine — say it plainly
- 3 trigger types: schedule, GitHub event, API/webhook
- MCP connectors: Slack, Gmail, Apify, GitHub, and more
- "It's Claude Code, but running in a cloud container on Anthropic's machines, not yours. Laptop closed. You're asleep. It still runs."

### [3:00 - 5:00] POINT 2: The Business Case
- Frame: "What if you had an employee who worked while you slept? Never took PTO. Never got sick. Cost you pennies."
- Math: VA at $20/hr × 5 hrs/day = $100/day. Routine = pennies per run.
- Compounding: 10-min daily task → 60+ hrs/year back
- Borrow Dan's line (adapted): "You don't need to do the work. You need to direct it."

### [5:00 - 8:30] POINT 3: Routine Example 1 — Morning Inbox Digest
- Show the actual Routine config on claude.ai
- Gmail connector pulls unreads
- Claude categorizes, drafts replies based on context
- Slack connector sends you the summary before you wake up
- Click "Run Now" to demo live
- **Business value:** "I wake up and half my inbox is triaged. That's 45 min saved every morning — 195 hours a year. A VA for this costs $1,500/month minimum."

### [8:30 - 12:00] POINT 4: Routine Example 2 — Apify Competitor Monitor
- Your Apify-powered TikTok hashtag scraper
- Routine runs daily, pulls new viral videos, summarizes angles, posts to Slack
- Show the Routine config + Apify connector + Slack output
- **Business value:** "I get a competitive report every morning. A social media manager would charge $800-1,500/month for this. It runs while I'm working out."

### [12:00 - 16:30] POINT 5: Build a Routine From Scratch — LIVE
- This is the instructional meat — go slow, show every click
- Navigate to claude.ai/code/routines
- Click "New Routine"
- Name: something real Tyler would actually use (e.g. "Daily YouTube idea generator")
- Paste prompt (structured as SOP — call out Nick's advice: "be more precise than a skill because it runs hands-off")
- Select repo, select model (Opus 4.6 1mil)
- Add Gmail connector (show the OAuth)
- Add Slack connector
- Add schedule trigger (6 AM)
- Hit "Run Now" to test — watch it execute live
- Show Slack output

### [16:30 - 17:30] POINT 6: Switch to Claude Code Local
- Transition: "Routines are amazing for scheduled, hands-off work. But there's a whole category they CAN'T do — interactive, iterative, one-off work on your own machine. That's Claude Code."
- "Let me show you where Claude Code wins."

### [17:30 - 20:30] POINT 7: Claude Code Demo — Iterative Work
- Run `/yt-search claude routines` live
- Show results populating in terminal
- Follow-up prompt: "Now search 'claude code' and compare engagement rates"
- Point: "This is what Routines can't do — conversational, iterative work where you're steering in real time. Routines run hands-off. Claude Code is hands-on."
- Access to local files, local git, local environment

### [20:30 - 23:30] POINT 8: The `/loop` Demo in Claude Code
- THIS IS THE "NOBODY'S TALKING ABOUT IT" MOMENT
- Run `/loop` watching a process (e.g. polling a build, checking a deploy, running `/yt-search` on a new keyword every hour)
- "Routines do cloud schedules. /loop does local schedules. Different tools. Different jobs."
- **Key distinction:** Routines = cloud cron. Loop = local polling + iteration on YOUR machine with full access to YOUR files.

### [23:30 - 26:30] POINT 9: Pros/Cons + Decision Framework
- On-screen comparison table:

| Feature | Routines (cloud) | Claude Code (local) |
|---------|-----------------:|--------------------:|
| Runs on | Anthropic cloud | Your machine |
| Trigger | Schedule / API / Webhook | You / /loop |
| Best for | Hands-off recurring | Interactive / iterative |
| Laptop closed? | Still runs | Doesn't run |
| Access local files | No | Yes |
| Token cost | Yes | Yes |
| Compute cost | Anthropic pays | You pay |
| MCP connectors | Yes (web OAuth) | Yes (any MCP) |
| Real-time steering | No | Yes |
| Best use case | Morning digests, scheduled scraping, API-triggered pipelines | Content creation, research, dev work, anything needing judgment |

- Decision framework: "If the task is predictable and you want it done without you — Routine. If the task requires thinking, exploration, or your judgment — Claude Code. Use both. That's the stack."

### [26:30 - 28:30] POINT 10: Make the Switch (Dan-style action close)
- "Here's my challenge: pick ONE task you do every day. Turn it into a Routine this week. Then come back and tell me what changed."
- "If you want the full system I run — 22+ Claude Code skills, the Routines I showed you, the whole content pipeline — I teach all of it inside my Skool community. Link in description."
- "Leave a comment: what's the first Routine you're going to build?"

### [28:30 - 29:30] OUTRO + CTA
- Sub + next video lead
- "Thanks for watching."

---

## Hooks to test (A/B candidates)

1. "Everybody's saying Claude Routines killed n8n. That's not the story."
2. "Claude just turned into a 24/7 automation platform. Here's what nobody's showing you."
3. "I ran Claude Routines for a week with Gmail, Slack, and Apify. Here's what it replaced."
4. "Anthropic quietly dropped something that replaces your VA. Most creators haven't noticed."
5. "Routines, Claude Code, and one loop command — this is the stack that runs my whole business."

## Title candidates

1. "Claude Routines + Claude Code — The Automation Stack Nobody's Teaching"
2. "I Built a Business on Claude Routines (Full Walkthrough + Claude Code Loop)"
3. "Claude Routines vs Claude Code — When to Use Each (Full Tutorial)"
4. "The Claude Automation Stack: Routines, Code, and /loop Explained"
5. "Replace Your VA with Claude Routines (Plus the Claude Code Trick Nobody Uses)"

## Thumbnail direction

- Nick Saraev's style as reference (`reference-thumbnails/nick-saraev.webp`)
- Tyler's face + big bold text
- Possible text: "ROUTINES + CLAUDE CODE" or "THE AI STACK"
- Visual split: cloud icon / terminal icon
