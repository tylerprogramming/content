# YouTube Brain

Part of the central BRAIN at `~/content/BRAIN/`. The living playbook for the Tyler AI channel (@TylerReedAI, ~23.5K subs). Jarvis's post-mortem agent updates this after every video review; the pre-flight gate and /yt-package read it FIRST. Structured per-video data lives in the Supabase `video_learnings` table; this file is the synthesized rules.

## Identity [confirmed 2026-06-22]
- **Tyler is a SHOWCASE creator, not a teacher.** Proven lane: 10-18 min showcase of a new/hot tool or capability ("I connected X to Y", "I automated Z", "Google is winning with X").
- AVOID "Master / Full Course / Explained / Tutorial" framing - that framing is the drag regardless of length (worst video: teach + 32 min = 171 views).
- Holds outside the channel [2026-08-02]: a 4-hour "AI AGENTS MASTERCLASS" on a 73.9K-sub channel pulled 21 views/day/1k subs in the same 14-day window where short outcome-titled builds pulled 41 to 153. Same lane, same week, one fifth the pull.
- Showcase winners: "I Automated My Entire YouTube Workflow" (2,803), "Google is Winning With Antigravity" (2,405), "Build ANYTHING With Claude Code" (1,862).

## Titles [confirmed 2026-08-02]
- Concrete OUTCOME or curiosity gap, never a description.
- Winning in-niche patterns: $ outcomes ("Claude Code + YouTube = $62K/Month"), % + time ("97% in 16 min"), insider/authority ("How Anthropic Engineers ACTUALLY..."), curiosity ("#1 Problem").
- No-outcome-hook titles ("I Automated X", "I Don't X Anymore") are now landing BELOW the old 300-500 week-1 baseline, not at it. Treat 300-500 as a ceiling for this class, not a floor. Three in a row: 483, 171, 232.
- A status claim ("I Don't Edit Videos Anymore") is not a payoff. Needs time saved, $ result, or a specific number.
- Title = payoff/stakes; thumbnail = the what/proof. Complement, don't repeat.
- Out-of-niche confirmation [2026-08-02]: the two hardest 14-day outliers both carry a number in the title. "$10,000" (12.3K-sub channel, 1.53x its own sub count in 10 days) and "in 14 minutes" (149K subs, 41 views/day/1k subs). The number is doing the work, not the channel.

## Topic reach [confirmed 2026-08-02]
- The problem in the title must be one a non-creator also has. Creator-only promises (editing, thumbnails, uploading) cap the addressable click before the video is judged.
- Evidence: creator-only topics cdvi2ooarDc (232) and h5VtHSXY8Hc (155) vs general automation T50plh-k3MY (483) and akcCiWLe51Q (592).
- Same test tyler-voice.md applies to written posts: the takeaway should transfer to someone who has never made a video. It applies to titles too.

## Thumbnails [confirmed 2026-06-21]
- Real expressive face (genuine smile/pointing) OR clean command/concept hero. Flat faces and AI-cartoon characters = ~3% CTR.
- Show the actual thing: real terminal, real SKILL.md, real number. 3-4 words max, one word in accent color. Composite the real Claude logo.
- Likeness generations anchor to `~/assets/identity/tylerai.png`.
- CTR is the persistent weak spot (~3% band). Use Studio's native Test & Compare.

## Retention [confirmed 2026-06-22]
- Fix the cold open: value in the first 60 seconds, proof-first, no slow intro.
- Sharper version [2026-08-02]: put a number in the FIRST SENTENCE. All three top-performing agent videos this window do it ("$10,000", "Four AI agents", "14 minutes") and each names the specific gap it closes before second 30. Not a promise of value, a quantity.
- Focused single-topic long-form (5-12 min) retains 35-53%; 20+ min courses retain 6-22%.
- Long evergreen content is slow-burn via search; day-1 undersells it.
- Shorts (~53% retention) and long-form (~34%) are different games - analyze separately.

## Traffic reality [confirmed 2026-06-22]
- Claude content does NOT rank in YouTube search (legacy crewai/algorithms videos do). Growth depends on Shorts + Browse + external.
- Suggested 2.6% and Subscriber 3.7% traffic = packaging + loyalty problem to fix.

## Mindset
A flop is data about packaging, not a verdict on Tyler. Every result is A/B input.

## Changelog
- 2026-08-02: Study pass read three 14-day agent-lane winners end to end (V7_YUe5skv8, TL8V41Ea6oM, UyoVmQLekBc). Confirmed the number-in-title rule and the anti-masterclass rule with out-of-niche evidence, and sharpened the cold-open rule to "number in the first sentence." No rule contradicted. Full report in jarvis/reports/2026-08-02-study.md.
- 2026-08-02: Tightened Titles rule and added Topic reach section. cdvi2ooarDc backfill review: 232 views in 10 days (23.2/day, roughly 31/day at day 7) vs T50plh-k3MY at 60/day at day 7. Below the 300-500 baseline, so that band is now a ceiling for outcome-free titles. Creator-only topic flagged as the second cap.
- 2026-07-22: Confirmed Titles baseline rule with day 7 data. T50plh-k3MY finished at 419 views (60/day), confirming 300-500 baseline for "I Automated X" without outcome hooks. WJabXRVe8JQ at 130 views (day 3, 43/day) tracking to same baseline.
- 2026-07-21: Updated Titles section with "I Automated X" baseline rule. Evidence: T50plh-k3MY (408 views/6 days) and WJabXRVe8JQ (118 views/2 days) both follow showcase formula but lack outcome hooks, tracking at baseline not breakout.
- 2026-07-20: seeded from youtube-channel-playbook memory by Jarvis build.
