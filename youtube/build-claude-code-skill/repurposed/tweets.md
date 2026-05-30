# Tweets — Build a Claude Code Skill from Scratch

---

## Standalone Tweets

**Tweet 1 (Practical tip):**
Claude Code skill structure is just: front matter + instructions. Front matter tells Claude when to trigger. Instructions tell Claude what to do. Two parts. That's it. Most people overcomplicate it.

---

**Tweet 2 (Hot take):**
Hot take: if your Claude Code output varies wildly every time you use it, you don't have a Claude problem. You have an instructions problem. Skills fix this. Write the SOP once, get consistent output every time.

---

**Tweet 3 (Practical tip):**
The description field in a SKILL.md front matter is the most important line you'll write. It's how Claude knows when to trigger your skill. Get it wrong and the skill never loads. Get it right and it fires on natural language every time.

---

**Tweet 4 (Hot take):**
Unpopular opinion: most Claude Code tutorials are useless because they show you the finished skill, not the iteration loop. The first version is always wrong. The process of fixing it is the actual skill.

---

**Tweet 5 (Insight):**
A Claude Code skills library is a moat. Anyone can prompt Claude. Not everyone has 20 custom skills that encode their exact workflow, their voice, their style, their formats. That gap compounds the longer you build.

---

**Tweet 6 (Practical tip):**
Add an examples.md file to any Claude Code skill. Drop in 5 outputs you love and 5 you hate. Tell the skill to read it before generating. Output quality jumps immediately. Most people skip this step.

---

**Tweet 7 (Insight):**
Skills are shareable. Build a workflow for yourself, zip the folder, send it to someone. They drop it in their skills directory and they're running your exact process in seconds. That's the real unlock nobody is talking about.

---

## 3-Tweet Thread

**Tweet 1:**
Built a Claude Code skill from scratch this week. Here's the exact structure that makes it work (and the one field that breaks everything if you get it wrong):

**Tweet 2:**
Every skill has two parts.

1. Front matter - the metadata. Name, description, allowed tools. The description field is critical - it's how Claude knows when to trigger your skill. Write it wrong and your skill never loads.

2. Instructions - the SOP. Step by step. What to do first, then what, what the output looks like, what rules to follow.

That's it. Two parts. Markdown file. Stored in ~/.claude/skills/.

**Tweet 3:**
The part nobody mentions: the first version is always wrong.

You test it. Something's off. You add two lines to the rules. You run it again. Better.

You add a reference file with examples of what you actually want. You run it again. Now it sounds exactly like you.

That iteration loop is the whole game.

---
