# Analysis, video 063: Claude Duet

Built 2026-10-27 from the researcher's two files. Research was not redone; this file picks the spine, records why, and adds the holes filled today. Full field data, fact sheet, and gap table live in the research file and are not copied here.

## Creator breakdowns

`research/youtube/creator-breakdowns/2026-10-26-claude-duet.md` (Peter Yang D-pz8L1orVI 91,399 views 17:25; Riley Brown ZIBI6FiLxgQ 106,416 views 24:24; beat tables with exact prompts; their-beat / our-beat / exact-prompt plan).

Research file: `research/2026-10-26-claude-duet.md` (28 videos, 40-row fact sheet, 6 gaps, 3 builds with prompts, the vs-Dots lane).

Transcripts used: `transcripts/transcript_D-pz8L1orVI.txt`, `transcript_ZIBI6FiLxgQ.txt`, `transcript_jC26BnJseAw.txt`, `transcript_HYb5w4PfPZM.txt`, `transcript_PkrjD2IOCm4.txt`, `transcript_JU0lX7y2Au0.txt`.

## 1. Reference structure (Peter Yang, the closest shape to ours)

| Time | Segment | Purpose |
|---|---|---|
| 0:00 to 0:45 | Promise list: morning brief, YouTube report, sponsor dashboard, kids club; Uber failure; ranking | hook |
| 0:48 to 1:49 | Onboarding, "already connected," 3 suggested tasks | teaching |
| 1:56 to 2:44 | Tasks tab: Active, Up next, Scheduled, Resolved | teaching |
| 2:51 to 4:46 | Channels tour, why it is a separate app | teaching |
| 4:46 to 5:42 | The scheduled check-in, history view, "every three hours 9 to 10" | demo |
| 5:47 to 6:23 | Sponsor | CTA |
| 6:24 to 7:20 | `/` skills, `/morning` renders the brief as HTML | demo |
| 7:26 to 9:03 | "Learn how I write," email triage artifact with comments | demo |
| 9:03 to 10:14 | YouTube report from public data, one-line prompt, reads 2 insights | demo |
| 10:14 to 11:16 | Sponsor revenue dashboard (mock data, says so) | demo |
| 11:16 to 12:08 | Kids club artifact, "too text heavy" | demo |
| 12:08 to 13:54 | Uber wall, can't see browser, can't see local skills | teaching |
| 13:54 to 16:46 | Ranking vs Grok Bot, Muse, Dots | opinion |
| 16:46 to 17:25 | Close, prediction | CTA |

Riley Brown's shape is a numbered "9 things" list with one live build (10:27 to 13:29) and the edit loop shown three ways (comment 5:27, voice 6:52, chat 1:13). Both tables in the breakdown file.

## 2. What works in the references

| Thing | Where | Why it matters for us |
|---|---|---|
| Artifacts from prompts under 20 words | Peter 9:03, 10:14, 11:16 | The bar is low; our prompts can be long and specific and still read as doable |
| The scheduled check-in history | Peter 4:46 | Only creator to show the proactive loop as a screen; our step 5 does the same on a user-made task |
| One live build with the task thread's step list visible | Riley 10:27 to 13:29 | Our step 3 copies this: paste, open the task, show the steps, leave it running |
| The edit loop from a phone | Riley 6:52 | Our step 9; the only beat where Tyler is away from the desk |
| Honest failure | Peter 12:08 Uber wall | Our step 12 is built from real pre-build failures, not a wishlist |
| Names every label while clicking | Peter throughout | Those labels are our "Confirm on your account" list |

## 3. Weaknesses in the references (our openings)

| Weakness | Who | Our beat |
|---|---|---|
| Judges by reading the output, never checks it against anything | Peter 9:24 ("it found personal AI agent videos are my breakout topic"), Riley 13:18 ("this is nice"), Brock 6:01 ("looks really solid"), How I AI 13:08 ("good not great") | Steps 4, 6, 8: artifact next to Studio, github.com, the transcript, with a count |
| Sponsor dashboard is mock data | Peter 10:31 | All three of ours are real accounts |
| "You can schedule a refresh" said, never done | Peter 11:10 | Step 1 and 5: the refresh in the Scheduled list and its history, fired unattended |
| Approvals described, never shown | Riley 20:56 to 21:34 | Step 7: the card, read aloud, approved, the message landing |
| Brief triggered by hand with `/morning` | Peter 6:46 | We do not use the brief at all; the unattended artifact is the dashboard refresh, which is more checkable |
| Tour first (5 minutes), artifacts second | Peter beats 2 to 6 | Zero tour. One channel made off camera, one line about it |
| Audience is generic busy professional | both | Step 2 is written for someone already in Claude Code: what carries over, what does not |

## 4. Target audience and level

