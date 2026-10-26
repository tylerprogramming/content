# Filming guide, video 059

The "do this, click that" version. Two filming days: day one is sections 2 to 7, day two is the cold open, section 8 and section 9. Hook 1 films last.

## Verify before you roll (the "to verify" list from the research, still open)

| # | Item | How to check | Fallback if it fails |
|---|---|---|---|
| 1 | Hostinger plan name and price | Open hostinger.com/applications/hermes-agent the morning you film. On 09-21 it showed KVM 1 $6.49/mo (renews $11.99) and a "Managed Hermes Agent" plan at $5.99/mo (renews $11.99). | Say what the screen says. Never quote a price from this file. |
| 2 | Template is still labelled "Hermes Agent" in the catalog | VPS > Manage > Docker Manager > Compose > one-click Deploy > search Hermes | Use whatever label it has, say "the label may have changed since I recorded" |
| 3 | One Slack app, two gateways (Mac and VPS) in Socket Mode | Paste the tokens on the VPS, restart its gateway, DM the bot from the phone, confirm only one reply. Leave both gateways up for an hour and confirm neither drops. | Second Slack app for the VPS (`hermes slack manifest --agent-view --write`, rename it in the JSON, install, paste new tokens). One line on camera: "I gave the server its own Slack app." |
| 4 | `.claude` folder visible to `hermes import-agent` inside the Docker container | Copy `~/.claude` to the VPS, then exec into the container (or use the dashboard Web Console) and run the dry run with `--source` | Trim to CLAUDE.md + `skills/`, copy that, say "I trimmed it for the video" |
| 5 | Content repo cloned on the VPS, git identity set, push works unattended | On the VPS: `git -C /root/content push` with no prompt. Use a deploy key or `gh auth login` with a token. | Use a scratch repo (`tylerprogramming/hermes-watch-demo`) instead of the content repo |
| 6 | The agent creates the cron job from the plain-language prompt, with the notepad | Run the prompt in a scratch session the day before. Then `hermes cron list` and `hermes cron notepad <job_id> list` | Tell it to keep the seen-list in `research/hermes-watch/seen.txt` instead |
| 7 | `yt-search` skill works on the VPS (yt-dlp installed, no API key) | `hermes cron run hermes-watch`, watch the log | Let the agent install yt-dlp on camera; it is a good beat |
| 8 | Desktop app menu path for the remote gateway | Open the installed app: Settings > Gateway > Remote Gateway (Hostinger doc), or Settings > Gateways > Add connection (Nous docs) | Web dashboard on the Mac. Say the desktop app can do it too and show the menu, do not fake the connection |
| 9 | Tyler's Hostinger affiliate link | Check the affiliate dashboard or ask | Plain link |
| 10 | OpenRouter spend limit UI | openrouter.ai > Keys > Edit > limit | Skip the limit on camera, mention it in narration |

Dry-run 3 through 8 the day before. The overnight proof cut depends on 5, 6 and 7 all working unattended.

## Pre-recording setup

1. Fresh Hostinger account or a fresh VPS on the existing one. Do not reuse a VPS that already has Hermes configured; the deploy beat has to be real.
2. OpenRouter key created with a weekly limit set. Have the key in a text file off screen to paste.
3. Slack tokens (bot + app) ready to paste. Blur on the paste.
4. `~/.claude` (or the trimmed copy) already copied to the VPS. The copy is not interesting on camera; show the `ls` and the command, speed it up.
5. Content repo (or the scratch repo) cloned at `/root/content` on the VPS, git identity set, one test push done.
6. Phone on the desk with Slack open on #content.
7. Desktop app on the Mac open to the local agent, ready for the section 8 beat.
8. A clock or the menu bar time visible somewhere for the close-the-laptop beat.
9. Camtasia set to record screen plus camera. Two recording days, two project files.

## Day one

### 1. Deploy (script section 3)

1. Open `hostinger.com/applications/hermes-agent`. Say the price once.
2. Click **Choose plan** on the smallest plan. Speed through checkout at 4x in the edit.
3. Uncheck the pre-checked AI credits add-on if present.
4. Post-checkout: username `hermes`, set a password, click **Deploy**.
5. While it deploys: **VPS > Manage > Docker Manager**. Show the container.
6. Copy the dashboard URL from the VPS overview page. Open it. Log in.

> "Keep the username as hermes, the template expects that. Set a password, write it down, click deploy."

Dead air while it deploys (60 to 120 seconds): explain that it is a Docker container, and that Docker Manager is where you restart it or read logs later. If you run out, cut.

### 2. Brain and Slack (script section 4)

1. Dashboard > **Models**. Show empty.
2. openrouter.ai > **Keys** > Create key > set a weekly limit > copy. Blur.
3. Dashboard > paste key > **Models > Main Model** > pick a model > Save.
4. Dashboard > **Chat**. Type:
   ```
   hello
   ```
5. Dashboard > **Channels > Slack**. Paste bot token and app token. Save and restart gateway.
6. Phone: DM the bot. Show the reply.

> "Set a spend limit on the key. This agent is going to run when I am not watching it. If something loops, I want a ceiling."

Dead air on the gateway restart: "The reference videos all use Telegram. I am on Slack because that is where my Mac agent already posts. Same idea, there is a QR flow for Telegram right here."

