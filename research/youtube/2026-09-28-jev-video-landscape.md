# Jev video landscape, 2026-09-28

Pulled for video 060. Six new transcripts read in full (`transcripts/transcript_<id>.txt`). Earlier references (Isenberg, Theo, Witteveen, Latent Space) are in `youtube/videos/060-jev-claude-code/analysis.md`. Stats from yt-dlp on 2026-09-28.

## What changed since the 09-23 search

The niche moved from "what is Jev" to **"Jev + Claude Code"**. A search for `jev claude code` returns 20 videos. The biggest one, RoboNuggets at 673K in 7 days, puts Claude Code in the title and beats every explainer except Caleb (698K).

| Video | Channel | Views | Comments | Length | Up |
|---|---|---:|---:|---|---|
| [Jev will 10x your Claude Code](https://youtube.com/watch?v=tTnUcSj-QPA) | RoboNuggets | 673,009 | 199 | 11:46 | 09-21 |
| [Building a Harness with Jev](https://youtube.com/watch?v=VE5dsWll06M) | LangChain | 243,585 | 129 | 9:14 | 09-21 |
| [Jev + Claude Code = Cheapest Agentic Coding Loop](https://youtube.com/watch?v=ScvXFi4MUSc) | Ray Amjad | 161,974 | 96 | 27:28 | 09-18 |
| [This NEW Jev + Claude OS…](https://youtube.com/watch?v=EOdXR6lU5ZA) | Chase AI | 109,749 | 50 | 22:16 | 09-25 |
| [Jev Sucks, Actually](https://youtube.com/watch?v=0AR1NvFcP_o) | Duncan Rogoff | 58,350 | **219** | 10:06 | 09-22 |
| [Jev Explained for Python Developers](https://youtube.com/watch?v=JpfLID19QnQ) | Dave Ebbelaar | 40,218 | 42 | 16:50 | 09-21 |

Others in the `jev claude code` results, not transcribed: Simon Scrapes 37:22 (61K), Zubair Trabzada (47K), Ben AI (76K), Rob Shocks (396K, title calls Jev "built for code", which the docs contradict).

## What each one does

### RoboNuggets: "Jev will 10x your Claude Code" (673K)
- **0:00** Cold open: sends a prompt, "that is real time", answer in under 1 s. No code.
- **0:32 to 3:00** Explains 3 shapes, System 1/2, "24x cheaper than Haiku, 230x cheaper than Fable".
- **3:00** Access through **OpenRouter**. Setup is "one prompt away". Starter prompt shown as a screenshot, PDF guide as lead magnet. Community pitch at 4:08.
- **Level 1, agentic OS:**
  - **5:03 Model routing.** 12 prompts, Jev routing vs Fable every time, "70% savings, 9 of 12 never needed the top model". A `/jv on` skill command switches it per session; a file-path lookup gets routed to Haiku.
  - **7:03 Skill finding.** 145 skills as Choice options. 14 tests, "Jev 5 seconds vs Opus 5 about 30 seconds".
- **Level 2 (8:02), business:** a 100-email lead classification race UI with Jev vs Haiku vs Fable columns.
- **Level 3 (9:52), apps:** semantic image search over his media library; the Unclutter Chrome extension (Jev classifies page elements as slop).
- **Technique:** three levels, a visual demo for each, every demo pre-built. No code on screen, no failure shown.

### LangChain: "Building a Harness with Jev" (244K)
- Sydney (open-source PM). Recaps the agent loop, tool calling and structured outputs, then Jev as "System 1".
- **3:27** PII check: LLM plus structured output takes ~5 s, Jev returns "98%" almost immediately.
- **5:35** `langchain-typesafe` integration, `TypeSafeClassifier`.
- **Use cases:** model routing for their internal coding agents (6:04); **auto mode**, a middleware that asks Jev whether a tool call is risky and blocks it (6:47); **Jev as judge** for online evals (7:28).
- **7:02 quote:** she had turned auto mode off because the risk classifier "was too slow for my coding agent to feel productive... it's back on now." **7:18:** "if a tool call... would delete a database or delete important files, Jev would **certainly** classify that as risky."
- **Discrepancy:** her slide puts the quickstart Stripe ticket at "billing 0.84, confidence 0.596". The docs and my live run both say **technical** 0.83 to 0.85. Her criteria may have differed; unverified.

### Ray Amjad: "Cheapest Agentic Coding Loop" (162K)
- **1:50 to 6:30** Live **Playground** tour.
  - Invoice fraud Noul: 85%, reruns vary "2-3%". Adding fraud signals to criteria gives 94%.
  - Lead-quality Score gives 2.91, with his own threshold bands.
  - Log-severity Score: 2.99 for pool exhaustion.
  - A 4-question diff review: addresses task, weakened test, verification strength, risk surface.
- **Factual error at 5:41:** "you can define up to 11 rubrics... a score between 0 and 10". Docs: max **10** levels (0 to 9).
- **8:00 to 12:30** System 1/2 loop: Jev plays Minecraft, GPT-5.6 Astra plans and reviews every 2 min. It runs in the corner for the rest of the video and reaches the Nether by 26:06. This is his retention device.
- **12:46** Skill selection, citing **TypeSafe's Hermes cookbook** (182 skills, 17% to 7.3%). Claims it would cut "about 10,000 tokens" of skill descriptions.
- **15:00** Browser-use flight search (7 s, 0.4 cents); a massively parallel adversarial browser test suite.
- **18:16 Live Claude Code demo:** installs the skill, asks Claude to grade code-comment quality with Jev. Result: "150 comments in 9.3 seconds for about 1 cent", whole codebase estimated at 57 cents, ~1,700 comments to rewrite.
- **19:44** "Qualitative linters". **20:53** Code smells: Claude's plan says 28M tokens, $1.19.
- **22:46** Jev-based code review idea. **25:31** Sentry security-pipeline tweet: "5x cheaper, faster, high accuracy" vs GPT-OSS 120B.
- Cohort pitch 3 times (13:55, 17:13, 23:30).

### Chase AI: "Jev + Claude OS" (110K)
- Jev is **about 3 minutes of 22**. The video is his voice-driven "Claude OS": Obsidian plugin, Whisper plus Kokoro local voice, a skill backbone.
- **7:03** Jev as a three-tier router:
  - Tier 1: no AI at all, open a report or a terminal.
  - Tier 2: Haiku or Luna.
  - Tier 3: headless Claude Code or Codex in a terminal.
- **9:07** 90-second explainer: "92% chance billing", "200x faster and cheaper".
- **Technique:** Jev in the title for packaging, delivered as one component of a larger system he sells (Chase AI Plus).

### Duncan Rogoff: "Jev Sucks, Actually" (58K, 219 comments)
- Contrarian framing, but no measurements. Built entirely from other creators' clips: Isenberg's iPhone explanation, Nate Herk's comments, Matthew Berman's Skittles, RoboNuggets' routing, Melee, self-driving.
- **Real critique at 4:44:** the schema problem. "What if his iPhone was black?" You must enumerate the options, and edge cases grow with them.
- **Verdict at 9:25:** "for most normal people... using the Anthropic or OpenAI models is going to be your best bet... a little bit overrated."
- Highest comment-to-view ratio of the set (0.38%). The contrarian angle drives comments.

### Dave Ebbelaar: "Jev Explained for Python Developers" (40K)
- The only code-first video. Walks his own `ai-cookbook` repo with the Python SDK: a Choice, then Score, Noul and a combined call.
- **10:14 The only measured latency that disagrees with the pitch:** from Europe, "500 600 milliseconds... compare that to Haiku, it's not that much faster."
- **Cost:** 100K requests at 500 tokens, "Jev about $2, Haiku 50 bucks".
- **14:35 Verdict:** early, data privacy for EU clients (a new US vendor), "3 months max" until the big labs copy it, hopes for self-hostable open models.
- Mispronounces it "Jeff" and "null" throughout.

## Patterns across all six

| Demo | Who did it | Count |
|---|---|---:|
| Model routing (cheap vs expensive model) | RoboNuggets, LangChain, Chase | 3 |
| Skill selection from a big skill list | RoboNuggets (145), Ray (cites Hermes cookbook), Duncan (clip) | 3 |
| Tool-call risk gate / auto mode | LangChain (asserted, not shown) | 1 |
| LLM-as-judge replacement | LangChain (said), Ray (diff-review questions) | 2 |
| Real Claude Code session calling Jev on screen | Ray (comment grading) | 1 |
| Side-by-side speed vs an LLM | RoboNuggets (race UI), LangChain (PII), Dave (latency script) | 3 |
| Showed Jev getting something wrong | none | 0 |
| Measured latency from their own desk | Dave (500 to 600 ms, EU) | 1 |
| Used the jaggedness page | none | 0 |

## Openings for 060 (checked against my live runs, `research/typesafe-docs/JEV-STUDY-GUIDE.md`)

1. **The Bash gate is now LangChain's claim, and I can test it.** She says Jev "would certainly classify that as risky" (7:18). My run: `find . -name __pycache__ -exec rm -rf {} +` scores 0.82, and a "# harmless" comment drops a force-push from 0.94 to 0.84. Nobody has shown the gate as a real hook, and nobody has shown it missing.
2. **Zero failures shown across six videos.** Duncan's "sucks" video has opinions but no failing call. A reproduced 1.19 (1.15 live) plus the adversarial comment is the honesty beat nobody has.
3. **Only one creator measured latency, and he's in Europe.** My East Coast numbers (median ~190 ms, 1 vs 20 questions 184 vs 191 ms) fill that gap. The fan-out proof is not in any of these videos.
4. **The LLM judge swap is still unclaimed as code.** LangChain says "Jev as judge" in one slide; the 060 before/after (`evaluate_optimizer.py` → `jev_judge.py`) is not in any of them.
5. **Skill selection is crowded**, three videos. Skip it, or do it only with the Hermes angle since TypeSafe's cookbook uses the Hermes catalog. It would have to be a real run over my own skills; not verified.
6. **Packaging:** "Claude Code" in the title correlates with the biggest number (RoboNuggets 673K). A contrarian title drew the most comments per view. Both fit 060's "where it falls over" beat.
7. **Correctable errors to avoid repeating:** "11 levels / 0 to 10" (Ray; the real max is 10 levels); "built for code" (Rob Shocks title); "replacement for Claude Code" (Chase says "sort of true in certain situations"; the docs say no).
