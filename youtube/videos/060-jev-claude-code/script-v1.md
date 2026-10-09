# Script - 060 - Turn Your LLM Judge Into ONE Jev Call Inside Claude Code

Target: ~11 min, hard ceiling 13. Showcase-led swap: one real decision from `tylerprogramming/ai`, run twice, then a Claude Code hook. Voice: short spoken sentences, "so" openers, hedges, no em dashes, no hype words.
Built live: nothing. The before (`evaluate_optimizer.py`) exists in the repo. The after (`jev_judge.py`) and the hook (`jev_gate.py`) are written before the shoot and run on camera. Detail in `filming-guide.md`.
Markers: [SHOW: ...] = what is on screen. [NOTE: ...] = production / retention note. [VERIFY: ...] = a number that needs a real Jev key before it is said.

Reference: Greg Isenberg with Ryan Vogel, 619,961 views, 28:24. Covered: what Jev is, the email demo, startup ideas. Did NOT cover: any code, any before next to an after, Claude Code at all. That is the hero here.

Retention shape (28-day channel data, 2026-09-23): viewers decide by 3:00. The Jev call returns a decision, with cost and latency next to the LLM version, at 2:45.

---

## [0:00 - 0:45] COLD OPEN

[SHOW: two terminal panes, already run. Left: `evaluate_optimizer.py` output, last lines a PASS and a `real` time. Right: `jev_judge.py` output, a score, a confidence, a `real` time. No face.]

So this is the same decision, made twice. Left side took [N] seconds. Right side took [N] milliseconds. [VERIFY: run once with a real key]

[SHOW: zoom left pane. The evaluator prompt, then `Literal["PASS", "NEEDS_IMPROVEMENT", "FAIL"]`, then `json.loads`.]

The left one is code I actually run. It is an LLM grading another LLM's work, in a loop, until it says PASS. Every trip through that loop is a full chat completion.

[SHOW: Tyler on camera, 0:08. Webcam PIP stays on from here.]

The right one is Jev. It is a model that cannot write a sentence. You hand it the same code and the same three options and it hands back a pick and a probability. No JSON. No parsing. And the price on that one call is [N]. [VERIFY]

[SHOW: the `usage` block of the Jev response, `input_tokens` and `output_tokens`.]

If you build agents with Claude Code, you already have a dozen of these decisions running through a frontier model. Which tool next. Is this command safe. Did this pass.

So today we take one of mine, swap it, and then I am going to show you where this thing falls over. Because it does. Let's go.

[NOTE: no intro card, hard cut. Two open loops planted: "a dozen of these" pays at 6:00, "where it falls over" pays at 8:00.]

---

## [0:45 - 1:45] What Jev is, in 60 seconds

[SHOW: typesafe.ai/blog/introducing-system-one-models-and-jev, the title only. 3 seconds.]

So one sentence on who made it. TypeSafe AI, a lab in San Francisco. The CEO is Diogo Almeida, one of 20 authors on the InstructGPT paper, the RLHF one. They launched Jev on September 15th. That is the whole backstory, we can move on.

[SHOW: docs.typesafe.ai/primitives. The three types.]

Here is what it does. You send it a state. That is any text or JSON. And you send it questions. Three kinds.

[SHOW: three lines appear one at a time, big type on a dark slide.]

Choice. Pick one of up to 255 options.

Score. Place it on an ordered scale, 2 to 10 levels.

Noul. Is this true. You get a probability from 0 to 1.

[SHOW: a response JSON, the docs quickstart one. `choice: technical, probabilities, confidence: 0.78`.]

Every question comes back typed, with the probability of each option and a confidence number. And every question in the request runs at the same time. Ten questions cost about the same latency as one. That is the part that matters for agents.

[SHOW: docs.typesafe.ai/models, the price row.]

Price, from their page: 4.2 cents per million input tokens. Output is free, because there is no output. Latency, from their launch post: 70 to 500 milliseconds. Those are TypeSafe's numbers. I will tell you which ones I could check.

[NOTE: "TypeSafe's numbers" said once here, plainly. The full audit is at 8:00. Do not relitigate it now.]

---

## [1:45 - 2:45] The before: an LLM as the judge

[SHOW: VS Code, `mini_projects/agentic_prompts/evaluate_optimizer.py`. Scroll to line 105.]

So this is the file. It is an evaluator-optimizer loop from my agentic prompts repo. A generator writes code. An evaluator grades it. Loop until the grade is PASS.

[SHOW: cursor on `evaluate`, lines 105 to 113.]

Look at what the evaluator actually returns.

```python
class Evaluation(BaseModel):
    evaluation: Literal["PASS", "NEEDS_IMPROVEMENT", "FAIL"]
    feedback: str

response = JSON_llm(full_prompt, Evaluation)
```

