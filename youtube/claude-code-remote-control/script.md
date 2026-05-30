# Video Script: I Control My Terminal From My Phone Now

---

## [0:00 - 0:30] Hook

> I'm on my couch right now. My laptop's in the other room. Claude Code is refactoring a file — and it just asked me to approve a change.
>
> Watch this.

[SHOW: Phone screen — Claude Code session showing a diff, you tap approve, Claude continues working]

> That's not a remote desktop app. That's not SSH. That's Claude Code running on my laptop — and I'm controlling it from my phone.
>
> Let me show you how this works.

[NOTE: Energy is high. The phone demo should be quick — 5 seconds max. Don't explain it yet, just show the approval. The viewer should be thinking "wait, how?"]

---

## [0:30 - 1:45] Why This Matters

> So here's the thing about Claude Code that nobody talks about. When you give it a big task — refactor this file, review this codebase, run and fix tests — it does the work, but then it hits a permission prompt.
>
> "Can I edit this file?" "Can I run this command?"
>
> And if you're not there to approve it? It just sits there. Waiting. The agent is blocked.
>
> That's the real problem. You want to walk away and let Claude work, but it can't keep going without you.

[SHOW: Terminal with Claude Code hitting an approval prompt, cursor blinking, waiting]

> Remote Control fixes this. You scan a QR code, and now your phone is an approval window for your laptop session.
>
> Claude keeps working. You keep living your life. When it needs something, your phone buzzes, you approve it, and it keeps going.
>
> It's the difference between babysitting the terminal and actually letting Claude be an agent.
>
> Let me show you how to set it up.

[NOTE: This is the WHY. Hit this clearly — "unblocking the agent" is the core value. Then move quickly to the demo.]

---

## [1:45 - 3:30] Demo 1: Basic Setup

> Alright, I've got Claude Code running here. I'm in a project folder, just doing normal work.
>
> To start Remote Control, I just type slash rc.

[SHOW: Terminal. Type `/rc` and press enter.]

> That's it. Slash rc.

[SHOW: The QR code and session URL appearing in the terminal.]

> Now I've got a QR code and a session URL. I can scan the code with the Claude app on my phone, or I can open that URL in any browser.
>
> Let me scan it.

[SHOW: Pick up phone, open Claude app, scan QR code. Show the session loading on the phone.]

> And now I'm connected. Same session. I can see everything we were just doing.
>
> Let me send a message from my phone.

[SHOW: Type something simple on the phone like "list the files in this directory". Watch Claude respond on the phone AND see the activity reflected in the terminal.]

> See that? The command ran on my laptop. I just triggered it from my phone.
>
> And watch the terminal.

[SHOW: Terminal showing the activity happening in real-time.]

> It's all synced. I can type from the terminal, type from my phone, type from a browser — doesn't matter. It's all the same session.

[NOTE: This is the "aha" moment. Let the sync sink in. Show both screens if possible — phone and terminal side by side.]

---

## [3:30 - 5:30] Demo 2: Walk Away Workflow

> Okay, but when would you actually use this? Here's my favorite example.
>
> I'm working on something — let's say I asked Claude to refactor a bunch of files. That's gonna take a few minutes. And I know it's going to need approvals along the way.
>
> Instead of staring at my terminal, I go remote.

[SHOW: Terminal with Claude Code. Type something like "Refactor the authentication module to use async/await instead of callbacks. Update all related files." Then type `/rc`.]

> I've given Claude a big task. Now I'm starting Remote Control.

[SHOW: QR code appears. Scan it with phone.]

> Now I can literally walk away.

[SHOW: You walking away from the desk. Go to the couch, another room, etc.]

> And from my phone, I can see exactly what's happening. Claude's working through the files, and when it needs me to approve a change...

[SHOW: Phone screen — Claude is working, then shows an approval prompt for editing a file.]

> Right there. I can read the diff on my phone, see what it wants to change, and approve it.

[SHOW: Approve the change on the phone.]

> Done. I just approved a code change from my couch. Claude keeps going. I'm not blocking it anymore.
>
> Think about this for bigger tasks too. You kick off a database migration at 2am because that's your maintenance window. You're in bed. Claude hits a snag — your phone buzzes, you approve the fix, go back to sleep.
>
> Or you're running three Claude Code sessions in different terminals, each working on a different part of your project. Remote Control on each one. You're monitoring all of them from your phone while you make dinner.
>
> The point is — you're not chained to your desk.

[NOTE: This is the money demo. Actually walk away. The physicality sells it. The 2am and multi-session examples paint a picture without needing to demo them.]

---

## [5:30 - 6:15] How It Works (30 Second Explainer)

> Quick explainer on what's actually happening.
>
> Your Claude Code session runs on your laptop. Your files never leave your machine. Your phone is just a remote window — all that flows through Anthropic's servers is the conversation. The actual code runs locally.
>
> No inbound ports open on your machine. Everything's encrypted. If your laptop sleeps, it reconnects when it wakes up.
>
> That's it. Your code stays on your machine. Your phone is just the remote control.

[SHOW: Simple text overlay: "Your Laptop: Files, Code, Tools ← encrypted messages → Your Phone: Just a window"]

[NOTE: 30-45 seconds MAX. Don't over-explain. Viewers care about using it, not the architecture.]

---

## [6:15 - 7:30] Pro Tips

> Alright, a few tips if you're gonna use this.
>
> Tip one: Rename your session before you go remote.

[SHOW: Terminal. Type `/rename "fixing auth bug"` then `/rc`.]

> When you look at your sessions on your phone, they're listed by name. If you don't rename, good luck figuring out which is which.
>
> Tip two: You can start a fresh session already in remote mode from the command line.

[SHOW: New terminal. Type `claude remote-control`.]

> Useful if you know from the start you'll be going mobile.
>
> Tip three: Get the Claude app on your phone. Type slash mobile in Claude Code.

[SHOW: Terminal. Type `/mobile`.]

> It gives you a QR code to download the app.
>
> And tip four: You can turn this on for ALL sessions by default.

[SHOW: Type `/config` and navigate to the Remote Control setting.]

> In your config, there's a setting to enable Remote Control for every session automatically. Then you're always remote-ready.
>
> Bonus: if you want to go even further, there's an open-source tool called Claude Code Remote that can send you notifications through Discord, Telegram, or email when Claude finishes a task. Search GitHub for "Claude Code Remote" and you'll find it.

[NOTE: Quick hits. 15-20 seconds per tip. The third-party mention is fast — don't demo it, just name-drop.]

---

## [7:30 - 8:30] Limitations

> One more thing. A few limitations to know.
>
> First — you need Claude Max. That's the $100 per month plan. Remote Control isn't available on the free tier or the Pro plan.
>
> If you close your terminal, the session ends. It's running locally, remember? Shut down the laptop, close the window — done.
>
> If your laptop loses internet for more than about 10 minutes, the session times out.
>
> And you can't START a session from your phone. You can only continue one. For starting fresh from mobile, that's Claude Code on the web — different feature, runs in the cloud.

[NOTE: Lead with the price requirement. People need to know this before they try. Keep the rest brisk — builds trust by being honest.]

---

## [8:30 - 9:15] Recap + CTA

> So that's Remote Control.
>
> Start a session on your laptop. Type slash rc. Scan the QR code. Keep working from your phone.
>
> The whole point is this: Claude Code is an agent. It wants to keep working. But it can't if you're not there to approve things. Remote Control means you're always there — even when you're not at your desk.
>
> Go try it. Slash rc. That's it.
>
> If you found this useful, subscribe. I make Claude Code content every week.
>
> Thanks for watching. See you in the next one.

[SHOW: Quick montage — terminal showing `/rc`, QR code, phone screen with Claude, you on the couch approving something. Fast cuts, same energy as the opening.]

[NOTE: End on energy. Callback to the opening — you're on the couch, things are working. Full circle.]
