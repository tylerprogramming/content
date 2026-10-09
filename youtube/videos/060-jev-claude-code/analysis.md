# Analysis, video 060: Jev inside Claude Code

Built 2026-09-23 from `research/2026-09-23-jev.md` (10 sections, by @researcher), `~/.hermes/kanban/attachments/t_de3d1cac/jev-code-snippets.md` (8 snippets, by @coder), and three transcripts. No research was redone; the web searches below filled two holes (access path, hook API) only.

## Creator breakdowns

- `research/youtube/creator-breakdowns/2026-09-23-greg-isenberg-jev-is-here.md` (the reference, 15 beats, his rhythm, our openings, beat-for-beat plan)
- `research/youtube/2026-09-28-jev-video-landscape.md` (6 more: RoboNuggets, LangChain, Ray Amjad, Chase AI, Duncan Rogoff, Dave Ebbelaar; what each demos, openings for 060)

## Reference: Greg Isenberg with Ryan Vogel, "Jev is HERE. How to use it"

619,961 views, 28:24, uploaded 2026-09-18. Podcast format: Greg hosts and plays the viewer, Ryan (OpenCode founding team) demos.

### Structure breakdown

| Time | Segment | Purpose |
|---|---|---|
| 0:00-0:45 | "Same guy whose research built ChatGPT," invite-only objection, access promise | hook |
| 0:45-2:23 | Guest contract: simplest explanation, 3-4 use cases | setup |
| 2:23-6:21 | Real inbox, iPhone-color analogy, email table with 4 outputs | demo + teaching |
| 6:21-7:15 | Fear ("10 hours, so expensive") then "18 cents for 1,700 emails" | payoff |
| 7:15-13:40 | Decision vs action, whiteboard, three types, "no internal reasoning" | teaching |
| 13:40-16:15 | Typing HELLO: why one decision beats 26 | teaching |
| 16:15-22:51 | $5 credit, lead scoring, traffic cop, startup ideas | use cases |
| 22:51-23:58 | Bitcoin bot failing on purpose | honesty |
| 23:58-26:19 | Clip finder (17 moments, 3 s), browser-use flight (7.1 s) | demos |
| 26:19-28:24 | Waitlist, Vercel gateway, "dangerously addictive" | CTA |

### What works

- The fear-then-reveal at 6:21-6:53. Thirty seconds of dread, then "oh, it's done, 18 cents." The number lands because the fear was built first.
- One physical object per concept: iPhone for Choice, typing HELLO for latency.
- Real data ("This is my email. I'm not afraid to share it").
- The host restates the three-tier confidence rule in his own words at 20:15, so the viewer hears it twice.
- A failing demo (Bitcoin) before the CTA.

### Weaknesses (our differentiation)

| Weakness | Evidence | What 060 does |
|---|---|---|
| Founder audience, not developers | 0:17, 1:57, 20:48 | Claude Code users who already own the decision code |
| Payoff at 6:49 of 28:24 | 24% of runtime | Before 3:00 |
| Zero code in 28 minutes | whiteboard only | A real file, a real swap, a real hook |
| No before next to the after | 18 cents stated, LLM cost never measured | Two `real` lines side by side |
| "Can't hallucinate" unqualified | 12:12 | Schema-safe, not correct; the 1.19 example |
| Vendor numbers as fact | 19:14 | Every multiplier labelled by who measured it |
| No Claude Code | not mentioned | The second half of the video |
| Access advice stale | 26:23 | OpenRouter and Vercel gateway, no waitlist (09-23) |

### Target audience and assumed level

His: founders and side-hustlers, no code assumed. Ours: developers who use Claude Code daily and have at least one LLM-as-router or LLM-as-judge in production. Assumed: they can read Python and a settings.json.

## Secondary references

| Video | Views | Length | What it adds | What it misses |
|---|---|---|---|---|
| Theo, "Jev is incredible" | 439,867 | 30:29 | Independent latency run: 100 emails, 200 ms avg, 240 ms P95, 38/s (20:43-21:07). RLCD named (7:04). Argues against Jev compaction (23:13) | No Claude Code integration, no before/after code |
| Sam Witteveen, "Ultimate Classification Model?" | 393,531 | 16:18 | Confidence drops with short inputs (9:05). "Can't hallucinate means won't break the schema" (14:11). OpenRouter access, 4.2 cents (5:06) | Toy classification app, no agent context |

