# Filming Guide: Claude Code Email System

**Runtime target:** 28-32 min
**Filming session:** 90-120 min
**Recording stack:** Face cam + screen recording (OBS), lapel mic

---

## Critical Pre-Production Sanity Checks

This video shows real email infrastructure. ANY of the following on screen = bad day:
- [ ] Real customer emails — blur in edit or use `example@example.com` substitutes
- [ ] Your Resend API key — never visible in terminal, env, or browser dev tools
- [ ] Your `.env` file — never open it on camera, period
- [ ] Skool member real names — anonymize or only show test member records
- [ ] Domain you don't want public — your sending domain WILL be in some email headers

**Do a full dry-run with a screen recorder before official take. Watch the recording. If you see anything sensitive, fix it before going live.**

---

## Demo Prep (do these BEFORE filming)

1. **Create 3 test contacts** in your SQLite that look real but aren't:
   - `alice.tester@example.com`, `bob.demo@example.com`, `carol.preview@example.com`
   - Insert them with timestamps that put them at different campaign steps (one due for step 1, one for step 2, one for step 3)

2. **Pre-populate `email_sends`** with some fake history so the SQL queries look real on camera

3. **Send 1 real test email to yourself** with a beautiful HTML template — screen-capture it for b-roll

4. **Have the ConvertKit pricing tab open** (or Beehiiv, or whichever competitor you're roasting) so the cold-open shot is one keystroke away

5. **Smoke test every command in the script** in the 24 hours before recording

---

## Shot List

### Segment 0 — Cold Open (0:00-0:30)
- Browser tab: competitor pricing page → cursor closes it
- Terminal opens, types `/email`
- VO: layered separately

### Segment 1 — Pain Point (0:30-2:30)
- Face to camera, slight pacing energy
- Use a whiteboard or on-screen text overlay to list the 3 email types (one-off, blast, drip)

### Segment 2 — Architecture (2:30-6:00)
- Animated diagram preferred (Remotion if you have time, or just a clean Excalidraw)
- 3 boxes: Resend → Claude Code → SQLite
- Cut back to face for the explanation

### Segment 3 — Demo 1: One-off (6:00-11:00)
- Real terminal recording
- Show the HTML preview before sending
- Show the Resend ID in the success message

### Segment 4 — Demo 2: Drip (11:00-19:00)
- THE LONGEST SEGMENT — give it room
- Open SQLite browser (TablePlus or DB Browser for SQLite)
- Walk through each table — campaigns, steps, sends
- Dry-run first, then live send
- Show open tracking script running

### Segment 5 — Demo 3: Blast (19:00-23:00)
- Show batching in action (50 at a time)
- Don't actually blast 247 real people — use the dry-run output or use a tiny test list

### Segment 6 — Build Your Own (23:00-27:00)
- Show `SKILL.md` opening in VS Code with syntax highlighting
- Show the folder structure: skill folder, Python scripts, templates
- Don't write code on camera — show the finished files and explain

### Segment 7 — Trade-offs (27:00-29:00)
- Face to camera, honest tone
- This builds trust — don't skip it

### Segment 8 — CTA (29:00-31:00)
- Direct to lens, energy up
- Mention the companion video (`7-skills-run-my-business`)

---

## Energy Cues

| Segment | Energy | Notes |
|---|---|---|
| Cold open | 10/10 | Drama of cancelling a paid tool |
| Pain point | 7/10 | Empathy with the viewer's pain |
| Architecture | 6/10 | Teaching mode, calm and clear |
| Demo 1 | 7/10 | Quick wins energy |
| Demo 2 (drip) | 8/10 | The "wow" moment |
| Demo 3 (blast) | 7/10 | Practical, fast |
| Build your own | 8/10 | Empowering — they can actually do this |
| Trade-offs | 6/10 | Honest, grounded |
| CTA | 10/10 | Get the click |

---

## Common Pitfalls

1. **Showing real data** — see the sensitive content checklist above
2. **The drip demo dragging** — keep it under 8 min. If you get stuck explaining SQLite, cut and reshoot
3. **Sounding like an ad for Resend** — you're not paid by them. Mention the trade-offs (no GUI, deliverability on you)
4. **Burying the build instructions** — Segment 6 is what makes this a useful video. Don't rush it
5. **Reading the script** — riff. The architecture section especially should feel conversational

---

## Post-Production

- Chapters already in script.md — paste into YouTube description
- Run `/chapters` on final cut to confirm timestamps
- Thumbnail brief: dark BG, "BYE CONVERTKIT" or "$0/MO" giant white text, Tyler face surprised/satisfied, orange asterisk, small terminal icon
- Music: subtle under face-to-camera segments only, none under terminal demos

---

## After-Filming Checklist

- [ ] Watch the full recording for sensitive content
- [ ] Render once at 720p for review
- [ ] Send to editor with cuts list
- [ ] Generate companion social posts via `/content claude-code-email-system`
- [ ] Add to status.md
- [ ] Update video-ideas.md to mark this idea Completed
