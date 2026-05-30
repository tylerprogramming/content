# Short #094 - Your First Claude Skill in 2 Minutes

**Format:** Screen recording tutorial
**Target length:** 45-60 seconds
**Hook pattern:** "Your first X in Y minutes" (mirrors #088 which was the opening post of the batch)

---

## Hook (0-3s)

"Build your first Claude skill in 2 minutes. Zero code."

**TEXT ON SCREEN:** "YOUR FIRST SKILL → 2 MIN"

[SHOW: Empty VS Code window, ~/.claude/skills folder visible]

---

## Script

[SHOW: Terminal — mkdir ~/.claude/skills/hello-world]

Step one. Open your skills folder. Make a new directory. Name it whatever the skill does.

[SHOW: Terminal — touch SKILL.md]

Step two. Create a file called SKILL.md. That's all you need.

[SHOW: VS Code — open SKILL.md, start typing frontmatter]

Step three. Paste this frontmatter. Name, description, trigger words.

```
---
name: hello-world
description: Greet the user by name
---
```

Then write the instructions in plain English. "Ask the user for their name. Respond with a short personalized greeting."

[SHOW: Save file, switch to Claude Code terminal]

Step four. Open Claude Code. Type /hello-world. It runs.

[SHOW: Claude Code executing the skill]

That's it. That's a skill. No Python. No API keys. No SDK. Just a markdown file.

I have 25 of these running my entire content business. Comment "Skill" and I'll send you four free ones to start with.

---

## Production Notes

**Screen recordings needed:**
1. Empty skills folder in Finder
2. Terminal mkdir + touch commands
3. VS Code — typing the frontmatter live
4. VS Code — typing plain English instructions
5. Claude Code — invoking /hello-world
6. Result displayed
