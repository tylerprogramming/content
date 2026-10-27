# Script, video 062: I Tested ChatGPT Dots vs Hermes Agent on the Same 3 Jobs

**Target runtime:** 13 to 14 minutes. Ceiling 15. If long, cut beat 7 (the two PRs) to a 30-second "both opened a PR, here they are" and keep beat 8.
**Version:** v1, 2026-10-24.
**Rule for every beat:** Tyler does it on screen or says it to camera. Nothing animated, nothing simulated. If a Dot output has personal data in it, show the real screen with the lines blurred and say why, like Riley Brown did with his brief. Never mock one up.
**Pre-built:** every output in this script already exists before the camera rolls (filming-guide PRE-BUILD). Live beats are the ones where the action itself is the point: creating the schedule (4), the rule firing (6), the memory file (9).

Voice: Tyler's. "So" openers, short sentences, hedge instead of hype, no em dashes.

## Facts the script leans on (from analysis.md, all sourced)

| Claim | Source |
|---|---|
| First dot included on Pro ($100 / $200 / $500) and Business Premium; not Plus; Pro users 18+ outside EEA/UK/CH | OpenAI help 20001530, 9793128 |
| Dot chats do not count toward ChatGPT limits; Work and Codex tasks do | OpenAI intro post, help 20001530 |
| Custom Rule labels: Take action without asking / Take action when you say so / Ask before taking action / Hand off to you | learn.chatgpt.com/docs/dots/controls |
| Auto-review is separate from Custom Rules and cannot be turned off by either | OpenAI safety post, controls doc |
| Proactive research is read-only, enforced in code | OpenAI safety post |
| Activity View: desktop app only, In progress / Scheduled / Completed | controls doc |
| You cannot view or edit individual dot memories; reset deletes the dot | help 20001529, 20001530 |
| Event-triggered tasks watch Gmail, Slack, GitHub; Slack needs @ChatGPT in the channel | help 10291617 |
| Researcher cron: 25 runs (24 completed, 1 failed), `45 7 * * 1-5` | `~/.hermes/profiles/researcher/cron/jobs.json` |
| Coder cron: 31 runs (29 completed, 2 failed), `0 8 * * 1-5` | `~/.hermes/profiles/coder/cron/jobs.json` |
| Repo Health cron: 42 runs (33 completed, 7 failed, 2 unknown), `0 9 * * *` | `~/.hermes/cron/jobs.json` |
| Researcher hard rule: "Never publish, post, or schedule anything" | `~/.hermes/profiles/researcher/SOUL.md:18` |

Marked *to verify* = the Dot side of it has not been run on Tyler's account yet. The PRE-BUILD resolves each one before filming.

## Beat table

Mirrors the researcher's creator breakdown. "Creator does" is Riley Brown (RB) or Paul Lipsky (PL) at the timestamp in their transcript. "You do" is Tyler's swap. Paths are absolute; `hermes -p <profile>` runs a command against that bot's home.

