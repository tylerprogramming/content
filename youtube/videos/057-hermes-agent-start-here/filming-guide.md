# Filming guide, video 057

The do-this, click-that version of `script.md`. You should be able to film from this without reading the script.

**Runtime target 30:00, hard ceiling 33:00.** The 35 to 60 minute band is the measured dead zone. If you are at 31 when you stop, you are fine. If you are at 36, you cut, you do not publish it long.

---

## Verify before you roll

Three things in the script are NOT verified on this machine. Check each one the morning you film. If it fails, use the fallback in the same row and cut the matching promise from the hook.

| # | Unverified claim | Check it like this | Fallback if it fails |
|---|---|---|---|
| 1 | A bot-to-bot handoff completes end to end and the reply lands | From Researcher's Bot Chat, send a trivial handoff to @packager and wait for the reply to appear. STATE.md says "sent, reply landing not yet eyeballed" and that is still where it stands. | Show the handoff being sent and Packager's files appearing. Cut the PR and the Slack ping. |
| 2 | Coder opens a real PR on tylerprogramming/content | Dry run it the day before against a scratch branch. `gh auth status` is good (tylerprogramming, ssh) but an agent opening a PR unattended has not been filmed. | Coder reviews the newest commit and posts the verdict to Slack. That is verified and it still lands the three-surface story, minus GitHub. |
| 3 | The Slack ping arrives from Coder specifically | Run the dry run all the way to the phone. | Use the 8am card you already have. Say it is a scheduled job, not the handoff. |

Also worth a look before you roll:

- `hermes -p coder cron list` and confirm the last run still says `ok`. Yesterday it was `ok` at 21:05 and it was 15 minutes late on the morning run. If it is late again on camera, that is fine, say nothing.
- `hermes config get auxiliary.background_review` and read what comes back. The script says gemma4:e4b. If it changed, narrate the screen, not the script.
- `ollama list`. The script says `qwen3.8:27b-q8_0` and `gemma4:e4b`. Use the real tags.
- **`coder-reviewer` is a fourth profile and it is a near-duplicate of `coder`.** Either delete it or hide it (right-click the row, Hide Bot) before you shoot the roster. Two bots with the same job in the roster is the kind of thing the comments will notice.

---

## Pre-recording setup

1. **Clean instance for the install take.** `mv ~/.hermes ~/.hermes.real` before, and move it back after. Do not skip the move-back and do not film the mature machine first.
2. Terminal font bumped, prompt cleaned up, 16:9 window.
3. Browser tabs pre-opened: hermes-agent.nousresearch.com, the GitHub repo, ollama.com.
4. Phone on the desk with Slack open, ready for two shots.
5. Close anything with a key, a token or a client name in it.
6. Screen recorder at the same resolution for every take so the seams cut clean.

## Record order

Film out of order. This is the order that works, not the order of the script.

1. **Sections 3 through 5 first, on the clean instance.** Install, hi, memory tier one. This is the only part that needs a virgin machine and you only get one shot at it per reset.
2. **Restore your real profile.** Then sections 6 through 10 on the mature machine, in script order.
3. **Section 11 and the camera pieces.** Anywhere.
4. **The cold open LAST.** You will know by then which of the three unverified beats actually landed, and the hook has to match.

---

## Step by step

### Section 3, install (2:30 to 5:00)

1. Open hermes-agent.nousresearch.com on the clean machine.
2. Show the curl line on screen, do not run it if you are doing the desktop path.
   ```
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```
3. Download for macOS, open it, first launch on camera.
4. Composer model picker. Show the provider list. Pick what you have.
5. Type `hi`.

> While it installs: "Same install whether this is your laptop or a five dollar server, and that matters in about twenty minutes when we get to the scheduled jobs."

### Section 4, memory tier one (5:00 to 8:30)

1. Paste the about-me line. It is in the script, use it word for word, every clause pays off later.
2. Point at "running memory" in the composer.
3. Type: `Given what you now know about me, what would you not bother explaining to me?`
4. `open ~/.hermes/memories/` in Finder.
5. Open USER.md in a text editor. **Count the files out loud on camera.** There are two.
6. Edit one line, save, then ask the agent something that proves it read the edit.

### Section 5, tier two (8:30 to 11:30)

