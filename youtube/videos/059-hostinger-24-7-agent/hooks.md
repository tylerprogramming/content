# Hooks, video 059

Three word-for-word 30-second opens. Each is a different technique. Brain rule (08-19): a working artifact already on screen is the strongest cold open in the pool, and the first sentence carries a number. All three obey that. Hook 1 is recommended because it is the proof beat the whole video is built to earn, shown first.

The counts in the hooks (number of runs, timestamps) are placeholders until the proof cut is filmed. Say the real number on camera. Never round up.

## Hook 1: artifact on screen, filmed the next morning (RECOMMENDED)

Technique: working artifact first, number in sentence one, withheld payoff.

[SHOW: phone in hand, Slack open on #content, a thread of timestamped posts from the agent. Laptop visibly closed on the desk behind it.]

> So this ran [N] times last night. Midnight, four, eight. My laptop was closed the whole time. I was asleep for all of these.
>
> [SHOW: scroll the thread. Each post is a short summary with a link to a file.]
>
> Every one of those is a real job. It searched YouTube, wrote a file into my repo, committed it, and posted the summary here. And the agent doing it is not on this Mac. It is on a server that costs less than a coffee a week.
>
> [SHOW: cut to the desktop app, the sidebar showing the VPS connection, same sessions.]
>
> If you watched the last video, you have Hermes Agent running on your machine right now. And it stops the second your laptop sleeps. So today we fix that. We are going to put it on a server, give it one real job, walk away, and come back tomorrow morning to see what it did.
>
> There is one thing in here nobody else shows, and I am holding it for the end. Let's go.

[NOTE: "nobody else shows" is the next-morning cut with the desktop app connecting to the VPS. That is the withheld payoff; do not spoil it in the first minute.]

## Hook 2: contrast, the 057 viewer's problem

Technique: contrast (what you have vs what you need), named villain is the sleeping laptop.

[SHOW: the Mac. Hermes desktop app open. Close the lid. Cut to the phone: nothing arrives.]

> So here is the thing about the setup from the last video. You have got an agent with memory, with cron jobs, with Slack. And it lives on a laptop. Close the lid, it is gone. The 8am job does not fire. The Slack message does not land.
>
> [SHOW: Hostinger dashboard, the Hermes Agent template, then the phone with a Slack thread of timestamped runs.]
>
> This is the same agent on a server. Six dollars a month. It ran [N] times last night while I slept, and every run left a file in my repo.
>
> In about twenty minutes we are going to deploy it, move your Claude Code setup onto it with one command, give it one job, and then I am going to close this laptop and come back tomorrow. That part, the coming back, is the part every other Hostinger video skips. Let's do it.

## Hook 3: bold claim, the one-command import

Technique: bold claim, then immediately prove a piece of it.

[SHOW: terminal on the VPS via the web console. Type the command as you say it.]

> So every video about Hermes on a server ends the same way. You send it a message, it answers, roll credits. Nobody shows you the next day.
>
> This one ends tomorrow morning. And it starts with a command I have not seen in a single one of those videos.
>
> [SHOW: `hermes import-agent claude-code --dry-run`, the preview scrolling: CLAUDE.md, MCP servers, skills.]
>
> That is my whole Claude Code setup, [N] items, moving onto a six dollar server in one line. Skills, rules, MCP servers. The agent on the server starts with everything the one on my Mac knows.
>
> Then we give it one job, put it on a schedule, and I close the laptop. Twenty minutes to set up. Twenty-four hours to prove it. Let's go.

[NOTE: the item count on the Mac was 55 on 09-16 (CLAUDE.md, 2 MCP servers, 52 skills). On the VPS the source is whatever gets copied there, so the number will differ. Say the number the screen shows.]

## Which one

| Hook | Strength | Risk |
|---|---|---|
| 1 | Artifact on screen in 3 seconds, open loop held to the end | Needs the proof cut filmed first, so it is recorded last |
| 2 | Cleanest tie to 057's audience, villain named in sentence two | Slower to the artifact (about 12 seconds) |
| 3 | The one thing no competitor shows, in the first 20 seconds | Spends the import beat early; section 5 has less to reveal |

Record 1. Keep 2 as the fallback if the overnight run fails and there is nothing to show on the phone.
