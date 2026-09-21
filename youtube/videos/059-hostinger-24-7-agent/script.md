# Script, video 059: Create Your First 24/7 Hermes Agent in 20 Minutes (Hostinger VPS)

Target 18 to 20 min. Hard ceiling 20:00 because it is in the title. If the cut runs long, cut section 8 (cost and troubleshooting) to 45 seconds first, then trim section 3 (deploy).

Filming order is not script order. Sections 2 through 7 film on day one. Sections 1 and 8 film the next morning after the job has run overnight. Hook 1 is filmed last.

Placeholders in [brackets] are numbers the screen will show. Say the real one.

## Beat table

| # | Beat | Time | Tell / show / do |
|---|---|---|---|
| 1 | Cold open, next morning | 0:00 to 0:45 | show |
| 2 | What we are building, why a server | 0:45 to 1:45 | tell |
| 3 | Deploy on Hostinger | 1:45 to 4:15 | do |
| 4 | Brain and Slack | 4:15 to 6:45 | do |
| 5 | Import your Claude Code setup | 6:45 to 8:45 | do |
| 6 | The job | 8:45 to 13:45 | do |
| 7 | Close the laptop | 13:45 to 14:15 | show |
| 8 | Next morning: phone, desktop app, repo | 14:15 to 17:15 | show |
| 9 | Cost and troubleshooting | 17:15 to 18:30 | show |
| 10 | Close | 18:30 to 19:15 | tell |

---

## [0:00 - 0:45] Cold open, filmed the next morning

