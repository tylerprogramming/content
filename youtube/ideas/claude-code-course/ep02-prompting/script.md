# Episode 2 — Full Script
## Claude Code Tutorial #2 - Write Prompts That Actually Work
**Target length:** 12 minutes

---

## HOOK (0:00 - 0:30) ~30 seconds

I'm going to build the same project twice. Same tool. Same goal. But two completely different prompts.

[SHOW: Terminal — type "Build me a website" and hit enter]

That's what most people do. Now watch this.

[SHOW: Terminal — type the detailed prompt from the demo section below]

Same tool. The only difference? How I asked.

In this video, I'm going to give you the exact formula I use to write prompts that get real results. Every time.

---

## SECTION 1: Why Prompts Matter (0:30 - 2:00) ~90 seconds

If you watched episode one, you already know how to install Claude Code and give it a basic prompt.

But here's what I didn't tell you. The prompt is everything.

[SHOW: Terminal with Claude Code open]

Claude Code is like a really talented contractor. If you tell them "build me a house," they'll build you a house. But it might have two bedrooms when you wanted four. The kitchen might be in the wrong spot. The color might be wrong.

Not because the contractor is bad. Because you didn't tell them what you actually wanted.

[NOTE: Use hand gestures here. This is an important concept to sell.]

Same thing with Claude Code. Vague prompt? Vague result. Specific prompt? Exactly what you wanted.

Let me show you what I mean.

---

## SECTION 2: The Side-by-Side Demo (2:00 - 4:30) ~2.5 minutes

Alright, let's build the same thing twice. I want a personal portfolio website. Simple. One page.

**Round one. The vague prompt.**

[SHOW: Type in Claude Code:]
```
Build me a portfolio website.
```

[SHOW: Claude Code works. Output appears.]

Okay, let's see what we got.

[SHOW: Open the result in a browser]

It's... fine. It's a website. It has my name — well, a placeholder name. Some sections. But it looks generic. The colors are random. There's no personality. It's like a template nobody asked for.

