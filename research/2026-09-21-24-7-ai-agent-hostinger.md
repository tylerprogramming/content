# Research: Create Your First 24/7 AI Agent (Hostinger VPS)

Date: 2026-09-21. Picked from the morning brief (option 1). Target: the video after 057, Hermes on a Hostinger VPS doing one job unattended.

Sources: 5 yt-search runs today (30 days, yt-dlp, no API key). Raw reports and JSON in this folder:
`2026-09-21-hermes-agent.md`, `2026-09-21-ai-agent-24-7.md`, `2026-09-21-ai-agent-while-you-sleep.md`, `2026-09-21-hermes-agent-vps.md`, `2026-09-21-hostinger-ai-agent.md`, `2026-09-21-hermes-agent-hostinger.md` (90 days).

## 1. The direct competitors (Hermes + VPS / Hostinger)

| # | Title | Channel | Views | Length | Uploaded | Ends at | Transcript |
|---|---|---|---:|---|---|---|---|
| 1 | Hermes Agent - Full Tutorial & Setup Guide (For Beginners) | Metics Media | 375,037 | 34:23 | 2026-08-31 | general setup, Hostinger-hosted | `transcripts/transcript_DYdvJCxWd6M.txt` (existing) |
| 2 | Hostinger Hermes Agent Tutorial - Full VPS Setup Guide | Metics Media | 21,303 | 31:19 | 2026-09-07 | one cron job written by the agent, one result shown | `transcripts/transcript_0ZnR7fqD5rM.txt` (new) |
| 3 | Hermes Agent Hostinger Deployment - Step-by-Step Tutorial | Liqui AI | 9,700 | 10:26 | 2026-07-03 | no demo at all, describes a monitor job in prose | `transcripts/transcript_6L4v-6ztQXE.txt` (new) |
| 4 | How to Connect Hermes Agent VPS to Desktop App (2026 Latest Guide) | Claritics | 105 | 2:52 | 2026-09-13 | remote gateway link only | not fetched |

Not in the 30-day window (from the 09-20 status.md pull, unverified today): ByteGrad 13K sponsored, Tech With Tim 125K course also on Hostinger.

## 2. What the "24/7" and "while you sleep" terms look like

| Term (30 days) | Long-form found | Biggest | Views | Notes |
|---|---:|---|---:|---|
| ai agent 24 7 | 20 | Nate Herk, I Turned GPT-6 Astra Into a 24/7 Stock Trader | 449,898 | trading/money framing. Metics general Hermes video ranks #5 here at 375,037 |
| ai agent while you sleep | 19 | Miles Deutscher, AI Trading Bot That Trades While You Sleep | 26,253 | 15 Shorts, all under 100 views except Jack Roberts 30,053 and Dan Martell 27,307 |
| hermes agent vps | 1 | Claritics | 105 | empty term |
| hostinger ai agent | 3 | Preet Tech Ideas | 235 | Hostinger's own "AI Agent" product, not Hermes; noise |
| hermes agent hostinger (90 days) | 1 | Liqui AI | 9,700 | |

Read: "24/7" is dominated by trading and money titles. "While you sleep" without a money hook stays under 30K. The Hermes term is the traffic (20 videos over 20K in 30 days); the VPS sub-term is nearly empty on YouTube search, so the title should lead with the outcome and carry "Hermes Agent" in it, with Hostinger in the description and thumbnail.

## 3. The Hermes head term, last 30 days (top 15)

| # | Title | Channel | Views | Length | Uploaded |
|---|---|---|---:|---|---|
| 1 | Hermes Agent - Full Tutorial & Setup Guide (For Beginners) | Metics Media | 375,037 | 34:23 | 08-31 |
| 2 | My FULL Hermes Agent Setup (HermesOS) | Tina Huang | 184,472 | 16:24 | 08-25 |
| 3 | Hermes Agent Skills That Make It 10x More Powerful | AI LABS | 115,094 | 11:54 | 08-30 |
| 4 | Why I'm back to Qwen 3.8 27B and Hermes Agent | Digital Spaceport | 109,987 | 16:48 | 09-06 |
| 5 | Every Hermes Agent Concept Explained for Normal People | The AI Architects | 89,502 | 40:00 | 08-24 |
| 6 | Master 95% of Hermes Agent | Zinho Automates | 74,445 | 15:20 | 08-28 |
| 7 | 7 INSANE Use Cases For Hermes Agent | The AI Architects | 65,949 | 22:30 | 09-03 |
| 8 | Building With Hermes Agent | Tina Huang | 65,643 | 1:10:50 | 09-19 |
| 9 | Hermes Agent Tutorial for Beginners: How to Build an App with AI | Mikey No Code | 50,453 | 19:47 | 08-26 |
| 10 | How I Made Hermes Agent 10x More Powerful | Sharbel A. | 41,240 | 13:31 | 08-23 |
| 11 | How to Set Up Hermes Agent on Your Computer (Desktop App) | Teacher's Tech | 34,577 | 21:19 | 09-07 |
| 12 | How I Upgrade My Hermes Agent Team: Bot Mode, Skills & MCP Tips | Wanderloots | 33,131 | 21:40 | 09-11 |
| 13 | Qwen Image 2.1 Local AI Image Generation Review with Hermes Agent | Digital Spaceport | 28,928 | 13:25 | 09-21 |
| 14 | 10 Hermes Agent Skills You Need to Install Today | Brandon Builds | 22,341 | 11:09 | 09-09 |
| 15 | Hostinger Hermes Agent Tutorial - Full VPS Setup Guide | Metics Media | 21,303 | 31:19 | 09-07 |