One of three words. That is a Score question with three levels. And to get it, I call gpt-5.4-mini with a system prompt, JSON mode, a schema, then `json.loads` the string and catch the validation error if it comes back wrong.

[SHOW: `helpers/json_llm.py`, the `try` / `except ValidationError`.]

That is the tax. Every structured decision an LLM makes pays it. Generate a string, parse the string, hope.

[SHOW: terminal. Type it.]

```bash
cd ~/dev/ai/mini_projects/agentic_prompts
time uv run evaluate_optimizer.py
```

[NOTE: speed-ramp the wait. Keep the `real` line on screen at the end. Say the number the screen shows, do not round.]

So there it is. [N] seconds, and that is with one pass through the loop. [VERIFY ON CAMERA] The judge call is the slow half of every iteration, and it gives me no confidence at all. It is either right or silently wrong.

[SHOW: line 121, `while True:`. Hold 2 seconds.]

And notice there is no iteration cap. If the judge never says PASS, this runs forever. Keep that in your head, it comes back.

---

## [2:45 - 4:00] The after: the same decision as one Jev question

[SHOW: VS Code, new file `jev_judge.py` next to the old one. Split view.]

So here is the swap. Same task, same generated code, same three levels. The generator stays an LLM, because it writes. The judge becomes one Jev question.

```python
from typesafe_sdk import Score, TypeSafeClient

def evaluate(task: str, generated_content: str):
    with TypeSafeClient() as client:
        response = client.system_one(
            state={"task": task, "code": generated_content},
            questions={
                "grade": Score(
                    instructions="Does this code implement the task correctly, in O(1), with clean style?",
                    criteria=[
                        "Incorrect or does not meet the O(1) requirement",
                        "Correct but has complexity or style issues worth fixing",
                        "Correct, O(1), no further suggestions",
                    ],
                ),
            },
        )
    answer = response.answers["grade"]
    return answer.score, answer.confidence
```

[NOTE: read the three criteria lines out loud slowly. They are the old prompt, rewritten as situations instead of grades. That is the one skill this video teaches. SDK field names are from docs.typesafe.ai/primitives/score as of 09-23; VERIFY the import and `system_one` signature before the shoot.]

Three things changed. There is no prompt telling it to "only output JSON." There is no parse. And I get a confidence back, which the old one never gave me.

[SHOW: terminal, second pane. Type it.]

```bash
export TYPESAFE_API_KEY=...   # off camera
time uv run jev_judge.py
```

[NOTE: KEY OFF CAMERA. Export it before rolling. VERIFY: run once with a real key. If no key by shoot day, see filming guide row 6 for the fallback.]

[SHOW: the response. Score, confidence, usage block. Then the `real` line.]

So. [N] milliseconds. [VERIFY] Score [N], confidence [N]. [VERIFY] And look at the usage block: [N] input tokens, output tokens listed but not billed. At 4.2 cents per million, that call cost [N]. [VERIFY, do the math on camera from the usage block, not from memory]

[SHOW: both `real` lines side by side, big. Hold 3 seconds.]

Same decision. That is the whole video in one frame. Now let me tell you what actually happened, because the speed is not the interesting part.

[NOTE: ~2:55 to 3:10 is the payoff frame. Let it breathe. This is the retention hinge.]

---

## [4:00 - 6:00] What just happened: three question types

[SHOW: Tyler on camera for the first line, then the slide.]

So why is it fast. An LLM makes a decision per token. If it wants to type PASS, that is four decisions, and it cannot start the second until the first is done. Jev makes one decision. It looks at the state, looks at the options, and puts probability on each one, all at once. There is nothing to stream.

