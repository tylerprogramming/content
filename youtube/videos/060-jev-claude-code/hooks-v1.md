# Hooks, video 060

Three word-for-word 30-second opens. Brain rule (08-19): a working artifact already on screen is the strongest cold open in the pool, and the first sentence carries a number. Face delayed to 0:08. All three obey that.

The two numbers in the hooks (LLM seconds, Jev milliseconds) are placeholders until the side-by-side is recorded with a real key. Say the number the screen shows. Never round in Jev's favor. If the Jev call has not been run, film Hook 3 instead; it works from the before alone.

## Hook 1: artifact on screen, the side-by-side (RECOMMENDED)

Technique: working artifact first, number in sentence one, withheld payoff.

[SHOW: two terminal panes, already run. Left: `evaluate_optimizer.py` output ending in a PASS line and a `real` time. Right: `jev_judge.py` output, the same decision, a probability, a confidence, a `real` time. No face yet.]

> So this is the same decision, made twice. Left side took [N] seconds. Right side took [N] milliseconds. [VERIFY: run once with a real key]
>
> [SHOW: zoom the left pane. The judge prompt, the `Literal["PASS", "NEEDS_IMPROVEMENT", "FAIL"]`, the `json.loads`.]
>
> The left one is code I actually run. It is an LLM grading another LLM's work, in a loop, until it says PASS. Every trip through that loop is a full chat completion.
>
> [SHOW: Tyler on camera, 0:08.]
>
> The right one is Jev. It is a model that cannot write a sentence. You hand it the same code and the same three options, and it hands back a pick and a probability. No JSON, no parsing, and the price on that call is [N]. [VERIFY]
>
> [SHOW: the `usage` block of the Jev response.]
>
> If you build agents with Claude Code, you already have a dozen of these decisions running through a frontier model. Which tool next. Is this command safe. Did this pass. So today we take one of mine, swap it, and then I am going to show you where this thing falls over, because it does. Let's go.

[NOTE: the withheld payoff is the PreToolUse gate at 6:00 and the 1.19 sum at 8:00. Do not name either here.]

## Hook 2: contrast, the loop with no exit

Technique: contrast, villain is the judge call.

[SHOW: `evaluate_optimizer.py` line 121, the `while True:`. Cursor on it.]

> So there are 3 calls in this loop and only 1 of them writes anything. [NOTE: count on camera: generate, evaluate, generate again.]
>
> [SHOW: scroll up to `evaluate`, the `Literal["PASS", "NEEDS_IMPROVEMENT", "FAIL"]`.]
>
> This one picks a word out of three. That is it. And I am paying gpt-5.4-mini a full completion, with a system prompt, with JSON mode, to pick one word out of three. Then I parse the string and hope.
>
> [SHOW: Tyler on camera, 0:08.]
>
> Last week a lab run by one of the InstructGPT authors shipped a model that only does that part. It never generates a token. TypeSafe says 70 to 500 milliseconds a call. That is their number, not mine. So I am going to measure it.
>
> [SHOW: the two terminal panes, both run, the two `real` times.]
>
> Same decision. Same code. Two different bills. And then the part every other Jev video skips: where it is wrong, and what that costs you inside Claude Code. Let's do it.

## Hook 3: bold claim, no key required

Technique: bold claim, then immediately prove a piece of it. Works with the before only.

[SHOW: `grep -rn "Literal\[" ~/dev/ai/mini_projects/agentic_prompts/` output scrolling. Count the hits.]

> So I searched one folder of my own agent code for the word Literal and got [N] hits. [NOTE: count on camera. Snippets file lists router.py line 76 and evaluate_optimizer.py line 109; the real count comes from the grep.]
>
> Every one of those is an if statement I outsourced to a frontier model. A router that picks a key out of a dict. A judge that says PASS or FAIL. A classifier that reads a filename and says meeting or contract.
>
> [SHOW: Tyler on camera, 0:08.]
>
> None of those are writing tasks. And there is now a model that only does that kind of task, for about four cents per million input tokens, with the output free. That is TypeSafe's price, I will show you the page.
>
> [SHOW: docs.typesafe.ai/models, the price row.]
>
> So today we take the judge, swap it for one Jev question, and put the two bills next to each other. Then I install it inside Claude Code as a hook, and then I show you the page in their own docs where it adds 0.72 and 0.47 and gets 1.19. Let's go.

## Which one

| Hook | Strength | Risk |
|---|---|---|
| 1 | Artifact in 2 seconds, two numbers in sentence one, both loops planted | Needs the Jev run recorded first, so it is filmed last |
| 2 | Villain named at line 121, the vendor number labelled in the open | Slower to the artifact (about 18 seconds) |
| 3 | Zero dependency on a key; the grep is real today | Spends the 1.19 beat early; section 7 has less to reveal |

Record 1. Keep 3 as the fallback if the key does not land before the shoot.
