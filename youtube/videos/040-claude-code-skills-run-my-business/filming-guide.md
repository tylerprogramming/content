# Filming Guide: 17 Claude Code Skills That Run My Business

The do-this / click-that playbook. Follow it top to bottom and you can film the whole thing without re-reading the script.

---

## Pre-recording setup

**Before you hit record, prep these so nothing stalls on camera:**

1. **Clean terminal** - fresh Claude Code session, `/clear` run, large readable font (18pt+). Dark theme.
2. **Status line on** - so viewers can see the model + context window (visual proof it's the real tool).
3. **Skills folder ready** - have `~/.claude/skills/` open in Finder or a file tree so you can show the 17+ folders instantly.
4. **Pick your demo topic ahead of time** - decide the `/yt-search` topic (e.g. "claude code") and have a transcript already downloaded so `/yt-package` doesn't make you wait 3+ minutes on camera. Pre-run the slow ones and cut to results.
5. **Pre-run the slow skills once** - `/yt-package` and `/social-copy` can take minutes. Run them BEFORE recording so the output folders already exist, then just show the finished files. Film the *command going in* live, cut to the *result*.
6. **Crontab visible** - have `crontab -l` output ready in a second terminal tab to prove the monitors are scheduled.
7. **Skool logged in** - browser tab on your Skool community + classroom, so the `/skool` demo lands somewhere real.
8. **One SKILL.md open** - a simple, clean example skill open in your editor for the "what is a skill" section.
9. **Draft mode confirmed** - double check `/yt-replier` and `/tiktok-replier` are in dry-run/draft mode so nothing auto-posts while filming.
10. **Hide anything private** - API keys, member emails, revenue you don't want shown. You chose NOT to put revenue on screen, so keep dashboards to counts/activity, not dollars.

---

## Step 1 - Hook + proof (0:00 - 0:35)

**What you do:** Talk to camera for the hook, then cut to the terminal and list your skills.

**Command to run on screen:**
```
ls ~/.claude/skills/
```
(or run `/help` if it shows your skill list cleaner)

> "You've probably seen a dozen videos where someone builds a fake business with Claude Code... I'm not going to do that. This is the real one. And I'm not a developer - if you can write a text file, you can build all of these."

**What happens next:** The folder list scrolls - dozens of skill names. That scroll IS the proof. Let it breathe for a second.

---

## Step 2 - What a skill is (1:30 - 2:45)

**What you do:** Switch to your editor. Open ONE simple SKILL.md. Point at the top line, then the body.

**What to show:** The YAML description line at the very top (when to use it) and the plain-English instructions below.

> "A skill is a folder with one text file in it. The top tells Claude when to use it, in plain English. The rest is just instructions - the same thing you'd tell an assistant."

**How to fill dead air:** N/A - this is talking, not waiting. Keep it slow and clear; this is the section that keeps non-coders watching.

**Do NOT:** open the frontmatter/allowed-tools rabbit hole. One sentence about "skills and slash commands are the same thing now" is plenty.

---

## Step 3 - Content pipeline (2:45 - 6:30)

### 3a - /yt-search (film live, it's fast enough)
**Command:**
```
/yt-search claude code
```
> "I don't guess what to make. This finds what's actually working right now, ranks it by views, pulls the thumbnails, and writes me a report."

**Fill dead air while it runs:** "This is the difference between hoping a video works and knowing the format works before you film."

**What happens next:** It prints a table + downloads a thumbnail grid. Show the report file and the thumbnails.

### 3b - /transcribe -> /yt-package (film command, CUT to result)
**Commands:**
```
/transcribe <url of top video>
```
```
/yt-package ~/content/scripts/transcript_<id>.txt
```
> "From one transcript it gives me a complete video plan - titles, hooks, full script, description, filming guide. The script I'm reading right now came out of this skill."

**What happens next:** [PRE-RUN THIS] Cut straight to the finished package folder. Open `titles.md`, `script.md`, `filming-guide.md` so viewers see real depth.

**Meta beat:** say out loud "this exact video was planned by this skill." It's sticky.

### 3c - /social-copy (film command, CUT to result)
**Command:**
```
/social-copy <slug>
```
> "The video isn't the end, it's the source. This turns one video into a week of posts, in my voice, because it's trained on my own transcripts."

**What happens next:** Show the generated LinkedIn / X / Instagram / community files.

**Land the before/after:** "That used to be four tools and two full days."

---

## Step 4 - Comments + email on autopilot (6:30 - 9:30)

### 4a - The monitors (the trust builder)
**What you do:** Switch to the second terminal tab. Show the actual scheduled jobs.

**Command:**
```
crontab -l
```
> "There's a job on my machine that fires every hour, finds comments I haven't replied to, and drops them in an inbox. For the easy ones it even drafts the reply."

**What to show:** The cron lines for `monitor_yt.py` / the tiktok monitor, then the inbox file and the drafts queue they produce.

**What happens next:** Open `inbox_yt.json` / `drafts_queue_yt.json` (or whatever's readable) to show real gathered comments + drafts.

> "Everything defaults to draft. Nothing posts without me. But the finding and the writing is done before I sit down."

### 4b - /email
**Command:**
```
/email
```
(show the welcome drip / a broadcast - do NOT actually send on camera unless it's a test)
> "New person joins, the welcome email goes out. I'm not in the loop."

**Callback:** "While I'm filming this, my comments are being gathered and my emails are going out. That's the business running itself."

---

## Step 5 - Skool community ops (9:30 - 11:30)

**What you do:** Run a `/skool` command that lands somewhere visible in your browser.

**Command examples (pick 1-2):**
```
/skool
```
- Write/schedule a post, OR
- Sync + show member list (counts, not private emails), OR
- Add a module to the classroom

> "I run my whole community from here. Write a post, pull my members, add a classroom module - without ever opening the website."

**What happens next:** Flip to the Skool browser tab and show the post/module actually there. That real landing is the proof.

**Emphasize:** "This is real business operations, not a toy app."

---

## Step 6 - Build a skill live (11:30 - 13:30)

**What you do:** Create a new skill from scratch, on camera, genuinely.

**Commands:**
```
mkdir ~/.claude/skills/hook-maker
```
Then create `~/.claude/skills/hook-maker/SKILL.md` and type this in live (keep it short and real):

```markdown
---
name: hook-maker
description: Turn a video topic or transcript into 3 punchy YouTube hook options. Use when I ask for hooks.
---

# Hook Maker

Given a topic or transcript, write 3 hook options for the first 15 seconds of a YouTube video.
Each hook uses a different technique: curiosity gap, bold claim, and story open.
Keep them short, spoken-word, no jargon. Match a confident, practical creator voice.
```

> "I make a folder, make a file called SKILL.md, write one line at the top for when to use it, then the instructions in plain English. Save it. That's it."

**Then run it:**
```
/hook-maker a video about claude code skills
```

**What happens next:** It returns 3 hooks. "That took two minutes. Every skill I showed you started exactly like this."

**Takeaway line (slow down):** "Every time you do a task twice, that's a skill. You stop doing the task and start reviewing the result."

---

## Step 7 - Recap + CTA (13:30 - end)

**What you do:** Back to camera.
> "That's the real system. Claude Code researches and writes my content, watches my comments and sends my email on a schedule, and runs my community. 17 skills, all text files, built by someone who isn't a developer. The skills and setup are free in my community, link's in the description."

[SHOW: end card - https://free.tylerai.dev/youtube/ + subscribe]

---

## Timing cheat sheet

| Section | Target | Running total |
|---------|--------|---------------|
| Hook + proof | 0:35 | 0:35 |
| What this is | 0:55 | 1:30 |
| What a skill is | 1:15 | 2:45 |
| Content pipeline | 3:45 | 6:30 |
| Comments + email autopilot | 3:00 | 9:30 |
| Skool ops | 2:00 | 11:30 |
| Build a skill live | 2:00 | 13:30 |
| Recap + CTA | 1:00-1:30 | ~14:30 |

---

## On-camera tips

- **Errors are content.** If a skill hiccups on camera, narrate it: "see, this is real - let me fix it." It reinforces that it's not staged. Don't panic-cut.
- **Pre-run the slow stuff.** `/yt-package` and `/social-copy` take minutes. Film the command going in, cut to the result. Never make the viewer wait.
- **The trust moment is the crontab.** Linger on it. That one screen proves the "runs while I sleep" claim.
- **Say "I'm not a developer" at least twice** - hook and build-a-skill section. It's the line that unlocks your whole audience.
- **Keep dashboards to activity, not dollars** (your call - no revenue on screen). Counts, scheduled posts, and firing jobs are proof enough.
- **Energy:** grounded and confident, not hyped. The edge of this video is that it's true, so let the proof carry it.
- **Visual variety:** rotate between talking-head, terminal, editor, browser (Skool), and the file tree. Don't sit on the terminal for 5 minutes straight.
