# 063 script: I Gave Claude Duet 3 Real Jobs

Duet only. No Hermes on screen. About 12 minutes.
Version 1, 2026-10-27. Built from `research/2026-10-26-claude-duet.md` and the Peter Yang / Riley Brown breakdown. Same shape as the 062 script you filmed from.

Lines in [brackets] are notes for you. Lines in quotes are what you say. Say what is actually on screen, even when it differs from these lines. Never read Duet's output off this page; it is not here on purpose.

## Before you roll

| Window | What's open |
|---|---|
| A | Browser tab 1: Claude Duet on the web, main thread, Chat tab |
| B | Browser tab 2: YouTube Studio > Content, sorted by date, views column visible |
| C | Browser tab 3: `https://github.com/tylerprogramming` (repositories, sorted by stars) |
| D | Browser tab 4: `https://claude.com/resources/articles/claude-duet` (launch post) |
| E | Slack, your own DM (or Gmail, if the approval beat runs on email; see filming-guide PRE-BUILD 6) |
| F | Editor: `transcripts/transcript_<id>.txt` for the Skool deck's video, plus `receipts.md` in this folder |
| G | Phone, Duet app, logged in, screen record ready (beat 9 only) |

Do Not Disturb on. Slack and Duet notifications off on the Mac. Duet notifications ON on the phone (beat 9 needs one).

## Beat table

| # | Creator does (time) | You do | Your exact prompt / click |
|---|---|---|---|
| 1 | Peter Yang 0:00 to 0:45: promise list of 4 artifacts; Riley Brown 0:00 to 0:25: "10 hours, 9 things" | **0:00 to 0:35.** Open on Channel Pulse in the Make tab, refreshed this morning on its own. Timestamp visible. Then the three jobs. | Window A, Make tab > Channel Pulse. Then camera |
| 2 | Peter Yang 0:48 to 1:49: onboarding, "already connected" | **0:35 to 1:35.** What Duet is, for someone who already uses Claude Code. What carried over, what did not. | Window D, scroll. Then Window A, Duet's connections view |
| 3 | Riley Brown 10:27 to 11:10: pastes one long prompt, task spins up | **1:35 to 2:15.** Paste Job 2 (Repo Health) live. Open the task thread. Show its step list and the "working" state. Leave it running. | Prompt R below. Then Tasks tab > Active > Repo Health |
| 4 | Peter Yang 9:03 to 10:14: YouTube report, judged by reading 2 insights | **2:15 to 4:00. Job 1, Channel Pulse.** Put YouTube Studio next to the dashboard. Count the rows that match. | Window A left, Window B right |
| 5 | Peter Yang 4:46 to 5:42: scheduled check-in, "view history" | **4:00 to 4:45.** Tasks > Scheduled > the Channel Pulse refresh > its history. The 6:30 run from this morning. | Tasks tab > Scheduled > Channel Pulse refresh |
| 6 | Brock 4:51 to 6:11: Supabase dashboard, "looks really solid" | **4:45 to 6:00. Job 2, the sheet.** Back to Repo Health, now ready for review. Three spot checks against GitHub. | Window A, Make tab > Repo Health. Window C |
| 7 | Riley Brown 20:56 to 21:34: approvals described, never shown | **6:00 to 7:00.** Ask it to send you the top 3 rows. Hold on the approval card. Read what it shows. Approve. Show it land. | Prompt S below. Then the card. Then Window E |
| 8 | Riley Brown 10:27 to 13:29: one-shot deck, "this is nice" | **7:00 to 8:30. Job 3, the Skool deck.** Open the deck. Put the transcript next to it. Count the prompts it quoted right. | Window A, Make tab > the deck. Window F |
| 9 | Riley Brown 6:52 to 9:00: voice edit from a phone | **8:30 to 9:15.** One voice edit from the phone. Then the slide changes on the web. | Window G, voice message V below. Then Window A |
| 10 | John Aspinall 6:14 to 6:42: "one shared pool", hard to see | **9:15 to 9:45.** Usage before and after the deck. One number. | Window A, claude.ai Settings > Usage (label to verify) |
| 11 | Peter Yang reads, never checks; nobody shows times | **9:45 to 10:45.** Receipts table. | Window F, `receipts.md` |
| 12 | Peter Yang 12:08 to 13:54: Uber failure; 13:54 ranking | **10:45 to 12:00.** What did not work. One line on Dots. The question. | Camera |

