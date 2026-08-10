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
- Insider/authority names pull like numbers [2026-08-05]: "Andrej Karpathy Just Fixed Claude Code's Biggest Weakness" hit 4.5x channel size in 2 days (55K on 12.3K subs); "6 NEW Rules by Anthropic Engineers" 0.43x in 2 days on 163K. A recognized insider name in the title is a payoff signal, same class as a number.
- Killing a named subscription is a $ outcome [2026-08-05]: "This 1 Claude Skill fully replaces your Higgsfield Subscription" did 1.09x on a 163K channel. Naming the product being cancelled (and its monthly price early) works like a dollar figure. Tyler already runs the Kie.ai version of this stack daily.
- CORRECTED [2026-08-10]: "I Automated X" is two classes, not one. **Entire + a whole system is a payoff in its own right**, in the same slot a number or a dollar figure fills. Whole-system titles: "I Automated My Entire YouTube Workflow" (2,803), "I Automated My Life with Claude Routines" (523), and -dEeg0WnJxs at 184 on day 1, the best day 1 in the store. Single-task titles with no payoff are the ones that cap: "I Automated My Video Ads" (186), "I Don't Edit Videos Anymore" (256). Do not treat the 300-500 ceiling as covering both.
- SCOPED [2026-08-08]: the number rule holds for showcase builds, NOT for reactive review. First in-channel test, J5lkE_jBEko ("Half the Price"), ran 60/74/45 over three days and never separated from the no-hook control (T50plh-k3MY, 419 at day 7). A price hook does not rescue a format the moment does not want. Do not credit a number in the title on launch-coverage content.

## Topic reach [confirmed 2026-08-07]
- The problem in the title must be one a non-creator also has. Creator-only promises (editing, thumbnails, uploading) cap the addressable click before the video is judged.
- Evidence: creator-only topics cdvi2ooarDc (232) and h5VtHSXY8Hc (155) vs general automation T50plh-k3MY (483) and akcCiWLe51Q (592).
- Runtime is not the cap, topic reach is [2026-08-07]: the channel's two worst recent lifetimes are both in the 17-20 min band (WJabXRVe8JQ 17.7 min at 180, h5VtHSXY8Hc 19.8 min at 167), and both are creator-only topics. J5lkE_jBEko is 18.3 min on a general topic (model pricing) and passed 134 in two days. Do not shorten a video to fix a reach problem.
- Same test tyler-voice.md applies to written posts: the takeaway should transfer to someone who has never made a video. It applies to titles too.
- NARROWED [2026-08-10]: the cap is on creator-only **tasks**, not creator-set **systems**. Editing (cdvi2ooarDc, 256 lifetime) and thumbnails (h5VtHSXY8Hc, 167 lifetime) are single chores only a creator has. A whole content workflow is a pipeline anyone recognises, and -dEeg0WnJxs did 184 on day 1, passing h5VtHSXY8Hc's entire 32-day lifetime in 24 hours, at 33.2 min. Apply the transfer test to the promise, not to the setting: if the system generalises to anyone's repetitive work, YouTube being the setting does not cap it. Pending confirmation at day 3 on 08-12.

## Format vs topic [new 2026-08-08]
- A launch-reactive topic decays in days, not weeks. Match the runtime to the spike: cover a model launch in short-form and a text breakdown, and save 15+ min long-form for builds that stay true for months.
- Evidence: the Opus 5 pricing topic beat its own baseline on three platforms in the same 48 hours it went average on YouTube. X costs thread 133 on day 1 vs a day-1 median of 78; TikTok cutdown 201 in 24 hours; Instagram 54 on day 1 vs 30 and 28 lifetime for the only other IG posts. The 18.3 min YouTube version paced to roughly the channel median.
- The distinction that matters: this is not a dead topic, it is a topic that wanted a different container. Do not retire a subject because the long-form underdelivered; check whether the short version outran its own platform first.
- Measurement caution: a `method: lifetime` breakout flag is not evidence. TikTok showed 68.1x purely because collection started 2026-08-04 and captured 26 mature posts at near-zero velocity. Only compare same-age, and only on a platform where young-post readings actually exist (currently X and YouTube).

## Thumbnails [confirmed 2026-06-21]
- Real expressive face (genuine smile/pointing) OR clean command/concept hero. Flat faces and AI-cartoon characters = ~3% CTR.
- Show the actual thing: real terminal, real SKILL.md, real number. 3-4 words max, one word in accent color. Composite the real Claude logo.
- Likeness generations anchor to `~/assets/identity/tylerai.png`.
- CTR is the persistent weak spot (~3% band). Use Studio's native Test & Compare.

