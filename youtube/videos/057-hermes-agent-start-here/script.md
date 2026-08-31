# Script — Set Up Hermes Agent in 10 Minutes (Claude Code Users Start Here)

Target: ~13 min. Conversational, short sentences. `[SHOW: ...]` = on screen. `[NOTE: ...]` = production.

**Structure change (v3, 2026-08-31):** the "what is it / why would I run this" section is BACK, and it is the segment that makes the rest land. v2 cut it and let the montage carry the differentiation; that was wrong. The same beat carried video 056 and it is what people searching a tool name actually need. Memory is also promoted from a 90-second feature to the hero, because it is the one thing Claude Code structurally cannot do, and the script already says so. Target moves ~10:30 → ~13:00, still less than half Tina's 29:40.

See `filming-guide.md` for record order: the montage is filmed LAST as cutaways.

---

## [0:00 - 0:30] Hook (tight, get in fast)

If you already use Claude Code, you are going to get this one fast. Hermes is the other half.

[SHOW: Hermes running in a terminal + the desktop app, quick]

It is a free, open-source agent from Nous Research. It runs on your own machine. It remembers everything. It writes its own skills as it works. And it keeps going while your laptop is closed.

Here is the part nobody tells you though. Most people install this, poke at it for ten minutes, and never open it again. And it is almost always the same three things they skipped. Get those three right and it stops being a toy and starts being staff.

Before I set it up, look at what that actually gets you.

