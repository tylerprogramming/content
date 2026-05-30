# AntiGravity Beginner Tutorial — FILMING PLAYBOOK

> This is your step-by-step guide for what to ACTUALLY DO on screen while recording.
> Includes exact prompts, UI clicks, what to narrate, and pre-built files.

---

## PRE-RECORDING SETUP (Do Before You Hit Record)

### 1. Clean AntiGravity Install
- Make sure AntiGravity is freshly opened (close old projects)
- Set your theme to **dark mode** (looks better on camera)
- Increase font size to **16-18px** so viewers can read (Settings > Editor > Font Size)
- Close any unnecessary panels to keep the UI clean

### 2. Settings to Configure Before Recording
Go to **AntiGravity > Settings > AntiGravity Settings**:

| Setting | Set To | Why |
|---------|--------|-----|
| Review Policy | **Request Review** | So viewers see YOU approving the plan (teaches the workflow) |
| Terminal Execution | **Auto** | Agent asks permission for terminal commands — good for teaching |
| Model | **Gemini 3 Pro** | Best quality for demo, mention it's the default |
| Mode | **Plan Mode** | So it creates the task list first (this is what you want to show) |

### 3. Have These Files Ready
See the markdown files at the bottom of this doc — copy them into the project before filming OR create them live on camera.

---

## FILMING: STEP BY STEP

---

### STEP 1: Create the Project (Show on Camera)

**What you do:**
1. Open AntiGravity — it shows the welcome screen
2. Click **"Open Folder"** (bottom of the left sidebar, or File > Open Folder)
3. Navigate to Desktop (or wherever) → Click **"New Folder"**
4. Name it `expense-tracker` → Click **Open**
5. You now have an empty project — the file explorer on the left is empty

**What you say:**
> "Alright, we've got a completely empty folder. No files, no code, nothing. We're going to build an entire app from scratch just by talking to AntiGravity."

**Screen time:** ~30 seconds

---

### STEP 2: (Optional but Recommended) Drop in a Product Design Doc

**Why do this:** It gives AntiGravity more context and produces a MUCH better first result. It also teaches viewers a pro tip right away.

**What you do:**
1. In the chat sidebar on the right, type this prompt:

```
Hey, I want to build a personal expense tracker dashboard. Before we start coding, can you create a product design document for me? Save it as productdesign.md in the project.

Here's what I want:
- A single-page web app with a clean, modern dark-mode design
- An input form to add expenses (amount, category, date, description)
- Categories: Food, Transport, Entertainment, Shopping, Bills, Other
- A summary card showing total spending this month
- A pie chart breaking down spending by category
- A bar chart showing daily spending for the last 7 days
- A scrollable list of recent transactions
- Use React with Tailwind CSS
- Make it look polished and professional — think glassmorphism style
```

2. AntiGravity will create a `productdesign.md` file on the left
3. Click on it — quickly show viewers what it created
4. "This is our blueprint. Now the AI knows exactly what we're building."

**What you say:**
> "Pro tip — before you ask it to build anything, have it create a product design doc first. This gives it a clear blueprint to follow and you'll get way better results on the first try."

**Screen time:** ~1-2 minutes

---

### STEP 3: The Build Prompt (THE MAIN EVENT)

**What you do:**
1. In the chat sidebar, type this prompt:

```
Awesome, now let's build this. Go ahead and build the full expense tracker app based on the product design document. Follow the productdesign.md spec exactly.

Make sure:
- It runs locally with npm
- The design is polished and dark-mode by default
- Charts are interactive
- The app is fully functional — I should be able to add expenses and see them reflected in the charts immediately
```

2. **Hit Enter / Submit**

**What happens next (and what to narrate):**

#### Phase 1: Task List Appears
AntiGravity will generate a **Task List artifact** in the chat. This is a structured breakdown of everything it plans to do.

**What you say while this appears:**
> "Watch this — before it writes a single line of code, it creates a plan. This task list breaks down everything it's going to do, step by step. You can see it's planning the project structure, the components, the charts, the styling — all of it."

> "This is one of the most important features. You're not just blindly letting AI write code. You can review the plan, leave comments if something's wrong, or approve it."

**What to point at on screen:**
- Hover over the task list items so viewers can read them
- Point out that each step has a checkbox/status

#### Phase 2: Implementation Plan
After the task list, AntiGravity may create an **Implementation Plan artifact** — a more detailed architectural breakdown.

