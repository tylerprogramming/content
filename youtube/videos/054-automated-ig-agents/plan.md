# 054 - I Fully Automated My Instagram With AI Agents (REMAKE)

## What this is
A 2026 full-build remake of Tyler's own short video, swapped from X to Instagram.

## Original source
- Title: "Here's How I Fully Automated My X Account with AI AGENTS"
- Channel: @TylerReedAI (his own video)
- Views: 13,893
- Published: 2024-11
- Length: 4:27 (short, thin build)

### What worked in the original
- The "I Fully Automated My ___ With AI Agents" showcase format. People want to see the
  machine actually run, not hear about it.
- Concrete outcome framing: an account that runs itself.
- Rode the "AI agents" wave while it was fresh.

### Why it underperformed its ceiling
- Only 4:27. It teased the idea but never showed a real, end-to-end build.
- Built on X, which is a weaker fit for showable content (image/carousel/reel work
  reads better on screen than tweets).
- 2024 tooling. The agent glue was clunky and dated fast.

## The remake in one line
Claude Code runs an Instagram account end to end: it generates the content, schedules and
publishes it through Blotato, and reads the comments and DMs and drafts the replies. Tyler
approves before anything goes live.

## The X -> IG swap (per Tyler)
- Instagram is far more visual, so the "AI did the real work" showcase actually has
  something to show: carousels, reel concepts, captions, generated images.
- It ties directly to Tyler's real stack. He already runs Blotato + Claude Code for his
  own cross-platform posting, so this is a real system, not a demo rigged for the camera.
- Broader relevance. Way more people care about an Instagram that runs itself than an X bot.

## What has changed for 2026 (the reason a remake is honest, not a rerun)
- Blotato exposes an MCP server (mcp.blotato.com/mcp). Claude Code posts to Instagram with
  one authenticated call, and the same call reaches 9 platforms. No wrestling Meta's auth.
- Scheduling runs on Blotato's side, so the agent does not have to stay running for a queued
  post to publish.
- Claude Code Skills exist now. The whole workflow lives in a folder of markdown files, not
  a brittle script.
- The comment/DM half is real but fenced by rules worth naming on camera: Instagram's
  messaging is user-initiated only, capped around 200 automated actions an hour, and DMs
  are blocked outside a 24-hour reply window. That constraint is part of the honest story.

## The concrete build shown (3 agents / 3 acts)
1. CONTENT AGENT. Claude Code takes a topic, writes the carousel or reel concept, drafts the
   caption in Tyler's voice from a voice file, and generates the images. Output lands as
   files in a folder.
2. PUBLISH AGENT. Claude Code hands the finished post to Blotato over MCP, sets the schedule,
   and confirms it queued. One call, and it is on the Instagram calendar.
3. INBOX AGENT. Claude Code reads the recent comments and DMs, drafts replies in Tyler's
   voice, and lines them up for approval. It never sends blind.

## The honesty beat (non-negotiable)
Nothing auto-posts on its own. Every post and every reply waits for Tyler's approval before it
publishes. The agents do the work. Tyler is still the one who says go. This is stated plainly,
early, and it is the thing that keeps the video credible instead of hypey.

## Delayed credibility
Tyler's resume (8 years as a software engineer at IBM and Chase, now an AI engineer at Pfizer)
lands around 0:35, after the payoff, never up front. Framed as "I still would not hand my
account to a bot I did not trust, so here is where I keep a human in the loop," not as a flex.

## Target audience
- Creators and small brands drowning in the manual Instagram grind (make it, post it, answer
  everyone) who want the repetitive parts off their plate.
- Claude Code and automation-curious people who want to see a real agent system, not a toy.
- Anyone with repetitive work. Instagram is the setting; the takeaway (agents do the doing,
  you keep approval) transfers to any inbox-and-output job.

## Angle
Not "grow your Instagram." The subject is using AI to take the repetitive Instagram work off
your plate while you stay the one who approves. Show the real system, admit the guardrails,
keep a human on the trigger.

## Target
10k+ views. Full build, 10 to 14 minutes.

## Working title
I Fully Automated My Instagram With AI Agents
