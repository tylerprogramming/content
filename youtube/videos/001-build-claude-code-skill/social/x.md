# X/Twitter Thread — Build a Claude Code Skill from Scratch

**Main tweet:**
I have 20 Claude Code skills. Every one of them was built the same way. Here's the exact process - live, from scratch:

---

**Reply 1:**
👉 Every skill starts with a SKILL.md file. Front matter at the top: name, description, allowed-tools. The description field is how Claude decides when to trigger it. Get this wrong and the skill never fires.

**Reply 2:**
👉 Below the front matter: step-by-step instructions. Not vague guidelines - an actual SOP. Step 1, Step 2, Step 3. Rules section at the bottom for everything that went wrong in testing.

**Reply 3:**
👉 Test it immediately. Type /hook-writer and watch Claude read your SKILL.md and follow it. First version will be off. That's fine - that's the loop.

**Reply 4:**
👉 Add a reference file. examples.md with real outputs you liked. "Match this tone. Avoid this." One line pointing to it in your instructions. Output shifts immediately.

**Reply 5:**
👉 Two files. That's a complete skill. SKILL.md + one reference doc. Complexity scales from there - but start with two files.

**Final reply:**
Full build demo - front matter to working slash command:
[VIDEO_URL]
