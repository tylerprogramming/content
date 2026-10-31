# Filming guide, video 063: I Gave Claude Duet 3 Real Jobs

Film from this without reading the script. Target 12 min, ceiling 13. Two of the three jobs (Channel Pulse, the Skool deck) exist before you press record. Three things happen live: the Repo Health sheet (step 3 and 6), the approval card (step 7), and the voice edit (step 9).

Everything the researcher could not see on a real account is marked **to verify**. The 062 lesson: docs and your screen did not match. Walk the "Confirm on your account" list below before you believe a single label in the script.

---

## PRE-BUILD (do all of this before filming day)

Every Duet task that has to have already run, with the earliest day it can be filmed. Dates assume you do the Day 0 items on **Tue 2026-10-27**. If Day 0 slips a day, every date below slips with it.

| # | What has to exist before filming | How | Needs to run for | Earliest film day |
|---|---|---|---|---|
| 1 | You are in. Duet open on the web and on the phone, same account. | Waitlist invitation on the email tied to your Claude account. Open `claude.ai` and the Duet app on the phone. If you are not in yet, nothing below can start; block the shoot, do not fake it. | 5 min | Day 0 |
| 2 | GitHub and Slack show up in Duet's connections view, and GitHub can read `tylerprogramming/content` (private). | `claude.ai` Settings > Connectors: confirm GitHub and Slack are connected. For the private repo, open the GitHub App settings from the connector and grant `tylerprogramming/content` (help center: private repos need the GitHub App grant). Then in Duet's main thread paste the test prompt below (Test G). If it reads the file, write "yes" in `receipts.md`. If it cannot, note the exact message; the fallback for Jobs 1 and 3 is to paste the status.md lines and the transcript text into the prompt, and you say that on camera in step 2. | 15 min | Day 0 |
| 3 | **Job 1, Channel Pulse**, built, and its weekday 6:30am refresh has fired on its own at least once. This is the hook. A test run does not count; the hook says "I was asleep." | Paste Prompt P1 below into Duet's main thread on Day 0. When it finishes, open Tasks > Scheduled and confirm the refresh is listed. Next morning after 6:30, open the task's history and the artifact. Write the time it shows into `receipts.md`. If it did not fire, ask Duet why in chat, screenshot the answer, and film the fallback open: "I asked for this to refresh at 6:30 and it did not. Here's what it said." | Build 10 to 15 min on Day 0, then one overnight | **Wed 2026-10-28** (Thu 10-29 if you want two clean mornings in the history) |
| 4 | Job 1 checked against YouTube Studio once, off camera, so you know the count before you say it live. | Open Studio > Content, last 10 uploads, next to the dashboard. Tick the rows that match. Write the count into `receipts.md`. On camera you do it again, slower. | 10 min | Day 1 morning |
| 5 | **Job 3, the Skool deck**, built from a real transcript. | Pick the newest public video that has a transcript in `transcripts/` (057 has `transcript_057-hermes-agent.txt`; 056 has `transcript_056-deepseek-harness.txt`; check whether a newer one exists with `ls -t ~/content/transcripts | head`). Paste Prompt P3 below with that video's id and filename filled in. When it lands in Make, click through it once and count the prompt slides. Do NOT fix anything; the live voice edit in step 9 is the fix. | 15 to 30 min | Day 0, filmable **Tue 2026-10-27** |
| 6 | The approval card path proven once, off camera, on a throwaway message. You need to know which channel raises a card: Slack DM or email. | In Duet chat: `Send me a Slack DM that says "test from Duet".` Watch what happens. Three outcomes: (a) a card appears asking you to approve, note exactly what it shows (action, destination, content, recipients); (b) it sends with no card, note that; (c) it says Slack cannot send from Duet (the help center says Slack "works with limits"), note the message and repeat the test with `Email me a one-line test at [your address].` Whichever path raised a card is the one Prompt S uses in step 7. Write the path and the card's layout into step 7's "What you will see" note. | 10 min | Day 0 |
| 7 | **Job 2, Repo Health**, run once off camera so you know how long it takes and whether the stars-gained column is wrong. | Paste Prompt R (in `script.md`) into a channel you will not film in, or into the main thread and delete nothing. Note: duration from the task thread, row count, what the stars-gained column did. On filming day you paste the same prompt live; if the live one is slow, you cut to this one and say so. | 10 to 20 min | Day 0 |
| 8 | Usage meter read before and after the deck (item 5). | Find the usage display on your account (Settings > Usage on claude.ai is the likely place; **label to verify**). Screenshot before pasting P3, screenshot after it lands. Two numbers into `receipts.md`. | 2 min | Day 0, around item 5 |
| 9 | Phone voice edit works end to end once. | On the phone, open Duet, hold voice, ask it to change one word on any artifact. Confirm the change shows on the web. If voice messages are not available on your account, step 9 becomes a typed edit on the phone; say so. | 10 min | Day 0 |
| 10 | `receipts.md` filled from real timestamps. | Copy is already in this folder. Every cell from a task thread, a Slack or email timestamp, Studio, github.com, or the transcript. No estimates. | 15 min | Filming morning |
| 11 | You know which plan you are on (Pro or Max, which tier) and say it once in step 10. | Not in any file. | 0 | |

