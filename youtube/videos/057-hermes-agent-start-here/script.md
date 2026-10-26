# Script, video 057

**Working title:** Set Up Hermes Agent in 30 Minutes (Claude Code Users Start Here)
**Target runtime:** 30:00. Hard ceiling 33:00. See `titles.md` for why the ceiling is not negotiable.
**Version:** v4, written 2026-09-15. Supersedes `_v3-13min/script.md`, which was a 13-minute cut with demos that no longer exist on this machine.

Conventions: `[SHOW: ...]` is what is on screen. `[NOTE: ...]` is for you, not the mic. Spoken rhythm, short sentences.

**Verified on this machine 2026-09-15 before writing.** Every number below was read off the install, not remembered:

| Claim in the script | How it was checked |
|---|---|
| Hermes Agent v0.21.3 (2026.9.14) | `hermes --version` |
| Four profiles: coder, coder-reviewer, packager, researcher | `ls ~/.hermes/profiles/` |
| Two memory files, MEMORY.md and USER.md | `ls ~/.hermes/memories/` |
| Local models `qwen3.8:27b-q8_0` and `gemma4:e4b` | `ollama list` |
| Coder's routine ran `ok` at 21:05 on 09-14, next 08:00 on 09-15 | `hermes -p coder cron list` |
| Two default-profile routines, both `ok` | `~/.hermes/cron/jobs.json` |
| GitHub CLI authed as tylerprogramming | `gh auth status` |

**Three things are NOT verified and the script marks each one.** See `filming-guide.md` section "Verify before you roll" and do not narrate them until you have.

---

## [0:00 - 0:40] Cold open

[NOTE: pick a hook from `hooks.md`. Hook 1 is the recommendation and is reproduced here. No camera until roughly 0:25.]

