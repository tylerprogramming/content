# Filming Guide: Claude Code Skills Masterclass (R2)

**Runtime target:** 45-52 min final
**Style:** Authoritative course. Teaching pace in the middle, high energy on the build and the Cowork payoff.
**Format reminder:** Riff from the script, do not read it. Answer on-camera questions on camera. No em dashes spoken. ONE CTA.

---

## THE ONE RISKY THING - read first

The Cowork segment (Chapter 6) is the unique payoff AND the part most likely to break on camera, because the exact skill-invocation UX in the current Cowork build was not fully documented in research. **Do a complete dry run of the Cowork demo before you record anything else.** Confirm:
- A custom skill is loaded and visible in Cowork
- You know exactly how it surfaces and gets invoked there
- It produces a real output on a real (non-confidential) file

If the standup skill feels awkward in Cowork, swap to an office-document skill (Excel/Word/PowerPoint) for the Cowork demo but keep the "same SKILL.md, different surface" message. If Cowork skills aren't behaving, push the shoot. Do not fake it. The whole brand is verifiability.

---

## Pre-Production Checklist

### The day before
- [ ] Delete `~/.claude/skills/standup/` so the build is genuinely from scratch
- [ ] Clear or move anything in `~/notes/standups/`
- [ ] Dry-run the full `/standup` build once off-camera so the body is muscle memory
- [ ] Dry-run the Cowork demo (see above)
- [ ] Open browser tabs: the June 3 2026 claude.com "How we use skills" blog, github.com/anthropics/skills, an awesome-claude-skills list, the superpowers repo
- [ ] Pick the safe SKILL.md to dissect in Chapter 3 (recommend /yt-search or /content). Confirm no secrets visible.

### Morning of
- [ ] Re-check SKILL.md frontmatter field names against live docs (spec evolves in 2026)
- [ ] Restart Claude Code clean
- [ ] Close anything with API keys, private notes, or client work

### OBS / capture scenes
- Face Cam (talking head)
- Terminal (Claude Code session)
- VS Code (editing SKILL.md)
- Finder (skills folders, notes folder)
- Browser (the receipts: Anthropic blog, GitHub)
- Cowork desktop app

---

## Shot-by-shot intent

| Chapter | Primary visual | Energy | Watch out |
|---|---|---|---|
| Cold open | Split: terminal + Cowork + the one file | 10/10 | This is the thumbnail/screenshot moment, nail the composition |
| Why this video | Face cam | 7/10 | "Cooking-show problem" line, deliver with a smile |
| Ch1 What a skill is | Finder + a real SKILL.md + 3-level graphic | 6/10 | Progressive disclosure is the depth most videos skip, do not rush |
| Ch2 Ecosystem | On-screen term cards + cheat-sheet table | 7/10 | The email analogy is the moment. The cheat sheet must be pause-and-screenshot clean |
| Ch3 Anatomy | SKILL.md with each field highlighted | 6/10 | The rewatch section. Methodical is fine. Highlight fields as you name them |
| Ch4 Proof | Anthropic blog + GitHub on screen | 8/10 | Show the actual receipts, do not just talk about them |
| Ch5 Live build | VS Code typing + terminal test | 7 -> 9/10 | The test is the money shot. Answer AskUserQuestion on camera |
| Ch6 Cowork | Cowork app running the skill | 9/10 | The unique payoff. Dry-run it. Same skill, two surfaces |
| Ch7 Best practices | Building list, one principle at a time | 7/10 | Keep it moving, ~40s per principle |
| CTA | Face cam + callback montage | 10/10 | ONE CTA, Skool waitlist |

---

## Energy curve (printable)

```
10 |#                                              #   #
 9 |#                            #        #            #
 8 |#              #             #        #
 7 |#  #        #     #          #     #        #   #
 6 |#         #    #       #
   +------------------------------------------------------
     Hook Why C1  C2  C3  C4   C5build C5test C6 C7  CTA
```

The shape: hook spike, settle into teaching, climb through proof and build, peak again on the test and the Cowork payoff, land the CTA hard.

---

## Continuity rule

The `/standup` skill is the spine of the video. You build it in Chapter 5 and run that same skill in Cowork in Chapter 6. Keep it the same skill the whole way through. That "I built this five minutes ago and now it runs in a totally different app" through-line is the entire payoff.

---

## Common mistakes (Tyler's standing rules)
1. Don't read the script, riff it.
2. Don't rush Chapter 3, the anatomy is why people clicked.
3. Don't fake the Cowork demo, push the shoot if needed.
4. Don't rebuild the content pipeline (yt-search/transcribe/yt), that's 067's video. Reference only.
5. Answer the AskUserQuestion on camera.
6. Don't apologize for a slow demo, cut the pause in edit.
7. Don't re-record a demo that worked, even if the wording was imperfect.
8. No em dashes spoken.
9. ONE CTA.

---

## Post-production
- Run `/chapters` on the final .mp4 to lock real timestamps (the ones in description.md are estimates)
- The cold open and the Cowork moment are your two best short-form clips, mark them while editing
- Likely shorts from this: "Skills vs MCP in 60 seconds" (Ch2), "Build a skill in 5 minutes" (Ch5), "One skill, two apps" (Ch6), "Anthropic runs hundreds of skills" (Ch4)
