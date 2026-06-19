# How to UPDATE the Skool course — Month 1 build/execution plan
Status: PLAN ONLY — no live writes yet. Confirm before EACH write (standing rule).
API mechanics: see `~/.claude/.../memory/reference_skool_classroom_api.md` (20d old — VERIFY live first).

---

## STRUCTURE DECISION

Month 1 = ONE course with 5 Sets (sections), each Set holding its modules. Skool hierarchy:
```
Course: "Month 1: Get AI To Do Your Work"  (privacy 0 = FREE)
  Set: Unit 1 — Start & Setup        → modules 1-4
  Set: Unit 2 — Cowork Clearly Expl. → modules 5-10
  Set: Unit 3 — Cowork Full Course   → modules 11-18
  Set: Unit 4 — Skills Masterclass   → modules 19-26
  Set: Unit 5 — Put It Together      → modules 27-30
```

**Two options for the course itself:**
- **A (recommended): rename + grow the existing "Claude Code" course** (id `92c3144920a3437880425ef5d14630ee`, currently 3 modules). Keeps history; the 3 existing modules fold into Unit 1/2. Retitle → "Month 1: Get AI To Do Your Work".
- **B: create a fresh course.** Cleaner slate, but loses the existing 3 modules' placement. Pick A unless the 3 existing ones are junk.

---

## BUILD STEPS (in order)

### 0. Verify live (READ first, no writes)
- GET classroom.json → capture current `build_id`, `group_id` (`currentGroup.id`), `user_id`, and the live course list + module ids. Memory is 20d old; counts already drifted (AI Agents shows 13 vs 18 elsewhere). Trust live, not the doc.

### 1. The course
- Option A: PUT the Claude Code course → `title: "Month 1: Get AI To Do Your Work"`, set `privacy: 0`.
- Option B: POST `unit_type: "course"` (navigate to classroom page first to prime session).

### 2. The 5 Sets (sections)
- POST `unit_type: "set"`, `parent_id` = course id, `root_id` = course id, one per Unit. Titles = the 5 unit names.

### 3. The 30 modules (two-step each — this is the critical gotcha)
For every module:
1. **POST blank** with MINIMAL payload only: `{group_id, user_id, metadata:{title, resources:"[]"}, parent_id:<set_id>, root_id:<course_id>, state:2, unit_type:"module"}`. NO desc/video on create (causes "Oops").
2. **PUT content** via `page.evaluate()` + native `fetch()` (Playwright `page.request.put()` is WAF-blocked):
   - `title` (<50 chars), `desc` = TipTap `[v2][...]` from the description in `month1-modules.md`.
   - For video modules: call `POST api2.skool.com/video-meta?url=<encoded>` to auto-get `video_thumbnail` + `video_len_ms`, then include `video_link`.
   - Descriptions are already written paste-ready in `month1-modules.md` — convert each to TipTap.

### 4. Attach resources (the PDFs)
- Module `resources` field is a JSON array of attachments. **UNKNOWN: the file-upload endpoint isn't mapped yet** — uploading a PDF to Skool's CDN + getting the attachment object needs to be reverse-engineered (watch the network tab on a manual upload), OR just **attach the PDFs by hand in the UI** for the ~11 modules that need them. Fallback = manual; don't block the build on this.

### 5. Free flag
- Course `privacy: 0`, and each module `hasAccess: 1` for free members. (Paid cohort later uses `privacy:1` + `minTier`.)

### 6. Reorder
- Move "Month 1" to sit right under "Start Here" so it's the first real course a member sees.

---

## SEQUENCING (don't wait for all edits)

1. **Now:** build the course + 5 empty Sets + all 30 module shells (titles + descriptions, no video yet). The classroom immediately looks structured.
2. **Unit 4 (Skills) first:** Masterclass is already recorded → add those video links (19-26) as soon as Nick's edits land.
3. **Units 1 + 5:** record the short Looms, add links.
4. **Units 2-3 (Cowork):** fill in as Cowork Clearly Explained + Full Course get filmed/edited.
5. A visibly-filling course reads as active — good for engagement.

---

## BROADER CLASSROOM REORG (around Month 1 — from reframe-plan)

After Month 1 exists:
- Add **Video Library** course (dump YouTube catalog).
- Add **Platform Playbooks** (YouTube/LinkedIn/Instagram with AI).
- Demote **n8n (49) + Agents (13) + Build Your First (9)** into "The Automation Library" (rename/regroup, never delete).
- Rename junk feed label "Category-1" → "Claude".
- Final order: Start Here → Month 1 → Platform Playbooks → Video Library → Automation Library → Utilities.

---

## GUARDRAILS
- Confirm before EVERY Skool write (even mid-streak).
- Verify live classroom before writing (memory is stale).
- Module titles < 50 chars.
- Navigate to the relevant Skool page first to prime cookies (WAF).
- No dollar amounts in any course/module titles.
- Pricing + paid-cohort positioning → `/harut` before that tier goes live.
