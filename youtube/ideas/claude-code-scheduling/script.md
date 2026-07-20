# Script: Claude Code Scheduling

**Working title:** I Let Claude Code Run My Research While I Slept (Here's What It Did)
**Target length:** 9–11 minutes

---

## [0:00 – 0:35] Hook

Last week I woke up, made coffee, and Claude Code had already done three hours of research while I slept.

It pulled competitor YouTube videos. It scanned my newsletters. And it generated an audio briefing I listened to in the shower.

I didn't touch my computer once.

And the wild part? It took about ten minutes to set up.

I'm going to show you exactly how — and the three workflows I have running right now that you can steal today.

[SHOW: Screen recording of Claude Code terminal with a scheduled task log from overnight. Show the timestamp — tasks ran at 6am.]

---

## [0:35 – 1:45] What Scheduling Actually Is

So first — what is this?

Claude Code has a built-in scheduling system. It's called the `/loop` command.

[SHOW: Terminal. Type `claude` to open Claude Code.]

Instead of you typing a prompt and waiting — you tell Claude Code: run this, every morning at 6am. And it does it. On its own. Even if you're not there.

[SHOW: Type `/loop` and show the command format.]

The command looks like this. You give it an interval — could be every hour, every day, whatever — and a prompt. That's it.

[SHOW: Simple example: `/loop 24h check yt-search for claude code news and save a report`]

What makes this different from just a regular cron job or a Python script?

This isn't just automation. This is a Claude Code *agent* running — the same one you talk to. Which means if it hits a problem, it figures it out. It doesn't just crash and send you an error. It adapts.

Nate Herk called this "agentic vs. deterministic" — and it's the right way to think about it.

[NOTE: Keep this section snappy — 60 seconds max. Don't over-explain. Move to demo.]

---

## [1:45 – 3:30] Demo 1: Competitor Intelligence on Autopilot

Okay, first workflow.

Every morning, I want to know what's performing in the Claude Code space on YouTube. What's blowing up. What angles people are using. Without me having to manually search.

[SHOW: Claude Code terminal, clean workspace.]

So I have this skill — `/yt-search` — that searches YouTube by keywords and gives me a ranked report.

[SHOW: Run `/yt-search claude code` manually first to show what it does.]

Now I'm going to schedule this to run every morning automatically.

[SHOW: Type the `/loop` command to schedule it — e.g., daily at 7am, keyword: "claude code".]

That's it. Claude Code will now run this every morning and drop a fresh report.

[SHOW: Open an example report from a previous run — the actual markdown file.]

When I wake up, I've got a ranked list of what's trending, view counts, what titles are working.

This alone saves me probably an hour of manual research per week. And I didn't write a single line of code.

[NOTE: Show the actual output file. Make it feel real — this is data you actually use.]

---

## [3:30 – 5:30] Demo 2: Gmail Research Digest

Second workflow — this one's about newsletters.

I subscribe to Creator Hooks, a handful of AI newsletters, industry stuff. The problem is I never actually read them when they come in.

[SHOW: Gmail inbox — lots of unread newsletters.]

So I built a scheduled task that reads my newsletters for me.

[SHOW: Claude Code terminal.]

Every morning, Claude Code searches my Gmail for newsletters from the last 24 hours, pulls the key insights, and saves a digest.

[SHOW: Type the `/loop` command — daily, searches Gmail for newsletters/research emails, outputs a digest file.]

No API setup beyond what I already have. Just Claude reading my own inbox.

[SHOW: Open the output digest — a clean summary of what came in overnight.]

Three newsletters, key takeaways, what's relevant to my content — in one clean file.

This is the Gmail skill I actually just built — so if you want it, I'll link it below.

[NOTE: Keep energy up here. This is the "relatable" demo — everyone has email overload.]

---

## [5:30 – 8:30] Demo 3 (Hero): The Morning Research Briefing

Okay, this is the one I'm most excited about.

The first two demos are useful. This one feels like something from the future.

I wanted a morning briefing. Like — you know those news shows where someone reads you the headlines? I wanted that. But for my specific niche. Delivered as audio. Generated overnight.

Here's how it works.

[SHOW: Claude Code terminal.]

I have a scheduled task that runs at 5:30am. It takes a set of keywords — AI tools, Claude Code, creator economy — and searches the web for anything published in the last 24 hours.

[SHOW: The prompt/command. Something like: search for news about [keywords] from the past 24 hours, summarize the top 5 stories, write a 2-minute briefing script.]

It synthesizes everything into a 2-minute briefing. Then it calls the ElevenLabs API and generates an MP3.

[SHOW: The output folder — a dated MP3 file sitting there ready to go.]

And when I wake up, I just press play.

[SHOW: Play a clip of the audio briefing — Tyler's voice reading back research.]

[NOTE: If ElevenLabs isn't set up yet — record a narrated version manually for the demo and show the script output. Be honest: "here's what it generates, and here's the audio step I'm still refining."]

This is three API calls wrapped in a prompt. The whole thing took me maybe 20 minutes to build.

But think about what this actually means.

You can define the keywords that matter to you. Your industry. Your competitors. Your niche. And every single morning, you get a research briefing — without touching anything.

---

## [8:30 – 9:30] How to Start + Limitations

Okay, a few honest things before you go try this.

**The limitations:**

Your computer needs to stay on. Claude Code scheduling runs locally — so if your laptop sleeps, the task waits. [SHOW: Quick visual of the laptop/sleep issue.]

If it misses a run, it'll catch up when you open the app again — up to 7 days back.

And tasks auto-expire after 3 days as a safety guard. So for anything you want running long-term, just recreate it. Takes 30 seconds.

**How to start:**

Step one — open Claude Code. Type `/loop` and describe what you want it to do and how often.

That's genuinely it for the basics.

[SHOW: One clean final example — `/loop 24h` with a simple prompt.]

If you want to go deeper — build out the skills first, then schedule them. That's the combo that makes this really powerful.

I've got a full skills walkthrough linked below if you haven't seen that yet.

---

## [9:30 – 10:00] CTA

If this was useful — like and subscribe, it genuinely helps.

And drop in the comments: what would YOU schedule first? I'm curious what people come up with.

I'll see you in the next one.

[SHOW: End card with linked videos — Claude Code skills video, Claude Code beginners video.]
