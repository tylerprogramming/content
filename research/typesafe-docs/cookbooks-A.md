# TypeSafe (Jev) cookbooks: batch A

Sources: local copies in `pages/` of docs.typesafe.ai: `cookbooks.md`, `parallel_questions`, `rerank_typesafe`, `semantic_find`, `autoformat`, `function_calling`, `skill_suggestion`.
Every number below is quoted from those pages. **All results are vendor-measured** (TypeSafe's own notebooks, replayed from a shipped `json_cache.json`) unless noted otherwise. Nothing here was independently reproduced.

Common to every cookbook:
- Model `TYPESAFE_MODEL = "jev-1.12"`.
- `pip install 'cooksafe>=0.2.0,<0.3.0'` (it pulls in `typesafe_sdk`). `cooksafe.JsonCache` replays cached API responses, so most notebooks run without a key. Delete `json_cache.json` to run live.
- Price constant `PRICE = (0.042, 0.00)`, "$ per 1M tokens (input, output); TypeSafe jev-1.12 as of 2026-09" (the rerank page says "as of 2026-08"). Output tokens are free.
- Core call: `client.system_one(state=..., questions={key: Question}, model=...)`. It returns `response.answers[key]` with `.noul`, `.choice`, `.probabilities`, `.confidence` and `.score`, plus `response.usage.input_tokens/output_tokens`.
- Most pages end with a `make_playground_link(...)` share link to console.typesafe.ai/playground.

---

## 0. Index page (`cookbooks.md`)

The page describes cookbooks as "End-to-end recipes that show TypeSafe in real problems". It groups them as follows (level in brackets):
- **Self-consistency:** consistency_noul [Beginner], consistency_choice [Beginner]
- **Batching:** parallel_questions [Beginner]: "batching every question into one TypeSafe call is 12.2x cheaper and 10.0x faster with no change in answers."
- **How-to:** rerank_typesafe [Beginner], semantic_find [Beginner], autoformat [Beginner], function_calling [Intermediate], skill_suggestion [Intermediate], entity_alignment [Beginner], classifying_rag_passages [Intermediate], citation_check [Beginner], llm_guardrails [Intermediate]
- **Extraction:** sde_cascade [Intermediate], date_extraction [Beginner], pre_parsed_value_extraction [Beginner]
- **Classification:** hierarchical_classification [Intermediate], autoresearch_feature_discovery [Advanced], classification_using_confidence [Beginner]

The page tells readers to learn the primitives and "how confidence works" first.

---

## 1. Parallel questions (`cookbooks/parallel_questions`)

**(1) Problem.** One document and N questions: can you send all N in one call without changing the answers?

**(2) Setup.**
- **State:** `{"article": DOCUMENT}`, where DOCUMENT is `{"source": url, "text": ...}`. The text is the Wikipedia GDPR article at pinned revision `1363040264`, "53,777 characters" (the prose rounds this to "~54,000").
- **13 questions:** 8 `Noul`, 2 `Choice` and 3 `Score`.
  - **Nouls** (instructions only, no criteria): e.g. `breach_72h` "Must a personal data breach be reported to the supervisory authority within 72 hours?", `us_federal_law` "Is the GDPR a United States federal law?" and `criminal_penalties`.
  - **Choices:** `instrument_type` has options Regulation/Directive/Treaty/Recommendation, each with a one-line meaning. `max_fine` has options `TwentyM_or_4pct`/`TenM_or_2pct`/`FixedCap`/`NoFines`.
  - **Scores:** criteria are a list of level descriptions from level 0 up. `individual_rights` (4 levels, None→Strong), `penalty_severity` (4 levels, None→Severe) and `compliance_burden` (5 levels, Negligible→Extreme).
- Each strategy runs `RUNS = 5` times: all 13 questions in one call, versus 13 single-question calls.

```python
@json_cache
def ask(keys: tuple[str, ...], run: int):
    started = perf_counter()
    response = client.system_one(
        state={"article": DOCUMENT},
        questions={key: QUESTIONS[key] for key in keys},
        model=TYPESAFE_MODEL,
    )
    values = {}
    for key in keys:
        answer = response.answers[key]
        if isinstance(answer, NoulAnswer):
            values[key] = answer.noul
        elif isinstance(answer, ChoiceAnswer):
            values[key] = max(answer.probabilities.values())
        else:
            values[key] = answer.score / (len(QUESTIONS[key].criteria) - 1)
    return (values, response.usage.input_tokens, response.usage.output_tokens,
            perf_counter() - started)
```

**(3) Post-processing.** Each answer is reduced to one number:
- Noul → p(yes)
- Choice → max prob
- Score → `score / (levels-1)`, a normalized value in 0–1

The code then computes the mean and std dev across the 5 runs for each strategy. Cost is `input_tokens/1e6*0.042 + output_tokens/1e6*0.00`, averaged over runs. Latency for the singles is the **sum** of the 13 calls, which assumes they run sequentially.

**(4) Results (vendor).** Batched vs single, over 5 runs each:

| question | metric | batched mean | single mean | batched std | single std |
|---|---|---|---|---|---|
| breach_72h | p(yes) | 0.804 | 0.814 | 0.0055 | 0.0055 |
| applies_non_eu | p(yes) | 0.990 | 0.990 | 0.0000 | 0.0000 |
| dpo_all_orgs | p(yes) | 0.030 | 0.030 | 0.0000 | 0.0000 |
| pre_ticked_consent | p(yes) | 0.040 | 0.040 | 0.0000 | 0.0000 |
| right_erasure | p(yes) | 0.990 | 0.990 | 0.0000 | 0.0000 |
| data_portability | p(yes) | 0.990 | 0.990 | 0.0000 | 0.0000 |
| us_federal_law | p(yes) | 0.010 | 0.010 | 0.0000 | 0.0000 |
| criminal_penalties | p(yes) | 0.108 | 0.108 | 0.0045 | 0.0084 |
| instrument_type | max prob | 1.000 | 1.000 | 0.0000 | 0.0000 |
| max_fine | max prob | 1.000 | 1.000 | 0.0000 | 0.0000 |
| individual_rights | normalized score | 1.000 | 1.000 | 0.0000 | 0.0000 |
| penalty_severity | normalized score | 1.000 | 1.000 | 0.0000 | 0.0000 |
| compliance_burden | normalized score | 0.750 | 0.750 | 0.0000 | 0.0000 |

Cost and speed:
```
one call, all 13     1   $0.000497   0.27s
13 calls, one each  13   $0.006090   2.71s
batching: 12.2x cheaper, 10.0x faster
```

**(5) Lesson.** Each Jev question is scored independently against the state, so batching has no cross-question contamination. Pack every question into one call: when the document dominates the tokens, the saving approaches N×. (The reranking and skill-suggestion pages point back to this and to the "Speculative Fan-Out" pattern.)

**(6) Caveats admitted.**
- `breach_72h` and `criminal_penalties` show small run-to-run noise. The page says it is "the same size under both batching strategies" and "a property of the question".
- The 10.0x speed figure assumes sequential single calls: "Fire them concurrently and the gap shrinks, but the 13x token cost stays."
- My observation, not the page's: `criminal_penalties` single std (0.0084) is higher than batched (0.0045), and `breach_72h` means differ by 0.010. The page attributes both to noise.

**(7) Video demo potential: 3/5.** The side-by-side "same answers, 12x cheaper" table is easy to explain and needs only `cooksafe` plus a key (the article comes from the Wikipedia API). But the result is a null effect, which is not very visual; it works better as a 20-second beat inside a bigger demo.

---

## 2. Re-ranking (`cookbooks/rerank_typesafe`)

**(1) Problem.** BM25 gets the right legal passage onto a 30-item shortlist but rarely ranks it first. The goal is to re-rank the shortlist with one yes/no score per query–candidate pair.

**(2) Setup.**
- **Data:** CLERC (jhu-clsp/CLERC `teva_train_dir/train_data.jsonl.gz`, streamed via `datasets`). Constants: `N_ROWS = 170` pooled rows → 3,565 passages, `N_QUERIES = 40`, `TOP_K = 30`. BM25 is `bm25s` with English stopwords.
- **Question:** 1 `Noul` per pair.
- **State:** `{"query_excerpt": query, "candidate_passage": candidate}`.
- That makes 40×30 = **1,200 separate calls**, run in `ThreadPoolExecutor(max_workers=12)`.

```python
is_cited_source = Noul(
    instructions=(
        "The query excerpt comes from a US federal court opinion and was written "
        "immediately around a citation to a precedent; the citation itself has been "
        "removed. Could the candidate passage be from that cited precedent — does it "
        "establish the specific legal proposition the query excerpt invokes at its "
        "citation point?"
    ),
    criteria=NoulCriteria(
        true=("The candidate passage states or establishes the specific rule, standard, "
              "holding, or fact pattern that the query excerpt attributes to its removed citation."),
        false=("The candidate passage is merely on a similar topic or doctrine; it does not "
               "supply the specific proposition the query excerpt relies on."),
    ),
)
response = client.system_one(
    state={"query_excerpt": query, "candidate_passage": candidate},
    questions={"is_cited_source": question},
    model=model,
)
```

**(3) Post-processing.** There are no thresholds and no confidence gating. The code just sorts each shortlist by noul, descending: `sorted(candidates[q], key=lambda c: -pair_scores[q][c]["noul"])`. It then reports the share of queries with the gold passage in the top 1, 5 and 10.

**(4) Results (vendor).**
- BM25 alone: gold passage in top 30 for "100% of the 40 queries", at rank 1 only "5% of the time".
- BM25 + TypeSafe re-rank:
  - **Top 1: 5% → 18%**
  - **Top 5: 15% → 35%**
  - **Top 10: 38% → 62%**
- Cost: "1200 TypeSafe calls used 1,536,002 input and 25,200 output tokens, costing $0.0645."
- The only comparison is against BM25. There is no comparison to an embedding re-ranker or cross-encoder.

**(5) Lesson.** A `Noul` with explicit true/false criteria is a ready-made pointwise re-ranker score: "No scoring scale has to be invented". Fast recall first, then noul-scored precision on the shortlist.

**(6) Caveats admitted.**
- "It cannot add a passage that fast search did not select."
- BM25 was kept deliberately simple.
- "This walkthrough asked one question per pair for clarity. A real application would ask several questions about the same pair in one call."
- Corpus note: BM25 selects from the full pooled corpus, not just each row's 20 negatives.
- My observation: n = 40 queries is small, and 62% top-10 still misses more than a third of queries.

**(7) Video demo potential: 3/5.** The before/after bar chart is good. But it needs `bm25s`, `datasets`, `matplotlib`, a CLERC download and 1,200 calls (fine if cached), and legal passages are hard to read on screen. The content is better swapped for a relatable corpus.

---

## 3. Line-by-line search (`cookbooks/semantic_find`)

**(1) Problem.** Given a document and a plain-language question, find the answering line **and** detect when the document has no answer.

**(2) Setup.**
- **State:** the whole document as a string, with each line prefixed by an ID (`L052| You own Your Content...`). It is GitHub's Terms of Service from a pinned gist: 218 lines, "43,980 characters".
- **Questions:** 2 per request.
  - `where`: a `Choice` whose options are all 218 line IDs, with criteria `None`. The query goes in the instructions.
  - `exists`: a `Noul` with criteria.

```python
def where_question(query: str) -> Choice:
    return Choice(
        instructions=f'Which line of the document contains the answer to: "{query}"?',
        criteria={line_id(i): None for i in range(len(LINES))},
    )

def exists_question(query: str) -> Noul:
    return Noul(
        instructions=f'Does any line of the document address or answer: "{query}"?',
        criteria=NoulCriteria(
            true="At least one line of the document states or directly implies the answer",
            false="No line of the document addresses this",
        ),
    )

response = client.system_one(state=state,
    questions={"where": where, "exists": exists}, model=model)
probabilities = response.answers["where"].probabilities
return {"exists": response.answers["exists"].noul,
        "relevance": [probabilities.get(line_id(i), 0.0) for i in range(len(LINES))]}
```

**(3) Post-processing.**
- Lines are ranked by Choice probability.
- `FOUND, ABSENT = 0.7, 0.35  # present answers typically read >=0.9, absent <=0.05`:
  - exists ≥ 0.7 → "answered in this document"
  - exists < 0.35 → "not in this document"
  - otherwise → "partially addressed"
- Relevance is shown as an ASCII bar (`"#" * round(p*12)`).

**(4) Results (vendor, 4 hand-picked queries).**
- "who owns the code I upload?" → exists 0.98, answered. L052 0.95, L046 0.02, L051 0.02, L217 0.01.
- "can GitHub kick me off the platform without warning?" → exists 0.97, answered. L168 0.97, L167 0.03.
- "do I have to take disputes to arbitration?" → **exists 0.14 → not in this document**, yet the top line L205 scores **0.86**.
- "can minors use GitHub with parental permission?" → exists 0.46 → partially addressed. L029 0.90 ("You must be age 13 or older…"), L012 0.07.

There is no benchmark or baseline comparison, only 4 examples.

**(5) Lesson.** Use line IDs as Choice options to turn classification into pointing. Choice probabilities sum to 1, so always pair the Choice with an independent Noul existence check: "The ranking tells you where to look; the `exists` score tells you whether the result answers the question." The same ID-tagging scheme is reused by autoformat.

**(6) Caveats admitted.**
- "A `Choice` question accepts up to 255 options". Longer documents need two passes (pick a window, then rank inside it).
- The thresholds "separate the examples below, but tune them against your own documents before using them in production."

**(7) Video demo potential: 5/5.** It is a single ~100-line script, one request per query, with terminal bar-chart output and only `cooksafe` as a dependency (the cache ships). The arbitration moment ("top line 0.86, but exists 0.14") is a strong on-screen beat, and it's easy to swap in any document up to 255 lines.

---

## 4. Structure recovery / autoformat (`cookbooks/autoformat`)

**(1) Problem.** Rebuild Markdown (headings, lists, code, callouts, quotes) from plain text that was hard-wrapped and stripped of markers, without the model rewriting any words.

**(2) Setup.** The input is a build-migration memo from a pinned gist: 28 non-blank lines. Two sequential requests:
- **Pass 1 (stitch).**
  - **State:** ID-tagged lines (`L013| ...`). Blank lines are kept as gaps in code.
  - **Questions:** one `Noul` per adjacent non-gap pair, **16 questions**.
- **Pass 2 (classify).**
  - **State:** stitched blocks tagged `B000|`.
  - **Questions, per block:**
    - `type_` Choice (heading/paragraph/list_item/quote/code/callout)
    - `hlevel_` Choice (title/section/subsection), only asked if the block is ≤ `HEADING_MAX_CHARS = 90`
    - `step_` Noul (is this an ordered step?)
    - `callout_` Choice (note/tip/warning)
  - That totals **62 questions** for 17 blocks. The companion questions are asked up front to avoid a third round trip.
- Explicit markers and blank lines are read in code and never sent to the model.

```python
def join_question(i: int) -> Noul:
    return Noul(
        instructions=f"Does line {line_id(i)} pick up mid-sentence, continuing a sentence left unfinished at the end of line {line_id(i - 1)}?",
        criteria=NoulCriteria(
            true="The line starts in the middle of a sentence that began on the previous line - the line break tore the sentence apart",
            false="The line begins a new sentence, item, heading, or thought of its own",
        ),
    )
questions = {line_id(i): make(i) for i in range(1, len(LINES)) if not LINES[i]["gap"]}
response = client.system_one(state=tag(LINES, "L"), questions=questions, model=TYPESAFE_MODEL)

TYPE_CRITERIA = {
    "heading": "A short label or title that names the document or the section that follows it - not a full sentence of content",
    "list_item": "One entry in a list of parallel items - an ingredient, a feature, a task, an attendee; reads as one of several sibling entries",
    "code": "Computer code, a shell command, terminal output, or a config snippet meant to be read verbatim",
    "callout": "A warning, tip, or important note that interrupts the flow to flag something the reader must not miss",
    # + paragraph, quote
}
```

**(3) Post-processing.**
- **Merge thresholds depend on punctuation read in code:** `JOIN_AFTER_DANGLING, JOIN_AFTER_TERMINAL = 0.2, 0.5`. The terminal set is `. ! ? : ;` (the regex also includes `…`).
- **Rendering:**
  - Consecutive list items are grouped. A group is numbered if the mean step noul ≥ `STEP_THRESHOLD = 0.5`, otherwise bulleted.
  - Headings map title/section/subsection → `#`/`##`/`###`.
  - Callouts render as `> [!WARNING]`, etc.
  - Only the answers relevant to the winning type are read; the rest are ignored.
- **Suggested UI gate:** flag blocks whose type confidence is < 0.55.

**(4) Results (vendor, one memo).**
- "16 pair questions, one request, 0.32s" → "28 lines -> 17 blocks (11 line breaks healed)".
- "62 questions about 17 blocks, one request, 0.51s".
- **Per-block type confidence:**
  - B000 heading 0.99 (title), B002 heading 0.75, B010 heading 0.96
  - B004 code 1.00
  - B006 paragraph **0.43**
  - Team list items: step 0.15 / 0.16 / 0.12 → bulleted
  - To-do items: step 0.86 / 0.87 / 0.90 → numbered
  - B014 callout 0.65, kind=warning
  - B015 quote 0.99
- **Totals:** "pass 1 16 questions 0.32s / pass 2 62 questions 0.51s / total 10,211 tokens 0.8s $0.0003".
- **Join probabilities:** true continuations score "0.39 and up" (e.g. L002 0.77, L004 0.39). The list item after a colon, L015, scores 0.22.
- **Wording ablation** ("mid-sentence" vs "same paragraph"):
  - L015 0.22 vs 0.77
  - L016 0.11 vs 0.81
  - L017 0.12 vs 0.78
  - L020 0.08 vs 0.88
  - L021 0.05 vs 0.91
  - Result: "blocks after merge: 17 (mid-sentence) vs 12 (same paragraph)".
- **Lowest-confidence block:** "confidence 0.43: paragraph 0.53, list_item 0.24, callout 0.19".
- There is no baseline against an LLM rewrite. The claim is qualitative: "Every word above is from the input."

**(5) Lessons.**
1. The model judges and code renders, so the output is verbatim-safe.
2. "When a judgment call feeds a threshold, the question should name the narrowest fact that decides it."
3. Let cheap code-readable facts (punctuation) choose between thresholds.
4. Ask conditional companion questions speculatively in the same request instead of adding a round trip.

**(6) Caveats and inconsistencies.**
- The first "same paragraph" wording failed: lists collapsed.
- A single join threshold doesn't work, so two are needed.
- B006 is genuinely ambiguous (0.43).
- **The page contradicts itself on cost.** The intro and appendix prose say "$0.0015", but the code output prints "$0.0003". The printed figure matches 0.042 $/M input pricing; $0.0015 looks stale.

**(7) Video demo potential: 5/5.** A mangled plain-text memo turns into rendered Markdown with numbered vs bulleted lists and a WARNING callout, in under 1 second and two calls. It is very visual, the only dependency is `cooksafe` (IPython optional), and the wording ablation (17 vs 12 blocks) is a great second beat.

---

## 5. Function calling (`cookbooks/function_calling`)

**(1) Problem.** Map natural-language trading requests to calls on ordinary typed Python functions, where arguments are closed sets, with a confidence per call.

**(2) Setup.**
- **Functions:** 10 in `trader.py`, over "156,780 one-minute bars" of 6 tickers.
- **Argument detection:** `closed_sets(fn)` reads type hints and classifies args as:
  - **choice** (`Literal`) → Choice
  - **set** (`list[Literal]`) → one Noul per member, e.g. `"Does the user want {} in the comparison?"`
  - **flag** (`bool`) → Noul

  That gives "28 fillable arguments in total". Ints, free text and dates get no question and keep their defaults (e.g. `top_movers.limit` stays 3).
- **`spec.json`** holds, per argument: a `question`, `options` (keys = the exact Literal strings) and a `stated` Noul that decides whether the argument is mentioned at all. There is also a per-function description and a routing Choice `__tool__`: "What is the user asking the trading assistant to do?". The page says "an LLM can write it for you from the signatures."
- **State:** the raw command string. The playground link passes `COMMAND` as the state.
- **Per command:** "54 questions per command" in one request, covering routing plus every function's arguments. Only the chosen function's answers are read.

```python
# spec.json excerpt
"style": {
  "question": "Does the user want a plain line or candles?",
  "stated": "Does the user say how the chart should be drawn, such as a line, candles, or OHLC bars?",
  "options": {
    "line": "a simple line through the closing prices",
    "candles": "a candlestick or OHLC chart, showing each bar's open, high, low and close"
  }
}
# usage
assistant = Dispatcher(SPEC, TOOLS, client)
  __tool__                      choice  What is the user asking the trading assistant to do?
  plot_price.style              choice  Does the user want a plain line or candles?
  plot_price.style?             noul    Does the user say how the chart should be drawn, ...
  compare_returns.symbols.NVDA  noul    Does the user want NVDA in the comparison?
CALLS = {command: assistant(command) for command in COMMANDS}
```
(The actual `system_one` call lives in `dispatch.py`, which is **not shown** on the page.)

**(3) Post-processing.**
- Call `confidence` = "the least certain judgement in the call, rather than the product of all of them, since one wrong argument is enough to spoil the result."
- `call.weakest()` names the lowest argument.
- If the `stated` Noul says the argument isn't mentioned, it is omitted and the function default applies.
- The numeric cutoff for `stated` and the set-membership cutoff are **not given** on the page (they're inside `dispatch.py`).

**(4) Results (vendor, 14 hand-written commands, no accuracy metric).** Selected results:
- "show nvda 1h" → `plot_price(symbol='NVDA', resolution='1h')`, conf 0.78, tool 1.00
- "plot rolling correlation between nvda and spy for the past month" → `rolling_correlation(symbol='NVDA', benchmark='SPY', window='1mo')`, 0.91 / 1.00
- "when during the day does nvda trade the most" → `intraday_pattern(symbol='NVDA')`, **0.53** / 1.00
- "what moved today" → `top_movers(window='1d', direction='gainers')`, 0.90 / 0.90
- "what tickers do you have" → `list_symbols()`, 1.00 / 1.00
- "candles for tesla with a 20 period moving average" → `plot_price(symbol='TSLA', style='candles', moving_average='20')`, 0.69 / 0.97
- "compare nvda amd and msft over the past three months" → `compare_returns(symbols=['NVDA','AMD','MSFT'], window='3mo')`, 0.94 / 1.00
- "worst drawdown for nvda this quarter, and chart it please" → `drawdown(symbol='NVDA', window='3mo', plot=True)`, 0.84 / 0.84
- "show me apple daily with volume" → `plot_price(symbol='AAPL', resolution='1d', include_volume=True)`, 0.75 / 0.85
- "is amd tracking nvidia lately" → `rolling_correlation(symbol='AMD', benchmark='NVDA')`, 0.82 / 0.82

Breakdown for the last one:
- symbol 'AMD' p 0.87 (NVDA 0.13)
- benchmark 'NVDA' p 0.78 (NVDA 0.92, AMD 0.08)
- window omitted p 0.96
- resolution omitted p 0.99
- Weakest argument: benchmark

Other listed results: "how did the market do this week" 0.96/0.99, "how volatile is tsla" 0.96/1.00, "biggest losers today" 0.98/0.98, "spy stats for the last month" 0.88/0.88.

**(5) Lessons.**
- Closed-set arguments become Choice questions, so invalid values are impossible.
- A separate "stated?" Noul prevents confidently hallucinated defaults: "Without it, the choice would have to name some window, and it would have named one confidently."
- Use min-confidence gating per call.
- Write questions about meaning, not keywords ("Avoid naming a question after its parameter").
- Spell out argument roles to disambiguate same-typed args (symbol vs benchmark).

**(6) Caveats.**
- Free-text, numeric and date arguments are not filled; defaults stand.
- No accuracy benchmark, only 14 examples.
- My observation: the "biggest losers today" output lists MSFT +0.67% and AAPL +1.40% as "losers", which is just the bottom-ranked of 6. "what moved today" was routed to `direction='gainers'`, an assumption.

**(7) Video demo potential: 4/5.** Typing a sentence and watching a chart pop up is compelling. But the page hides the substance in `trader.py`, `dispatch.py`, `spec.json` and a 156,780-bar dataset (plus `polars`, `matplotlib`, `numpy`), so you'd need the full repo files. A strong demo if those ship with the cookbook repo.

---

## 6. Skill suggestion (`cookbooks/skill_suggestion`), in extra detail

Note: the catalog is **Nous Research's Hermes** (`NousResearch/hermes-agent`, MIT), not Anthropic's. The *agent under test* is Anthropic's `claude-haiku-4-5-20251001`. The Hermes PREAMBLE quoted on the page ("## Skills (mandatory) … Err on the side of loading …") is verbatim from `agent/prompt_builder.py:build_skills_system_prompt`. It is the same text as the skills block in this Hermes install's system prompt.

**(1) Problem.** Agents choose skills from a truncated one-line index: Hermes cuts descriptions to 60 characters, so they average "54 characters on average, 60 at most". At that width lookalike skills are confused (e.g. `.pptx` *editing* vs *authoring*), and the preamble's "err on the side of loading" causes needless loads. The goal is to pick **at most one** skill per turn with two cheap TypeSafe calls and inject it as a hint.

**(2) Setup.**
- **Roster:** `hermes_roster.json` has "182 skills in 33 categories", with fields `name`, `category`, `description` (index text), `description_full` and `body` (first 1600 chars of SKILL.md). The roster prompt is "16,089 characters".
- **Agent prompt:** IDENTITY + PREAMBLE + `<available_skills>` index + FOOTER, with Anthropic `cache_control: ephemeral` on it. The suggestion is appended **after** the cache breakpoint so prefix caching is preserved.
- **Agent tools:** `skill_view` (verbatim Hermes schema; exact name match needed), `terminal`, `read_file` and `web_search`.
- **Constants:**
  - `SHORTLIST = 3`
  - `EXCERPT_CHARS = 700`
  - `GATE_THRESHOLD = 0.30` ("mean of the three request nouls, below which nothing is suggested")
  - `FITS_THRESHOLD = 0.30` ("a shortlist whose best 'does this fit' noul is under this is dropped")
  - `WORKERS = 8`
- **State for both requests:** `{"request": request, "recent_context": ""}`. **The skills are not in the state.** They go into the Choice **criteria** (option name → description text).

**Request 1, `rank_wide`** (1 Choice over all 182 + 3 gate Nouls):
```python
CHOICE_INSTRUCTIONS = ("Which of these skills, if any, is the right one to load to help with the "
                       "user's latest request?")
GATE_QUESTIONS = {
  "acts_on_user_system": "Is the assistant being asked to act on the user's files, accounts, devices, "
                         "or online services, rather than only to explain or advise?",
  "would_follow_documented_procedure": "Would a careful expert answering this consult a specific documented procedure "
                         "or set of commands, rather than answering from general understanding?",
  "prose_suffices": "Could a knowledgeable generalist fully satisfy this request in prose, with "
                    "no tools, no documentation, and no access to the user's files or accounts?",
}
INVERTED = {"prose_suffices"}
questions = {"which": Choice(instructions=CHOICE_INSTRUCTIONS,
                criteria={skill["name"]: skill["description"] for skill in ROSTER})}
for key, text in GATE_QUESTIONS.items():
    questions[f"gate::{key}"] = Noul(instructions=text)
response = client.system_one(state=build_state(request), questions=questions, model=TYPESAFE_MODEL)
oriented = [(1.0 - v) if k in INVERTED else v for k, v in values.items()]
gate = sum(oriented) / len(oriented)   # suggest nothing if < 0.30
```

**Request 2, `rerank`** (1 Choice over the top 3 + 1 `fits::` Noul per candidate). The criteria are richer: `description_full + " — " + body[:700]`.
```python
RERANK_INSTRUCTIONS = ("Exactly one of these skills is the right one to load for the user's latest "
                       "request. Which one? Read what each actually does, not just its name.")
questions = {"which": Choice(instructions=RERANK_INSTRUCTIONS,
                             criteria=rerank_criteria(names, excerpt))}
for name in names:
    questions[f"fits::{name}"] = Noul(instructions=(
        f"Does the skill '{name}' do the specific thing the user's request asks "
        f"for? It is described as: {BY_NAME[name]['description_full']}"))
```

**(3) Post-processing and decision.**
```python
def suggest(request):
    wide = rank_wide(request)
    if wide["gate"] < GATE_THRESHOLD: return ()
    shortlist = tuple(name for name, _ in wide["ranked"][:SHORTLIST])
    result = rerank(request, shortlist, EXCERPT_CHARS)
    if max(result["fits"].values()) < FITS_THRESHOLD: return ()
    return (result["winner"],)
```
- The Choice winner decides *which* skill. The max `fits` noul decides *whether* to say anything. They can disagree, and the page treats that as intended.
- **Injected block:** `<skill_relevance>Relevant to the current request: {name}. Ignore this if it does not fit what the user actually asked for.</skill_relevance>`.
- When nothing is suggested, the block says "No skill in the roster appears relevant to this request." This is deliberate: it stops the preamble's "err on the side of loading" from going unopposed.
- The "Ignore this" wording is also deliberate: "pushing harder wins compliance on wrong suggestions too."

**(4) Results (vendor, n = 488 requests, agent = claude-haiku-4-5-20251001, jev-1.12, rendered 2026-07-31).**
- **Dataset:**
  - 315 requests are covered by exactly one skill (171 distinct skills), written by "Claude Sonnet 5" from each skill's SKILL.md.
  - 173 uncovered requests: 85 everyday, 42 technical questions no skill serves, and 46 asking for a missing skill (e.g. Mastodon when only X exists).
- **Metrics** (first response only): wrong load = first `skill_view` ≠ gold; a turn with no load counts as a miss. Needless load = any `skill_view` on an uncovered request.
- **Baseline diagnostic:** "of 36 wrong first picks, 10 came from the right skill's own category".

| run | wrong loads | needless loads |
|---|---|---|
| baseline (roster only) | 16.8% | 9.8% |
| TypeSafe suggestion | 7.3% | 4.0% |
| oracle (given right answer) | 2.5% | 1.2% |

- "baseline -> TypeSafe: 2.3x fewer wrong loads, 2.4x fewer needless ones"
- "of 315 covered requests: 37 the suggestion fixed, 7 it broke"

**Demo traces:**
- **Notes.app request.** Gate 0.75, 0.31s. apple-notes 0.990, computer-use 0.010. Rerank keeps apple-notes (fits 0.60 / 0.54 / 0.01, 0.12s).
- **Pitch-deck .pptx request.** Gate 0.76, 0.16s. powerpoint 0.700, pptx-author 0.300, chroma 0.000. Rerank **flips to pptx-author** (0.09s) even though fits = powerpoint 0.73, pptx-author 0.38, chroma 0.02.
- **Mastodon request.** Gate 0.78. xurl 0.550, computer-use 0.140, openhands 0.080. Rerank keeps xurl (fits 0.56 / 0.38 / 0.05), so the system wrongly **suggests xurl** for Mastodon.

**(5) Lesson.** Progressive disclosure for large rosters: a cheap Choice rank over everything (short descriptions) plus an action-oriented gate, then a close look at the top 2–3 with full text plus absolute per-candidate Nouls. "Either step may come back empty-handed." Keep the roster prompt byte-stable for caching, and inject a soft, ignorable hint. Write gate questions about *whether an action is wanted*, not subject matter: a question about subject matter "will not separate *explain what a monad is* from a request that needs a skill". Swap `hermes_roster.json` to reuse it; it only needs `name`, `description`, `description_full` and `body`.

**(6) Caveats admitted.**
- The covered requests were LLM-written from the SKILL.md files, "so the labels are trustworthy and the requests are easier than the ones users send."
- The oracle floor isn't zero.
- The suggestion breaks 7 turns the agent had right: "A confident wrong suggestion is more persuasive than no suggestion at all".
- Mastodon-style near-misses can pass both checks: "The second pass can only reject what the wide ranking hands it".
- One Choice handles 182 options; "a few times larger" needs chunking.
- Editing `suggestion_block` text invalidates the cache and the shipped results.
- Only one agent model was tested, with a single turn and an empty `recent_context`.

**(7) Video demo potential: 5/5 for this channel.** It directly improves the Hermes agent the viewer may already run. The three demo requests (Notes / pptx flip / Mastodon failure) make a sub-2-minute story. The `suggest()` demo needs only `cooksafe` plus `hermes_roster.json`; the full 488×3 Haiku eval needs an Anthropic key and `requests.json`, though the cache replays it. Showing the Mastodon failure honestly makes it more credible.

---

## Cross-cutting patterns (batch A)
- **ID-tag the state, then use Choice to point** (semantic_find, autoformat).
- **Choice for relative ranking plus Noul for absolute existence/fit**, because Choice probabilities always sum to 1 (semantic_find, skill_suggestion).
- **Batch everything into one request.** Answers are independent, so extra questions are nearly free (parallel_questions, autoformat, function_calling with 54 questions and skill_suggestion).
- **The model judges, code acts:** thresholds, rendering and dispatch all live in plain Python.
- **Question wording is the spec.** Name the narrowest decidable fact ("mid-sentence", "act on the user's system").
- **Cheapest demo stack:** `pip install 'cooksafe>=0.2.0,<0.3.0'` plus the shipped `json_cache.json` (replays without a key).
