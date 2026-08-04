# Gate: SKILLS

The 17 Claude Code skills that run the content business, as actual files.

## Keyword

`SKILLS`

One word across all four carousels, numbered `SKILLS 1/4` … `4/4` on the CTA slide,
same as how `EDITOR` runs across its five. The four posts were originally drafted
with four different words (SKILLS, BUILD, AUTOPILOT, REAL) pointing at four
different-sounding deliverables. Same asset, so same word, same promise.

## Promise

The 17 skills as real files you can drop in and run, plus where the skills folder
lives on your machine.

That sentence is the promise everywhere: the four carousel captions, the 040
description, the end card, and email 01 of the Skool onboarding sequence. If a
CTA says something else, it is wrong.

## Source posts

| Post | Slug | CTA slide |
|---|---|---|
| 17 text files run my whole business | `claude-skills-system` | SKILLS 1/4 |
| Build your first skill in 2 minutes | `first-claude-skill` | SKILLS 2/4 |
| Some of my skills run while I sleep | `skills-on-a-schedule` | SKILLS 3/4 |
| Everyone fakes these demos | `not-a-demo` | SKILLS 4/4 |

Rendered 2026-07-29, in `platform/instagram/<slug>/`. Nothing scheduled yet.

Supporting the video **"17 Claude Code Skills That Actually Run My Business"**
(`040-claude-code-skills-run-my-business/`, re-recorded 2026-07-31, not published).

## Asset

**Mostly already exists.** The skills repo is public and live, which is the actual
deliverable. What is missing is the page in front of it.

| Piece | State |
|---|---|
| The skill files | ✅ public at `github.com/tylerprogramming/claude-skills` |
| Where the skills folder lives (install note) | ☐ needs writing, one paragraph |
| Skool classroom module | Tyler is handling |
| `free.tylerai.dev/skills/` landing page | ☐ 404s today. Tyler is building it — Hostinger, with CF Pages/Workers already wired to the repo. |

The repo means nobody is blocked. Someone who just wants the files has them in one
click. The page only exists to capture email on the way past, which is worth doing
but is not what they came for.

**Do not put API keys in any of it.** Standing rule. Anything pulled out of
`~/.claude/skills/` for public consumption gets keys stripped and the `~/content/...`
paths generalized before it ships.

## Links

Checked 2026-07-31.

| What | URL | Status |
|---|---|---|
| Skills repo (the asset) | https://github.com/tylerprogramming/claude-skills | ✅ 200 |
| Skool | https://www.skool.com/the-ai-agency | 403 to bots, expected |
| Funnel, existing | https://free.tylerai.dev/youtube/ | ✅ 200 |
| Funnel, this gate | https://free.tylerai.dev/skills/ | ❌ 404, not built |
| The video | not published yet | — |

## DM copy — manual (use this one now)

Every link here is live. Nothing promises something that does not exist.

```
Hey, thanks for commenting.

The skills are all here, they are just markdown files:
https://github.com/tylerprogramming/claude-skills

Drop a folder into ~/.claude/skills/ and it works. That is the whole install.

Do not grab all of them. Pick the one that matches something you already
do every week and run that one first.

If you want the walkthrough and the rest of the setup, it is free in here:
https://www.skool.com/the-ai-agency

And if you get stuck on where the folder goes, just reply. I read these.
```

## DM copy — automated (once `/skills/` exists)

Swap the Skool paragraph for the funnel link so the email capture happens on the
landing page instead of after the join:

```
All 17 skills, the files themselves plus where to put them:

https://free.tylerai.dev/skills/

That is also where the newsletter signup is, if you want the weekly stuff.
```

## Notes

- The DM leads with the repo because that is what the posts were about. Someone who
  only wants the files has them in the first three lines and never clicks the
  funnel. The ones who want the walkthrough are the ones worth capturing.
- "Do not grab all of them" is in the DM on purpose. It matches email 01 and it is
  the thing that actually decides whether someone uses this or bounces off it.
- The 040 description currently says "Free skills, prompts, and the full setup are
  in my community." Once this gate is live that line should name the outcome and
  point at the same place, per the `/harut` note on selling the outcome rather than
  the group.
