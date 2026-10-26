# OpenAI Dots: research for video 062

Date: 2026-10-24. Redo of the 9/30 card (t_1cbc6611), which was written from memory. Everything below is from yt-dlp data, 7 local transcripts, or OpenAI's own pages. Anything I could not confirm is marked.

Angle under test: Tyler's real Dot running next to what his Hermes setup already does. Show off what we can do, not what OpenAI announced.

## 1. YouTube field, last 30 days

4 searches, 35 unique videos, 0 Shorts in any search (Shorts cutoff 60s). Views per hour = total views / hours since the upload date (midnight) as of 2026-10-24 14:30 ET. Rough; it flatters newer uploads.

Raw yt-dlp output: `2026-10-24-openai-dots.json`, `2026-10-24-chatgpt-dots.json`, `2026-10-24-dots-vs-claude-code.json`, `2026-10-24-openai-devday-2026-agents.json` (+ matching `.md` and `-thumbnails/`). The yt-search table for "OpenAI Dots" is kept at `2026-10-24-openai-dots-raw-search.md`.

### Top 20 by views (all 4 searches merged)

| # | Title | Channel | Views | Views/hr | Dur | Uploaded | Transcript |
|---|---|---|---:|---:|---|---|---|
| 1 | [AI Secretary Revolution with dots] New ChatGPT Features (Japanese) | NAKATA UNIVERSITY | 1,242,365 | 6,808 | 41:21 | 2026-10-17 | no |
| 2 | OpenAI Dots Failed Live on Stage | SAMTIME | 1,030,970 | 1,900 | 4:58 | 2026-10-02 | yes |
| 3 | Introducing dots, always-on agents built to handle everything | OpenAI | 750,967 | 1,222 | 2:28 | 2026-09-29 | no |
| 4 | I Tested OpenAI's Dots vs. Meta's Muse | Nate Herk | 492,800 | 835 | 16:30 | 2026-09-30 | yes |
| 5 | ChatGPT Dots Finally Clicked When I Learned This | Paul J Lipsky | 288,685 | 584 | 12:34 | 2026-10-04 | yes |
| 6 | ChatGPT "dots" Breaking News (Japanese) | Leo Tohyama | 272,078 | 480 | 22:16 | 2026-10-01 | no |
| 7 | OpenAI's Dots lead on the future of ChatGPT | Sources Podcast / Alex Heath | 244,983 | 433 | 45:29 | 2026-10-01 | no |
| 8 | I Tested OpenAI's New Personal Assistant Agent: DOTS | Futurepedia | 226,145 | 368 | 11:03 | 2026-09-29 | yes |
| 9 | The Biggest ChatGPT Update Yet: Meet dots | Skill Leap AI | 201,149 | 327 | 11:28 | 2026-09-29 | yes |
| 10 | Meet the NEW CHATGPT AGENT: DOTS (Portuguese) | Rafa Voss | 174,690 | 308 | 15:10 | 2026-10-01 | no |
| 11 | How ChatGPT Dots Can Change Your Life in 4 Minutes | The AI Advantage | 155,371 | 286 | 4:46 | 2026-10-02 | no |
| 12 | OpenAI's Head of ChatGPT: new era of AI (again), Tibo Sottiaux | Lenny's Podcast | 153,499 | 310 | 37:23 | 2026-10-04 | no |
| 13 | Set up your dot in the ChatGPT mobile app | OpenAI | 136,274 | 364 | 2:46 | 2026-10-09 | no |
| 14 | Introducing OpenDots, open-source alternative | CopilotKit | 135,835 | 240 | 1:07 | 2026-10-01 | no |
| 15 | ChatGPT Dots is INCREDIBLE (but only if you use it the right way) | Alex Finn | 131,255 | 232 | 19:18 | 2026-10-01 | no |
| 16 | ChatGPT Dots Is WAY More Powerful Than You Think | Riley Brown | 128,581 | 343 | 25:56 | 2026-10-09 | yes |
| 17 | OpenAI dots deep test (Chinese) | AI超元域 | 126,972 | 215 | 12:15 | 2026-09-30 | no |
| 18 | OpenAI Dots: Openclaw Inside ChatGPT. Full Review (Russian) | Продуктивный Совет | 109,897 | 186 | 25:39 | 2026-09-30 | no |
| 19 | I Tested ChatGPT Dot vs GrokBot (Not Even Close) | Jack Roberts | 109,475 | 185 | 20:47 | 2026-09-30 | no |
| 20 | I tested OpenAI's new personal assistant agent: DOTS (Spanish) | Eli Rigobeli | 106,123 | 180 | 26:44 | 2026-09-30 | no |

