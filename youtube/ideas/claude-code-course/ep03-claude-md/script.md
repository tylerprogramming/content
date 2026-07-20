# Episode 3 — Full Script
## Claude Code Tutorial #3 - CLAUDE.md Changes Everything
**Target length:** 12 minutes

---

## HOOK (0:00 - 0:35) ~35 seconds

I'm going to ask Claude Code to add a feature to this project. But first — watch what happens without a CLAUDE.md file.

[SHOW: Terminal. Claude Code gets the framework wrong, creates files in the wrong place, uses the wrong style.]

Wrong framework. Wrong structure. It's guessing. Now I'm going to add one file. Just one. And ask the exact same thing.

[SHOW: Terminal. Same prompt. Claude nails it — right framework, right conventions, clean output.]

That file is called CLAUDE.md. And after this video, you'll never start a project without one.

---

## SECTION 1: What Is CLAUDE.md? (0:35 - 2:00) ~85 seconds

So what is this file?

CLAUDE.md is a plain text file you put in the root of your project. When you start Claude Code, it reads this file first — before you even type a prompt.

[SHOW: File tree with CLAUDE.md highlighted at the root]

Think of it as the instruction manual for your project. It tells Claude things like:

- What this project is about
- What tools and technologies you're using
- How files are organized
- What style or conventions to follow
- What to avoid

[SHOW: Quick scroll through an example CLAUDE.md file]

Without it, Claude is starting from zero every single conversation. It looks at your files, makes guesses, and hopes for the best.

With it? Claude already knows the rules before you ask your first question.

[NOTE: Let this sink in. Brief pause.]

Here's the analogy I use. Imagine you hire a new developer. Without CLAUDE.md, they show up day one with no onboarding. No documentation. No context. They just start writing code and hope it fits.

With CLAUDE.md? They show up with a full briefing document. They know the stack. They know the conventions. They know what not to touch.

Which developer would you rather have?

---

## SECTION 2: The Demo — Without CLAUDE.md (2:00 - 3:30) ~90 seconds

Let me show you exactly what I mean. I have a simple project here. It's a task manager app built with basic HTML, CSS, and vanilla JavaScript. Three files.

[SHOW: File tree — index.html, styles.css, app.js]

No CLAUDE.md file. Nothing. Let's start Claude Code and ask it to add a feature.

[SHOW: Start Claude Code in the project folder]

```
claude
```

[SHOW: Type prompt]
```
Add a dark mode toggle to this app.
```

[SHOW: Claude Code works...]

Okay let's see what happened.

[SHOW: Look at the output / files]

Hmm. It added a React component. We're not using React. It created a new file called DarkModeToggle.jsx. That doesn't fit our project at all. It also used Tailwind classes in the HTML. We're using plain CSS.

[SHOW: Point out the wrong framework, wrong files]

Claude did its best. But it guessed wrong. It didn't know our project uses vanilla JavaScript and plain CSS. So it defaulted to what it sees most often — React and Tailwind.