## Claims table (from research section 6, reproduced so the script can be checked against it)

| Claim | Number | Who measured | Caveat |
|---|---|---|---|
| Speed | 70 to 500 ms; "40x to 200x" | TypeSafe launch post | vendor, "from our laptops on the West Coast" |
| Homepage headline | 193.6x faster, 444.6x cheaper | TypeSafe workflow evals | vendor; workflows written by TypeSafe; reference is the average of two frontier models; TypeSafe says "higher end of real world gains" |
| Price | $0.042 per Mtok input, output free | TypeSafe docs | vendor; "we can't prove it isn't subsidized" |
| Type errors | 0%, "mathematically impossible" | TypeSafe | schema guaranteed, correctness not |
| Vercel command-safety classifier | 5 to 18x faster, more accurate | Pranit Sharma, Vercel, via TechCrunch | one engineer's report |
| Email classification vs Gemini | Gemini slightly more accurate, Jev 10 to 20x cheaper | Nikhil Mudholkar, Bryo AI, via TechCrunch | one test |
| 100 emails | 200 ms avg, 240 ms P95, 38/s | Theo, transcript 20:55-21:02 | creator run, own inbox |
| 1,700 emails | 18 cents, 4.2M in / 500K out | Ryan Vogel on Isenberg, 6:49-6:58 | creator demo |
| Sum of two Nouls | 0.72 + 0.47 = 1.19 | TypeSafe jaggedness page | vendor's own failure example |
| Jev-Mem on LoCoMo | 0.777, +11% over best baseline | arXiv 2609.23986, UT Dallas | academic, one benchmark |
| Discord | 100,000 | Latent Space host, 3:12 | spoken |
| Ecosystem | 155 projects, 805 call sites | GitHub READMEs | community counts |

Rule used in the script: TypeSafe's numbers are said as "TypeSafe's." Independent numbers are said with the name of who measured them. There are three independent measurements (Vercel, Bryo, Theo) and the script says "three."

## Technical facts used on screen (research section 5, docs fetched 2026-09-23)

| Item | Value |
|---|---|
| Model | jev-1.13.0 (aliases jev-latest) |
| Endpoint | POST https://api.typesafe.ai/v1/systemone |
| Context | 64k total, 32k for state plus longest question |
| Input | text only |
| Question types | Choice (up to 255 options, choice + probabilities + confidence), Score (2 to 10 ordered levels, score + probabilities + confidence, can land between levels), Noul (0 to 1, no confidence field) |
| SDK | `pip install typesafe-sdk`, classes `Choice`, `Score`, `Noul`, `TypeSafeClient`, method `system_one(state=, questions=)` |
| Claude Code plugin | `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`, invoke `/typesafe:typesafe-ai` |
| Documented failure modes | 9: literal reading, math and counting, date comparison, indirection, large irrelevant state, adversarial content, contradictory criteria, structural invariants (1.19), generation |
| Not a coding-agent model | docs: "There is no `model: 'jev-latest'` setting that turns your coding agent into a Jev-powered agent" |

## The before code (from the snippets file)

Chosen for the video: Snippet 3, `mini_projects/agentic_prompts/evaluate_optimizer.py` lines 53-99 (the LLM judge in a loop). Reasons: it is the cleanest Score question in the repo, the `while True` with no cap makes the confidence-threshold beat land, and the task inside it (an O(1) min-stack) is small enough to run on camera.

Confirmed on this Mac 2026-09-23: the file exists at `~/dev/ai/mini_projects/agentic_prompts/evaluate_optimizer.py`, `helpers/json_llm.py` is at lines 10-36 as described, `router.py` `model_routes` has one entry (so the router demo was not used).

Not used, and why: Snippet 2 (router) needs a second route added before it demos anything. Snippet 4 (CrewAI file classifier) needs Google Drive creds. Snippet 7 (churn Score) is a good short but needs the 058 hosted agent running. Snippets 1, 5, 6, 8 are teaching beats, not demos; the script uses 1 (the parse tax) in section 3.

## Holes filled by web search (2026-09-23)

