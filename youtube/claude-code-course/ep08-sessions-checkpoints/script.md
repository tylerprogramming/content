# Episode 8 — Sessions & Checkpoints
## Claude Code Tutorial #8 - Sessions & Checkpoints

**Target length:** 12 minutes
**Audience:** Non-technical founders, beginners
**Tone:** Conversational, practical, fast-paced

---

### INTRO (0:00 - 1:30) ~1.5 min

Have you ever been working with Claude Code, things are going great, and then it makes a change that breaks everything? And you're sitting there thinking — how do I get back to where things worked?

[SHOW: Terminal with a broken app — error messages, something clearly wrong]

That's exactly what checkpoints solve. Claude Code automatically snapshots your project before every single edit. And with one command, you can rewind to any point in history.

[SHOW: Quick flash of /rewind command — code restored, app working]

Today I'm covering two features. Sessions — so you never lose your conversation. And checkpoints — so you never lose your code. By the end of this video, you'll feel completely safe experimenting with Claude Code. Because you can always go back.

[NOTE: Title card — "Claude Code Tutorial #8 - Sessions & Checkpoints"]

This is part of a free Claude Code course. Links in the description. Let's go.

---

### SESSIONS: THE BASICS (1:30 - 3:00) ~1.5 min

Let's start with sessions.

Every time you open Claude Code and start working, that's a session. Your conversation, the files Claude read, the changes it made — all of that is saved automatically.

[SHOW: Terminal with Claude Code — a normal working session]

You don't need to do anything. There's no save button. It just happens.

So when you close Claude Code — maybe you shut your laptop, maybe you close the terminal — your session is saved. Your work isn't gone.

[SHOW: Close the terminal window]

The question is: how do you get back to it?

---

### RESUMING SESSIONS (3:00 - 5:00) ~2 min

There are two ways to resume a session.

Option one. If you want your most recent session — the last one you were working on — you type:

[SHOW: Terminal — type the command]

```
claude --continue
```

[SHOW: Claude Code opens with the previous conversation intact]

Boom. You're right back where you were. Same conversation. Same context. Claude remembers everything.

Option two. If you want to pick from a list of past sessions, you type:

[SHOW: Terminal — type the command]

```
claude --resume
```

[SHOW: A list of past sessions appears with dates and previews]

This shows you all your recent sessions. You can scroll through them, see when they happened, and pick the one you want.

