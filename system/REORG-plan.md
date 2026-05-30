# Folder Reorg Plan — Execute Sunday May 24 (after R1 ships)

**Created:** 2026-05-23 (Saturday — recording day)
**Execute:** Sunday afternoon, AFTER the video is published and social is scheduled
**Estimated time:** 30-45 minutes of moves + skill path updates + verification + git commit
**Risk:** Medium (destructive moves + 26 skill files to update)

---

## DO NOT RUN ON SATURDAY

Saturday is recording day. This reorg involves moving ~700+ files and updating 26 skill SKILL.md files. If something goes sideways mid-reorg, you don't want to be debugging during a recording session.

Run this Sunday after the video is uploaded, social is scheduled, and you've walked away from your desk for an hour.

---

## Target Structure (UPDATED — no completed-weeks/, distribute everything)

```
~/content/
├── youtube/
│   ├── 001-<slug>/         ← all video packages renamed with NNN prefix
│   ├── 067-3-skills-and-build/
│   └── status.md           ← live pipeline state (what's recording next, queued)
├── platform/                ← NEW — standalone content per platform
│   ├── linkedin/
│   ├── skool/
│   │   └── _covers/        ← Skool social-media cover image variants
│   ├── pinterest/
│   ├── instagram/
│   ├── youtube-community/  ← NEW — YT Community posts
│   ├── flash-video/
│   └── shorts/             ← standalone (news series, weekly)
├── research/                ← renamed from yt-research/
├── transcripts/             ← renamed from scripts/
├── journal/
├── emails/                  ← already has campaigns/, templates/, broadcasts/
├── custom-gpts/             ← LOCAL ONLY (gitignored)
├── submagic/                ← LOCAL ONLY (gitignored)
└── system/
    ├── INDEX.md             ← moved from research/INDEX.md
    ├── tracker.md           ← merged + updated content inventory
    ├── linkedin-strategy.md ← moved from root
    ├── filming-schedules/   ← past weekly filming schedules
    │   ├── 2026-03-23.md
    │   ├── 2026-03-30.md
    │   └── 2026-04-15.md
    └── shorts-schedules/    ← past weekly shorts schedules
        └── 2026-04-20.md
```

**Tyler's call: NO `completed-weeks/` folder.** Old weekly date bundles get broken apart and the contents distributed to the platform/system folder they actually belong in. Past content stops piling up in date silos — it lives where it's discoverable by platform.

**Naming convention for date-stamped moves:** prepend the original week date to the filename, e.g.:
- `2026-03-23/linkedin-friday.md` → `platform/linkedin/2026-03-23-friday.md`
- `2026-03-30/skool-tuesday.md` → `platform/skool/2026-03-30-tuesday.md`

Files sort chronologically by date, no naming conflicts.

---

## Phase 1 — Create new parent folders + move stuff

```bash
cd ~/content

# Create new parent folders
mkdir -p platform system completed-weeks

# Move platform-specific content under platform/
mv linkedin platform/linkedin
mv skool platform/skool
mv pinterest platform/pinterest
mv instagram platform/instagram
mv flash-video platform/flash-video
mv shorts platform/shorts

# Merge shorts-ai-assets into platform/shorts/_assets/
mkdir -p platform/shorts/_assets
mv shorts-ai-assets/* platform/shorts/_assets/ 2>/dev/null || true
rmdir shorts-ai-assets 2>/dev/null

# Rename research-y folders
mv yt-research research
mv scripts transcripts

# Break apart old weekly bundles — distribute contents to their proper homes
# (See "Phase 1B" section below for the full per-file move plan)

# Move stray files into system/ or merge
mv linkedin-strategy.md system/linkedin-strategy.md
mv research/INDEX.md system/INDEX.md

# Merge the two tracker files
cat tracker.md content-tracker.md > system/tracker.md 2>/dev/null
rm tracker.md content-tracker.md

# bundles/ — review contents and either distribute or move to system/_bundles/
mkdir -p system/_bundles
mv bundles/* system/_bundles/ 2>/dev/null || true
rmdir bundles 2>/dev/null

# schedule/ — move to system/
mv schedule system/schedule
```

---

## Phase 1B — Break apart the 7 date folders (per-file moves)

