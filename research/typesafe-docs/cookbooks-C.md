# TypeSafe (Jev) cookbooks, batch C + demos

Sources are the local copies in `pages/`: `cookbooks__consistency_noul_cookbook.md`, `cookbooks__consistency_choice_cookbook.md`, `cookbooks__hierarchical_classification.md`, `cookbooks__autoresearch_feature_discovery.md`, `cookbooks__classification_using_confidence.md`, `demos.md`, `demos__smart-home.md`. All numbers are quoted verbatim from those pages. Every result was measured by TypeSafe in its own cookbook runs. None of them is independent.

---

## Cross-cutting: confidence vs probability, calibration, and "self-consistency"

- **What "self-consistency" means here:** send the *same* state and rubric to the model 15 times (`NUM_SAMPLES = 15`) and check whether each answer "holds still across the repeats." Each run adds a throwaway `uid` field (`f"{sample_index}:{token_hex(4)}"`) to the state or prompt, so every call is a distinct request. The page says: "This setup cannot separate sensitivity to the irrelevant field from variation that would occur on identical requests." This is run-to-run **repeatability**. It is *not* self-consistency in the chain-of-thought majority-vote sense, and it does not measure accuracy.
- **Neither consistency cookbook measures calibration or accuracy.** The choice page says: "These percentages measure repeatability only." It also says: "None of this shows accuracy or superiority: Haiku at temperature 0 had 100% agreement here, with no abstentions." The chart footnote reads: "100% repeatability does not imply correctness. This experiment does not measure accuracy." The uncertainty bands and thresholds are described as "illustrative; it is neither a calibrated guarantee nor an optimized threshold. Set production boundaries from labeled examples and from the cost of incorrect decisions and of review."
- **Probability vs confidence:**
  - The **choice consistency** cookbook gates on the *top returned probability* (≥ 0.60). It says so directly: "This uses the returned probabilities, not the API's separate `confidence` field."
  - The **noul** cookbook gates on the noul value P(true) with an inclusive uncertain band from 0.30 to 0.70.
  - **classification_using_confidence** gates on the separate `confidence` field (≥ 0.9). The page defines it as "high when nearly all the probability landed on one option and low when it spread across several." It explains why it prefers confidence to the winner's probability: "A winner at 0.45 with a runner-up at 0.44, and a winner at 0.45 with the rest of the weight scattered thinly, are different situations, and `confidence` is what separates them."
- **The closest thing to a calibration result** is in classification_using_confidence. The confident half (conf ≥ 0.9) is right 27/30, or 90%. The unsure half is right 12/30, or 40%. This is a selective-accuracy split at one threshold on 60 filings. It is not a reliability curve.

---

## 1. Self-consistency: nouls (`consistency_noul_cookbook`)

**(1) Problem.** In auto-insurance claims triage (pay, deny, or send to a human), sampled probabilities wobble near a decision threshold. The cookbook measures that wobble and routes the uncertain middle band to human review.

**(2) Question setup.**
- 14 `Noul` questions (yes means "the thing we're checking for is true"), all asked in one `system_one` call. Keys: `covered`, `exclusion`, `on_circuit`, `deductible`, `docs_sufficient`, `within_limit`, `within_window`, `reported_timely`, `rental_eligible`, `fraud_flag`, `human_review`, `manual_review`, `line_items_sum`, `subrogation`.
- Example wording: `"covered": "Is the loss covered under the policy's collision coverage?"` and `"fraud_flag": "Are there indicators that warrant a fraud review?"`
- **State:** a JSON claim (policy, claim, adjuster_notes, claim_history) with borderline cases built in:
  - the loss happened at a track-day event, but in the parking lot and stationary, while the policy excludes "track/competitive driving"
  - a rental line item is claimed, but the policy has no rental coverage
  - no police report, although one is required above $2,000 and the claim is $3,250
  - an auto-triage note says "Approved. Pay full amount $3,250" without taking out the deductible
- TypeSafe takes the dict directly. The LLMs get `json.dumps(CLAIM)`.
- **Comparisons:**
  - `claude-haiku-4-5` and `gpt-5.4-mini`, each at t=0, at API-default temperature, and in yes/no mode at t=0 (answers mapped to 1.0/0.0)
  - `gpt-5.5` (reasoning_effort high) and `claude-opus-4-8` (adaptive thinking)
  - TypeSafe `jev-latest`, which resolved to `jev-1.13.0` on all 15 calls, sampled 2026-09-11

