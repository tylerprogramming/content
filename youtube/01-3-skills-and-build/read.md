# READ COPY — 3 Skills + Live Build

**Glance version. Quotes = say close to verbatim. Bullets = riff in your words.**
**Length ~32 min · Energy: demos relaxed, payoffs UP, CTA UP · No em dashes**
**Demo continuity: same Alberta Tech URL flows through all 3 skills**

---

## 0:00 — HOOK (energy 10)

▶ On screen: three terminals running in parallel (yt-search, transcribe, yt)

> "Research, transcripts, video packages. Three Claude Code skills, three outputs. Total time, about 8 minutes."

> "I'm going to show you all three working, then build a brand new one from scratch, live on camera. By the end you'll know what a Claude Code skill can do and how to build your own."

*(Let the visual breathe ~3 sec before you talk.)*

---

## 0:25 — SETUP (energy 7) · keep under 90 sec

- Full-time software engineer. Wife and kids. Content gets made 4–5:30 PM weekdays, a few hours on weekends. That's the budget.
- Not full-time on content? You have to be ruthless about leverage. Skills are how I get leverage out of Claude Code.
- Built 43 of them. Most are experiments. About 7 I use every week.
- Today: the 3 that kick off every Monday. A complete pipeline — research, input, output. Then I build a brand new one, `/meeting-notes`, in front of you.

> "Let's start with the one that kicks everything off."

---

## 1:45 — SKILL 1: /yt-search (energy 6 → 8)

**TYPE:**  `/yt-search claude code`

Setup line:
> "Every Monday at 4 PM I plan two videos. The first question isn't 'what should I make?' It's 'what's actually working right now in my space?'"

> "If you don't answer that first, you're guessing. And guessing is how channels die before they ever get traction."

Beats while it runs (~60 sec):
- Whole command is just the keyword
- Under the hood: yt-dlp, last 30 days, sorted by views, downloads thumbnails, saves a markdown report

▶ Open the report:
- 33 videos, last 30 days, sorted by views
- See title formulas, who's making them, what durations hit — in 30 seconds

▶ Open thumbnails folder:
- Alberta Tech "Well... that explains it" — face left, text right — doing 413,000 views right now

PAYOFF:
> "This used to take 2 hours a week of clicking around YouTube. Now it's 60 seconds."

> "And this report is the input to every other skill in my pipeline. Garbage in, garbage out. Research is the moat."

> "Skill 1 of 3. Done. On to the second."

---

## 7:30 — SKILL 2: /transcribe (energy 6 → 8)

**TYPE:**  `/transcribe https://youtube.com/watch?v=LACyqdAfnaw`
*(the Alberta Tech video from the search above — keep continuity)*

Setup:
> "Once I know what's working, I need to study the actual content. Watching a 30-minute video to take notes is a waste when I can just read it."

Beats while it runs (~90 sec):
- Paste any YouTube URL
- Downloads audio with yt-dlp, runs it through OpenAI Whisper, saves the transcript

▶ Open the transcript:
- Full transcript with timestamps. Read the whole video in 5 minutes.

**TYPE into chat:**
`read [transcript] and tell me the hook, the 3 main beats, and the CTA in bullet form`

- 30 seconds of reading → I have the structure. Riff on it, beat it, or steal it.

PAYOFF:
> "Most creators watch their competitors. I read them. I can process 5 competitor videos in the time it takes someone to watch one."

- Bonus: a corrections file auto-fixes Whisper mishears — "Cloud" → "Claude," "Appify" → "Apify." Set once, runs forever.

> "Skill 2 done. On to the heavy lifter."

---

## 13:30 — SKILL 3: /yt (energy 6 → 9, biggest payoff)

**TYPE:**  `/yt ~/content/transcripts/transcript_LACyqdAfnaw.txt`

Setup:
> "Skill 3 does the most work. Most people sit down with a blank doc and start typing. I never start with a blank doc. I run /yt with a transcript, and 5 minutes later I have a complete video package."

▶ It asks a clarifying question — ANSWER ON CAMERA:
> "See that? It asked my angle. My take. Because if I skip this, the script sounds like every other one."

**TYPE the answer:**
`Technical / creator angle. I'll show actual commands and skills, not just talk about Claude Code at a high level.`

Watch the folder fill — name them as they land:
- analysis.md · titles.md (10 scored) · hooks.md (4 to test) · script.md (word for word) · description.md · filming-guide.md

PAYOFF:
> "This used to be my entire weekend. Saturday morning to Sunday night, exhausted. Now it's 5 minutes."

The thing to internalize:
> "The skill isn't writing the video for me. It's writing the 80% draft I edit and personalize. I still bring the stories, the takes, the recording. But I never start from zero. Ever."

> "That's the difference between people who publish 1 video a month and people who publish 8."