```bash
cd ~/content

# Create platform subfolders + system subfolders we'll need
mkdir -p platform/youtube-community
mkdir -p platform/skool/_covers/2026-03-26 platform/skool/_covers/2026-03-27
mkdir -p platform/linkedin/carousels/2026-03-26-claude-code-setup
mkdir -p platform/instagram/2026-03-26-claude-code-setup
mkdir -p system/filming-schedules system/shorts-schedules

# ===== 2026-03-23/ (5 LinkedIn + 5 Skool + 1 filming schedule) =====
mv 2026-03-23/linkedin-friday.md     platform/linkedin/2026-03-23-friday.md
mv 2026-03-23/linkedin-saturday.md   platform/linkedin/2026-03-23-saturday.md
mv 2026-03-23/linkedin-sunday.md     platform/linkedin/2026-03-23-sunday.md
mv 2026-03-23/linkedin-tuesday.md    platform/linkedin/2026-03-23-tuesday.md
mv 2026-03-23/linkedin-wednesday.md  platform/linkedin/2026-03-23-wednesday.md
mv 2026-03-23/skool-friday.md        platform/skool/2026-03-23-friday.md
mv 2026-03-23/skool-saturday.md      platform/skool/2026-03-23-saturday.md
mv 2026-03-23/skool-sunday.md        platform/skool/2026-03-23-sunday.md
mv 2026-03-23/skool-tuesday.md       platform/skool/2026-03-23-tuesday.md
mv 2026-03-23/skool-wednesday.md     platform/skool/2026-03-23-wednesday.md
mv 2026-03-23/filming-schedule.md    system/filming-schedules/2026-03-23.md
rmdir 2026-03-23

# ===== 2026-03-26/ (1 carousel + 3 asset folders + 1 LinkedIn draft + 4 Skool covers) =====
mv 2026-03-26/carousel-claude-code-setup.md platform/linkedin/carousels/2026-03-26-claude-code-setup.md
mv 2026-03-26/carousel-slides/*             platform/linkedin/carousels/2026-03-26-claude-code-setup/
mv 2026-03-26/instagram-carousel/*          platform/instagram/2026-03-26-claude-code-setup/
mv 2026-03-26/linkedin-custom-gpt-draft.md  platform/linkedin/2026-03-26-custom-gpt-draft.md
mv 2026-03-26/2026-03-26-skool-social-media-cover/*    platform/skool/_covers/2026-03-26/
mv 2026-03-26/2026-03-26-skool-social-media-cover-v2/* platform/skool/_covers/2026-03-26/v2/
mv 2026-03-26/2026-03-26-skool-social-media-cover-v3/* platform/skool/_covers/2026-03-26/v3/
mv 2026-03-26/2026-03-27-skool-social-media-cover-v4/* platform/skool/_covers/2026-03-27/
# Clean up empty subfolders + DS_Store
rm -rf 2026-03-26/carousel-slides 2026-03-26/instagram-carousel
rm -rf 2026-03-26/2026-03-26-skool-social-media-cover*
rm -rf 2026-03-26/2026-03-27-skool-social-media-cover*
rm -f  2026-03-26/.DS_Store
rmdir 2026-03-26

# ===== 2026-03-30/ (5 LinkedIn + 5 Skool + 2 YT Community + 1 filming schedule) =====
mv 2026-03-30/linkedin-friday.md     platform/linkedin/2026-03-30-friday.md
mv 2026-03-30/linkedin-saturday.md   platform/linkedin/2026-03-30-saturday.md
mv 2026-03-30/linkedin-sunday.md     platform/linkedin/2026-03-30-sunday.md
mv 2026-03-30/linkedin-tuesday.md    platform/linkedin/2026-03-30-tuesday.md
mv 2026-03-30/linkedin-wednesday.md  platform/linkedin/2026-03-30-wednesday.md
mv 2026-03-30/skool-friday.md        platform/skool/2026-03-30-friday.md
mv 2026-03-30/skool-saturday.md      platform/skool/2026-03-30-saturday.md
mv 2026-03-30/skool-sunday.md        platform/skool/2026-03-30-sunday.md
mv 2026-03-30/skool-tuesday.md       platform/skool/2026-03-30-tuesday.md
mv 2026-03-30/skool-wednesday.md     platform/skool/2026-03-30-wednesday.md
mv 2026-03-30/yt-community-monday.md   platform/youtube-community/2026-03-30-monday.md
mv 2026-03-30/yt-community-thursday.md platform/youtube-community/2026-03-30-thursday.md
mv 2026-03-30/filming-schedule.md    system/filming-schedules/2026-03-30.md
rmdir 2026-03-30

# ===== 2026-04-08/ (1 IG research folder) =====
mv 2026-04-08/instagram-yt-research platform/instagram/2026-04-08-yt-research
rm -f 2026-04-08/.DS_Store
rmdir 2026-04-08

# ===== 2026-04-09/ (1 flash-video folder) =====
mv 2026-04-09/flash-video/* platform/flash-video/2026-04-09/ 2>/dev/null
mkdir -p platform/flash-video/2026-04-09  # ensure exists
rm -rf 2026-04-09/flash-video
rm -f 2026-04-09/.DS_Store
rmdir 2026-04-09

# ===== 2026-04-15/ (1 filming schedule) =====
mv 2026-04-15/filming-schedule.md system/filming-schedules/2026-04-15.md
rmdir 2026-04-15

# ===== 2026-04-20/ (1 shorts schedule) =====
mv 2026-04-20/shorts-schedule.md system/shorts-schedules/2026-04-20.md
rmdir 2026-04-20
```

