# Claude Code Tutorial #5 - Permissions & Safety

**Target Length:** 10 minutes
**Style:** Talking head + live terminal demo
**Tone:** Conversational, practical, trust-building

---

## HOOK (0:00 - 0:30) ~30 sec

If you've been using Claude Code for more than five minutes, you've seen this. "Claude wants to run this command. Allow? Yes or no." Over and over and over again.

It's annoying. I get it. But here's the thing. Claude is asking because it's about to change something on your actual computer. And some of those changes? You really do want to approve first.

But here's the good news. You can pre-approve the safe stuff so Claude stops asking. And you can lock down the dangerous stuff so it always asks. Best of both worlds. I'll set it all up in the next 10 minutes. Episode five. Let's go.

[NOTE: Cut to terminal]

---

## SECTION 1: Why Claude Asks for Permission (0:30 - 2:00) ~1.5 min

[SHOW: Terminal with Claude Code open]

Okay, so let's start with why Claude asks for permission in the first place.

Claude Code isn't just a chatbot. It can actually do things on your computer. It can create files. Delete files. Run commands. Install packages. Push code to the internet.

[SHOW: Ask Claude something that triggers a permission prompt, e.g., "Create a new file called test.txt"]

See that? Claude wants to create a file. It's asking me if that's okay. If I say yes, it actually creates that file on my computer.

[SHOW: Approve the action, show the file was created]

And that's the key difference from something like ChatGPT. ChatGPT just talks. Claude Code acts. It changes things. And because it changes things, it needs to check with you first.

[NOTE: Quick talking head]

Now this is actually a great safety feature. You don't want AI just running wild on your computer without asking. But for things that are totally safe, like reading a file? That permission prompt just slows you down.

So let's fix that.

---

## SECTION 2: The Approval Flow (2:00 - 3:00) ~1 min

[SHOW: Terminal with a fresh prompt]

Let me show you the approval flow real quick. When Claude wants to do something, you get a few options.

[SHOW: Trigger a permission prompt]

You can approve it once. That's the default. Claude does the thing, and next time it needs to do something similar, it asks again.

You can also approve it for the whole session. That means for this conversation, Claude won't ask again for that type of action. But next time you start Claude Code, it'll ask again.

[SHOW: Point out the approval options]

Or you can deny it. Claude won't do the thing, and it'll try a different approach.

But none of these are permanent. For permanent settings, we need the permissions system.

---

## SECTION 3: Setting Up Permissions with /permissions (3:00 - 5:30) ~2.5 min

[SHOW: Terminal]

Here's where it gets good. Type slash permissions.

[SHOW: Type `/permissions` and press enter]

This opens up the permissions settings. And it's really straightforward.

[SHOW: The permissions interface]

You've got two lists. An allow list and a deny list. The allow list is stuff Claude can do without asking. The deny list is stuff Claude should never do without asking.

Let me set up what I recommend for beginners. These are the safe actions you should pre-approve.

[SHOW: Add permissions one by one]

First, reading files. Claude reads files constantly. It needs to understand your code. Totally safe. Let's allow that.

[SHOW: Add read file permission]

Next, running your test suite. If you have tests, Claude runs them to check its work. Safe. Allow it.

[SHOW: Add test command permission, e.g., `npm test`]

Running your dev server. Also safe. It just starts your app locally.

[SHOW: Add dev server permission]

Git commands. Things like git status, git diff, git add, git commit. These are local operations. Safe to pre-approve.

[SHOW: Add git permissions]

Now let me show you what to keep gated. What you do NOT want to pre-approve.

Installing packages. Like npm install or pip install. These download code from the internet onto your machine. Always review these.

Deleting files. Obviously. You want to see what's being deleted before it happens.

API calls or network requests. Anything that sends data somewhere. Keep that gated.

[NOTE: Talking head moment]

Think of it this way. If Claude is just looking at stuff on your computer, that's probably safe. If Claude is changing stuff or reaching out to the internet, you want to approve it.

---

## SECTION 4: settings.json Deep Dive (5:30 - 7:00) ~1.5 min

[SHOW: Terminal]

Now behind the scenes, these permissions get saved to a file called settings.json. Let me show you where it lives.

[SHOW: Open or display the settings.json file path]

You can find it in your project's .claude directory. Or in your home directory for global settings.

[SHOW: The contents of settings.json with allow/deny lists]

Here's what it looks like. You've got your allow list up here. These are patterns. Like "read" for reading files, or specific commands like "npm test."

And down here, your deny list. Things Claude should always ask about.

You can edit this file directly if you want. Or just use slash permissions in Claude Code. Same result.

[SHOW: Point out the structure]

The cool thing is you can have project-level settings and global settings. So if you have specific rules for one project, like "never touch the database migration files," you can set that up just for that project.

---

## SECTION 5: Having Claude Set Up Permissions For You (7:00 - 8:30) ~1.5 min

[SHOW: Terminal with Claude Code]

Okay here's a pro tip. You can actually ask Claude to set up permissions for you.

[SHOW: Type something like "Set up permissions for this project. Allow reading files, running tests with npm test, and git commands. Deny any file deletions and package installs."]

Watch this. I'm going to ask Claude to configure my permissions.

[SHOW: Claude's response and the actions it takes]

See? Claude knows what settings.json looks like. It knows the format. It just sets it up for you. You still approve the changes, because it's modifying your settings file. But it does the work.

[SHOW: Verify the permissions are set by running `/permissions`]

And there they are. All configured. This is one of those things where Claude Code is really good at configuring itself. You just have to tell it what you want in plain English.

---

## SECTION 6: Demo - The Speed Difference (8:30 - 9:15) ~45 sec

[SHOW: Terminal, split screen or before/after]

Let me show you the difference this makes. Before permissions, I ask Claude to do something and I get interrupted every few seconds. Approve this. Approve that. Approve this.

[SHOW: Quick montage or example of constant approval prompts]

After permissions? Watch.

[SHOW: Ask Claude to do a multi-step task. It reads files, runs tests, makes changes -- all without stopping]

It just goes. No interruptions. It reads the files it needs, makes changes, runs tests. All stuff I pre-approved. And if it hits something on the deny list, it stops and asks. Exactly how it should work.

That's the speed difference. Night and day.

---

## SECTION 7: Recap & Next Episode (9:15 - 10:00) ~45 sec

[NOTE: Talking head to camera]

Alright, quick recap. Claude Code asks for permission because it actually changes your computer. That's a good thing.

But you can pre-approve safe actions to make it faster. Reading files, running tests, git commands. Safe. Allow them. Installing packages, deleting files, network requests. Keep those gated.

Use slash permissions to set it up. Or just ask Claude to do it for you.

Next episode, we're covering models and memory. I'll show you the three different AI models you can use, when to pick each one, and how to make Claude remember things across conversations. It's a good one. I'll see you there.

[SHOW: End screen with subscribe button and next episode link]

[NOTE: Add end screen elements in post, 20 seconds]