[SHOW: phone in hand, Slack #content, a thread of timestamped posts from the agent. Closed laptop visible behind it.]

So this ran [N] times last night. Midnight, four, eight. My laptop was closed the whole time. I was asleep for all of these.

[SHOW: scroll the thread. Each post is a short summary with a link to a file.]

Every one of those is a real job. It searched YouTube, wrote a file into my repo, committed it, and posted the summary here. And the agent doing it is not on this Mac. It is on a server that costs less than a coffee a week.

[SHOW: cut to the desktop app, sidebar showing the VPS connection, same sessions listed.]

If you watched the last video, you have Hermes Agent running on your machine right now. And it stops the second your laptop sleeps. So today we fix that. We are going to put it on a server, give it one real job, walk away, and come back tomorrow morning to see what it did.

There is one thing in here nobody else shows, and I am holding it for the end. Let's go.

[NOTE: the withheld payoff is section 8, the desktop app connecting to the VPS. Do not name it here.]

---

## [0:45 - 1:45] What we are building, and why a server

[SHOW: talking head, or the 057 setup on the Mac with the desktop app open.]

So quick context. Last video we set up Hermes on the Mac. Memory, skills, a cron job that posts to Slack at 8am, a couple of bot profiles. It is good. I use it every day.

But here is the thing, right? It lives on this laptop. Which means it lives on my schedule. Lid closed, it is asleep. Mac in my bag, the 8am job just does not fire. And if I want to talk to it from my phone while I am out, it has to be awake at home.

[SHOW: simple diagram or just the Hostinger page. Three boxes: server, Slack, desktop app.]

So the fix is kind of obvious. Put the agent on a machine that never sleeps. A small server. And then everything else stays the same: Slack on the phone, the desktop app on the Mac, both talking to the one agent on the server.

Now, every Hostinger plus Hermes video I have watched does the install and stops at "send your first message." Which is fine, but it does not prove anything. The whole point of a server is what happens when you are not there. So this video has a job in the middle and a next-morning check at the end. That is the part I care about.

Four steps. Deploy, connect the brain and Slack, move your Claude Code setup over, give it a job. Then we wait.

[NOTE: transition. "Step one. It needs somewhere to live."]

---

## [1:45 - 4:15] Deploy on Hostinger

[SHOW: hostinger.com/applications/hermes-agent. Do not linger on the marketing.]

So Hostinger has a one-click template for Hermes. Link in the description. I will say the price once: the smallest plan was [$X] a month when I recorded this, and it renews higher, so read the page. The small plan runs one agent fine. If it ends up browsing the web all day you can bump it later without reinstalling anything.

[NOTE: on 09-21 the page showed KVM 1 at $6.49/mo promotional, renewing at $11.99, and a "Managed Hermes Agent" plan at $5.99/mo. Verify on the day and say what the screen says. Do not read out coupon rules or billing periods. That is two and a half minutes in the reference video and nobody needs it.]

[SHOW: choose plan, checkout. Speed this up 4x in the edit. Uncheck any pre-checked AI credits add-on if you are bringing your own key.]

Pick the plan, check out. One thing to catch: there is sometimes a pre-checked box that adds credits for a different AI service. We are bringing our own key, so I uncheck it.

[SHOW: post-checkout setup. Keep the username as hermes. Set a password. Click deploy.]

It asks for a username. Keep it as hermes, the template expects that. Set a password, write it down, click deploy. This takes a minute or two.

[SHOW: while it deploys, the VPS overview page. Then: VPS > Manage > Docker Manager. The Hermes Agent container running.]

While that spins up: what it is actually doing is running Hermes in a Docker container. So if you ever want to see the container, restart it, or read its logs, it is here under Docker Manager. We will come back to that at the end.

[NOTE: the reference uses VPS > Manage > Docker Manager > Compose > one-click Deploy > search Hermes. That is the manual path if the template did not auto-deploy. Verify the label is still "Hermes Agent" in the catalog on the day.]

[SHOW: the Hermes dashboard URL from the VPS page. Open it. Log in.]

And this is the dashboard. It is the same web UI you get with `hermes serve` on your own machine, just running on the server. Copy this URL somewhere. We need it twice more.

[NOTE: transition. "Step two. It needs a brain and a phone."]

---

## [4:15 - 6:45] Brain and Slack

[SHOW: dashboard > Models. Empty or default.]

So right now the agent has nowhere to think. No model. Same as the last video, you can point it at any provider. I am using OpenRouter here because one key gets you every model and you can cap the spend.

[SHOW: openrouter.ai > Keys > create key > set a limit. Blur the key.]

One thing I like about OpenRouter for a server specifically: set a spend limit on the key. This agent is going to run when I am not watching it. If something loops, I want a ceiling. I set [$10] a week. It resets. That is the whole safety net and it takes ten seconds.

[SHOW: paste key into dashboard, Models > Main Model > pick a model. Save.]

Paste it here, pick a model. I am going with [model]. Cheap and fast is the right default for a scheduled job; you can point specific jobs at a bigger model later.

[SHOW: dashboard > Chat. Type "hello". Reply.]

Quick test. It talks. Good.

[SHOW: dashboard > Channels > Slack.]

Now the phone. The reference videos all use Telegram. I am using Slack because that is where my Mac agent already posts, and I want the server agent in the same channel. If you are on Telegram it is the same idea, there is a QR flow for it right here.

[SHOW: paste the bot token and app token from the existing Slack app. Save and restart the gateway.]

I already have a Slack app from the last video, so I am pasting the same two tokens. Bot token, app token. If you do not have one, the command `hermes slack manifest --agent-view --write` writes you a manifest, you paste it into api.slack.com, and you are done. That is in the description.

[NOTE: TO VERIFY before filming. Two gateways (Mac and VPS) sharing one Slack app in Socket Mode. Slack allows multiple Socket Mode connections per app, but confirm both gateways stay connected and that messages route to the one you expect. If they fight, make a second Slack app for the VPS (rename the manifest) and say so on camera in one line. Also confirm the home channel setting on the VPS is `C0C0CD3JUTU` or whichever channel you want the job to land in.]

[SHOW: phone. DM the bot. Reply lands.]

And from the phone. It answers. That is the loop most videos end on. We are about a quarter of the way through.

[NOTE: transition. "Step three. Right now it is a blank agent. Let's fix that."]

---

## [6:45 - 8:45] Import your Claude Code setup

[SHOW: dashboard > Web Console, or SSH into the VPS. Terminal.]

So here is the thing that bugged me about every server video. You spend half an hour setting up an agent that knows nothing. No rules, no skills, no memory. If you use Claude Code, you have all of that already, and it is sitting on your Mac.

[SHOW: on the Mac, `ls ~/.claude`. Then a quick `scp` or `rsync` of `~/.claude` to the VPS. Blur any paths that reveal keys. Speed up.]

So I copy my `.claude` folder up to the server. Just the config, the skills, CLAUDE.md. Not credentials; Hermes never imports those anyway.

[NOTE: TO VERIFY. The template runs Hermes inside Docker, so the import has to see the folder from inside the container. Options: copy into the mounted Hermes data volume, or exec into the container. Dry run this the day before. If it is messy, copy a trimmed `.claude` with just CLAUDE.md and the skills folder and say "I trimmed it for the video."]

[SHOW: on the VPS terminal.]

```
hermes import-agent claude-code --source /path/to/.claude --dry-run
```

[SHOW: the preview scrolling. Count of items.]

Dry run first. Look at that. [N] items. CLAUDE.md becomes the agent's memory file. My MCP servers come across. And every skill I have written for Claude Code, [N] of them, lands as a Hermes skill. Credentials are skipped on purpose.

[SHOW: run it for real.]

```
hermes import-agent claude-code --source /path/to/.claude
```

Now for real. And that is it. The agent on this six dollar server starts with everything my Claude Code setup knows. I have not seen this command in a single one of the Hermes server videos, and it is the whole reason I would bother moving to a server at all.

[SHOW: `hermes skills list` or dashboard > Skills. The imported skills visible, including `yt-search`.]

One of those skills matters for the next step. `yt-search`. It searches YouTube with yt-dlp, no API key. We are about to give it a job that uses it.

[NOTE: transition. "Step four. The job. This is the video."]

---

## [8:45 - 13:45] The job

[SHOW: talking head for 20 seconds, then the dashboard chat.]

So, the job. I want to keep this honest. One task, one schedule, and it has to leave something behind that I can check the next day. Not a paragraph in a chat window. A file in a repo, committed, and a message telling me it is there.

The job I picked: watch YouTube for new Hermes Agent videos. Every few hours, search the term, keep track of what it has already told me, and if there is a new video over ten thousand views, write it to a file in my content repo, commit, and post a three-line summary in Slack. If nothing is new, say so in one line and stop.

That is a real job I actually want. Swap in your own. The shape is what matters: search something, remember what you saw, write it down, tell me.

[SHOW: dashboard chat. New session. Type the prompt.]

One message. Watch the whole loop.

```
Set up a scheduled job for me.

Every 4 hours: use the yt-search skill to search YouTube for "hermes agent" from the last 7 days. Compare against a list of video IDs you have already reported (keep that list in your notepad for this job). For every new video over 10,000 views, append a line to research/hermes-watch/YYYY-MM-DD.md in /root/content with the title, channel, views, and link. Commit that file with the message "hermes-watch: <date> <time>". Then post a 3-line summary to Slack #content with a link to the commit. If nothing new cleared the threshold, post one line saying so.

Name the job "hermes-watch". Deliver to Slack.
```

[NOTE: "every 4 hours" is for the video, so the overnight proof shows more than one run. Say on camera that in real life you would run this once a morning. The notepad reference maps to `hermes cron notepad`, which is a per-job KV store that survives between runs. TO VERIFY that the agent uses it when asked in plain language; if not, tell it to keep the list in a file instead.]

[NOTE: `/root/content` assumes the repo is cloned on the VPS and `gh` or a deploy key is authenticated. Do that before filming and say "I cloned my repo and authenticated GitHub on the server earlier, it is one command, link in the description." TO VERIFY: git identity set in the container, push works unattended.]

[SHOW: the agent working. It may install yt-dlp, read the skill, create the job. Let it run. Speed up the boring middle.]

So it is reading the skill, and it looks like it is installing yt-dlp because the container does not have it yet. That is fine. It is kind of the point. It sets itself up.

[SHOW: the agent confirms the job is created. Then the terminal.]

```
hermes cron list
```

There it is. hermes-watch, every 4 hours, next run at [time], delivering to Slack. Same command from the last video, just on a server now.

[SHOW: trigger it by hand.]

```
hermes cron run hermes-watch
```

I am not going to wait four hours on camera, so I am triggering the first run by hand. Watch three places: the terminal, the repo, and the phone.

[SHOW: split or quick cuts. Logs scrolling. Then GitHub: a new commit "hermes-watch: 2026-09-XX 14:32". Then the phone: a Slack post with three lines and a link.]

There is the run. There is the commit. And there is the phone. Three places, one job, nobody typed anything.

[SHOW: open the file on GitHub. Real video titles, channels, view counts.]

Open the file. Real videos, real numbers, from ten minutes ago. Now, will it be right every time? No. It is an LLM doing a search. Expect it to miss things and occasionally double-report. That is what the notepad and the threshold are for. You nudge it. You do not babysit it.

[SHOW: `hermes cron runs hermes-watch`.]

One more, because I like this one. `hermes cron runs` shows you every attempt, when it ran, and whether it worked. This is what we check tomorrow.

[NOTE: transition. Stand up. "Okay. Now the part that matters."]

---

## [13:45 - 14:15] Close the laptop

[SHOW: talking head. Then actually close the laptop on camera. Hold on the closed lid for two seconds. Cut to black or a clock.]

So here is what I am going to do. Nothing. I am going to close this laptop, and I am going to go to bed. The job is scheduled for every four hours. If this works, by tomorrow morning there should be four or five runs in Slack, four or five commits in the repo, and I will not have touched any of it.

See you tomorrow.

[NOTE: the cut. Overlay the date and time. Next scene overlays the next morning's date and time.]

---

## [14:15 - 17:15] Next morning

[SHOW: filmed the next day. Phone first. Slack #content. Scroll the overnight thread slowly. Read the timestamps out loud.]

Okay. Next morning. Phone first, before I open anything.

[Read them.] Six PM. Ten PM. Two AM. Six AM. [N] runs. Two of them said "nothing new," which is what I want, and [N] found something.

[SHOW: tap one. The summary. The link to the commit.]

[SHOW: GitHub on the phone or the Mac. The commit list. Overnight timestamps.]

And the repo. Same timestamps. Every run that found something left a commit. The laptop was closed for all of these.

[SHOW: open the Mac. Open the Hermes desktop app. Settings > Gateway.]

Now here is the part I said I was holding. The desktop app on this Mac has been talking to the local agent this whole time. It can also talk to the one on the server.

[SHOW: Settings > Gateway > Remote Gateway (or Settings > Gateways > Add connection > Remote gateway, depending on the app version). Paste the dashboard URL. Session token if asked. Save. Restart the app if it asks.]

Settings, Gateway, Remote Gateway. Paste the dashboard URL from the server. Save. It may ask you to restart the app.

[NOTE: TO VERIFY on the actual app version. Hostinger's support doc (09-21) says Settings > Gateway > Remote Gateway > paste URL > Save > restart app. The Nous docs for the multi-connection desktop say Settings > Gateways > Add connection > kind Remote gateway > name + Gateway URL + session token > Test > Reachable. Film whichever the installed version shows and say the menu path you see.]

[SHOW: the sessions list refreshes. The overnight cron sessions are there. Click one. The full transcript of a run that happened at 2am.]

And there it is. Same sessions. This is the 2am run, the whole transcript, what it searched, what it wrote, the commit it made. From my Mac, which was closed at 2am.

So what you have now is one agent, on a server, and three ways in. Slack on the phone. The desktop app on the Mac. And the web dashboard from anywhere. All the same memory, same skills, same jobs.

[SHOW: type a message in the desktop app to the remote agent: "What did you find overnight? One line per run."]

And I can just ask it. [Read the reply.]

[NOTE: if the desktop app on Tyler's version does not support a second gateway cleanly, fall back to the web dashboard on the Mac and say "the desktop app can do this too, the menu is under Settings, Gateway; I will show that in a follow-up." Do not fake it.]

[NOTE: transition. "Two quick things before we wrap. What it cost, and what to do when it breaks."]

---

## [17:15 - 18:30] Cost and troubleshooting

[SHOW: OpenRouter > Activity. Real numbers after the overnight runs.]

Cost. This is the Activity page after [N] runs overnight plus everything we did on camera. [N] requests, [N] tokens, [N] cents. Most of the tokens are cache hits because the system prompt does not change between runs. So a job like this is pennies a day. The server is the real cost, and it is [$X] a month.

[SHOW: dashboard > Logs. Then Restart Gateway. Then Docker Manager > restart.]

Troubleshooting, three tiers. If Slack goes quiet: dashboard, Logs, filter to gateway, see what it says. If it is stuck: Restart Gateway, one button. If that does not do it: Docker Manager, restart the container. The bigger hammer. And in the web console, `hermes doctor` prints a health report if you want the full picture.

[SHOW: `hermes cron doctor`.]

And one specifically for scheduled jobs: `hermes cron doctor`. It checks the jobs for the common problems, wrong schedule, gateway not ticking, skill missing.

---

## [18:30 - 19:15] Close

[SHOW: talking head.]

So that is the whole thing. A server, your Claude Code setup on it, one job, and a morning where you did not do the work.

The job I picked is a YouTube watcher because that is my repetitive thing. Yours is probably different. A repo you want checked every morning. A site you want watched for a price change. An inbox you want triaged before you sit down. The shape is the same every time: search something, remember what you saw, write it down, tell me.

Pick one. Small. Put it on a schedule tonight, and check your phone tomorrow.

Tell me in the comments what job you would put on a server first. I read every one. And if you have not done the base setup yet, the last video is the one to start with, it is linked below.

See you in the next one.

[SHOW: end card, 057 on the left.]
