# The Claude Code Blueprint

Three concepts, in order. Use them on real work for a week before you add anything else.

There are 23 things worth knowing in Claude Code. I have used it nearly every day for a year
and I still use about six. The three below are the ones that change how the tool feels. The
rest can wait until you hit a wall that needs them.

---

## 1. The context window

**What it is:** Claude's short term memory for the current session. It fills up as you work.

**Why it matters:** when it fills, Claude quietly starts dropping things you told it earlier.
The answers get worse and nothing announces it. Most people conclude the model got dumber and
start writing longer prompts, which fills the window faster.

**What to do:**

- Watch it. The status line shows how much you have used.
- `/compact` summarizes the conversation so far and keeps going with a clean window. Use it
  when you are mid task and do not want to lose the thread.
- `/clear` wipes and starts fresh. Use it between unrelated tasks.
- Clear early rather than late. Once quality drops you have already lost work.

**The tell:** you explain something, and twenty minutes later it does the opposite. That is
not a prompting problem. That is the window.

---

## 2. CLAUDE.md

**What it is:** a plain text file in your project folder. Claude reads it at the start of every
session, automatically, with no prompting.

**Why it matters:** it is the difference between a tool you re-explain yourself to every morning
and one that already knows how you work.

**What to do:**

- Run `/init` to generate a first draft, then edit it by hand. The generated version is a
  starting point, not the answer.
- Write down the things that are true every time: how you want things named, what you never
  want in output, where files belong, what "good" looks like.
- Grow it by correction. Every time Claude does something wrong, do not just fix it in the
  chat. Add the rule to the file. After a few weeks you stop correcting the same things.
- Keep it short enough to actually be read. A page is plenty.

**The test:** if you have explained something to Claude twice, it belongs in the file.

---

## 3. Plan Mode

**What it is:** press `Shift+Tab` and Claude goes read only. It explores, then proposes an
approach, without touching a single file.

**Why it matters:** Claude will build the wrong thing very quickly and very confidently if you
never say what you want. Plan Mode puts a checkpoint between "I have an idea" and "files have
changed."

**What to do:**

- Use it for anything touching more than one file.
- Read the plan. Push back on the part that is wrong. That conversation is cheaper than the
  rewrite.
- Approve, then let it build.

**Think first, build second.** That is the whole idea.

---

## The safety net: `/rewind`

Claude checkpoints before every edit. If you go down the wrong path, `/rewind` rolls back to any
earlier point. An undo button for the whole project.

Learn it before you need it, not during the incident.

---

## Your first week

- **Today.** Pick a real project, not a toy one. Run `/init`. Edit the CLAUDE.md it writes.
- **This week.** Use Plan Mode on every multi file change. Notice when the context window fills.
- **When you hit a wall.** Add exactly one new concept. Not all 23.

The tool is not the hard part. Knowing what good looks like is the hard part.

And never expect it to be a hundred percent right. Eighty or ninety, then you nudge it the rest
of the way. That is the honest ceiling and it is still worth it.
