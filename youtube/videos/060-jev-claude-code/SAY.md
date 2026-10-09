# What you say, 060 (teleprompter)

Generated from `script.md` on 2026-09-28: every spoken line, in order. `▶` = what's on screen / what to type. If this and script.md ever disagree, script.md wins.

---

### [0:00] COLD OPEN

▶ uv run show.py inbox

So that is 1,700 of my real emails. Five questions each. 8,490 answers. Two and a half minutes. Nine cents.

▶ cut to Claude Code in `gate-demo`, the "Jev gate: p(destructive)=0.84... Not sure, so you 

And that is the same model sitting in front of Claude Code, stopping it from running `rm -rf`.

▶ face, PIP on from here.

The model is called Jev. Everyone made a video about it this month. So I took the demos from those videos, reran every one on my own data, and I am going to show you the numbers. Including the ones that make it look bad.

---

### [0:30] 1. Why anyone wants this

▶ uv run show.py why

So first, why would you want this at all. Here is a question I ask a model all the time in code. Does this text have personal info in it. Yes or no.

Left is Claude Haiku. 1,738 milliseconds. And look what it gave back. A code fence, then JSON, then a closing fence. My code now has to strip that, parse it, and handle the day it comes back different.

Right is Jev. 241 milliseconds. It gave back one number. 0.99. Nothing to parse.

▶ slide, three lines.

That is the whole pitch. Three things.

Speed. An LLM writes its answer one token at a time. Jev does not write anything. It reads your text once and puts a probability on each answer you allowed.

Cost. It charges for input only. Output is free, because there is no output. 4.2 cents per million tokens. That call cost a fourteenth as much as Haiku's.

And no parsing. It can only answer with options you gave it. So the JSON-cleanup code goes away.

▶ face.

If you have ever written "respond only in JSON" in a prompt, and then written a try/except under it, that is the code Jev replaces. Not Claude. The little decisions around Claude.

---

### [2:00] 2. What it is, in 90 seconds

▶ docs.typesafe.ai/primitives, the table.

You send two things. A state, which is your text or JSON. And questions. There are three kinds.

Choice. Pick one of up to 255 options. Score. Where does this land on a scale you describe, 2 to 10 levels. Noul. Is this true, a number from 0 to 1.

Choice and Score also give you a confidence number. That one matters later.

▶ uv run show.py fanout

And here is the part none of the videos I watched measured. Every question in a request runs at the same time. One question, 184 milliseconds. Twenty questions on the same text, 191. So you stop asking "should I make another call" and just ask everything you might need.

---

### [3:30] 3. Isenberg's inbox, on my inbox

▶ Isenberg thumbnail, 3 seconds. "1,700 emails, 18 cents."

Ryan Vogel ran his inbox on Greg Isenberg's show. 1,700 emails, 18 cents. So I pulled my last 1,700 from Gmail and asked five questions per email in one call. What kind of email. How good a lead. Does it need a reply from me. Is it time-sensitive. Is it automated.

▶ uv run inbox_demo.py --limit 50

That is fifty, live. Here is the full 1,700 from earlier.

▶ uv run show.py inbox

8,490 answers. 157 seconds with 16 running at once. Two million input tokens. At their list price that is 8.6 cents. OpenRouter had billed my key 8.9 cents at that point, test runs included.

Their number was 18 cents. Mine is under half, mostly because I cut every email to 1,500 characters. So that is not Jev being cheaper for me. That is me sending less.

▶ the "Top leads" list.

And this is the part I actually use. Sort by lead score and my sponsorship pitches float up. 49 emails it thinks need a reply from me.

---

### [5:00] 4. The race

▶ RoboNuggets' race UI, 3 seconds.

RoboNuggets raced Jev against Haiku on 100 emails. Same thing, my emails.

▶ uv run show.py race

Jev, 6.3 seconds wall clock. Haiku, 26.9. Jev cost 0.4 of a cent. Haiku, 7.8 cents. So 4.3 times faster, about 20 times cheaper. And they agreed on 74 of 100 labels. I will come back to what that 26 means.

---

### [5:45] 5. The model router

▶ RoboNuggets' router slide, 3 seconds. "70% savings, 9 of 12."

RoboNuggets' best idea was a router. Jev reads your prompt and picks Haiku, Sonnet, or Opus. He tested 12 prompts. I have 200 of my real Claude Code prompts on this Mac, so I used those.

▶ uv run show.py router

133 went to Haiku, 22 to Sonnet, 45 to Opus. 2.8 seconds for all 200. Half a cent.

But read these. "Run chapters on the FINAL version." Haiku. "Update the content repo." Haiku. "Do a sweep again, any gaps between animations." Haiku. In my session every one of those was real work. The prompt is short because the context is long.

So I gave it the last three turns of each session. It changed 32 routes. Those three stayed on Haiku.

▶ face.

So the router is real, and it is cheap. But it is judging the text of your prompt, not the size of the job. For short follow-ups, keep the model you were already on.

---

### [7:00] 6. The skill picker

▶ uv run show.py skills

Quick one. RoboNuggets picked skills from his list. TypeSafe's own cookbook does it with the Hermes skill catalog. I have 115 Hermes skills installed, so, eight requests.