### Prompts (paste as written)

Prompt R, Job 2, Repo Health (pasted live in beat 3):

```
Make a spreadsheet called Repo Health. One row for every public repository under github.com/tylerprogramming. Columns: repo, stars, stars gained last 30 days, open issues, open PRs, age of oldest open PR in days, last commit date, checks on main (pass/fail/none), and "video candidate" with a one-line reason using the numbers. Sort by stars gained. Put it in Make and message me when it is ready. Do not open, close, comment on, or merge anything.
```

Prompt S, the send (beat 7; use the Slack line or the email line, whichever PRE-BUILD 6 proved works):

```
Send me the top 3 rows of Repo Health as a Slack DM, with the repo name, stars gained, and the video candidate reason for each.
```

```
Email me the top 3 rows of Repo Health at [your address], with the repo name, stars gained, and the video candidate reason for each.
```

Voice message V (beat 9, spoken into the phone, do not read it like a script):

```
Hey, on the Skool deck, move each prompt onto its own slide so there's one prompt per slide, and cut the mistakes slide down to three bullets. Keep everything else.
```

Job 1 and Job 3 prompts ran before filming. They are in `filming-guide.md` PRE-BUILD 3 and 5.

---

## 1. Hook (0:00 to 0:35)

[Screen: Window A, Make tab, Channel Pulse open. Scroll to wherever the refresh time or "last updated" shows. No camera yet. If the refresh did not fire this morning, do not say it did; see filming-guide PRE-BUILD 3 for the fallback open.]

"So this rebuilt itself at six thirty this morning. [Only if true: I was asleep.] I didn't open Claude. It's a dashboard for my channel and Claude Duet made it, and then it made it again on its own."

[Camera]

"So I gave Claude Duet three real jobs. A dashboard for my YouTube channel, a spreadsheet across my GitHub repos, and the lesson deck for my Skool community. All on my real stuff. And every Duet video I watched this week ends with the creator reading the output out loud and saying 'nice.' I wanted to put the output next to the source and count what it got right. So let's do that."

## 2. What Duet is, if you already use Claude (0:35 to 1:35)

[Window D, scroll slowly]

"So quick version. Claude Duet is a separate app from Anthropic. Research preview, waitlist, US only, Pro and Max. It runs on its own computer in Anthropic's cloud, so it keeps working when you close the app. It has its own browser for sites that don't have a connector. And before it sends a message, pays for anything, signs, or deletes, it's supposed to stop and show you. We're going to make it do that."

