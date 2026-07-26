# Script: 17 Claude Code Skills That Actually Run My Business

**THE 17 (the on-screen wall - keep count consistent everywhere):**
YouTube engine (7): /yt-search /transcribe /yt-package /yt-seo /yt-thumbnail /yt-analytics /yt-replier
Distribution (6): /yt-shorts /repurpose /social-copy /instagram-writer /flash-video /tiktok-replier
Community & money (4): /skool /email /harut /journal

**Target length:** 12-15 min | **Audience:** non-dev creators/solopreneurs | **Angle:** real system, not a staged demo

---

## [0:00 - 0:35] Hook

> You've probably seen a dozen videos where someone builds a fake business with Claude Code to show you how to make money. I'm not going to do that.

> Instead, I'm going to open up the actual Claude Code that runs my real content business. 17 skills that research my videos, write my posts, reply to my comments, and run my community.

> And here's the part that matters. None of this is code. They are just text files. I have been an engineer for years, and you do not need to be one to build any of it. If you can write instructions, you can build every single one of these.

> Let me show you the whole system.

[SHOW: Terminal open, run something that lists your skills - `/help` or `ls ~/.claude/skills/` - show the 17-skill wall (a clean on-screen list or filtered /help) as instant proof - do NOT scroll the full skills folder, it has framework skills that muddy the count]
[NOTE: Land the "you do not need to be an engineer, these are just text files" line with conviction. This is what keeps non-coders watching.]

---

## [0:35 - 1:30] What this video is (and the promise)

> So most Claude Code videos fall into two camps. Either it's a developer building an app you'll never build, or it's someone spinning up a pretend startup to sell you a course.

> This is neither. Everything I show you today is already running. Some of it is running right now, while I'm recording this, without me touching it.

> I'm going to walk through three parts of my business that Claude Code runs - how I make content, how I stay on top of comments and email, and how I run my community. Then at the end I'll show you how to build your very first skill in about two minutes.

[SHOW: Quick montage - the skills folder, a scheduled post, a cron job list, the Skool dashboard]
[NOTE: Set the three-part structure clearly. Retention comes from people knowing the map.]

---

## [1:30 - 2:45] What a skill actually is

> Before the demos, let me kill the scary part. Because "Claude Code" sounds like a developer thing, and "skill" sounds technical. It's not.

> A skill is a folder with one text file in it called SKILL.md. The top of the file tells Claude when to use it, in plain English. The rest of the file is just instructions - the same thing you'd tell an assistant if you were training them.

> That's it. No app to install, no code to compile. You write what you want done, once, and now it's a command you can run forever.

[SHOW: Open one real SKILL.md in your editor - a simple one. Scroll slowly. Point at the description line at the top, then the instructions below.]
[NOTE: This is the "you can do this too" moment. Go slow. Make it feel obvious.]

> Anthropic literally merged skills and slash commands into one thing this year. So when you hear people say slash commands, custom commands, or skills, it's all the same idea now. A text file that becomes a command.

