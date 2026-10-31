# Creator breakdown: Claude Duet (video 063)

Date: 2026-10-27 (card asked for the 10-26 filename). Two reference videos, both transcribed locally (mlx). Timestamps are from the transcripts. View counts from yt-dlp on 2026-10-27 15:30 ET.

| Reference | Id | Views | Dur | Uploaded | Transcript |
|---|---|---|---:|---|---|
| Peter Yang, "Claude Duet Is Here! (Better than Grok Bot?)" | D-pz8L1orVI | 91,399 | 17:25 | 2026-10-21 | `transcripts/transcript_D-pz8L1orVI.txt` |
| Riley Brown, "How I'm Actually Using Claude Duet (After 10 Hours of Testing)" | ZIBI6FiLxgQ | 106,416 | 24:24 | 2026-10-23 | `transcripts/transcript_ZIBI6FiLxgQ.txt` |

Why these two: Peter built the most artifacts on his own data (morning brief, YouTube report, sponsor dashboard) and is the only one who showed the scheduled check-in. Riley is the only one who built a deliverable live from prompt to result on camera and showed the edit loop (comment, voice). The other 4 transcripts (Alex Finn, How I AI, Brock live test, John Aspinall) are tours or opinion; cited in the research file.

Field answers (6 transcripts): real deliverable on own business and judged, partly (3 built, 0 checked against source); approval card firing on screen, 0; morning brief arriving on its own, 0. Table in `research/2026-10-26-claude-duet.md` section 3.

---

## A. Peter Yang, 17:25

### Beat table

| # | Beat | Time | What is on screen, what he types |
|---|---|---|---|
| 1 | Cold open, promise list | 00:00 to 00:45 | Face. "walk through how I use it to create a morning brief, a YouTube report, a sponsored dashboard, and even an AI explorer club for my kids". Promises the Uber failure and a ranking vs Grok Bot, Muse, Dots. |
| 2 | Onboarding | 00:48 to 01:49 | Mobile app plus "its own interface on Claude web". Already connected to his Claude account, no re-auth. First conversation: Duet read email, calendar, connected apps and wrote back how he works ("I run Behind the Craft like a product"). It suggested 3 starting tasks: sponsor call prep with Diana, podcast interview guide, cleaning meetup entries. |
| 3 | Tasks tab | 01:56 to 02:44 | Clicks the interview guide; Duet spins up a task. Tasks tab shows Active, Up next, Scheduled ("scheduled routines and scheduled jobs that run every day or every week"), Resolved. "works a lot like Claude Projects, main chat with sub chats". |
| 4 | Channels | 02:51 to 04:24 | Cannot rename or avatar the main thread. Creates "test channel", changes icon pencil to home, changes color. The new channel suggests 3 tasks from his email and calendar. Creates "test group", drags channels in. |
| 5 | Why it is a separate app | 04:24 to 04:46 | Opinion: research preview first, merge into the Claude app later "like cowork and chat". |
| 6 | The proactive check-in | 04:46 to 05:42 | Opens a default scheduled task, "view history". "runs every three hours from 9am to 10pm". Reads one message: "morning to you Peter, here's a sponsorship deal with Diana ... Mercury payroll video ... Friday podcast with Nate". Judges 5 a day "too much", says you can ask Duet to change the schedule. |
| 7 | Sponsor | 05:47 to 06:23 | Wispr Flow. |
| 8 | `/` skills and `/morning` | 06:24 to 07:20 | "if you type slash you can see all kinds of skills". `/morning` "renders the user's morning brief as a styled HTML artifact". Prompt: **"morning, let's try out the skill"**. Shows the brief: 2 short calls before 9, day open, a sun graphic, items to address (Mercury contract). |
| 9 | "Learn how I write" skill | 07:26 to 08:06 | It read 33 sent emails, 89 Slack messages, 47 DMs, 11 docs and wrote a style guide ("open with the point, number your asks, lowercase with your team"). |
| 10 | Daily to-do and email triage artifacts | 08:06 to 09:03 | Two default artifacts. On the triage artifact he comments per email: **"for Freeman, let's decline. Can you send the reply? For Nikhil, I recommended two colleagues from Roblox. Can you reply directly?"** Drafts appear below for edit before send. No approval card shown. |
| 11 | YouTube report | 09:03 to 10:14 | A year of published videos, public data. Subscribers and video count up top, insights ("personal AI agent videos are my breakout topic", "solo beats guest unless the guest has a demo"), chart of every video by publish date, keywords, length. The prompt, verbatim: **"hey can you make a dashboard and insights on my YouTube performance data"** plus his channel link. |
| 12 | Sponsor revenue dashboard | 10:14 to 11:16 | Mock data, he says so (10:31). Revenue booked 2026, revenue by sponsor, follow-ups waiting, contracted. Insights: "lots of revenue ending in Q4, nothing booked for next year". Says you can schedule weekly refresh and email delivery; does not do it. |
| 13 | AI Explorer club for his kid | 11:16 to 12:08 | Animated artifact with a robot, adventure path, lesson 1 on chatbots. Judges "too text heavy". |
| 14 | Shortcomings | 12:08 to 13:54 | Uber skill: asked pickup, time, destination; he typed **"Palace of Fine Arts"**; blocked by Uber's human check; "Duet doesn't actually let me see its browser". Second: skill library cannot see his local skills. |
| 15 | Ranking | 13:54 to 16:46 | Grok Bot 1 (free X integration), Muse 2 (phone calls, free), Dots 3 (inside ChatGPT, buggy at launch), Duet "most proactive out of the box" but missing browser view and local skills. |
| 16 | Close | 16:46 to 17:25 | Prediction: merged into the Claude app. Waitlist line. |

