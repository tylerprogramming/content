# Episode 7 — Plan Before You Build
## Claude Code Tutorial #7 - Plan Mode & Thinking

**Target length:** 12 minutes
**Audience:** Non-technical founders, beginners
**Tone:** Conversational, practical, fast-paced

---

### INTRO (0:00 - 1:30) ~1.5 min

Here's the biggest mistake I see beginners make with Claude Code. They jump straight into building. They type a prompt, Claude starts editing files, and ten minutes later they realize it built the wrong thing.

[SHOW: Terminal with Claude Code open, a messy prompt, files being edited rapidly]

There's a better way. Plan Mode lets you explore your codebase and map out exactly what Claude will do — before it touches a single file.

[SHOW: Quick flash of Plan Mode output — a clean numbered plan]

Today I'm going to show you how to use Plan Mode, when to use it, and how Claude's extended thinking works behind the scenes. By the end of this video, you'll have a workflow that saves you from wasting time on wrong implementations.

[NOTE: Title card — "Claude Code Tutorial #7 - Plan Before You Build"]

If you're new here, this is part of a free course on Claude Code. Links to every episode are in the description. Let's get into it.

---

### WHAT IS PLAN MODE? (1:30 - 3:00) ~1.5 min

Okay. So what is Plan Mode?

[SHOW: Terminal with Claude Code running]

Think of it like this. Normally when you give Claude a task, it just starts doing it. It reads files, edits code, creates things. That's great for simple stuff. But for anything complex? You want Claude to think first.

Plan Mode is a toggle. When it's on, Claude can read your files but it cannot edit them. It's read-only. It explores your code, understands the structure, and then tells you what it would do — step by step.

[SHOW: Type in terminal — highlight the Plan Mode indicator]

You review that plan. You say "yeah that looks right" or "actually, change this part." And then — only then — you flip Plan Mode off and let Claude build.

It's the difference between a contractor who just starts swinging a hammer and one who shows you blueprints first.

[NOTE: Consider a quick visual metaphor — blueprint vs construction]

---

### HOW TO TOGGLE PLAN MODE (3:00 - 4:30) ~1.5 min

Let me show you how it works. It's incredibly simple.

[SHOW: Terminal with Claude Code open, cursor in the input area]

You toggle Plan Mode with Shift+Tab. That's it. Shift+Tab.

[SHOW: Press Shift+Tab — show the mode indicator change in the input area]

See that? The input area now says "plan" instead of "normal." That tells you Plan Mode is on. Claude will only read — it won't write.

Let me toggle it back. Shift+Tab again.

[SHOW: Press Shift+Tab — mode goes back to normal]

Normal mode. Now Claude can read and write.

One more time. Shift+Tab — Plan Mode. Shift+Tab — normal mode. Easy.

[SHOW: Toggle back and forth twice quickly]

[NOTE: Make sure the mode indicator is clearly visible on screen. Zoom in if needed.]

Now there's actually a third mode here too. If you keep pressing Shift+Tab you'll see "plan (auto-accept)." That's for when you want Claude to plan AND automatically start building once the plan is ready. I'd skip that for now. Stick with regular Plan Mode where you review the plan first.

---

### DEMO: PLANNING A FEATURE (4:30 - 7:00) ~2.5 min

Let's do a real example. Say I have a simple web app and I want to add a dark mode toggle.

[SHOW: Open a project folder — a basic web app with a few files]

First, I'm going to toggle Plan Mode on. Shift+Tab.

[SHOW: Press Shift+Tab — Plan Mode indicator appears]

Now I'll type my request.

[SHOW: Type: "I want to add a dark mode toggle to this app. A button in the top right corner that switches between light and dark themes. The user's preference should be saved."]

Hit enter. Now watch what happens.

[SHOW: Claude reading files — show it examining the HTML, CSS, JavaScript files]

See? It's reading files. It's looking at the structure. But it's not changing anything.

[SHOW: Claude outputs a numbered plan — something like:
1. Add a toggle button to the header in index.html
2. Create dark mode CSS variables in styles.css
3. Add JavaScript to handle the toggle and save preference to localStorage
4. Add a transition effect so the switch is smooth]

There's the plan. Four steps. Clear. Specific. I can read each one and decide if that's what I want.

Maybe I read step 4 and think — actually, I don't want a transition effect. I want it to switch instantly. So I can tell Claude:

[SHOW: Type: "Looks good but skip the transition effect on step 4. Just make it an instant switch."]

