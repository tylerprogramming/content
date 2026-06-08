# Filming Guide: I Control My Terminal From My Phone Now

---

## Pre-Recording Setup

### Environment Cleanup
- [ ] Close all unnecessary apps and browser tabs on laptop
- [ ] Clean up desktop — nothing distracting visible
- [ ] Set terminal font size large enough to read on camera (16-18pt)
- [ ] Use a clean terminal theme with good contrast
- [ ] Clear terminal history so it looks fresh
- [ ] Charge your phone fully
- [ ] Enable Do Not Disturb on phone (no notifications during demo)

### App Setup
- [ ] Update Claude Code to latest version (`claude update`)
- [ ] Confirm you have Claude Max subscription ($100/mo) — Remote Control requires it
- [ ] Download Claude app on your phone if you don't have it (iOS or Android)
- [ ] Log into Claude app with the same account as your Claude Code CLI
- [ ] Have a project folder ready with some real files (not an empty directory)

### Test Run
- [ ] Run `/rc` once to confirm it works
- [ ] Scan QR code with phone, confirm session connects
- [ ] Send a test message from phone, confirm it runs on laptop
- [ ] End the session and clear for the real recording

### Physical Setup
- [ ] Have your phone easily visible/accessible for the camera
- [ ] Consider: Phone stand or mount so you can show the screen clearly
- [ ] Optional: Second camera angle for phone screen, or screen record phone and composite in post
- [ ] Location for "walking away" shot — couch, another room, etc.

---

## Filming Steps

### Step 1: Record the Hook [0:00 - 0:30]

**What you do:** Start on the couch (or away from desk) with phone visible.

**What you say:**
> "I'm on my couch right now. My laptop's in the other room. Claude Code is refactoring a file — and it just asked me to approve a change. Watch this."

**On phone — exact actions:**
1. Open Claude app
2. Should already have a session connected (pre-set this up)
3. Show a diff/approval prompt on screen
4. Tap approve
5. Show Claude continuing to work

**Then say:**
> "That's not a remote desktop app. That's not SSH. That's Claude Code running on my laptop — and I'm controlling it from my phone. Let me show you how this works."

**Tip:** For the hook, pre-setup the session and get Claude to an approval prompt before recording. You want this to be snappy — no waiting.

---

### Step 2: Why This Matters [0:30 - 1:45]

**What you do:** Talking head + screen recording of a blocked terminal.

**The narrative — hit these beats:**
1. When you give Claude a big task, it hits permission prompts
2. If you're not there, the agent is BLOCKED — just sitting there waiting
3. Remote Control = your phone becomes the approval window
4. Claude keeps working, you keep living your life

**On screen:** Show terminal with Claude Code hitting an approval prompt, cursor blinking, waiting. This visual sells the problem.

**What you say:**
> "Here's the thing about Claude Code nobody talks about. When you give it a big task, it does the work — but then it hits a permission prompt. And if you're not there? It just sits there. Waiting. The agent is blocked. Remote Control fixes this."

**Tip:** The "blocked agent" is the WHY. Make sure this lands clearly before moving on.

---

### Step 3: Demo Basic Setup [1:45 - 3:30]

**What you do:** Screen recording of terminal + phone.

**On laptop — exact commands:**
```bash
# You should be in a project directory with Claude Code running
/rc
```

**What happens:** QR code and session URL appear in terminal.

**What you say while it loads:**
> "To start Remote Control, I just type slash rc. That's it."

**On phone — exact actions:**
1. Open Claude app
2. Tap the QR scanner (or use camera)
3. Scan the QR code from terminal
4. Wait for session to connect (~2-3 seconds)

**What you say:**
> "Now I've got a QR code and a session URL. Let me scan it with my phone."

**After connected — on phone, type:**
```
List the files in this directory
```

**What you say:**
> "Let me send a message from my phone. See that? The command ran on my laptop. I just triggered it from my phone."

**Show:** Both screens — phone showing the response, terminal showing the activity.

---

### Step 4: Demo Walk Away Workflow [3:30 - 5:30]

**What you do:** This is the money shot — actually walk away from your desk.

**On laptop — exact prompt:**
```
Refactor the authentication module to use async/await instead of callbacks. Update all related files.
```
Then:
```
/rc
```

**What you say:**
> "I've given Claude a big task. Now I'm starting Remote Control."

**On phone:** Scan the QR code.

**What you do next:** Physically walk away from your desk. Go to another room or your couch.

**What you say (while walking or from couch):**
> "Now I can literally walk away. And from my phone, I can see exactly what's happening."

**On phone:** Show Claude working, then show it hitting an approval prompt.

**What you say:**
> "Right there. I can read the diff on my phone, see what it wants to change, and approve it."

**On phone:** Approve the change.

