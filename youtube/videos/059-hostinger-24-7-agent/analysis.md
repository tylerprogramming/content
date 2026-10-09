# Analysis, video 059: Create Your First 24/7 Hermes Agent (Hostinger VPS)

Written 2026-09-21 by @packager from @researcher's files. Research was not redone; this file consolidates what was on disk and adds only what was missing (current Hostinger pricing, the cron and desktop-app docs, the CLI flags on this install).

Source files:
- `research/2026-09-21-24-7-ai-agent-hostinger.md` (report)
- `research/youtube/creator-breakdowns/2026-09-21-metics-media-hermes-hostinger-vps.md` (beat table, prompts, our-beat plan)
- `research/2026-09-16-hermes-10-minute-guide.md` (import-agent dry run on the Mac: 55 items)
- Transcripts: `transcript_0ZnR7fqD5rM.txt` (Metics VPS), `transcript_6L4v-6ztQXE.txt` (Liqui AI), `transcript_DYdvJCxWd6M.txt` (Metics general)

## 1. Reference structure: Metics Media, Hostinger Hermes VPS guide (21,303 views, 31:19, 09-07)

| Time | Segment | Purpose |
|---|---|---|
| 0:00-0:55 | "Hiring your first AI employee": place to work, brain, phone number, training, schedule | hook |
| 0:55-3:29 | Buy KVM1, coupon rules, register, pay, keep username hermes, deploy | setup |
| 3:29-5:08 | Docker Manager > Compose > one-click Deploy > Hermes Agent | setup |
| 5:08-6:38 | Dashboard tour: Models, Cron, Chat, Gateway | teaching |
| 6:38-10:30 | OpenRouter key, $5 credits, $10 weekly limit, DeepSeek V4 Flash, "hello" | setup |
| 10:38-13:28 | Telegram via QR, /sethome | setup |
| 13:30-15:24 | "what tools do you have?", standing desk comparison | demo |
| 15:24-19:38 | Desktop app install, Remote Gateway, HUD mode | demo |
| 19:46-21:38 | Memory: "too wordy, save as a preference", new session | demo |
| 21:38-23:12 | Capabilities page, Skills Hub | teaching |
| 23:12-25:06 | The cron job: one prompt, YouTube trends watcher, one result | demo |
| 25:06-27:20 | Cost: 105 requests, 4M tokens, 13 cents, cache | teaching |
| 27:20-29:06 | Logs, Restart Gateway, Docker restart, hermes doctor | teaching |
| 29:06-31:15 | Sub-agents Lisbon prompt, channels, profiles, OpenClaw import, affiliate CTA | CTA |

### What works
- Employee metaphor as a table of contents, repeated at 19:38 as a progress check.
- "Here's the demo I promised earlier" at 23:14: promise early, pay late.
- Cost as a reveal with real numbers, not a disclaimer.
- Spend limit set before the first message.
- Three-tier troubleshooting.
- Every click narrated with its menu path.

### Weaknesses (our openings)
| Weakness | Evidence | What 059 does |
|---|---|---|
| 24/7 never proven | one result at 24:35, same session, no time gap | close the laptop on camera, next-morning cut with N runs |
| Job is generic, leaves a Telegram paragraph | 23:36 | job writes a file, commits it, posts a link |
| Payoff at 23:12 of 31:19 (74% in) | | job on screen by 8:45 of ~19:00 (46% in) |
| 2:34 buying a plan | 0:55-3:29 | under 2:30 for the entire deploy, no coupon talk |
| "No terminal, no coding" beginner frame | 0:17 | Claude Code users from 057; they get import-agent |
| Telegram | 10:38 | Slack, same channel as the Mac agent |
| Desktop app is a 4-minute tour | 15:24-19:38 | desktop app is the proof device, next morning |
| Nothing touches a repo | | repo cloned on the VPS, job commits |

### Liqui AI (9,700 views, 10:26, 07-03)
0:00-4:08 why a VPS, 4:08-6:32 buy and deploy described not clicked, 6:32-10:23 a competitor-monitor job in prose. No prompt typed, no result shown. Useful only as evidence that the lane tolerates a 10-minute cut.