Also relevant, lower views:

| Title | Channel | Views | Views/hr | Dur | Uploaded | Transcript |
|---|---|---:|---:|---|---|---|
| Should You Pay $100 A Month For Dots When Muse Has A Free Version? | Nate B Jones | 76,978 | 149 | 38:31 | 2026-10-03 | no |
| OpenAI Dots vs Meta Muse: One Is Built for Work | Vaibhav Sisinty | 40,996 | 474 | 13:24 | 2026-10-21 | no |
| ChatGPT Dots vs Claude vs Grok: Everyday Tasks | Neo Marlin | 2,398 | 6 | 4:44 | 2026-10-07 | no |
| I Tested OpenAI Dots vs Claude Code on the Same Job. Who Won? | Build Alone | 522 | 1 | 5:32 | 2026-10-06 | yes |

### Read of the field

| Signal | Count |
|---|---|
| Videos found across 4 searches | 35 |
| Shorts found | 0 |
| Videos over 100k views | 20 |
| Of those, English creator demos (not OpenAI, not podcasts, not news) | 9 |
| Videos comparing Dots to Meta Muse | 5 |
| Videos comparing Dots to GrokBot | 2 |
| Videos comparing Dots to Claude Code | 2 (522 and 2,398 views) |
| Videos comparing Dots to a self-hosted agent (Hermes, OpenClaw, cron) | 0 in English. Nate Herk mentions Hermes/OpenClaw once, at 03:32, as a reference point for Muse's soul file. The Russian title says "Openclaw inside ChatGPT"; not transcribed. |
| "DevDay 2026 agents" search | 7 videos, top one 4,953 views. Dead query. |

The vs-Claude-Code lane is empty. Build Alone did the closest thing (a 6am news job on both) and got 522 views in 18 days. That is a channel size problem, not a topic problem; the comparison videos that did get views (Muse, GrokBot) all came from channels with 100k+ baselines.

### Title patterns (top 20)

| Pattern | Count | Examples |
|---|---|---|
| "I Tested" / "I Tried" | 6 | Nate Herk, Futurepedia, Eli Rigobeli, Jack Roberts, Mark Kashef, Leslie Samuel |
| X vs Y | 6 | Muse x4, GrokBot x1, Claude x1 |
| "Finally clicked" / "right way" / "more powerful than you think" (reframe) | 3 | Lipsky, Finn, Brown |
| Failure angle | 1 | SAMTIME, 1.03M views on a 5 min video |
| Number in title | 1 | "in 4 Minutes" |

Tyler's formula (number + outcome + tool) appears in 1 of the top 20. The field is running on tool-name recognition plus a reaction word.

### Thumbnails (looked at the files, not guessed)

| Video | Face | Text | Elements |
|---|---|---|---|
| Nate Herk, 492k | Yes, smiling, centered at laptop | "Tested." | 5 plush dot characters floating on both sides, MacBook, glow |
| Lipsky, 288k | Yes, smiling, pointing | "I Get It Now" | laptop showing the "dots" wordmark and 12 plush dots, yellow arrow |
| Riley Brown, 128k | Yes, neutral, close | "I'M OBSESSED" (yellow) | phone with "dots" wordmark and waveform, 4 plush dots |
| SAMTIME, 1.03M | Yes, laughing | "It failed" | one teal plush dot with sparkle eyes, white background |
| Build Alone, 522 | No | "WHO WINS? OPENAI DOTS vs CLAUDE CODE / from $100 / from $20" | two logos, price tags |