### His rhythm

- Promise list of 4 artifacts in the first 20 seconds, then deliver them in order. Each artifact beat is 60 to 70 seconds: say the prompt, show the result, read 2 insights out loud, move on.
- Tour first (beats 2 to 6, 5 minutes), artifacts second (beats 8 to 13, 6 minutes), failures third, ranking last. The viewer who came for "what did it make" waits 6 minutes.
- Judges by reading the output, never by checking it. "it found that personal AI agent videos are my breakout topic" is accepted as true.
- Names every UI label as he clicks it (Active, Up next, Scheduled, Resolved, view history, Make). Useful to us: those labels are verified on camera.
- Hedges the mock data honestly (10:31). Keeps trust.

### What works

| Thing | Evidence |
|---|---|
| Artifacts from one-line prompts | 11, 12 and 13 all from prompts under 20 words. The audience learns the bar is low. |
| The scheduled check-in history view | Only creator to show it (beat 6). It answers "is it actually proactive". |
| `/` skills reveal | Beat 8. A hidden feature the docs do not mention. |
| Honest failure | Beat 14, the Uber wall. |

### Weaknesses, our openings

| Weakness | Opening |
|---|---|
| Sponsor dashboard is mock data | Tyler's are real: analytics CSVs, status.md, the Skool audit. |
| YouTube report judged by reading, not checked | Put YouTube Studio or the analytics file next to the artifact and count what it got right. |
| Never showed the brief arriving; triggered `/morning` by hand | Set the cadence on day 0, film the 10-28 morning arrival with the timestamp. |
| Scheduled refresh "you can" but not done | Schedule Build 1's refresh and show the Scheduled list with it in there, then the refreshed artifact next morning. |
| Email triage sends with no approval card shown | A Slack send or a delete will raise the card (S). Film the card. |
| Audience is generic busy professional | Ours is Claude Code users. Open with what carries over (memory, skills, Make artifacts from Cowork and Claude Code) and what does not (local files, local skills, local sessions). |

---

## B. Riley Brown, 24:24

### Beat table

