# LinkedIn - Claude Design + Claude Code: Prompt to Live URL in 23 Minutes

**Video:** https://www.youtube.com/watch?v=aiMZrj4zqo8
**Best time:** Tue-Thu 10-11 AM ET. Put the link in the first comment if reach dips.

---

I built a landing page without opening Figma, hiring a designer, or writing frontend code.

Prompt to a live production URL in 23 minutes.

Most of the Claude Design videos out there stop at the prototype. They generate a nice looking page and move on. The part nobody covers well is the handoff, where the design actually becomes real code that ships.

So that is the thing I wanted to show start to finish.

Here is the actual workflow.

First I set up a design system, which is the most slept-on feature in Claude Design. I did not point it at a repo. I just uploaded four screenshots of designs I liked from Google Images. Claude pulled the color palette, the typography, and the spacing from those.

Then I prompted the landing page. Before it generated anything, it asked me clarifying questions, kind of like plan mode in Claude Code.

Once it was drafted, I iterated right in the canvas. Four ways to do it. Pull the tweak sliders, click and edit an element directly, drop a comment, or literally draw an arrow on the design. You just point at the thing instead of writing a full prompt every time.

Then the handoff. Claude Design bundles the design, a readme, and the chat history, and hands Claude Code a single command. Claude Code wrote the page into my real Next.js repo, using my existing components and design tokens.

I ran it locally, fixed one small thing myself, then deployed it from inside Claude Code with the Vercel MCP. No dashboard, no tab switching. A live URL came back in two minutes.

I want to be honest about the catch. Claude Design has its own weekly usage meter, separate from Claude Code. One full workflow burned about three quarters of my Pro allowance. It is not a dealbreaker, but you should know what you are buying.

This is not one-click magic and it will not do the thinking for you.

But the end-to-end loop is genuinely new, and if you already live in Claude Code, this is the visual layer that was missing.

What is the first thing you would ship with it?

https://www.youtube.com/watch?v=aiMZrj4zqo8