Metics' VPS-specific video did 21,303 in 14 days against 375,037 for their general one. Same channel, same host, same month: the VPS framing cut reach by roughly 17x. Do not title on the VPS.

## 4. What the two reference transcripts actually do

Metics VPS (31:19), beats by timestamp:

| Beat | Time | On screen |
|---|---|---|
| Hook | 0:00-0:55 | "hiring your first AI employee": place to work, brain, phone number, training, schedule |
| Buy the VPS | 0:55-3:29 | KVM1 plan, coupon, register, pay, keep username hermes, click deploy |
| Deploy template | 3:29-5:08 | VPS > Docker Manager > Compose > one-click Deploy > catalog "Hermes Agent" |
| Dashboard tour | 5:08-6:38 | Models, Cron, Chat, Gateway |
| OpenRouter key + spend limit | 6:38-10:30 | $5 credits, $10 weekly limit, DeepSeek V4 Flash, "hello" test |
| Telegram bot | 10:38-13:28 | Create with QR, save and restart, /sethome |
| First job | 13:30-15:24 | "what tools do you have?", then "research the top three standing desks and give me a one paragraph comparison" |
| Desktop app remote gateway | 15:24-19:38 | download, install, Settings > Gateway > Remote Gateway, paste URL, HUD mode |
| Memory demo | 19:46-21:38 | "too wordy... save that as a preference", new session, preference holds |
| Capabilities + Skills Hub | 21:38-23:12 | |
| The cron job | 23:12-25:06 | one prompt: "Watch YouTube for AI productivity trends. Build yourself a reusable skill for the check. Keep track of what you've already shown me. Schedule it every few hours and message me here only when there's something new." Shows job list, one result |
| Cost | 25:06-27:20 | 105 requests, 4M tokens, 13 cents, cache explained |
| Troubleshooting | 27:20-29:06 | Logs, restart gateway, Docker restart, web console `hermes doctor` |
| Extras + CTA | 29:06-31:15 | sub-agents Lisbon prompt, channels, profiles, OpenClaw import, affiliate link |

Liqui AI (10:26): 0:00-4:08 why a VPS, 4:08-6:32 buy + deploy (described, not clicked through), 6:32-10:23 a competitor-monitor job described in prose. No prompt typed, no result shown.

## 5. The gap, in counts

| Claim | Metics VPS | Liqui | Us |
|---|---|---|---|
| Shows the job running more than once | 0 runs shown live, 1 sample result | 0 | 24h of runs on the phone |
| Shows a schedule firing while the creator is away | no | no | yes, the proof cut |
| Job produces an artifact (file, PR, report in repo) | no, a Telegram message | no | yes |
| Uses a second machine to prove the laptop is closed | no | no | yes, desktop app connects to the VPS the next morning |
| Minutes on buying the plan | 2:34 | 1:30 | under 1:00 |
| Minutes on the job itself | 1:54 | 3:51 prose | 8 to 10 |

Both end at "the loop closes". Neither shows the loop closing more than once.

## 6. Angle

Title lane (money off the title, price on the thumbnail): "Your First AI Agent That Runs While You Sleep (Hermes Agent + Hostinger)". 24/7 as a word sits with trading videos; "while you sleep" is cleaner for this channel.

Proof beat: film the setup, then cut to the next morning. Phone shows every run in Slack or Telegram. Desktop app on the Mac shows the same sessions through the remote gateway, laptop was closed.

Reuse from 057: the cron beat (`hermes -p coder cron list`, `0 8 * * 1-5`), Slack delivery, the bot roster. New material: Hostinger one-click Docker template, remote gateway from the desktop app, the next-day proof cut.

Creator breakdown with the beat-by-beat plan and exact prompts: `research/youtube/creator-breakdowns/2026-09-21-metics-media-hermes-hostinger-vps.md`.

## 7. Unverified

- Hostinger plan names and prices as of today (Metics says KVM1; check the Hermes Agent page before filming).
- Whether the Hostinger template is still labelled "Hermes Agent" in the catalog.
- Tyler's Hostinger affiliate link.
- ByteGrad and Tech With Tim view counts (from the 09-20 note, not re-pulled).