[NOTE: Keep it plain-English. Don't go down the frontmatter rabbit hole on camera - one sentence is enough.]

---

## [2:45 - 6:30] Part 1 - The content pipeline (research to published)

> Okay, part one. The thing that used to eat my entire week. Making content.

> Here's the actual pipeline, and every arrow is one command.

[SHOW: On-screen text or simple graphic: /yt-search -> /transcribe -> /yt-package -> /social-copy]

### Demo 1a - /yt-search
> First, I don't guess what to make. I run slash yt-search.

[SHOW: Type `/yt-search claude code` in the terminal. Let it run.]

> This goes out to YouTube, finds what's actually working on a topic right now, ranks it by views, pulls the thumbnails, and writes me a research report. So instead of a hunch, I start from data.

[NOTE: While it runs, talk: "This is the difference between hoping a video works and knowing the format already works before you film."]
[SHOW: The generated report + the thumbnail grid it downloaded]

### Demo 1b - /transcribe -> /yt-package
> I pick the top video, and I run slash transcribe on it to pull the full transcript. Then I feed that into slash yt-package.

[SHOW: Kick off `/yt-package` on a transcript. Cut ahead to the finished folder.]

> And this is the one that still feels like magic. From one transcript, it gives me a complete video plan. Titles, hooks, a full script, the description, a filming guide, even thumbnail concepts. The exact thing I'm reading off of to make this video came out of this skill.

[SHOW: Open the package folder - titles.md, hooks.md, script.md, filming-guide.md]
[NOTE: Meta moment - "this video was planned by this skill." Say it out loud, it's sticky.]

### Demo 1c - /social-copy
> Then the video isn't the end, it's the source. I run slash social-copy and it turns that one video into a week of posts. LinkedIn, X, Instagram, a community post - all in my voice, because I trained it on my own transcripts.

[SHOW: Run `/social-copy`, show the generated platform files]

> So that's one topic turning into a researched video plan and a week of social content, and I barely touched a keyboard. That used to be four different tools and two full days.

[NOTE: Land the before/after. "Two days" vs "a few commands" is the emotional payoff.]

---

## [6:30 - 9:30] Part 2 - Comments + email on autopilot

> Part two is my favorite, because this one runs when I'm not even here.

> The problem every creator has - you post, comments come in, and if you don't reply in the first hour or two, you lose the engagement. But you can't sit there refreshing all day.

> So I built skills that watch for me.

### Demo 2a - the comment monitors
> Slash yt-replier and slash tiktok-replier. These check my YouTube and TikTok for new comments I haven't replied to, on a schedule, automatically.

[SHOW: Open the crontab or the scheduled job list - prove it's actually scheduled, firing on its own. Show the inbox file it produces.]

> This isn't me clicking a button. There's a job on my machine that fires every hour, finds the unreplied comments, and drops them into an inbox for me. For the easy ones - someone asking for a link - it even drafts the reply pointing them to my community.

[NOTE: The proof here is that it's genuinely scheduled. Show the real cron line. That's the trust builder.]
[SHOW: The drafted replies queue]

> I default everything to draft mode, so nothing gets posted without me. But the thinking, the finding, the writing - that's done before I sit down.

### Demo 2b - /email drips
> Same idea with email. Slash email runs my welcome sequence for new members and can send a broadcast. New person joins, the first email goes out. I'm not in the loop for any of it.

[SHOW: The email skill / a drip sequence or a sent broadcast]

> So while I'm filming this, my comments are being gathered and my emails are going out. That's what I mean by the business running itself.

[NOTE: Circle back to the hook's "running right now while I record." Payoff.]

---

## [9:30 - 11:30] Part 3 - Running my Skool community from the terminal

> Part three. My community. This is the one people don't believe until they see it.

> I run my whole Skool community from Claude Code. Slash skool.

[SHOW: Run a `/skool` command - post to the community, or sync members]

> I can write and schedule a post. I can pull my member list and see who's new. I can add a whole module to my classroom course without ever opening the website. Member sync, engagement tracking, even auto-replies to comments in the community.

[SHOW: The post landing in Skool, or the member data, or a classroom module being created]

> This is real business operations. Not a to-do app, not a toy. The actual admin work of running a paid community, turned into commands.

[NOTE: Emphasize "real operations." This separates you from every "build a todo app" tutorial.]

> And the reason this matters for you - none of these were hard to build. They're the same thing as that first SKILL.md I showed you. Just pointed at different tasks.

---

## [11:30 - 13:30] Build your first skill (do this today)

> So let me prove how simple this is by building one live, right now.

[SHOW: Create a new folder in `~/.claude/skills/`, make a SKILL.md]

> I'm making a skill. I create a folder, I make a file called SKILL.md, and at the top I write one line - what this is and when to use it. Then underneath, I just write the instructions in plain English.

[SHOW: Type a simple, real example - e.g. a skill that summarizes a YouTube video into 3 hooks, or drafts a caption in your voice. Keep it genuinely short.]

> Save it. That's it. Now I can run it as a command.

[SHOW: Run the new skill. Let it work.]

> That took two minutes. And every single skill I showed you today started exactly like that - one small text file that I improved a little each time I used it.

> The mindset shift is this. Every time you do a task twice, that's a skill. You stop being the person doing the task and you become the person who reviews the result.

[NOTE: This is the takeaway line. Slow down and let it breathe.]

---

## [13:30 - end] Recap + CTA

> So that's the real system. Not a fake business - the actual one.

> Claude Code researches and writes my content, it watches my comments and sends my email on a schedule, and it runs my community from the terminal. 17 skills, all just text files. You do not need to be an engineer to build any of it.

> If you want the skills, the prompts, and the full setup, they're free in my community - the link's in the description. There's a whole group of people building this stuff, and I'd love to see what you make.

> If this showed you something new, hit like, it genuinely helps. And I'll see you in the next one.

[SHOW: End card - free.tylerai.dev/youtube/ , subscribe, next video]
[NOTE: Keep the CTA warm and short. The proof already did the selling.]