## Retention [confirmed 2026-06-22]
- Fix the cold open: value in the first 60 seconds, proof-first, no slow intro.
- Sharper version [2026-08-02]: put a number in the FIRST SENTENCE. All three top-performing agent videos this window do it ("$10,000", "Four AI agents", "14 minutes") and each names the specific gap it closes before second 30. Not a promise of value, a quantity.
- Widened [2026-08-05]: the first sentence needs a number, an insider name, OR a named villain. This week's 4.5x video opens on a Karpathy clip, the 1.09x one opens "I just replaced Higgsfield" with the price seconds later. All three winners state their concrete hook in sentence one; none warms up.
- Focused single-topic long-form (5-12 min) retains 35-53%; 20+ min courses retain 6-22%.
- Long evergreen content is slow-burn via search; day-1 undersells it.
- Shorts (~53% retention) and long-form (~34%) are different games - analyze separately.

## Traffic reality [confirmed 2026-06-22]
- Claude content does NOT rank in YouTube search (legacy crewai/algorithms videos do). Growth depends on Shorts + Browse + external.
- Suggested 2.6% and Subscriber 3.7% traffic = packaging + loyalty problem to fix.

## Mindset
A flop is data about packaging, not a verdict on Tyler. Every result is A/B input.

## Changelog
- 2026-08-10: Day-1 read on -dEeg0WnJxs ("I Automated My Entire Content Workflow with Claude Code") contradicts two rules at once: 184 views in 24 hours, 3.1x the only other day-1 reading in the store (J5lkE_jBEko at 60), at 33.2 min on a creator-set topic. Corrected the Titles rule to split "I Automated X" into whole-system (Entire is the payoff: 2,803, 523, and this one) versus single-task (186, 256, capped). Narrowed Topic reach to cap creator-only tasks rather than creator-set systems. Runtime-is-not-the-cap confirmed a second time. Both changes ride on a sample of one and get their real test at day 3 on 08-12. No companion post exists on any other platform, so the cross-platform read was YouTube only; a cutdown is the missing test. Report in jarvis/reports/2026-08-10-postmortem-automated-entire-content-workflow.md.
- 2026-08-08: Day-3 read on J5lkE_jBEko resolves the number-in-title test: 179 views (60/74/45 daily adds), the day-2 acceleration reversed, and it never separated from the no-hook control. Scoped the number rule to showcase builds only, not reactive review. Added the Format vs topic section: the same Opus 5 pricing topic beat its own baseline on X, TikTok and Instagram in the same window it went average on an 18.3 min YouTube video, so the topic was fine and the container was wrong. Also recorded the measurement caution that `method: lifetime` breakout flags are artifacts when the collector has no young-post baseline. Report in jarvis/reports/2026-08-08-postmortem-opus-5-half-the-price.md.
- 2026-08-07: Day-2 read on J5lkE_jBEko: 134 views (67/day), day 2 adding more than day 1, level with T50plh-k3MY at the same age and still not separated from the no-hook class. Number-in-title rule unchanged and still pending the day-7 call, but two clean days of level pacing leans toward "number hooks work on showcase builds, not on reactive review." Confirmed Topic reach and added the runtime-is-not-the-cap rule from in-channel evidence. Report in jarvis/reports/2026-08-07-postmortem-opus-5-half-the-price.md.
- 2026-08-06: First in-channel test of the number-in-title rule is live: J5lkE_jBEko ("Half the Price") did 60 views on day 1, even with the no-hook class at the same age, not ahead of it. No rule changed; the day-7 postmortem decides whether the number rule holds for reactive review content or only for showcase builds. Report in jarvis/reports/2026-08-06-postmortem-opus-5-half-the-price.md.
- 2026-08-05: Study pass read three 14-day lane winners end to end (jI4ZVB_MPhU, 9C4TRbucmhQ, gQeRjkb_Hlc). Added two Titles rules (insider names pull like numbers; killing a named subscription is a $ outcome) and widened the cold-open rule to number OR insider name OR named villain in sentence one. No rule contradicted. Full report in jarvis/reports/2026-08-05-study.md.
- 2026-08-02: Study pass read three 14-day agent-lane winners end to end (V7_YUe5skv8, TL8V41Ea6oM, UyoVmQLekBc). Confirmed the number-in-title rule and the anti-masterclass rule with out-of-niche evidence, and sharpened the cold-open rule to "number in the first sentence." No rule contradicted. Full report in jarvis/reports/2026-08-02-study.md.
- 2026-08-02: Tightened Titles rule and added Topic reach section. cdvi2ooarDc backfill review: 232 views in 10 days (23.2/day, roughly 31/day at day 7) vs T50plh-k3MY at 60/day at day 7. Below the 300-500 baseline, so that band is now a ceiling for outcome-free titles. Creator-only topic flagged as the second cap.
- 2026-07-22: Confirmed Titles baseline rule with day 7 data. T50plh-k3MY finished at 419 views (60/day), confirming 300-500 baseline for "I Automated X" without outcome hooks. WJabXRVe8JQ at 130 views (day 3, 43/day) tracking to same baseline.
- 2026-07-21: Updated Titles section with "I Automated X" baseline rule. Evidence: T50plh-k3MY (408 views/6 days) and WJabXRVe8JQ (118 views/2 days) both follow showcase formula but lack outcome hooks, tracking at baseline not breakout.
- 2026-07-20: seeded from youtube-channel-playbook memory by Jarvis build.
