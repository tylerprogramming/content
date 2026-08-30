# CLAUDE.md

This is Tyler's **content operations repo** — the working home of his YouTube channel and all cross-platform content (LinkedIn, Instagram, Pinterest, Skool, TikTok, shorts, email). It contains markdown packages, research, transcripts, and planning docs. There is no application code to build or test; media files (mp4/png/jpg) are gitignored.

## Sources of truth (read these first)

| File | Role |
|---|---|
| `youtube/notes/status.md` | **Live pipeline state** — what's recording next, with editor, published. The operational source of truth. |
| `system/tracker.md` | **Content inventory** — what exists across all platforms. |
| `system/INDEX.md` | File-finder front door when you don't know where something lives. |

**ClickUp sync rule:** the pipeline is mirrored in ClickUp (YouTube list id `901710640585`). `youtube/notes/status.md` is the source of truth — whenever a video moves stages, update the file **and** the ClickUp task.

## Folder map

```
youtube/            Long-form video production
  videos/           One folder per package, NNN-prefixed (001-…, 034-…). See anatomy below.
  notes/status.md   Live pipeline state (source of truth)
  ideas/            video-ideas.md tracker + parked/stub packages
  analytics/        Channel diagnostics, daily/cohort trackers
  shorts/           Numbered short scripts ("047 - Title…") + news-series folders
  thumbnails/       Dated thumbnail generation folders
  resources/        Evergreen how-to docs (publishing stack, yt-upload setup)
  _archive/         Retired packages
platform/           Standalone (non-video-tied) content, one folder per channel:
                    linkedin/, skool/, pinterest/, instagram/, carousels/,
                    youtube-community/, flash-video/, shorts/
research/           Competitive research by type: youtube/ (incl. strategy/ master plans),
                    instagram/, tiktok/, skills-frameworks/. /yt-search writes here.
BRAIN/              Per-platform playbooks (brain.md) + tyler-voice.md (voice guide for ALL
                    written content). Research skills WRITE here; creation skills READ first.
transcripts/        Whisper transcripts (own videos + competitors): transcript_<id>.txt
emails/campaigns/   Drip campaigns (Resend)
journal/            Daily journal entries + weekly summaries
standup/            Standup logs
system/             tracker.md, INDEX.md, filming-schedules/, shorts-schedules/, strategy notes
scripts/            Misc working transcripts (chapters audio, etc.)
_archive/           Old weekly batches and catch-up snapshots
```

## Video package anatomy

Each `youtube/videos/NNN-<slug>/` package typically contains: `titles.md`, `hooks.md`, `script.md` (or `.txt`), `filming-guide.md`, `description.md`, `status.md`, and often `seo.md`, `thumbnail.md`, `analysis.md`, `plan.md`, plus `social/` (cross-platform posts) and `shorts/` (cut-down scripts). Multi-video projects nest: `034-elevenlabs-flows/video-2-flows-agent/`.

## Conventions

- **Numbering:** long-form packages are `NNN-slug` in record order; shorts are numbered `NNN - Title` in `youtube/shorts/`.
- **Dating:** standalone platform posts and research files are date-stamped `YYYY-MM-DD-slug`.
- **Voice:** all written content follows `BRAIN/tyler-voice.md`. Standing rules include: no em dashes in content, no money amounts in titles, confirm before scheduling/publishing anything.
- **BRAIN hygiene:** distilled rules only (with `[confirmed YYYY-MM-DD]` stamps), never raw data; retire stale rules.

## Skill workflow (long-form video chain)

Skills live in the separate `tylerprogramming/claude-skills` repo at `~/claude-skills`, symlinked into `~/.claude/skills/`. YouTube skills are `yt-` prefixed.

```
/yt-search → /transcribe → /yt-package → /yt-seo → [FILM] → /yt-chapters
   → /yt-shorts → /social-copy (or /repurpose) → /yt-upload → schedule
```

- `/yt-search` writes to `research/`
- `/yt-package` writes to `youtube/videos/<NNN-slug>/`
- `/social-copy` writes to the package's `social/` folder
- `/linkedin-writer` writes the LinkedIn post to the package's `social/linkedin.md` (or `platform/linkedin/` when standalone). Reads `BRAIN/linkedin/brain.md` first; defaults to the **build post** format, which is the only shape that has broken out on the account.
- `/yt-upload` handles YouTube API uploads/edits (replaced Blotato for long-form)

## Lifestyle OS (personal — kept here for convenience, separate from content)

Tyler also runs a personal whole-life tracker from this machine (runs, lifts, meals, water, caffeine, weight, reading). It is **not** part of the content pipeline:

- **Logging** → the **lifestyle Supabase project** via the `/lifestyle` skill (the project id lives in private config, intentionally *not* in this repo).
- **Dashboard** → rebuilt to `~/lifestyle/dashboard.html` via the `/lifestyle-show` skill.
- Key tables: `meal_plan` (planned meals + actuals), `cardio_log` (runs), `activity_log` (daily macro totals), `weight_log`, `caffeine_log`, `daily_checkin`.
- Content/recording **time-blocks** (Claude course, Blotato, Arcade) are scheduled on **Google Calendar** (`America/New_York`). Blotato showcase source: `research/youtube/2026-06-20-blotato.md` (+ `.json`).

## Git workflow

Private repo (`tylerprogramming/content`), synced across two Macs: commit + push after working on one machine, pull when sitting at the other. Media files and `custom-gpts/`, `submagic/` are local-only (gitignored). Commit messages describe the content change (see `git log` for style).