### 3. Import (script section 5)

1. On the Mac: `ls ~/.claude`. Two seconds.
2. On the VPS terminal (Web Console or SSH):
   ```
   hermes import-agent claude-code --source /root/.claude --dry-run
   ```
   Adjust `--source` to wherever the folder landed inside the container.
3. Scroll the preview. Read the count.
4. Run it for real:
   ```
   hermes import-agent claude-code --source /root/.claude
   ```
5. `hermes skills list` or Dashboard > Skills. Point at `yt-search`.

> "That is my whole Claude Code setup, [N] items, on a six dollar server in one line. I have not seen this command in a single Hermes server video."

### 4. The job (script section 6)

1. Dashboard > Chat > new session. Paste the prompt:
   ```
   Set up a scheduled job for me.

   Every 4 hours: use the yt-search skill to search YouTube for "hermes agent" from the last 7 days. Compare against a list of video IDs you have already reported (keep that list in your notepad for this job). For every new video over 10,000 views, append a line to research/hermes-watch/YYYY-MM-DD.md in /root/content with the title, channel, views, and link. Commit that file with the message "hermes-watch: <date> <time>". Then post a 3-line summary to Slack #content with a link to the commit. If nothing new cleared the threshold, post one line saying so.

   Name the job "hermes-watch". Deliver to Slack.
   ```
2. Let it work. Speed up the middle. If it installs yt-dlp, keep that.
3. Terminal:
   ```
   hermes cron list
   ```
4. Terminal:
   ```
   hermes cron run hermes-watch
   ```
5. Watch three places: terminal log, GitHub commit list, phone. Record all three; cut between them.
6. Open the committed file on GitHub. Read two lines.
7. Terminal:
   ```
   hermes cron runs hermes-watch
   ```

> "Every four hours is for the video, so tomorrow morning shows more than one run. In real life I would run this once a morning."

> "Will it be right every time? No. It is an LLM doing a search. That is what the notepad and the threshold are for. You nudge it, you do not babysit it."

Fallback job if 5 (repo push) is not working: same prompt without the commit step, and the file goes to `~/hermes-watch/` on the VPS. Show the file over SSH the next morning instead of a commit. Weaker but honest.

### 5. Close the laptop (script section 7)

1. Talking head, 20 seconds. Say the schedule and what you expect by morning.
2. Close the lid on camera. Hold two seconds.
3. Overlay date and time in the edit.

## Day two (next morning, before touching anything)

### 6. Phone first (script section 8a)

1. Do not open the laptop yet. Phone: Slack #content. Scroll the overnight thread slowly. Read every timestamp.
2. Tap one summary. Show the commit link.
3. GitHub on the phone: commit list with overnight timestamps.

> "Six PM. Ten PM. Two AM. Six AM. [N] runs. The laptop was closed for all of these."

Count the runs before you start talking. Say the number the screen shows.

### 7. Desktop app to the VPS (script section 8b)

1. Open the Mac. Open the Hermes desktop app.
2. **Settings > Gateway > Remote Gateway** (or **Settings > Gateways > Add connection > Remote gateway**). Paste the dashboard URL. Session token if it asks. Save. Restart if it asks.
3. Sessions list refreshes. Open the 2am cron session. Scroll the transcript.
4. Type to the remote agent:
   ```
   What did you find overnight? One line per run.
   ```

> "This is the 2am run, the whole transcript, from my Mac, which was closed at 2am."

### 8. Cost and troubleshooting (script section 9)

1. openrouter.ai > **Activity**. Read requests, tokens, cost.
2. Dashboard > **Logs**. Filter to gateway.
3. Dashboard > **Restart Gateway**.
4. **Docker Manager** > restart container. Do not actually click it unless you want to wait.
5. Web Console:
   ```
   hermes doctor
   hermes cron doctor
   ```

### 9. Close and Hook 1

1. Close (script section 10). Talking head.
2. Then record Hook 1 last, phone in hand, closed laptop behind you, with the real run count.

## Timing cheat sheet

| Section | Target | Cut first if over |
|---|---|---|
| 1 Cold open | 0:45 | no |
| 2 Why a server | 1:00 | trim to 0:40 |
| 3 Deploy | 2:30 | yes, to 2:00 |
| 4 Brain and Slack | 2:30 | trim Slack to 1:00 |
| 5 Import | 2:00 | no, this is the differentiator |
| 6 The job | 5:00 | no, this is the video |
| 7 Close laptop | 0:30 | no |
| 8 Next morning | 3:00 | no |
| 9 Cost and troubleshooting | 1:15 | yes, to 0:45 |
| 10 Close | 0:45 | no |
| **Total** | **19:15** | ceiling 20:00 |

## On-camera tips

- Say the number on the screen, never the number in this file. Runs, items, cents, dollars.
- The three "to verify" beats (Slack sharing, Docker import path, desktop remote gateway) each have a one-line honest fallback in the script. Use it rather than cutting around a failure. The honest line is the trust beat.
- One "right?" per section at most.
- Hedge on the job's accuracy. "It will miss things" is the line that earns the comment section.
- The close-the-laptop beat is 30 seconds and it is the reason the video exists. Do not rush it.
- No em dashes in any overlay text.
