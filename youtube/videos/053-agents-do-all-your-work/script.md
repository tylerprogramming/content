# Script - 053 How To Use AI Agents To Do ALL Your Work

Format: tight showcase-led build, target 30 to 40 min. Cold-open payoff, then the one idea,
then build 4 agents live, then the subagent pattern, honest limits, CTA.

Voice: short spoken sentences, "so" openers, hedges, no em dashes, no hype words, humble.
Markers: [SHOW: ...] = what is on screen. [NOTE: ...] = production / retention note.

---

## 0:00 - 0:41 COLD OPEN (use Hook A verbatim, see hooks.md and first-2-min-opening.md)

[SHOW: agents-already-ran montage, face hidden until 0:08. Briefing doc, triaged inbox,
ClickUp task flipping done, calendar block appearing.]
[NOTE: this is the retention make-or-break. Follow first-2-min-opening.md second by second.]

VO: (Hook A) "This morning my email was already sorted, my calendar was already cleared, and
my tasks were already updated before I got out of bed..." through the roadmap card and hard cut
at 0:41.

---

## 0:41 - 2:00 SHOW IT RUNNING (live - per first-2-min-opening.md rev 2)

[SHOW: hard cut to Claude Code. The morning-briefing agent runs LIVE. Webcam PIP bottom-right, push-in.]

So watch this. This is Claude, and I am running the agent right now, on my real accounts. Not a
recording, not a fake inbox.

[NOTE: real-time generation is the money shot, let it actually play a beat.]

It is reading everything from the last twenty four hours. Now it is checking today's calendar. Now
my open tasks. And there is the briefing, writing itself. One of these already ran at six this
morning while I was asleep, this is just me running it again so you can see it is real.

[SHOW: highlight-sweep the three sections of the briefing as he names them.]

Three parts. What happened while I was out. What is on today. And what is slipping.

That last one is the part I actually care about. It is not just listing my tasks, it is telling
me which ones are aging. [NOTE: animated highlight on the "slipping" line.]

[SHOW: cut to the inbox, labels already applied: Action, Waiting, FYI, Promo.]

And here is my inbox. Every email from the last day is already sorted into four buckets. The
ones that need me. The ones I am waiting on. The stuff that is just for my information. And the
promotional noise I will never read.

I did not sort any of this. So now the whole point.

---

## 2:30 - 5:00 THE ONE IDEA (an agent is a text file plus tools)

[SHOW: open one agent file in the editor. It is short. Markdown. Scroll it slowly.]

So here is the thing that makes all of this click, and it is way less complicated than it looks.

So here is the whole model, and it is the one thing to remember. An agent is a text file that says
what its job is, plus your apps as its tools, put on a schedule. And its memory is just more files.
That is the entire idea.

[SHOW: cards build. Card 1: "Instructions (a text file)". Card 2: "Tools (your apps)". Card 3: "A schedule". Card 4: "Memory = more files".]
[NOTE: kinetic caption on the model line, this is the sentence you want people to repeat.]

The instructions are in plain English. The tools are the apps you already have, your email, your
calendar, your tasks. They get connected through something called MCP, and you do not have to
understand MCP to use it, you just turn it on.

[NOTE: chip "MCP = plug your apps in". Do not lecture on the protocol, keep it a footnote.]

And I want to be straight with you here, because most videos on this are not. A lot of what gets
called an "AI agent" is really an automation. A fixed set of steps, wired up once, with one AI step
bolted in the middle. It is useful, but it only ever does exactly what you drew. A real agent is
different. You hand it a goal and the tools, and it decides the steps itself. Everything I am
building in this video is the real thing, deciding what to do, on my real accounts. [NOTE: two-card
graphic, "AUTOMATION: fixed steps you drew" vs "AGENT: decides its own steps". This is a
differentiator and a curiosity spike, land it, then move on, do not lecture.]

So when I say "agent," I do not mean some giant system. I mean a short file that says "read my
inbox, sort it into these four buckets, draft replies to the urgent ones," and then it has
permission to actually touch my email.

[SHOW: side by side, the 20-line file next to the result it produced.]

Twenty lines of English produced everything you just saw. So let me build these with you, one
at a time, and you will see there is no magic in any of them.

[NOTE: roadmap card reprise, "The 4 agents: 1 Briefing, 2 Inbox, 3 Content, 4 Calendar".]

---

## 5:00 - 12:00 AGENT 1 - THE MORNING BRIEFING AGENT

[SHOW: blank file. Type the instructions live, section by section, captions mirror key lines.]

Let's build the briefing agent first, because it is the one that pays for itself day one.

So I open a new file and I just tell it what I want. Read my email from the last twenty four
hours. Look at my calendar for today. Pull my open tasks. Then write me a short briefing with
three sections.

[SHOW: connect the tools, Gmail, Google Calendar, ClickUp, toggling each on.]

Now it needs permission to actually do that. So I connect three tools. My email. My calendar.
My tasks. That is the MCP part, I am just plugging in the apps I already use.

[SHOW: run it live. The briefing writes itself in real time, line by line. Push-in.]

And now I run it. Watch. It is reading the inbox. It is checking the calendar. And there is the
briefing, writing itself.

[NOTE: let this play. Real-time generation is the money shot, do not cut away.]

