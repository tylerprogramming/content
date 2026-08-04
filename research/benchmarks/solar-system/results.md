# model-bench results

**Prompt:** Create a 3D solar system in a single self-contained HTML file using three.js loaded from a CDN. The sun at the center, planets orbiting at different speeds, and a camera you can orbit with the mouse. No build step, it should just run when the file is opened.

_Cost = equivalent API cost from task tokens (subscription run, no real charge)._

| Model | In | Out | Cost | Time | Type | Output | Runs? | Score |
|---|---|---|---|---|---|---|---|---|
| opus-4.8 | 10 | 4456 | $0.1114 | 56.4s | html | `opus-4-8.html` |  |  |
| opus-5 | 10 | 19539 | $0.4885 | 225.3s | html | `opus-5.html` |  |  |
| fable-5 | 10 | 10265 | $0.5133 | 130.1s | html | `fable-5.html` |  |  |
_Fill in Runs? and Score by opening/running each output._