### Target audience and level
Claude Code users who watched 057 and have Hermes on a Mac. They know terminals, skills, CLAUDE.md, cron. They do not have a machine to leave on. Assumed level: comfortable pasting a command, not interested in what Docker is.

## 2. The landscape in counts (from the 09-21 report)

| Claim | Metics VPS | Liqui | 059 |
|---|---|---|---|
| Runs shown | 1 sample | 0 | N overnight, on the phone |
| Schedule firing while creator is away | no | no | yes |
| Job leaves an artifact | Telegram message | no | file + commit |
| Second machine proves the laptop was closed | no | no | desktop app to VPS next morning |
| Minutes buying the plan | 2:34 | 1:30 | under 1:00 |
| Minutes on the job | 1:54 | 3:51 prose | ~5:00 plus 3:00 proof |

Head term: "Hermes Agent", 20 long-form videos over 20K in 30 days. VPS sub-term nearly empty (Claritics 105 views). "24/7" is trading titles (Nate Herk 449,898). "While you sleep" without money under 30K. Metics VPS-titled did 21,303 vs 375,037 for their general one, same channel, same month: do not lead with the VPS.

## 3. What was filled in on 09-21 (new, verified today)

| Item | Finding | Source |
|---|---|---|
| Hostinger Hermes page pricing | KVM 1 $6.49/mo promo (was $19.49), renews $11.99/mo for 2 years; KVM 2 $8.99 (renews $14.99); KVM 4 $12.99; KVM 8 $25.99. A separate "Managed Hermes Agent" plan at $5.99/mo (renews $11.99) with built-in AI credits and Telegram pairing. Coupon AIPOWER10 for 10% on 12m+ plans. "10,000+ Hermes Agents already launched." All plans paid upfront. | hostinger.com/applications/hermes-agent, 09-21 search snippet. **Re-verify on filming day.** |
| Managed vs VPS | Managed: no root, web UI, Telegram built in, AI credits built in. VPS: root, Docker template, "connect messaging using the terminal." For 059 the VPS is the right one because we need the terminal for import-agent and the repo. | same page |
| Desktop app remote gateway, Hostinger's own doc | Settings > Gateway > Remote Gateway > paste dashboard URL > Save > close and reopen the app | hostinger.com/support/how-to-connect-the-hermes-desktop-app-to-a-hostinger-vps |
| Desktop app remote gateway, Nous docs | Settings > Gateways > Registered gateways > Add connection > kind: Remote gateway > Name + Gateway URL (a running `hermes serve`) + Session token or OAuth > Save > Test > "Reachable". Every connection needs a unique device name. Profiles, chats, messaging and cron are scoped per gateway. | hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop |
| Which menu path Tyler's app shows | **Unverified.** Two docs, two paths. Film whichever appears. | |
| `hermes cron create` flags on this install (v0.21.3) | `--name`, `--deliver` (origin, local, telegram, discord, signal, platform:chat_id, bot-chat[:profile]), `--skill` (repeatable), `--workdir` (injects CLAUDE.md from that dir and uses it as cwd), `--script`, `--no-agent`, `--monitor-script`, `--monitor-url`, `--model`, `--provider`, `--repeat`, `--paused` | `hermes cron create --help` |
| `hermes cron` subcommands | list, create, edit, pause, resume, run, remove, resnap, status, runs (history), incidents, notepad, doctor, tick | `hermes cron --help` |
| Notepad | `hermes cron notepad <job_id> {get,set,delete,list} [key] [value]`, a per-job KV store that persists across runs. This is what the job prompt means by "keep that list in your notepad." Whether the agent reaches for it from a plain-language prompt is **unverified**. | `hermes cron notepad --help` |
| `hermes cron runs` | shows durable execution attempts per job, `--limit 1-500`. This is the next-morning proof command. | `hermes cron runs --help` |
| Cron docs | Jobs run in fresh sessions with no chat memory; prompts must be self-contained. `--deliver slack` goes to the Slack home channel. `[SILENT]` trick for no-op runs. Gateway ticks every 60 seconds; a CLI chat session does not fire cron. `hermes cron doctor` checks jobs for common health issues. | docs/user-guide/features/cron, docs/guides/automate-with-cron, docs/guides/cron-troubleshooting |
| `hermes import-agent` on this install | `hermes import-agent [claude-code|codex] [--source PATH] [--dry-run] [--overwrite] [--yes] [--sync]`. Auto-detects `~/.claude`. Credentials never imported. | `hermes import-agent --help` |
| Slack | Socket Mode, no public URL. Bot token `xoxb-` + app token `xapp-`. `hermes slack manifest --agent-view --write` writes `~/.hermes/slack-manifest.json`. | docs/user-guide/messaging/slack |
| Hermes version on the Mac | v0.21.3 (2026.9.14), 3,826 commits behind upstream per `hermes --version` on 09-21. The VPS template will likely ship a newer build; expect UI differences and say so. | `hermes --version` |