| # | Creator does (time) | You do | Your exact prompt / click |
|---|---|---|---|
| 1 | RB 00:00 to 00:46: "7 days with Dot," claims a 40 min walk clears his inbox | **0:00 to 0:40.** Open on the two Slack DMs, Dot and Researcher, both 7:45. Then camera: three jobs, same week, receipts. | No prompt. Slack, scroll to the two messages from this morning. (Hook A in hooks.md.) |
| 2 | PL 00:31 to 01:32: reads OpenAI's claims, "on paper nothing new" | **0:40 to 1:40.** 60 seconds of what a Dot is, from OpenAI's page on screen, not a graphic. Own cloud computer, GPT-6 Astra, plugins, read-only background research, first dot in Pro. One sentence on the Hermes side: 10 profiles on this Mac, 8 crons. | Browser: `https://openai.com/index/introducing-dots/`. Terminal: `hermes profile list` |
| 3 | RB 00:57 to 02:33: opens the dot's computer, shows Blender installed on it | **1:40 to 3:10.** Open the Dot's profile > Computers > its computer > Take over. Move the mouse. Return control. Then Profile > Activity, read the three columns. Then the Hermes side: the log file and the kanban card that built this video. | Dot (type in chat): `What are you working on right now, and what needs my input?` Terminal: `tail -40 /Users/tylerreed/.hermes/profiles/researcher/logs/agent.log` then `hermes kanban show t_ab09f580` |
| 4 | RB 19:12 to 21:09: creates a noon automation by voice, hides his 9am brief | **3:10 to 4:40.** Open Scheduled, show the content brief task that already ran this morning, open it, edit the time by a minute and back (new since Oct 13). Then the Hermes twin: the cron that has run 25 times, and its last run. Show the brief itself; it is a content brief, nothing to hide. | Dot: open Profile > Activity > Scheduled > "Morning content brief". Terminal: `hermes -p researcher cron list`, then the executions count query from filming-guide.md step 4 (`cron list` prints no run count), then `hermes -p researcher cron runs bff2da40e427 --limit 5` |
| 5 | RB 02:38 to 03:58: voice call, dot reads his Slack, sends a team message | **4:40 to 5:50.** Ask the Dot in text to read the bots channel and summarize what Researcher handed Packager this week. No voice. Point at the answer, then at the actual thread, which the bots wrote on their own. *to verify: Dot's Slack app can read that channel; @ChatGPT must be in it* | Dot: `Read the #bots channel in my Slack from the last 48 hours. Tell me what Researcher handed to Packager, and whether Packager finished. Do not reply in the channel.` Slack: open #bots, scroll to the handoff. |
| 6 | Skill Leap 08:21: types three custom rules, dot "asked for my okay," nothing blocked on screen | **5:50 to 7:40.** The beat nobody has. Open Settings > Personalization > Custom rules, show the rule set up in PRE-BUILD: "create, merge, or comment on GitHub pull requests and issues" = Hand off to you. Open the 9 AM repo digest the Dot sent. Pick one item. Tell it to open the issue. Film what the rule does. Then the Hermes side: Researcher's SOUL line 18, and Coder's prompt that says read-only. *to verify: what the hand-off looks like on screen* | Dot: `Go ahead and open that issue on the repo.` Terminal: `sed -n '15,19p' /Users/tylerreed/.hermes/profiles/researcher/SOUL.md` |
| 7 | RB 05:08 to 09:46: voice-spawned Codex session ships a feature, never opens the diff | **7:40 to 9:10.** Two PRs, same change, one from each side, both opened in PRE-BUILD and both stopped before merge. Open each PR's Files tab. Read the diff out loud. Say which one you would merge and why. Neither is merged on camera. | Browser: `https://github.com/tylerprogramming/content/pulls`. The two PR numbers go in the filming guide once they exist. |
| 8 | PL 02:26 to 04:02: two unprompted finds, both blurred screenshots, no times | **9:10 to 10:40.** The receipts table on screen as a markdown file in the editor. Three jobs, two agents, time sent, time delivered, what came back, what each got wrong. Filled in from this morning's Slack timestamps. Read it row by row. Include the Skool draft (job 3) here as a result, not a demo. | Editor: `/Users/tylerreed/content/youtube/videos/062-openai-dots/receipts.md` (written in PRE-BUILD item 9). Slack: hover each message for the timestamp. |
| 9 | Build Alone 02:38 and Nate Herk 03:40: complain you cannot edit the dot's memory | **10:40 to 11:40.** Open the Dot's memory screen, show what the help center says you can and cannot do. Then open Researcher's memory file in a text editor, change one line, save. That is the whole beat. | Dot: Profile > Memory. Terminal: `open -e /Users/tylerreed/.hermes/profiles/researcher/memories/MEMORY.md` |
| 10 | PL 10:51 to 11:39: plan, "starts at $100," region | **11:40 to 12:40.** Price in one sentence from the page. Which Pro tier you are on (Tyler says it; not in any file). Then the Hermes number, read off the machine, not estimated. | Browser: `https://learn.chatgpt.com/docs/pricing`. Terminal: the per-profile insights loop in filming-guide.md step 10 (`hermes insights` is per profile; there is no all-profiles flag) |
| 11 | RB 24:47 to 25:55: recap, "it will get better" | **12:40 to 13:30.** No recap. One line on what only the Dot can do (voice from a walk, wakes itself up) and what only the bots can do (talk to each other, memory in a file, run on a local model). Then the question. | Camera. End card: 057 on the left. |

---

## Beat 1 [0:00 to 0:40] Two messages, same minute

[SHOW: Slack. The Dot's DM at 7:45 on top, Researcher's DM at 7:45 below it. Both are a content brief. No camera.]

Two messages. Same morning, same minute, same job.

The top one is from my Dot. That is OpenAI's always-on agent. I paid for it on Saturday.

