# Audit: 7 Existing Packages vs Proven Pattern

**Date:** 2026-05-17
**Reference pattern:** Tyler's AntiGravity beginner script (the proven format) + Jeff Su Cowork 803K transcript
**Pattern checklist:** (1) proof-first cold open, (2) concrete prompts in code blocks, (3) specific verifiable numbers, (4) `[SHOW:]` and `[NOTE:]` cues, (5) no em dashes (Tyler's standing rule)

---

## TL;DR

5 of 7 existing packages are **on-pattern as-is**. 2 packages have factual issues that should be fixed before filming. None need full rewrites.

| Package | Verdict | Action |
|---|---|---|
| claude-code-course-30 | ⚠️ Mismatch | Decide course vs automation story (see below) |
| claude-cowork-course-30 | ✅ On pattern | Ready to film |
| claude-routines-content-system | ✅ On pattern (thumbnail done!) | Ready to film |
| 100-pieces-content-pipeline | ⚠️ Number conflict | Reconcile 32 vs 100+ before filming |
| claude-code-for-creators | ⚠️ Soft opening | Strengthen proof-first hook |
| mastering-claude-code | ✅ On pattern (live Peeps build is proof) | Ready to film |
| claude-code-remotion | 🔧 Quick fixes | Remove em dashes, update "22 skills" to "43 skills" |

---

## Package-by-Package

### 1. `claude-code-course-30/` — ⚠️ Mismatch

**Issue:** Title options pitch "Master 80% of Claude Code in 30 Min." Script title says "I Automated My Entire YouTube Channel with Claude Code." These are two completely different videos.

**Recommendation:** Pick one path:
- **Path A (course):** Keep the 30-min course framing. Script needs to be rewritten as a teaching course (CLAUDE.md → skills → MCP → hooks → plugins → real project → daily workflow). This is the right play for SEO — "claude courses" keyword has 1 competitor in 60 days.
- **Path B (automation story):** Keep the existing script. Retitle to something like "How I Automated My YouTube Channel With Claude Code (Full Workflow)." This duplicates Idea #6 (`mastering-claude-code`) — risky.

**My pick:** Path A. The keyword opportunity is too big to waste.

**Effort to fix:** Rewriting the script (~2-3 hours) OR retitle and merge with #6. Decide before next filming session.

---

### 2. `claude-cowork-course-30/` — ✅ On Pattern

- Title scorecard with proper references to competitor view counts (Jeff Su 317K, Dan Martell 498K, Eliot Prince 892K).
- Audience-direct opening structure that matches Jeff Su's 803K formula.
- Per-section word counts called out.
- Business-focused demos throughout.

**Action:** Ready to film. No changes needed.

---

### 3. `claude-routines-content-system/` — ✅ On Pattern (and thumbnail done)

- Strong title work — references Nick Saraev (112K in 1 day) and Eliot Prince (856K).
- Already trimmed to fit YouTube's 70-char display ceiling.
- Has `fallbacks.md` for A/B backups.
- Has `thumbnail-final.png` already rendered.
- Hook calls out the unique slot (no competitor pairs Routines + Claude Code).

**Action:** Ready to film. This is the most production-ready of the 10.

---

### 4. `100-pieces-content-pipeline/` — ⚠️ Number Conflict

**Issue:** Title claims "100+ Pieces of Content Per Week." The new `7-skills-run-my-business` script I wrote today uses "32 posts a week." Both numbers can't be right on the same channel within 2 weeks of each other without explanation.

**Reconciliation:** Tyler's CLAUDE.md says ~32 unique pieces per week (2 YT long + 5 shorts + 5 TikTok + 5 IG Reels + 4 IG carousels + 7 LinkedIn + 2 X + 2 YT Community ≈ 32). If you count cross-platform versions as separate pieces (the same short going to YT/TikTok/IG = 3 pieces), you can credibly hit 100+.

**Decision needed:** Are we counting unique pieces (32) or surface impressions (100+)? Pick one and stick with it across both videos.

**Recommendation:** Use **32** for credibility. "100+" is a stretchy number that other creators have already overused; "32" sounds more honest and more achievable for the viewer to believe. Update this video's title to "I Make 32 Pieces of Content a Week Working Full-Time (Here's How)" — same hook, sharper number.

**Effort to fix:** Title change + 2-3 line script edits to align the number. ~30 minutes.

---

### 5. `claude-code-for-creators/` — ⚠️ Soft Opening

**Issue:** Hook starts with a contrarian claim ("Every Claude Code tutorial on YouTube right now is for developers") that's not immediately backed by proof. AntiGravity's hook starts with proof (empty folder → finished app) before making the claim.

**Recommendation:** Restructure the cold open to show the proof first:

[SHOW: Quick montage — Tyler running /content, carousel app opening, Blotato calendar filling, Skool post going live. 5 seconds of "here's what content creators can actually do with Claude Code." THEN cut to the contrarian claim.]

**Effort to fix:** 1-page rewrite of the first 60 seconds. ~30 minutes.

---

### 6. `mastering-claude-code/` — ✅ On Pattern

- Live build of "Peeps" app on camera is the strongest proof element of any package.
- Hook directly addresses the misconception ("you're using it like a chatbot").
- Promises 4 specific things (CLAUDE.md, custom skills, planning, Ralph loops).

**Action:** Ready to film. The Peeps build IS the verification.

**Watch-out:** Make sure Peeps actually finishes building during the recording window. If it stalls, have a backup pre-built version to demo.

---

### 7. `claude-code-remotion/` — 🔧 Quick Fixes

**Issues:**
1. **Em dashes in the hook:** "here's the thing —" and "I haven't opened a video editor in months. — I use Claude Code and a free open-source tool" — violates Tyler's standing rule (`feedback_no_em_dashes`).
2. **Outdated skill count:** "I run 22 Claude Code skills" — Tyler now has 43.

**Effort to fix:** Find-and-replace pass. ~10 minutes.

---

## Recommended Action Order

**Before next filming session:**
1. Fix em dashes + skill count in `claude-code-remotion/script.md` (10 min)
2. Reconcile 32 vs 100+ in `100-pieces-content-pipeline/` (30 min)
3. Decide course vs story for `claude-code-course-30/` (decision only — Tyler should pick)
4. Strengthen `claude-code-for-creators/` cold open (30 min)

**Total fix time:** ~1.5 hours of edits + 1 Tyler decision.

**The other 3 (cowork-30, routines, mastering) are ready to film as-is.**

---

## What I Did Not Do (and Why)

I did NOT rewrite any of the 7 existing scripts top-to-bottom. They were generated by Tyler's own `/yt` skill which already follows his proven format. The issues above are surgical — title mismatches, factual updates, and one cold-open restructure. Full rewrites would be scope creep without value.

**The 3 new packages I built today (7-skills, email-system, build-first-skill) got full revisions** because I wrote those without seeing the AntiGravity reference pattern. Those needed proof-first openings, concrete code blocks, `[SHOW:]` cues. They're now aligned.
