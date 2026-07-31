# Claude Model Benchmark — Final Scorecard

**Opus 4.8 ($5/$25)  vs  Opus 5 ($5/$25)  vs  Fable 5 ($10/$50)** — same prompt, three models, run on the subscription via `/model-bench`. Cost = equivalent API cost from output tokens. "Runs?" verified by opening/running each output.

## Builds

| Prompt | Metric | Opus 4.8 | Opus 5 | Fable 5 |
|---|---|---|---|---|
| **Hexagon ball** (Python) | Cost | **$0.095** | $0.276 | $0.245 |
| | Time | **52s** | 126s | 59s |
| | Out tokens | 3,797 | 11,047 | 4,891 |
| **Suika** (HTML) | Cost | **$0.344** | $0.696 | $1.706 |
| | Time | **174s** | 315s | 443s |
| | Out tokens | 13,764 | 27,824 | 34,113 |
| **Flappy Bird** (HTML) | Cost | **$0.115** | $0.249 | $0.290 |
| | Time | **53s** | 108s | 68s |
| | Out tokens | 4,599 | 9,966 | 5,795 |
| **Solar system** (HTML) | Cost | **$0.111** | $0.489 | $0.513 |
| | Time | **56s** | 225s | 130s |
| | Out tokens | 4,456 | 19,539 | 10,265 |
| **Design-to-code** (HTML) | Cost | **$0.162** | $0.300 | $0.389 |
| | Time | **70s** | 135s | 92s |
| | Out tokens | 6,476 | 12,003 | 7,771 |

Every build **ran** on all three models (Runs? = ✅ across the board).

## Reasoning trio (all three correct on all three models ✅)

| Puzzle | Correct? | Opus 4.8 | Opus 5 | Fable 5 |
|---|---|---|---|---|
| Strawberry (3 r's) | ✅✅✅ | $0.0026 / 2.7s | **$0.0001 / 1.8s** | $0.0035 / 2.9s |
| Alice (3 sisters) | ✅✅✅ | $0.0054 / 4.2s | **$0.0023 / 2.6s** | $0.0085 / 3.7s |
| Marble (on table) | ✅✅✅ | $0.0066 / 5.0s | $0.0062 / 4.7s | **$0.0074 / 3.4s** |

## Totals (all 8 prompts)

| | Opus 4.8 | Opus 5 | Fable 5 |
|---|---|---|---|
| **Total cost** | **~$0.84** | ~$2.02 | ~$3.16 |
| **vs cheapest** | — | 2.4x | **3.8x** |
| Cheapest on builds | **5 / 5** | 0 | 0 |
| Fastest on builds | **5 / 5** | 0 | 0 |

## The verdict

- **Opus 4.8 = the value winner.** Cheapest AND fastest on every single build, ~1/4 of Fable's total cost. If you can't see a quality difference, it's the obvious daily driver.
- **Opus 5 = right-sizes effort.** Leanest/cheapest on reasoning (5-token "Three."), but over-generates on builds (2–4x the code, ~2x cost/time). Only "cheaper" if the extra code earns it.
- **Fable 5 = premium tax.** Priciest every time (2x rate), occasionally wild (Suika alone: $1.71). Fast enough, but you pay.
- **Reasoning is solved** — all three ace every puzzle. Not a differentiator.

**The one axis left = visual/play quality** (does Opus 5's / Fable's extra code actually look or feel better?). That's the on-camera judgment call, filled in live. Everything measurable already points one way: **the cheap model kept winning.**