Claude Code users and people already paying for Claude Pro or Max who want to know whether Duet does anything their current setup does not. Assumed level: comfortable with connectors, GitHub, and reading a spreadsheet. Nothing is explained from zero. The transfer test from tyler-voice.md: the dashboard, the repo sheet, and the deck-from-a-transcript all map to anyone's repetitive work (a status page, an inventory of things you own, a summary of a long document); YouTube and Skool are the setting, not the topic.

## 5. Which build is the spine, and why

The researcher proposed three builds. All three are in the video, but one has to carry the hook, the title's promise, and the longest on-camera check.

| Build | What it proves | Checkable against | Risk | On-camera time |
|---|---|---|---|---|
| 1 Channel Pulse dashboard | The unattended loop: a scheduled refresh that fires while Tyler is asleep (gap 3 and 4, 0 of 6 filmed it). The first thing in the help center's "bigger results" list. | YouTube Studio, row by row, 10 rows | Needs one overnight before the hook is true. GitHub connector may not reach the private repo (fallback: paste status.md text). Dashboard may not show a refresh time (fallback: the task history time). | 2:15 across steps 1, 4, 5 |
| 2 Repo Health sheet | The live build and the approval card (gap 2, 0 of 6 filmed it). Forced by the "send me the top 3" follow-up. | github.com, 3 spot checks | Sheet artifact type unconfirmed. Slack send may be blocked; email fallback. Stars-gained column will likely be wrong, which is a good moment. | 2:55 across steps 3, 6, 7 |
| 3 Skool lesson deck | The deck, Duet's own pitch, judged against a transcript with a prompt-by-prompt count (gap 1). Plus the phone voice edit. | The transcript file, prompt by prompt | Depends on the GitHub connector for the transcript (fallback: paste it). Easiest build, least novel. | 2:15 across steps 8, 9 |

**Spine: Build 1, Channel Pulse.** Reasons:

1. It is the only one of the three that produces a "this showed up on its own" moment, and that moment is the hook. Nobody in 28 videos has filmed Duet doing anything unattended on a user-made task. The brief would also do it, but a brief about Tyler's inbox is not checkable on camera and would mean blurring half the screen. A dashboard about public YouTube numbers is checkable row by row with Studio open next to it.
2. It is the most checkable. Ten rows, ten numbers, a count. That count becomes Hook B, the thumbnail text, and the receipts table's first row.
3. It is the one that generalises. A status page that rebuilds itself every morning is a job anyone has. A repo sheet is a developer job, a lesson deck is a creator job.

Build 2 gets the live build and the approval card, because those are the two beats that need to happen on camera, and a sheet is the fastest build to start live (10 to 20 min per the pre-build). Build 3 gets the deck-vs-transcript check and the phone edit, because the deck is the artifact Anthropic leads with and the prompt-quoting check is a clean number.

Filming order differs from the researcher's (3, 2, 1) because the researcher ordered by setup speed and the script orders by story: open on the unattended artifact, start the live job, check the first artifact while the live one runs, come back to it, force the card, then the deck. Pre-build order still follows the researcher: Build 1 first on Day 0 because it needs the overnight.

Runtime: 12:00 target, 13:00 ceiling, inside the 10 to 13 the card asked for. Step 9 (voice edit) and step 5 (the schedule) are the cuts if it runs long.

## 6. What this video adds that the field does not

| Gap (research section 3) | Our beat | Status |
|---|---|---|
| 1 Deliverable checked against the source on a real business | Steps 4, 6, 8 with counts | in script |
| 2 Approval card firing | Step 7 | in script, path to verify in PRE-BUILD 6 |
| 3 Something arriving on its own, timestamped | Step 1 (the refresh), step 5 (its history) | in script, first filmable 10-28 |
| 4 Scheduled refresh of a dashboard firing | Same as 3 | in script |
| 5 Usage cost of one job | Step 10 | in script, label to verify |
| 6 Claude Code users: what carries over | Step 2 | in script |

## 7. The Duet vs Dots alternative (not the 063 plan)

The researcher found the "Claude Duet vs Dots" search open: 3 videos, 469 / 11 / 0 views, none of them puts the same prompt into both. Tyler filmed 062 on 2026-10-26 with 3 jobs on Dots (morning content brief, repo check, Skool prep), and 063's three jobs map onto them one to one: Channel Pulse is the brief turned into an artifact, Repo Health is the repo check turned into a sheet, the Skool deck is the Skool prep turned into a deck.

Why it is not 063: the Hermes half of 062 was cut because the video stopped being about making something and became a scorecard, and Tyler corrected it to one tool on screen. The same risk applies here. Also, the Dots videos that got views on a versus frame (Nate Herk 492k vs Muse, Jack Roberts 109k vs GrokBot) came from channels with 100k+ baselines.

