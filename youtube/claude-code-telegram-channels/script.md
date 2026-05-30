# Script: Claude Code Just Got a Phone Number (Telegram Channels)

**Target runtime:** 8–10 minutes
**Format:** Tutorial + Demo + Lifestyle angle

---

## [0:00 – 0:20] HOOK

[SHOW: Phone screen in hand, Telegram open, message being typed]

> "Normally, to use Claude Code you have to be at your terminal. Sitting at your desk. Logged in. Present.
>
> But this morning — while I was running — I pulled out my phone, texted Claude Code, and got my fitness stats back. My YouTube research done. A social post ready to publish.
>
> All from Telegram. While I was mid-run."

[NOTE: Cut fast here — don't let this breathe too long. Show the phone response coming in.]

---

## [0:20 – 1:15] DEMO FIRST

[SHOW: Live Telegram demo — phone screen recording. Send a message, watch it process, response comes back.]

> "Let me just show you right now."

[NOTE: Run a real skill live — either `/fitness show` or a quick `yt-search` command via Telegram. Keep narration minimal here — let the demo speak.]

> "I literally did this during my half marathon this morning. Sent a message. Got the data back. Didn't open my laptop once."

[SHOW: Response in Telegram — real structured data or summary from your fitness skill]

> "That's Claude Code Channels. It's an official new feature from Anthropic — just dropped March 20th. And I'm going to show you exactly how to set it up."

---

## [1:15 – 1:49] RESULTS + ONE MORE THING

[SHOW: Second demo — run another skill or show a different use case message thread]

> "And it's not just fitness. I can run any of my custom Claude Code skills from Telegram. YouTube research. Content posts. Nutrition check. Anything I've built — all accessible from my phone."

[NOTE: If you have a thread of multiple exchanges, scroll through it here to show the range.]

> "I'm Tyler Reed. I make videos about using AI tools to actually run your life — not just your code. Today: Claude Code Channels."

[NOTE: Brief title card/transition here if you use one]

---

## [1:49 – 2:10] ONE-SENTENCE OVERVIEW

> "Here's the one-sentence version: You pair a Telegram bot to Claude Code, and it's like giving your AI a phone number. Anyone you authorize can text it — including you — and it runs whatever you ask."

[SHOW: Simple diagram or text overlay: Telegram → Bot → Claude Code → Skills → Response back]

> "It's persistent. It's native notifications. It works with your full skills library. Let's set it up."

---

## [2:10 – 3:30] SETUP WALKTHROUGH

[SHOW: Screen recording of setup steps — clean desktop]

### Step 1: Create Your Bot (30 seconds)

> "Open Telegram. Search for @BotFather — that's Telegram's official bot for creating bots."

[SHOW: Telegram → search BotFather → /newbot command]

> "Send /newbot. Give it a display name — I called mine ClaudeCodeBot. Then give it a username that ends in 'bot'."

[SHOW: BotFather returning the token]

> "It gives you a token. Copy that. You'll need it in the next step."

### Step 2: Install the Plugin

> "Jump to Claude Code. Run this command:"

[SHOW: Terminal]
```
/plugin install telegram@claude-plugins-official
```

> "This is the official Anthropic plugin. Then configure it with your token:"

[SHOW: Terminal]
```
/telegram:configure YOUR_TOKEN_HERE
```

### Step 3: Relaunch with the Channel Flag

> "Now exit Claude Code and relaunch with this flag:"

[SHOW: Terminal]
```
claude --channels plugin:telegram@claude-plugins-official
```

> "This is the step most people will miss. You have to relaunch with that flag — it's what activates the channel listener."

### Step 4: Pair Your Phone

> "Now go back to Telegram. DM your bot. It'll send you a 6-character pairing code."

[SHOW: Telegram — bot responding with pairing code]

> "Take that code, jump back to Claude Code, and run:"

[SHOW: Terminal]
```
/telegram:access pair XXXXXX
```

> "That's it. Four steps. You're paired."

[NOTE: Pause here — let the simplicity land.]

---

## [3:30 – 5:30] THINGS TO KNOW

[SHOW: Switch to talking head or slide-style points]

### It runs ANY skill

> "The first thing to know — this isn't just for asking questions. It runs your full Claude Code skills library."

[SHOW: Quick demo of running a skill via Telegram — `/fitness show` or similar]

> "Whatever you've built — your custom skills, your automations — they're all accessible from Telegram now."

### It's persistent — no session URL needed

> "Remote Control was great, but it required an active session. You'd start it at your desk, scan a QR code, and if the session timed out you'd have to reconnect."

> "Channels is different. It's always running. You don't need to be at your computer to start it. As long as Claude Code is running on your machine, Telegram is connected."

### Native push notifications

> "This is the one that gets me. When a long-running task finishes — say I ask Claude to do research or draft something — Telegram pings my phone natively. Not a web notification. A real Telegram notification."

> "Fire and forget. Start a task. Go for a run. Get pinged when it's done."

### Access control — it's secure

> "Quick security note because I know people will ask. By default, it uses pairing mode — strangers can't just message your bot and have Claude do stuff for them."

> "Once you've paired your phone, switch to allowlist mode:"

[SHOW: Terminal]
```
/telegram:access policy allowlist
```

> "Now only the IDs you've approved can reach it. Anyone else gets ignored."

### Send images, get files back

> "You can send images to Claude through Telegram — photos of nutrition labels, screenshots of anything — and get files back. It's a full two-way channel."

---

## [5:30 – 7:00] REAL USE CASE DEMOS

[SHOW: Phone demos — real Telegram thread]

> "Let me show you how I actually use this."

### Use case 1: Fitness mid-run

[SHOW: Telegram → typing "log workout: 13.1 miles, half marathon" → response]

> "This morning I logged my half marathon from Telegram. Hit send at mile 13. Done. No app. No laptop."

### Use case 2: YouTube research

[SHOW: Telegram → "run yt-search nutrition" → response with top videos]

> "I can kick off YouTube research from my phone. By the time I'm back at my desk, the report's ready."

### Use case 3: Content posting

[SHOW: Telegram → "post today's fitness update to Twitter" → Claude drafts + posts]

> "I can trigger a social post. Draft it, review it, confirm. All in Telegram."

### Use case 4: Ask anything async

> "Or just ask Claude to do something while you're away. 'Research competitors for my next video.' 'Summarize this PDF.' 'Draft a Skool post from my last YouTube video.' You come back and it's done."

[NOTE: Keep each use case short — 15-20 seconds each. Fast cuts.]

---

## [7:00 – 7:50] WHY THIS IS EXCITING

[SHOW: Talking head — more energy here]

> "Here's the thing about Remote Control. It was cool. It worked. But it was designed around a session model — you're still tethered to an active connection."

> "Channels is architecturally different. Your bot doesn't need you present. It's persistent. It runs skills, it pushes notifications, and it's extensible — Discord is already supported too, with more platforms coming."

> "But the bigger picture? This is what 'AI in your pocket' actually looks like. Not a chat app. Not a mobile version of a tool. An AI that runs your workflows, from your phone, asynchronously, while you're living your life."

> "That's a different paradigm. And I think this is just the beginning."

---

## [7:50 – 8:20] CTA

[SHOW: Talking head — direct to camera]

> "If you're using Claude Code, this is worth setting up today. It's five minutes, it's official from Anthropic, and it opens up a whole different way of working."

> "If you want to go deeper — I've got a community where I share exactly how I build these skills and workflows. Link's below."

> "Give this a like if it helped, subscribe if you want to keep up with what's actually moving in AI tools, and I'll see you in the next one."

[SHOW: End card]
