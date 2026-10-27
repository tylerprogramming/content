# Filming guide, video 062: I Tested ChatGPT Dots vs Hermes Agent on the Same 3 Jobs

Film from this without reading the script. Target 13 to 14 min. Every output on screen already exists before you press record. The only things that happen live are: editing a schedule (step 4), the rule firing (step 6), and editing a memory file (step 9).

---

## PRE-BUILD (do all of this before filming day)

Everything here has to have run and produced a result on screen before the camera rolls. Timing column is how long it needs, not how long you spend on it. Items marked overnight need their scheduled fire; plan on Monday and Tuesday setup, film Wednesday or later. Dot side is unverified until you run it on your account; the researcher could not see it.

| # | Side | What has to exist before filming | How | Needs to run for |
|---|---|---|---|---|
| 1 | Hermes | Researcher and Coder crons deliver to Slack again. Both failed on 10/23 with `no delivery target resolved for deliver=slack`. Without this, hook A has no bottom message. | `hermes -p researcher cron doctor` then `hermes -p coder cron doctor`. Fix the delivery target (the profile's `SLACK_HOME_CHANNEL` is set to `C0C0CD3JUTU` in config; the researcher profile may need its own Slack bot per the `hermes profile list` warning). Then force one run: `hermes -p researcher cron run bff2da40e427` and confirm it lands in Slack. | 20 min, then one scheduled 7:45 fire the next weekday to prove it |
| 2 | Dot | Job 1 scheduled task exists and has delivered at least two mornings. | In the Dot's chat, paste the prompt below (Job 1). Confirm the schedule when it asks. Check Profile > Activity > Scheduled the next morning. Needs the GitHub plugin connected and `tylerprogramming/content` authorized (Settings > Plugins > GitHub). | Overnight x2 (two weekday mornings) |
| 3 | Dot | The Custom Rule for beat 6 is saved. | Settings > Personalization > Custom rules. Add: action `create or close GitHub issues, merge or comment on pull requests` = **Hand off to you**. Add a second: action `open a pull request on my GitHub repos` = **Ask before taking action**. (Two rules so beat 7's PR can still happen with an approval; beat 6's issue cannot.) | 5 min |
| 4 | Dot | Job 2 scheduled task exists and has delivered at least one 9 AM digest. Then the hand-off tested once off camera. | Paste the Job 2 prompt below. Next morning, open the digest in Slack, pick an issue it suggested, and in chat type `Go ahead and open that issue on the repo.` Write down exactly what the screen does (a hand-off card, a refusal line, an Auto-review banner). Put that in the "What you will see" note under step 6 so you narrate the real thing on camera. | Overnight x1, then 10 min |
| 5 | Dot | The Dot can read `#bots` in Slack. | Invite the ChatGPT Slack app to `#bots` (`/invite @ChatGPT` in the channel). Then paste the beat 5 prompt once. If it works, note the answer. If it cannot read the channel, note the exact error; beat 5 films the error instead. | 10 min |
| 6 | Hermes | Researcher's 7:45 brief from the same morning as the Dot's. | Automatic once item 1 is fixed. Confirm in Slack on filming morning. | Overnight, same morning as item 2's second fire |
| 7 | Dot | A PR from the Dot (via Codex) on `tylerprogramming/content`, open, not merged. | Paste the PR prompt below. Approve when the "Ask before taking action" rule prompts you. Write the PR number into step 7. If Codex cannot reach the private repo, note that; beat 7 shows the failure. *to verify* | 30 min, Codex run time varies |
| 8 | Hermes | A PR from Coder on the same repo, same change, open, not merged. | `cd /Users/tylerreed/content && hermes kanban create "062: add Dots row to system/INDEX.md" --assignee coder --body "Open a PR on tylerprogramming/content (branch off main) that adds one row to system/INDEX.md under the research section linking research/2026-10-24-openai-dots.md with a one-line description. Do not merge. Report the PR URL in Slack."` Coder's SOUL rule 3 allows small PRs when asked and never merges. Write the PR number into step 7. | 15 to 30 min |
| 9 | Both | Job 3 drafts from both sides for the newest public video. | Dot: paste the Job 3 prompt below. Hermes: `hermes kanban create "Skool: prep lesson + post for newest public video" --assignee skool-librarian --body "Prep the lesson, guide PDF and feed post for the newest public video on tylerreedai. Do not post. Block the card for my approval as usual."` The Librarian will Slack you one message and block itself; leave it blocked. Open the Dot's draft page and the Librarian's Slack message side by side for beat 8. | 30 min each, can run in parallel |
| 10 | Both | `receipts.md` filled in from real timestamps. | Copy the template at the bottom of this file to `/Users/tylerreed/content/youtube/videos/062-openai-dots/receipts.md` on filming morning. Hover each Slack message for its timestamp. Every cell comes from Slack, a file, or Activity. No estimates. "Did not run" is a valid cell. | 15 min, filming morning |
| 11 | Hermes | The per-profile cost loop prints ten Estimated lines. `hermes insights` is per profile; there is no all-profiles flag (checked `hermes insights --help`, Oct 24). | Run `for p in default coder coder-reviewer inbox-triage opus packager researcher skool-librarian sol workshop; do echo "== $p"; hermes -p $p insights --days 7 \| grep Estimated; done` once. Add the ten numbers and write the sum into `receipts.md`. If a profile errors or prints nothing, note it and say so on camera. | 3 min |
| 12 | Hermes | Decide on the broken ClickUp crons. `Attend: today` and `YouTube: What's Next` both errored 10/23 with a ClickUp API traceback (`~/.hermes/cron/jobs.json`, `last_error`). | Either fix the token, or leave them and show `hermes cron runs 4037e1072b29 --limit 3` in step 4 as "and when one breaks, it tells me." Optional beat; 20 seconds. | 10 min |
| 13 | Both | Tyler knows which Pro tier he is on and says it in step 10. | Not in any file. | 0 |
| 14 | Hermes | The counts you say to camera in steps 2, 4 and 10 are read off disk on filming morning, not from this guide. | Run `hermes profile list` (profile count), then `grep -c '"id":' ~/.hermes/cron/jobs.json ~/.hermes/profiles/*/cron/jobs.json` (jobs per profile; on Oct 24 it was default 4, coder 1, opus 1, researcher 1, sol 1 = 8 jobs on 5 profiles, 10 profiles total), then `sqlite3 ~/.hermes/profiles/researcher/cron/executions.db "select status,count(*) from executions where job_id='bff2da40e427' group by status"` (completed and failed totals; on Oct 24 it read completed 24, failed 1). `cron list` prints no run count and `cron runs --limit 5` prints 5 rows, so neither is the number. Write the three numbers into `receipts.md` and say those. | 3 min, filming morning |

### Prompts for the Dot (paste as written)

Job 1, morning brief:

```
Every weekday at 7:45 AM Eastern, for the next 4 weeks, read youtube/notes/status.md, the newest file in youtube/analytics/daily/, youtube/ideas/video-ideas.md, and anything in research/ from the last 7 days in my tylerprogramming/content GitHub repo. Send me one Slack DM under 900 characters: what is filming next, yesterday's channel numbers, and 3 video openings with a one-line reason each. End with "Reply with a number." Do not post anywhere else and do not change any files. Confirm the schedule.
```

Job 2, repo check:

```
Every day at 9 AM Eastern, check my GitHub repos under tylerprogramming. Look for open PRs with failing checks, issues with no reply for 7+ days, and dependencies flagged by Dependabot. Send me a Slack DM with at most 5 items, each with a link. Never open, close, merge, or comment on anything; if you think a PR or issue should be created, ask me first. Confirm the schedule.
```

Job 3, Skool prep (daily check; YouTube is not an event source the Dot can watch, per OpenAI's scheduled-tasks page):

```
Every day at 10 AM Eastern, check my YouTube channel tylerreedai for a video that went public in the last 24 hours. If there is one, get its transcript, then draft: a lesson title, two short paragraphs describing the video, 2 to 4 key links from the description, and a 120-word community post for my Skool group The AI Agency. Put the drafts in a page and send me the link in Slack. Never post to Skool or anywhere public; I will post. Confirm the schedule. For the first run, use the newest public video on the channel even if it is older than 24 hours.
```

PR task (beat 7):

```
Open a pull request on my tylerprogramming/content repo, branched from main, that adds one row to system/INDEX.md under the research section linking research/2026-10-24-openai-dots.md with a one-line description. Use Codex. Do not merge. Send me the PR link.
```

### Timings summary

| Day | Do |
|---|---|
| Mon | Items 1, 2, 3, 4 (create), 5, 7, 8, 9, 11, 12, 13. About 2.5 hours of hands-on time, mostly waiting on Codex and Coder. |
| Tue morning | Check: Dot brief (7:45), Researcher brief (7:45), Dot digest (9:00). Item 4 hand-off test after the digest. |
| Wed morning | Second Dot brief and Researcher brief. Item 10 (receipts) and item 14 (counts). Film. |

If Wednesday's pair of 7:45 messages is clean, use Wednesday's. If not, Tuesday's.

---

## Pre-recording setup (filming morning)

1. ChatGPT desktop app open, signed in, Dot's profile visible. Window A.
2. Slack open on the Dot DM and the Researcher DM, both from this morning, scrolled so both are visible. Window B.
3. Terminal, cwd `/Users/tylerreed/content`, font size up. Window C. Use a default-profile shell (no `HERMES_PROFILE` set), or prefix every default-home command with `-p default`; under another profile `hermes cron runs 1a2d2f48d80f` prints "No cron execution attempts recorded" and `hermes insights` shows that profile's number, not default's.
4. Browser tabs in order: `https://openai.com/index/introducing-dots/`, `https://github.com/tylerprogramming/content/pulls`, `https://learn.chatgpt.com/docs/pricing`. Window D.
5. Editor open on `/Users/tylerreed/content/youtube/videos/062-openai-dots/receipts.md`. Window E.
6. Do Not Disturb on the Mac. Slack notifications off (the Dot and the bots both ping).
7. Camera framed. Mic check.

---

## Steps

### Step 1. Hook (0:00 to 0:40)

Screen only, no camera. Window B. Scroll so both 7:45 messages are visible.

> Two messages. Same morning, same minute, same job. The top one is from my Dot. I paid for it on Saturday. The bottom one is from Researcher, a Hermes bot that has been running on this Mac for five weeks.

Cut to camera.

> So I gave the Dot the three jobs my bots already do. Same prompts, same accounts, same week. And I kept the receipts.

What happens next: you move to the browser.

Dead-air filler: "And I want to be clear, I did not clean these up. This is what landed."

### Step 2. What a Dot is (0:40 to 1:40)

Window D, tab 1. Scroll slowly.

> Quick version. A Dot is an agent that lives in ChatGPT. Own computer in the cloud, own browser, runs on GPT-6 Astra. Plugins from ChatGPT and Codex carry over. Background research is read-only. One Dot, included on Pro or Business Premium, not Plus, not in the EU or UK right now.

Window C:

```
hermes profile list
```

> This is the other side. Ten profiles. Each one is a bot with its own model, memory, and rules. Five of them have scheduled jobs, eight jobs total. [Say the numbers from PRE-BUILD item 14, not these.]

### Step 3. What you can see (1:40 to 3:10)

Window A. Click the Dot's profile > Computers > the computer > **Take over**. Move the mouse. Click something. **Return control**.

> That is me on a computer I do not own. If it gets stuck on a login, this is where you help it.

Profile > **Activity**. Point at In progress, Scheduled, Completed.

> Desktop only. You cannot see this on your phone.

Type in the Dot's chat:

```
What are you working on right now, and what needs my input?
```

Wait for the answer. Window C:

```
tail -40 /Users/tylerreed/.hermes/profiles/researcher/logs/agent.log
```

> Same thing for Researcher. It is a log file. Ugly, but I can grep it.

```
hermes kanban show t_ab09f580
```

> This is the card that built this video. Researcher handed to Packager, Packager wrote the script. That handoff is a row in a SQLite file.

Dead-air filler while the Dot thinks: "The Dot is on a real machine, so sometimes you wait. That is kind of the point."

### Step 4. Job 1, the brief (3:10 to 4:40)

Window A. Activity > Scheduled > click "Morning content brief". Show the instructions.

> I set this up Monday. Since October 13th you can open these and edit them.

Change the time to 7:46, then back to 7:45. Save.

Window B. The Dot's brief, full screen. Blur any personal line and say so.

> This is what it sent this morning. [Say what the real brief got right and what it got wrong. Check it against status.md first. Never mock one up.]

Window C:

```
hermes -p researcher cron list
sqlite3 ~/.hermes/profiles/researcher/cron/executions.db "select status,count(*) from executions where job_id='bff2da40e427' group by status"
hermes -p researcher cron runs bff2da40e427 --limit 5
```

Point at the completed row of the query, not at `cron list` (it prints no count).

> [Read the completed count off the query.] completed runs, and it tells me the one that failed. The last five with their status. One failed to deliver last week and it told me.

Optional (item 12): `hermes cron runs 4037e1072b29 --limit 3` to show a broken job reporting itself.

Window B. Researcher's brief.

> Same shape. Three openings, reply with a number. When I reply, it does the research. The Dot does not have that step, because the Dot is one agent and this is three.

### Step 5. The Dot reads the bots (4:40 to 5:50)

Window A. Type:

```
Read the #bots channel in my Slack from the last 48 hours. Tell me what Researcher handed to Packager, and whether Packager finished. Do not reply in the channel.
```

Wait. Narrate what comes back. If it errors, show the error and say "so it cannot see this channel, and that is a result."

Window B. `#bots`, scroll to the real handoff.

> This is the thread it read. Researcher wrote this. Packager wrote this. I did not type any of it.

### Step 6. Job 2 and the rule (5:50 to 7:40)

Window A. Settings > Personalization > Custom rules. Show both rules.

> Before I turned the repo check on, I set this. Create or close issues, merge or comment on PRs: Hand off to you. Strictest of the four levels.

Window B. The Dot's 9 AM digest.

> [Say what the real digest contained: item count, links, and whether it stayed read-only. If it did something you did not ask for, say that.]

Window A. Pick one issue from the digest. Type:

```
Go ahead and open that issue on the repo.
```

Hold on whatever happens.

**What you will see:** [fill in from PRE-BUILD item 4 before filming. Describe the actual card or banner. If Auto-review fired instead of the Custom Rule, say so; it is a separate system.]

> It stopped, it told me why, and the issue did not get created.

Window C:

```
sed -n '15,19p' /Users/tylerreed/.hermes/profiles/researcher/SOUL.md
```

> Line 18. "Never publish, post, or schedule anything." A sentence in a markdown file. The bot reads it every time it wakes up.

Camera:

> The Dot's rule is enforced by OpenAI, with Auto-review behind it that I cannot turn off. Mine is enforced by the model reading a file. It has held for five weeks. But it is a different kind of promise.

### Step 7. Two PRs (7:40 to 9:10)

Window D, tab 2. Two open PRs.

PR numbers: Dot `#____`, Coder `#____` (fill in from PRE-BUILD 7 and 8).

Click the Dot's PR > Files changed. Read the diff out loud. Click Coder's > Files changed. Same.

> I'd merge [which]. [Why, one sentence.] Riley Brown's video trusted "all tests passed." I would rather read eleven lines.

Do not merge either.

If long: cut this to 30 seconds, show both PRs exist, move on.

### Step 8. Receipts (9:10 to 10:40)

Window E. `receipts.md` full screen. Read row by row.

For job 3, split Window A (Dot's draft page) and Window B (Librarian's Slack message) for ten seconds.

> The Dot put its draft in a page. The Librarian put it in the course and blocked itself until I approve. Neither posted. That was the rule on both sides.

Camera: the honest read. What the Dot did better, what the bots did better, what both got wrong.

### Step 9. Memory (10:40 to 11:40)

Window A. Profile > Memory.

> I can see it has memories. The help center says I cannot view or edit individual ones. Reset deletes the Dot.

Window C:

```
open -e /Users/tylerreed/.hermes/profiles/researcher/memories/MEMORY.md
```

TextEdit opens. Change one word. Save. Close.

> Two lines. I changed one. That is the whole beat.

### Step 10. Cost (11:40 to 12:40)

Window D, tab 3.

> First Dot is included on Pro, starts at a hundred a month, or Business Premium. Not Plus. I am on [tier]. Dot chats do not count against limits. Codex work does.

Window C:

```
for p in default coder coder-reviewer inbox-triage opus packager researcher skool-librarian sol workshop; do echo "== $p"; hermes -p $p insights --days 7 | grep Estimated; done
```

Ten Estimated lines, one per profile. Read two or three, then the sum from `receipts.md`.

> Ten profiles, one line each, eight scheduled jobs, last seven days. Software is free. The model is what you pay for, and I can point any bot at a local model and make that line zero.

### Step 11. Close (12:40 to 13:30)

Camera.

> Only the Dot: I can call it from a walk, it wakes itself up, it has a browser that is not mine. Only the bots: they talk to each other, memory is a file I can edit, any of them can run on a local model for nothing. The whole point is you probably do not pick one.
>
> Tell me in the comments: of the three jobs, which would you hand to the Dot, and which would you keep on your own machine. I read every one.

End card. 057 left.

---

## Timing cheat sheet

| Step | Start | Length | Window |
|---|---|---|---|
| 1 Hook | 0:00 | 0:40 | B, camera |
| 2 What a Dot is | 0:40 | 1:00 | D1, C |
| 3 What you can see | 1:40 | 1:30 | A, C |
| 4 Job 1 brief | 3:10 | 1:30 | A, B, C |
| 5 Dot reads bots | 4:40 | 1:10 | A, B |
| 6 Job 2 and the rule | 5:50 | 1:50 | A, B, C, camera |
| 7 Two PRs | 7:40 | 1:30 | D2 |
| 8 Receipts | 9:10 | 1:30 | E, A, B, camera |
| 9 Memory | 10:40 | 1:00 | A, C |
| 10 Cost | 11:40 | 1:00 | D3, C |
| 11 Close | 12:40 | 0:50 | camera |
| Total | | 13:30 | |

## On-camera tips

- Never say "it should." Say what is on the screen. If the Dot did something the docs did not predict, that is the best 20 seconds in the video.
- Blur, do not fake. If a brief has a personal line, blur it and say "that one is personal." Riley Brown did this and it reads as honest.
- Hedge on the verdicts. "I think," "for me," "kind of." The table does the arguing.
- The Dot is slow sometimes. Let it be slow on camera, cut it in the edit. Do not fill with hype.
- Say the tier once. Do not say a price in the first 30 seconds; the thumbnail and description carry it.

---

## receipts.md template

Copy to `/Users/tylerreed/content/youtube/videos/062-openai-dots/receipts.md` on filming morning and fill from Slack timestamps, Activity, and the files.

```
# Receipts, week of 2026-10-27

| Job | Agent | Asked / scheduled | Delivered | What came back | What it got wrong |
|---|---|---|---|---|---|
| 1 Morning brief | Dot | 7:45 ET | __:__ | | |
| 1 Morning brief | Researcher (Hermes) | 7:45 ET, run __ | __:__ | | |
| 2 Repo check | Dot | 9:00 ET | __:__ | __ items | |
| 2 Repo check | Repo Health (Hermes) | 9:00 ET, run __ | __:__ | __ items | |
| 2 Hand-off test | Dot | "open that issue" at __:__ | __:__ | | |
| 3 Skool prep | Dot | 10:00 ET | __:__ | page link | |
| 3 Skool prep | Skool Librarian (Hermes) | card at __:__ | __:__ | blocked for approval | |
| PR | Dot via Codex | __:__ | __:__ | PR #__ | |
| PR | Coder (Hermes) | __:__ | __:__ | PR #__ | |

Counts read off disk this morning (PRE-BUILD item 14):
- profiles: __  (`hermes profile list`)
- cron jobs: __ across __ profiles  (`grep -c '"id":' ~/.hermes/cron/jobs.json ~/.hermes/profiles/*/cron/jobs.json`)
- Researcher runs: __ completed, __ failed  (`sqlite3 ~/.hermes/profiles/researcher/cron/executions.db "select status,count(*) from executions where job_id='bff2da40e427' group by status"`)
- Hermes 7-day cost, sum of the ten profile lines: $__  (PRE-BUILD item 11 loop)
```
