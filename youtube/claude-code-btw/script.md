# Video Script: Claude Code /btw — Ask Questions While It Works

---

## [0:00 - 0:25] Hook

> Every time you open a new Claude Code session just to ask a quick question, you're burning ten to twenty thousand tokens for nothing. There's a feature most people don't know about that fixes this completely. It's called /btw, and once you see how it works, you'll never waste tokens on a second session again.

[SHOW: Face to camera, quick energy]
[NOTE: Keep this tight — 25 seconds max. Get to the demo fast.]

---

## [0:25 - 1:00] The Problem

> Here's the situation. You've got Claude Code working on something — building a feature, refactoring a file, whatever. It's in the middle of a task. And you realize you need to ask it something. Maybe you forgot what pattern it used for the auth setup. Maybe you want to change the output format.

> Before /btw, you had two options. Interrupt the task — which kills the flow and wastes everything it was doing. Or open a brand new session, which costs you ten to twenty thousand tokens just to load up. And that new session has zero context about what you were working on. You'd have to re-explain everything.

> Both options suck. /btw fixes this.

[SHOW: Terminal with Claude Code running a task — something visible and active]
[NOTE: Show the pain — maybe briefly show opening a new terminal tab to illustrate the "old way"]

---

## [1:00 - 1:45] What /btw Does

> /btw lets you ask a side question without interrupting the main task. You type /btw, space, then your question. A little overlay pops up with the answer. The main task keeps running above it. When you're done reading, you hit space, enter, or escape to dismiss it.

> Here's what makes it powerful. It has full visibility into your entire conversation. So it knows every file Claude has read, every decision it's made, everything in context. But — and this is important — it's ephemeral. The question and answer never get added to your conversation history. They don't take up context. And it reuses your existing prompt cache, so it costs almost nothing.

[SHOW: Terminal — type /btw followed by a question while a task is running]
[NOTE: Make sure the main task is visibly still running when the overlay appears — this is the key visual]

---

## [1:45 - 2:45] Live Demo

> Let me show you. I've got Claude Code working on building out a component. While it's doing that, I want to ask — what was the name of that utility function it created earlier?

> /btw what's the name of the utility function you created?

> See — it answered instantly. The main task is still going. And when I press space — boom, right back to the main thread. Nothing was interrupted.

> I can also use it to course-correct. Say I realize I want the output in a different format. /btw actually, can you make that a CSV instead of JSON?

> Now here's the thing — this one won't work. And that's because /btw can't actually change anything. It has no tool access. It can't read files, it can't run commands, it can't make edits. It can only answer from what's already in the conversation. So for corrections like that, you'd still need to wait for the task to finish or interrupt it.

[SHOW: Live terminal demo — real task running, real /btw interactions]
[NOTE: Do this live, not faked. Show a real success AND a real limitation. The limitation demo is important — it builds trust.]

---

## [2:45 - 3:30] When to Use What

> So when do you use /btw versus something else? Here's the mental model.

> /btw is for quick questions about stuff Claude already knows. What file did you edit? Why did you choose that approach? What's the status? It's cheap, it's fast, it doesn't interrupt.

> If you need Claude to actually go DO something — read a new file, run a command, make changes — that's not /btw. That's either a new prompt after the task finishes, or a subagent if you need parallel work.

> Think of it this way. /btw sees everything but can't touch anything. A subagent can touch everything but starts with nothing. They're opposites.

[SHOW: Maybe a simple side-by-side comparison on screen or just face to camera]
[NOTE: The "inverse of a subagent" framing is straight from the docs — it's the clearest mental model]

---

## [3:30 - 4:00] Quick Recap + CTA

> So that's /btw. Side questions that cost almost nothing, don't interrupt your task, don't clutter your history, and give you answers from your full context. Just type /btw, space, your question.

> If you found this useful, let me know in the comments. I've got more Claude Code workflow videos coming. I'll see you in the next one.

[SHOW: Face to camera]
[NOTE: Keep the CTA short — no begging for subs. Just clean and confident.]