[NOTE: this is Ryan Vogel's "typing HELLO" beat at 13:40 of the reference, compressed to 15 seconds. It is the clearest latency explanation in any of the three transcripts. Keep it.]

[SHOW: the docs quickstart response, one call, three answers.]

And that is why one call can carry three questions. Here is the docs example. A support ticket as the state. Three questions: which department, a Choice. How frustrated, a Score. Is it urgent, a Noul. One request, all three come back together.

[SHOW: the three answers highlighted one at a time.]

Choice gives you the pick plus a probability per option plus a confidence. Score gives you a position on your scale, and it can land between two levels, plus a confidence. Noul gives you one number, the probability of yes, and no separate confidence, because the number is the confidence.

[SHOW: back to `jev_judge.py`. Add the threshold lines live.]

Now here is the thing the old loop could not do. The confidence is a real number I can branch on.

```python
score, confidence = evaluate(task, response)

if confidence < 0.6:
    return response, "unsure, send to a human"
if score >= 1.8:
    return response, "pass"
# otherwise loop, with a cap this time
```

[NOTE: count on camera: three branches.]

So now the loop has a stopping rule that is not "the model said the magic word." Under 0.6 confidence, I stop guessing and escalate. Over 1.8 on a 0 to 2 scale, pass. In between, loop, and I can cap it. That `while True` from before is gone.

[SHOW: Tyler on camera.]

Now, one thing to be honest about right here. This is a rule from TypeSafe's own docs, not mine: someone else's 0.6 is not your 0.6. You calibrate the threshold on your own examples. I ran this on [N] examples before filming. [VERIFY ON CAMERA, say the real count, or say "I have not calibrated it yet" if that is true.]

Okay. That is one decision, in one Python file. The bigger question is what this looks like inside Claude Code, where you do not own the loop. That is next.

---

## [6:00 - 8:00] Second example: a Jev gate on Claude Code's Bash tool

[SHOW: Claude Code in the terminal, a session open on `~/dev/ai`.]

So here is a decision Claude Code makes for me all day. Should this shell command run. Right now that is either a permission prompt I click through, or an allowlist I maintain by hand.

[SHOW: `.claude/settings.json`, the hooks block. Type or paste.]

Claude Code has a hook called PreToolUse. It fires before a tool runs. If the hook exits with code 2, the tool is blocked and Claude reads the message. So the whole gate is one hook and one Noul.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "uv run ~/dev/ai/hooks/jev_gate.py" }
        ]
      }
    ]
  }
}
```

[SHOW: `hooks/jev_gate.py`. Scroll slowly, it is short.]

```python
import json, sys
from typesafe_sdk import Noul, TypeSafeClient

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")

with TypeSafeClient() as client:
    response = client.system_one(
        state={"command": command, "cwd": payload.get("cwd", "")},
        questions={
            "destructive": Noul(
                instructions="Would running this shell command delete, overwrite, force-push, or otherwise irreversibly change files or remote state?",
            ),
        },
    )