[SHOW: Claude updates the plan]

Now I'm happy with it. Time to build. I toggle Plan Mode off — Shift+Tab.

[SHOW: Press Shift+Tab — back to normal mode]

And I type:

[SHOW: Type: "Go ahead and implement the plan."]

[SHOW: Claude starts creating and editing files — show the actual code changes happening]

Now it's building. And it's following the plan we agreed on. No surprises.

[NOTE: Let Claude finish the implementation. Show the final result — the dark mode toggle working in a browser.]

That's the workflow. Explore. Plan. Review. Build.

---

### THE WORKFLOW: EXPLORE > PLAN > IMPLEMENT > COMMIT (7:00 - 8:30) ~1.5 min

Let me give you the framework I use for every non-trivial task.

[SHOW: Text overlay or whiteboard style:
1. EXPLORE — Plan Mode on, ask Claude to look around
2. PLAN — Ask for a step-by-step approach
3. IMPLEMENT — Plan Mode off, tell Claude to build
4. COMMIT — Ask Claude to commit the changes]

Step one. Explore. Turn on Plan Mode and ask Claude to look at the relevant parts of your codebase. "Look at the auth system and tell me how it works." Claude reads files and explains.

Step two. Plan. Now ask for the plan. "How would you add Google login?" Claude gives you a numbered list.

Step three. Implement. Toggle Plan Mode off. Tell Claude to build it. It follows the plan.

Step four. Commit. Ask Claude to commit the changes. We covered this in episode 5.

[SHOW: Quick montage of each step happening in the terminal]

This four-step loop is how I approach anything complex. A new feature. A refactor. A bug that spans multiple files. Explore, plan, implement, commit.

---

### WHEN TO USE PLAN MODE (AND WHEN TO SKIP IT) (8:30 - 9:30) ~1 min

Now — you don't need Plan Mode for everything.

[SHOW: Two-column comparison on screen]

Use Plan Mode when:
- The task touches multiple files
- You're not sure how your codebase is structured
- The feature is complex or ambiguous
- You want to understand before you change

[SHOW: Right column]

Skip Plan Mode when:
- It's a simple, obvious task — "fix this typo"
- You've done this exact thing before
- The task is one file, one change
- You just need something quick

[SHOW: Terminal example of a simple task]

If someone asks me to fix a button color? I'm not using Plan Mode. I'm just telling Claude to do it.

But if someone asks me to add a payment system? Plan Mode. Every time.

[NOTE: Keep this section punchy. Don't over-explain.]

---

### EXTENDED THINKING (9:30 - 11:00) ~1.5 min

One more thing I want to cover. Extended thinking.

[SHOW: Terminal with Claude Code]

You might have noticed that sometimes Claude pauses for a moment before responding. It's not frozen. It's thinking.

Extended thinking is Claude reasoning through your problem before it acts. It's on by default in Claude Code. You don't need to do anything.

[SHOW: Claude processing a request — show the thinking indicator]

Think of it like this. Plan Mode is you asking Claude to think out loud and show you the plan. Extended thinking is Claude's internal thought process — it happens automatically on every request.

They work together. When you're in Plan Mode, Claude uses extended thinking to reason about your codebase and come up with a good plan. When you're in normal mode, it uses extended thinking to figure out the best way to implement things.

[SHOW: A more complex prompt — Claude takes a moment to think, then responds with a well-structured answer]

The key takeaway? You don't need to manage extended thinking. It just works. But now you know what's happening when Claude takes a beat before responding. It's thinking through the problem. That's a good thing.

[NOTE: Keep this high-level. The audience is non-technical. Don't get into token counts or model details.]

---

### RECAP & NEXT EPISODE (11:00 - 12:00) ~1 min

Let's recap.

[SHOW: Bullet points appearing one at a time]

- Plan Mode — Shift+Tab to toggle. Read-only exploration before building.
- The workflow — Explore, Plan, Implement, Commit.
- Use Plan Mode for complex tasks. Skip it for simple ones.
- Extended thinking — Claude reasons before acting. It's on by default.

[SHOW: Terminal with a final clean Plan Mode example]

Next episode, we're covering sessions and checkpoints. You'll learn how to pick up where you left off, name your sessions, and — this is the big one — rewind your code to any point in history if something goes wrong. It's like an undo button for your entire project.

If this was helpful, subscribe and I'll see you in the next one.

[NOTE: End card with subscribe button, playlist link, next episode teaser]