4 of 5 use OpenAI's plush dot characters. 4 of 5 have a face. 0 of 5 show a real screen with real work. That is the open thumbnail: Tyler's face, his actual Dot's Activity View or Slack thread on one side, his Hermes Slack on the other, 2 to 3 words.

## 2. Transcripts fetched

Local mlx-whisper, 7 videos, 2 min 52 s total wall time.

| Video | File | Lines |
|---|---|---:|
| Nate Herk, Dots vs Muse | `transcripts/transcript_BvvfZKKz4Yo.txt` | 279 |
| Paul J Lipsky, Finally Clicked | `transcripts/transcript_9RYDaLnB6ec.txt` | 195 |
| Build Alone, Dots vs Claude Code | `transcripts/transcript_SfVfgzhOd9c.txt` | 100 |
| Riley Brown, 9 tips | `transcripts/transcript_WXhOxfPECnM.txt` | 480 |
| Futurepedia, I Tested DOTS | `transcripts/transcript_V_1Vn2WfpEY.txt` | 189 |
| SAMTIME, Failed Live | `transcripts/transcript_a_jihWpd8cc.txt` | 93 |
| Skill Leap AI, Meet dots | `transcripts/transcript_gfh6l3DxHK0.txt` | 190 |

Not transcribed: NAKATA (Japanese, 41 min, 1.24M views). It is the biggest video in the set but a Japanese-language explainer; not useful as a beat reference for an English demo video.

## 3. Fact check of the 9/30 script

Sources read in full on 2026-10-24:

- A: https://openai.com/index/introducing-dots/ (Sep 29, 2026)
- B: https://openai.com/index/how-we-build-safety-security-and-privacy-into-dots/ (Sep 29, 2026)
- C: https://learn.chatgpt.com/docs/dots (Meet dots)
- D: https://learn.chatgpt.com/docs/dots/controls
- E: https://learn.chatgpt.com/docs/dots/tasks-and-memory
- F: https://help.openai.com/en/articles/20001530 (Getting started with your dot, updated 2 days before 10/24)
- G: https://help.openai.com/en/articles/20001529 (Dots privacy, security, and safety FAQs)
- H: https://help.openai.com/en/articles/9793128 (About ChatGPT Pro tiers)
- I: https://learn.chatgpt.com/docs/pricing

| Claim in 9/30 script | Verdict | Source |
|---|---|---|
| Powered by GPT-6 Astra | Confirmed | A, C, F |
| Each Dot gets its own virtual computer and browser in the cloud | Confirmed. "their own cloud computer, their own browser" | A, C |
| Connects to 4,000+ apps via plugins | Confirmed as OpenAI's number: "readily connect to over 4,000 apps" | A |
| Slack and Teams channels | Confirmed. Texting is a limited US Pro beta via a third party; dot cannot initiate calls at launch; no standalone email address at launch | A, F |
| Continuous loop Goal -> Action -> Review -> Refine | Not found. OpenAI's wording: "tracks progress, works out what needs to happen next, and follows through as things change"; "can decide when to pause and wake up" | C, E |
| Learns preferences through feedback over time | Confirmed | A, C |
| Proactive research is read-only and runs in the background | Confirmed. Enforced in code: cannot send messages, change app content, or control a browser or computer | B, E, G |
| Custom Rules: allow / require approval / block | Confirmed, with the real labels: Take action without asking; Take action when you say so (docs) or if pre-approved (help center); Ask before taking action; Hand off to you | D, F |
| Auto-review checks sensitive actions | Confirmed. Separate system, runs before actions that affect accounts or share info, cannot be turned off by the dot or by Custom Rules | B, D, G |
| Password changes always stay with the user | Confirmed. Also money transfers. Deleting data, installing software, granting new access need approval each time | B, G |
| Activity View shows everything a Dot does | Confirmed with a caveat: desktop app only. Profile > Activity shows In progress / Scheduled / Completed and delegated tasks. Help center: you cannot view or edit individual dot memories | B, D, F, G |
| Dot watching a Slack channel for bugs, then fix -> PR | Confirmed as OpenAI's own example ("A bug appears in Slack, and dots immediately start investigating"; event monitoring in E). Adding it to a channel does not start monitoring; you must ask | A, C, E |
| "Self-managing digital employee" / enterprise specialist dots | Confirmed as a preview only: "focused enterprise pilots", plus Microsoft Agent 365 integration | A |
| Price | Not in the 9/30 script. Facts: first dot included at no extra cost on Pro ($100, $200, $500 tiers) and Business Premium; Enterprise beta off by default. Not on Free, Go ($8), Plus ($20), or standard Business. Pro users must be 18+ and outside EEA, UK, Switzerland | A, C, F, H, I |
| Usage limits | Conversations with the dot do not count toward ChatGPT limits. Tasks it starts in Work or Codex do count. "Allowance for deeper work, with extended limits for the first month after launch." No number published | A, C, F |
| More than one dot | Not yet. "Today, you can start with your primary dot." More dots and speed/volume scaling are "in the future" | A, F |
| Mobile | Can create a dot on mobile per C; F says you cannot currently create on mobile. Docs disagree with each other. Mobile web unsupported in both | C, F |
| Local computer access | Confirmed, off by default, one computer at a time, ChatGPT app must be open. Separate from Codex computer access and Work Sync | C, F |
| Reset deletes the dot | Confirmed: conversations, saved memories, scheduled tasks. Disconnecting a plugin does not delete what it already learned | F, G |