How to keep it alive: step 12 has one line ("I ran the same three jobs on Dots last week; that comparison is its own video if you want it") and asks for comments. If the comments ask, the third video is "Same 3 jobs, Duet vs Dots, receipts side by side," built from 062's `receipts.md` and 063's `receipts.md` with no new filming beyond a camera close. Recommended only after 062 publishes and 063 is in the can. Title candidates for that video are not written here on purpose; it is a separate package.

## 8. Research added today (beyond the researcher's file)

Searches run 2026-10-27: "Claude Duet GitHub connector repositories", "Claude Duet Make tab spreadsheet dashboard scheduled refresh", "site:support.claude.com Claude Duet", "Claude Duet approval before sending Slack message review".

| Finding | Effect on the package |
|---|---|
| Claude's GitHub integration help page: private repos need the GitHub App grant; if a valid URL fails it is "most likely" a private repo without access. Two open issues on anthropics/claude-code (#68517, #71542) report the connector linking but failing to read content, public and private. | PRE-BUILD 2 is a hard gate with a paste-in fallback for Jobs 1 and 3; step 2 has a line for it. |
| Help center "Get started with Claude Duet" (re-fetched): finished work "appears in the Make tab"; named result types are research brief, financial model, slide deck, dashboard. No spreadsheet named. | Confirm #7: the sheet label is to verify; the script has a line if it comes back as a document. |
| Third-party Duet pages (duetcases.com) note the 5:30am dashboard refresh in Anthropic's product video is a scripted demo and not documented as a requestable feature. Peter Yang says you can schedule one (11:10); Riley shows a user-made routine under Scheduled (17:06). | The refresh is the single biggest risk in the hook. PRE-BUILD 3 requires it to have fired; filming-guide step 1 has the fallback open. P1 asks Duet to print its refresh time on the page. |
| Safety post (re-fetched): before sending "a potentially sensitive message," paying, or deleting, it shows action, destination, content, every recipient. "Your own request counts as consent" for some sends. | A DM to yourself may NOT raise a card, since it is your own request to your own address. PRE-BUILD 6 tests this off camera first; if no card appears, step 7 says so plainly, and Hook C is dropped. |
| Help center: Slack "works with limits in Claude Duet," limits unspecified. | Email is the fallback send path in Prompt S. |

Nothing above was verified on Tyler's account. Every claim in the script that depends on it is bracketed.

## 9. Packaging checks

| Check | Result |
|---|---|
| Head term demand | Claude Duet: 28 videos in 6 days, 12 over 50k. Passes. Launch term, so ship this week. |
| Money in title | none |
| "Explained" | none |
| Em dashes | none in any file (grep before review) |
| "I" in title | attached to an external subject and a stake ("I Gave Claude Duet 3 Real Jobs"), the allowed shape |
| Duration | 12:00 target, 13:00 ceiling, inside the 10 to 35 band and under 20 |
| Cold open | working artifact on screen inside 10 seconds (rule widened 2026-08-19), number in the first sentence for Hook B |
| Thumbnail | split with a count (the before/after the rules say is missing from the channel), one logo, face absent or reacting |
| Spacing | 062 (Dots) is in editing. If both publish inside four days they share the "3 real jobs" promise. Space them a week or more, or publish 063 first since its term is fresher. |
| Hermes on screen | none |

## Sources

- https://claude.com/product/claude-duet
- https://claude.com/resources/articles/claude-duet
- https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
- https://support.claude.com/en/articles/17631495
- https://support.claude.com/en/articles/17666484
- https://support.claude.com/en/articles/17666489
- https://support.claude.com/en/articles/10167454-use-the-github-integration
- https://github.com/anthropics/claude-code/issues/71542
- https://github.com/anthropics/claude-code/issues/68517
- https://claude.com/docs/connectors/slack
- https://duetcases.com/data/dashboard-forecast
- https://duetcases.com/research/slide-deck
- https://www.eesel.ai/blog/claude-duet-review
- https://www.youtube.com/watch?v=D-pz8L1orVI (Peter Yang)
- https://www.youtube.com/watch?v=ZIBI6FiLxgQ (Riley Brown)
- https://www.youtube.com/watch?v=jC26BnJseAw (Alex Finn)
- https://www.youtube.com/watch?v=HYb5w4PfPZM (How I AI)
- https://www.youtube.com/watch?v=PkrjD2IOCm4 (Brock Mesarich live test)
- https://www.youtube.com/watch?v=JU0lX7y2Au0 (John Aspinall)
- `research/2026-10-26-claude-duet.md`, `research/2026-10-26-claude-duet.json`
- `research/youtube/creator-breakdowns/2026-10-26-claude-duet.md`
- `youtube/videos/062-openai-dots/script.md` (format template)