Jev 8 for 8, under 2 seconds total. Haiku 7 for 8, 12.6 seconds. And look at Haiku's miss. The right answer was "none", and it did say none. Then it kept going for a paragraph, so my exact-match check failed. That is the parse tax again. Jev cannot do that. It can only pick from the list.

---

### [7:45] 7. Swapping my own LLM judge

▶ VS Code, `~/dev/ai/mini_projects/agentic_prompts/evaluate_optimizer.py`, lines 38 to 71, t

So this is code I actually run. An evaluator-optimizer loop. One model writes code, another grades it PASS, NEEDS_IMPROVEMENT, or FAIL, and it loops until PASS. The judge is gpt-5.4-mini with a JSON schema. And there is no cap on that loop.

▶ `~/dev/jev-lab/judge_swap.py`, the `JEV_QUESTIONS` block.

Same three outcomes as a Jev Score. Plus two yes/no questions the old judge mashed together: can it return a wrong minimum, and is anything slower than O(1).

I gave both judges the same three stack implementations, five times each.

▶ uv run show.py judge

First one is correct. The LLM said PASS twice and NEEDS_IMPROVEMENT three times. Same code, same prompt. That is why the loop runs forever sometimes. Jev scored it 1.84 to 1.87 out of 2, every time.

Second one has a getMin that is O(n). Both caught it. Jev put 0.98 on "slower than O(1)."

Third one has a real bug. Pop never updates the minimums. The LLM said FAIL three times and NEEDS_IMPROVEMENT twice. Jev scored it around 0.8, and the confidence came back zero. Five times out of five.

▶ face.

And that zero is the useful part. It is Jev saying "I do not know." In the loop, that is my rule: confidence under 0.5, stop and show a human. The old judge never told me it was unsure. It just picked a word.

Cost, per call: LLM about a tenth of a cent and 1.7 seconds. Jev, two thousandths of a cent and 230 milliseconds.

---

### [9:30] 8. Where the design bites

▶ uv run show.py iphone

Ryan Vogel's explainer was an orange iPhone. Five color options, pick one. Orange, 1.0. Duncan Rogoff asked the right question: what if the phone is black.

So I asked. Black phone, same five options. It said blue. 0.82 confidence.

It is not broken. It has to pick one of yours. Add an "other" option and it says other, 1.0. Every Choice you write needs an escape hatch.

▶ uv run show.py short

Sam Witteveen found confidence drops on short inputs. "stripe not working", three words: billing, 0.43. The full ticket: technical, 0.94. Low confidence on short input is it telling you the truth.

---

### [10:30] 9. A Jev gate on Claude Code

▶ LangChain video, 7:18, 5 seconds.

LangChain said Jev "would certainly classify that as risky" for a tool call that deletes files. So I built it. A PreToolUse hook. Every Bash command Claude wants to run goes to Jev first. One question.

▶ `gate-demo/.claude/settings.json`, then `.claude/hooks/jev_gate.py`, the thresholds.

Over 0.9, deny. 0.5 to 0.9, ask me. Under 0.5, allow. The thresholds are the whole policy.

▶ `[LIVE]` Claude Code in `~/dev/jev-lab/gate-demo`. Type:

    ▶ type: list the files in mini_projects, then delete the __pycache__ folders, then delete the mini_projects folder entirely

So the `ls` went through. Both deletes got 0.82 and 0.84. That is "ask", so Claude stopped. And it would not try a third way around my hook. 300 milliseconds a check.

▶ uv run show.py gate

Now here is why the middle band matters. At a single 0.85 line, like I first planned, the `find -exec rm` at 0.82 walks straight through. And look at the last two. A force push is 0.94, blocked. Add a comment, "# harmless: just syncs", and it drops to 0.84. Under the line. The comment talked it down.

So "certainly"? No. It is a good first filter, it is fast enough that you will not notice it, and it needs the ask band.

---

### [12:00] 10. Where it falls over

▶ uv run show.py jagged

I promised the bad parts. TypeSafe's own docs list nine ways it fails. Here is their headline one, rerun. "Is the customer asking for a refund": 0.71. "Asking for something other than a refund": 0.44. Those should add to 1. They add to 1.15. Each answer is calibrated on its own. Do not do math across them.

It does not count well either. Letters in "strawberry": it said 3, which is right, at 0.39 confidence.

▶ uv run show.py health

And the one nobody mentioned. At 9:36 in the morning, ten calls in a row: 13.7 second median, 37 seconds worst, a 503. Their status page said all services online. An hour later: 210 milliseconds. OpenRouter did not help. It sends you to the same servers.

▶ face.

So if it sits in a request path, give it a timeout and a fallback. My hook falls back to "ask me" if Jev does not answer in time.

---

### [13:15] 11. Where it fits

▶ slide, three rows: Code / Jev / LLM.

So here is how I use it. If a regex can decide it, code. If it is fuzzy but the answer is on a list you can write down, Jev. If anything has to be written, Claude.

▶ docs.typesafe.ai/introduction/coding-agents, the quoted line.

And their own docs say it: there is no setting that turns Claude Code into a Jev agent. It sits next to Claude and takes the decisions that never needed a writer.

▶ face.

Everything I ran is in the repo, link below, including the replay script so you can see my numbers without a key. Tell me which decision in your code you would swap first.

▶ end card.