[NOTE: Don't be mean about it. Just be honest. "It works, but..."]

Now let me close this and start fresh.

[SHOW: Type `/clear` in Claude Code, then delete the files]

**Round two. The specific prompt.**

[SHOW: Type in Claude Code:]
```
Build me a personal portfolio website. Single HTML file with embedded CSS.

About me: I'm Tyler, a content creator who makes videos about AI tools.

Design: Dark theme with a deep navy background (#0a192f). Clean, minimal.
Use Inter or system sans-serif font. Subtle hover animations on links.

Sections:
1. Hero — my name large, one-line tagline "I help people build with AI",
   and links to YouTube and Twitter
2. Projects — 3 cards in a grid: "Claude Code Course" (description: beginner
   series on AI coding), "AI Tool Reviews" (description: honest reviews of
   the latest AI tools), "Newsletter" (description: weekly AI tips)
3. Footer — simple, just "Made with Claude Code" and a copyright line

Make it responsive. Mobile-first.
```

[SHOW: Claude Code works. Takes a bit longer — that's fine.]

Let's see this one.

[SHOW: Open in browser]

Night and day difference. The dark theme is there. The sections are exactly what I asked for. The hover animations work. It looks like a real website someone would actually use.

[SHOW: Side-by-side comparison — vague result vs specific result]

Same tool. Same amount of time writing the prompt — maybe an extra 30 seconds. Totally different result.

---

## SECTION 3: The Prompt Formula (4:30 - 7:00) ~2.5 minutes

So how do you write prompts like that? I use a simple formula. Four parts.

[SHOW: Text overlay or draw on screen:]
```
CONTEXT + TASK + CONSTRAINTS + FORMAT
```

Let me break it down.

**Part one: Context.** Who is this for? What's the background?

[SHOW: Highlight "About me: I'm Tyler, a content creator..." from the previous prompt]

This tells Claude who you are and what the project is about. Without this, Claude guesses. And it usually guesses wrong.

**Part two: Task.** What do you actually want built?

[SHOW: Highlight "Build me a personal portfolio website" from the prompt]

Be specific. Not "build a website." But "build a personal portfolio website with a hero section, project cards, and a footer."

**Part three: Constraints.** What rules should it follow?

[SHOW: Highlight "Dark theme with deep navy... responsive... mobile-first" from the prompt]

Colors. Fonts. Layout rules. Technology choices. These are the guardrails that keep Claude from going off track.

**Part four: Format.** What should the output look like?

[SHOW: Highlight "Single HTML file with embedded CSS" from the prompt]

Do you want one file or many? What language? What structure? Tell Claude exactly what to hand you.

[NOTE: Pause here. Let viewers absorb.]

You don't need all four every time. But the more you include, the better your results.

Let me give you a cheat sheet.

[SHOW: Quick reference card:]
```
CONTEXT  → Who/what is this for?
TASK     → What should Claude build?
CONSTRAINTS → Colors, rules, limits, style
FORMAT   → File type, structure, output
```

---

## SECTION 4: Common Mistakes (7:00 - 9:00) ~2 minutes

Let me save you some pain. Here are the three biggest prompting mistakes I see beginners make.

**Mistake number one: Being too vague.**

[SHOW: Example in terminal]
```
Bad:  "Make me an app"
Good: "Build a to-do list app with add, complete, and delete
       functionality. Use HTML, CSS, and JavaScript in a single file."
```

"Make me an app" could be anything. A mobile app. A web app. A calculator. A game. Don't make Claude guess.

**Mistake number two: Asking for everything at once.**

[SHOW: Example in terminal]
```
Bad:  "Build me a full SaaS platform with user auth, payments,
       a dashboard, admin panel, and API"
Good: "Build me a simple login page with email and password fields.
       Use HTML and CSS. We'll add more features after."
```

Start small. Build in layers. You can always add more with follow-up prompts. Trying to build everything in one shot leads to messy results.

**Mistake number three: Not giving examples.**

[SHOW: Example in terminal]
```
Bad:  "Make it look modern"
Good: "Make it look like the Stripe homepage — clean, lots of
       whitespace, sans-serif font, subtle gradients"
```

"Modern" means something different to everyone. But "like the Stripe homepage" gives Claude a clear target.

[NOTE: These three can be quick-fire. Keep the energy up.]

---

## SECTION 5: Iterating with Follow-ups (9:00 - 10:30) ~90 seconds

Here's a secret. You don't need the perfect prompt on the first try.

Claude Code remembers your entire conversation. So you can iterate.

[SHOW: Claude Code with the portfolio site from earlier]

Watch. I'll just type:

[SHOW: Type follow-up prompt]
```
Add a "Contact" section before the footer with an email link
and a short message that says "Let's build something together."
```

[SHOW: Claude adds the section]

Done. Now another:

[SHOW: Type another follow-up]
```
The project cards need more spacing between them. Add 2rem gap.
And make the card backgrounds slightly lighter than the page background.
```

[SHOW: Claude makes the changes]

See? You're having a conversation. Build the foundation with your first prompt. Then refine with follow-ups.

This is actually how I work in real life. First prompt gets me 80% there. Then two or three follow-ups to polish it.

---

## SECTION 6: When to Start Fresh (10:30 - 11:30) ~1 minute

One more thing. Sometimes the conversation goes sideways. Claude starts making weird changes. Or it's confused about what you want.

When that happens, don't keep pushing. Just start fresh.

[SHOW: Type `/clear` in Claude Code]

```
/clear
```

This wipes the conversation and starts over. Your files are still there. Nothing is deleted. You just get a clean slate.

My rule of thumb: if I've sent more than five or six follow-ups and the result still isn't right, I start over with a better first prompt.

[SHOW: Start a new prompt incorporating lessons from the failed attempt]

Think of it like this. Sometimes it's faster to rewrite the blueprint than to keep patching a bad foundation.

And honestly? Your second attempt is always better. Because now you know what you actually want.

---

## OUTRO (11:30 - 12:00) ~30 seconds

Quick recap. The formula is Context, Task, Constraints, Format. Be specific. Start small. Iterate with follow-ups. And don't be afraid to start over.

[SHOW: Quick formula recap on screen]

Next episode is a big one. I'm going to show you CLAUDE.md — a file that completely changes how Claude Code works on your projects. It's like giving Claude a permanent instruction manual. You don't want to miss it.

[SHOW: End screen — "Episode 3: CLAUDE.md — The Most Important File"]

See you there.

[NOTE: End screen elements, subscribe animation.]

---

## Total Runtime Estimate: ~12 minutes
| Section | Duration |
|---------|----------|
| Hook | 0:30 |
| Why Prompts Matter | 1:30 |
| Side-by-Side Demo | 2:30 |
| The Prompt Formula | 2:30 |
| Common Mistakes | 2:00 |
| Iterating with Follow-ups | 1:30 |
| When to Start Fresh | 1:00 |
| Outro | 0:30 |
| **Total** | **~12:00** |
