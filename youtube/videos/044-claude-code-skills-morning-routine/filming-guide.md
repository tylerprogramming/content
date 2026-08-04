# Filming Guide - 044 Claude Code Skills Morning Routine

The do-this-click-that version. You should be able to follow this without reading the script.

**Film this in the morning.** Not as a gimmick - the skills pull live data, and an actual overnight backlog of email and community activity is the entire proof. Filming at 4pm with an empty inbox kills the video.

---

## Pre-recording setup

### The night before

- [ ] **Do not check email, Skool, or YouTube Studio.** Let the backlog build. This is the most important prep item on the list.
- [ ] Verify the skill count: `ls ~/.claude/skills | wc -l` - it was **51** on 2026-08-02. Write down the real number, you say it out loud twice.
- [ ] Confirm all three skills authenticate cleanly. Run each once tonight so you find broken OAuth tonight, not on camera:
  - `/gmail unread from the last 24 hours`
  - `/skool community health`
  - `/yt-analytics`
- [ ] If any of them prompt for re-auth, do it now.
- [ ] Decide the redaction plan (see below) and write it down.

### Terminal setup

- [ ] Font size up. Test by viewing your monitor from across the room - if you can't read it there, mobile viewers can't read it at all.
- [ ] Clear scrollback: `clear`
- [ ] Close every other tab and window. No Slack, no notifications.
- [ ] Turn on Do Not Disturb.
- [ ] Hide the desktop, hide the dock if it's cluttered.
- [ ] Editor ready in a second window with `~/.claude/skills/gmail/SKILL.md` already open but not focused.

### Redaction plan - decide before you record

| What's on screen | Call |
|---|---|
| Email sender names + subjects | Blur senders in post, leave subjects. Subjects carry the "it sorted this" proof. |
| Skool member names | Blur names, **leave every count visible.** The counts are the proof. |
| YouTube analytics numbers | Leave everything. This is the most credible screen in the video. |
| Anything with a client name, invoice, or password | Don't open it. Plan around it. |

Blur in the edit, never by swapping in a fake account. The moment you use a demo account you've made the same video as everyone else.

---

## Step 1: The cold open (0:00 - 0:35)

**What you do.** Terminal fullscreen, no face on camera yet. Camera rolling before you touch the keyboard.

**Type this live - do not paste:**
```
/gmail unread from the last 24 hours
```

> "This is my actual morning."

Hit enter.

> "That's my real inbox. Not a demo account."

**What happens next.** It takes 20-45 seconds. That's your dead air and it's already scripted:

> "While that runs - I used to do this by hand. Open Gmail. Open Skool. Open YouTube Studio. Three tabs, about twenty minutes, every single morning. Before I'd done one thing that actually mattered. Now it's three commands. And by the end of this video, you'll have built one yourself. Without writing any code."

**Then cut to your face for the first time** and say "Let's go."

**Why typing beats pasting:** the audience needs to see a human hand doing a thing a human could do. Pasting reads as pre-baked.

---

## Step 2: The confession (0:35 - 1:20)

**What you do.** Face on camera, then cut to terminal.

```
ls ~/.claude/skills | wc -l
```

Then:
```
ls ~/.claude/skills
```

Let the list scroll. It should look slightly absurd. That's the point.

> "Quick confession. I've built [REAL NUMBER] of these things. I use three of them before nine in the morning."

**Then open a SKILL.md.** Second window, already open:
```
~/.claude/skills/gmail/SKILL.md
```

Scroll slowly. Don't explain the syntax yet.

> "A skill is not code. It's a text file. That's the whole thing."

**Pause here.** Three full seconds of silence. This is the unlock for a non-technical viewer and it needs air.

> "If you can write an email, you can write one of these."

---

## Step 3: Skill 1, email (2:00 - 5:15)

**What you do.** Back to the terminal where the cold-open output has now landed. Scroll through it.

**Point at the categories on screen.** Narrate what it sorted, not that it sorted.

> "Anyone can ask an AI to read their inbox. The skill is the instructions for what to *do* with it."

**Cut to the SKILL.md, highlight the description line only.** 15 seconds maximum here - the full teardown is Step 6.

> "That line is how Claude knows to reach for this when I say 'check my inbox.' I never have to remember a command name."

**The failure moment.** Look for something genuinely miscategorized - a newsletter marked urgent is the most likely candidate.

- **If something is wrong:** point at it, say what's wrong, say the fix is one line in the text file. Move on. Do not fix it now.
- **If nothing is wrong:** do not fabricate one. Say instead: *"It gets this wrong maybe one in five mornings, usually newsletters. When it does, I add a line to the file."*

**The boundary line** - say this one, it's the best line in the reference video and it's true:

> "This reads my email. It does not send anything. I set it up that way on purpose. And if you're a little uneasy about pointing AI at your inbox - good. Stay uneasy for a while. Let it earn it."

---

## Step 4: Skill 2, community (5:15 - 8:15)

```
/skool community health
```

**What happens next.** Member counts, at-risk members, pending join requests. Roughly 20-40 seconds.

**Dead air filler:** the manual version - clicking to the members tab, sorting by last active, eyeballing it. Be honest that you did it twice a week, not daily.

**Point specifically at the at-risk section**, not the total member count:

> "The total member count doesn't change fast enough to check daily. This does. Who's gone quiet. That's the one where showing up a day early actually changes the outcome."

**If there are zero pending requests:** say so. *"Nothing pending today, which is its own useful answer."* Do not re-shoot for a fuller screen.

---

## Step 5: Skill 3, analytics (8:15 - 10:30)

```
/yt-analytics
```

