# Creator breakdown: Metics Media, Hostinger Hermes Agent Tutorial - Full VPS Setup Guide

Reference: https://youtube.com/watch?v=0ZnR7fqD5rM. 21,303 views, 31:19, uploaded 2026-09-07 (yt-search pull 2026-09-21).
Transcript: `~/content/transcripts/transcript_0ZnR7fqD5rM.txt` (mlx-whisper, 501 lines).
Target video: Create Your First 24/7 AI Agent (Hostinger VPS), no package folder yet.
Second reference read alongside: Liqui AI `transcript_6L4v-6ztQXE.txt` (9,700 views, 10:26, no live demo).

## 1. Beat table

| # | Beat | Time | What he does on screen |
|---|---|---|---|
| 1 | Hook | 0:00-0:55 | Cold open on the payoff: "messages your phone on Telegram when it finds something worth knowing." Frame: "you're hiring your first AI employee. We'll give it a place to work, a brain, a phone number, some training, and a schedule." |
| 2 | Buy the server | 0:55-3:29 | Affiliate link, "click the choose plan button", KVM1 ("runs one agent comfortably... upgrade later without reinstalling"), coupon caveat on 1-month plans, register, pay, "keep the username as Hermes", eye icon for the admin password, "click deploy" |
| 3 | Deploy template | 3:29-5:08 | Manual path: "VPS > Manage > Docker Manager > Compose > one-click Deploy > search Hermes > Hermes Agent" |
| 4 | Dashboard tour | 5:08-6:38 | Names the four pages: "Models is the brain... Cron is the schedule, and this is the page that lets it work while you're asleep." Shows Chat failing with no model. Gateway "connects your agent to the outside world" |
| 5 | Brain | 6:38-10:30 | OpenRouter signup, "$5 for testing", spend limit "$10... resets weekly", paste key in dashboard, Models > Main Model > Change > DeepSeek V4 Flash, reload, "hello" test. Mentions Nous subscription "from about $20 a month" as the alternative |
| 6 | Phone | 10:38-13:28 | Channels > Telegram > "Create with QR", phone scan, "save and restart", gateway stopped then running, tap Start, first message, `/sethome` ("that's where Hermes will deliver your cron job results") |
| 7 | First job | 13:30-15:24 | Desktop Telegram. Prompt 1: "what tools do you have?" Prompt 2: "research the top three standing desks and give me a one paragraph comparison." Notes it asks permission before touching files |
| 8 | Desktop app | 15:24-19:38 | Download, 11-step installer, "I'll choose a provider later", Settings (Cmd-,) > Gateway > Remote Gateway, paste URL, sign in, "save and reconnect". Test: "what was my first ever message to you?" Cmd-Shift-H HUD mode |
| 9 | Memory | 19:46-21:38 | Prompt: "write a short post about productivity habits for remote workers." Correction: "too wordy. I prefer short, punchy sentences, three paragraphs max, no headings or bullets. Save that as a preference." Same session: "now write one about managing focus while working from home." New session (Cmd-N): "write me a short post about the best European travel destinations for plenty of beach time." Style holds |
| 10 | Capabilities | 21:38-23:12 | Capabilities page = Skills + Tools + MCP in the app, separate pages on the web. "learned" label. Skills Hub, searches "Calendar", Google Workspace already built in |
| 11 | The schedule | 23:12-25:06 | One prompt in a new session: "Watch YouTube for AI productivity trends. Build yourself a reusable skill for the check. Keep track of what you've already shown me. Schedule it every few hours and message me here only when there's something new." Agent installs a dependency, writes the skill, schedules every 4 hours. Shows Scheduled Jobs page (interval, next run, prompt, pause, trigger). Shows one Telegram result: "Eight new videos clear the threshold" |
| 12 | Cost | 25:06-27:20 | OpenRouter Activity: 105 requests, ~4M tokens, 13 cents. "38,000 tokens every time I say anything." Cache explains it. "$5 covers somewhere around 4,000 messages." Switches to Opus 5 in the model picker, `/model` in Telegram |
| 13 | Troubleshooting | 27:20-29:06 | Logs page and filters, Restart Gateway, Docker Manager restart ("the bigger hammer"), Web Console `hermes doctor` |
| 14 | Extras + CTA | 29:06-31:15 | Sub-agents prompt: "plan me three days in Lisbon. One sub-agent on which neighborhood to stay in, one on where to eat, one on a day trip worth taking, and one on getting around, then give me a single itinerary." Channels, profiles, OpenClaw import prompt. Homework: "Ask your agent what it could take off your plate." Affiliate link again |

## 2. His rhythm

| Technique | Where | Note |
|---|---|---|
| Employee metaphor as the table of contents | 0:41, 19:38 | "place to work, brain, phone number, training, schedule." He repeats it at 19:38 as a progress check. Viewers always know where they are |
| Promise the schedule demo early, pay it at 23:12 | 5:46, 23:14 | "Here's the demo I promised earlier" |
| Say the seam | 21:55, 27:26 | Names when the app and the web dashboard disagree ("The app calls this page Capabilities... the browser dashboard separates") and when he moves back to the web ("troubleshooting is a server job") |
| Cost as a reveal, not a disclaimer | 25:06 | Real Activity page, real numbers, then explains cache |
| One correction, then a new session | 19:46 | The memory beat is a 3-prompt test: correct, same session, fresh session |
| Ease framing on the payoff | 23:29 | "It takes just one message, so watch the whole loop" |

## 3. What works

