# Filming Guide — Claude Routines + Claude Code

**Target runtime:** 28-30 min final cut
**Estimated filming time:** 2-3 hours (includes retakes + screen recording setup)
**Target upload:** See filming schedule

---

## Pre-Production Checklist

### Routines Setup (CRITICAL — do this 30 min before filming)

- [ ] **Morning Inbox Digest Routine** — confirmed working, last run successful
- [ ] **Apify Competitor Monitor Routine** — confirmed working, output in Slack
- [ ] **New Routine for live build** — DO NOT pre-build. Start from scratch on camera.
- [ ] **Backup recordings** — run each Routine once before filming and screen-record the successful output, in case live demo fails
- [ ] **Slack channel clean** — pin the Routine output messages so they're at the top
- [ ] **Gmail test** — make sure you have 3-5 unread emails to triage for the inbox demo
- [ ] **OAuth connections** — verify Gmail, Slack, Apify connectors are all green

### Claude Code Local Setup

- [ ] Terminal at correct font size (readable on 1080p — 14pt minimum)
- [ ] Catppuccin dark theme or similar clean theme
- [ ] Working directory clean (no embarrassing files visible)
- [ ] `/yt-search` skill tested with "claude routines" query
- [ ] `/thumbnail` skill tested, ready to generate
- [ ] `/loop` command tested with a short interval (60s) so you don't wait
- [ ] Hide any API keys or secrets in terminal output

### Equipment

- [ ] Main camera (Tyler on camera for intro/outro/transitions)
- [ ] Screen recording software (OBS / ScreenFlow) running at 1920x1080 or 4K downscaled
- [ ] Audio: shotgun or lav mic, levels checked
- [ ] Second monitor for notes/script scroll
- [ ] CueCard app open with this script loaded
- [ ] Lighting: soft key + fill, no harsh shadows

### Thumbnail Reference Open

- [ ] `~/content/youtube/claude-routines-content-system/reference-thumbnails/nick-saraev.webp`
- [ ] Pull Nick's thumbnail up on a second monitor for reference while filming facial expressions

---

## Shot List (In Filming Order)

### Block 1 — On-Camera Takes (film first, while energy is fresh)

1. **Hook (0:00 - 1:00)** — On camera, direct to lens. Reshoot 3-5 times. Pick strongest.
2. **Transition beats** — 4-6 short on-camera takes:
   - "Okay let me show you what that actually looks like" (transition into demos)
   - "Alright, Routines are amazing for scheduled work, but there's a whole category they can't touch" (switch to Claude Code)
   - "Now the part nobody is covering" (/loop reveal)
   - "Here's my challenge to you" (action close)
   - "Thanks for watching" (outro)
3. **Retention hooks** — 4-5 short direct-to-camera punch-ins for editor to insert mid-sections

### Block 2 — Routines Demos (screen recording)

4. **Morning Inbox Routine** — click Run Now, show execution, cut to Slack output
5. **Apify Competitor Routine** — click Run Now, show execution, cut to Slack output
6. **Live Build Routine** — full walkthrough:
   - Click New Routine
   - Type name
   - Paste / type prompt (prepare prompt text in advance so you don't fumble)
   - Select repo, model, environment
   - Add schedule
   - Add connectors
   - Click Run Now
   - Show execution + output

### Block 3 — Claude Code Local Demos (terminal screen recording)

7. **`/yt-search claude routines`** — show initial run, results populating, then a follow-up iterative prompt
8. **`/thumbnail`** — generate thumbnail for this video, show all 3 variants
9. **`/loop`** — demonstrate with 30 second interval on a useful task

### Block 4 — Overlays + B-Roll

10. **Comparison table** — Routines vs Claude Code (designed in Figma or Canva, exported as PNG)
11. **Dollar number overlays** — "$3,000/month VA" "$800-1,500/month social media manager" "195 hours/year"
12. **Text callout slides** — "Routine = Claude Code + Schedule + Connectors (runs on cloud)"
13. **B-roll** — desk shots, hands on keyboard, coffee, etc. for cutaways during longer narration

---

## Delivery Tone Reminders

From Tyler's credibility memory (`user_credibility.md`):
- Confident but not arrogant
- State credentials as facts, not bragging
- Move quickly to the value after credibility
- Natural, conversational, short sentences
- Use "right?" as a verbal checkpoint
- Use "okay" as transitions
- Explain technical terms simply right after using them
- **No em dashes when speaking** (pause or comma instead)

**Energy:** Match the energy of the hook. Don't let it drop when you hit the technical sections. The goal is "friend who knows this stuff and is excited to share it," not "instructor giving a lecture."

---

## Retakes Priority

If you run long or something fails, these are the must-nail sections:

1. **Hook (0:00-1:00)** — biggest impact on CTR/retention
2. **Business case section (3:00-5:00)** — biggest impact on shareability
3. **Live Routine build (12:00-16:30)** — biggest impact on perceived value
4. **/loop reveal (20:30-23:30)** — your differentiation moment
5. **Action close (26:30-28:30)** — drives comments and Skool conversion

Everything else can be tightened in edit.

---

## Post-Production Notes

### Cuts & Pacing
- Aim for a cut every 4-6 seconds in the hook
- Screen recordings can breathe a bit more (6-10 seconds per cut)
- NO dead air. If you pause to think, cut it.
- Speed up any loading/execution that takes more than 15 seconds to 2x or 3x

### Graphics Needed
- Lower third with Tyler's name + "YouTube @ tylerprogramming" (first appearance)
- Dollar overlay graphics ($3,000 VA, $800 SMM, 195 hrs, pennies-per-run)
- Comparison table (Routines vs Claude Code) — design in Figma
- Section chapter titles as overlays ("Point 1: What Are Routines?")
- Skool community callout card for the action close

### Audio
- Remove ums, uhs, and filler words aggressively
- Light background music under hook and section transitions only, NOT under tutorial sections
- Ducking on music when you speak

### Chapters (for YT description)
After editing, run `/chapters` skill on the final video to generate accurate timestamps.

### SEO
After editing, run `/seo` skill to finalize title, description, and tags.

### Thumbnail
Generate via `/thumbnail` skill using:
- Reference: `reference-thumbnails/nick-saraev.webp`
- Text overlay from `titles.md` (Option A recommended)
- Tyler's likeness: `~/assets/identity/tylerai.png`

### Social Repurposing
After upload, run `/repurpose` skill to generate:
- 5 short-form scripts
- LinkedIn posts
- X threads
- Instagram carousels

---

## CueCard Setup For Filming

1. Open CueCard app
2. Load `~/content/youtube/claude-routines-content-system/script.md`
3. Position window near camera for eye contact
4. Set scroll speed to match your natural pace (usually 0.8x - 1.2x)
5. Use section navigation (left/right arrows) to jump between points if you retake

Note: Don't read the script verbatim. Use it as a scaffold. Your delivery is better when you paraphrase within each section than when you read line-by-line.

---

## Pro Tips

- **Film the live Routine build in ONE take if possible.** Cutting around mistakes makes it look edited. Authenticity sells.
- **Say the viewer's name in your head.** "Hey Mark, here's what you need to know." One person, not "everyone watching."
- **Stop apologizing.** No "sorry for the long intro" or "hopefully this was helpful." Confidence sells.
- **End each point with a mini-recap.** "So that's Routine one. Inbox triage. Saves me 195 hours a year." Helps retention.