### Timings summary

| Day | Do |
|---|---|
| Tue 10-27 (Day 0) | Items 1, 2, 3 (build + schedule), 5, 6, 7, 8, 9, 11. About 2 hours hands-on, mostly waiting on builds. |
| Wed 10-28 morning | Check the 6:30 refresh (item 3). Item 4. Item 10. Film, or wait one more morning. |
| Thu 10-29 morning | Second refresh in the history. Film if you skipped Wed. |

Earliest full shoot: **Wed 2026-10-28**. Without item 3 you can film steps 2 to 12 on Tue 10-27 and record step 1 (the hook) Wed morning; the hook is a screen recording plus one camera line, so it cuts in clean.

### Prompts (paste as written)

Test G (item 2, GitHub reach):

```
Read youtube/notes/status.md in my GitHub repo tylerprogramming/content and tell me the first line under the heading "FRESH". Do not change anything.
```

[Confirm the heading exists before pasting; use any heading that is actually in the file.]

Prompt P1, Job 1, Channel Pulse (item 3):

```
Build me a dashboard called Channel Pulse. Source 1: my YouTube channel youtube.com/@tylerreedai, public data for every video from the last 90 days. Source 2: my GitHub repo tylerprogramming/content, files youtube/notes/status.md and the newest 3 files in youtube/analytics/daily/. Show: a table of the last 10 uploads with views, views per hour since upload, and whether each beat the median of the previous 20 uploads. One line for what is filming next, from status.md. Three "where to look" bullets with the number that made you pick each. Show the time you last refreshed it on the page. Refresh every weekday at 6:30am Eastern. Do not post, comment, or change anything.
```

Prompt P3, Job 3, Skool deck (item 5; fill in the id and filename):

```
New task. My video [TITLE] (youtube.com/watch?v=[ID]) is live. Get its transcript from my GitHub repo tylerprogramming/content, file transcripts/transcript_[FILENAME].txt. Make a slide deck for my Skool community The AI Agency, 6 to 8 slides: title, what you will have at the end, the 3 steps in order with the exact prompt I used on each step's slide quoted word for word from the transcript, the links from the video description, one slide of mistakes to avoid. Plain style. Then write a 120-word community post in my voice. Put both in the Make tab and message me. Do not post to Skool or anywhere.
```

Prompt R (Job 2) and Prompt S (the send) are in `script.md` under the beat table. Paste from there.

---

## Confirm on your account before filming

Every button, tab, and screen name the script leans on. Source column says where the researcher saw it. Tick it, or write the real label in the margin and say the real one on camera.

| # | Script says | Where it was seen | Status |
|---|---|---|---|
| 1 | Tabs: **Chat**, **Tasks**, **Make** | Help center + Riley 03:34, Brock 03:46 | likely, confirm |
| 2 | Tasks tab sections: **Active**, **Up next**, **Scheduled**, **Resolved** | Peter 02:28, Riley 11:40, John 03:33. Not in docs | confirm |
| 3 | Task states: **working**, **ready for review** | Peter 02:28, Riley 11:40 | confirm |
| 4 | A scheduled task has a **view history** (or similar) view | Peter 04:53, on a default check-in. Never seen on a user-made refresh | **to verify** |
| 5 | A user-made scheduled refresh appears under **Scheduled** | Riley 17:06 shows his own "artifact recap" there | likely, confirm |
| 6 | The dashboard artifact shows a refresh or last-updated time | Not seen anywhere. P1 asks for it on the page | **to verify**; if absent, the task history time is the receipt |
| 7 | Make tab has a **spreadsheet / sheet** artifact type | Brock 04:45 lists document, presentation, design, dashboard, page. No sheet label seen | **to verify the label**; if Duet returns a table inside a doc instead, say "it made it a document, not a sheet" |
| 8 | Duet has a **connections** view that lists GitHub and Slack | Riley 02:42 taps a connections icon. Label unknown | **to verify** |
| 9 | GitHub connector reaches Duet at all, and reaches a **private** repo | Not stated on any Duet page. Help center says private repos need the GitHub App grant | **to verify** (PRE-BUILD 2) |
| 10 | Slack **send** from Duet raises an approval card | Safety post: asks before sending a message. Help center: Slack "works with limits" in Duet. Nobody filmed it | **to verify** (PRE-BUILD 6); email is the fallback |
| 11 | The approval card shows **action, destination, content, every recipient** | Safety post text. Layout never filmed | **to verify** the layout; read what is there |
| 12 | **Approve** is the button label on the card | Assumed | **to verify** |
| 13 | **Settings > Usage** is where the meter lives, and what unit it shows | John 06:14 says it is hard to see. Label unknown | **to verify** (PRE-BUILD 8) |
| 14 | Voice messages on the phone app; no voice call on web | Help center (voice messages), John 02:10 (no voice on web) | confirm on your phone |
| 15 | Comment-on-artifact editing on web | Riley 05:43 | optional, not in the script; use it only if voice fails |
| 16 | `/` opens a skills list in chat | Peter 06:30 | optional, not in the script |
| 17 | Model is Opus 5.5 with no picker (said in step 12) | Help center Limitations | confirm the help page still says it on filming day |

