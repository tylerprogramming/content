# Video Script: Google AntiGravity in 12 Minutes — Build Your First App

---

## [0:00 - 0:30] Hook

> This is an empty folder. No files, no code, nothing. And in the next 12 minutes, I'm going to turn it into a fully working app — with charts, a database, and a polished UI — without writing a single line of code.
>
> This is Google AntiGravity. It's free. And almost nobody knows how to use it properly.

[SHOW: Screen recording of an empty folder in AntiGravity. Quick flash-forward cut to the finished expense tracker dashboard — dark mode, glassmorphism cards, pie chart, transactions list.]

[NOTE: Energy is HIGH here. Confident, fast. The flash-forward is the money shot — make sure the finished app looks gorgeous before you record the hook.]

---

## [0:30 - 1:30] What Is AntiGravity?

> So what is AntiGravity? In short — it's Google's new AI coding tool. Think of it as having an entire development team that works for you.
>
> You describe what you want in plain English. It plans, builds, tests, and fixes it. All powered by Gemini 3 — Google's most advanced AI model.
>
> And right now, it's completely free.
>
> But here's the important thing — this is NOT a chatbot. This is a full development environment with AI agents that autonomously build your apps. It plans before it codes, it shows you what it's going to do before it does it, and you approve every step.
>
> You're the boss. It does the work. That's the concept.

[SHOW: AntiGravity welcome screen. Maybe a quick pan across the interface — file explorer, chat sidebar, terminal.]

[NOTE: Keep this punchy. No history lesson about when it launched or benchmarks. Just: what it is, why it's different, and that it's free. 60 seconds max.]

---

## [1:30 - 2:30] Download & Setup

> Getting set up takes about 2 minutes. Head to antigravity.google/download. Grab the version for your OS — I'm on Mac.
>
> Open it up. It'll ask you to sign in with your Google account. Do that.
>
> And when it opens, you'll notice it looks a lot like VS Code. That's because it's built on VS Code. So if you've used that before, you'll feel right at home. If you haven't — don't worry, we only need two things.
>
> The file panel on the left. And the chat panel on the right.
>
> Two more quick settings. Click on AntiGravity up here, then Settings.
>
> Set your model to Gemini 3 Pro — that's the best one.
>
> And make sure you're in Plan Mode — not Fast Mode. Plan Mode means it thinks before it builds. That's what we want.

[SHOW: Screen recording — download page, installer, opening AntiGravity, signing in. Then point at left panel and right chat panel. Show Settings > Model selection > Plan Mode toggle.]

[NOTE: Speed this up in editing. Nobody wants to watch an installer progress bar. Show the key moments: download, open, sign in, settings. Cut everything else.]

---

## [2:30 - 3:00] Create Your First Project

> Alright. Let's build something.
>
> Click Open Folder down here. Create a new folder — I'll call it expense-tracker. Open it.
>
> Empty project. Blank slate. Zero files. This is where the magic happens.

[SHOW: File > Open Folder > create `expense-tracker` folder > open it. Show the empty file explorer.]

[NOTE: Quick. 30 seconds. The emptiness of the folder is important — it sets up the transformation.]

---

## [3:00 - 4:30] Product Design Doc (Pro Tip)

> Now, before we ask it to build anything, I'm going to give you a pro tip that most tutorials skip.
>
> Don't just say "build me an app." First, have it create a product design document. This gives the AI a clear blueprint to follow and you'll get way better results on the first try.
>
> Watch this.

[SHOW: Type the following prompt in the chat panel:]

```
Hey, I want to build a personal expense tracker dashboard. Before we start coding, can you create a product design document for me? Save it as productdesign.md.

Here's what I want:
- A single-page web app with a clean, modern dark-mode design
- An input form to add expenses (amount, category, date, description)
- Categories: Food, Transport, Entertainment, Shopping, Bills, Other
- A summary card showing total spending this month
- A pie chart breaking down spending by category
- A bar chart showing daily spending for the last 7 days
- A scrollable list of recent transactions
- Use React with Tailwind CSS
- Glassmorphism style — frosted glass cards, subtle gradients
```

