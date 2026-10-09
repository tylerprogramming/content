# Jev in one page (for Tyler, before filming 060)

## What Jev is

- A model from TypeSafe AI (released Sep 15). They call it a "System One" model, after Kahneman's fast thinking.
- **It does not write text.** No sentences, no code, no explanations.
- You send it two things:
  - **state**: the thing to judge (an email, a command, a code snippet, a prompt). Text or JSON.
  - **questions**: each question comes with the answers you allow.
- It sends back a probability for each answer you allowed. That's it.
- Three question types:
  - **Choice**: "which of these?" (up to 255 options) → the pick, a probability per option, and a confidence number.
  - **Score**: "where on this scale?" (2 to 10 levels you describe) → a position, which can land between levels, and a confidence number.
  - **Noul**: "is this true?" → one number from 0 to 1.
- It **cannot answer outside your options**. If none fit, it still picks one of yours unless you give it an "other".

## Why it's faster

- An LLM writes its answer one token at a time, and each token waits for the one before it.
- Jev writes nothing. It reads your text once and scores every option in a single pass.
- All questions in one request run at the same time. My test: 1 question in 184 ms, 20 questions in 191 ms.
- **My numbers (healthy API, from New York):** about 200 to 270 ms a call. Haiku doing the same job: about 930 ms to 1.7 s.

## Why it's cheaper

- $0.042 per million input tokens. **Output is free**, because there is no output.
- My 1,700 emails with 5 questions each came to $0.086.
- The same 100-email job cost Jev $0.004 and Haiku $0.078, about 20x less.

## Why it's simpler to build with

- No "respond only in JSON" prompt, no parsing, no try/except when it comes back wrong. My run: Haiku wrapped its JSON in a code fence. Jev returned `0.99`.
- A built-in **confidence** number, so your code can act when it's high and ask a human when it's low. An LLM judge just picks a word, even when it's unsure.
- Your policy is **thresholds in code** (deny ≥ 0.90, ask ≥ 0.50), not prose in a prompt.

## How it helps you (Claude Code / agents)

- It **doesn't replace Claude**. It takes the small decisions around Claude that never needed a writer:
  - **Guard tool calls:** a PreToolUse hook that scores every Bash command. Built and tested: `rm -rf` → ask or deny, `ls` → allow, about 300 ms each.
  - **Judge output:** replaces the LLM judge in an evaluate/optimize loop. It gave stable scores across 5 runs; the LLM flipped between PASS and NEEDS_IMPROVEMENT on the same correct code.
  - **Route:** pick a model, a skill (8/8 on your 115 Hermes skills), or a queue.
  - **Triage at volume:** classify, score and flag thousands of items for cents.
- Rule of thumb: **code first** (if a regex can do it), **Jev second** (fuzzy, but the answer is on a list), **LLM last** (anything that has to be written).

## Where it falls short (in the video, beat 10)

- **It has to pick one of your options.** A black iPhone came back "blue" at 0.82 until I added "other".
- **It judges the text, not the job.** "Run chapters on the FINAL version" got routed to Haiku.
- **Wording can steer it.** A "# harmless" comment dropped a force-push from 0.94 to 0.84.
- **Answers don't add up across questions.** Refund 0.71 + not-refund 0.44 = 1.15. Do math in code.
- **Reliability:** at 9:36 today, 13.7 s median and 503 errors while the status page said all services were online. It was healthy again by 10:25. Use timeouts and a fallback.
