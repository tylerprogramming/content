# Reels from the Model Benchmark

5 short scripts pulled from the Opus 4.8 vs Opus 5 vs Fable 5 benchmark. Lead with the visual/number, keep talking to voiceover. Priority: 1, 2, 3.

---

## Reel 1 — "The cheapest Claude model won" (the value reveal, flagship)
**Hook:** "I ran the same prompts through three Claude models. The cheapest one won almost every time."
- **Show:** the totals — Opus 4.8 ~$0.84, Opus 5 ~$2.02, Fable 5 ~$3.16 (across 8 prompts).
- Say: same prompt, three models, and the oldest/cheapest was cheapest AND fastest on every build.
- **Payoff:** "Fable costs almost 4x as much. The real question isn't the price, it's whether it actually builds better. That's the next one."

## Reel 2 — "Same prompt, 3 AI models, watch the cost" (build head-to-head)
**Hook:** "I made three AI models build the exact same game. Watch what each one cost."
- **Show:** the three Suika games side by side, then drop the costs: $0.34 / $0.70 / $1.71.
- Say: same brief, same everything, only the model changed.
- **Payoff:** "Same game. One cost five times more than the other. Can you even tell which is which?"

## Reel 3 — "The cheapest model lost the eye test" (the honest twist)
**Hook:** "The cheapest AI model was the fastest and cost the least, every single time. Then I actually played what it built."
- **Show:** all three versions of one game side by side ([pick the one with the clearest gap], playing each on camera).
- Say: on the receipt, Opus 4.8 won on price and speed. But cost and feel are two different things.
- **Payoff:** "The cheap one won the receipt. It did not win the eye test. [WINNER] built the one that actually felt right." (reveal the winner playing)
- **[NEED FROM TYLER]:** which model won the eye test, and on which game — that sets the payoff line.

## Reel 4 — "The newer AI model writes 3x the code" (over-generation)
**Hook:** "Newer doesn't mean better. Sometimes it just means more."
- **Show:** token counts for the same build — Opus 4.8 vs Opus 5 (e.g. solar system: 4,456 vs 19,539 tokens).
- Say: the newer model wrote 3 to 4x the code for the same task, which means 2x the cost and 2x the time.
- **Payoff:** "More code isn't better code. The question is whether it actually runs better." Cut to them side by side.

## Reel 5 — "I built a tool to benchmark every AI model" (the build reel)
**Hook:** "I built a tool that runs any prompt through every AI model and tells me exactly what each one costs."
- **Show:** `/model-bench "build a game" --models opus-4.8,opus-5,fable-5` running, then the results table populating (cost, time, tokens).
- Say: one command, same prompt to every model, runs on my subscription so there's no API bill, and it saves each result to compare.
- **Payoff:** "Now I never guess which model to use. I just check the receipt." (it's just a text file / skill)

---

## Extra pulls if you want more
- **"Do AI models still fail the strawberry test?"** — all three now answer 3 correctly; reasoning is basically solved.
- **"I made 3 AIs rebuild the same website from a screenshot"** — the design-to-code three-tab compare.
- **"The setting that controls your AI bill"** — tie to the effort/right-sizing point (Opus 5 terse on reasoning, verbose on builds).