> "Three skills, complete pipeline. Monday morning, 90 minutes, two videos planned for the week."

---

## 21:30 — THE AHA (energy 10) · SCREENSHOT MOMENT · slow down

▶ Open all three SKILL.md files side by side (yt-search, transcribe, yt)

> "Pause for one second. Look at what you just watched. Three skills, different jobs, different outputs."

> "All three — same format. A markdown file. 50 to 100 lines each. Frontmatter on top, plain English below."

> "No SDK. No framework. No plugin install."

(direct to lens, energy up)
> "Let me build a brand new one in front of you right now. From scratch. About 7 minutes."

---

## 22:30 — LIVE BUILD: /meeting-notes (energy 7 → 9)

▶ Empty folder: `~/.claude/skills/meeting-notes/`

> "Empty folder. We're building /meeting-notes — type the command with a topic, Claude generates a meeting template with agenda, action items, decisions, and saves it. Touches every concept: frontmatter, arguments, asking a question, writing a file. Watch."

**TYPE the frontmatter LIVE** (SKILL.md):
```yaml
---
name: meeting-notes
description: Generate a meeting note template with agenda, action items, and decisions. Triggers on - meeting notes, take notes, meeting template.
argument-hint: [topic]
allowed-tools: Read, Write, Bash(date:*), AskUserQuestion
user-invocable: true
---
```
- Five fields. Name matches folder. Description tells Claude when to fire. Argument-hint shows what to pass. Allowed-tools, keep minimal. User-invocable makes it a slash command.

**PASTE the body** (ok to paste for speed):
```markdown
# Meeting Notes Skill

Generate a structured meeting notes template based on a topic the user provides.

## What to Do
1. If no topic, ask with AskUserQuestion: "What's this meeting about?" — options 1:1, Team sync, Customer call, Other.
2. Get today's date: `date +%Y-%m-%d`.
3. Create markdown: Title (h1), Date, Attendees (blank), Agenda (3 bullets), Decisions (empty), Action items (empty + one example "- [ ] Owner: Action - Due: date"), Notes (empty).
4. Save to `~/notes/meetings/<date>-<slug>.md`. Slug = topic lowercased, spaces to hyphens.
5. Confirm the saved path.

## Rules
- Use today's actual date from `date`, not hardcoded.
- Never overwrite. If slug exists, append -2, -3.
- No em dashes, use regular hyphens.
```
- Plain English. No code. Body tells Claude what to do. Rules section prevents it doing something dumb later.

**Save → restart Claude Code** (so it picks up the skill)

**TYPE:**  `/meeting-notes`
- It hits AskUserQuestion → pick "Team sync"
- Claude calls date, generates file, confirms path

▶ Open the file — point at each part:
- Title. Today's date. Attendees blank. Three agenda bullets. Decisions empty. Action items example row. Notes blank. Exactly what I described in plain English.

▶ Run it again, same topic → shows `-2` appended:
- "Rule worked — second run got -2 instead of overwriting."

THE AHA (face to camera, let it land 2–3 sec):
> "That's it. About 50 lines of YAML and English. No code, no SDK. Now I have a slash command that does a real, useful task forever."

> "Every skill in my system works exactly like this. The three at the start — same format. Longer body, more tools, same structure."

> "Once you get this, the floodgates open. You stop thinking 'how do I automate this' and start thinking 'what's the skill called and what should the body say.'"

---

## 29:30 — 3 PATTERNS (energy 7) · tight

▶ On-screen text for each pattern name

> "Three patterns make every skill robust. You'll use these forever."

- **One — Ask when input is missing.** Don't error out. AskUserQuestion. The skill becomes forgiving.
- **Two — Write to predictable paths.** Meeting notes → `~/notes/meetings/`. Videos → `~/content/youtube/<slug>/`. Consistent paths let skills cooperate.
- **Three — Put rules at the bottom.** "Never overwrite." "Always confirm." "No em dashes." Rules prevent disasters.

> "Ask when missing. Predictable paths. Explicit rules. That's 80% of what makes a skill robust."

---

## 31:00 — CTA (energy 10) · get the click

> "Want all three skills you just saw — /yt-search, /transcribe, /yt — plus the /meeting-notes SKILL.md we just built, plus 5 more starter templates I'd build next? They're in my free Skool community."

> "Link's in the description. Join the waitlist for the full Claude Code skills course I'm building. That's it. See you in the next one."

---

### Pre-flight (do before you hit record)
- [ ] Delete `~/.claude/skills/meeting-notes/` — must be a fresh build
- [ ] Clear `~/notes/meetings/` of real notes
- [ ] Run `/yt-search claude code` this morning so results are fresh
- [ ] Smoke-test `/transcribe` on a short URL · `/yt` on a recent transcript
- [ ] Have the transcribe URL + meeting-notes body in a paste doc
- [ ] Don't show .env or any API keys
