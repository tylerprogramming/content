# Filming Guide: Claude Code Just Got a Phone Number

**Target runtime:** 8–10 minutes
**Format:** Talking head + screen recording + phone demo

---

## Pre-Recording Setup

### Environment prep
- [ ] Clean desktop — close all apps except Terminal + Telegram
- [ ] Set terminal font to 18pt+ — readable on YouTube at all sizes
- [ ] Telegram open on phone AND Mac (for easy screen recording)
- [ ] Claude Code running with channels: `claude --channels plugin:telegram@claude-plugins-official`
- [ ] Test your bot: send a test message from Telegram, confirm it responds
- [ ] Have your fitness skill ready to demo (`/fitness show` or similar)
- [ ] Have a yt-search query ready to run from Telegram

### Phone setup
- [ ] iPhone screen recording enabled (Control Center)
- [ ] Telegram notifications turned ON (you want the ping sound on camera)
- [ ] Airplane mode OFF — needs real internet
- [ ] Do Not Disturb OFF — want notifications to show
- [ ] Telegram chat with your bot open and ready

### Files to have ready
None needed — all demos are live.

---

## Timing Cheat Sheet

| Section | Target | Running Total |
|---------|--------|---------------|
| Hook | 0:20 | 0:20 |
| Demo first | 0:55 | 1:15 |
| Results + intro | 0:34 | 1:49 |
| One-sentence overview | 0:21 | 2:10 |
| Setup walkthrough | 1:20 | 3:30 |
| Things to know | 2:00 | 5:30 |
| Use case demos | 1:30 | 7:00 |
| Why it's exciting | 0:50 | 7:50 |
| CTA | 0:30 | 8:20 |

---

## Step-by-Step Filming

---

### STEP 1 — Hook (0:00 – 0:20)
**Camera:** Talking head OR phone in hand showing Telegram

**What you do:** Hold your phone so the screen is visible. Have the Telegram chat with Claude open.

**What you say:**
> "Normally, to use Claude Code you have to be at your terminal. Sitting at your desk. Logged in. Present. But this morning — while I was running — I pulled out my phone, texted Claude Code, and got my fitness stats back. My YouTube research done. A social post ready to publish. All from Telegram. While I was mid-run."

**On-camera tip:** Look slightly past camera, like you're sharing something you're genuinely excited about. The contrast setup ("normally... but now") needs to land with energy — don't rush through it.

---

### STEP 2 — Demo First (0:20 – 1:15)
**Camera:** Phone screen recording (use iPhone screen record + mirror to Mac for capture, OR record phone screen directly)

**What you do:**
1. Open Telegram on phone
2. Type: `check my fitness stats` or `run /fitness show`
3. Hit send — let it process
4. Show the response coming back with real data

**What to say while waiting:**
> "I literally did this during my half marathon this morning. Sent a message. Got the data back. Didn't open my laptop once."

**What happens next:** Claude processes the request, runs your fitness skill, replies in Telegram with the structured output.

**What to say after response:**
> "That's Claude Code Channels. It just dropped March 20th. Let me show you how to set it up."

**On-camera tip:** If there's a 10–15 second processing delay, fill with the half marathon line — it's authentic dead air. Don't cut it.

---

### STEP 3 — Results + More (1:15 – 1:45)
**Camera:** Stay on phone screen OR cut to second demo

**What you do:** Run a second quick demo OR scroll through your Telegram thread to show the range of what's possible.

**What to say:**
> "And it's not just fitness. I can run any of my custom Claude Code skills from Telegram. YouTube research. Content posts. Nutrition check. Anything I've built — all accessible from my phone."

Then:
> "I'm Tyler Reed. I make videos about using AI tools to actually run your life — not just your code. Today: Claude Code Channels."

---

### STEP 4 — Overview (1:49 – 2:10)
**Camera:** Talking head

**What you say:**
> "Here's the one-sentence version: You pair a Telegram bot to Claude Code, and it's like giving your AI a phone number. Anyone you authorize can text it — including you — and it runs whatever you ask."

**On-camera tip:** The metaphor ("phone number") is your hook phrase. Slow down on it slightly. Let it land.

---

### STEP 5 — Setup: BotFather (2:10 – 2:40)
**Camera:** Screen recording — Telegram desktop or phone

**What you do:**
1. Search for `@BotFather` in Telegram
2. Click the verified account
3. Type `/newbot` and send
4. When asked for name: type your bot's display name (e.g., `ClaudeAssistant`)
5. When asked for username: type a unique name ending in `bot` (e.g., `tyler_claude_bot`)
6. Copy the token BotFather returns

**What you say:**
> "Open Telegram. Search for BotFather — that's Telegram's official bot for creating bots. Send /newbot. Give it a display name... then a username that ends in 'bot'."

[SHOW: Each step clearly — zoom in on token if possible]

> "It gives you a token. Copy it. Keep it private — this is the key to your bot."

**Timing:** This should take ~30 seconds of screen time. Speed up the typing if needed in editing.