p = response.answers["destructive"].noul
if p >= 0.85:
    print(f"Blocked by Jev gate: p(destructive)={p:.2f}. Ask the user.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
```

[NOTE: `[to build]`. Not verified on this Mac. Hook stdin fields (`tool_input.command`, `cwd`) are from code.claude.com/docs/en/hooks as of 09-23; confirm before the shoot. The 0.85 threshold is TypeSafe's "before anything irreversible" pattern, said as theirs.]

One question. Is this destructive. And the threshold, 0.85 before anything irreversible, that is the number TypeSafe uses in their own confidence-routing example. I did not make it up, and you should still tune it.

[SHOW: Claude Code. Type the prompt.]

```
list the files in mini_projects and then delete the __pycache__ folders
```

[NOTE: VERIFY ON CAMERA. Expected: the `ls` passes, the `rm -rf` is blocked with the Jev message and Claude asks. If Jev lets the rm through, say so, show the probability it returned, and cut to the honest section early. That is a better video than pretending.]

[SHOW: the block message in Claude Code. Hold.]

So the `ls` went through. The `rm` got stopped, and Claude read the message and asked me. And the gate call took [N] milliseconds. [VERIFY] You would not have noticed it.

[SHOW: TechCrunch article, the Vercel paragraph.]

And this is the one place I have a number that is not TypeSafe's. Vercel replaced their command-safety classifier, which was an OpenAI model, with Jev. Their engineer, Pranit Sharma, told TechCrunch it came back 5 to 18 times faster with better accuracy on their labels. One engineer, one report. But it is the same shape as this hook, and it is independent.

[NOTE: open loop from the cold open closed here: "is this command safe" was the dozen-decisions list.]

---

## [8:00 - 9:30] HONEST LIMITATIONS (do NOT skip, this is the brand)

[SHOW: Tyler on camera. Then the docs jaggedness page.]

Okay. Here is where it falls over, and I promised you this in the first 30 seconds.

[SHOW: docs.typesafe.ai/model-jaggedness/jev-1.13. Scroll to the refund example.]

First, the one that surprised me. This is TypeSafe's own page. One support ticket. Two questions. Is the customer asking for a refund: 0.72. Is the customer asking for something other than a refund: 0.47. Add them up. 1.19. It is not a calculator. The probabilities are calibrated inside one question, not across questions. So do not do math between answers. Keep the arithmetic in your code.

[SHOW: the rest of the list, scroll.]

Same page lists nine of these. It reads literally. It cannot count. Dates confuse it. Junk in the state drops accuracy. And adversarial text can move it, which for a Bash gate means someone can write a command whose comment argues it is safe. Test that before you trust it.

[SHOW: a slide, two columns: "TypeSafe measured" and "someone else measured".]

Second, the numbers. Every headline multiplier, 193 times faster, 444 times cheaper, 70 to 500 milliseconds, is TypeSafe's, measured on workflows TypeSafe wrote, against an average of two frontier models. They say so themselves on the page. The independent numbers I found are smaller and there are three of them. Vercel: 5 to 18 times, one engineer. Bryo AI: Gemini was a bit more accurate, Jev was 10 to 20 times cheaper, one test. Theo ran 100 of his own emails and got 200 milliseconds average, 240 at P95. That is it. That is the whole independent evidence pile, as of the day I filmed this.

[SHOW: the Latent Space interview thumbnail, 3 seconds.]

Third. The training method is called RLCD. There is no paper. The host asked Almeida directly and he said "not yet." The weights are closed, it is hosted only, US only, and the rate limits page says they change without notice. TypeSafe also says plainly that "cannot hallucinate" means it cannot return an option you did not give it. The type is always right. The answer can still be wrong.

[SHOW: Tyler on camera.]

And fourth, mine. [If the key did not arrive:] Every "after" number you saw today I could not run myself. Those were the documented responses, and I said so on screen. [If it did:] Every "after" number you saw was one run on my machine, not a benchmark. Both of those are fine, as long as you know which one you watched.

[NOTE: honesty beat lands at ~9:00. Land it once, clean, then move. This section is what the audience shares.]

---

## [9:30 - 10:30] Where it fits next to Claude Code

[SHOW: a slide, three rows: Code / Jev / LLM.]

So here is how I am thinking about it now. The phrase going around is "code first, Jev second, LLM last," and I think that is right.

If a regex or an allowlist can decide it, use code. If it is fuzzy but the answers are a fixed list, that is Jev. Which tool. Which model. Is this safe. Did this pass. Is this chunk relevant. If it has to write anything, it is still Claude.

[SHOW: docs.typesafe.ai/introduction/coding-agents, the quoted line.]

And their docs say this outright: there is no `model: jev-latest` setting that turns Claude Code into a Jev agent. It is not a replacement. It sits in the loop, next to Claude, and takes the decisions that never needed a writer.

[SHOW: terminal. Type the two commands.]

If you want Claude Code to write the questions for you, TypeSafe ships a plugin. Two commands.

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Then in a session, `/typesafe:typesafe-ai` and a prompt like this one from their docs:

```
Using the TypeSafe skill, explore the project and find opportunities for using intelligent judgement to stand in for complex parsing or other fragile code.
```

[NOTE: VERIFY the plugin installs on this Mac before the shoot; if not, show the docs page and skip the live run. The 6,548-star compaction plugin exists too; mention it in one line and say Theo argued against it at 23:13. Do not demo it.]

One warning from their own docs. Agents are not great at writing Jev questions yet. Put every question and threshold in one file and edit them yourself. That is what I did with the three criteria lines.

---

## [10:30 - 11:00] Recap + CTA

[SHOW: the two `real` lines side by side, one more time.]

So that is it. One judge call, swapped for one Jev question, with a real confidence I can branch on. One Bash gate inside Claude Code, one Noul, one hook. And the honest part: the big numbers are the vendor's, the small numbers are everyone else's, and the docs page with 1.19 on it is the one to read first.

[SHOW: Tyler on camera.]

If you use Claude Code every day, look at your agent for the calls that just pick something. Tell me in the comments which one you would swap first. I read every one. The code from today is in the repo, link below, and the free community is where I post the calibration results once I have run more than one example.

[SHOW: end card.]

---

## Production notes (whole video)

| Item | Target |
|---|---|
| Face in the first 2 minutes | ~25%. Artifact first, face at 0:08, back to screen by 0:20 |
| Webcam PIP | always on from 0:08 |
| New visual, first 30 s | every 5 s (six [SHOW:] markers in the cold open) |
| New visual, after 0:30 | every ~8 s. Sections 3 and 4 have a marker roughly every 2 lines |
| Payoff frame | 2:55 to 3:10, both `real` lines. Hold 3 s, let it breathe |
| Open loop 1 | planted 0:30 ("a dozen of these"), closed 7:45 (Bash gate) |
| Open loop 2 | planted 0:40 ("where it falls over"), closed 8:00 |
| Honesty beat | 8:00 to 9:30, before the verdict, never after |
| Credibility | 1:45 "code I actually run," 4:00 "my agentic prompts repo." No IBM/Chase/Pfizer line needed; the repo is the credential |
| Counts said on camera | 3 ("3 calls in this loop," "three branches," "nine of these"). Each has a [NOTE: count on camera] |
| Every number's source | research `2026-09-23-jev.md` section 5 and 6, snippets file, or the transcript line cited in `analysis.md`. Nothing from memory |
| [VERIFY] count | 8 in the narration. All listed in `filming-guide.md` dry run table with a fallback each |
| Runtime | sections sum to 11:00. Ceiling 13:00. If the Bash gate demo runs long, cut the plugin commands at 10:00 to the docs page only |
