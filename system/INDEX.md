# File Index — Where Everything Lives

The evergreen front door for the YouTube/content system. Whenever you're not sure where to look, start here.

> **Updated:** 2026-07-22 (paths refreshed for youtube/videos + youtube/notes + research/youtube reorg; see root CLAUDE.md for the repo overview)

---

## The 4 Top-Level Folders You Care About

| Folder | What lives there |
|---|---|
| `~/content/youtube/` | Long-form video packages, one folder per video (NNN-prefixed for new ones). Plus `status.md` (live pipeline state) and `video-ideas.md` (idea tracker) |
| `~/content/platform/` | All standalone (non-video-tied) content, organized by channel — `linkedin/`, `skool/`, `pinterest/`, `instagram/`, `youtube-community/`, `flash-video/`, `shorts/`, `carousels/` |
| `~/content/research/` `~/content/transcripts/` `~/content/journal/` `~/content/emails/` | Working folders — competitive research, whisper transcripts, daily logs, email campaigns |
| `~/content/system/` | Navigation + planning docs — this INDEX.md, tracker.md, REORG-plan.md, filming-schedules/, linkedin-strategy.md |

Plus `~/.claude/skills/` (separate repo at `tylerprogramming/claude-skills`) — the 43 skills that power the workflow.

---

## The 3 Files You Open First

1. **`~/content/youtube/notes/status.md`** — current pipeline state. What you're recording next, what's queued, what needs decisions. **Open this first every Monday morning.**
2. **`~/content/system/tracker.md`** — content inventory across all platforms. What exists, what's been built.
3. **`~/content/research/youtube/strategy/2026-05-20-RESTART-plan.md`** — current restart plan. Saturday recording, perfectionism rules, 90-day priority.

For pre-recording: **`~/content/research/youtube/strategy/2026-05-20-LEVERAGE-be-better.md`** — the 8 levers checklist.

---

## How To Find Things

### "What am I recording next?"
→ `~/content/youtube/notes/status.md` (top section: NEXT RECORD)

### "Where is my script?"
→ `~/content/youtube/videos/NNN-<slug>/script.md` — one folder per video

### "Where are my titles / hooks / filming guide / social posts for a video?"
→ Same folder as the script. Each package has: `titles.md`, `hooks.md`, `script.md`, `filming-guide.md`, `description.md`, sometimes `seo.md`, sometimes `thumbnail.png`, and `social/` for per-video cross-platform posts.

### "Where do my standalone LinkedIn posts go?"
→ `~/content/platform/linkedin/<YYYY-MM-DD>-<slug>.md` (date-stamped)

### "Where do my standalone Skool posts go?"
→ `~/content/platform/skool/<YYYY-MM-DD>-<slug>.md`

### "Where do my Pinterest pins go?"
→ `~/content/platform/pinterest/<NNN>-<slug>/` (numbered pin folders)

### "Where do my Instagram carousels go?"
→ `~/content/platform/instagram/<slug-or-date>/` or `~/content/platform/carousels/`

### "Where do my YouTube Community posts go?"
→ `~/content/platform/youtube-community/<YYYY-MM-DD>-<day>.md`

### "Where do my flash videos go?"
→ `~/content/platform/flash-video/<date>/`

### "What research backs my topic?"
→ `~/content/research/<YYYY-MM-DD>-<keywords>.md` + thumbnails folders

### "What's the 90-day priority?"
→ `~/content/research/youtube/strategy/2026-05-20-RESTART-plan.md` (top section)

### "Where are competitor transcripts?"
→ `~/content/transcripts/transcript_<video_id>.txt`
- Jeff Su Cowork: `transcript_z9rdrNrkvDY.txt`
- Productive Dude Tutorial: `transcript_Xg55nTrbYYY.txt`

### "What shorts have I scripted?"
Three possible locations depending on the type:
- **News series shorts** (recurring Tuesday): `~/content/youtube/shorts/news-series-may-2026/` and future months
- **Per-video shorts** (cut from a long-form): `~/content/youtube/videos/<NNN-slug>/shorts/`
- **Standalone shorts:** `~/content/platform/shorts/`

### "What weekly filming schedule did I plan?"
→ `~/content/system/filming-schedules/<YYYY-MM-DD>.md`

### "Where are my journal entries?"
→ `~/content/journal/<YYYY-MM-DD>.txt` + `weekly_summary.txt`

### "What ideas haven't I built into packages yet?"
→ `~/content/youtube/ideas/video-ideas.md`

