# Filming Guide — Claude Design + Kling 3 Animated Hero

## Pre-recording prep

- [ ] Claude Design at ~0% weekly usage (this uses ~15-20%)
- [ ] Kling 3 credits available — minimum $5 reserved for this build
- [ ] Vercel account + repo wired up (same as main Claude Design video)
- [ ] Reference screenshots saved: Apple.com, Stripe.com, Linear.app hero sections (for the "why animated heroes matter" section)
- [ ] Save to `~/content/youtube/claude-design-kling-animated-hero/b-roll/`
- [ ] ffmpeg installed (`brew install ffmpeg` if not)

## Shot list

1. **Hook:** 4-second animated hero playback (record this at the END, after the full build, so the result is real)
2. **Apple/Stripe/Linear** product page scrolls (3-5 sec each)
3. **Claude Design prompt + 4-question Q&A**
4. **Generated landing page scroll**
5. **PNG export of hero section**
6. **Kling 3 interface:** drop PNG, type prompt, generate
7. **Kling video playing** full screen
8. **Cost panel** close-up
9. **Claude Code terminal** with the video-embed prompt
10. **Drop MP4 into /public/assets**
11. **Localhost showing animated hero**
12. **Vercel deploy dashboard**
13. **Live URL** with animated hero on production
14. **Outro** talking head + Skool preview

## Key tactical nuggets to hit

- The "subtle" prompt tip (section 4) is the tactical unlock. Don't skip it.
- The ffmpeg compression one-liner for hero videos: `ffmpeg -i hero-raw.mp4 -vf "scale=1920:-2" -c:v libx264 -preset slow -crf 28 -c:a copy hero-optimized.mp4` — mention this or put it in the description.
- The phone-mockup-floating motion is proven. Stick with it for the demo.

## Alternative products to demo (pick one)

- AI workout coach app (current script)
- Direct-to-consumer skincare brand
- SaaS dev tool (terminal + glowing particles would look great)
- Restaurant/hospitality (food-focused animation)

## On-camera tips

- The hero reveal at 0:00 needs 4+ seconds onscreen before any narration. Let it breathe.
- When you show the cost ($0.50 for Kling) — pause on it. That's the trust moment.
- Don't hype. The animated result sells itself.

## Target runtime: 14-15 minutes