So that is agent one. It is honestly maybe fifteen lines. And here is the good part, you can
put it on a schedule so it runs before you wake up. Mine runs at six. [NOTE: chip "runs on a
schedule".]

Now, one honest thing. [open loop nod] The schedule runs on a clock, not on events. It cannot
watch your inbox and fire the second something lands. It runs at the time you pick. For a
morning briefing that is perfect. Just know the limit.

---

## 12:00 - 19:00 AGENT 2 - THE INBOX TRIAGE AGENT (and the leash)

[SHOW: new file. Type the triage rules.]

Agent two is the inbox one, and this is the agent I mentioned at the start, the one I keep on a
leash.

So the instructions are simple. Go through every email from the last day. Put each one in a
bucket. Action, waiting, information, or promotional. And for anything in the action bucket,
draft a reply.

[SHOW: run it. Labels sweep onto the inbox. Then open the drafts folder, real drafts sitting
there.]

Watch it sort. Action. Waiting. FYI. Promo. And now look, it wrote actual replies. They are
sitting in my drafts.

[NOTE: this closes the 0:32 open loop. Land it clearly.]

And here is why I keep this one on a leash. It drafts, it does not send. That is partly the
tool, the email connector is draft only on purpose, and partly me. I have been an engineer long
enough to know you do not let an agent hit send on your real email unsupervised.

So every morning I open my drafts, I read them, and I send the good ones. It saved me the blank
page, not the judgment. That is the right split.

[SHOW: read one draft out loud, edit one word, hit send manually.]

For me that is the rule for anything that talks to the outside world. Let the agent do the
work. You keep the send button. [NOTE: kinetic caption, "agent does the work, you keep send".]

[SHOW: scroll back to a borderline email the agent got wrong. Point right at it.]

And here, let me show you where it breaks, because I promised you that at the start. Look at this
one. It filed this in Promo. But it is not promo, it is a real person who just happens to email
from a newsletter-looking address. It got it wrong.

[NOTE: THIS is the featured-failure beat, the trust moment nobody else shows. Real miss, on screen,
not dramatized. This closes the "where it breaks" open loop from the roadmap card.]

So hear this part. It is not perfect. It gets maybe eighty, ninety percent of my inbox right, and
every so often it misfiles one exactly like this. That is the whole reason it drafts instead of
sends, and the whole reason I glance at it every morning. The agent does the boring sorting. I keep
the judgment. Anybody telling you it runs your life at a hundred percent is selling you something.

---

## 19:00 - 25:00 AGENT 3 - THE CONTENT PIPELINE AGENT

[SHOW: the content repo, status.md and a ClickUp board side by side.]

Agent three does the job I hated most, the admin around my content.

So when a video goes out, a bunch of boring things have to happen. My status file has to
update. The matching task has to move. And I have to write the posts for the other platforms.

[SHOW: run it. status.md edits itself, the ClickUp task moves stage, social drafts appear.]

So I told an agent to do all three. Watch. It updates the status file. It moves the ClickUp
task to the right stage. And it drafts the social posts in my own voice, because it has a file
that describes how I write.

[NOTE: chip "it reads your voice guide". This is a nice reveal, the agent uses a style file.]

That voice file is just another text file. It is how I keep everything sounding like me instead
of like a robot. So the drafts come out in my words, and I just tweak them.

This is the one that gives me back the most time. Not because any single step is hard, but
because it was ten little steps I did not want to do.

---

## 25:00 - 29:00 AGENT 4 - THE CALENDAR AGENT + THE SUBAGENT PATTERN

[SHOW: ask it to schedule the next recording. It checks the calendar, finds a slot, books it.]

Agent four is the smallest one and I use it constantly. Scheduling.

So I just say, find me a two hour block this week and put my next recording on the calendar.
It looks at what is free, picks a slot, and books it. In the right timezone, without the back
and forth.

[SHOW: the event appears on the calendar.]

That is it. Small, but it removes a tiny decision I make every day.

[SHOW: kick off a research subagent in the background, keep working in the main window.]

And here is one more idea that levels this whole thing up. Subagents.

So instead of one agent doing everything, I can send a helper off to do a job on its own. Watch,
I send one to go research a topic. It goes off in the background, does the whole thing in its
own window, and hands me back just the report. Meanwhile I keep working.

[NOTE: show both windows, the subagent churning while the main one is free.]

That is the pattern that turns one assistant into a team. Each one has a narrow job, and they
do not get in each other's way.

---

## 29:00 - 32:00 HONEST LIMITS (the trust beat)

[SHOW: talking head, PIP off, direct to camera. Slower pace.]

So let me be straight with you about where this breaks, because nobody selling you this will.

[SHOW: chips build as he names each.]

One. It is not a hundred percent. It gets you eighty, ninety percent there, and you nudge it.
Never expect perfect.

Two. The schedules run on a clock, not on events. It cannot react the instant something
happens, at least not cleanly, yet.

Three. Anything that sends, emails, messages, posts, keep it draft only and keep your hand on
it. That is not the tool being weak, that is you being smart.

So this is not "walk away and it runs your life." It is "the boring ninety percent is done, and
you spend your time on the ten percent that actually needs you." For me that is the whole win.

---

## 32:00 - END - RECAP + CTA

[SHOW: all four agent files on screen as a grid, then the morning results again.]

So that is the setup. Four agents. A briefing that writes itself. An inbox that sorts itself.
A content pipeline that runs itself. And a calendar that books itself. Plus subagents when you
want a team instead of one worker.

And every single one is just a text file plus the apps you already own.

[NOTE: CTA folded in, then snap back. No dead-air "smash like."]

I put all four of these files in a folder you can copy. It is in the free community, link in
the description, grab it and change the names to your accounts. That is genuinely all it takes.

[SHOW: back to the briefing doc one last time.]

So pick the most annoying part of your day, the thing you do every morning without thinking,
and make that your first agent. Start with one. It takes about ten minutes.

Tell me in the comments what you would hand off first. I read every one.

[END]