**What you say:**
> "Done. I just approved a code change from my couch. Claude keeps going."

**Then paint the bigger picture (talking head from couch):**
> "Think about this for bigger tasks too. You kick off a database migration at 2am — your phone buzzes, you approve the fix, go back to sleep. Or you're running three sessions at once, monitoring all of them from your phone while you make dinner."

**Tip:** If your project doesn't naturally hit approvals, set up a task that will (refactoring multiple files works well). The approval from the couch is THE moment.

---

### Step 5: Quick Explainer [5:30 - 6:15]

**What you do:** Talking head + simple text overlay. 30-45 seconds MAX.

**Key points to hit (rapid fire):**
1. Session runs on your laptop — files never leave
2. Phone is just a window — only conversation flows through servers
3. Everything encrypted, no inbound ports
4. Auto-reconnects if laptop sleeps

**Visual:** Simple text overlay: "Your Laptop: Files, Code, Tools ← encrypted → Your Phone: Just a window"

**What you say:**
> "Quick explainer. Your session runs on your laptop. Files never leave your machine. Your phone is just a remote window. Everything's encrypted. That's it."

---

### Step 6: Pro Tips [6:15 - 7:30]

**What you do:** Quick screen recordings for each tip.

**Tip 1 — Rename before going remote:**
```
/rename "fixing auth bug"
/rc
```

**Tip 2 — Start fresh in remote mode:**
```bash
claude remote-control
```

**Tip 3 — Get the mobile app:**
```
/mobile
```

**Tip 4 — Enable for all sessions:**
```
/config
```
Navigate to "Enable Remote Control for all sessions" → set to true.

**Tip 5 — Third-party tools (mention only, no demo):**
> "If you want notifications through Discord, Telegram, or email when Claude finishes, check out Claude Code Remote on GitHub."

**Pacing:** 15-20 seconds per tip. Don't linger.

---

### Step 7: Limitations [7:30 - 8:30]

**What you do:** Talking head. Honest, straightforward.

**Key points (in this order):**
1. **Requires Claude Max ($100/mo)** — lead with this
2. Close terminal = session ends
3. ~10 minute timeout if laptop loses internet
4. Can't START from phone, only continue
5. For starting fresh from mobile, use Claude Code on the web (different feature)

**What you say:**
> "One thing to know upfront — you need Claude Max. That's the hundred dollar a month plan. Remote Control isn't on the free or Pro tier."

---

### Step 8: Recap + CTA [8:30 - 9:15]

**What you do:** Talking head, high energy.

**Key points:**
- "Slash rc. Scan QR. Keep working from your phone."
- Callback to the WHY: "Claude is an agent. It wants to keep working. Remote Control means you're always there to unblock it."
- CTA: Subscribe

**End montage:** Quick cuts — `/rc` in terminal, QR code, phone screen, you on couch approving something. Fast cuts, mirrors the opening.

---

## Timing Cheat Sheet

| Section | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:30 | 0:30 |
| Why This Matters | 1:15 | 1:45 |
| Demo: Basic Setup | 1:45 | 3:30 |
| Demo: Walk Away Workflow | 2:00 | 5:30 |
| Quick Explainer | 0:45 | 6:15 |
| Pro Tips | 1:15 | 7:30 |
| Limitations | 1:00 | 8:30 |
| Recap + CTA | 0:45 | 9:15 |

**Total target: ~9-10 minutes** (editing will tighten to ~8 min)

---

## On-Camera Tips

### Energy Flow
- **Hook:** High energy, confidence
- **Why This Matters:** Conversational, relatable — "here's the real problem"
- **Demos:** Focused, clear narration
- **Explainer:** Quick and breezy — don't over-explain
- **Tips:** Punchy, rapid fire
- **Limitations:** Honest, straightforward
- **CTA:** Back to high energy

### Handling the Phone
- Use a phone stand if possible
- If handheld, keep it steady
- Consider screen recording the phone separately and compositing in post
- The approval tap is the key moment — make sure it's visible

### If Something Goes Wrong
- If the QR code doesn't scan: "Let me try that again" — keep rolling
- If the session disconnects: "This actually happens sometimes if your network hiccups — let me reconnect"
- Turn errors into teaching moments

### Visual Moments to Capture
- The QR code appearing in terminal
- Phone screen loading the session
- Split screen: phone + terminal showing same activity
- You physically walking away from desk
- **The "approve from couch" moment** — this is the thumbnail moment
- Terminal sitting blocked at an approval prompt (the problem)

---

## B-Roll Suggestions

- Close-up of phone screen during Claude interaction
- Over-the-shoulder of terminal showing QR code
- Wide shot of you walking away from desk
- Couch shot with phone visible
- Close-up of fingers tapping "approve"
- Terminal with blinking cursor at approval prompt (the "blocked" visual)
