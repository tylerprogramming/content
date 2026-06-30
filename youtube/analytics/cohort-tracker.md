# Long-Form Cohort Tracker

> **The fixed 20-video long-form cohort.** Every analytics pull refreshes these same 20 videos so we watch the set trend over time, and roll new long-form releases in as they publish. Long-form only (>3 min) - never Shorts.
>
> **Source of truth:** Supabase `lifestyle` project, `youtube_daily` table (one row per video per snapshot date). This file mirrors the latest snapshot for quick reading.
>
> Numbers below are **lifetime cumulative** (views, likes, comments, shares, subs) + **lifetime retention** (avg_view_pct). CTR is Studio-only (filled manually).

---

## Latest snapshot: 2026-06-30

Channel: 23,500 subs | 1,633,717 lifetime views | net subs last 4 days +5

| # | Video | ID | Views | Retention | Avg Sec | Subs | Likes | Pub |
|---|---|---|---|---|---|---|---|---|
| 1 | I Automated My Entire YouTube Workflow | `MLfyfNj1JrI` | 2,854 | 16.0% | 145 | +42 | 59 | 3/12 |
| 2 | Google is Winning With Antigravity | `B5eDktBzXMg` | 2,405 | 15.0% | 166 | +14 | 42 | 2/01 |
| 3 | Build ANYTHING With Claude Code (Beginner) | `XAcqU3zuZmE` | 1,895 | **29.4%** | 178 | +20 | 24 | 3/06 |
| 4 | Claude Code Skills Changed How I Use AI | `lfwt5tFfaSo` | 1,203 | 19.6% | 127 | +11 | 25 | 3/01 |
| 5 | 23 Claude Code Concepts in 24 Min | `MVr2GrAjrgQ` | 1,169 | 16.9% | 248 | +9 | 32 | 3/17 |
| 6 | I'll never pay for n8n again | `8kocqs1ktrg` | 1,016 | 17.9% | 132 | +12 | 34 | 1/08 |
| 7 | This Claude Code Plugin (Ralph Wiggum) | `RQ57cUcGDGg` | 932 | 16.6% | 159 | +5 | 14 | 2/05 |
| 8 | Claude Code: Only Beginner Tutorial | `NL6qUfJRujs` | 848 | 17.9% | 180 | +16 | 29 | 3/09 |
| 9 | Local Invoice Parsing w/ Docling | `NsORND5fmcQ` | 832 | 17.7% | 146 | +3 | 27 | 1/18 |
| 10 | Claude Code on Your Phone | `JEveW6KULyg` | 692 | 16.2% | 109 | +2 | 14 | 3/23 |
| 11 | n8n Image+Video Automation | `Km1CjLGLtLQ` | 683 | 12.2% | 100 | +8 | 14 | 12/28 |
| 12 | Claude Routines + Claude Code | `akcCiWLe51Q` | 516 | 17.9% | 208 | +3 | 9 | 4/29 |
| 13 | Claude Design is Incredible | `aiMZrj4zqo8` | 486 | 15.6% | 111 | +2 | 7 | 4/26 |
| 14 | n8n RAG Agent Template | `qA08vhuvjfA` | 313 | 20.6% | 108 | +2 | 12 | 1/29 |
| 15 | What I'd Learn for AI Automation 2026 | `80-zKvov8Fk` | 298 | 24.3% | 152 | +2 | 18 | 1/25 |
| 16 | Stop Skipping Evaluation | `btbg8lRMAiY` | 295 | 13.2% | 101 | +1 | 8 | 2/08 |
| 17 | **Skills Masterclass (32m)** | `9ZsZgnWrs_E` | 288 | 10.5% | 202 | +3 | 8 | 6/21 |
| 18 | **3 Claude Code Skills** | `aPeHhNPjtEo` | 274 | 13.1% | 125 | +2 | 10 | 6/14 |
| 19 | **Cowork Easily Explained** | `7ND_buIAQfA` | 250 | 20.5% | 184 | +2 | 10 | 6/25 |
| 20 | n8n Autosave | `hTzQtsN4oEI` | 200 | 20.3% | 113 | +3 | 5 | 1/23 |

**Read (2026-06-30):**
- The 3 newest releases (#17-19) sit at the bottom of the cohort. Older Claude Code beginner videos do 3-10x better - cadence gap + packaging problem.
- Retention champion: **Build ANYTHING With Claude Code (Beginner) at 29.4%** - clean beginner-tutorial framing is the format to copy. Cowork Easily Explained (20.5%) is the new one closest to it.
- **Skills Masterclass (10.5%) = weakest retention in the cohort.** The 32-min course format is dead weight for discovery. Showcase/clearly-explained format wins.
- Suggested/related traffic still ~4% channel-wide - the packaging fix (Nano Banana showdown #14) is the lever.

**New long-form since last snapshot:** none yet (Routines + Granola still with editor - roll in once published).

---

## How this works

- Long-form only (duration > 3 min). Shorts are tracked separately, never mixed in.
- Fixed cohort = the 20 videos above. New long-form releases get appended as they publish (cohort grows; nothing drops).
- Each pull: refresh all cohort IDs, insert a dated row per video into `youtube_daily`, update the snapshot table here.
- Batch pull script: `~/.claude/skills/yt-analytics/yt_analytics.py` (overview) + cohort batch via videos.list + analytics grouped-by-video.
- CTR is Studio-only - fill the `ctr` column manually from YouTube Studio when reviewing.
