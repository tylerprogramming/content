# Claude Code Tutorial #6 - Models & Memory

**Target Length:** 10 minutes
**Style:** Talking head + live terminal demo
**Tone:** Conversational, practical, "insider knowledge" feel

---

## HOOK (0:00 - 0:30) ~30 sec

Did you know Claude Code actually has three different AI brains you can switch between? One is fast and cheap. One is balanced. And one is the most powerful AI model in the world.

Most people just use whatever the default is and never think about it. But picking the right model for the right task? That's how you save money and get better results at the same time.

Plus, I'm going to show you something most people don't know about. Claude has memory. It remembers things about you across conversations. I'll show you how to use it. Episode six. Let's go.

[NOTE: Cut to terminal]

---

## SECTION 1: The Three Models (0:30 - 2:30) ~2 min

[SHOW: Terminal with Claude Code open]

Okay. Three models. Let me break them down.

[NOTE: Consider a simple graphic overlay showing the three tiers]

First, there's Haiku. Haiku is the fast one. It's also the cheapest. Think of it like a junior assistant. It's great for simple stuff. Quick questions. Formatting text. Basic tasks that don't require deep thinking.

Second, Sonnet. Sonnet is the balanced one. Good speed, good quality, reasonable cost. This is what most people use for everyday work. Writing code, explaining concepts, working through problems. Sonnet handles it well.

Third, Opus. Opus is the powerhouse. It's slower. It costs more. But it's the smartest model available. When you need deep reasoning, complex architecture decisions, or really tricky debugging, Opus is what you want.

[NOTE: Quick talking head]

Here's how I think about it. Don't use a sledgehammer to hang a picture frame. Match the model to the task. Simple task? Haiku. Normal work? Sonnet. Hard problem? Opus.

That's it. That's the framework.

---

## SECTION 2: When to Use Each Model (2:30 - 4:00) ~1.5 min

[SHOW: Terminal or talking head with text overlay]

Let me get specific. Here's when I use each one.

Haiku. I use this for quick lookups. "What does this error mean?" Formatting something. Renaming variables. Anything where speed matters more than depth. Haiku answers in like two seconds. It's great for those rapid-fire tasks.

[SHOW: Text overlay or list of Haiku use cases]

Sonnet. This is my daily driver. Building features. Writing functions. Code reviews. Explaining how something works. Sonnet is the sweet spot for 80 percent of what I do.

[SHOW: Text overlay or list of Sonnet use cases]

Opus. I save this for the hard stuff. Designing a system architecture from scratch. Debugging something really weird that Sonnet couldn't figure out. Writing complex business logic. If I need Claude to really think, I switch to Opus.

[SHOW: Text overlay or list of Opus use cases]

The cost difference is real, by the way. Haiku is way cheaper than Opus. So if you're paying per token, using Haiku for simple stuff saves you real money.

---

## SECTION 3: Switching Models with /model (4:00 - 5:30) ~1.5 min

[SHOW: Terminal with Claude Code]

Okay, let me show you how to actually switch. It's one command.

[SHOW: Type `/model` and press enter]

Slash model. That's it. You get a list of available models and you pick the one you want.

[SHOW: The model selection interface]

Right now I'm on Sonnet. Let me switch to Opus.

[SHOW: Select Opus]

Done. Now everything I ask Claude will use Opus until I switch again. And here's the cool part. You can switch mid-conversation. You don't have to start over.

