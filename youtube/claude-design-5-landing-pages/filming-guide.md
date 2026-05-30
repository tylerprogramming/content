# Filming Guide — 5 Landing Pages in One Afternoon

## Pre-recording prep

**⚠️ Critical:** you'll burn ~65% of weekly Claude Design Pro allowance. Pick a week with no other Claude Design work planned. Alternatively do this on Max plan.

- [ ] Vercel project with 5 route slots planned: `/argus`, `/northbound`, `/luna`, `/sam-grant`, `/harbor-dental`
- [ ] Master prompt template finalized (see below)
- [ ] Shared design system set up ONCE before filming (saves your usage for the actual builds)
- [ ] Nano Banana credits ready — you'll generate ~8-10 placeholder images
- [ ] Camtasia 1080p, screen + camera tracks
- [ ] Dedicate a full 4-hour block. Do not interrupt.

## The master prompt template

```
Build a landing page for [PRODUCT NAME], a [INDUSTRY] [product/service].
Target audience: [AUDIENCE DESCRIPTION].
Tone: [TONE — e.g. professional-technical, warm-editorial, friendly-trustworthy].
Primary CTA: [PRIMARY ACTION].

Include sections:
- Hero (headline + subhead + primary CTA + visual)
- 3-column features/services grid
- Social proof (testimonials or stats)
- Secondary section appropriate to industry
- Final CTA + footer

Use my design system.

Before generating, ask me 4 clarifying questions.
```

Fill in the 5 bracketed variables for each build. Everything else stays the same.

## Shot list per build (repeat × 5)

1. Timer overlay (counts down from 4:00:00)
2. Master prompt with variables filled in
3. Claude Design Q&A (4 questions + your answers)
4. Generation time-lapse
5. 2-3 tweak moments
6. Export / hand-off
7. Claude Code running in VS Code
8. Localhost preview
9. Git push
10. Vercel deploy
11. Live URL reveal with scroll

**Per-build time budget on camera:** ~2:30 compressed from ~40 min real-time work.

## Critical editing note

This video lives or dies on editing. Each build must compress to 2:30 from 40 minutes of real work. Use time-lapses, jump cuts, speed ramps. Don't let any single build feel slow.

## The 5 side-by-side shot

At minute 15, show all 5 live URLs in a browser tab cycle. Each gets 5-6 seconds. This is the emotional payoff of the video.

## Target runtime: 20 minutes