[NOTE: Don't be frustrated. Be matter-of-fact. "It's not Claude's fault — we didn't tell it."]

Let me undo that and try again. But this time, with a CLAUDE.md file.

[SHOW: Undo the changes — `git checkout .` or manually revert]

---

## SECTION 3: Using /init (3:30 - 5:30) ~2 minutes

The fastest way to create a CLAUDE.md file is to let Claude write it for you.

Start Claude Code in your project folder and type:

[SHOW: Type in Claude Code]
```
/init
```

That's it. One command.

[SHOW: Claude Code analyzes the project and generates a CLAUDE.md file]

Watch what it does. It's looking at your files. It's figuring out what technologies you're using. It's checking your file structure. And it's writing a CLAUDE.md file based on what it finds.

[SHOW: The generated CLAUDE.md file]

Let's look at what it created.

[SHOW: Open CLAUDE.md in the terminal or editor]

See? It identified that this is a vanilla JavaScript project. It noted the file structure. It even picked up on the CSS approach.

Now, this auto-generated file is a good starting point. But it's not perfect. Let me show you how to make it actually useful.

---

## SECTION 4: What to Put In CLAUDE.md (5:30 - 8:00) ~2.5 minutes

Here's what I recommend including. I'll edit the file Claude just generated.

[SHOW: Open CLAUDE.md for editing]

**Number one: Project overview.** One or two sentences. What is this thing?

[SHOW: Type/edit in the file]
```markdown
# Task Manager App

A simple browser-based task manager. Single-page app using
vanilla HTML, CSS, and JavaScript. No frameworks. No build tools.
```

That's it. Short. Clear. Now Claude knows the boundaries.

**Number two: Tech stack and conventions.** Be explicit.

[SHOW: Type/edit]
```markdown
## Tech Stack
- HTML5, CSS3, vanilla JavaScript (ES6+)
- No frameworks (no React, no Vue, no Tailwind)
- No build tools or bundlers
- Single stylesheet: styles.css
- Single script file: app.js
```

This is huge. See that "no React, no Tailwind" line? That would have prevented the mistake we saw earlier.

**Number three: File structure.** Tell Claude where things live.

[SHOW: Type/edit]
```markdown
## File Structure
- index.html — main page, all markup here
- styles.css — all styles, using CSS custom properties for theming
- app.js — all logic, uses DOM manipulation (no jQuery)
```

**Number four: Rules and preferences.** Things Claude should always do or never do.

[SHOW: Type/edit]
```markdown
## Rules
- Keep all code in these three files. Do not create new files.
- Use CSS custom properties (variables) for colors and spacing.
- Mobile-first responsive design.
- No external dependencies or CDN links.
- Comments on functions only, not on every line.
```

[NOTE: Slow down here. Each rule should feel deliberate.]

**And here's my favorite one. Number five: What NOT to do.**

[SHOW: Type/edit]
```markdown
## Do NOT
- Do not add React, Vue, or any JavaScript framework
- Do not add Tailwind or any CSS framework
- Do not create new files without asking first
- Do not add a package.json — this is not a Node project
```

This is the secret weapon. Telling Claude what to avoid is just as important as telling it what to do.

[SHOW: The complete CLAUDE.md file, scroll through it]

That whole file is maybe 30 lines. Took two minutes to write. But it completely changes how Claude works with your project.

---

## SECTION 5: The Demo — With CLAUDE.md (8:00 - 9:15) ~75 seconds

Alright, moment of truth. Same project. Same prompt. But now we have CLAUDE.md.

[SHOW: Start a fresh Claude Code session]
```
/clear
```

[SHOW: Type the exact same prompt as before]
```
Add a dark mode toggle to this app.
```

[SHOW: Claude Code works...]

Let's see.

[SHOW: Look at the output]

Look at that. No React. No Tailwind. No new files. It added the toggle right into index.html. The styles went into styles.css using CSS custom properties — exactly what we asked for. The JavaScript went into app.js using vanilla DOM manipulation.

[SHOW: Open in browser, click the dark mode toggle]

It works. And it fits perfectly with the rest of the project.

[SHOW: Quick side-by-side — without CLAUDE.md result vs with CLAUDE.md result]

Same prompt. Totally different results. The only difference? That one file.

---

## SECTION 6: Global vs Project CLAUDE.md (9:15 - 10:15) ~1 minute

One more thing. There are actually two types of CLAUDE.md files.

**Project-level.** That's the one we just made. It lives in your project folder. It only applies to that project.

[SHOW: File tree — CLAUDE.md in project root]

**Global.** This one lives at `~/.claude/CLAUDE.md`. That's your home directory, in a folder called `.claude`.

[SHOW: Terminal — navigate to ~/.claude/]
```
cat ~/.claude/CLAUDE.md
```

This file applies to every project. Every time you start Claude Code, anywhere on your computer, it reads this file first.

[SHOW: Example of a global CLAUDE.md]

I use my global one for personal preferences. Things like:

```markdown
- I prefer TypeScript over JavaScript
- Always use descriptive variable names
- When creating functions, add a brief comment explaining what it does
```

Think of it this way. Global CLAUDE.md is your personal style. Project CLAUDE.md is the project's rules. Both get loaded. Project takes priority if there's a conflict.

---

## SECTION 7: The Iteration Approach (10:15 - 11:15) ~1 minute

Here's my favorite tip about CLAUDE.md. Ready?

Every mistake becomes a rule.

[NOTE: Say this slowly. It's the key takeaway.]

Let me explain. You're working on a project. Claude does something wrong. Maybe it creates a file you didn't want. Maybe it uses the wrong naming convention. Maybe it adds a dependency you don't need.

Instead of just fixing it and moving on — add a rule to your CLAUDE.md.

[SHOW: Example]

Claude created a `.env` file you didn't ask for? Add this:

```markdown
- Do not create .env files. Environment variables are handled by Vercel.
```

Claude used camelCase but your project uses snake_case? Add this:

```markdown
- Use snake_case for all file names and variable names.
```

[SHOW: Adding these rules to CLAUDE.md]

Over time, your CLAUDE.md becomes a living document. It gets smarter with every mistake. After a week of working on a project, your CLAUDE.md file is dialed in. Claude barely makes mistakes anymore.

That's the magic. It's not about writing the perfect CLAUDE.md on day one. It's about building it up over time.

---

## SECTION 8: Quick Reference — @imports (11:15 - 11:30) ~15 seconds

One quick advanced tip. If your project is big and you want to split your CLAUDE.md into multiple files, you can use @imports.

[SHOW: Example in CLAUDE.md]
```markdown
@coding-standards.md
@api-conventions.md
```

Claude will read those files too. But don't worry about this yet. For most projects, one CLAUDE.md file is plenty.

---

## OUTRO (11:30 - 12:00) ~30 seconds

Let's recap. CLAUDE.md is a file that tells Claude Code how your project works. Use /init to generate one. Then customize it with your stack, your rules, and your "do nots."

And remember — every mistake becomes a rule. That's how you build a CLAUDE.md that actually works.

[SHOW: The complete CLAUDE.md file one more time]

This is episode three of the Claude Code course. If you've been following along, you now know how to install Claude Code, write great prompts, and set up CLAUDE.md. That's a solid foundation.

[SHOW: End screen — playlist link, subscribe]

Next episode, we'll get into building real projects from start to finish. I'll see you there.

[NOTE: End screen elements, subscribe animation.]

---

## Total Runtime Estimate: ~12 minutes
| Section | Duration |
|---------|----------|
| Hook | 0:35 |
| What Is CLAUDE.md? | 1:25 |
| Demo — Without | 1:30 |
| Using /init | 2:00 |
| What to Put In | 2:30 |
| Demo — With | 1:15 |
| Global vs Project | 1:00 |
| Iteration Approach | 1:00 |
| @imports | 0:15 |
| Outro | 0:30 |
| **Total** | **~12:00** |