**What you say:**
> "It's also creating an implementation plan — this is the deeper architectural thinking. What tech to use, how the components connect, file structure. Click on it if you want to review."

#### Phase 3: Approve & Let It Build
AntiGravity will ask for your approval or show a **"Proceed"** button.

**What you do:**
1. Click **Proceed** / **Approve** (or type "Looks great, go ahead!")
2. Now watch the magic happen

**What you say:**
> "This looks solid to me. Let's let it cook."

#### Phase 4: Watch It Auto-Build (THE MONEY SHOT)
AntiGravity will now:
- Create files in the left panel (you'll see them appear one by one)
- Run terminal commands (npm init, install packages, etc.)
- Write code across multiple files
- The terminal at the bottom shows commands executing

**What you say while it builds (fill the dead air):**
> "Look at the left panel — it's creating the file structure. You can see the components folder, the styles, the chart library being installed..."

> "Down in the terminal, it's installing the packages it needs. React, Tailwind, Chart.js — all automatically."

> "Now it's writing the actual component code. Each file it creates, you can click on and see the code if you're curious. But you don't NEED to understand any of it."

> "This is what I mean by 'agent-first' — you're not writing code, you're directing an AI team."

**Pro tip for filming:** Speed this up in editing if it takes more than 60-90 seconds. Use a time-lapse / fast-forward effect with music.

**Screen time:** ~2-3 minutes (cut down in editing)

---

### STEP 4: Preview the App

**What you do:**
1. Once it's done building, type in chat:

```
Open this in the local preview browser so I can see it
```

2. AntiGravity will run `npm start` or `npm run dev` in the terminal
3. The **built-in browser panel** opens showing your app (or it opens in your default browser)
4. If it opens in external browser, that's fine too — show both

**What you say:**
> "Alright, moment of truth. Let's see what it built."

> [App loads] "Look at that. We went from an empty folder to a fully working expense tracker in about 3 minutes. Dark mode, glassmorphism cards, charts — all of it."

**What to demo on screen:**
1. **Add an expense:** Click the form, type Amount: 45, Category: Food, Description: "Lunch with team", hit Add
2. **Watch the charts update:** "See how the pie chart just updated? And the total spending card? It's all wired up."
3. **Add 2-3 more expenses** in different categories so the pie chart looks interesting
4. **Scroll the transaction list:** "Every expense I add shows up here"
5. **Point out the bar chart:** "Daily spending over the last 7 days — fully interactive"

**Screen time:** ~1-2 minutes

---

### STEP 5: Iterate (Show the Power of Conversation)

**What you do — Prompt 1 (Design Tweak):**

```
The cards look good but can you add more of a glassmorphism effect? I want frosted glass backgrounds with subtle borders and a slight blur effect. Also bump up the spacing between sections.
```

- Wait for it to update
- Refresh the preview
- Show the before/after (if you can do a quick screen comparison in editing, even better)

**What you say:**
> "Don't like the design? Just tell it. You don't need to know CSS — describe what you want in plain English."

**What you do — Prompt 2 (Add Feature):**

```
Can you add a "Delete" button on each transaction in the list? When I click it, it should remove the expense and update all the charts.
```

- Wait for it to implement
- Demo clicking Delete on a transaction
- Show the charts updating

**What you say:**
> "Need a new feature? Just ask. Watch — I just added delete functionality in 30 seconds."

**Screen time:** ~2 minutes

---

### STEP 6: Quick Rules Overview (Teach the Pro Concept)

**What you do:**
1. Click the **three dots (...)** in the top-right of the chat panel
2. Click **"Customizations"**
3. Show the **Rules** section
4. Click **"+ Global"** to show where global rules go (GEMINI.md)
5. Either paste in the example below or just describe it

**What you say:**
> "Before I let you go — one thing that separates beginners from power users. See this? These are Rules. Think of them as permanent instructions for the AI."

> "For example, I can set a global rule that says 'always use dark mode, always use TypeScript, always add error handling.' Every single project I create from now on will follow these rules automatically."

> "You've got three levels — global rules that apply everywhere, workspace rules for specific clients or projects, and project-level rules. Set these up once and it will save you hours."

**Screen time:** ~1 minute

---

### STEP 7: Tease Manager View

**What you do:**
1. Press `Cmd + Shift + M` (Mac) or `Ctrl + Shift + M` (Windows) to switch to **Manager View**
2. Show the Agent Manager interface briefly
3. Show that you could spin up multiple agents

**What you say:**
> "And here's where it gets really crazy. This is the Agent Manager. Instead of one AI agent, you can run five, ten agents all at the same time — one designing, one building features, one testing. It's like having an entire dev team."

> "But that's a whole video on its own. I'll cover that next — make sure you're subscribed."

**Screen time:** ~30 seconds

---

## MARKDOWN FILES TO HAVE READY

### File 1: Global Rules (for the rules demo)
**Location:** Show this in the Customizations > Global Rules section
**You don't need to save this as a file** — just paste it into the Global Rules editor on camera, or have it pre-loaded.

```markdown
# Global Development Rules

## Persona
You are a senior full-stack developer. Write clean, production-quality code.

## Tech Defaults
- Always use React with TypeScript for frontend projects
- Use Tailwind CSS for styling
- Use modern ES6+ syntax
- Default to dark mode for all UI designs

## Code Quality
- Add meaningful comments only where logic isn't obvious
- Always handle errors gracefully with user-friendly messages
- Never leave console.log statements in production code

## Design Standards
- Use a consistent spacing system (multiples of 4px)
- All interactive elements must have hover states
- Prefer glassmorphism and modern UI patterns
- Ensure text is readable (minimum contrast ratio 4.5:1)

## Definition of Done
- App runs without errors
- All features from the spec are implemented
- UI is polished and responsive
- Code is clean and well-structured
```

### File 2: Product Design Doc (created by AntiGravity during filming)
This gets created in Step 2 — AntiGravity generates it for you. But if you want a fallback, here's what it should roughly contain. **You should NOT need to manually create this** — let AntiGravity make it live on camera.

### File 3: Project Rules (optional — for showing workspace rules)
**Location:** `expense-tracker/.agent/rules/project-rules.md`
**Only show this if you have time** — it's a nice bonus but not critical for the beginner video.

```markdown
# Expense Tracker Project Rules

## Stack
- React 18+ with TypeScript
- Tailwind CSS for styling
- Chart.js or Recharts for data visualization
- Local storage for data persistence (no backend needed)

## Design
- Dark mode only
- Glassmorphism card style
- Color palette: deep navy background, frosted white cards, accent colors for categories

## Categories
Food, Transport, Entertainment, Shopping, Bills, Other

## Component Structure
- Keep components small and focused
- One component per file
- Group by feature, not file type
```

---

## TIMING CHEAT SHEET

| Section | Target Time | Running Total |
|---------|------------|---------------|
| Hook (show finished app) | 0:30 | 0:30 |
| What is AntiGravity | 1:00 | 1:30 |
| Download & Setup | 1:00 | 2:30 |
| Create empty project | 0:30 | 3:00 |
| Product design doc prompt | 1:30 | 4:30 |
| Build prompt + task list + approval | 1:30 | 6:00 |
| Watch it auto-build (time-lapse) | 1:00 | 7:00 |
| Preview & demo the app | 1:30 | 8:30 |
| Iterate (design + feature) | 2:00 | 10:30 |
| Rules overview | 1:00 | 11:30 |
| Manager View tease + CTA | 1:00 | 12:30 |
| **TOTAL** | **~12:30** | |

---

## ON-CAMERA TIPS

### While AntiGravity is Building (Fill the Dead Air)
- Narrate what's happening in the file explorer: "Look, it just created the components folder..."
- Point at the terminal: "It's installing Chart.js for our pie chart..."
- Zoom into specific files briefly: "If you're curious, here's the actual React code..."
- Talk about the concept: "This is called vibe coding — you describe what you want, AI builds it"

### If Something Goes Wrong (It Will)
- **Don't panic.** This is GREAT content. Say: "See? It's not perfect — but watch how easy it is to fix."
- Just type what's wrong: "The pie chart isn't showing. Can you fix that?"
- AntiGravity will debug and fix it — this shows the iterative process
- **Honestly, a small bug that gets fixed makes the video MORE relatable and trustworthy**

### Energy & Pacing
- Keep your energy high during the build reveal and demo
- Slow down slightly when explaining concepts (rules, task list)
- Cut aggressively in post — remove all dead air where you're just waiting
- Use picture-in-picture (your face in corner) during screen recordings

### Visual Moments to Capture
- [ ] Empty folder → first files appearing (satisfying)
- [ ] Task list appearing for the first time
- [ ] The app loading in the preview browser (big reveal moment)
- [ ] Adding an expense and watching charts animate
- [ ] Before/after of design iteration
- [ ] Manager View with multiple agents (tease shot)