Price for Tyler on camera: he is on Pro. Which tier he paid for on 10/24 is not in any file I can read; he states it.

## 4. What the field covered, and did not

Answers to the three questions on the card, from the 7 transcripts:

| Question | Answer | Where |
|---|---|---|
| Did anyone show a Dot doing real work on their own accounts? | Yes, 4 of 7. Lipsky: dot flagged a hotel billing issue and a sponsor payment on its own (02:41, 03:11), then took 3 voice-assigned jobs (07:12 to 09:46). Riley Brown: voice call reads his Slack and sends a team message (03:10 to 03:52), spins up a Codex session that ships a feature (05:28 to 08:48), sends Amazon links by email to an assistant (12:11 to 13:11). Skill Leap: 3 custom rules typed, dot finds a pricing mismatch across docs and rewrites 3 social drafts (08:21 to 09:14). Build Alone: 6am news job posted on time (01:46). | transcripts above |
| Did anyone compare a Dot to a self-hosted agent? | 1 of 7, barely. Build Alone vs a Claude Code routine, 5:32 long, 522 views, no screen of either agent working, just the output. Nate Herk names Hermes and OpenClaw once (03:32) as "memory and soul files" context. Riley Brown credits OpenClaw for the heartbeat idea (21:31). Nobody put a Dot next to Hermes, OpenClaw, or Claude Code + cron on screen. | SfVfgzhOd9c, BvvfZKKz4Yo, WXhOxfPECnM |
| Did anyone show the Activity View or a guardrail firing? | Activity View: nobody opened it by name. Nate Herk showed "recent activity" and complained he could not find Scheduled (11:32 to 12:07). Riley Brown showed the Schedule tab with a dot dropdown (20:09). Guardrail firing: nobody. Skill Leap set 3 custom rules and the dot "asked for my okay" (08:37) but no blocked action on screen. Build Alone described the 4 rule levels in words (03:44). Lipsky was told to keep sensitive things out of the voice call and complied; not a system guardrail. | 9RYDaLnB6ec, gfh6l3DxHK0, BvvfZKKz4Yo, WXhOxfPECnM |

Other things covered, so we do not repeat them as news:

| Beat | Who |
|---|---|
| DevDay voice demo failed on stage | SAMTIME (1.03M), Nate Herk 00:42 |
| Voice "call" UI | Lipsky 06:45 (calls it gimmicky), Riley Brown 02:38 (builds his whole workflow on it) |
| Spin up Codex sessions from the dot | Riley Brown, Lipsky, Futurepedia |
| Daily brief automation | Riley Brown 19:12 |
| Heartbeat every hour | Riley Brown 21:13 |
| Slack 3-click setup, dot replies in thread | Nate Herk 04:30 |
| Dot read Gmail before being asked | Build Alone 00:00, Skill Leap 04:09, Lipsky 02:29 |
| Starts from stale ChatGPT memory | Nate Herk 02:48 |
| Cannot edit memory line by line | Build Alone 02:38, Nate Herk 03:40 |
| Scheduled tasks live in the Codex/Work scheduled list, not the dot UI | Nate Herk 11:32 |
| Dot creates Codex threads but does not file them in the right project | Nate Herk 12:07 |
| Price $100 Pro floor, no EU/UK/CH | Lipsky 10:56, Build Alone 03:23, Skill Leap 01:38 |

### Gaps (our openings)

1. Nobody put a Dot next to a self-hosted agent on screen. Tyler has 3 Hermes bots in Slack and 7 crons running. The split-screen does not exist on YouTube yet.
2. Nobody showed a guardrail firing. Auto-review blocking an action, or a Custom Rule set to "Hand off to you" kicking a step back, has not been on camera. Hermes side: a Researcher bot refusing to publish (hard rule) is the same moment, self-hosted.
3. Nobody opened Activity View or the dot's cloud computer with "Take over" and explained what you are looking at. Nate Herk got lost in it. The Hermes side is `~/.hermes/profiles/<bot>/logs/agent.log` and the kanban board; same idea, readable files.
4. Memory: 2 creators complained you cannot edit the dot's memory. Hermes memory is a text file Tyler can open. Nobody showed that contrast.
5. The one Dots-vs-Claude-Code video has 522 views and no screens. The lane is open for a channel with a baseline.
6. Nobody did the "same job, both agents, same morning" with a receipts table. Build Alone narrated it; no table, no timestamps on screen.

## 5. Three Dot jobs for Tyler, with the Hermes twin

Rule: every Hermes item below exists on this Mac today; anything marked "to build" does not. Dot prompts follow OpenAI's own shape (what to check, when, time zone, what deserves a message, where to deliver, confirm the schedule). Dot side is unverified until Tyler runs it; Dots rolled out gradually and his account's connectors are unknown to me.

### Job 1. Morning content brief, 7:45 ET weekdays

| | Dot | Hermes (exists) |
|---|---|---|
| What runs | Scheduled task in the dot | Researcher cron `Content: morning brief`, `45 7 * * 1-5`, deliver slack, runs the `content-brief` skill |
| Reads | Connected Google Drive / GitHub for `~/content` (needs the content repo reachable; GitHub plugin on the private repo) | `youtube/notes/status.md`, newest `youtube/analytics/daily/*.json`, `youtube/ideas/video-ideas.md`, `research/` last 7 days |
| Output | Message in Slack | Slack message under 900 chars, 3 openings, ends "Reply with a number" |
| Follow-through | Dot: reply in thread, it keeps working | Tyler replies a number; Researcher runs yt-search, transcribe, creator-breakdown, hands to Packager |

Exact Dot prompt:

```
Every weekday at 7:45 AM Eastern, for the next 4 weeks, read youtube/notes/status.md, the newest file in youtube/analytics/daily/, youtube/ideas/video-ideas.md, and anything in research/ from the last 7 days in my tylerprogramming/content GitHub repo. Send me one Slack DM under 900 characters: what is filming next, yesterday's channel numbers, and 3 video openings with a one-line reason each. End with "Reply with a number." Do not post anywhere else and do not change any files. Confirm the schedule.
```

Side by side on screen: both Slack messages at 7:45. Hermes has 25 completed runs in `~/.hermes/profiles/researcher/cron/jobs.json`; the Dot has day 1.

### Job 2. GitHub repo health, daily

| | Dot | Hermes (exists) |
|---|---|---|
| What runs | Scheduled task, GitHub plugin, read-only | Default-profile cron `GitHub: Repo Health`, `0 9 * * *`, skill `github-repo-health`, deliver slack. Plus Coder cron `coder: morning repo check` on skoolos and jarvis-public, `0 8 * * 1-5` |
| Rule | Custom Rule: "Hand off to you" for creating PRs or issues | Prompt says read-only; Coder never pushes without a PR |
| Output | Slack digest, up to 5 actions | Slack digest, up to 5 actions, coverage, access limits |

