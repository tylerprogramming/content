# 053 - The 5 agents, production-grade (make them REALLY good)

The bar: every agent has to make a viewer think "I need that," not "cute demo." The difference is
always the same move - the agent SYNTHESIZES or DECIDES, it does not just list. Below, each agent's
real instruction file, the upgrade that makes it impressive, the on-camera wow, and the honest limit.

**Cross-cutting quality rules (put these in every agent's file so they don't embarrass you on camera):**
- Ground everything. Only state what the tools actually returned. If a field is missing, say so, never invent.
- Handle empty gracefully ("no action emails today" is a valid, good answer).
- One clear output format every time, so it is skimmable in 5 seconds.
- Say the limit out loud in the output when relevant ("drafted, not sent").

---

## Agent 1 - Morning Briefing (the cold-open payoff)

**Tools:** Gmail (read), Google Calendar (read), ClickUp (read).

**The upgrade (this is what makes it not-generic):** it does NOT summarize each source separately.
It **cross-links them** and opens with the single most important thing. A summary lists; a good
briefing connects the email to the meeting to the task and tells you what to do first.

**Instruction file (`~/.claude/skills/morning-briefing/SKILL.md`):**
```
Write my morning briefing. Use my Gmail (last 24h), my Google Calendar (today), and my open
ClickUp tasks. Ground every line in what the tools return; never invent.

Output exactly this shape:
FIRST THING: the single most important action for today, one sentence, with why.
WHAT HAPPENED: 3-5 bullets from overnight email that actually matter (skip promo/newsletters).
TODAY: each calendar event, and if an email or task relates to it, link them on the same line.
SLIPPING: open tasks whose due date has passed or is today, oldest first, with how many days over.
If a section is empty, write "nothing" and move on. Keep the whole thing under 200 words.
```

**On-camera wow:** the "TODAY" line that reads *"2:00 Sarah (she emailed 20 min ago, moving it to
2:30) - the 'send deck' task for this is 2 days overdue."* That cross-link is the moment people lean in.

**Honest limit:** runs on a schedule (a clock), not on live events. Perfect for a morning brief.

---

## Agent 2 - Inbox Triage + the leash (closes the open loop)

**Tools:** Gmail (read + label + draft). Draft-only by design.

**The upgrade:** it reduces the inbox to **"the 2 that actually need you today"** and drafts replies
that pass as Tyler (reads his voice file). And it handles the edge case out loud: the email that
looks like promo but is actually the sponsor. Bucketing is table-stakes; the judgment is the wow.

**Instruction file (`~/.claude/skills/inbox-triage/SKILL.md`):**
```
Triage my last 24h of Gmail. Label each: Action, Waiting, FYI, or Promo.
Rules: Action = needs a reply or a decision from ME. Waiting = I'm blocked on someone else.
FYI = read-only. Promo = marketing/newsletters.
Watch for traps: a real person or a partner/sponsor is NEVER Promo even if it looks automated.
For each Action email, write a draft reply in my voice (read voice.md). Draft only, never send.
Then output: "NEEDS YOU TODAY:" the 1-3 Action emails, one line each, with the draft attached.
If you were unsure on any email, list it under "JUDGMENT CALLS:" with why, so I can correct you.
```

**On-camera wow:** open the drafts folder - real, good drafts sitting there - then the "JUDGMENT
CALLS" line proving it knows what it is unsure about. That self-awareness is the trust beat.

**Honest limit (the leash):** the Gmail connector is **draft-only** - it cannot send, and you would
not let it anyway. You keep the send button. State it plainly; it is the most important line in the video.

---

## Agent 3 - Content Pipeline (the most time saved)

**Tools:** filesystem (edit `status.md`), ClickUp (move task), Gmail/Blotato optional, voice file.

**The upgrade:** it reads the **real published video** (title, description, transcript) and drafts
**platform-native** posts (LinkedIn no hashtags, X punchy, Pinterest keyword-first) in his voice -
not one generic blurb reposted. And it keeps project state in sync in the same run.

**Instruction file (`~/.claude/skills/content-pipeline/SKILL.md`):**
```
A video just went live. Input: its YouTube URL and package folder.
1. Pull the video's title + description. Update status.md: mark it LIVE with the video id and date.
2. Move its ClickUp task to "Published."
3. Draft social posts in my voice (read voice.md), one per platform, each written FOR that platform:
   LinkedIn (no hashtags, teaches), X (short, punchy), Pinterest (keyword-first title), YT community.
   Save them into the package's social/ folder. Draft only - I approve before anything posts.
Report what you changed as a short checklist so I can verify.
```

**On-camera wow:** one command, and status.md edits itself + the ClickUp card slides to Published +
a folder of on-brand, per-platform drafts appears. "Ten little steps I hated, gone."

**Honest limit:** it drafts posts; you approve before publishing. Nothing auto-posts.

---

## Agent 4 - Calendar (small, used daily)

**Tools:** Google Calendar (read + create).

**The upgrade:** it books against **your real rules**, not just "next free slot." Protect mornings,
batch recording on weekends, no back-to-back, right timezone. It books like an assistant who knows you.

**Instruction file (`~/.claude/skills/book-time/SKILL.md`):**
```
Book me a {duration} block for {purpose} this week. My rules:
- Mornings before 11 are deep-work, do not book over them unless I say so.
- Recording sessions go on Sat or Sun by default.
- Never schedule back-to-back; leave 15 min around existing events.
- Always America/New_York.
Find the best slot that fits, create the event, and tell me the one you picked and why.
If nothing fits the rules, say so and offer the closest option instead of forcing it.
```

**On-camera wow:** you ask once, it picks Saturday 10am (not the literal next gap) *because* it knows
recording goes on weekends. Small, but it reads as genuinely smart.

**Honest limit:** it proposes and books; glance at it. It is not reading your energy, just your rules.

---

## Agent 5 - The Research Subagent (turns one worker into a team)

**Tools:** web search/fetch, runs as a background Claude Code subagent.

**The upgrade:** it returns a **decision-ready brief** (recommendation + 3 bullets + sources), not a
data dump - and it runs in the background while the main agent keeps working. Parallelism + usable output.

**Instruction (spawned from the main agent):**
```
Research {topic} in the background. Return ONLY: a one-line recommendation, 3 supporting bullets,
and the sources. No preamble, no essay. Then stop. I'm working in the main window meanwhile.
```

**On-camera wow:** both windows on screen - the subagent churning on the right, you still working on
the left - then it drops a tight brief, not a wall of text. "One assistant becomes a team."

**Honest limit:** subagents are great for bounded jobs (research, a summary); do not hand one an
open-ended task with no clear "done."

---

## How to prove they're real (optional, strongest possible flex)
Before filming, actually run each once on real data and screen-record the true output. A real briefing
with real names beats any staged one. I can dry-run the briefing + triage logic live against your
connected Gmail/Calendar/ClickUp right now to pressure-test the output quality - say the word.