## 4. The angle

Title leads with the outcome and the head term, host in the parenthetical: **Create Your First 24/7 Hermes Agent in 20 Minutes (Hostinger VPS)**. Money on the thumbnail, not the title.

Structure: deploy fast (2:30), brain and Slack (2:30), import-agent (2:00, the beat nobody has), the job (5:00, the video), close the laptop (0:30), next morning (3:00, the proof and the withheld payoff), cost and troubleshooting (1:15), close. About 19:15.

Reused from 057: cron beat (`hermes cron list`, `hermes cron run`), Slack delivery, the OpenRouter spend cap idea, Tina-style beat table.
New: Hostinger deploy, import-agent on a server, a job that commits to a repo, `hermes cron runs`, the overnight cut, desktop app remote gateway.

## 5. Risks

| Risk | Mitigation |
|---|---|
| Overnight run fails and there is nothing on the phone | Hook 2 as fallback; film the job beat with the hand-triggered run and say plainly that the overnight one did not fire, then show the incident in `hermes cron incidents`. That is honest and still a video. |
| Two gateways on one Slack app fight | Second Slack app for the VPS, one line on camera |
| Desktop app version does not do the remote connection cleanly | Web dashboard on the Mac, say the desktop menu exists |
| Docker container cannot see `~/.claude` | Copy into the mounted volume or exec in; trim to CLAUDE.md + skills if needed |
| "Runs While You Sleep" style titles capped on the channel (0.27x, 0.51x) | Recommended title is instruction-led with a time box; the sleep line is the day-8 B-test only |
| 057 and 059 are both Hermes promises. Brain rule: do not ship two videos on one promise inside four days | 057 published 09-20. 059 needs two filming days plus edit, so it lands at least a week later. Space it further if 057 is still adding. |

## 6. Unverified (carry into the filming guide, do not state on camera)

- Hostinger plan names and prices on filming day
- Template label "Hermes Agent" in the catalog
- Tyler's Hostinger affiliate link
- One Slack app serving two gateways
- import-agent path inside the Docker container
- The agent using the cron notepad from a plain-language prompt
- Desktop app menu path on Tyler's installed version
- ByteGrad 13K and Tech With Tim 125K view counts (from the 09-20 note, not re-pulled)

## Sources

- https://www.hostinger.com/applications/hermes-agent
- https://www.hostinger.com/applications/hermes-agent/1 (Managed vs VPS comparison)
- https://hostinger.com/support/how-to-connect-the-hermes-desktop-app-to-a-hostinger-vps
- https://hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop
- https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
- https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
- https://hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting
- https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack
- https://youtube.com/watch?v=0ZnR7fqD5rM (Metics Media, VPS guide)
- https://youtube.com/watch?v=DYdvJCxWd6M (Metics Media, general guide)
- https://youtube.com/watch?v=6L4v-6ztQXE (Liqui AI)
- `research/2026-09-21-24-7-ai-agent-hostinger.md` and the five raw yt-search reports it cites
- `research/youtube/creator-breakdowns/2026-09-21-metics-media-hermes-hostinger-vps.md`
- `research/2026-09-16-hermes-10-minute-guide.md`
