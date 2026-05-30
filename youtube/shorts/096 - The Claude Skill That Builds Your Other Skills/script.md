# Short #096 - The Claude Skill That Builds Your Other Skills

**Format:** Screen recording tutorial, meta framing
**Target length:** 40-55 seconds
**Hook pattern:** Meta curiosity hook + specific outcome ("skill that builds skills" loops back on itself)

---

## Hook (0-3s)

"There's a Claude skill whose only job is to build other Claude skills. I'm not joking."

**TEXT ON SCREEN:** "A SKILL THAT BUILDS SKILLS"

[SHOW: Terminal with /plugin install skill-creator command visible]

---

## Script

[SHOW: Claude Code — /plugin command]

It's called skill-creator. Anthropic ships it in the official plugin marketplace. One command to install.

```
/plugin install skill-creator
```

[SHOW: Installation completing, skill-creator ready]

Now here's the move. You ask it to build you a skill. In plain English.

[SHOW: Typing in Claude Code]

"Build me a skill called /meal-log that reads a food photo and logs the calories and protein to a CSV."

[SHOW: skill-creator running — generating SKILL.md, asking clarifying questions]

It asks what triggers the skill. What inputs it takes. What outputs it produces. Then it writes the SKILL.md file, the Python helper, the frontmatter. Everything.

[SHOW: Finished skill file in VS Code]

Two minutes later, I have a working /meal-log skill. I didn't write a line of it.

The wild part — it can also improve your existing skills. And run evals to measure how well they perform.

I built 25 of my skills by hand. I wish I had this from day one.

Comment "creator" and I'll send you the install command plus 3 prompts that generate the best skills.

---

## Production Notes

**Screen recordings needed:**
1. Terminal — `/plugin install skill-creator` command
2. Installation output
3. Claude Code — typing the "build me a /meal-log skill" prompt
4. skill-creator asking clarifying questions (trigger, inputs, outputs)
5. SKILL.md being written live (speed up)
6. VS Code showing the finished file
7. Running the new /meal-log skill once to prove it works
8. Quick beat showing a folder with 25+ skills in ~/.claude/skills/