---

## Pre-recording setup (filming morning)

1. Browser, four tabs in order: Duet web (main thread, Chat tab), YouTube Studio > Content sorted by date with the Views column visible, `github.com/tylerprogramming?tab=repositories&sort=stargazers`, `claude.com/resources/articles/claude-duet`. Windows A to D.
2. Slack open on your own DM (or Gmail, if PRE-BUILD 6 landed on email). Window E.
3. Editor split: the transcript file for the Skool deck's video on the left, `receipts.md` on the right. Window F.
4. Phone: Duet app open, notifications on, screen recording ready. Window G.
5. Usage meter: take one more "before" screenshot now, in case the live sheet moves it.
6. Do Not Disturb on the Mac. Duet and Slack desktop notifications off.
7. Camera framed. Mic check.

---

## Steps

### Step 1. Hook (0:00 to 0:35)

Screen only. Window A, Make tab, Channel Pulse. Scroll to the refresh time.

> So this rebuilt itself at six thirty this morning. I was asleep. I didn't open Claude. Claude Duet made it, and then made it again on its own.

Camera.

> So I gave Claude Duet three real jobs. A dashboard for my channel, a spreadsheet across my GitHub repos, and the lesson deck for my Skool community. Every Duet video I watched ends with someone reading the output and saying "nice." I wanted to put the output next to the source and count.

What happens next: Window D.

Fallback if the refresh did not fire: open on the task history instead and say "I asked for this to refresh at 6:30 and it didn't. So that's the first receipt." Then the same camera line.

### Step 2. What Duet is (0:35 to 1:35)

Window D. Scroll.

> Separate app from Anthropic. Research preview, waitlist, US, Pro and Max. Own computer in the cloud, keeps working when you close the app, own browser. Supposed to stop before it sends, pays, signs, or deletes. We'll test that.