### "What skills do I have available?"
→ `~/.claude/skills/` — listing folders gives you all 43

### "Where is the full content inventory?"
→ `~/content/system/tracker.md`

---

## The Master Plans (read once, reference forever)

| File | What it covers |
|---|---|
| `~/content/research/youtube/strategy/2026-05-17-MASTER-claude-banger-ideas.md` | The 10-video lineup (with R1/R2 restart pivot) |
| `~/content/research/youtube/strategy/2026-05-17-AUDIT-existing-packages.md` | Per-package verdict on the 7 existing scripts |
| `~/content/research/youtube/strategy/2026-05-20-RESTART-plan.md` | The restart strategy + 90-day priority |
| `~/content/research/youtube/strategy/2026-05-20-LEVERAGE-be-better.md` | The 8 levers — pre-flight checklist before every recording |
| `~/content/system/REORG-plan.md` | The folder reorg plan executed 2026-05-23 |
| `~/content/system/linkedin-strategy.md` | LinkedIn posting framework |

---

## Skill Workflow Reference

Every long-form video follows this skill chain:

```
/yt-search <topic>           # Research what's working → ~/content/research/
   ↓
/transcribe <competitor URL> # Pull a reference transcript → ~/content/transcripts/
   ↓
/yt <transcript>             # Generate full video package → ~/content/youtube/<slug>/
   ↓
/seo <package slug>          # Optimize title/desc/tags
   ↓
[FILM THE VIDEO]
   ↓
/chapters <final.mp4>        # Generate accurate timestamps
   ↓
/shorts                      # 5 short-form scripts from research → ~/content/youtube/shorts/
   ↓
/content <slug>              # Cross-platform posts → ~/content/youtube/<slug>/social/
   ↓
[SCHEDULE via Blotato]
```

Steady-state, this whole chain takes ~90 minutes on a Monday morning and produces a week of content.

---

## Memory (auto-loaded each session)

Located in `~/.claude/projects/-Users-tylerreed-content/memory/`. Auto-loads — you don't open these directly.

- **User profile:** schedule, credentials, fitness — `user_*.md`
- **Feedback:** standing rules (no em dashes, no money in titles, confirm before scheduling) — `feedback_*.md`
- **Projects:** Instagram carousel framework, flash video system, YouTube workflow, news shorts series, monetization plan — `project_*.md`
- **References:** Skool API, Apify MCP, Pinterest board IDs, Vercel MCP — `reference_*.md`

Index at `~/.claude/projects/-Users-tylerreed-content/memory/MEMORY.md`.

---

## Git / GitHub

| Repo | Purpose | Visibility |
|---|---|---|
| `tylerprogramming/content` | This whole `~/content/` folder | Private |
| `tylerprogramming/claude-skills` | The 43 skills at `~/.claude/skills/` | Public |

**Daily workflow:**
- After working on Mac 1: `cd ~/content && git add . && git commit -m "update" && git push`
- When sitting at Mac 2: `cd ~/content && git pull`

**Excluded from git** (local only): `custom-gpts/`, `submagic/`, all media files (`*.mp4`, `*.png`, `*.jpg`, etc.)

---

## Two Sources of Truth

| File | What it tracks | When to update |
|---|---|---|
| `youtube/notes/status.md` | **Live pipeline state** — what's recording, what's queued, what's live | Whenever a video moves between stages |
| `system/tracker.md` | **Content inventory** — what exists across all platforms | Whenever you add new content |

These two are intentionally separate. Status = operational. Tracker = inventory.

---

## When You're Stuck

The order to read when you don't know what to do:

1. `~/content/youtube/notes/status.md` — what's next?
2. `~/content/research/youtube/strategy/2026-05-20-RESTART-plan.md` — what does this week look like?
3. `~/content/research/youtube/strategy/2026-05-20-LEVERAGE-be-better.md` — am I about to make a video that performs?

If you've read all 3 and still stuck, the answer is usually: **pick one task, set a 30-minute timer, ship the imperfect version.**

---

## Cleanup Notes

Folders in `~/content/youtube/` that could be archived eventually (low priority):

- `claude-code-btw/` — 8-min stub
- `claude-code-course/` — no script, abandoned
- `top-10-things-you-should-know-about-claude-code-as/` — 282-word stub
- `creator-hooks/` — asset folder, no script
- `tyler-reference-images/` — asset folder
- `antigravity-analysis/` — research artifact, not a video

Not urgent. Lives at root of `youtube/` doesn't hurt anything for now.
