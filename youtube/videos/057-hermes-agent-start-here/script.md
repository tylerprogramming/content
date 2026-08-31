# Script — Set Up Hermes Agent in 10 Minutes (Claude Code Users Start Here)

Target: ~10 min. Conversational, short sentences. `[SHOW: ...]` = on screen. `[NOTE: ...]` = production.

**Structure change (v2):** hook lands by 0:30, then a punchy "look what it does" montage of real results (0:30-1:00), then straight into the live install. The old talky "what is it vs Claude Code" section is cut - the montage and the feature demos carry the differentiation. See `filming-guide.md` for record order: the montage is filmed LAST as cutaways.

---

## [0:00 - 0:30] Hook (tight, get in fast)

If you already use Claude Code, you are going to get this one fast. Hermes is the other half.

[SHOW: Hermes running in a terminal + the desktop app, quick]

It is a free, open-source agent from Nous Research. It runs on your own server. It remembers everything. It writes its own skills as it works. And it keeps going while your laptop is closed.

Before I set it up, look at what that actually gets you.

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

## [1:00 - 2:30] Install and pick a model (LIVE RECORDING STARTS HERE)

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

## [2:30 - 4:00] Feature 1 — It remembers everything

First thing to do, and the thing everyone skips: tell it about yourself.

[SHOW: typing the line below]
```
Here is a bit about me, please remember this: I'm a software engineer building AI content. Keep answers concise.
```

Watch this. It says running memory. It just wrote that to disk.

Here is where it lives.

[SHOW: the .hermes folder in Finder, then memory/user.md open in a text editor]

That is plain markdown. You can read exactly what your agent knows about you. A file about you, a file about your setup, a file about the agent itself.

And that is just the first tier. Every conversation you have also gets saved to a database. So when I start a brand new session and ask about something from last week, it searches its own history and pulls it back.

[SHOW: new session, type below, it runs session search and answers]
```
Remind me what we discussed about my content workflow earlier this week.
```

This is the thing Claude Code cannot do out of the box. It remembers.

---

## [4:00 - 5:45] Feature 2 — It writes its own skills

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

## [5:45 - 8:30] Feature 3 — It runs on a schedule, without you

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

## [8:30 - 9:30] Bonus — Run it 100% local and free (desktop or terminal)

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

## [9:30 - 10:30] Where it fits, and what's next

So here is how I think about it as a software engineer. This is not Claude Code versus Hermes. I run both.

Claude Code is my specialist. I open it in a repo when I am writing serious code. Hermes is my generalist. It is always on, it remembers, and it handles the background work all day.

[SHOW: split - Claude Code in a repo on one side, Hermes running a scheduled task on the other]

If you set up just those three things - memory, a self-written skill, and one cron job on a server that stays on - you already have something most people never get to.

Next I am going to show you exactly how I use it every day, and how to run it fully private with a local model. If you want those, subscribe so you catch them.

[SHOW: end card]

And if you want the setup notes and the commands from this video, they are in the free community, link below. See you in the next one.

[NOTE: CTA stays short, one destination]