---

### STEP 6 — Plugin Install + Configure (2:40 – 3:05)
**Camera:** Terminal screen recording

**What you type:**
```
/plugin install telegram@claude-plugins-official
```
Then:
```
/telegram:configure YOUR_TOKEN_HERE
```

**What you say:**
> "Back in Claude Code, run this install command. Then configure it with your token."

**What happens next:** Plugin installs, token is saved locally. Claude confirms configuration.

---

### STEP 7 — Relaunch with --channels Flag (3:05 – 3:20)
**Camera:** Terminal

**What you do:**
1. Exit current Claude Code session (Ctrl+C or `/exit`)
2. Relaunch:

```
claude --channels plugin:telegram@claude-plugins-official
```

**What you say:**
> "Now exit Claude Code and relaunch with this flag. This is the step most people miss. You have to relaunch — this is what activates the channel listener. Without it, Telegram is connected but nothing responds."

**On-camera tip:** Emphasize the `--channels` flag visually — zoom in or highlight it. This is the gotcha moment.

---

### STEP 8 — Pair Your Phone (3:20 – 3:30)
**Camera:** Split — phone Telegram + terminal

**What you do:**
1. DM your bot on Telegram ("hi" is enough)
2. Bot responds with a 6-character pairing code
3. In terminal:
```
/telegram:access pair XXXXXX
```

**What you say:**
> "Now DM your bot. It sends you a 6-character pairing code. Take that code, run this in Claude Code, and you're paired. That's it — four steps, done."

---

### STEP 9 — Things to Know (3:30 – 5:30)
**Camera:** Talking head with occasional screen cuts for demos

**Points to hit (in order):**

1. **Runs any skill**
> "This isn't just for questions. Your full skills library is accessible — anything you've built in Claude Code, you can trigger from Telegram."

[SHOW: Quick Telegram demo of running a skill]

2. **Persistent — no session needed**
> "Remote Control required an active session. Channels doesn't. As long as Claude Code is running on your machine, the bot is live. No QR code. No reconnecting."

3. **Native push notifications**
> "When a long task finishes — Claude pings your phone. Native Telegram notification. Fire a job, go do something, get notified when it's done."

4. **Security — switch to allowlist**
> "By default it uses pairing mode. Once you've paired, run this to lock it down:"

[SHOW: Terminal]
```
/telegram:access policy allowlist
```

> "Now only you can reach it."

5. **Send images, get files back**
> "Two-way channel. You can send a photo of a nutrition label, Claude reads it. You can get documents back. Not just text."

---

### STEP 10 — Use Case Demos (5:30 – 7:00)
**Camera:** Phone screen recording, fast cuts

**Demo 1 — Fitness**
- Type: `log workout: half marathon, 13.1 miles`
- Show response

> "This morning I logged my half marathon from Telegram. Hit send at mile 13."

**Demo 2 — YouTube research**
- Type: `run yt-search for nutrition videos last 30 days`
- Show response with top videos list

> "I can kick off research from my phone. Report's ready by the time I'm back at my desk."

**Demo 3 — Social post**
- Type: `draft a tweet about this morning's half marathon`
- Show Claude's draft response

> "Draft a post, review it, approve it. All in Telegram."

**On-camera tip:** Keep these snappy. 15–20 seconds each. Don't over-explain. The demo is the point.

---

### STEP 11 — Why It's Exciting (7:00 – 7:50)
**Camera:** Talking head — more energy

**What you say:**
> "Remote Control was designed around a session model. You're still tethered. Channels is architecturally different — persistent, notification-driven, extensible."

> "Discord is already supported. More platforms are coming. The plugin system is open."

> "But the bigger picture? This is what 'AI in your pocket' actually looks like. Not a chat app. An AI that runs your workflows, from your phone, asynchronously, while you're living your life."

> "That's a different paradigm."

**On-camera tip:** This is the most opinionated section — let your genuine excitement out. You've been using this live. The half marathon angle is real. Let it be personal.

---

### STEP 12 — CTA (7:50 – 8:20)
**Camera:** Talking head — direct eye contact

> "If you're on Claude Code, set this up today. Five minutes. It's official from Anthropic. It changes how you work."

> "Link to my community is below — that's where I share how I build all of these workflows."

> "Like if it helped. Subscribe if you want more. See you in the next one."

---

## On-Camera Tips

- **Energy on the hook** — the contrast setup is everything. Don't blow through it.
- **Let processing time breathe** — dead air while Telegram responds is authentic. Fill with a genuine aside, not scripted lines.
- **Phone demos** — film these in portrait on a stable surface OR use iPhone mirror via USB to record phone screen on Mac. Either works.
- **The `--channels` flag** — circle it or zoom in when it appears on screen. It's the one step people will pause on.
- **If something breaks on camera** — say "let me try that again" and do it. Don't hide it. Authenticity > polish for this audience.
- **Pacing** — this audience knows Claude Code. Don't over-explain basics. Trust that they get it.