After this section runs, all 7 date folders should be gone and their contents distributed to `platform/<channel>/` or `system/filming-schedules/` accordingly.

---

## Phase 2 — Rename video packages with NNN prefix

This requires deciding the numbering. Recommend: chronological by published date for live videos, then queued videos get next-available numbers.

```bash
cd ~/content/youtube

# Example renames (CONFIRM ORDER WITH status.md BEFORE RUNNING):
# Live videos (chronological by publish date — verify against status.md):
mv claude-getting-started 001-claude-getting-started
mv claude-code-skills 002-claude-code-skills
mv build-anything-claude-code 003-build-anything-claude-code   # if folder exists
mv claude-beginners 004-claude-beginners
mv claude-code-youtube-workflow 005-claude-code-youtube-workflow
mv 23-claude-code-concepts 006-23-claude-code-concepts
mv claude-code-telegram-channels 007-claude-code-telegram-channels
mv claude-code-remote-control 008-claude-code-remote-control
mv claude-design 009-claude-design

# Queued / unscripted (60s range):
mv 3-skills-and-build 067-3-skills-and-build              # R1 — Saturday
mv claude-routines-content-system 068-claude-routines-content-system   # R3
mv claude-cowork-course-30 069-claude-cowork-course-30    # R4
mv claude-code-email-system 070-claude-code-email-system  # R5
mv 100-pieces-content-pipeline 071-100-pieces-content-pipeline
mv claude-code-for-creators 072-claude-code-for-creators
mv claude-code-remotion 073-claude-code-remotion
mv mastering-claude-code 074-mastering-claude-code        # may skip, overlaps with Ralph loop
mv 7-skills-run-my-business 075-7-skills-run-my-business  # source for R2
mv build-first-skill-15-min 076-build-first-skill-15-min  # source for R2
mv claude-code-course-30 077-claude-code-course-30        # needs decision
mv claude-code-scheduling 078-claude-code-scheduling
mv claude-design-5-landing-pages 079-claude-design-5-landing-pages
mv claude-design-kling-animated-hero 080-claude-design-kling-animated-hero
mv claude-design-rebuild-stripe 081-claude-design-rebuild-stripe
mv antigravity-beginner 082-antigravity-beginner

# Other folders (review case-by-case):
# - antigravity-analysis (delete?)
# - claude-code-course (no script, abandoned — delete or archive)
# - claude-code-btw (8-min stub — archive?)
# - top-10-things-you-should-know-about-claude-code-as (282-word stub — archive)
# - creator-hooks (asset folder, no script — keep as _assets?)
# - tyler-reference-images (asset folder — move to system/)
# - claude-code-beginner-concepts, build-claude-code-skill (already live, low-priority renames)
# - shorts (separate from youtube/shorts/ in old structure)
# - thumbnails (move to platform/youtube-thumbnails/ or _assets/)
# - tiktok-analytics, tiktok-research (where? maybe platform/tiktok/research/)
```

**Suggested numbering scheme:**
- 001-050 reserved for live/published videos (chronological)
- 051-099 for queued/scripted but not yet recorded
- 100+ for future ideas

---

## Phase 3 — Update all skill paths AGAIN

Same pattern as today's path update. Run sed across:
- `~/.claude/skills/` (all SKILL.md + .py files)
- `~/.claude/CLAUDE.md`
- `~/.claude/projects/-Users-tylerreed/memory/`
- `~/content/` (all .md files inside)