[NOTE: the three things = the three features (memory, a self-written skill, one cron on an always-on host). The outro already pays this off word for word - "if you set up just those three things." This line is what sets it up. Stakes framing borrowed from Tina's open, compressed to 12 seconds.]

[NOTE: no channel intro. 20-25 seconds max, then hard cut to the montage]

---

## [0:30 - 1:00] What it actually does (montage — FILM LAST, cutaways)

[NOTE: this whole section is B-roll captured from your mature Hermes on the VPS AFTER the main take. Fast cuts, tight voiceover. Three real results.]

[SHOW: a morning brief in Telegram on your phone, ~7am - channel views + top video]
Seven in the morning, this was already on my phone. My channel's numbers and my top video, pulled and sent while I slept.

[SHOW: a Discord channel or terminal - "12 new YouTube comments summarized" with draft replies listed]
Overnight it read my new YouTube comments, summarized them, and drafted the replies. I just approve them.

[SHOW: a phone notification - "Heads up: [competitor channel] just posted a new video"]
And the moment a competitor I watch posted, it pinged me.

[SHOW: quick shot of the VPS terminal, Hermes process running]
No laptop babysitting. It runs on a five dollar server all day.

Here is the whole setup, and the three features that make it worth running.

[NOTE: this montage IS the sell. It replaces the old explainer. Keep it under 30 seconds, energy up]

---

## [1:00 - 2:30] What this actually is, and why you'd run one

Before we install anything, thirty seconds on what this thing is, because the category is new and the name does not tell you.

Hermes is not a chatbot and it is not a coding tool. It is a process that runs.

[SHOW: a plain diagram - CLAUDE CODE = a session you open. HERMES = a process that stays running.]

And that one difference is the whole thing. Think about how you use Claude Code. You open it in a repo. It does the work. You close it. And when you open it again, it does not know you. Every session starts from nothing. That is not a flaw, that is the design. It is a specialist you call in.

Hermes is the opposite shape. It starts once and it does not stop. Which buys you three things a session-based tool structurally cannot do.

[SHOW: three items building on screen as you say them]

One, it remembers. Not context inside one conversation, actual memory on disk that survives across every session, forever.

Two, it runs when you are not there. Scheduled, on its own, at three in the morning, laptop closed.

Three, it reaches you anywhere. Telegram, Discord, Slack, email. Same agent, same memory, on your phone.

[SHOW: back to camera]

So the honest answer to "why would I run this if I already have Claude Code" is that they are not for the same work. Claude Code is for the code. This is for everything around the code that you currently do by hand. Watching things. Checking things. Drafting things. Remembering things. The work that is not hard, it is just constant.

It is free, it is open source, it is from Nous Research, and it runs on your own machine or a five dollar server. There is one real cost and I will be straight about it up front: it only works while the machine it lives on is awake. We will deal with that later in the video.

[NOTE: 90 seconds, do not let it drift. If a read runs long, cut the "not a flaw, that is the design" line.]

---

## [2:30 - 4:00] Install and pick a model (LIVE RECORDING STARTS HERE)

Let's install it. Two ways, pick whichever fits you.

[SHOW: hermes-agent.nousresearch.com]

If you like the terminal, one command.

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

[SHOW: paste into terminal, the onboarding sequence running]

If you would rather have an app, download the desktop version for Mac, Windows, or Linux. Same agent, nicer interface.

[SHOW: desktop app opening, clean chat interface]

Now the one choice that trips people up: the model. Hermes drives on anything. The easiest way to start is a frontier model through the Nous Portal, hundreds of models on one subscription.

But you do not have to pay per token. At the very end I will show you how to run it on a model that lives on your own machine, completely free. For now, connect what you have and say hi.

[SHOW: sending "hi", the agent responding]

[NOTE: dead-air filler while it installs - "same install whether this is your laptop or a five dollar VPS, and that VPS part matters in a few minutes"]

---

## [4:00 - 6:15] Feature 1 (the big one) — It remembers everything

This is the feature. If you only take one thing from this video, take this one, because it is the thing I said Claude Code structurally cannot do.

First move, and the thing everyone skips: tell it about yourself.

[SHOW: typing the line below]
```
Here's some stuff about me I want you to remember. I'm a software engineer, 8 years, now doing AI engineering. I run a YouTube channel called tylerreedai about Claude and AI automation. I already use Claude Code every day. When you write for me: short sentences, no em dashes.
```

[NOTE: every fact in that line is load-bearing later. The channel name pays off in the skills beat when it already knows whose channel to compare against. "Claude Code every day" pays off in the outro. The style rule pays off in the very next answer, on screen.]

Watch the bottom. It says running memory. It just wrote that to disk.

Now before I show you the file, watch this, because storing it is not the interesting part. Using it is.

[SHOW: type the follow-up]
```
Given what you now know about me, what would you not bother explaining to me?
```

[SHOW: it answers - it won't explain what an agent is, or how Claude Code works, and the answer itself is short]

Ten seconds in and it already talks to me differently. And notice it kept the answer short, because I told it to once.

And here is what I want you to actually look at.

[SHOW: the .hermes folder in Finder, then memory/user.md open in a text editor]

That is a markdown file. On my machine. I can open it, read it, and see exactly what my agent believes about me, in plain English.

[SHOW: scroll the file slowly]

There are a few of these. One about me, one about my setup, one about the agent itself. And because it is just a file, I can edit it. If it learned something wrong, I delete the line. If I want it to always know something, I type it in myself.

[NOTE: land this. Compare to a black box on purpose.]

Think about how different that is from every assistant you have used. ChatGPT has memory, but you cannot open it. You cannot read the file. You cannot fix a line. Here the memory is yours, it is text, and it is sitting in a folder.

That is tier one. There are two more.

[SHOW: on-screen list building: 1 core files / 2 session history / 3 optional plugins]

Tier two is every conversation you have ever had with it. All of them get written to a database on disk and summarized, so it can search its own history. Watch.

[SHOW: brand new session, type below]
```
Remind me what we discussed about my content workflow earlier this week.
```

[SHOW: it runs a session search and answers with the real detail]

Brand new session. It went and found it. And notice what did not happen: I did not paste anything in, I did not point it at a file, I did not re-explain who I am. It just knew.

Tier three is optional and I will not set it up here, but you can plug in deeper user modeling, or point it at an Obsidian vault so its memory and your notes are the same thing.

[SHOW: back to camera]

Here is why this matters more than it sounds. Every one of these tools starts a session from zero. So you spend the first two minutes of every session re-explaining your setup, your preferences, your project. Multiply that by every session, every day. This is the thing that stops.

And the compounding part: the longer it runs, the better it gets, because it knows more about you. A session-based tool is exactly as good on day two hundred as it was on day one. This one is not.

[NOTE: this is the hero beat now, ~2:15. Let the file on screen breathe. Do not rush the "I can edit it" moment.]

---

## [6:15 - 8:00] Feature 2 — It writes its own skills

Second feature, and this is the one Claude Code users will feel at home with: skills.

If you have built a Claude Code skill, you know the idea. A skill is an instruction manual for a task. Hermes ships with a bunch already.

[SHOW: skills and tools panel, scroll the pre-built skills]

But here is the magic. You do not have to write them. Watch me give it a real task, the kind of thing I actually want every week.

[SHOW: type a real task]
```
Look at my last 20 YouTube uploads and the recent top videos from these three channels: [competitor 1], [competitor 2], [competitor 3]. Find the patterns in what is getting views, then give me 5 new video ideas I could film, each scored 1 to 10 with a one line reason.
```

It pulls the data, finds the patterns, and hands me scored ideas. Now the important part. I just say:

[SHOW: type below]
```
Make this into a skill for finding my next video.
```

Done. Now let me show you what it actually did, because this is simpler than it sounds.

[SHOW: open ~/.hermes/skills/next-video/SKILL.md in a text editor]

That is the whole skill. A plain markdown file in a skills folder. A description of what it does, and step by step how it should do it next time. It wrote that itself, using a built-in skill tool. You never touched a config file.

And now I can call it with a slash command forever.

[SHOW: run it]
```
/next-video
```

I did the exact same move to build a skill that drafts my Skool post from a new video, and a couple of others. That is the learning loop. It did the work once, wrote the how-to to disk, and kept it. Do this with everything you repeat, and the agent slowly turns into your setup.

---

## [8:00 - 10:45] Feature 3 — It runs on a schedule, without you

Third feature, and this is the one that turns it from a chatbot into an employee: cron jobs and gateways.

Hermes has a built-in scheduler. You describe a task in plain English, and it runs on its own.

[SHOW: setting up a scheduled task]
```
Every hour, check these channels for new uploads: [competitor 1], [competitor 2]. The moment one posts, send me the title and link on Telegram.
```

I asked in plain English, but watch what it actually created.

[SHOW: run `hermes cron list` in the terminal, then open the new job]

A cron job is just three things: a schedule, a prompt, and where to deliver it. Here it is. Every hour, this exact prompt, delivered to Telegram. You can also make it by hand with one command if you want.

[SHOW: hermes cron create "0 * * * *" "..." --name "competitor-watch" --deliver telegram]

Two things worth knowing, because this is where people trip. Every scheduled run starts a fresh session. It has no memory of last time. So the instruction has to stand on its own. And before it ever runs, Hermes checks the job will actually work: the model key, the skills it needs, and that it can really reach your Telegram. If something is missing, it tells you now, instead of failing silently.

Let me trigger it once to prove it.

[SHOW: hermes cron run "competitor-watch", then a ping arriving on Telegram - "[competitor] just posted: <title> <link>"]

And it can reach you anywhere. Telegram, Discord, Slack, WhatsApp, email. Same agent, same memory, on your phone.

One setup note, because it is the step people fumble: keys. Any job that touches a service needs a credential, and you never paste it in the chat. You drop it in with one command.

[SHOW: hermes config set GITHUB_TOKEN <paste your token>]

Now it lives in the .env file, not the conversation. Same move for any service, YouTube included.

And as a software engineer, the cron I lean on most is a GitHub one. Every night it pulls my repos, runs the tests, and pings me on Telegram only if something broke. I wake up already knowing what is red. Alongside that, one summarizes my new YouTube comments and drafts the replies in Discord, and one sends my channel numbers every morning. But it only reads and drafts, it never posts. Publishing goes through my own scheduler. Same pattern every time: describe it once, it runs forever.

Now one honest thing, because it matters. Hermes runs as a background process. It only keeps working while the machine it lives on is awake. So on your laptop, you close the lid, it sleeps. That is why you do not run it on your laptop for this.

You put it on a host that is always on. That is either a machine you leave running, like a Mac mini in the corner, or a five dollar cloud server, a VPS, that is on twenty four seven by design. You install Hermes there once, and your laptop just becomes a remote you check in from.

[SHOW: a terminal SSH'd into a cheap VPS with Hermes running, or the VPS provider dashboard]

Now picture this. It is on that five dollar server, on twenty four seven. Overnight it runs your briefing, checks your systems, drafts your replies, and it is waiting for you in the morning, laptop closed the whole time. That is the piece Claude Code does not try to do.

[NOTE: this is the "aha" - let it breathe. Being honest about the laptop limitation builds trust]

---

## [10:45 - 11:45] Bonus — Run it 100% local and free (desktop or terminal)

One more, because I promised you free. You can run this entirely on your own machine, no API keys. I already have Ollama installed, so let me point Hermes at it. I will show you both ways, terminal and the desktop app.

First, pull a model that can actually use tools. Not every model can, and an agent that cannot call tools is useless. I will grab a tool-capable one.

[SHOW: terminal]
```
ollama pull qwen3
```

Here is the one gotcha that trips everyone. Agents need a big context window, and Ollama does not report one, so you have to set it yourself. Restart Ollama with at least sixty four thousand.

[SHOW: terminal]
```
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
```

Now connect Hermes. The fast way is a single command.

[SHOW: terminal]
```
ollama launch hermes
```

Or do it by hand: run the model picker, choose a custom endpoint, and point it at Ollama's local address, with a blank API key.

[SHOW: terminal - `hermes model`, choose custom endpoint, enter http://127.0.0.1:11434/v1, leave key blank, confirm the model]

Prefer the app? Same idea. In the desktop, open Settings, go to Models, click Edit models, Add provider, pick a custom OpenAI-compatible provider, paste that same local address, leave the key blank, and select your model.

[SHOW: desktop app - Settings > Models > Edit models > Add provider > custom endpoint http://127.0.0.1:11434/v1]

Then always test that it actually uses tools, not just chats.

[SHOW: run a real task fully offline, e.g. "list the files here, read the README, and tell me the project name"]

Now everything is private. The model is on your machine, the memory is on your machine, nothing leaves. For anyone who cares about privacy or cost, this is the setup.

---

## [11:45 - 13:00] Where it fits, and what's next

So here is how I think about it as a software engineer. This is not Claude Code versus Hermes. I run both.

Claude Code is my specialist. I open it in a repo when I am writing serious code. Hermes is my generalist. It is always on, it remembers, and it handles the background work all day.

[SHOW: split - Claude Code in a repo on one side, Hermes running a scheduled task on the other]

If you set up just those three things - memory, a self-written skill, and one cron job on a server that stays on - you already have something most people never get to.

Everything I showed you here is running on mine right now. The competitor watch, the comment drafts, the morning brief. That is not a demo I built for the video, that is the setup.

The next one is the multi-agent version, where several of these run at once and hand work to each other. If you want that, subscribe so you catch it.

[SHOW: end card]

And if you want the setup notes and the commands from this video, they are in the free community, link below. See you in the next one.

[NOTE: CTA stays short, one destination]