Exact Dot prompt:

```
Every day at 9 AM Eastern, check my GitHub repos under tylerprogramming. Look for open PRs with failing checks, issues with no reply for 7+ days, and dependencies flagged by Dependabot. Send me a Slack DM with at most 5 items, each with a link. Never open, close, merge, or comment on anything; if you think a PR or issue should be created, ask me first. Confirm the schedule.
```

Then add the Custom Rule in Settings > Personalization > Custom rules: action "create or merge pull requests, open or close issues", behavior "Hand off to you". The guardrail-firing beat: ask the Dot in chat to "go ahead and open that issue" and film what the rule does. Unverified; this is the moment nobody has on camera.

### Job 3. New video goes live, Skool lesson and feed post get prepped

| | Dot | Hermes (exists) |
|---|---|---|
| Trigger | Dot event monitoring, if YouTube is a supported source; otherwise a daily check | Skool Librarian bot (profile `skool-librarian`), kicked by a kanban card per video |
| Steps | Pull transcript, write 2 paragraphs, draft a feed post, draft a PDF outline | `check_public.py`, `dup_gate.py`, transcript via `transcribe`, lesson + guide PDF, post scheduled in Attend for 9am ET next open weekday |
| Approval | Custom Rule: posting to Skool or Attend = "Ask before taking action" | Hard rule in SOUL: one Slack message to Tyler, then block the card until he approves |
| Output | Draft in chat or a Space page | Lesson in The AI Agency YouTube Library course, post in Attend |

Exact Dot prompt:

```
Watch my YouTube channel tylerreedai. When a new video goes public, get its transcript, then draft: a lesson title, two short paragraphs describing the video, 2 to 4 key links from the description, and a 120-word community post for my Skool group The AI Agency. Put the drafts in a page and send me the link in Slack. Never post to Skool, Attend, or anywhere public; I will post. Confirm which events you can watch.
```

Attend: Tyler's crons use the ClickUp API (`attend_brief.py`, failing 10/23 with an API error) and the Skool Librarian uses Attend MCP. Whether the Dot can reach Attend at all depends on a plugin that I cannot confirm exists. Mark "to verify" on camera.

### What only one side can do today

| Capability | Dot | Hermes |
|---|---|---|
| Voice call from a walk | Yes | No |
| Wake itself up with no schedule (proactive research) | Yes, read-only | No; crons only |
| Edit its memory in a text editor | No (G: cannot view or modify individual memories) | Yes, `~/.hermes/profiles/*/memories/` |
| Read the log of what it did | Activity View, desktop only | `logs/agent.log`, kanban events, `executions.db` |
| Run on Tyler's Mac | Yes if the ChatGPT app is open | Always, it is the Mac |
| Bot-to-bot handoff | No (one dot per account) | Yes, Researcher -> Packager -> Coder via Slack and kanban |
| Cost | Included in Pro ($100+) | Model API spend, number not in this file |

## 6. Working titles

Formula: number + outcome + tool.

1. I Gave OpenAI's Dot the 3 Jobs My Hermes Bots Already Do
2. OpenAI Dots vs My Self-Hosted Agents: Same 3 Jobs, Same Morning
3. 7 Days With a Dot Next to 3 Hermes Bots (What Each One Actually Did)
4. The One Thing a $100 Dot Does That My Free Agents Can't

No. 4 breaks the "no money in titles" rule in CLAUDE.md; listed to reject.

## Files

- This file: `~/content/research/2026-10-24-openai-dots.md`
- Raw search JSON: `~/content/research/2026-10-24-openai-dots.json` (+ chatgpt-dots, dots-vs-claude-code, openai-devday-2026-agents)
- Thumbnails: `~/content/research/2026-10-24-*-thumbnails/`
- Creator breakdown: `~/content/research/youtube/creator-breakdowns/2026-10-24-openai-dots.md`
- Transcripts: 7 files listed in section 2