| # | Beat | Time | What is on screen, what he types |
|---|---|---|---|
| 1 | Cold open, "9 things" | 00:00 to 00:25 | "I've spent around 10 hours using this app for my business, content, creating apps, and presentations". 9 things format. |
| 2 | Thing 1: standalone iOS and web app | 00:25 to 01:13 | Claude app and Duet app side by side on his phone. The access hack: DM Richard Kim on X. |
| 3 | Thing 2: snappy, Channels | 01:13 to 04:24 | Not personified, "musical themes", Slack-like channels. Made 10, deleted most, kept content, finances, artifacts. Voice dictation prompt: **"hey, can you please add something at the end of the presentation we were last working on in the content channel? Add that I really like voice dictation, just as a little bonus slide at the end."** Taps the connections icon (02:42). Duet routes it to the content channel, task "adding the voice dictation bonus slide to the end of the Duet deck". Opens the deck. Real-time sync to web. Bottom tabs: chat, Tasks (Active, Up next), Make. |
| 4 | Sponsor | 04:24 to 05:27 | Bluehost VPS. |
| 5 | Thing 3: comment tool on artifacts (web) | 05:27 to 06:52 | Clicks a slide, adds a comment: **"make number three adding comments, great artifact editing on web"**. The comment is sent to Duet as an edit. Then: **"can you make these super easy to comment? And then add an image on this slide right here, which is the thing three details page, except crop out the little edge here."** Image lands on the slide. |
| 6 | Thing 4: voice-edit artifacts from a phone | 06:52 to 09:00 | Opens the deck in Make on the phone. Cannot voice inside the artifact; exits, taps voice. One long spoken edit list (07:40 to 08:25): line break after "need", bigger text, "a cool little graphic that's only gray", a bullet on how he uses Duet, a new slide after 19 with "I'm not sure how I feel about this one". Hits X, fires. |
| 7 | Thing 5: every task gets a thread | 09:00 to 10:27 | First deck took "about 10 minutes" (09:31 to 09:36). Three levels: main chat, channel chat, task thread. "a little confusing". |
| 8 | Live build: Q4 predictions deck | 10:27 to 13:29 | Main thread prompt, verbatim: **"Hey, I have a new task for you. I want you to create a slide deck, which is a Q4 predictions. And I want them in the same format as the Duet doc with the grid and I want to do a let's do nine predictions for Q4 but before that we need to have a where we are now section look at my previous videos and predict what my predictions are"**. Duet adds task "Q4 agent predictions deck", open task, sub thread. Task thread shows its steps: studying the deck format, read past videos, research where agents stand, write 9 predictions, build the deck. States: working, ready for review. The underlined link is the task, the card is the artifact. Result: "this is one shot ... this slide deck is nice". |
| 9 | Thing 6: like Claude Projects, and the local session gap | 13:29 to 16:45 | Shows Claude Projects spinning a local Claude Code session from his phone (prompt at 14:01 to 14:29). "with Claude Duet, you cannot do this. I can ask it to spin off a Claude Code session in the cloud and it can do it". Parallel tasks prompt: **"spin off a new task right now that analyzes the trending topics right now on Twitter. If you use Composio, you should have a GrokBot skill ..."**. |
| 10 | Thing 7: an artifacts channel with a routine | 16:45 to 18:09 | Channel "Artifacts". "you can set up routines that live inside the channel". Show tasks, Scheduled: "artifact recap", runs "9am to 5pm". It resurfaces decks he forgot. |
| 11 | Thing 8: real-time voice | 18:09 to 19:38 | Taps voice: **"Hey buddy, old pal, what's going on? Can you give me just like a one sentence or two sentence summary of that?"** then **"Can you send an email to emily at agentnative.inc giving her this little breakdown, please?"**. Says "Sure" twice, unclear if sent. Cannot mute. "5% as good as Dots" (21:45). |
| 12 | Comparison grid | 19:38 to 20:23 | Duet, Dots, Gemini Spark, GrokBot, Hermes Agent, Instinct, Muse, OpenClaw. No desktop app for Duet. |
| 13 | Approvals | 20:56 to 21:34 | Spoken only: asks before sending a message ("I want slightly less approvals"), payments, signatures, deletion. "I was trying to remove a video from a Notion database, it asked me for approval". Not shown. |
| 14 | Thing 9: negatives | 21:34 to 24:12 | Voice, 3 chat levels, no model picker or effort control, no local Claude Code sessions. Wishlist. |
| 15 | Close | 24:12 to 24:24 | "much more in-depth tutorial as it gets better". |

