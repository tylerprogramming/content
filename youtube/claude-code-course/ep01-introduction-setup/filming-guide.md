# Episode 1 — Filming Guide
## Claude Code Tutorial #1 - Install & Build Your First App

---

## Pre-Recording Setup

### Terminal Prep
- [ ] Clean terminal history: `history -c`
- [ ] Set terminal font size to 16pt+ (readable on mobile)
- [ ] Use a clean terminal theme (dark background, high contrast text)
- [ ] Set terminal window to ~80% screen width (leave room for facecam)
- [ ] Close all other apps, notifications OFF
- [ ] Clear desktop of any personal files

### Environment Prep
- [ ] **Uninstall Claude Code** if already installed: `npm uninstall -g @anthropic-ai/claude-code`
- [ ] Confirm Node.js is installed: `node --version` (install fresh if you want to show the full install)
- [ ] Have console.anthropic.com open in a browser tab, logged in
- [ ] Have a fresh API key ready (or create one during recording)
- [ ] Create a clean working directory: `mkdir -p ~/demo && cd ~/demo`
- [ ] Delete any old `beanbox` folder: `rm -rf ~/demo/beanbox`

### Browser Prep
- [ ] Open tabs: nodejs.org, console.anthropic.com
- [ ] Bookmark bar hidden
- [ ] No personal bookmarks visible
- [ ] Browser zoom at 125%+ for readability

### Recording Prep
- [ ] Screen recording software ready (OBS / ScreenFlow)
- [ ] Microphone tested, levels set
- [ ] Camera on, framing good
- [ ] Record in 4K if possible, export at 1080p

---

## Recording Playbook

### Scene 1: Hook (0:00-0:30)
**Setup:** Terminal open, empty screen
**Say:** "Most people use AI wrong..." (read from hook script)
**On screen:** Terminal with blinking cursor
**Cuts:** At "landing page," quick cut to the finished BeanBox page in browser, then back

---

### Scene 2: What Is Claude Code (0:30-2:00)
**Setup:** Split screen — ChatGPT (left), Terminal (right)
**Say:** Walk through chatbot vs agent comparison
**On screen:**
1. Show ChatGPT briefly (a generic Q&A)
2. Show Claude Code terminal side
3. Can use a simple graphic overlay: "Chatbot = talks | Agent = acts"
**Tip:** Keep energy up here — this is conceptual, easy to lose people

---

### Scene 3: Installing (2:00-4:30)
**Exact commands in order:**
```bash
# Step 1: Verify Node.js
node --version
# Expected output: v20.x.x or similar

# Step 2: Install Claude Code
npm install -g @anthropic-ai/claude-code
# Wait for install to complete (~30 sec)
```
**Browser actions:**
1. Go to console.anthropic.com
2. Navigate to API Keys
3. Click "Create Key"
4. Name it "claude-code-tutorial"
5. Copy key

**Say:** Narrate each step as you do it. "Go to console.anthropic.com..."
**Post-production:** Speed up the npm install output (2x or 3x). Blur the API key.

---

### Scene 4: First Launch (4:30-5:30)
**Exact commands:**
```bash
claude
# First launch — paste API key when prompted
# Claude Code welcome screen appears
```
**Say:** "In your terminal, just type claude. That's it. One word."
**On screen:** The Claude Code welcome screen / init prompt
**Tip:** Let the welcome screen sit for 2-3 seconds so viewers can read it

---

### Scene 5: Terminal Basics (5:30-6:30)
**Exact commands:**
```bash
# Already inside Claude Code from previous scene

# Show /clear
/clear

# Show /exit
/exit

# Restart for the demo
claude
```
**Say:** "Start, stop, clear. Three things. You're a terminal expert now."
**On screen:** Each command and its result
**Tip:** Keep it snappy. This should feel fast and easy.

---

### Scene 6: Live Demo (6:30-9:00) — MOST IMPORTANT SCENE
**Exact commands:**
```bash
# Exit Claude Code first if still in it
/exit

# Create project folder
mkdir beanbox && cd beanbox

# Start Claude Code
claude
```

**Exact prompt to type (type it live, don't paste):**
```
Build me a landing page for a coffee subscription startup called BeanBox.
Include a hero section with a tagline, a "how it works" section with 3 steps,
a pricing section with 3 tiers, and a footer. Modern, clean design.
Use just HTML and CSS in a single file called index.html.
```

**What happens next:**
1. Claude Code processes the prompt
2. It asks permission to create `index.html` — approve it (press `y`)
3. It writes the file
4. It finishes

**After Claude finishes:**
```bash
# Open the file in the browser
open index.html
```

**Say:** Narrate as Claude works. "See, it's creating the HTML... adding the CSS... look at those pricing tiers..."
**On screen:** Claude Code output streaming, then the finished page in browser

**BACKUP PLAN:** If the output doesn't look great:
- Type a follow-up: "Make it look more modern. Use a sans-serif font, add more spacing, and use a dark blue hero section."
- Or re-record with a slightly tweaked prompt
- Have a pre-built version of the page ready as a safety net

---

### Scene 7: Interface Tour (9:00-9:45)
**On screen:** Claude Code running from the previous demo
**Point out:**
1. Context bar at the top
2. An approval prompt (create a new one by asking Claude to make a change)
3. Show a follow-up prompt:
```
Make the hero section background dark blue with white text.
```
**Say:** Explain each element briefly. Don't go deep — save that for later episodes.

---

### Scene 8: Outro (9:45-10:00)
**Say:** "That's episode one..." (read from script)
**On screen:** End screen template with Episode 2 teaser
**Post-production:** Add subscribe button animation, end screen cards

---

## Timing Cheat Sheet

| Section | Start | Duration | Priority |
|---------|-------|----------|----------|
| Hook | 0:00 | 0:30 | HIGH — nail this |
| What Is Claude Code | 0:30 | 1:30 | MEDIUM |
| Installing | 2:00 | 2:30 | LOW — speed up in post |
| First Launch | 4:30 | 1:00 | MEDIUM |
| Terminal Basics | 5:30 | 1:00 | LOW — keep snappy |
| **Live Demo** | **6:30** | **2:30** | **HIGHEST — hero moment** |
| Interface Tour | 9:00 | 0:45 | MEDIUM |
| Outro | 9:45 | 0:15 | LOW |

---

## Common Mistakes to Avoid
- Don't let the install segment drag — speed up in post
- Don't explain code on screen — the audience doesn't care about HTML syntax
- Don't apologize for the terminal — own it, make it feel easy
- Don't forget to blur the API key in post-production
- Don't skip the "open in browser" moment — that's the payoff

## If Things Go Wrong
- **npm error:** Make sure Node.js is actually installed. Run `node --version` first.
- **API key rejected:** Double-check at console.anthropic.com. Create a new one.
- **Claude output is ugly:** Use a follow-up prompt to improve it, or re-record.
- **Terminal looks weird:** Reset with `clear` command, restart terminal if needed.
