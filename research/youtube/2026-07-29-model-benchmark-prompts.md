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

---

## More TYPES of benchmarks (variety palette)

The public world sorts LLM benchmarks into ~8 categories: **Reasoning, Coding, Math, Safety, Multimodal, Agentic, Long-context, Real-world.** For the video, pick a spread across types so it isn't five physics games. Options by type:

### Type A - Physics / games (have plenty)
Hexagon, heptagon, flappy, Suika. Add if you want: **Conway's Game of Life**, **boids flocking**, or a **double pendulum** - all one-file, visual, physics-flavored.

### Type B - Visual / SVG (fast, funny)
- Pelican on a bicycle (above).
- Bonus: *"Generate an SVG of an analog clock showing 10:10 with a sweeping second hand"* or *"Draw an SVG self-portrait of yourself as a robot."*

### Type C - 3D "wow" (three.js)
> Build a 3D solar system in a single self-contained HTML file using three.js from a CDN. The sun at center, planets orbiting at different speeds, camera you can orbit with the mouse. No build step, just open the file.

Great B-roll, big visual payoff, separates models fast.

### Type D - Frontend / UI (your real lane, strong fresh data)
- **Design-to-code from a screenshot** (you already have this as the opener) - this IS a benchmark: **UI Bench** and **DesignBench** both test "replicate a design from a reference screenshot."
- Fresh data to cite:
  - **Startrise Frontend Benchmark** (12 models, same 12 briefs, single-shot, one HTML file each): **Claude Opus 5 scored 82.3, effectively TIED for #1** with Kimi K3 (79.8) - but **Fable 5 won all three open-ended design briefs**. Perfect for the 3-way story.
  - **Design Arena Elo:** Kimi K3 1455, **Fable 5 1373**, GPT-5.6 1372.
- Prompt idea: *"Build a polished pricing page for a SaaS called PostPilot, one self-contained HTML file, three tiers, modern and clean."* (you already have the PostPilot brief.)

### Type E - Reasoning / trick questions (no code, quick cuts)
Instant, funny, shows the "thinking" difference. Source: `cpldcpu/MisguidedAttention`.
- *"How many 'r' letters are in the word strawberry?"* (classic - should be 3)
- *"Alice has 3 brothers and 2 sisters. How many sisters does Alice's brother have?"*
- *"A marble is put in a glass, the glass is turned upside down on a table, then the glass is picked up and put in the microwave. Where is the marble?"*
- *"There are three killers in a room. Someone enters and kills one of them. Nobody leaves. How many killers are in the room?"*

### Type F - Agentic / real code (closest to how you actually use Claude)
- *"Here's a small repo with a failing test. Find the bug and fix it so the test passes."* (this is what **SWE-bench** actually measures - top models >78%.)
- *"Build a CLI todo app in Python with add/list/done commands and passing pytest tests."*
- Tool-use: **BFCL** (function-calling) is the standard here. This type maps directly to your skills, so it's the most "on brand" segment.

### Type G - Math (one quick one)
> A snail climbs 3 feet up a 30-foot well each day and slips back 2 feet each night. How many days to get out?

Or an AIME-style problem for a harder read.

## Recommended spread for the 3-way video (variety, ~6 prompts)
1. **Design-to-code from screenshot** (Type D - your opener, real UI benchmark)
2. **Heptagon 20 balls** (Type A - the rigorous /90 one)
3. **three.js solar system** (Type C - the visual wow)
4. **Your Suika game** (Type A - continuity + feel)
5. **Strawberry + Alice** (Type E - 20-second funny reasoning cut)
6. **Fix-the-bug repo** (Type F - your real lane, agentic)
Score each: runs? -> correctness -> feel -> cost -> time. Run all on Opus 4.8 / Opus 5 / Fable 5.

---

## Sources
- Hexagon: https://github.com/aligeramy/ai-benchmark
- Heptagon (rubric): https://github.com/KCORES/kcores-llm-arena
- Pelican: https://github.com/simonw/pelican-bicycle
- V-GameGym: https://v-gamegym.github.io/index.html
- World of AI Bench: https://www.woaibench.ai/
- Coding benchmarks 2026: https://tolearn.blog/blog/llm-coding-benchmark-comparison-2026
- Startrise frontend benchmark: https://www.startrise.io/blog/llm-frontend-benchmark/
- UI Bench: https://ui-bench.dev/
- Design Arena / best for design: https://modelgrep.com/best/design
- Benchmark categories deep dive: https://medium.com/@srinivasrao.marri/llm-benchmarks-explained-a-technical-deep-dive-into-ai-model-evaluation-a82ea998e759
- Reasoning trick prompts (MisguidedAttention): https://github.com/cpldcpu/MisguidedAttention
- AI agent benchmark compendium: https://github.com/philschmid/ai-agent-benchmark-compendium
