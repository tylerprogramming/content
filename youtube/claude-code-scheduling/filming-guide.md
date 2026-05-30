# Filming Guide: Claude Code Scheduling

## Pre-Recording Setup

**Before you hit record:**
- [ ] Clean up terminal — close extra tabs, use a fresh window
- [ ] Have Claude Code desktop app open with the Schedule tab visible
- [ ] Pre-run the yt-search skill so you have an example output file ready to show
- [ ] Pre-run the Gmail skill so you have an example digest file ready
- [ ] Have the overnight task log ready to show (the "woke up to this" moment at the start)
- [ ] Set terminal font size large enough to read on screen (18-20pt minimum)
- [ ] Close Slack, email, notifications — no pings on screen
- [ ] Get ElevenLabs account + API key if demoing the audio step live

---

## Timing Cheat Sheet

| Section | Target | Running Total |
|---------|--------|---------------|
| Hook | 0:35 | 0:35 |
| What scheduling is | 1:10 | 1:45 |
| Demo 1: yt-search | 1:45 | 3:30 |
| Demo 2: Gmail digest | 2:00 | 5:30 |
| Demo 3: Audio briefing | 3:00 | 8:30 |
| Limitations + how to start | 1:00 | 9:30 |
| CTA | 0:30 | 10:00 |

---

## Step-by-Step Filming

### STEP 1 — Hook shot (pre-recorded output)

**What you do:** Show a real overnight run log. This is the "woke up to this" moment.

**What to show:** A terminal or file explorer with a timestamped output file — dated from early morning (6am-ish). Open the file briefly so viewers can see it's real research.

> **Say:** "Last week I woke up, made coffee, and Claude Code had already done three hours of research while I slept..."

**Key:** Make this feel real. Don't use a freshly-run file — use one that's actually timestamped from overnight or early morning.

---

### STEP 2 — Explain `/loop` (60 seconds max)

**What you do:** Open a fresh Claude Code terminal session.

```bash
claude
```

**What to say while it loads:**
> "Claude Code has a built-in scheduling system. It's called the loop command. Instead of you typing a prompt and waiting — you tell it to run something on a schedule."

**Type this to show the format:**
```
/loop 24h search YouTube for top claude code videos today and save a report to research/
```

**What to say:**
> "You give it an interval — every hour, every day — and a prompt. That's it. And what makes this different from a Python script is this is a Claude Code *agent* running. If it hits a problem, it figures it out. It doesn't crash."

**[NOTE: Don't let it actually run — cancel after showing the format. Move to the real demos.]**

---

### STEP 3 — Demo 1: Competitor YouTube Research

**What you do:** Show the `/yt-search` skill running, then show a scheduled version.

**Step 3a — Run it live first:**
```bash
/yt-search claude code --days 7
```

> "So I have this skill — yt-search — that pulls YouTube data by keyword and ranks it. Watch what it does..."

**Fill dead air while it runs:** Talk about what you use this for — spotting trending angles, seeing what's performing, noticing title patterns.

**Step 3b — Show the output:**
Open the generated report file.
> "This is what I get — ranked by views, with titles, channels, and dates. I use this to figure out what to make next."

**Step 3c — Schedule it:**
```
/loop 24h run the yt-search skill for "claude code" and save the report to ~/research/daily-yt-report.md
```

> "Now I just schedule it. Every morning at 7am, fresh report waiting for me. I didn't write a single line of code."

---

### STEP 4 — Demo 2: Gmail Research Digest

**What you do:** Show the Gmail skill, then schedule it.

**Step 4a — Show the skill:**
```bash
/gmail search newsletters from the last 24 hours --body
```

> "Second workflow. I subscribe to newsletters — Creator Hooks, AI research digests. I never read them when they land. So I have Claude read them for me overnight."

**Fill dead air:** Talk about email overload — everyone relates to having a pile of unread newsletters.

**Step 4b — Show example output:**
Open the pre-generated digest file.
> "Here's what it produces — three newsletters, key takeaways, what's relevant to my content. One clean file."

**Step 4c — Schedule it:**
```
/loop 24h run the gmail skill to search for newsletters from the last 24 hours and save a summary digest to ~/research/daily-email-digest.md
```

> "Scheduled. Runs every morning before I wake up. My inbox does the work so I don't have to."

---

### STEP 5 — Demo 3: Morning Audio Briefing (Hero)

**This is the wow moment — slow down, let it land.**

**Step 5a — Set up the concept:**
> "Okay. This one is the one I'm most excited to show you. The first two were useful. This one feels like something from the future."

**Step 5b — Show the prompt you use:**

```
/loop 24h Search the web for news about AI tools, Claude Code, and the creator economy published in the last 24 hours. Summarize the top 5 stories into a 2-minute morning briefing script. Then call the ElevenLabs API with the script and save the audio to ~/research/morning-briefing-[date].mp3
```

> "I have a task that runs at 5:30am. It searches the web for anything in my niche from the last 24 hours. Synthesizes the top stories. Then calls ElevenLabs and turns it into audio."

**Step 5c — Show the output folder:**
Open `~/research/` and show the dated MP3 file sitting there.
> "When I wake up — there it is. Dated MP3, ready to play."

**Step 5d — Play the audio:**
Press play on the file.
> "I just press play while I'm making coffee. Two minutes. Everything I need to know."

**[NOTE: If ElevenLabs isn't set up yet — show the text briefing output and narrate it yourself on camera. Say: "Here's the script it generates — I'm still setting up the audio piece, but you get the idea."]**

**Step 5e — Pause and let it land:**
> "Three API calls. One prompt. Twenty minutes to build. And every single morning I get a custom research briefing for my exact niche. Without touching anything."

---

### STEP 6 — Limitations (be honest, keep it fast)

**What to show:** Claude Code desktop app, Schedule tab.

> "Okay — a few honest things. Your computer needs to stay on. This runs locally, so if your laptop sleeps, the task waits. When you open back up, it catches up — runs anything it missed in the last 7 days."

> "Tasks also auto-expire after 3 days. Safety feature. For anything long-term, just recreate it — takes 30 seconds."

**Show one quick recreation:**
Click New Task → fill in the same prompt → done.

---

### STEP 7 — How to Start (30 seconds)

> "To try this right now: open Claude Code, type /loop, describe what you want it to do and how often. That's the basics."

**Show on screen:**
```
/loop 24h [your task here]
```

> "If you want to go deeper, build your skills first, then schedule them. I've got a full skills video linked below."

---

## On-Camera Tips

- **Energy:** This topic is genuinely exciting — let that show. The "wow" moments are real.
- **Errors on camera:** If a command fails, don't cut — say "this happens sometimes, here's how to fix it" and show the fix. It builds trust.
- **Dead air during API calls:** Have a talking point ready for each demo (listed above as "fill dead air").
- **The audio demo:** Play it confidently. Even if the voice isn't perfect — the *concept* is what lands.
- **Pacing:** Demo 3 should feel slower and more deliberate. Let the audience absorb it.

---

## Files to Have Ready Before Filming

**Pre-generated outputs to show:**
1. `~/research/daily-yt-report.md` — an actual overnight yt-search output (timestamped early AM)
2. `~/research/daily-email-digest.md` — a real Gmail digest from a previous run
3. `~/research/morning-briefing-2026-03-21.mp3` — the ElevenLabs audio output (or narrated version)

**Skills to have installed:**
- `/yt-search` — already working
- `/gmail` — already working (just built!)
- Morning briefing script — build this before filming