| Hole | Finding | Source |
|---|---|---|
| Is there still a waitlist | Conflicting. learnjev.com and two X threads say the waitlist ended and console.typesafe.ai signup is open; research file says early access; TechCrunch says the API closed to new users at least once. OpenRouter and Vercel AI Gateway serve it with no TypeSafe account | openrouter.ai/docs/guides/community/jev; vercel.com/ai-gateway/models/jev |
| OpenRouter model id and base URL | `typesafe/jev-1.13`, Decisions API at `/api/alpha/decisions`, or point the TypeSafe SDK at `https://openrouter.ai/api` | OpenRouter docs |
| Claude Code hook that blocks a tool | PreToolUse, matcher on tool name, command hook, exit 2 blocks and feeds stderr to Claude | code.claude.com/docs/en/hooks |
| Existing Claude Code + Jev projects | fast-jev-compaction (6,548 stars, function hooks, Theo argues against it), typesafe-ai/skills (official plugin), Jev Model Router (per dev.to survey) | GitHub, dev.to |
| Search demand for "Jev" | 21 videos in 30 days, 10 over 170K views, 9 of 15 titles lead with "Jev." Web tutorials indexed at learnjev.com, DataCamp, Zovi, Julian Goldie, OpenRouter | yt-search pull, web search |
| Independent latency beyond Vercel/Bryo | Theo, 100 emails, 200 ms avg / 240 P95 | transcript_F3YXg7AaKWE.txt 20:55 |

## Update 2026-09-28: live key, verified

Working key in `~/.hermes/.env`. SDK import names and `system_one` signature confirmed (typesafe-sdk 0.7.2). Docs examples reproduced live, and the Bash-gate Noul was tested on 10 commands: the script's own `__pycache__` prompt scores 0.82 and is NOT blocked at 0.85. Full table and decisions: `research/typesafe-docs/JEV-STUDY-GUIDE.md` sections 8 and 9. Scripts: `~/dev/jev-lab/`.

## Unverified (say so on camera or cut)

- ~~Any Jev response. No key on this Mac.~~ (resolved 2026-09-28, see above) Eight [VERIFY] markers in `script.md`, each with a fallback in `filming-guide.md`.
- The `typesafe_sdk` import names and `system_one` signature. From docs as of 09-23; confirm at install.
- Claude Code hook stdin field names (`tool_input.command`, `cwd`). From docs as of 09-23; confirm with the echo test in the filming guide.
- Whether the plugin installs cleanly on this Mac.
- The "waitlist ended" claim. Three secondary sources, no primary. Try the console first.

## Sources

- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://typesafe.ai/blog/bitterest-lesson
- https://docs.typesafe.ai/models
- https://docs.typesafe.ai/primitives
- https://docs.typesafe.ai/primitives/score
- https://docs.typesafe.ai/model-jaggedness/jev-1.13
- https://docs.typesafe.ai/introduction/coding-agents
- https://docs.typesafe.ai/agent-skill
- https://www.businesswire.com/news/home/20260915525333/en/
- https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
- https://www.langchain.com/blog/building-a-harness-with-jev
- https://docs.langchain.com/oss/python/integrations/providers/typesafe
- https://arxiv.org/abs/2203.02155
- https://arxiv.org/abs/2609.23986
- https://github.com/tamaratran/fast-jev-compaction
- https://github.com/typesafe-ai/skills
- https://github.com/browser-use/jev-ultrafast
- https://dev.to/hao_kang_82922526dfe5d934/we-read-100-jev-repositories-the-best-part-was-the-code-around-the-model-call-am3
- https://openrouter.ai/docs/guides/community/jev
- https://openrouter.ai/docs/guides/community/jev-tutorial
- https://vercel.com/ai-gateway/models/jev
- https://vercel.com/changelog/ai-gateway-now-supports-typesafe-clients-and-http-api-for-jev
- https://code.claude.com/docs/en/hooks
- https://learnjev.com/tutorials/first-call
- https://youtube.com/watch?v=4mTLpuQpB80 (Isenberg, reference)
- https://youtube.com/watch?v=F3YXg7AaKWE (Theo)
- https://youtube.com/watch?v=X117w2Rark8 (Witteveen)
- https://youtube.com/watch?v=cFx9Z3ZXca0 (Latent Space)
- `research/2026-09-23-jev.md`, `research/2026-09-23-jev-typesafe.md`, `~/.hermes/kanban/attachments/t_de3d1cac/jev-code-snippets.md`