Window A. Open the connections view (the real label from Confirm #8). Point at GitHub and Slack.

> What carried over: connectors, memory, and the Make tab already had my older artifacts. What didn't: files on my Mac, local Claude Code skills, local sessions. Everything from my repo goes through GitHub.

If PRE-BUILD 2 failed on the private repo, one line here: "and GitHub could not read my private repo, so for two of these I pasted the text in. Say it, move on."

### Step 3. Kick off Repo Health (1:35 to 2:15)

Window A, Chat. Paste Prompt R. Send.

> Job two, live. One row per public repo. Stars, open PRs, oldest PR age, checks on main, and a column that says which repo is a video and why.

Tasks > Active > Repo Health. Show the step list.

> It opens a task, the task has a thread, and you can see the steps. Says working. We'll come back.

Dead-air filler: "Riley Brown's first deck took about ten minutes, so we're not waiting on this."

### Step 4. Job 1, Channel Pulse vs Studio (2:15 to 4:00)

Window A left (dashboard), Window B right (Studio). Go down the last 10 uploads. Count out loud.

> [N] of ten match. [The ones that were off, and by how much.]

Filming-next line: right video or not, and where it came from.

Three bullets: read one, say whether the number behind it is real and whether you would act on it.

> [One-line verdict. Only if true.]

### Step 5. The schedule (4:00 to 4:45)

Tasks > Scheduled > Channel Pulse refresh > history (real labels from Confirm #4 and #5).

> Every weekday at six thirty. In the list. This morning's run, [time]. Peter Yang said you could schedule this and didn't. [Fired every morning since Day 0, or missed one.]

### Step 6. Job 2, the sheet (4:45 to 6:00)

Tasks > Active > Repo Health. If ready, open in Make. If not, open the PRE-BUILD 7 copy and say "this is the one from yesterday, same prompt."

Window C on the right. Three spot checks: top row stars and open PRs, a middle row's last commit, the stars-gained column anywhere.

> [Each check: right or wrong.] Stars gained in 30 days isn't a GitHub API field. I expected that column to be wrong. [Was it.]

Video candidate column: read its top pick, say whether you would make it.

### Step 7. The approval card (6:00 to 7:00)

Window A, Chat. Paste Prompt S (the version PRE-BUILD 6 proved). Send.

> Nobody filmed this part. Anthropic says it stops and shows the action, where it's going, what's in it, and every recipient. Let's see.

Hold on the card. Do not cut.

**What you will see:** [fill in from PRE-BUILD 6 before filming. Describe the real card. If no card came and it sent, write that here and say it on camera. If Slack could not send, this step runs on email.]

Approve. Window E, the message lands.

> There it is. [Time.] It built it, it asked, I said yes, it sent. Nothing moved until I said yes.

### Step 8. Job 3, the deck vs the transcript (7:00 to 8:30)

Window A, Make > the deck. Window F, transcript on the right.

> Job three. Video goes live, it becomes a Skool lesson. Six to eight slides, the steps, the exact prompts, the links, and a post. Drafted, not posted.

Click through, count slides. On each prompt slide, find the line in the transcript.

> This is the prompt on the slide. This is what I said. [Match, close, or invented.] ... [N] of [M] quoted right.

Open the post, read two lines.

> [Does it sound like you.] It didn't post anywhere. I post.

### Step 9. Voice edit from the phone (8:30 to 9:15)

Window G. Hold voice. Say in your own words: move each prompt to its own slide, cut the mistakes slide to three bullets, keep the rest. Send.

Cut to Window A.

> [Both edits, one, or neither. How long.]

Filler while it works: "No voice call on the web version, per John Aspinall. The phone is where voice lives."

### Step 10. Usage (9:15 to 9:45)

Window A, the usage meter (real label from Confirm #13).

> Included in Pro and Max right now, nothing extra, but it shares your limits. Before the deck: [number]. After: [number]. So that's one deck. I'm on [plan]. [Does a daily refresh worry you, one line.]

### Step 11. Receipts (9:45 to 10:45)

Window F, `receipts.md`, full screen. Read every row.

> Every time from the task thread. Every count from the output next to the source.

### Step 12. Close (10:45 to 12:00)

Camera.

> What didn't work: [two or three real ones from the pre-build]. No model picker, Opus 5.5 decides effort. Can't watch its browser. Can't see local skills, which is the one I'd want first.
>
> I ran the same three jobs on ChatGPT's Dots last week. That comparison is its own video if you want it, tell me in the comments.
>
> Where I landed: [which job stays on Duet, which doesn't, why]. The dashboard rebuilt itself and I didn't touch it. The judgment on top is still mine.
>
> Of these three, which would you hand to Duet first? I read every one.

End card.

---

## Timing cheat sheet

| Step | Start | Length | Window |
|---|---|---|---|
| 1 Hook | 0:00 | 0:35 | A, camera |
| 2 What Duet is | 0:35 | 1:00 | D, A |
| 3 Kick off Repo Health | 1:35 | 0:40 | A |
| 4 Job 1 vs Studio | 2:15 | 1:45 | A, B |
| 5 The schedule | 4:00 | 0:45 | A |
| 6 Job 2, the sheet | 4:45 | 1:15 | A, C |
| 7 Approval card | 6:00 | 1:00 | A, E |
| 8 Job 3 vs transcript | 7:00 | 1:30 | A, F |
| 9 Voice edit | 8:30 | 0:45 | G, A |
| 10 Usage | 9:15 | 0:30 | A |
| 11 Receipts | 9:45 | 1:00 | F |
| 12 Close | 10:45 | 1:15 | camera |
| Total | | 12:00 | |

If you are over 13: cut step 9 to 20 seconds (show the result only) and step 5 to 25 seconds.

## On-camera tips

- Say what is on the screen, not what the docs say. If the label is different, say the real one. If Duet does something the docs did not predict, that is the best 20 seconds in the video.
- Count out loud. "Seven of ten" beats "mostly right."
- Hedge the verdicts. "I think," "for me," "kind of." The receipts table does the arguing.
- If the approval card does not appear, do not re-run until it does. Film what happened.
- Do not say the plan price. The description carries it.
- Blur, do not fake. If a bullet or a DM has a personal line, blur it and say so.
