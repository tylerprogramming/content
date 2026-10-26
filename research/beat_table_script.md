# 🎥 Jev: System One - Beat Table & Script Draft 🎥

**Goal:** Synthesize all research and technical artifacts into a camera-ready beat-table script and visual asset outline for the YouTube video.

**Format:** Beat-by-beat breakdown, prioritizing the *comparison* between Legacy LLM/Agent patterns and the Jev System One model's capabilities.

---

## 🎬 Beat 1: The Overview & The Hook (Narrative Setup)
**(Sources: Research Doc, Sections 1, 2, 5)**

*   **Visual Hook:** Start with the Stripe comparison metric graph (Speed/Cost). Showcase the raw numbers: "329 seconds vs. 70-500 ms."
*   **Narrative:** Introduce Jev (TypeSafe AI's System One model) and founder Diogo Almeida's shift from "chat" to "controlled decisions."
*   **Concept:** Jev doesn't generate text; it generates *probabilities* and *typed values*. It forces the LLM's brain into a decision machine state.
*   **Key Metrics to Display:**
    *   ✅ **Model:** `jev-1.13.0`
    *   ✅ **Input:** `state` (Text/JSON) + `questions` (Choice, Score, Noul).
    *   ✅ **Output:** Typed answers + Calibrated Probabilities/Confidence.
    *   ⚠️ **Crucial Limitation:** Jev cannot generate prose. The final descriptive text (`summary: str`) must still come from a standard LLM call post-Jev decision.

---

## 🔄 Beat 2: The Old Way - The Problem Space (The "Tax" of Text)
**(Source: Snippet 1: `json_llm.py`)**

*   **Title:** The State-of-the-Art LLM Workflow: Parsing the Ambiguity.
*   **Demonstration:** Show the standard `try/except ValidationError` block.
*   **Explanation:** We ask the LLM to output JSON (a string), and we pay an entire API call just to *validate* that string. The logic is scattered: `parse` -> `try` -> `except`.
*   **Visual:** Flowchart showing the overhead: LLM Call -> String Output -> Python Code Block -> Validation/Parsing.
*   **Jev Contrast:** Jev eliminates this failure mode. Since the model is architecturally forced to pick from a closed set of options (e.g., `Choice`), the output *must* conform to the schema, making the "type error" mathematically impossible (TypeSafe's claim).

---

## 🛣️ Beat 3: The Decision Point (The Router/If Statement)
**(Sources: Snippet 2: `router.py` and Snippet 4: `googledrive/main.py`)**

*   **Title:** Moving from General Purpose to Specific Routing.
*   **Demonstration:**
    1.  **Concept A (Snippet 4):** Show the brittle `if/else` on a string comparison (`if self.state.file_type == "meeting":`).
    2.  **Concept B (Snippet 2):** Show using an LLM-as-Router (e.g., `Literal[...]` in a schema). This is better, but still relies on the LLM generating text to fit a constrained schema.
*   **Jev Advantage:** Jev provides a typed, probabilistic route. Instead of checking `if model_output == "meeting"`, you check `if probability(meeting) > 0.9`. This makes the routing decision a quantitative, verifiable step, not a textual guess.

---

## 🔎 Beat 4: The Iterative/Complex Process (The Loop & The Quantify)
**(Sources: Snippet 3: `evaluate_optimizer.py` & Snippet 5: `parallelization.py`)**

*   **Title:** From Guessing to Calibration.
*   **Flow:** The classic "Loop until PASS" pattern.
*   **Visualization:** Show the multi-step loop (Generate -> Eval -> Context Build -> Re-Generate). Emphasize that the `evaluate` step (the judge) is costly, repetitive, and slow.
*   **Jev Solution (Calibration):** Jev compresses the **Judge** step. We don't need the full loop; we just need to ask: "Based on the initial state, what is the probability of a Pass, and what is the confidence interval?" We skip the expensive back-and-forth.
*   **Speed Demo (Snippet 5):** Show 10 separate questions running in an agent loop (10 API calls). Then, show the Jev side-by-side: 10 questions run in **parallel** in one request, with nearly the same latency as the single longest question.

---

## ⚙️ Beat 5: Tying It Together (The Agent Hook)
**(Sources: Snippet 6, Snippet 7, Research Doc, Section 6)**

*   **Title:** Where Jev Lives: The Agent Decision Middleware.
*   **The Core Demo:** This is the most valuable segment. Show the `AutoModeMiddleware` hook.
*   **Scenario:** When an agent/tool call is about to run (e.g., `lookup_member` or any action), Jev intercepts the decision.
*   **The Comparison:**
    *   **Legacy:** The agent calls the tool. The tool fails, or the prompt fails.
    *   **Jev:** The agent first calls Jev, asking: "Should I proceed with tool X right now?" Jev replies with `Noul(X, p=0.95, conf=0.98)`. Only then does the agent proceed.
*   **Takeaway:** Jev makes the *internal decision-making* explicit, measurable, and auditable—it is the safety guardrail for the agent.

---

## 🎨 Beat 6: Conclusion & Full Picture
**(Sources: Research Doc, Sections 9, 10)**

*   **Summary:** Reiterate the stack:
    1.  **Input/Memory:** LLMs are great for consuming and synthesizing raw data (Research doc).
    2.  **Control Layer (The Brain):** Jev is for the structured decision-making, routing, and quantification of *intent*.
    3.  **Output:** LLMs are still needed for the final, narrative prose.
*   **The Call to Action:** Use this process to replace N calls with 1 call, or multi-step logic with one probabilistic query.
*   **Action Items:** Call out the need for a `TYPESAFE_API_KEY` for the "After" demo shots.

*This script structure moves from conceptual problem (Beat 1) to concrete technical examples (Beats 2-5) and concludes with the high-level architectural value proposition (Beat 6).*