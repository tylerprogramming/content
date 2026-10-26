# Hooks, video 058 (OpenAI Agents API on your own Mac)

Three word-for-word opens, about 30 seconds each. Pick one. Do not blend them.

Rules applied from `BRAIN/youtube/brain.md`:
- Cold open admits four openings: a number in sentence one, an insider name, a named villain, or a working artifact already on screen. The 08-19 entry says the artifact is the strongest, and we have one: a file landing on the Mac, written by an agent running in OpenAI's cloud.
- Name a withheld payoff around 0:20 and hold it to the end. Ours is the cost line, side by side with what Tyler already runs for free.
- Never imply Tyler is not a developer. No hype words. No em dashes.

Every claim below is traceable to `research/youtube/2026-09-15-openai-agents.md` or the OpenAI docs linked in `analysis.md`.

---

## Hook 1, artifact first (RECOMMENDED)
*Technique: working artifact on screen before a single claim*

> [no camera yet. Split screen: left, a terminal on the Mac with `codex exec-server` connected. Right, Finder, a folder called `workspace`.]
>
> Watch the folder on the right.
>
> [an `index.md` appears in the folder]
>
> That file just landed on my Mac. The agent that wrote it is not on my Mac. It is running in OpenAI's cloud, on the same harness that runs Codex. The only thing on my machine is one command, and it is the one on the left.
>
> [cut to the OpenAI docs, the line "The environment can be a laptop"]
>
> So OpenAI shipped the Agents API last week, and every video I found runs it inside OpenAI's hosted sandbox. Which is fine. But the docs say the environment can be a laptop, and nobody has done that on camera. That is what we are doing. Three steps.
>
> [camera]
>
> And at the end I will put the cost of this next to the thing I already run on this same Mac for free, because I think that comparison is the whole decision.

Why this one: real artifact inside ten seconds, no warm-up, names the head term and the gap, states the withheld payoff at about 0:25, and every line is something the video actually shows.

---

## Hook 2, the wedge
*Technique: contrast against the tool they already know*

> If you use Claude Code or Codex, you already know what the harness is. It is the loop. It calls the model, runs the tool, compacts the context when it gets long, retries when something fails. The model is one piece of that.
>
> So here is what OpenAI did on September tenth. They took the harness that runs Codex, and they made it an API. You send a task, they run the loop.
>
> [terminal: `codex exec-server` connecting]
>
> And the part I care about is this line right here. Their harness in the cloud, my files on my Mac. No container, no sandbox bill. Just an outbound connection from this terminal.
>
> In the next ten minutes we set that up from nothing. Then I will tell you what it actually costs, and when I would still reach for the agent that already lives on this machine instead.

Use this if the cold open footage is not clean. It carries the same promise with one terminal shot.

---

## Hook 3, name the mistake
*Technique: pattern interrupt, the wrong way first*

> So the first thing I did with OpenAI's new Agents API was the quickstart. Spin up their hosted sandbox, give it a task, watch it go. It worked. And then I looked at the pricing page and saw the container line, and the five minute minimum, and I thought, hang on, I have a computer.
>
> [docs on screen, the self-hosted page]
>
> Turns out there is a mode where you run one command on your own machine and their harness treats it as the environment. Same agent, same loop, your files, no container. It is three steps, and I could not find a single video that does it.
>
> [camera]
>
> So that is this video. We set it up, we give it something real to do in a folder on my Mac, and at the end I show you the cost line next to what I already run here for zero.

Use this if Tyler wants the honest "I tried the default first" story. It is the most him of the three. Keep "hang on, I have a computer" as the line; it is the reframe.