[SHOW: Ask Claude a question, note it's using Opus]

So a totally valid workflow is this. Start with Sonnet for the normal stuff. Hit a wall on something complex. Switch to Opus for that one hard part. Then switch back to Sonnet for the rest.

[SHOW: Type `/model` again and switch back to Sonnet]

See? Took two seconds. No context lost. You're back on Sonnet.

[NOTE: Quick talking head]

Think of it like shifting gears in a car. You don't drive in first gear the whole time. You shift up when you need power and back down when you don't.

---

## SECTION 4: Live Model Comparison (5:30 - 6:30) ~1 min

[SHOW: Terminal, prepare to demo the same task with different models]

Let me show you the difference in real time. I'm going to ask the same question to two different models and you'll see the difference.

[SHOW: Switch to Haiku with `/model`]

Okay, I'm on Haiku. Let me ask it something moderately complex.

[SHOW: Type a task like "Explain the trade-offs between SQL and NoSQL databases for a startup MVP"]

[SHOW: Haiku's response -- fast but potentially less thorough]

That was fast. And the answer is decent. But watch this.

[SHOW: Switch to Opus with `/model`]

Now the same question on Opus.

[SHOW: Type the same question]

[SHOW: Opus's response -- slower but more nuanced and detailed]

See the difference? Opus went deeper. More nuance. More specific recommendations. But it also took longer. Neither answer is wrong. It's about what you need in the moment.

---

## SECTION 5: Memory - Claude Remembers You (6:30 - 8:00) ~1.5 min

[SHOW: Terminal with Claude Code]

Okay, now let's talk about memory. This is one of my favorite features.

Claude Code can remember things about you and your preferences. And it carries those memories across conversations. So you tell it something once, and it just knows from then on.

[SHOW: Terminal]

Let me show you. I'm going to tell Claude to remember something about how I like my code.

[SHOW: Type something like "Remember that I always want TypeScript code with explicit types, never use 'any'. Also remember that I prefer functional programming patterns over classes."]

[SHOW: Claude's confirmation that it will remember this]

Okay. Claude says it'll remember that. Now watch what happens. I'm going to start a completely new conversation.

[SHOW: Type `/clear` to start fresh, or close and reopen Claude Code]

Brand new session. Claude has no context from our previous conversation. But let me ask it to write some code.

[SHOW: Type "Write a function that fetches user data from an API and formats it"]

[SHOW: Claude's response -- should use TypeScript with explicit types, functional patterns, no 'any']

Look at that. TypeScript. Explicit types. Functional pattern. No classes. It remembered. I didn't have to tell it again. It just knew.

[NOTE: Talking head moment]

This is huge for your workflow. Over time, Claude learns how you like things. Your coding style. Your preferences. Your project conventions. And it just applies them automatically.

---

## SECTION 6: Managing Memory (8:00 - 9:15) ~1.25 min

[SHOW: Terminal]

Now you might be wondering, where does Claude store these memories? And can I see them?

Yes. Claude stores memories in a file called CLAUDE.md. There's one in your home directory for global preferences, and you can have one in each project for project-specific stuff.

[SHOW: Display the CLAUDE.md file contents]

Here's mine. You can see the things Claude has remembered about me. My preferences, my coding style, project-specific notes.

You can also edit this file directly. Just open it and add whatever you want. Or delete things you don't want Claude to remember anymore.

[SHOW: Open CLAUDE.md in an editor or show it in terminal]

And if you want Claude to remember something specific, just tell it in plain English. Say "Remember that..." or "From now on, always..." Claude gets it.

[SHOW: Type "From now on, always add error handling to every function you write"]

[SHOW: Claude confirms]

Easy.

You can also ask Claude what it remembers about you. Just ask.

[SHOW: Type "What do you remember about my preferences?"]

[SHOW: Claude lists its memories]

That's it. Full transparency. You see everything Claude knows. You control everything it remembers.

---

## SECTION 7: Recap & Next Episode (9:15 - 10:00) ~45 sec

[NOTE: Talking head to camera]

Alright, let's recap. Three models. Haiku is fast and cheap for simple tasks. Sonnet is your daily driver for normal work. Opus is the powerhouse for hard problems. Switch with slash model. Match the model to the task.

Memory. Tell Claude your preferences once and it remembers them across conversations. It stores them in CLAUDE.md. You can view, edit, or delete memories anytime.

That wraps up the foundations of Claude Code. You now know how to install it, use it, manage context, set up permissions, pick the right model, and make Claude remember your preferences.

If you've been following along with the whole course, you're way ahead of most people. In the next set of episodes, we're going to get into the real power features. Stay tuned. I'll see you there.

[SHOW: End screen with subscribe button, playlist link, and next episode]

[NOTE: Add end screen elements in post, 20 seconds]
