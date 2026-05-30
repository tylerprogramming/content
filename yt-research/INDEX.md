# File Index — Where Everything Lives

This is the evergreen front door for the YouTube/content system. Whenever you're not sure where to look, start here.

---

## The 5 Folders You Care About

| Folder | What lives there |
|---|---|
| `~/content/youtube/` | Video packages (scripts, titles, hooks, filming guides) — one folder per video. Plus `status.md` (current pipeline) and `video-ideas.md` (idea tracker) |
| `~/content/yt-research/` | Competitive research (yt-search reports + thumbnails), master plans, audits, this index |
| `~/content/scripts/` | Whisper transcripts of YouTube videos (yours + competitors') |
| `~/content/` | Cross-platform output — LinkedIn / Instagram / Pinterest / flash videos. Organized by date and platform |
| `~/.claude/skills/` | The 43 Claude Code skills that power all of the above |

---

## The 3 Files You Open First

1. **`~/content/youtube/status.md`** — current pipeline state. What you're recording next, what's queued, what needs decisions. **Open this first every Monday morning.**
2. **`~/content/yt-research/2026-05-20-RESTART-plan.md`** — this week's restart plan. Saturday recording, perfectionism rules, 90-day priority.
3. **`~/content/yt-research/2026-05-20-LEVERAGE-be-better.md`** — the 8 levers that separate 800K from 8K. Pre-flight checklist before every recording.

---

## How To Find Things

### "What am I recording next?"
→ `~/content/youtube/status.md` (top section: NEXT RECORD)

### "Where is my script?"
→ `~/content/youtube/<slug>/script.md` — one folder per video

### "Where are my titles / hooks / filming guide?"
→ Same folder as the script. Each package has: `titles.md`, `hooks.md`, `script.md`, `filming-guide.md`, `description.md`, sometimes `seo.md`, sometimes `thumbnail-final.png`

### "What research backs my topic?"
→ `~/content/yt-research/2026-05-17-claude-*.md` (5 reports from May 17) + thumbnails folders

### "What's the 90-day priority?"
→ `~/content/yt-research/2026-05-20-RESTART-plan.md` (top section)

### "Where are my published video transcripts?"
→ `~/content/scripts/transcript_<video_id>.txt`

### "Where are competitor transcripts?"
→ Same place. `transcript_z9rdrNrkvDY.txt` = Jeff Su Cowork. `transcript_Xg55nTrbYYY.txt` = Productive Dude.

### "What shorts have I scripted?"
→ `~/content/youtube/shorts/` — organized by week date (e.g. `2026-03-30/`) or special series (e.g. `news-series-may-2026/`)

### "Where do my LinkedIn / Instagram / Pinterest posts go?"
→ `~/content/<YYYY-MM-DD>/` — organized by week and platform

### "What ideas haven't I built into packages yet?"
→ `~/content/youtube/video-ideas.md`

### "What skills do I have available?"
→ `~/.claude/skills/` — listing folders gives you all 43

---

## The Master Plans (read once, reference forever)

| File | What it covers |
|---|---|
| `~/content/yt-research/2026-05-17-MASTER-claude-banger-ideas.md` | The 10-video lineup (updated with R1/R2 restart pivot) |
| `~/content/yt-research/2026-05-17-AUDIT-existing-packages.md` | Per-package verdict on the 7 existing scripts — what's ready, what needs fixes |
| `~/content/yt-research/2026-05-17-BREAKDOWN-and-2-week-plan.md` | Original 2-week plan from research session |
| `~/content/yt-research/2026-05-20-RESTART-plan.md` | The restart strategy + 90-day priority |
| `~/content/yt-research/2026-05-20-LEVERAGE-be-better.md` | The 8 levers — pre-flight checklist before every recording |

---

## Skill Workflow Reference

Every long-form video follows this skill chain:

```
/yt-search <topic>           # Research what's working
   ↓
/transcribe <competitor URL> # Pull a reference transcript
   ↓
/yt <transcript>             # Generate full video package
   ↓
/seo <package slug>          # Optimize title/desc/tags
   ↓
[FILM THE VIDEO]
   ↓
/chapters <final.mp4>        # Generate accurate timestamps
   ↓
/shorts                      # 5 short-form scripts from research
   ↓
/content <slug>              # X, LinkedIn, IG, YT Community, Skool posts
   ↓
[SCHEDULE via Blotato]
```

Steady-state, this whole chain takes ~90 minutes on a Monday morning and produces a week of content. Restart week = just the recording part. Don't try to run the whole chain on Day 1 back.

---

## Memory (auto-loaded each session)

These memories shape how Claude works with you across all sessions. Located in `~/.claude/projects/-Users-tylerreed/memory/`:

- **User profile:** schedule, credentials, fitness — `user_*.md`
- **Feedback:** standing rules you've established (no em dashes, no money in titles, confirm before scheduling) — `feedback_*.md`
- **Projects:** Instagram carousel framework, flash video system, YouTube workflow, news shorts series, monetization plan — `project_*.md`
- **References:** Skool API, Apify MCP, Pinterest board IDs, Vercel MCP — `reference_*.md`

You don't need to open these directly. Claude pulls from them automatically. But the index is at `~/.claude/projects/-Users-tylerreed/memory/MEMORY.md`.

---

## Cleanup Recommendations (low priority — only do if you want)

These folders in `~/content/youtube/` could be archived to declutter:

- `claude-code-btw/` — 8-min short, low priority
- `claude-code-course/` — no script, abandoned
- `top-10-things-you-should-know-about-claude-code-as/` — only 282 words, stub
- `creator-hooks/` — asset folder, no script
- `tyler-reference-images/` — asset folder
- `claude-code-beginner-concepts/` — already live, can archive

**Quick archive:** `mkdir -p ~/content/youtube/archive && mv ~/content/youtube/{claude-code-btw,claude-code-course,top-10-things-you-should-know-about-claude-code-as,creator-hooks,tyler-reference-images,claude-code-beginner-concepts} ~/content/youtube/archive/`

Not required. Just an option if the folder list feels noisy.

---

## When Things Change

Update **`~/content/youtube/status.md`** any time:
- A video moves from "queued" to "recording"
- A video goes live
- A new idea moves into the lineup
- The 90-day priority changes

That doc is the single source of truth. Don't try to keep this index in sync with state — this index points to status.md and lets status.md be the live thing.

---

## When You're Stuck

The order to read when you don't know what to do:

1. `~/content/youtube/status.md` — what's next?
2. `~/content/yt-research/2026-05-20-RESTART-plan.md` — what does this week look like?
3. `~/content/yt-research/2026-05-20-LEVERAGE-be-better.md` — am I about to make a video that performs?

If you've read all 3 and still stuck, the answer is usually: **pick one task, set a 30-minute timer, ship the imperfect version.**