### His rhythm

- Numbered list (9 things) as the spine; each thing is a feature with one demo. Viewer always knows where they are.
- Tell, then show on a real past artifact, then do one live (beat 8 is the only live build; beats 3, 5, 6 edit decks he already had). Never demos on an empty state.
- Says the seam out loud when he switches phone to web (03:11 "this is real-time synced").
- Prompts are spoken, long, and messy; he keeps them in. That is the ease framing: you do not need a good prompt.
- The honest "I'm not sure how I feel about this one" is a slide in his own deck (08:18). The video's opinion is built into the artifact.

### What works

| Thing | Evidence |
|---|---|
| One live build from prompt to deck, with the task thread's steps visible | Beat 8, 3 minutes. Most-watched creator demo in the set for a reason. |
| The edit loop shown 3 ways | Comment (beat 5), voice from a walk (beat 6), chat (beat 3). Viewers learn the artifact is not final. |
| Routine inside a channel | Beat 10. Only creator to show a user-made scheduled task. |
| Names the 3 chat levels as a problem | Beat 7 and 14. Sets expectations. |

### Weaknesses, our openings

| Weakness | Opening |
|---|---|
| The deck is about Duet itself and about his predictions | Our artifact is for a real audience with a check: the Skool lesson deck, judged against the transcript. |
| "one shot ... nice" is the whole review | Count: slides right, prompts right, links right. |
| Approvals described, not shown | Film one. |
| Routine shown as a list entry, never seen firing | Film the Build 1 refresh on 10-28. |
| 10 hours of use, but no "it came to me" moment | The brief arriving, timestamped. |
| Access hack (DM someone on X) | We have access. Skip. |

---

## C. Their beat / our beat / exact prompt

Target: 063, Tyler makes 3 things with Duet. Builds are specified in `research/2026-10-26-claude-duet.md` section 5. Every UI name below is marked where it came from. Nothing here assumes Hermes on screen.