1. **Say the seam.** "I am switching machines, this one is my real setup." Do not hide the cut.
2. New session. Type: `Based on everything you know about how I work, draft the outline for my next video. Don't ask me any questions first.`
3. Let it search. Show the session_search call happening.
4. Screenshot the result before it scrolls.
5. Open the context meter and point at memory's share.
6. Say the caps: about 2,200 characters and about 1,375.

### Section 6, the two settings (11:30 to 13:30)

```
hermes config set memory.write_approval true
/memory pending
hermes config get auxiliary.background_review
```

Approve one staged write on camera so the queue is not theoretical.

### Section 7, skills (13:30 to 17:00)

1. Capabilities panel, Skills tab. Say "Capabilities" out loud once.
2. Open the past title-check chat.
3. Type: `Make this into a skill for checking my titles.`
4. Open the SKILL.md it wrote, in an editor, and scroll it.
5. New chat, `/title-check`.
6. Show `claude-to-hermes-skill-porting`, run it on one real yt- skill from `~/.claude/skills`.
7. Show the four jarvis skills. One line about drift. Move on.

### Section 8, routines (17:00 to 20:30)

1. Routines pane with the two green ones.
2. ```
   hermes -p coder cron list
   ```
3. ```
   hermes -p coder cron run "coder: morning repo check"
   ```
4. Cut to Slack, the card landing.
5. Say the two gotchas: fresh session per run, credentials by command not by chat.
6. ```
   hermes config set GITHUB_TOKEN <dummy>
   ```
   **Dummy value or blur it. Never a real token on screen.**

### Section 9, local (20:30 to 23:00)

```
ollama list
ollama launch hermes
```

Then the offline tool test: "list the files in this folder, read the README, and tell me what this project is." It has to call tools, not just talk.

This is the first section to cut if you are running long.

### Section 10, bots (23:00 to 29:00)

1. Bots tab. Roster with avatars. (`coder-reviewer` hidden or deleted first.)
2. `ls ~/.hermes/profiles/` so they see a bot is a folder.
3. New Agent on camera. Name, Title, Description.
4. CLI equivalent:
   ```
   hermes profile create packager --description "Turns research and a reference transcript into a full video package."
   ```
5. Open Researcher's Bot Chat. Send the handoff:
   ```
   @packager build the package for video 058 from the research you already have. When it's done, ask @coder to open a PR with it on tylerprogramming/content and post the link to Slack.
   ```
6. **Cut away while it works.** Do not film a spinner. Come back to: Packager's files, then the PR on GitHub, then the phone.
7. Say the limit: desktop is where you talk to a bot, Slack is where bots talk to you.

---

## Dead-air fillers

Have these ready, you will need them at least twice.

- While the install runs: the same install works on a five dollar server, and that is the point of the scheduled jobs later.
- While a model loads: why a tool-capable model matters, and that a chat-only model will look like it is working and then do nothing.
- While the handoff runs: a bot is just a folder, so backing one up is copying a directory.
- While a skill is being written: skills are markdown on both sides, which is why the port works at all.

## Timing cheat sheet

| Section | In | Out | Budget | Cut first? |
|---|---|---|---|---|
| Cold open | 0:00 | 0:40 | 0:40 | no |
| What it is | 0:40 | 2:00 | 1:20 | trim to 1:00 |
| Host | 2:00 | 2:30 | 0:30 | no |
| Install | 2:30 | 5:00 | 2:30 | no |
| Memory tier 1 | 5:00 | 8:30 | 3:30 | no, this is the hero |
| Memory tier 2 | 8:30 | 11:30 | 3:00 | no |
| Two settings | 11:30 | 13:30 | 2:00 | trim to 1:30 |
| Skills | 13:30 | 17:00 | 3:30 | no |
| Routines | 17:00 | 20:30 | 3:30 | trim to 3:00 |
| Local | 20:30 | 23:00 | 2:30 | **cut this one first** |
| Bots | 23:00 | 29:00 | 6:00 | no, this is the payoff |
| Close | 29:00 | 30:00 | 1:00 | no |

If you are over at 33, the order to cut is: section 9 whole, then section 6 down to the one `write_approval` command, then the porting beat in section 7. Never cut section 5 or section 10.

## On camera

- "So" to open a thought is your normal speech, keep it.
- Short sentences. You run long when you explain twice.
- Hedge where you are unsure. The drift line in section 7 and the Slack limit in section 10 are the two places the video earns trust.
- No em dashes means nothing on screen either, including slides and overlays.
- You are a software engineer with eight years in. Nothing in this script should sound like an apology for that.
