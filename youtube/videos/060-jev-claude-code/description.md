# Description, video 060 (v2)

v1 in `description-v1.md`. Line 1 carries the money, since it cannot go in the title.

---

I ran 1,700 of my own emails through Jev for about 9 cents, raced it against Claude Haiku (4.3x faster, about 20x cheaper, 74/100 agreement), and put it in front of Claude Code as a hook that stops `rm -rf`. Then I show where it breaks.

Jev is TypeSafe AI's new "System One" model. It does not write text. You send it your text and a list of allowed answers, and it returns a probability for each one, typed, with a confidence number. This month every AI channel made a Jev video. I took their demos (Greg Isenberg's inbox, RoboNuggets' model router and race, LangChain's PII check and tool-call guard, Ryan Vogel's iPhone, Sam Witteveen's short inputs) and reran each one on my real data from my desk. I also swapped the LLM judge in my own evaluator-optimizer loop for one Jev call.

What held up: speed and cost at real volume, 20 questions in the same time as 1, and a confidence score that says "I don't know" when it should. What didn't: a black iPhone classified as blue, a router that sends big follow-up prompts to Haiku, a "# harmless" comment that talks a force-push under the block line, 0.71 + 0.44 = 1.15 on their own docs example, and an hour-long slowdown (13.7 s median, 503 errors) while the status page said all services online.

Code and replay script (see every number without a key): [UPDATE: public repo link]
Free community: [UPDATE: Skool link]

Chapters
00:00 1,700 emails and a hook that stops rm -rf
00:30 Why anyone wants a model that can't write
02:00 What Jev is: state, questions, Choice / Score / Noul
03:30 Isenberg's inbox, on my inbox
05:00 The race: Jev vs Claude Haiku
05:45 RoboNuggets' model router, on 200 real prompts
07:00 Picking 1 of 115 skills
07:45 Swapping my own LLM judge
09:30 Where the design bites: the black iPhone
10:30 Jev as a Claude Code PreToolUse hook
12:00 Where it falls over
13:15 Code first, Jev second, LLM last
[UPDATE: timestamps after the edit]

Numbers, and who measured them
All mine unless labelled. Measured 2026-09-28 from New York, jev-1.13, TypeSafe direct and OpenRouter. Latency is from my desk; TypeSafe says about 100 ms, Dave Ebbelaar measured 500 to 600 ms from Europe. Costs are Jev's input tokens at the $0.042/Mtok list price; Haiku and gpt-5.4-mini costs are what OpenRouter billed. Emails were cut to 1,500 characters each, which is most of why 1,700 cost 9 cents here vs 18 in Isenberg's video.

Sources
TypeSafe docs: https://docs.typesafe.ai
Jev failure modes (jev-1.13): https://docs.typesafe.ai/model-jaggedness/jev-1.13
TypeSafe status: https://status.typesafe.ai
Claude Code hooks: https://code.claude.com/docs/en/hooks
OpenRouter Jev: https://openrouter.ai/docs/guides/community/jev
Greg Isenberg with Ryan Vogel: https://youtube.com/watch?v=4mTLpuQpB80
RoboNuggets: https://youtube.com/watch?v=tTnUcSj-QPA
LangChain: https://youtube.com/watch?v=VE5dsWll06M
Sam Witteveen: https://youtube.com/watch?v=X117w2Rark8
Duncan Rogoff: https://youtube.com/watch?v=0AR1NvFcP_o

---

## Before publishing

- [ ] Public repo: copy `~/dev/jev-lab` without `emails.jsonl`, `inbox_results.*` (real senders), `router_results.json` and `router_ctx_results.json` (raw prompts). Ship redacted versions of those files so `show.py` still runs.
- [ ] Replace chapter times after the edit.
- [ ] Pinned comment: "Which decision in your code would you swap first?"
