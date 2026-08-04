# model-bench results

**Prompt:** Build a complete, playable Suika (watermelon merge) game in a single self-contained HTML file, vanilla JavaScript and canvas, no libraries. Fruits drop from the top, same-size fruits merge into the next size with gravity and collisions, score goes up on each merge, and it is game over if the pile overflows the top. Make it fun to play.

_Cost = equivalent API cost from task tokens (subscription run, no real charge)._

| Model | In | Out | Cost | Time | Type | Output | Runs? | Score |
|---|---|---|---|---|---|---|---|---|
| opus-4.8 | 10 | 13764 | $0.3442 | 174.3s | html | `opus-4-8.html` |  |  |
| opus-5 | 8 | 27824 | $0.6956 | 314.9s | html | `opus-5.html` |  |  |
| fable-5 | 8 | 34113 | $1.7057 | 442.9s | html | `fable-5.html` |  |  |
_Fill in Runs? and Score by opening/running each output._