| Item | Count or quote |
|---|---|
| Every click narrated with the menu path | 14 beats, all click-level |
| Real numbers on cost | 105 requests, 13 cents, 4M tokens |
| The cron prompt is genuinely one message and the agent builds the skill itself | 23:36 |
| Spend limit before the first message | 7:52 |
| Troubleshooting section | 3 tiers: gateway, container, `hermes doctor` |

## 4. Weaknesses (our openings)

| Weakness | Evidence | Our opening |
|---|---|---|
| The 24/7 claim is never proven | 1 sample result shown at 24:35, filmed in the same session. No second run, no time gap | Film setup, close the laptop, cut to the next morning with a day of runs on the phone |
| The job is generic | "AI productivity trends" watcher, a Telegram paragraph | A job that leaves an artifact: a file committed, a report in the repo, a PR |
| Payoff arrives at 23:12 of 31:19 | 74% of runtime before the schedule | Job on screen by minute 8 |
| 2:34 on buying a plan, coupon rules, billing address | 0:55-3:29 | Under 1 minute, cut the coupon talk |
| Audience is "no coding, no terminal" beginners | 0:17 | Claude Code users who watched 057. They have skills, CLAUDE.md, a repo. The VPS agent gets those imported |
| Telegram only; Slack mentioned as a name | 10:59 | Slack, matching 057 and the bot roster |
| Desktop app is a tour (HUD mode, Cmd-N) | 15:24-19:38, 4 minutes | Desktop app is the proof device: connect to the VPS the next morning, read the same sessions |
| No file or repo work on the VPS | none | Give the VPS agent the content repo or a scratch repo so the job writes something |
| Sub-agents demo is a travel itinerary | 29:15 | Skip or make it part of the job |

## 5. His beat / our beat / exact prompt

| # | His beat | Our beat | Exact prompt or command | Status |
|---|---|---|---|---|
| 1 | Employee metaphor hook | Cold open on the next-morning phone: Slack thread with 3 timestamped runs, "I was asleep for all of these" | none | to film last |
| 2 | Buy KVM1, coupon, register | Hostinger Hermes Agent page, pick plan, deploy. Say the price once, keep it off the title | none | verify plan name and price before filming |
| 3 | Docker Manager path | Same path, one pass, no detours | Docker Manager > Compose > one-click Deploy > Hermes Agent | verify template label |
| 4 | Dashboard tour | Skip the tour. Models and Gateway only | none | |
| 5 | OpenRouter, $5, spend cap | Same, 60 seconds. Keep the spend cap beat, it is good | OpenRouter > API keys > Edit > limit | to verify on Tyler's OpenRouter |
| 6 | Telegram QR | Slack, same app Coder posts to in 057 | Channels > Slack, paste bot token | reuse 057 setup, verified on the Mac, to verify on VPS |
| 7 | "what tools do you have?" | Import what the viewer already has | `hermes import-agent claude-code` (from the 09-16 research: 55 items on this Mac, 0 competitor videos show it) | dry-run verified on the Mac 09-16, not on a VPS |
| 8 | Desktop app tour | Hold until the proof beat | Settings > Gateway > Remote Gateway | to verify |
| 9 | Memory: "too wordy, save as a preference" | Skip. 057 covered memory | | |
| 10 | Capabilities page | Skip | | |
| 11 | One-prompt cron, YouTube watcher | The job. One prompt, then show the job it wrote, then trigger it once by hand so the viewer sees a real run before the cut | "Every weekday at 7:45am pull the latest video's views and comments from my channel, write them to research/daily/YYYY-MM-DD.md in the content repo, and post a 3 line summary in #content. If nothing changed say so in one line." Then: `hermes cron list` and `hermes cron run "<name>"` | to build; needs the repo on the VPS and YouTube API creds, or use a no-auth job (yt-search on a term) as the fallback |
| 12 | Cost reveal | Keep. Show the OpenRouter Activity page after 24h, real request count and cents | OpenRouter > Activity | after the proof cut |
| 13 | Troubleshooting | 30 seconds: Logs, Restart Gateway | Logs, Restart Gateway | |
| 14 | Sub-agents, OpenClaw import | The proof cut. Next morning, phone first, then the desktop app connecting to the VPS: same sessions, laptop was shut | Settings > Gateway > Remote Gateway > paste URL | to film the next day |

Fallback job if the YouTube API creds are not worth setting up on camera: "Every morning at 7 search YouTube for hermes agent, keep a list of what you already sent me, and post only new videos over 10K views to #content." No auth, same shape as his watcher but with a threshold and a memory file.

## 6. Possible extras (we have, he did not show)

| Extra | Note |
|---|---|
| `hermes import-agent claude-code` | 0 of 10 Hermes transcripts in the 09-16 research mention it |
| A second profile on the VPS (`-p coder`) | 057's roster, shown running remotely |
| Bot-to-bot handoff over the VPS gateway | only if verified, 057 STATE.md says the chain is unverified end to end |
| Cost after 24h of real runs, not one session | his 13 cents was one filming session |

## 7. Timing plan (target 18 to 20 min)

| Section | Minutes |
|---|---|
| Cold open, next-morning phone | 0:45 |
| Deploy on Hostinger | 3:00 |
| Brain + Slack | 3:00 |
| Import Claude Code setup | 2:00 |
| The job: prompt, cron list, hand-run | 5:00 |
| Cut: next morning, phone, desktop app remote | 3:00 |
| Cost + troubleshooting | 1:30 |
| Close | 0:45 |
