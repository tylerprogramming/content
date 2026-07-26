# Claude Opus 5 — Video Research (launched 2026-07-24)

**Purpose:** Plan a full hands-on video on Claude Opus 5, comparing it to Fable 5.
**Angle constraint (per [[tyler-voice]]):** This is NOT a benchmark/news recap. It's "I tested the new model on real automation and here is the honest take." Show what you can *build* with it, not a spec sheet.

---

## 1. What actually launched (the facts)

Anthropic released **Claude Opus 5** on **July 24, 2026** — two months after Opus 4.8. (Note: my cached model catalog stopped at Opus 4.8, so verify the exact API string in Anthropic's docs before you quote it on camera. Everything below is from launch-day reporting.)

| | **Claude Opus 5** | **Claude Fable 5** |
|---|---|---|
| API model id | `claude-opus-5` *(verify)* | `claude-fable-5` |
| Price / 1M input | **$5** | $10 |
| Price / 1M output | **$25** | $50 |
| Context window | 1M (default + max) | 1M |
| Thinking | On by default; **effort toggle** low/med/high (+xhigh) | Always on, can't disable |
| Positioning | New **default** for day-to-day / office work | The **ceiling** — hardest reasoning + long-horizon agentic |
| Data retention | **No** 30-day requirement | Requires 30-day retention (no ZDR) |
| Safety guardrails | Safeguards fire **~85% less** than Fable 5 | More restrictive (bio/cyber refusals) |

**The one-line story:** *Opus 5 gets you close to Fable 5's quality at half the price — and it's the model most people should now default to.*

## 2. What Anthropic says (official framing)

- Opus 5 "**approaches the capabilities of Fable 5 in many categories, at half the price**," and they expect it to be "the **default option for many day-to-day office needs**."
- It's **easier to use — less back-and-forth**; it "**verifies its own work and recovers from errors without intervention**."
- It **outperforms Fable 5 on several of the benchmarks** in the announcement.
- Demo they highlighted: it **wrote its own computer-vision pipeline from an incomplete prompt** (self-directed, filled the gaps).
- New **Automatic Fallbacks** (beta): when a safety classifier trips, it routes to a less-powerful model and returns a working answer instead of an error.
- Restrictions remain on cybersecurity (no binary vuln scanning; source-code analysis is fine).

## 3. The YouTube landscape (who's already covering it)

Fresh, from the last 24h — this is a crowded, fast-moving launch, so your edge is the **honest hands-on** angle, not being first.

| Views | Date | Title | Take |
|---|---|---|---|
| 58,945 | 07-24 | Opus 5 Just Dropped and Its Numbers Are Legit INSANE | hype/benchmarks |
| 45,449 | 07-24 | Vibe Coding With Claude Opus 5 (2hr) | live build |
| 20,137 | 07-24 | Claude Opus 5 is Going to Save You Money | **cost angle (strong)** |
| 17,699 | 07-24 | We Tested Claude Opus 5. Frustrating with Flashes of Brilliance | **honest test (your lane)** |
| 13,594 | 07-24 | Claude Opus 4.8 Is Acting Like Opus 5 | contrarian |

**Winning angles:** "we actually tested it" + "will it save you money vs Fable." Both fit your voice. The pure-benchmark videos will be a race to the bottom.

## 4. Recommended angle for YOUR video

**"I replaced Fable 5 with Opus 5 for a week of real automation. Here's what I found."**

- Frame around **your own workflows** (the automations you already run), not abstract benchmarks.
- The spine is the **cost/quality question**: *is Fable 5 worth double, or is Opus 5 good enough for the real work?*
- Stay honest (your differentiator): where Opus 5 wins, where Fable still wins, and the effort toggle as the practical lever.
- CTA ladder as usual: video → the prompts/setup in the community.

## 5. Demo prompts / things to build on camera (Opus 5 vs Fable 5)

Run each on **both models** so the whole video is a live A/B. These double as your "things to create with it."

**A. The one-sentence agentic build (headline demo)**
> "Build an agent that pulls the last 20 videos from these YouTube channels, scores each by views-per-day, and writes a ranked summary to a Google Sheet. Plan it first, then build and run it."
Compare: plan quality, how each handles the API setup, whether it self-corrects on the inevitable auth error, total tokens (cost), wall-clock.

**B. The self-verification / incomplete-prompt test** (mirrors Anthropic's CV-pipeline demo)
> "Here's a rough idea and a half-finished script. Figure out what I actually need, fill the gaps, get it working, and tell me what you changed and why."
Whoever recovers from errors with less hand-holding wins — that's Opus 5's whole pitch.

**C. The effort-toggle cost curve** (the feature nobody else will demo well)
Run the *same* real task at **low → medium → high → xhigh** and put the token cost + output quality side by side. This is the most useful, most saveable segment.

**D. The "is Fable worth 2x?" money math**
Take one real task you'd actually run daily, show the token count, multiply out: Opus 5 ($5/$25) vs Fable 5 ($10/$50). Concrete dollars on screen. (This is the 20k-view "save you money" angle, done honestly.)

**E. Rebuild one of your existing skills on Opus 5**
Point it at a skill you already use (e.g. a `/yt-` skill) and have Opus 5 improve or extend it — show it's cheaper/faster for the work you're already doing.

**F. The guardrails difference** (optional, keep it clearly legitimate)
A benign task Fable 5 over-refuses that Opus 5 handles (Opus 5 fires safeguards ~85% less). Only use a clean, defensible example.

## 6. Title / hook directions (draft — run through /yt-seo later)

- "I tested Claude Opus 5 on my real automations (honest take)"
- "Claude Opus 5 vs Fable 5 — is the expensive one worth it?"
- "The new Claude is half the price. Is it good enough?"
- Hook: *"Anthropic just shipped a model that's almost as good as their best one for half the price. So I pointed it at the work I actually do."*

## 7. Sources
- [TechCrunch — Anthropic launches Opus 5](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)
- [Fortune — how Opus 5 is different (cost/capability toggle)](https://fortune.com/2026/07/24/anthropic-debuts-claude-opus-5-with-feature-that-lets-users-toggle-between-cost-and-capability/)
- [Bloomberg — affordable workplace tasks](https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks)
- [Quartz — half the price of Fable 5](https://qz.com/anthropic-claude-opus-5-fable-5-price-072426)
- [9to5Mac — Opus 5 details](https://9to5mac.com/2026/07/24/anthropic-upgrades-claude-with-new-opus-5-model-details-here/)
- [OpenRouter — Opus 5 pricing/providers](https://openrouter.ai/anthropic/claude-opus-5)