The bottom one is from Researcher. That is a Hermes bot that has been running on this Mac for about five weeks. [Read the completed count off the executions query in PRE-BUILD 14 on filming day; it was 24 completed plus 1 failed on Oct 24.] mornings so far.

[SHOW: camera]

So I gave the Dot the three jobs my bots already do. A morning brief, a repo check, and prepping a Skool post when a video goes live. Same prompts, same accounts, same week. And I kept the receipts, because every video I found on Dots ends when the Dot says "I'll get started on that," and I wanted to see what actually came back.

[NOTE: if the real timestamps are not the same minute, say the real ones. See hooks.md note.]

---

## Beat 2 [0:40 to 1:40] What a Dot is, from the page

[SHOW: browser, openai.com/index/introducing-dots/, scroll slowly]

So quick version, because a lot of people have covered this part.

A Dot is an agent that lives in ChatGPT. It has its own computer in OpenAI's cloud, its own browser, and it runs on GPT-6 Astra. It connects to your apps through the same plugins ChatGPT and Codex already use. OpenAI says over four thousand of them. Their number, not mine.

Two things from the page that matter for this video. One, when you are not around it can do research on its own, but that research is read-only. It cannot send anything. Two, you get one Dot, and it is included if you are on Pro or Business Premium. Not Plus. And not in the EU or the UK right now.

[SHOW: terminal, `hermes profile list`]

And on the other side, this is what I already have. Ten profiles on this Mac. Each one is a bot with its own model, its own memory, its own rules. Five of them have scheduled jobs, eight jobs total. [Counts as of Oct 24 from the jobs.json files; re-read on filming day per PRE-BUILD item 14.] The ones you will see in this video talk in Slack.

[SHOW: camera]

So that is the setup. Let's open the Dot up first.

---

## Beat 3 [1:40 to 3:10] What you can see