> And just like that — it created a product design doc.

[SHOW: Click on the `productdesign.md` file that appears in the left panel. Quickly scroll through it.]

> You can see it took everything I described and expanded it into a proper spec. Components, color palette, layout — all of it. This is our blueprint. Now the AI knows exactly what we're building.

[NOTE: Don't read the whole design doc on camera. Just show it exists, point at a couple interesting sections, and move on. The point is the concept — plan before you build.]

---

## [4:30 - 6:00] The Build Prompt + Task List + Approval

> Alright, now let's build it. Here's the prompt.

[SHOW: Type in the chat:]

```
Let's build this. Go ahead and build the full expense tracker app based on the product design document. Follow the productdesign.md spec exactly.

Make sure:
- It runs locally with npm
- The design is polished and dark-mode by default
- Charts are interactive
- The app is fully functional — I can add expenses and see them in the charts immediately
```

> Hit enter. And now watch what happens.

[SHOW: AntiGravity generates a Task List artifact in the chat.]

> See this? Before it writes a single line of code, it creates a task list. Look at this — it's planning the project structure, the components, the charts, the styling, the state management.
>
> This right here is what makes AntiGravity different from just asking ChatGPT to write you some code. It PLANS first. You can see every step it's going to take.

[SHOW: Hover over task list items. Point at specific items — "Set up React project", "Create expense form component", "Implement pie chart", etc.]

> And if something looks off? You can leave a comment right here and redirect it. You're the architect. It's the builder.
>
> This looks good to me. Let's let it cook.

[SHOW: Click "Proceed" / "Approve" button, or type "Looks great, go ahead!"]

[NOTE: This is a KEY teaching moment. Spend time here. The task list is what makes beginners feel safe — they can see the plan before committing. Don't rush past it.]

---

## [6:00 - 7:30] Watch It Auto-Build

> And now watch the left panel.

[SHOW: Files start appearing in the file explorer — package.json, src folder, components, styles, etc.]

> See the files appearing? It's creating the project structure. There's our components folder. There's the styles. It's setting everything up.

[SHOW: Terminal at the bottom running commands — npm init, npm install, etc.]

> Down in the terminal — it's installing React, Tailwind, Chart.js. All the packages it needs. Automatically.

[SHOW: Click on a component file briefly to show code being written.]

> And if you're curious, you can click on any file and see the actual code it's writing. But here's the thing — you don't need to understand any of this. That's the whole point.
>
> This is what they call vibe coding. You describe the vibe. The AI writes the code.

[NOTE: This section is mostly watching the build happen. Speed it up in editing — use a time-lapse effect with chill music if the build takes more than 60-90 seconds. Narrate over the time-lapse. Don't let dead air kill the pacing.]

---

## [7:30 - 9:00] Preview & Demo the App

> Alright, it's done. Let's see what it built.

[SHOW: Type in chat:]

```
Open this in the local preview so I can see it
```

> It's starting the dev server...

[SHOW: Terminal runs `npm run dev`. Built-in browser opens, or external browser opens with the app.]

> And there it is.

[NOTE: Pause here for a beat. Let the viewer take in the app. This is the reveal moment.]

> We went from an empty folder to THIS. Dark mode. Glassmorphism cards. Pie chart. Transaction list. All of it. In about 5 minutes.
>
> But does it actually work? Let's find out.

[SHOW: Demo on camera — click through the app:]

> I'll add an expense. Lunch — 45 dollars — Food category.

[SHOW: Fill in the form: Amount: 45, Category: Food, Description: "Lunch with the team", click Add.]

> Look at that. The pie chart updated. The total spending card updated. And it's in my transactions list.

[SHOW: Point at the pie chart, the total card, and the transaction list updating.]

> Let me add a couple more. Uber ride — 28 bucks — Transport. Netflix subscription — 15 — Entertainment.

[SHOW: Add 2-3 more expenses in different categories. Watch the pie chart fill out with different colors.]

> See the pie chart now? Three categories, all color-coded. The bar chart is showing daily spending. Everything is wired up and working.
>
> This is running right here on my laptop. No server, no hosting, no deployment. Just my machine.

[NOTE: Be genuinely excited here. Click around. Add expenses. Show it working. This is the payoff for the viewer — make it feel like a big deal, because it is.]

---

## [9:00 - 10:30] Iterate: Design & Features

> Now here's where it gets really fun. We can just keep talking to it and it keeps improving the app.
>
> Let's say I want the design to be more polished.

[SHOW: Type in chat:]

```
The cards look good but can you add more glassmorphism? I want frosted glass backgrounds with a stronger blur effect and subtle glowing borders. Also add more spacing between sections.
```

> Watch the app update.

[SHOW: App refreshes with updated design. If possible, show a quick before/after comparison.]

> Before. After. I didn't touch a single line of CSS. I just described what I wanted.
>
> What about a new feature? Let's add a delete button.

[SHOW: Type in chat:]

```
Add a delete button on each transaction. When I click it, remove the expense and update all the charts.
```

> And there it is. Delete button on every transaction.

[SHOW: Click delete on one of the expenses. Watch the pie chart and totals update.]

> I just added a fully working delete feature in about 30 seconds. By typing one sentence.
>
> That's the workflow. Build, review, iterate. All in plain English.

[NOTE: Keep the energy up. The speed of iteration is impressive — sell it. If the design change is dramatic, do a side-by-side comparison in editing.]

---

## [10:30 - 11:30] 3 Things Every Beginner Should Know

> Before I let you go — three things that'll save you hours.

### Number One: Rules

[SHOW: Click the three dots `...` in the top-right of the chat panel → Click "Customizations" → Show the Rules section.]

> See this? Rules. Think of these as permanent instructions for the AI.
>
> You can set global rules that apply to EVERY project. Things like — always use dark mode, always use TypeScript, always handle errors gracefully.

[SHOW: Click `+ Global` → briefly show the GEMINI.md editor. You can paste or just describe:]

> Set these up once and every single project you create from now on will follow them automatically. Game changer.

### Number Two: The Task List Is Your Best Friend

> Remember that task list it created before building? Get used to reading it. It's your safety net.
>
> Before the AI writes any code, it shows you the plan. You approve it. If something looks wrong, leave a comment. You're always in control.

### Number Three: Manager View

[SHOW: Press `Cmd + Shift + M` (Mac) to switch to Manager View.]

> Once you're comfortable, there's this. The Agent Manager. Instead of running one AI agent, you can run five, ten, all at the same time. One designing, one building, one testing.
>
> It's like having an entire dev team. But that's a whole video on its own.

[NOTE: Don't explain Manager View in depth. Just show it, say it's powerful, and tease the next video. The viewer needs to subscribe for that one.]

---

## [11:30 - 12:30] CTA + What's Next

> So let's recap. You just watched me go from a completely empty folder to a fully working expense tracker — with charts, categories, a polished UI, and delete functionality — without writing a single line of code.
>
> And AntiGravity is free right now. Go to antigravity.google/download and try it yourself.
>
> If this was useful, hit subscribe. I'm going deep on AntiGravity.
>
> Next up — I'm going to show you how to connect AntiGravity to tools like databases and web scrapers using something called MCP servers. And after that — the setup mistakes that 99% of users make that are costing them time.
>
> Drop a comment and tell me what you want to build with AntiGravity. I'll see you in the next one.

[SHOW: Quick montage callback — empty folder → files appearing → app loading → adding expenses → charts animating → delete working. Fast cuts, 2-3 seconds each. Same energy as the hook.]

[NOTE: End strong. The callback montage mirrors the opening and gives closure. Include an end card with links to the next videos.]
