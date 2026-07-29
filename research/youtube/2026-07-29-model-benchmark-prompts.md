# Established LLM Benchmarks + Their Real Prompts (for 3-way model test)

**Purpose:** Run the SAME community-known benchmark prompts on **Opus 4.8 → Opus 5 → Fable 5** so the comparison is credible (not "vibes"). These are prompts other people already use to compare models, so viewers recognize them.

**The 3-way story:**
- **Opus 4.8** = the model you were already on (baseline)
- **Opus 5** = the free upgrade (same price as 4.8: $5/$25 per 1M)
- **Fable 5** = the premium (double: $10/$50 per 1M)
Same prompt, all three, then show score + cost. The punchline writes itself: is the free upgrade better than what you had, and is the expensive one worth 2x?

---

## The prompts (verbatim, attributed)

### 1. Bouncing ball in a spinning hexagon (the viral one)
**Source:** aligeramy/ai-benchmark (widely copied since early 2025)
**Prompt:**
> Write a Python program that shows a ball bouncing inside a spinning hexagon. The ball should be affected by gravity and friction, and it must bounce off the rotating walls realistically.

**Tests:** physics reasoning, geometry, real-time graphics. Simplest to run, most recognizable. Good opener.

### 2. 20 balls in a spinning heptagon (the hard one, has a real rubric)
**Source:** KCORES LLM Arena (`kcores-llm-arena`). Scored on 18 criteria / 90 points; best of 3 runs.
**Prompt:**
> Write a Python program that shows 20 balls bouncing inside a spinning heptagon. All balls have the same radius, are numbered 1 to 20 with a distinct color each, and drop from the center of the heptagon at the start. The balls are affected by gravity and friction, and must bounce off the rotating walls realistically; a ball's bounce height should not exceed the heptagon radius but should be larger than the ball radius. The heptagon spins around its center at a speed of 360 degrees per 5 seconds. Do not use the pygame library; implement collision detection and collision response yourself. Allowed libraries: tkinter, math, numpy, dataclasses, typing, sys. Put all code in a single Python file.

**Tests:** the big one. Self-implemented physics, many-body collisions, spin, numbering/color spec-following. This is where models separate. GPT-4.5-Preview once hit a perfect 90.
**Scoring (their rubric, simplified for camera):** single file (5), library rules (5), correct ball count/size/numbers/colors, gravity, friction, wall collisions, ball-ball collisions, spin speed, smoothness. Score /90.

### 3. SVG of a pelican riding a bicycle (Simon Willison's benchmark)
**Source:** simonw/pelican-bicycle (the famous one; every new model gets this)
**Prompt:**
> Generate an SVG of a pelican riding a bicycle.

**Tests:** spatial reasoning, composition, valid SVG, restraint. Fast, funny, visual. Great B-roll and instantly recognizable to the audience.

### 4. Flappy Bird in a single HTML file (community staple)
**Source:** widely used single-file game test
**Prompt:**
> Build Flappy Bird as a single self-contained HTML file, vanilla JavaScript, no libraries. The bird flaps on spacebar or click and is pulled down by gravity. Pipes scroll in from the right with gaps to fly through. Add collision detection, a score counter that goes up for each pipe passed, and a game-over screen with a restart button.

**Tests:** game loop, physics, state, input, UI. Very watchable, everyone knows the game.

### 5. Suika / watermelon merge game (you already have this)
**Source:** your own spec in `041-claude-opus-5/filming-guide.md`
**Tests:** physics + state + "does it feel good." Keep using your version for continuity.

---

## How the public benchmarks score (name-drop for credibility)
- **pass@1 / pass@k** — did the first (or any of k) attempt run correctly
- **KCORES heptagon** — 90-pt rubric above
- **V-GameGym** — game generation scored on code quality, visual output (screenshot), dynamic behavior (gameplay video); top models only ~45%
- **World of AI Bench** — AI-judged on functionality, design, code quality, creativity, composite. Leaderboard currently led by **Fable 5 at 85.2** (real data: Fable tops it, but it's 2x the price)
- **Your two axes that matter most on camera:** cost (tokens x price) and time to finish

## Suggested scoring for the video (simple, defensible)
For each prompt, score all three models on:
1. **Runs?** (yes/no - the gate)
2. **Correctness / spec-following** (out of 5, or the heptagon /90)
3. **Feel / polish** (out of 5)
4. **Cost** (real dollars from token counts)
5. **Time** (seconds to finish)
Then a one-line verdict per prompt. Land the pattern: Opus 5 >= 4.8 at the same price, and within reach of Fable at half the cost.

---

## Sources
- Hexagon: https://github.com/aligeramy/ai-benchmark
- Heptagon (rubric): https://github.com/KCORES/kcores-llm-arena
- Pelican: https://github.com/simonw/pelican-bicycle
- V-GameGym: https://v-gamegym.github.io/index.html
- World of AI Bench: https://www.woaibench.ai/
- Coding benchmarks 2026: https://tolearn.blog/blog/llm-coding-benchmark-comparison-2026