```python
@json_cache
def _call_typesafe(sample_index: int, rubric_hash: str, model: str):
    questions = {
        key: Noul(instructions=question) for key, question in QUESTIONS.items()
    }
    started = perf_counter()
    response = typesafe_client.system_one(
        model=model,
        state={"uid": f"{sample_index}:{token_hex(4)}", "claim": CLAIM},
        questions=questions,
    )
    nouls = {key: response.answers[key].noul for key in QUESTIONS}
    return (nouls, response.usage.input_tokens, response.usage.output_tokens,
            perf_counter() - started,
            {"requested_model": model, "response_model": response.model})
```

**(3) Post-processing.**
- Plots every sample as a heatmap: question × condition rows, 15 columns.
- Application rule `noul_decision_with_uncertainty`: `< 0.30` → "no", `> 0.70` → "yes", anything from 0.30 to 0.70 inclusive → "uncertain", which goes to a human. The page stresses this is "application logic over the returned probability: no new question, no second API call."
- The LLM parse path strips haiku's ```json fences. Anything unparseable becomes NaN, "counted but not scored."
- The rubric hash is part of the cache key, so editing the rubric forces fresh samples.

**(4) Reported numbers** (TypeSafe's own run; costs use "historical price assumptions… not verified `jev-latest` prices or current billing amounts"):
- "TypeSafe's mean per-question probability standard deviation is `0.0102`, below all LLM probability conditions here." The local copy has no per-condition std table for the LLMs.
- TypeSafe "`covered` answers span `0.43` to `0.53`, crossing a `0.5` decision threshold". `exclusion` ranges `0.53` to `0.62`. "its other 13 questions stay on one side of that threshold throughout this run."
- Cost and speed per 14-question call (mean of 15 calls):

| condition | time/call | cost/call | speed vs ts | cost vs ts |
|---|---|---|---|---|
| claude-haiku-4-5 t=0 | 1780ms | $0.001798 | 16.0x | 42.2x |
| claude-haiku-4-5 t=default | 1644ms | $0.001798 | 14.8x | 42.2x |
| claude-haiku-4-5 yes/no t=0 | 1485ms | $0.001650 | 13.4x | 38.8x |
| gpt-5.4-mini t=0 | 1405ms | $0.001089 | 12.7x | 25.6x |
| gpt-5.4-mini t=default | 1177ms | $0.001179 | 10.6x | 27.7x |
| gpt-5.4-mini yes/no t=0 | 1113ms | $0.000950 | 10.0x | 22.3x |
| gpt-5.5-reasoning | 11125ms | $0.033157 | 100.2x | 778.9x |
| claude-opus-4-8-reasoning | 13886ms | $0.034275 | 125.0x | 805.1x |
| typesafe_noul | 111ms | $0.000043 | 1.0x | 1.0x |

- Pricing assumptions: TypeSafe `(0.042, 0.00)` $/1M tokens ("Historical TypeSafe rate, as of 2026-08"). LLM prices are "as of 2026-07". LLM calls ran in a 16-worker pool.
- Qualitative: "The factual checks hold steady across most conditions." Among the LLMs, `exclusion`, `rental_eligible`, `fraud_flag`, and `manual_review` "shift across samples or disagree across models", including at temperature 0.

**(5) Transferable lesson.** Don't threshold a noul at 0.5. Add an explicit "uncertain" band and send it to review. It costs nothing extra, because it is plain code over the returned P(true), and it absorbs jitter near 0.5. Batch the whole rubric into one call and pin/record the resolved model version (`response.model`), because aliases move.

**(6) Caveats the page admits.**
- TypeSafe is not deterministic. `covered` crosses 0.5 across runs.
- The review band "has edges of its own… A value near either outer boundary can still move between `uncertain` and yes or no. The model is no more deterministic for it, and an automatic decision that clears the band is not shown to be correct."
- The band is illustrative, not calibrated.
- The uid confound: the setup cannot separate sensitivity to the irrelevant field from true sampling variance.
- It is one claim, 15 repeats, one day.
- Haiku ignores the "ONLY a JSON object" instruction.

**(7) Video demo potential: 3/5.** "Same prompt 15 times" heatmaps are a strong visual, and TypeSafe runs at ~111ms. But it needs TypeSafe, Anthropic, and OpenAI keys plus `cooksafe`, the reasoning arms take 11–14s per call, and the result is repeatability rather than a wow moment. The shipped `json_cache.json` allows an instant replay. For under 2 minutes, trim to TypeSafe vs haiku t=0.

---

## 2. Self-consistency: choices (`consistency_choice_cookbook`)

**(1) Problem.** In content moderation, a wobbling label sends the same post to different enforcement queues. The cookbook measures label flips across repeats and adds an "uncertain" abstention.

**(2) Question setup.**
- 8 `Choice` questions in one call: `category`, `primary_risk`, `target`, `action`, `queue`, `link_handling`, `review_path`, `severity`. Each has instructions and a dict of mutually exclusive labels with descriptions (passed as `criteria`).
- Example: `"action": ("What enforcement action should be taken on this post?", {"Allow": "Leave the post up with no action.", "Warn": ..., "Remove": ..., "Strike": "Remove the post and add a strike to the account.", "Escalate": "Take no automated action; hold for a human decision."})`
- **State:** a JSON post (author with 38-day account and 1 prior strike, context, content text, a discord.gg link, 4 user reports). The post is heated and insulting, with ambiguous threat-like wording ("Keep it up and I'll end your whole channel.").
- **Comparisons:**
  - haiku-4-5 and gpt-5.4-mini in distribution mode at t=0 and at default temperature, plus single-pick mode at t=0
  - gpt-5.5 and opus-4-8 reasoning
  - TypeSafe `jev-latest` → `jev-1.13.0` on all 15 calls, 2026-09-11

```python
questions = {
    key: Choice(instructions=instructions, criteria=choices)
    for key, (instructions, choices) in QUESTIONS.items()
}
response = typesafe_client.system_one(
    model=model,
    state={"uid": f"{rubric_hash}:{sample_index}:{token_hex(4)}", "post": POST},
    questions=questions,
)
distributions = {}
for key, (_instructions, choices) in QUESTIONS.items():
    probabilities = dict(response.answers[key].probabilities)
    distributions[key] = [probabilities.get(label, float("nan")) for label in choices]
```

**(3) Post-processing.**
- `argmax_label` picks the top label, or `None` if any value is missing.
- `choice_decision_with_uncertainty` returns the label if `max(prob) >= MIN_CHOICE_PROBABILITY` (0.60). Otherwise it returns `"uncertain"`. Exactly 0.60 selects the label.
- Metrics:
  - **mean prob std**: std of each label's probability across the 15 repeats, averaged over labels and questions
  - **max prob std**
  - **raw agree**: plurality label share, averaged over the 8 questions
  - **policy agree**: plurality share after abstention, where "uncertain" counts as a decision and parse failures count against it
  - **uncertain / automatic** rates
  - **conflicts**: questions with more than one concrete label across repeats
- Single-pick LLM rows are excluded from the std and agreement metrics, since "their synthetic one-hot vectors cannot measure uncertainty."

**(4) Reported numbers** (TypeSafe's run):
- Headline: "the LLM distribution settings repeat their plurality labels 87.5% to 100% of the time, compared with TypeSafe's 90.8%." "TypeSafe flips on 2 of the 8 questions."
- Probability std:

| condition | mean prob std | max prob std | parse fail | x TypeSafe |
|---|---|---|---|---|
| claude-haiku-4-5 t=0 | 0.0012 | 0.0221 | 0% | 0.12x |
| claude-haiku-4-5 t=default | 0.0516 | 0.3150 | 1% | 5.29x |
| gpt-5.4-mini t=0 | 0.0312 | 0.0905 | 0% | 3.20x |
| gpt-5.4-mini t=default | 0.0543 | 0.2303 | 0% | 5.56x |
| gpt-5.5-reasoning | 0.0305 | 0.1047 | 0% | 3.12x |
| claude-opus-4-8-reasoning | 0.0245 | 0.0693 | 0% | 2.52x |
| typesafe_choice | 0.0098 | 0.0515 | 0% | 1.00x |

- Agreement with abstention:

| condition | raw agree | policy agree | uncertain | automatic | conflicts |
|---|---|---|---|---|---|
| claude-haiku-4-5 t=0 | 100.0% | 100.0% | 0.0% | 100.0% | 0 |
| claude-haiku-4-5 t=default | 87.5% | 86.7% | 0.8% | 98.3% | 2 |
| gpt-5.4-mini t=0 | 99.2% | 87.5% | 12.5% | 87.5% | 0 |
| gpt-5.4-mini t=default | 90.8% | 84.2% | 22.5% | 77.5% | 2 |
| gpt-5.5-reasoning | 90.0% | 93.3% | 30.8% | 69.2% | 1 |
| claude-opus-4-8-reasoning | 92.5% | 94.2% | 33.3% | 66.7% | 0 |
| typesafe_choice | 90.8% | 99.2% | 25.8% | 74.2% | 0 |

- TypeSafe's flips before abstention:
  - `primary_risk`: Harassment 11 times, Violence 4 times
  - `link_handling`: RmLink 8 times, Brigade 7 times
- After the rule, `primary_risk` and `link_handling` are "uncertain" on every repeat. `category` "alternated between Violence and `uncertain`". "No question produced two different concrete TypeSafe labels."
- Stable across conditions: `target` = Person and `severity` = High "across the board".
- Cost and speed per 8-question call:

| condition | time/call | cost/call | speed vs ts | cost vs ts |
|---|---|---|---|---|
| claude-haiku-4-5 t=0 | 3853ms | $0.003498 | 33.8x | 76.1x |
| claude-haiku-4-5 t=default | 3860ms | $0.003494 | 33.8x | 76.0x |
| claude-haiku-4-5 single-pick t=0 | 992ms | $0.001527 | 8.7x | 33.2x |
| gpt-5.4-mini t=0 | 2293ms | $0.002299 | 20.1x | 50.0x |
| gpt-5.4-mini t=default | 1986ms | $0.002164 | 17.4x | 47.1x |
| gpt-5.4-mini single-pick t=0 | 826ms | $0.000936 | 7.2x | 20.3x |
| gpt-5.5-reasoning | 12978ms | $0.041255 | 113.7x | 897.4x |
| claude-opus-4-8-reasoning | 10376ms | $0.028375 | 90.9x | 617.2x |
| typesafe_choice | 114ms | $0.000046 | 1.0x | 1.0x |

**(5) Transferable lesson.** Choice distributions let you abstain: gate on the top probability and send low-margin cases to a human. This turns label flips into a stable "uncertain" route. TypeSafe's policy agreement rose from 90.8% to 99.2% with zero concrete-label conflicts, at the cost of acting automatically on only 74.2% of answers. Report raw agreement, policy agreement, *and* abstention rate together, because a higher abstention rate can buy agreement.

**(6) Caveats the page admits.**
- Haiku at t=0 beats TypeSafe on both std (0.0012 vs 0.0098) and agreement (100%).
- TypeSafe itself flips labels on 2 of 8 questions.
- "This policy does not make the model deterministic… a probability near `0.60` can still move between a concrete label and `uncertain`."
- The threshold is illustrative, not calibrated. Only repeatability is measured, not accuracy.
- It is one post, and the uid confound applies.

**(7) Video demo potential: 3/5.** The colored heatmap of flipping labels, and the gray "uncertain" cells absorbing the flips, is visual and easy to explain. The costs are the same as the noul cookbook: three API keys, slow reasoning arms, and a nuanced message (Haiku t=0 "wins"). Best as a TypeSafe-only "15 reruns → abstain" clip using the shipped cache.

---

## 3. Hierarchical classification (`hierarchical_classification`)

**(1) Problem.** Classify a document to a leaf in a deep taxonomy by walking it top-down with one `Choice` per node. Beam search fixes early greedy mistakes.

**(2) Question setup.**
- Each node is one `Choice`:
  - instructions: `"Which direct child category best matches this document?"`
  - criteria: `{f"c{i}": label}` over the direct children
- The state is the raw document string.
- A single-child node returns `{label: 1.0}` with no API call.
- Settings: `MODEL, BEAM_WIDTH, MAX_DEPTH, EPSILON = "jev-1.12", 3, 12, 1e-9`, and `RetryPolicy(max_retries=5, backoff_initial=1.0, backoff_max=20.0)`.
- Four hierarchies, one test document each:
  - CPC 2026.05 patents: a wooden bird perch abstract
  - Shopify 2026-02 products: a cat window shelf bed
  - MeSH 2026, a DAG expanded into tree-number paths: a Crohn disease clinical abstract
  - the CookSafe repo file tree, from a frozen `codebase_files.txt` snapshot: "find the experimental Python module under x/eugene that implements BM25…"

```python
@json_cache
def choose(state: str, labels: tuple[str, ...]) -> dict[str, float]:
    """Ask one atomic direct-child question and return its distribution."""
    if len(labels) == 1:
        return {labels[0]: 1.0}
    question, keys = child_question(labels)
    response = client.system_one(
        state=state, questions={"child": question}, model=MODEL
    )
    probabilities = response.answers["child"].probabilities
    return {label: probabilities[key] for key, label in keys.items()}

def child_question(labels):
    keys = {f"c{i}": label for i, label in enumerate(labels)}
    question = Choice(
        instructions="Which direct child category best matches this document?",
        criteria=keys,
    )
    return question, keys
```

**(3) Post-processing.**
- **Greedy:** take the argmax child at each level.
- **Beam (K=3):** each round expands every non-leaf beam candidate in parallel (`ThreadPoolExecutor(max_workers=BEAM_WIDTH)`, one `system_one` call per frontier node). Every child is scored with `path_score = product(edge_probabilities) ** (1 / decisions)`, the geometric mean, which is length-normalized so shallow and deep leaves compare fairly. Edge probabilities are floored at EPSILON, and single-child edges don't count as decisions. The top 3 across finished and expanded candidates are kept.
- `separation = top_path_score / second_path_score` is reported "but not used for pruning". Near 1× means ambiguous.
- Suggested alternatives: use `exp(mean(log(probs)))` for trees deeper than about 10 levels to avoid precision loss, and `min(top_prob/second_top_prob)` if you want paths that are decisive at every node.
- Renders an SVG per hierarchy: orange = greedy, green = beam winner, purple = retained, dashed = pruned.
- Note: the prose says the beam "runs as parallel questions." In the code, the parallelism comes from concurrent single-question requests, not multiple questions in one request.

**(4) Reported numbers** (TypeSafe, `jev-1.12`, 4 labeled examples):
- "Beam search matched 4 of 4 expected leaves; greedy search matched 2 of 4. Keeping three paths recovered the expected classification for CPC patents, Shopify products."

| Hierarchy | Expected | Greedy | Beam K=3 |
|---|---|---|---|
| CPC | A01K31/12 Perches for poultry or birds, e.g. roosts | E99Z99/00 Subject matter not otherwise provided for in this section (wrong) | correct |
| Shopify | Cat Window Beds & Perches | Pet Chairs (wrong) | correct |
| MeSH | C06.405.469.432.500 Crohn Disease | correct | correct |
| CookSafe | retrievers.py | correct | correct |

- Node counts and separation ratios appear only in the SVG images, which are not in the local copy.

**(5) Transferable lesson.** Split a huge label space into a tree of small `Choice`s. You get observability ("which nodes your misclassifications occur most in"), testability when the hierarchy changes, and beam search over full probability distributions, which recovers from ambiguous early splits at little extra wall-clock time because the frontier calls run in parallel. This works for taxonomies, file trees, org charts, skills, and moderation policies.

**(6) Caveats.**
- The evidence is 4 hand-picked examples, one per hierarchy. It is not a benchmark.
- Greedy's "one early mistake cannot be recovered."
- MeSH is a DAG and had to be expanded into paths.
- Codebase results depend on the frozen snapshot, because sibling order "is part of the question, not presentation."
- Deep trees need log space.

**(7) Video demo potential: 4/5.** Very visual: an animated or SVG tree with greedy going wrong (bird perch → "E99Z99 not otherwise provided for") and beam finding the right leaf. It is runnable with one key plus `cooksafe`. For a fast demo, use the Shopify `categories.txt` (a small text file) or your own repo's file tree. CPC and MeSH need large zip downloads. `codebase_files.txt` comes from the cookbook repo.

---

## 4. Autoresearch feature discovery (`autoresearch_feature_discovery`)

**(1) Problem.** Predict a wine critic's 80–100 score from a free-text tasting note. An LLM proposes TypeSafe questions, TypeSafe's answers become numeric columns for CatBoost, and the model's errors feed the next round of proposals.

**(2) Question setup.**
- Two question kinds, chosen by the proposer per feature:
  - `intensity` → `Score(instructions=q, criteria=INTENSITY_LEVELS)` on 5 fixed levels: "Not present in this note at all", "Barely present - mentioned once, in passing", "Present at a moderate level", "Present strongly - the note dwells on it", "Dominant - the note is largely about this"
  - `presence` → `Noul(instructions=q, criteria=NoulCriteria(true="The note states this or clearly implies it", false="The note gives no indication of this"))`
- One request per note carries every question proposed that round. The state is the note string.
- The proposer is `claude-sonnet-5` with a JSON-schema output of add/revise/drop actions, capped at `PROPOSALS = 18`.
- The TypeSafe model is `jev-1.12`, run 2026-08-03.
- Data: 2,000 winemag reviews from a pinned HuggingFace CSV (`GroNLP/ik-nlp-22_winemag`), split into `N_DEV, N_TEST = 1200, 800`.
- The baseline "ask for the score" arm is a single `Score` over 10 quality bands ("Faulty or unpleasant…" to "Profound…").

```python
@json_cache
def answer(model: str, note: str, features_json: str) -> dict:
    """One request per note; every question of the round rides it."""
    features = json.loads(features_json)
    response = client.system_one(
        state=note, questions=feature_questions(features), model=model
    )
    raw = {}
    for feature in features:
        got = response.answers[feature["name"]]
        if feature["kind"] == "intensity":
            raw[feature["name"]] = [
                got.probabilities.get(i, 0.0) for i in range(len(INTENSITY_LEVELS))
            ]
        else:
            raw[feature["name"]] = [got.noul]
    return {"raw": raw, ...}
```

**(3) Post-processing.**
- Score answers use `mean_spread` encoding and become two columns: expected level `probabilities @ levels`, and sd `sqrt(E[l²] − mean²)`. A noul becomes one column (P(true)).
- The loop:
  - Adds are kept unless the column's dev std is below `MIN_SPREAD = 0.05`.
  - Revisions and drops are kept only if 5-fold × 3-repeat CatBoost CV RMSE improves (`CHANGE_TOLERANCE = 0.0`). CatBoost settings: 400 iterations, depth 4, lr 0.05.
  - Feedback to the proposer includes the RMSE history, per-feature importance percentage, and column spread, plus the 30 worst and 30 best predicted dev notes with current and previous predictions.
- The direct-score arm maps the expected level to `80 + 20*expected/9`, then applies one dev-measured shift.
- Significance: paired bootstrap (2,000 resamples) of the held-out RMSE change.

**(4) Reported numbers** (TypeSafe's run, scored once on the 800 held-out rows):
- Data: "1200 dev rows, 800 held out; scores run 80-98, mean 88.73, sd 3.17"

| arm | RMSE | spearman |
|---|---|---|
| predict the mean of the dev rows | 3.088 | -0.014 |
| the note as word counts, same CatBoost | 2.466 | 0.605 |
| ask for the score itself, shifted -1.71 | 2.145 | 0.761 |
| 18 questions from round 1, no loop | 1.869 | 0.778 |
| 38 questions after all 5 rounds | 1.772 | 0.799 |

- Dev CV RMSE by round: 1.903 → 1.881 → 1.861 → 1.838 → 1.840. Round 5 gave "the first dev number that did not improve".
- "round 1 -> round 5 on the held-out rows: -0.097 points, 95% CI [-0.147, -0.050]" ("worth 0.10 points").
- Final set: "38 questions the loop kept: 29 score, 9 noul", which gives 67 numeric columns.
- Top importance shares:

| feature | kind | importance |
|---|---|---|
| note_overall_tone_positivity | score | 17.4% |
| savory_food_wine_seriousness | score | 8.7% |
| positive_superlative_language | score | 8.4% |
| single_vineyard_or_prestige_signal | noul | 7.2% |
| descriptive_detail_density | score | 5.7% |
| elegance_finesse_language | score | 5.0% |
| complexity | score | 5.0% |
| aging_potential | score | 5.0% |
| balance_harmony | score | 2.9% |
| drinkability_easiness | score | 2.9% |
| critic_enthusiasm_confidence | score | 2.7% |
| flavor_distinctiveness | score | 2.6% |

- "Most of the gain is in that first call": 1.87 after round 1 vs 1.77 after round 5.

**(5) Transferable lesson.** Use TypeSafe as a *featurizer*. Typed questions turn unstructured text into a tabular feature matrix that a classical supervised model trains on. An LLM-in-the-loop searches over questions, with CV as the arbiter. Adding a question to a request costs no extra request. Encode `Score` answers as expected value plus spread so the answer's uncertainty becomes a feature. The whole pattern is generic: `PROPOSER_TASK` "is the only string that mentions wine."

**(6) Caveats.**
- "All of this is one dataset and one run of the loop."
- The word-count baseline is "CatBoost's own text handling, not a tuned text-regression pipeline."
- The loop adds only 0.10 RMSE over a single proposal.
- Request count scales with rows: "one request per row per round, so 100,000 rows is 100,000 requests a round". Each round here answers all 2,000 rows. "Eight is already enough to hit a rate limit on a shared key."
- A `Score` takes at most 10 levels: "eleven comes back as a server error".
- The `gpt-5.6-luna` proposer branch "was not run".
- Next steps (not done): screening candidate questions, pruning correlated features, embedding baselines, stability across seeds.

**(7) Video demo potential: 2/5.** The idea is compelling ("LLM writes the features, CatBoost learns"), but a live run is 2,000 requests per round × 5 rounds plus Sonnet and CatBoost, far beyond 2 minutes. Only a cache replay of the charts (round curve, feature heatmap) is feasible. Deps: catboost, numpy, matplotlib, anthropic, cooksafe, and the HF CSV.

---

## 5. Classification using confidence (`classification_using_confidence`)

**(1) Problem.** Classify SEC 10-K "Item 1 Business" text into 75 SIC major groups. Use the answer's `confidence` to decide between reporting the group or backing off to its broader division, with no second call.

**(2) Question setup.**
- One `Choice` per document with 75 options: the two-digit major groups. Each option is described by `describe(group)`, which gives the umbrella title plus up to `MAX_NAMED = 8` member industries.
- Instructions: `"Which broad industry does this company operate in? Judge the company's own operations as this filing describes them."`
- **State:** the filing's Item 1 text, 700–2,200 words and 1,438 on average.
- The page says a Choice "works reliably up to roughly 240 options".
- Model `jev-1.12`, run 2026-08-12. `CONFIDENT = 0.9`.
- Taxonomy: "444 industries -> 75 major groups -> 10 divisions", built from the SEC's `sic_codes.tsv` (fetched 2026-08-10).

```python
def questions() -> dict:
    return {"group": Choice(
        instructions=QUESTION,
        criteria={group: describe(group) for group in sorted(GROUPS)},
    )}

@json_cache
def ask(filing_id: str, text: str) -> dict:
    response = client.system_one(state=text, questions=questions(), model=TYPESAFE_MODEL)
    answer = response.answers["group"]
    return {"group": answer.choice, "confidence": answer.confidence,
            "probabilities": dict(answer.probabilities)}

def classify(filing: dict) -> dict:
    answer = ask(filing["id"], filing["text"])
    sure = answer["confidence"] >= CONFIDENT
    return {"level": "group" if sure else "division",
            "label": answer["group"] if sure else division(answer["group"]),
            "confidence": answer["confidence"], "group": answer["group"]}
```

**(3) Post-processing.**
- If confidence ≥ 0.9, report the group. Otherwise map the *same* chosen group to its SIC division (fixed digit ranges, pure code).
- Scoring: a group counts as correct if it equals the gold code's first two digits. A division counts as correct if it equals the gold group's division.

**(4) Reported numbers** (TypeSafe's run on 60 filings):
- "forced to name a group every time 39/60 right"
- "of those, the 30 it was sure about 27/30 right"
- "and the 30 it was not 12/30 right"
- "letting it answer coarsely when unsure 48/60 useful answers"
- Prose: "The confident half is right 90% of the time; the other half, 40%. Reported one level up, that 40% becomes 70%."
- Examples:
  - conf 1.00: groups 28 (chemicals), 63 (life insurance), 49 (electric, gas & sanitary)
  - conf 0.22: 1372167_2013 → division manufacturing, group 38
  - conf 0.23: 1398633_2009 → wholesale trade, group 50
  - conf 0.29: 46653_1999 → services, group 87
- The low-confidence cases have readable reasons. Two are development-stage shells describing businesses they "intend" to start (Nevaeh, Barricode). One sold one of its two segments weeks before filing.

**(5) Transferable lesson — calibration angle.** In this run `confidence` separated reliable answers from unreliable ones: 90% vs 40% accuracy at the 0.9 cut. With a hierarchical label set, a low-confidence fine answer can be cheaply coarsened to its parent instead of dropped or escalated, at one request per document. Use `confidence` (concentration of the distribution) rather than the winner's probability to judge trust. Pass humans only what is still too coarse to act on.

**(6) Caveats.**
- It is 60 filings, and they "were filtered down to filings whose own text supports the code they carry, so the numbers here measure the recipe rather than the state of EDGAR's metadata". Real EDGAR labels are self-reported and go stale.
- A single threshold (0.9) was shown. There is no sweep and no reliability or calibration curve.
- Division-level "useful" is a looser bar than group-level "right".
- A division may be too coarse to act on. That branch is "where you hand it to a person."

**(7) Video demo potential: 4/5.** It is simple and runnable: one call per document, printed confidence, and a live group → division fallback, with a clear bar chart (90%/40% → 70%). It needs only a TypeSafe key plus `cooksafe`. The `sic_codes.tsv` and `filings.jsonl` files come from the cookbook repo, and the cache ships. The easy vs hard examples (utility vs shell startup) make a good story.

---

## 6. Demos index (`demos.md`) and the smart home assistant demo (`demos__smart-home.md`)

`demos.md` lists a single demo, the "Smart Home Assistant Demo — Evaluate user smart home requests with speculative questions and LLM fallback." It also invites users to submit "killer use case[s]."

**(1) Problem.** Route natural-language smart-home requests fast and cheaply, and use an LLM only where text generation is truly needed.

**(2) Question setup.** No code or question definitions are published on the page. It only describes them:
- Each request is evaluated against "a long list of questions, including many that will end up irrelevant", all in one upfront call. This is the **speculative fan-out** pattern (`/patterns/fan-out`).
- Example for "Turn off all of the lights in the house":
  - "What category of request is this?" → smarthome command
  - "What domain is this request targeting?" → whole house
  - "What type of device is this request targeting?" → lights
  - "What action should be taken on the lights?" → turn off
- The last one is a "speculative question," asked before knowing whether the request is about lights.
- One `Noul` asks whether the request contains more than one distinct action.

**(3) Post-processing.**
- Code filters out irrelevant answers after the call.
- If the compound-request Noul is true, an LLM splits the request into atomic commands, and each command is re-evaluated by TypeSafe.
- If TypeSafe classifies the query as general information or conversation, an LLM generates a freeform reply.

**(4) Numbers.** None. The page says qualitatively that sequential gating "ends up being much slower and more expensive than batching all of the questions in to one upfront API call," and that the TypeSafe step "adds negligible latency to the overall system" relative to the LLM.

**(5) Transferable lesson.** Ask everything at once, including speculative, conditional questions, and let code pick the relevant answers. Don't chain dependent calls. Pair System One routing with an LLM only for generation (splitting compound requests, chat fallback).

**(6) Caveats.**
- No metrics.
- The page embeds a video iframe, but the video isn't in the local copy.
- "The full source code will be available on GitHub at release" (a Vite/React SPA), so it is not runnable yet.

**(7) Video demo potential: 4/5.** The concept is ideal for a YouTube short: type a command and watch many typed answers appear at once, with an LLM kicking in only for chat or compound requests. Speed contrast is visual. But the source is not yet released, so a creator would have to rebuild it: a small React or Python app with one `system_one` call of about 10 Choice/Noul questions, plus an OpenAI or Anthropic key for the fallback.