[SHOW: Select a session from the list — Claude opens with that session's conversation]

This is great when you were working on multiple things. Maybe you had a session where you were building a feature on Monday, and a different session for a bug fix on Tuesday. You can jump back to either one.

Now here's a pro tip. Name your sessions so they're easy to find. While you're in a session, type:

[SHOW: In Claude Code, type:]

```
/rename adding dark mode feature
```

[SHOW: Session gets renamed — show it appearing with the new name in the resume list]

Now when you do `claude --resume`, that session shows up with a clear name instead of just a timestamp. Way easier to find.

[NOTE: Show the --resume list again with the renamed session visible]

---

### CHECKPOINTS: WHAT THEY ARE (5:00 - 6:30) ~1.5 min

Okay. Sessions save your conversation. But what about your code?

That's where checkpoints come in. And this is the feature that makes Claude Code feel safe.

[SHOW: Terminal with Claude Code]

Every time Claude edits a file — every single time — Claude Code automatically takes a snapshot of your project. Before the edit. This is called a checkpoint.

You don't set this up. You don't turn it on. It just happens. Every edit, a snapshot.

[SHOW: Claude making several edits to files — each one quietly creating a checkpoint]

Think of it like automatic save points in a video game. You're exploring, making progress, and the game keeps saving your state. If you die, you go back to the last save point.

Same idea. If Claude makes a change that breaks things? You go back to a checkpoint.

[NOTE: The video game analogy works well for this audience. Lean into it.]

---

### DEMO: USING /REWIND (6:30 - 9:00) ~2.5 min

Let me show you this in action. I've got a simple app here that's working fine.

[SHOW: Browser showing a working app — maybe the dark mode app from episode 7]

I'm going to ask Claude to make a change. And I'm going to intentionally let it break something.

[SHOW: In Claude Code, type:]

```
Refactor the entire CSS to use a new naming convention and reorganize all the files
```

[SHOW: Claude makes a bunch of changes — files being edited, restructured]

Okay. It made a lot of changes. Let me check the app.

[SHOW: Switch to browser — the app is broken. Styles are messed up, things are misaligned or missing]

Yep. It's broken. The old me would be panicking right now. But watch this.

[SHOW: Back in Claude Code, type:]

```
/rewind
```

[SHOW: A list of checkpoints appears — timestamped snapshots of different points in the conversation]

See this? Every checkpoint. Every edit Claude made. I can see exactly what happened at each point.

I want to go back to before that big refactor. So I'll select this checkpoint — right before it started.

[SHOW: Select the checkpoint from before the refactor]

Now Claude Code asks me what I want to restore. I have options:

[SHOW: The restore options appearing]

- **Code and conversation** — go back to that exact point in time. Code and conversation both rewind.
- **Code only** — rewind the files but keep the conversation. Useful if you want to remember what happened but undo the code changes.
- **Conversation only** — keep the code changes but rewind the conversation. Less common but it's there.

I'll pick code and conversation. Full rewind.

[SHOW: Select "code and conversation" — files revert, conversation rewinds]

Let me check the app now.

[SHOW: Switch to browser — refresh — the app is working perfectly again]

Back to normal. Like the refactor never happened. That is the power of checkpoints.

[NOTE: This is the money shot of the episode. Make sure the before/after is dramatic and clear.]

---

### WHEN TO USE /REWIND (9:00 - 10:00) ~1 min

So when would you actually use /rewind?

[SHOW: Bullet points on screen]

**Rewind when:**
- Claude breaks something and you want to undo it
- You went down a wrong path and want to start over
- An experiment didn't work out
- You realize three changes ago was the right version

**You probably don't need it when:**
- The change is small and you can just ask Claude to fix it
- You already committed your code (use git instead)

[SHOW: Terminal]

The key insight is this: checkpoints make it safe to experiment. Try something wild. Ask Claude to completely restructure your app. If it doesn't work? Rewind. No harm done.

That's a completely different mindset than being afraid to make changes.

---

### PUTTING IT ALL TOGETHER (10:00 - 11:00) ~1 min

Let me show you how sessions and checkpoints work together in a real workflow.

[SHOW: Terminal]

Day one. You start a session. You build a feature. You name your session with /rename. You close your laptop.

Day two. You open your terminal. Type `claude --continue`. You're right back where you were. Same conversation. Same context.

You keep building. Claude makes a change that doesn't work. You type `/rewind`. Pick a checkpoint. You're back on track.

You finish the feature. You commit it. Done.

[SHOW: The full flow — continue, work, rewind, work, commit]

Sessions keep your conversation. Checkpoints keep your code. Together, they mean you never lose anything.

---

### RECAP & NEXT EPISODE (11:00 - 12:00) ~1 min

Quick recap.

[SHOW: Bullet points appearing one at a time]

- Sessions are saved automatically. No action needed.
- `claude --continue` for your most recent session.
- `claude --resume` to pick from a list.
- `/rename` to name sessions so you can find them.
- Checkpoints snapshot your code before every edit. Automatic.
- `/rewind` to go back to any point.
- You can restore code only, conversation only, or both.

[SHOW: Terminal with a clean session]

Next episode — slash commands and custom commands. You'll learn how to create your own shortcuts in Claude Code. Like a deploy command, a test command, anything you want. One slash and it runs. Super powerful.

Subscribe and I'll see you there.

[NOTE: End card with subscribe button, playlist link, next episode teaser]