[SHOW: phone, Slack, this morning's cards. Do not scroll fast, let them read one.]

This landed on my phone at eight this morning. I was not awake for it.

That is one of my agents. It pulled my repos, read the newest commit, and posted what it found. The one below it is a different agent on a different schedule, telling me what to film next.

[SHOW: cut to desktop, Bots tab, the roster with avatars]

So this is the part I actually want to show you. These are named agents on one machine. Own memory, own skills, and they can hand work to each other. By the end of this video one of them opens a real pull request on my GitHub, and another one tells me about it in Slack, and I do not touch either step.

[SHOW: camera]

This is Hermes Agent. Free, open source, from Nous Research. If you already use Claude Code you are going to get this fast. Thirty minutes, start to finish.

[NOTE: that PR promise is the open loop. It pays off at 26:00. If the PR does not land on the day you film, cut the promise from the hook too. Do not leave it hanging.]

---

## [0:40 - 2:00] What it is, and why you would run one next to Claude Code

So before we install anything, ninety seconds on what this actually is, because the name does not tell you.

Hermes is not a chatbot and it is not a coding tool. It is a process that runs.

[SHOW: plain diagram, two boxes. CLAUDE CODE: a session you open. HERMES: a process that stays running.]

And that one difference is the whole video. Think about how you use Claude Code. You open it in a repo, it does the work, you close it. Open it tomorrow and it does not know you. Every session starts from nothing. That is not a flaw, that is the design. It is a specialist you call in.

Hermes is the opposite shape. It starts once and it does not stop. Which buys you three things a session tool structurally cannot do.

[SHOW: three items building on screen]

One, it remembers. Not context inside one conversation. Actual memory on disk that survives every session.

Two, it runs when you are not there. Scheduled, on its own, laptop closed.

Three, it reaches you where you already are. Slack, Telegram, Discord, email. Same agent, same memory, on your phone.

[SHOW: back to camera]

So the honest answer to "why would I run this if I already have Claude Code" is that they are not for the same work. Claude Code is for the code. This is for everything around the code that you currently do by hand. Watching things, checking things, drafting things, remembering things. Work that is not hard, it is just constant.

And one real cost, up front. It only works while the machine it lives on is awake. We will deal with that in a minute.

[NOTE: ninety seconds, do not let this drift. If a read runs long, cut "that is not a flaw, that is the design."]

---

## [2:00 - 2:30] Where it lives

Thirty seconds on the host, because this is the one decision that matters later.

I run mine on a Mac Studio that is on all day. That is it, that is the whole requirement. A machine that stays awake.

An old laptop you leave open works. A five dollar cloud server works, and that is what I would do if I did not have a machine sitting here. Your daily laptop technically works, but you close the lid and it stops, so you will be disappointed.

[NOTE: no hardware tour. Tina spends two minutes on four options here. We spend thirty seconds because our audience already owns a computer they leave on.]

---

## [2:30 - 5:00] Install, and say hi

[NOTE: LIVE RECORDING STARTS HERE. Fresh instance. See the filming guide for the backup-and-restore move so this take is genuinely clean.]

Let's install it. Two ways, pick whichever you like.

[SHOW: hermes-agent.nousresearch.com]

If you like the terminal, one command.

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

If you would rather have an app, download the desktop version. Mac, Windows, or Linux. Same agent underneath, and the desktop is what I use, so that is what I will show.

[SHOW: the desktop app opening on a clean install]

[NOTE: dead air filler while it installs. "Same install whether this is your laptop or a five dollar server, and that matters in about twenty minutes when we get to the scheduled jobs." Do not fill with the roadmap, you already said it.]

Now the one choice that trips people. The model.

Hermes drives on anything. If you have an Anthropic or OpenAI key, use it. The easy path is the Nous Portal, which is one subscription for a few hundred models.

[SHOW: the composer model picker, the provider list]

But you do not have to pay per token at all. Around the twenty minute mark I will point this whole thing at a model running on my own machine for free, and honestly that is the setup I would want most people on.

For now, connect what you have and say hi.

[SHOW: type `hi`, the agent answers]

That is it. That is your agent.

---

## [5:00 - 8:30] Memory, tier one: the file you can open

So here is the first thing everybody skips, and it is the thing that makes the rest of it work. Tell it about yourself.

[NOTE: open on the pain first, the audience has lived this one.]

Think about the last time you opened Claude Code on a project you had not touched in a week. You spent the first two minutes re-explaining. What the stack is, how you like things done, what you already tried. You do that every session, every day, and none of it sticks.

That is not a bug. That is what a session is. But it is a tax, and this is the thing that stops paying it.

[SHOW: typing]

```
Here's some stuff about me I want you to remember. I'm a software engineer, 8 years, now doing AI engineering. I run a YouTube channel called tylerreedai about Claude Code and AI automation. I already use Claude Code every day. When you write for me: short sentences, no em dashes.
```

[NOTE: every fact in that line is load bearing later. The channel name pays off in section 7 when the skill already knows whose channel to compare. "Claude Code every day" pays off in section 11. The style rule pays off in the very next answer, on screen.]

Watch the bottom of the composer. It says running memory. It just wrote that to disk.

Now, storing it is not the interesting part. Using it is. Watch.

[SHOW: type the follow-up]

```
Given what you now know about me, what would you not bother explaining to me?
```

[SHOW: the answer. It skips what an agent is and what Claude Code is, and the answer itself is short.]

Ten seconds in and it already talks to me differently. And look, it kept the answer short, because I told it once.

Now here is what I actually want you to look at.

[SHOW: Finder, `~/.hermes/memories/`, then USER.md open in a text editor]

That is a markdown file. On my machine. I can open it, read it, and see exactly what my agent believes about me in plain English.

[SHOW: scroll it slowly. Count the files on camera.]

There are two. USER dot MD is about me. MEMORY dot MD is the agent's own notes, what it has worked out about my setup and what is in progress. And because they are just files, I can edit them.

[SHOW: edit one line live, save, ask the agent something that proves it read the edit]

If it learned something wrong, I delete the line. If I want it to always know something, I type it in myself. Try that with ChatGPT's memory. You can see a summary. You cannot open the file, and you cannot fix a line.

[NOTE: VERIFIED 2026-09-15. Two files, MEMORY.md and USER.md. There is no SOUL.md in the memories folder. Tina names three. SOUL.md exists but it lives at the profile root and it is the persona file, not a memory store. If you want to say that on camera, say it in one sentence and move on.]

---

## [8:30 - 11:30] Memory, tier two, and the thing nobody explains

That was tier one. There is a second tier, and it is doing more work than you would think.

[NOTE: SAY THE SEAM. Cut from the fresh install to the mature machine and tell the audience you did. Tina does this and it reads as honest rather than as a continuity error.]

Right, I am switching machines. Everything you have seen so far was a clean install I did for this video. This one is my actual setup, and it has months on it, because the next demo needs a memory that is not empty.

[SHOW: new session on the mature profile]

Tier two is every conversation I have ever had with it. All of them get written to a database on disk and summarized, so it can search its own history. And here is the demo I want, because it is not the one you usually see.

[SHOW: brand new session, type this, do not add context]

```
Based on everything you know about how I work, draft the outline for my next video. Don't ask me any questions first.
```

[SHOW: it searches past sessions, reads status.md and the package folder, and returns a numbered section table]

Brand new session. One sentence. No context. And it did not ask me a single question, because it did not need to.

[NOTE: this is deliberately NOT "remind me what we talked about." That demo proves storage, which is a database lookup. This one proves the memory is load bearing, because it produces work in his format from nothing. Do not swap it back.]

[NOTE: the outline it produces IS this video's outline, `OUTLINE-v4.md`. Screenshot the session before it scrolls off. If you re-run it live and get something different, use the new one, do not fake the old one.]

Now here is the detail that makes the whole design click, and I have not seen anyone explain it.

Those two files from a minute ago are capped. Hard limits. About twenty two hundred characters for the agent's notes, about thirteen hundred for the profile. You cannot dump your life story in there even if you want to.

[SHOW: the context meter, the memory slice of it]

And that is not a limitation, that is the point. Those files get loaded into the system prompt at the start of every single session. Every one. So they have to stay small, or you would be paying for your entire history on every message you send.

So now the two tiers make sense as an architecture. A tiny profile that is always loaded, and an unlimited archive that gets searched only when it is needed. Small and always on, big and on demand.

[NOTE: this is the "oh, that is why" beat. Nobody in the competitor set has it. Let it land, then move.]

---

## [11:30 - 13:30] Two settings I would actually change

Two settings worth knowing. Neither one needs an account and neither one costs anything.

First one. You can make it ask permission before it writes anything to memory.

[SHOW: terminal]

```
hermes config set memory.write_approval true
```

Flip that and instead of writing straight to the file, it queues the change and you review it.

[SHOW: `/memory pending` with a staged write in it, approve one]

So nothing goes into your agent's head without you seeing it first. That is memory with a code review step, and it is one command, not a service.

Second one, and this is already on here.

[SHOW: terminal]

```
hermes config get auxiliary.background_review
```

[SHOW: the output: enabled, provider ollama-launch, model gemma4:e4b]

There is a review pass that runs after your turns and saves what it learned. And look at what it is pointed at. That is a model on this machine. So the thing that curates my agent's memory all day is running locally and costing me nothing.

[NOTE: VERIFIED 2026-09-15, background_review is enabled and pointed at gemma4:e4b via ollama-launch. Re-run the `config get` on film day before you narrate it. If the value changed, read what is on screen, not what is written here.]

There is a tier above this, an external service that models you from your patterns, and you can point the whole thing at an Obsidian vault as well. I am not setting either up here. The two tiers you just watched are the default, they need no signups, and they are genuinely enough.

[NOTE: this is the Honcho replacement. Tina spends about four and a half minutes on Honcho plus Obsidian, both third-party, one with paid credits. We spend two minutes on two config lines. That gap is the whole reason our cut is shorter without being thinner.]

---

## [13:30 - 17:00] Skills, and the one for Claude Code users

Second feature, and this is where Claude Code users are already at home. Skills.

If you have written a Claude Code skill you know the shape. A skill is an instruction manual for a task, in markdown, that gets loaded when it is relevant.

[SHOW: Capabilities panel, Skills tab, scroll the bundled ones]

That is Capabilities. Skills and Tools on one panel.

[NOTE: the panel was called "Skills and Tools" when Tina filmed. It is Capabilities now. Say the current name once so the video does not date.]

Hermes ships with a pile of them. But the interesting part is that you do not have to write them. Watch me do a real task first.

[SHOW: a chat that already happened, the title check across the last ten uploads]

That is a job I actually wanted. Look at my last ten uploads, find the title pattern that is winning, give me five new ones scored out of ten. It did it. Now the move.

[SHOW: type]

```
Make this into a skill for checking my titles.
```

[SHOW: open the SKILL.md it wrote, in an editor]

That is the whole skill. A markdown file. A description of when to use it, and step by step what to do. It wrote that itself. I never touched a config file.

[SHOW: new chat, run `/title-check`]

And now it is a slash command, forever.

[NOTE: tell, show a real past example, then do one live. That is Tina's rhythm and it is the reusable part of her video. Do not demo this on empty state.]

Now the beat for the Claude Code users specifically, because this is the question I would have.

You already have skills. In `~/.claude/skills`. Do you have to rewrite them?

No.

[SHOW: the `claude-to-hermes-skill-porting` skill in the list, then run it on one real yt- skill]

I built a skill whose whole job is porting my Claude Code skills over. So this one goes and gets one of mine and brings it across.

[SHOW: the ported skill running in Hermes]

Same markdown idea on both sides, which is why this works at all.

And one honest thing while we are in this folder.

[SHOW: the skills list, four jarvis-prefixed skills]

Four skills for one project. It writes them as it goes, and it does drift. So every so often you go in and merge them. That is the maintenance cost, and it is real, and it is about ten minutes a month.

[NOTE: one line. Do not turn this into a section. It buys credibility for everything else.]

---

## [17:00 - 20:30] Routines: the jobs that run without you

Third feature, and this is the one that turns it from a chat window into staff.

Hermes has a built-in scheduler. You describe the job in plain English and it runs on its own. In the desktop it is the Routines pane, next to the Bots tab.

[SHOW: Routines pane, the two that are already running]

These two are mine. One at eight in the morning, one at nine at night. Weeks of green.

[SHOW: hover or open one so the last-run status is readable]

A job is three parts and that is all. A schedule, a prompt, and where to deliver it. Here it is.

[SHOW: terminal]

```
hermes -p coder cron list
```

[SHOW: the coder routine: `0 8 * * 1-5`, deliver slack, skills code-review, last run ok]

That one belongs to a different agent, which is the thing we get to at the end. Every weekday at eight it checks my repos, and it delivers to Slack. Let me just run it.

```
hermes -p coder cron run "coder: morning repo check"
```

[SHOW: the run, then cut to Slack and the card landing]

That is the same card from the cold open. Not a mockup, that is the job.

Two things worth knowing, because this is where people trip.

Every scheduled run starts a fresh session. So the prompt has to stand on its own, you cannot write it like you are continuing a conversation. Newer versions can carry the last run forward if you turn that on, which is how a monitor stops telling you the same thing twice.

And keys. Any job that touches a service needs a credential, and you never paste one into the chat. One command.

[SHOW: terminal, do NOT show a real token]

```
hermes config set GITHUB_TOKEN <your token>
```

That puts it in the env file where it belongs.

[NOTE: use a dummy value on camera or blur it. Do not read a token out loud.]

---

## [20:30 - 23:00] Free and local

Now the part I promised. You can run this entirely on your own machine.

[SHOW: terminal]

```
ollama list
```

[SHOW: the two models, qwen3.8:27b-q8_0 and gemma4:e4b]

Two rules for picking one. It has to be able to call tools, because an agent that cannot call tools is just a chat box. And you have to give it a real context window, because agents eat context and Ollama will not raise it for you.

[SHOW: Settings, Providers, Local Models. Or the one-liner.]

```
ollama launch hermes
```

[SHOW: point Hermes at the local model, then run a real task offline]

And then always test that it uses tools, not just that it talks.

[SHOW: "list the files in this folder, read the README, and tell me what this project is"]

[SHOW: it runs the tools and answers]

That is local. Model on my machine, memory on my machine, nothing leaves.

And here is the part that ties back. The background review you saw earlier, the one curating my memory all day, was already running on one of these. That has been free this whole time.

---

## [23:00 - 29:00] Bots: the payoff

Alright. This is the part I have been building to.

[SHOW: Bots tab, the roster]

Every one of these is a separate agent. Its own memory, its own skills, its own model if you want, its own scheduled jobs. And underneath, a bot is just a profile, which is a folder. There is no new concept to learn.

[SHOW: `ls ~/.hermes/profiles/`]

That is them on disk. Let me make one from nothing so you see the whole thing.

[SHOW: Bots tab, New Agent. Name, Title, Description.]

Name, title, description. And the description matters more than it looks, because that is what the other bots read to decide who to hand something to. So write it like a job posting, not like a label.

[SHOW: terminal equivalent]

```
hermes profile create packager --description "Turns research and a reference transcript into a full video package."
```

[SHOW: the new bot appearing in the roster with its avatar]

Same thing, two surfaces.

Now the handoff.

[NOTE: THIS IS THE UNVERIFIED BEAT. See the filming guide. Do the end-to-end dry run the day before and again on the morning you film. If any link in the chain does not land, film the fallback and cut the hook promise. Do not fake a PR.]

[SHOW: open Researcher's Bot Chat]

I am going to ask my research bot to hand work to my packaging bot, and then have the coding bot ship it.

[SHOW: type]

```
@packager build the package for video 058 from the research you already have. When it's done, ask @coder to open a PR with it on tylerprogramming/content and post the link to Slack.
```

[SHOW: the handoff firing, then cut away. Do not sit on a spinner.]

[SHOW: Packager's Bot Chat, the files it wrote]

[SHOW: GitHub, the actual pull request]

[SHOW: phone, Slack, Coder's message with the link]

So that is three surfaces and one story. I asked one bot, in a desktop chat. A second bot did the work. A third opened a pull request on GitHub. And it told me on my phone.

[SHOW: camera]

Now the honest limit, and you should know it before you go build your whole life on this.

Desktop is where you talk to a bot. Slack is where bots talk to you. My Slack has one app in it, so if I type at-coder in Slack, nobody answers, because Coder is not a Slack user. Bots posting out to Slack works fine. Me talking to a specific bot from Slack needs a second app set up for that bot, and I did not do it for this video.

[NOTE: this is true as of filming and it is the single most likely comment question. Say it plainly, once, and do not apologize for it.]

---

## [29:00 - 30:00] Where it fits, and the CTA

So, how I actually think about this as an engineer. It is not Claude Code versus Hermes. I run both, every day.

Claude Code is the specialist. I open it inside a repo when I am writing real code, and I close it when I am done.

This one never closes. It remembers, it runs on a schedule, and it reaches me on my phone. It is the staff around the work, not the work.

[SHOW: the Slack cards from the cold open again]

And everything you saw today is what actually ran on my machine this morning. The eight a.m. check, the nine p.m. one, the pull request. That is not a demo I built for a video, that is the setup, and the video is just me pointing at it.

If you set up the three things we did here, memory you can open, one skill it wrote itself, and one job on a machine that stays awake, you are further along than most people ever get.

Setup notes and every command from this video are in the free community, one link below.

[SHOW: end card]

See you in the next one.

[NOTE: one destination in the CTA. Do not stack the community, the newsletter and the next video.]