| # | Their beat | Our beat | Exact prompt or action | Verified? |
|---|---|---|---|---|
| 1 | Peter 00:00 promise list; Riley 00:00 "10 hours, 9 things" | Open on the artifact, not the app. The Channel Pulse dashboard from 10-28 morning, refreshed on its own, timestamp visible. Then: "So I gave Claude Duet three real jobs for my channel, my community, and my repos. Here's what came back." | Screen: Make tab > Channel Pulse (Make tab per H and Riley 03:40). Timestamp from the task thread | Needs the 10-27 setup. First filmable 2026-10-28 |
| 2 | Peter 00:48 onboarding, "already connected" | 30 seconds, Claude Code user framing: what carried over (memory, connectors, Make already has my Cowork and Claude Code artifacts, Brock 04:01) and what did not (local files, local skills, H). | Screen: Duet connections list (Riley 02:42) and claude.ai Settings > Connectors | Connections view label: to verify on Tyler's account |
| 3 | Peter 02:51 to 04:24 channels tour (90 s) | Skip the tour. One channel, "content", made off camera. Say it in one line. | none | n/a |
| 4 | Riley 10:27 live build of a deck from one spoken prompt | Build 3 live: Repo Health sheet. Paste the prompt, open the task thread, show its step list (Riley 12:14), cut to the result. | Prompt in research section 5, Build 3. Screen: Tasks > Active > task thread, "working" then "ready for review" (Peter 02:28, Riley 11:40) | Sheet type in Make "+" menu: Brock 04:45 lists document, presentation, design, dashboard, page; sheet label to verify |
| 5 | Riley 20:56 approvals described, not shown | The Slack DM at the end of Build 3 raises the approval card. Read what it shows: action, destination, content, recipients (S). Approve. Show the DM land in Slack. | Action: tap Approve on the card | Card appearance for Slack send: S says it asks before sending a message; Riley 21:02 confirms. Exact card layout to verify |
| 6 | Peter 09:03 YouTube report from public data, judged by reading | Build 1 shown as built on 10-27: Channel Pulse. Put YouTube Studio or `youtube/analytics/` latest file next to it. Count the rows that match. Say which were wrong. | Prompt in research section 5, Build 1. Screen split: Make > Channel Pulse left, Studio right | GitHub connector reading the private content repo: to verify. Fallback: paste the status.md text and the analytics numbers into the prompt |
| 7 | Peter 10:14 "you can schedule a weekly refresh" (not done) | Show Tasks > Scheduled with the Channel Pulse refresh in it (Peter 02:28 label), then the refreshed artifact from this morning (beat 1 callback). | Action: Tasks > Scheduled > Channel Pulse refresh > view history (Peter 04:53 label) | Whether a user-made refresh appears under Scheduled: Riley 17:06 shows his own "artifact recap" there. Likely yes, to verify |
| 8 | Riley 05:27 to 09:00 edit by comment and by voice | Build 2: the Skool lesson deck. Paste the prompt, come back to the result, then one voice edit from the phone (Riley 07:40 style): "move the prompts onto their own slides and cut the mistakes slide to 3 bullets". Show the sync on web (Riley 03:11 seam). | Prompt in research section 5, Build 2. Voice edit text above | Comment tool on web: Riley 05:43, to verify on Tyler's account. Voice on web: John 02:10 says no voice call on web, so do the voice edit on the phone |
| 9 | Nobody | Judge Build 2 against the transcript: count prompts it quoted right, links it got right. Then say it is a draft and you post it yourself. | Screen: `transcripts/transcript_<id>.txt` next to the deck | n/a |
| 10 | John 06:14 usage is one shared pool | Read the usage meter before Build 2 and after. One number. | Screen: claude.ai usage page (to verify the label) | To verify |
| 11 | Peter 12:08 Uber failure; Riley 21:34 negatives | 45 seconds of what did not work, from the receipts: the wrong column, the missing connector, the approval you did not expect. | none | Fill from the pre-build |
| 12 | Peter 13:54 ranking vs Grok Bot, Muse, Dots | Skip the ranking. One line: "I filmed the same three jobs on Dots last week; that comparison is its own video if you want it. Tell me in the comments." | none | Keeps the Duet vs Dots lane open (research section 6) |

Order on camera: 1 (the morning artifact), 2, 4, 5, 6, 7, 8, 9, 10, 11, 12. Target 13 to 15 minutes, same as 062.

## D. Possible extras the references did not show

| Extra | Source | Status |
|---|---|---|
| `/` skill list and a custom skill from the Claude account showing up in Duet | Peter 06:30 showed `/morning`; whether Tyler's account skills (`~/.claude/skills` are local and will not; skills saved in claude.ai might) | To verify |
| The "learn how I write" skill run on Tyler's Slack and email, then used for the Skool post | Peter 07:26 | To verify the skill exists on Tyler's account |
| Quiet hours | John 10:54 | To verify, settings location unknown |
| Reset memory from app settings; disconnect an app and show it keeps what it learned | S | To verify |
| Pay for something with Link, one-time card, approve in the Link app | L | Off topic for 063 |

## E. Pointer

No `youtube/videos/063-*` package exists yet. When Packager creates it, append under `analysis.md` `## Creator breakdowns`: `research/youtube/creator-breakdowns/2026-10-26-claude-duet.md`.