**What happens next.** Views, CTR, retention, top videos. This is the slowest of the three - budget 45-60 seconds.

**Dead air filler:** why you were worst at doing this one consistently.

**Point at whatever actually moved.** A CTR change, a video over-performing, anything.

> "That's a decision I can make before breakfast. Everything else on the Studio dashboard is a decision for Sunday."

Slow down on "a decision for Sunday."

**Then cut to face for the honesty beat.** Do not cut this for time:

> "This didn't make me a better YouTuber. It made me a consistent one. I check my numbers every day now instead of twice a week and panicking. That's the actual benefit. It's smaller than 'automate your life' and it's real."

---

## Step 6: Build the fourth skill, live (10:30 - 14:00)

This is the segment the video is selling. Do not rush it.

**Type:**
```
use skill-creator to build me a morning skill
```

**What happens next.** skill-creator interviews you. It will ask what the job is, what tools it should use, and when it should trigger. **Show every question.** Do not cut the interview down.

**Your answer to the main question - have this ready but say it naturally, don't read it:**

> Run my gmail check, my skool community health, and my youtube analytics, in that order. Give me one combined summary at the end with anything that needs a decision today.

> "Watch what it's asking. It's not asking me for code. It's asking me what the job is."

**When the SKILL.md is generated, open it fullscreen in the editor.** Spend 45-60 seconds here. Scroll slowly.

**Walk through exactly two things:**

1. **The top part** - highlight the frontmatter block. Say "the top part," then name it. Never say "frontmatter" alone.
   > "Name, and a description. The description is how Claude decides when to reach for this skill. Notice it lists the phrases I might say."

2. **The bottom part** - highlight the body.
   > "The instructions. In English. That's what it does when it runs."

**Do not explain YAML. Do not say "allowed-tools" unless you immediately define it.**

**Then the progressive disclosure explanation** - this is the answer to the most common objection:

> "Here's the thing nobody tells you, which is the answer to 'doesn't having fifty-one of these slow it down?' It doesn't load all of them. It only reads the name and the description at startup - a couple of lines each. It only opens the full file when it actually needs it. So you can have a hundred of these and it costs you almost nothing."

**Run it:**
```
/morning
```

**DEAD AIR WARNING.** This runs all three skills in sequence - expect 90 seconds or more. This is the longest wait in the video. Fill it with the arithmetic:

> "Twenty minutes a day. Times five days. That's an hour and forty minutes a week. That's a video I didn't film."

**If it misfires on the first run - LEAVE IT IN.** Fix it on camera. That is the most valuable 90 seconds in the entire video and no competitor has anything like it. A skill that works on the first try is a demo. A skill you fix on camera is proof.

---

## Step 7: Close (14:00 - 15:00)

Face, direct to camera. No terminal.

> "Pick the one thing you check every single morning. Just one. The tab you open before you've decided to open it. Build a skill for that. Give it twenty minutes. If it sticks for a week, build the second one. That's how I got to three. Not by planning a system - by replacing one tab at a time."

> "The fifty-one skills are the part of my setup that looks impressive. The three are the part that actually changed anything."

**Only say the SKILL.md download line if you're actually publishing the files.** Otherwise cut it.

End clean. No long outro.

---

## Timing cheat sheet

| Step | Section | Target | Running total |
|---|---|---|---|
| 1 | Cold open | 0:35 | 0:35 |
| 2 | Confession + what a skill is | 0:45 | 1:20 |
| - | Roadmap | 0:40 | 2:00 |
| 3 | Skill 1: email | 3:15 | 5:15 |
| 4 | Skill 2: community | 3:00 | 8:15 |
| 5 | Skill 3: analytics | 2:15 | 10:30 |
| 6 | Build the fourth skill | 3:30 | 14:00 |
| 7 | Close | 1:00 | **15:00** |

Research says the 8-22 minute band is where views-per-minute peaked in this category. 15 is comfortably inside it. If you land at 17, that's fine. If you land at 22, cut per the priority list at the bottom of `script.md`.

---

## On-camera tips

**When something breaks.** Do not apologize and do not restart. Say what you expected, say what happened, then fix it. Every competing video in this category is failure-free and that is exactly why they feel staged. Your bugs are the moat.

**Energy.** The #1 video in the research set (241K) is delivered calmly by a guy who looks like he'd rather be reading. Calm is winning in this category right now. Do not push energy - push specificity.

**Pacing.** Three deliberate pauses: after "it's a text file" (Step 2), after "a decision for Sunday" (Step 5), and after "one tab at a time" (Step 7). Count to three each time. It will feel far too long and it will look right.

**The word you must not use.** "Simply." Also "just." To a non-technical viewer, both translate to "you should already understand this."

**Visual moments worth catching:**
- The `ls ~/.claude/skills` list scrolling past - it looks absurd and that sells the confession
- The SKILL.md fullscreen at Step 6 - your single most screenshot-able frame
- The `/morning` combined output landing - the payoff shot for the thumbnail and for the Shorts cut

---

## Assets to have ready

Both windows open before you hit record:

1. **Terminal** - fullscreen, cleared, large font
2. **Editor** - `~/.claude/skills/gmail/SKILL.md` open in a second window, unfocused

Nothing else needs to be prepared. The whole premise is that this is the setup you already have.

---

## Shorts to pull from this footage

Flag these timestamps in the edit for `/yt-shorts` later:

- **"A skill is not code, it's a text file"** (Step 2) - the single most clippable 20 seconds
- **The progressive disclosure explanation** (Step 6) - answers a real question people have
- **"I built 51, I use 3"** (Step 2) - works standalone as a hook
- **The on-camera fix**, if you get one (Step 6) - the most valuable clip if it happens