[Window A. Open Duet's connections view. Point at GitHub and Slack. Say the real label you clicked; the researcher could not confirm it.]

"If you already use Claude, here's what carried over for me. My connectors. My memory. And the Make tab already had my older artifacts in it before I asked for anything."

"What did not carry over. It can't see files on my Mac. It can't see my local Claude Code skills. It can't start a Claude Code session on this machine. So anything from my content repo has to come through GitHub. Keep that in mind, because it's the thing that bit me."

[If the GitHub connector did not reach the private repo in the pre-build, say so here in one line and say what you did instead.]

## 3. Kick off the live one (1:35 to 2:15)

[Window A, Chat tab. Paste Prompt R. Send.]

"So before we judge the two that already ran, I want one running live. This is job two. A spreadsheet. One row per public repo under my GitHub, stars, open PRs, age of the oldest one, checks on main, and a column that says which repo is a video candidate and why."

[Tasks tab > Active > click Repo Health. Show the step list and the state.]

"And this is what I like. It opens a task, and the task has its own thread, and you can see the steps it's planning. It says working. We'll come back to it."

[Dead-air filler if the task takes a second to appear: "Riley Brown's first deck took about ten minutes. So we're not waiting on this one."]

## 4. Job 1: Channel Pulse, checked (2:15 to 4:00)

[Window A, Make tab > Channel Pulse, left half. Window B, YouTube Studio > Content, right half.]

"Job one. I asked for one page I can open every morning. Last ten uploads, views, views per hour since upload, and whether each one beat the median of the twenty before it. Plus what's filming next, from my status file, and three 'where to look' lines with the number behind each."

"This is the dashboard. This is Studio. Same videos. Let's go row by row."

[Go down the last 10 uploads. For each: does the view count match Studio within a day's drift? Say the count as you go. Do not round it up.]

"So [N] of ten rows match. [Which ones were off, and by how much.]"

[Scroll to the "filming next" line.]

"And the filming-next line. [Is it the right video? If it came from status.md, say that. If it guessed from the channel page, say that.]"

[Scroll to the three bullets.]

"[Read one bullet. Is the number behind it real? Is it something you would actually act on, or generic?]"

"[Your verdict, one line. Something like: the numbers I can check are mostly right, the advice is the part I'd push back on. Only if true.]"

## 5. The schedule (4:00 to 4:45)

[Tasks tab > Scheduled. Click the Channel Pulse refresh. Open its history. Say the labels you actually see; Peter Yang's were "Scheduled" and "view history".]

"So this is the part from the hook. I asked for a refresh every weekday at six thirty. It's in here under Scheduled, and this is the history. This morning's run, [the time it shows]."

"Peter Yang said you can schedule a refresh in his video and didn't do it. I wanted to see it in the list and see it fire. [Say if it fired every morning since you set it, or missed one.]"

## 6. Job 2: the sheet, spot checked (4:45 to 6:00)

[Window A, Tasks > Active > Repo Health. If it is ready for review, open it in Make. If not, use the one from the pre-build run and say so.]

"Okay, job two is back. [How long did it take, from the task thread.]"

[Open the sheet. Window C on the right, your GitHub repos sorted by stars.]

"Three spot checks. [Pick the top row: stars right? open PRs right? last commit date right?] [Pick a middle row.] [Pick the stars-gained-in-30-days column anywhere.]"

"[Stars gained in 30 days is not a GitHub API field. The researcher flagged it before I ran it. So if that column is wrong or blank, say that and say it's the column you expected to be wrong. If it's right, say you're surprised and ask it how it got the number.]"

[Click the video candidate column.]

"[Read its top pick and reason. Would you make that video? One line.]"

## 7. The approval card (6:00 to 7:00)

[Window A, Chat. Paste Prompt S, whichever version PRE-BUILD 6 proved. Send.]

"So now the thing nobody filmed. Anthropic says before it sends a message it stops and shows you the action, where it's going, what's in it, and every recipient. Let's see if that's true."

[Hold on whatever comes up. Do not cut. Read the card out loud: what action, what destination, what content, who the recipients are. If it does not match the safety post's description, say what is missing.]

"[What the card actually shows.]"

[Tap Approve.]

[Window E. The message lands.]

"And there it is. [Time stamp.] That's the loop. It built the thing, it asked, I said yes, it sent it. It did not send anything until I said yes."

[If no card appeared and it just sent: say so plainly, on camera. That is the bigger story. If it refused or said the connector could not send: show the message and say "so Slack is read-only here, and that's a result."]

## 8. Job 3: the Skool deck, checked against the transcript (7:00 to 8:30)

[Window A, Make tab > the Skool deck. Window F, the transcript file, on the right.]

"Job three. When I publish a video, I turn it into a lesson for my Skool community. A short deck, the steps, the exact prompts, the links, plus a community post. I gave Duet [which video] and the transcript from my repo and asked for six to eight slides and a hundred-and-twenty-word post. Drafted, not posted."

[Click through the deck. Count slides out loud.]

"[How many slides. Does it have the shape you asked for: what you'll have, three steps with a prompt each, links, mistakes.]"

[Stop on a prompt slide. Find the same prompt in the transcript.]

"So here's the check. This is the prompt on the slide. This is what I actually said in the video. [Match, close, or made up?]"

[Do that for each prompt slide. Say the count: N of M prompts quoted right.]

[Open the community post.]

"[Read two lines of the post. Does it sound like you? What would you cut?]"

"And it didn't post it anywhere, because I told it not to. It's a draft. I post."

## 9. The edit from the phone (8:30 to 9:15)

[Window G, phone screen recording. Open Duet, main thread. Hold the voice button. Say voice message V in your own words.]

"So I'm not at my desk for most of these. Let's fix the deck from the phone."

[Send. Wait for the task to spin up. Cut to Window A on the web.]

"[Did the slides change? Did it do both edits, one, or neither? How long?]"

[Dead-air filler while it works: "John Aspinall's video says there's no voice call on the web version. So the phone is where voice lives. Riley Brown does a whole walk this way."]

## 10. What it cost in usage (9:15 to 9:45)

[Window A, claude.ai Settings > Usage, or wherever your usage meter is. Say the label you clicked.]

"So Duet is included in Pro and Max right now, nothing extra. But it shares your limits. The morning refresh, the background work, all of it counts. I wrote the meter down before the deck and after."

"[Before number. After number. The difference, as a percent of the weekly limit.] So that's what one deck costs me. [Does that worry you for a daily refresh? One line.]"

## 11. Receipts (9:45 to 10:45)

[Window F, `receipts.md`, full screen. Read row by row.]

"So this is the table I wanted when I watched the other videos. Every time is from the task thread. Every count is from putting the output next to the source."

[Read each row: job, when asked, when done, what came back, how many checks it passed, what it got wrong.]

## 12. What didn't work, and the question (10:45 to 12:00)

[Camera]

"So, what didn't work. [Pick the real ones from the pre-build, two or three: the GitHub connector and the private repo, the stars-gained column, the refresh that missed a morning, the approval that didn't look like the docs, the deck prompt it paraphrased. Only ones that actually happened.]"

"And a couple of things to know. There's no model picker. It's Opus 5.5 and it decides how hard to think. You can't watch its browser. And it can't see your local skills, which, if you've built a bunch of them in Claude Code like I have, is the one I'd want first."

"I filmed three jobs on ChatGPT's Dots a few days ago. That comparison is its own video if you want it. Tell me in the comments."

"Where I landed. [Which of the three would you keep running on Duet?] [Which one wouldn't you, and why?] For me the whole point is the dashboard rebuilt itself and I didn't touch it. The judgment on top of the numbers is still mine."

"So tell me. Of these three jobs, which one would you hand to Duet first? I read every one."

[End card]

---

## receipts.md (fill in before you roll, from task threads and the files)

```
# Receipts, video 063

Every time from the Duet task thread (hover or open the task). Every check from putting the artifact next to the source. "Did not run" and "could not check" are valid cells.

| Job | Asked (date, time ET) | Ready (date, time ET) | What came back | Checked against | Right / checked | What it got wrong |
|---|---|---|---|---|---|---|
| 1 Channel Pulse, first build | 10-27 __:__ | __:__ | dashboard in Make | YouTube Studio, last 10 uploads | __ / 10 rows | |
| 1 Channel Pulse, 6:30 refresh | scheduled 6:30 | 10-__ __:__ | refreshed on its own: yes / no | Tasks > Scheduled history | | |
| 2 Repo Health | live, __:__ | __:__ | sheet, __ rows | github.com, 3 spot checks | __ / 3 | stars-gained column: |
| 2 "Send me the top 3" | __:__ | card at __:__, landed __:__ | approval card: yes / no | Slack DM or email timestamp | | card showed: action / destination / content / recipients (circle what it showed) |
| 3 Skool deck | 10-__ __:__ | __:__ | __ slides + post | transcript_<id>.txt | __ / __ prompts quoted right | |
| 3 Voice edit from phone | __:__ | __:__ | slides changed: both / one / neither | the deck on web | | |

Usage meter (Settings > Usage, or the label on your account):
- before the deck: __
- after the deck: __
- weekly limit resets: __

Connectors confirmed in Duet's connections view on filming morning: GitHub ( ), Slack ( ), Gmail ( )
GitHub connector reached tylerprogramming/content (private): yes / no / fallback used: ______
```