[SHOW: ChatGPT desktop app. Click the Dot's profile. Computers. Click its computer.]

So this is the thing nobody clicks on. This is the Dot's computer. It is a real machine in OpenAI's cloud, and I can take it over.

[SHOW: click Take over. Move the mouse around. Open whatever is on screen.]

That is me moving the mouse on a computer I do not own. If the Dot gets stuck on a login or a captcha, this is where you help it. Return control.

[SHOW: click Return control. Then Profile > Activity.]

And this is Activity. Three columns. In progress, Scheduled, Completed. Everything the Dot has done or is going to do. This is desktop only, by the way, you cannot see this on your phone.

[SHOW: type in the Dot's chat]

```
What are you working on right now, and what needs my input?
```

[SHOW: the answer. Point at anything that lines up with the Activity columns.]

So that is the Dot's version of "what have you been doing."

[SHOW: terminal]

```
tail -40 /Users/tylerreed/.hermes/profiles/researcher/logs/agent.log
```

Here is the same thing for Researcher. It is a log file. Every tool call, every message, with a timestamp. Kind of ugly. But I can grep it.

```
hermes kanban show t_ab09f580
```

And this is the card that built this video. Researcher wrote the research, handed it to Packager, Packager wrote the script I am reading right now. That handoff is a row in a SQLite file. I can read it.

[SHOW: camera]

So that is the first real difference, I think. The Dot shows you a view. The bots show you a file. We'll come back to that.

---

## Beat 4 [3:10 to 4:40] Job 1: the morning brief

[SHOW: Dot > Activity > Scheduled. Click "Morning content brief".]

Okay, job one. Every weekday at 7:45 I want a short brief: what's filming next, yesterday's channel numbers, three video ideas. This is the Dot's version. I set it up Monday, and this is the prompt, word for word.

[SHOW: the task's instructions panel. Read the first line out loud.]

Since the October 13th update you can open these and edit them, which you could not do at launch.

[SHOW: change the time to 7:46, then back to 7:45. Save.]

[SHOW: the Dot's DM from this morning, full screen. If anything personal is in it, blur the line and say so.]

And this is what it sent this morning. [Say what the real brief got right and what it got wrong. Check it against `youtube/notes/status.md` before filming: did it name the right next video? Are the three openings specific to the channel or generic? Say the honest version. Never mock one up.]

[SHOW: terminal]

```
hermes -p researcher cron list
```

Here is the same job on the Hermes side. `45 7 * * 1-5`, that is 7:45 weekdays. And the number I care about is this one.

```
sqlite3 ~/.hermes/profiles/researcher/cron/executions.db "select status,count(*) from executions where job_id='bff2da40e427' group by status"
```

[SHOW: point at the completed row of the query output. On Oct 24 it read completed 24, failed 1. `cron list` prints no run count, so do not point at it.]

```
hermes -p researcher cron runs bff2da40e427 --limit 5
```

[Read the completed count off the query.] completed runs, and it also tells me the one that failed. The last five are right there with their status. One of them failed to deliver last week, and it told me. I'll show you what that looks like in a second.

[SHOW: Researcher's DM from this morning]

And this is this morning's brief from Researcher. Same shape. Three openings, reply with a number. And when I reply with a number, it goes and does the research. That part the Dot does not have yet, because the Dot is one agent and this is three.

[SHOW: camera]

So on job one, honestly, they are close. The Dot's brief reads a little nicer. The Hermes one is wired into the next step.

---

## Beat 5 [4:40 to 5:50] Can the Dot read what the bots said

[SHOW: Dot chat. Type.]

```
Read the #bots channel in my Slack from the last 48 hours. Tell me what Researcher handed to Packager, and whether Packager finished. Do not reply in the channel.
```

So here is a fun one. My bots talk to each other in Slack. Researcher finishes a job and pings Packager. I wanted to see if the Dot could read that thread and tell me what happened.

[SHOW: the Dot's answer. Wait for it. Dead air is fine, cut it in the edit.]

[NOTE: *to verify.* If the Dot cannot read the channel, say so on camera and show the error. That is a real result. PRE-BUILD item 5 checks this before filming so you know which version you are filming.]

[SHOW: Slack, #bots, scroll to the actual handoff from this week]

And this is the thread it was reading. Researcher wrote this. Packager wrote this. I did not type any of it.

[SHOW: camera]

So the Dot can sit on top of the bots and summarize them. Which is kind of a weird sentence. But it is one of the more useful things I found.

---

## Beat 6 [5:50 to 7:40] Job 2: the repo check, and the rule that stops it

[SHOW: ChatGPT Settings > Personalization > Custom rules. The rule is already there.]

Job two. Every morning at nine, check my GitHub repos. Failing checks, stale issues, Dependabot. Send me five things max.

But before I turned that on, I set this rule. Action: create, merge, or comment on GitHub pull requests and issues. Behavior: Hand off to you. There are four levels, and this is the strictest one. It does not ask me. It just stops and hands me the task.

[SHOW: the Dot's 9 AM repo digest in Slack from this morning]

Here is this morning's digest. [Say what the real digest contained: how many items, whether each had a link, and whether it stayed read-only like the prompt asked. If it did something you did not ask for, that is the more interesting line; say it.]

[SHOW: Dot chat. Pick one item from the digest. Type.]

```
Go ahead and open that issue on the repo.
```

Now watch what happens when I ask it to cross the line.

[SHOW: whatever the Dot does. Hold on it.]

[NOTE: *to verify.* This is the beat nobody has filmed. PRE-BUILD item 4 runs it once off camera so you know what the hand-off looks like. On camera, do it again and narrate what is on screen, not what the docs say should be. If Auto-review fires instead of the Custom Rule, say that; it is a separate system and the docs say it cannot be turned off.]

So that is a guardrail. Not a diagram of one. It stopped, it told me why, and the issue did not get created.

[SHOW: terminal]

```
sed -n '15,19p' /Users/tylerreed/.hermes/profiles/researcher/SOUL.md
```

Here is the same idea on the Hermes side. Line 18. "Never publish, post, or schedule anything. You research and draft; Tyler publishes." That is a sentence in a markdown file. The bot reads it every time it wakes up.

[SHOW: camera]

Now, the honest difference. The Dot's rule is enforced by OpenAI, and there is a second system called Auto-review behind it that I cannot turn off. My rule is enforced by the model reading a file. It has held for five weeks. But it is a different kind of promise, and I think you should know which one you are buying.

---

## Beat 7 [7:40 to 9:10] Two PRs, same change

[SHOW: browser, github.com/tylerprogramming/content/pulls. Two open PRs.]

So both sides can write code. The Dot hands coding to Codex. My side has a bot called Coder. I gave both of them the same small change: add a line to the index file pointing at this week's research. Open a PR, do not merge.

[SHOW: click the Dot's PR. Files changed tab. Read the diff.]

This is the Dot's. [Read what it did. Note anything extra it touched.]

[SHOW: click Coder's PR. Files changed tab. Read the diff.]

This is Coder's. [Same.]

[NOTE: PR numbers go in the filming guide once PRE-BUILD items 7 and 8 produce them. Do not merge either on camera. If one of them did not produce a PR, show that instead; it is a result.]

[SHOW: camera]

I'd merge [whichever]. [One sentence why.] And the thing Riley Brown's video skipped is this tab. He trusted "all tests passed." I would rather read eleven lines.

---

## Beat 8 [9:10 to 10:40] The receipts

[SHOW: editor, `/Users/tylerreed/content/youtube/videos/062-openai-dots/receipts.md`, full screen]

Okay. This is the table I wanted when I watched the other videos. Three jobs, two agents, what time I asked, what time it came back, what came back, and what each one got wrong.

[NOTE: read it row by row. Every cell is filled from a real timestamp in Slack or a real file. PRE-BUILD item 9. The template is in the filming guide. Do not estimate a time. If a cell is "did not run," say "did not run."]

[SHOW: for job 3, open the Dot's draft page and the Skool Librarian's lesson draft side by side for ten seconds]

Job three is the Skool one. New video goes live, draft the lesson and the post. The Dot put its draft in a page. The Librarian bot put its draft in the course and blocked itself until I approve. Neither one posted. That was the rule on both sides.

[SHOW: camera]

So on the table. [Say the honest read: what the Dot was better at, what the bots were better at, what both got wrong.]

---

## Beat 9 [10:40 to 11:40] Memory you can open

[SHOW: Dot > Profile > Memory]

Two of the videos I watched complained about this screen. This is what the Dot remembers about me. I can see that it has memories. The help center says I cannot view or edit individual ones. If I want a clean slate, I reset the Dot, and that deletes everything. Conversations, scheduled tasks, all of it.

[SHOW: terminal]

```
open -e /Users/tylerreed/.hermes/profiles/researcher/memories/MEMORY.md
```

[SHOW: TextEdit opens. Two lines. Change one word. Save.]

This is Researcher's memory. Two lines. I just changed one. Saved. That is the whole beat.

[SHOW: camera]

I am not saying one is right. The Dot's way is safer if you do not want to think about it. My way is better if you do. But nobody showed you both, so there they are.

---

## Beat 10 [11:40 to 12:40] What each one costs

[SHOW: browser, learn.chatgpt.com/docs/pricing]

So price. The first Dot is included on Pro, which starts at a hundred a month, and on Business Premium. It is not on Plus. I am on [Tyler says the tier]. Talking to the Dot does not count against my ChatGPT limits. Work it kicks off in Codex does.

[SHOW: terminal]

```
for p in default coder coder-reviewer inbox-triage opus packager researcher skool-librarian sol workshop; do echo "== $p"; hermes -p $p insights --days 7 | grep Estimated; done
```

And this is the Hermes side for the last seven days, read off the machine. Insights is per profile, so this loops over all ten and prints one line each. [Read two or three of the lines, then say the sum you wrote in receipts.md.] That is ten profiles, eight scheduled jobs, plus whatever I did by hand. The software is free. The model is what you pay for, and I can point any of these bots at a local model and make that number zero for that bot.

[SHOW: camera]

So the comparison is kind of: one subscription that covers one agent, or a bill that scales with how many agents you run and which model each one uses.

---

## Beat 11 [12:40 to 13:30] Which jobs would you hand over

[SHOW: camera]

So here is where I landed, and it is not a winner.

Things only the Dot can do right now: I can call it from a walk. It wakes itself up and looks at my stuff without a schedule. It has a browser that is not my browser.

Things only the bots can do: they talk to each other. Researcher hands to Packager hands to Coder, and that handoff is a file I can read. Their memory is a file I can edit. And any one of them can run on a model on this Mac for nothing.

The whole point of all this is you probably do not pick one. The Dot is good at the jobs where you want OpenAI to hold the guardrail. The bots are good at the jobs where you want to hold it yourself.

So tell me in the comments: of the three jobs, which one would you hand to the Dot, and which one would you keep on your own machine. I read every one.

[SHOW: end card. 057 (Set Up Hermes Agent) on the left, this video's Skool link on the right.]

If you want the bot side set up, the thirty-minute version is right there.

[NOTE: end on the question, not a recap. No "like and subscribe" line; the end card does it.]