```bash
# Pattern substitutions needed:
# ~/content/yt-research → ~/content/research
# ~/content/scripts → ~/content/transcripts
# ~/content/linkedin → ~/content/platform/linkedin
# ~/content/skool → ~/content/platform/skool
# ~/content/pinterest → ~/content/platform/pinterest
# ~/content/instagram → ~/content/platform/instagram
# ~/content/flash-video → ~/content/platform/flash-video
# ~/content/shorts → ~/content/platform/shorts

find ~/.claude/skills ~/.claude/projects/-Users-tylerreed/memory ~/content -type f \( -name "*.md" -o -name "*.py" \) -exec sed -i '' \
  -e 's|~/content/yt-research|~/content/research|g' \
  -e 's|~/content/scripts|~/content/transcripts|g' \
  -e 's|~/content/linkedin|~/content/platform/linkedin|g' \
  -e 's|~/content/skool|~/content/platform/skool|g' \
  -e 's|~/content/pinterest|~/content/platform/pinterest|g' \
  -e 's|~/content/instagram|~/content/platform/instagram|g' \
  -e 's|~/content/flash-video|~/content/platform/flash-video|g' \
  -e 's|~/content/shorts|~/content/platform/shorts|g' \
  -e 's|/Users/tylerreed/content/yt-research|/Users/tylerreed/content/research|g' \
  -e 's|/Users/tylerreed/content/scripts|/Users/tylerreed/content/transcripts|g' \
  -e 's|/Users/tylerreed/content/linkedin|/Users/tylerreed/content/platform/linkedin|g' \
  -e 's|/Users/tylerreed/content/skool|/Users/tylerreed/content/platform/skool|g' \
  -e 's|/Users/tylerreed/content/pinterest|/Users/tylerreed/content/platform/pinterest|g' \
  -e 's|/Users/tylerreed/content/instagram|/Users/tylerreed/content/platform/instagram|g' \
  -e 's|/Users/tylerreed/content/flash-video|/Users/tylerreed/content/platform/flash-video|g' \
  -e 's|/Users/tylerreed/content/shorts|/Users/tylerreed/content/platform/shorts|g' \
  {} \;

# Also separately handle the global CLAUDE.md
sed -i '' \
  -e 's|~/content/yt-research|~/content/research|g' \
  -e 's|~/content/scripts|~/content/transcripts|g' \
  -e 's|~/content/linkedin|~/content/platform/linkedin|g' \
  -e 's|~/content/skool|~/content/platform/skool|g' \
  -e 's|~/content/pinterest|~/content/platform/pinterest|g' \
  -e 's|~/content/instagram|~/content/platform/instagram|g' \
  -e 's|~/content/flash-video|~/content/platform/flash-video|g' \
  -e 's|~/content/shorts|~/content/platform/shorts|g' \
  ~/.claude/CLAUDE.md
```

Note: skill paths that reference specific subfolders inside youtube/ (e.g. `~/content/youtube/<slug>/`) DON'T change. The skill's `/yt` slug logic stays the same.

---

## Phase 3B — Update tracker.md with the new inventory

Replace the two old tracker files (already merged into `system/tracker.md` in Phase 1) with the new content inventory template. Update the body to reflect the new structure:

```markdown
# Content Tracker

> Master inventory of all content across all platforms.
> For pipeline state (what's recording next), see `youtube/status.md`.
> Updated: 2026-05-24

---

## Long-Form Videos

### Live
| # | Title | Folder | Date | URL |
|---|-------|--------|------|-----|
| 001 | Claude Getting Started | `youtube/001-*/` | TBD | TBD |
| 002 | Claude Code Skills | `youtube/002-*/` | 2026-03-01 | youtu.be/lfwt5tFfaSo |
| ... |

### Scripted, not yet recorded
| # | Title | Folder | Status |
|---|-------|--------|--------|
| 067 | 3 Skills + Live Build | `youtube/067-3-skills-and-build/` | R1 — Sat May 23 |
| 068 | Routines + Code Stack | `youtube/068-claude-routines-content-system/` | R3 — thumbnail done |
| 069 | Cowork 30-min Course | `youtube/069-claude-cowork-course-30/` | R4 |
| ... |

### Needs decision
| # | Title | Issue |
|---|-------|-------|
| 077 | Master 80% Claude Code 30 Min | Title vs script mismatch |
| 074 | Mastering Claude Code | Overlaps with Ralph loop video |

---

## LinkedIn (`platform/linkedin/`)

### Standalone Posts (date-stamped from old date folders + new weekly drops)
- 2026-03-23 week (Tue/Wed/Fri/Sat/Sun)
- 2026-03-30 week (Tue/Wed/Fri/Sat/Sun)
- 2026-03-26 custom GPT draft
- ...

### Carousels (`platform/linkedin/carousels/`)
- 2026-03-26 Claude Code Setup
- ...

---

## Skool (`platform/skool/`)

### Posts (date-stamped)
- 2026-03-23 week (Tue/Wed/Fri/Sat/Sun)
- 2026-03-30 week (Tue/Wed/Fri/Sat/Sun)
- ...

### Cover Images (`platform/skool/_covers/`)
- 2026-03-26 (v1, v2, v3)
- 2026-03-27 (v4)

---

## Instagram (`platform/instagram/`)
- 2026-03-26 Claude Code Setup carousel
- 2026-04-08 YT Research carousel
- ... + 4 active subdirs

---

## Pinterest (`platform/pinterest/`)
29 pin folders. See subdirectory.

---

## YouTube Community (`platform/youtube-community/`)
- 2026-03-30 Monday + Thursday

---

## Flash Videos (`platform/flash-video/`)
- 2026-04-09

---

## Shorts (`platform/shorts/`)
### News Series (recurring Tuesdays)
- 2026-05 (5 scripts, see `news-series-may-2026/`)

### Per-video shorts
- Cut from each long-form video, live in `youtube/<NNN-slug>/shorts/`

---

## Filming Schedules (`system/filming-schedules/`)
- 2026-03-23
- 2026-03-30
- 2026-04-15

---

## Shorts Schedules (`system/shorts-schedules/`)
- 2026-04-20
```

The actual file population happens during reorg — you'd update tracker.md by hand or via a one-time `ls` script after Phase 1B finishes. Or I can write a helper that auto-generates tracker.md from disk state.

---

## Phase 4 — Update .gitignore to exclude custom-gpts

```bash
cat >> ~/content/.gitignore << 'EOF'

# Tyler's call — custom GPTs stay local only
custom-gpts/
EOF
```

Then remove custom-gpts from git tracking (file content stays on disk):

```bash
cd ~/content
git rm -r --cached custom-gpts
```

---

## Phase 5 — Smoke test + commit + push

```bash
# Quick smoke test: invoke /yt-search or just verify a path works
ls ~/content/youtube/067-3-skills-and-build/script.md
ls ~/content/research/
ls ~/content/platform/linkedin/

# Commit and push
cd ~/content
git add .
git commit -m "Reorg: platform/ parent, completed-weeks/, NNN-prefixed video packages, custom-gpts local-only"
git push
```

---

## Verification Checklist

After running, confirm:

- [ ] `~/content/youtube/` exists with NNN-prefixed subfolders
- [ ] `~/content/platform/` contains 6 platform subfolders
- [ ] `~/content/research/` exists (renamed from yt-research)
- [ ] `~/content/transcripts/` exists (renamed from scripts)
- [ ] `~/content/completed-weeks/` contains 7 date-named subfolders
- [ ] `~/content/system/` exists with INDEX.md, tracker.md, linkedin-strategy.md
- [ ] `~/content/custom-gpts/` exists locally but NOT tracked by git (`git ls-files | grep custom-gpts` returns nothing)
- [ ] No old top-level folders (yt-research, scripts, linkedin, skool, pinterest, instagram, flash-video, shorts, bundles, schedule)
- [ ] Run `/yt-search test` in Claude Code → confirm it writes to `~/content/research/`
- [ ] Run `/transcribe <short YT URL>` → confirm it writes to `~/content/transcripts/`

---

## Rollback Plan

If anything goes badly wrong:

```bash
cd ~/content
git reset --hard HEAD~1   # only reverts the commit, not the file moves
# OR for full restoration:
git stash                  # stash any uncommitted changes
git checkout <commit-hash-before-reorg>  # get back to today's state
```

Since the moves are tracked by git AFTER the commit, you can revert. But anything not committed before the reorg is at risk. Make sure Saturday's video is fully committed BEFORE starting Sunday's reorg.

---

## Time Budget

| Phase | Time |
|---|---|
| 1. Create folders + move | 5 min |
| 2. Rename video packages with NNN | 10 min (the longest — needs care) |
| 3. Update skill paths (bulk sed) | 5 min |
| 4. .gitignore custom-gpts | 2 min |
| 5. Smoke test + commit + push | 5 min |
| Buffer for verification | 10 min |
| **Total** | **~35 min** |

---

## When You're Done

Update `system/INDEX.md` to reflect the new paths. The current INDEX.md was written with old paths.

Then close the laptop. The org is done. You're back to your real job — making videos.
