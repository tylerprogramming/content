# Claude Code Tutorial #4 - Context Window Mastery

**Target Length:** 12 minutes
**Style:** Talking head + live terminal demo
**Tone:** Conversational, teacher-to-student, zero jargon without explanation

---

## HOOK (0:00 - 0:30) ~30 sec

Have you ever been working with Claude Code, everything's going great, and then suddenly... the outputs just get worse? Like, noticeably worse. It starts forgetting things you told it. It repeats itself. It ignores your instructions.

That's not a bug. That's context rot. And once you understand why it happens, you'll never get frustrated by it again.

In this video I'm going to show you exactly what the context window is, how to monitor it in real time, and the two commands that fix everything when things start to slip. This is episode four of my Claude Code course for beginners. Let's get into it.

[NOTE: Cut to terminal after "Let's get into it"]

---

## SECTION 1: What Is the Context Window? (0:30 - 2:30) ~2 min

[SHOW: Terminal with Claude Code open, empty conversation]

Okay. So the context window. What is it?

Think of it like Claude's short-term memory. Every time you send a message, and every time Claude responds, all of that text gets added to the context window.

[SHOW: Type a simple prompt like "What is a REST API?" and get a response]

So right now, my prompt is in the context window. Claude's response is in the context window. If I ask a follow-up question, that goes in too. And Claude's answer to that. It all stacks up.

[SHOW: Ask a follow-up: "Can you give me an example?"]

Now here's the thing. The context window has a limit. It's big, but it's not infinite. Think of it like a bucket. Every message is water going in. And at some point, the bucket gets full.

[NOTE: Consider a simple bucket graphic overlay here]

When it gets full, Claude has to start making trade-offs. It can't hold everything perfectly. And that's when things start to get weird.

But don't worry. Claude Code gives you a way to see exactly how full that bucket is. Let me show you.

---

## SECTION 2: Reading the Context Bar (2:30 - 4:00) ~1.5 min

[SHOW: Terminal with Claude Code, point out the bottom bar]

See this bar at the bottom of your terminal? This is your context meter. It tells you how much of the context window you've used.

[SHOW: Zoom in or highlight the context usage indicator]

Right now we're barely using any. We just started. But watch what happens as we keep talking.

[SHOW: Send a few more messages, watch the bar grow]

See it filling up? Every message adds to it. And the more complex your conversation, the faster it fills. If you're asking Claude to read files, those files go into the context too. Big files eat up a lot of space.

Here's the rule of thumb. When you see that bar getting past about 70 or 80 percent, start paying attention. That's when you want to think about managing it. I'll show you how in a minute.

[NOTE: Emphasize this is something to glance at regularly, like checking your gas gauge]

---

## SECTION 3: Context Rot - When Outputs Degrade (4:00 - 6:00) ~2 min

[SHOW: Terminal with a longer conversation, context bar showing high usage]

Okay, now let me show you what context rot actually looks like. I've been having a long conversation here. I've asked Claude to build out several features. Look at the context bar. We're getting pretty full.

[SHOW: Ask Claude to do something it was told about earlier in the conversation]

Now watch this. I'm going to ask it to reference something I told it near the beginning of our conversation.

[SHOW: Claude's response that misses or contradicts earlier context]

See that? It kind of... forgot. Or it got it partially right but missed key details. That's context rot. The early parts of our conversation are getting fuzzy for Claude. It's like when someone tells you a phone number and by the time you get to the last digits, you've already forgotten the first ones.

This is totally normal. It's not Claude being bad. It's just how context windows work. Every AI has this limitation.

[NOTE: Quick talking head moment here]

Now the good news. There are two commands that solve this. And they're dead simple.

---

## SECTION 4: /compact - Your Secret Weapon (6:00 - 9:00) ~3 min

[SHOW: Terminal, same high-context conversation]

Command number one. Slash compact.

[SHOW: Type `/compact` and press enter]

Watch what happens. Claude is going to take the entire conversation and compress it. It keeps all the important stuff. The decisions you made, the files you're working on, what you asked for. But it gets rid of all the fluff. All the back-and-forth that doesn't matter anymore.

[SHOW: Claude compacting, context bar dropping significantly]

Look at that context bar. It just dropped way down. We went from like 80 percent back to maybe 20 or 30. That's a huge amount of room we just freed up.

Now here's the really cool part. You can give compact custom instructions. You can tell it what to focus on when it compresses.

[SHOW: Type `/compact focus on the API changes we discussed`]

So if I type slash compact, and then add "focus on the API changes we discussed," Claude will make sure those API details survive the compression. Everything else gets summarized, but the API stuff stays crisp.

[SHOW: Result of the focused compaction]

This is super useful when you're deep into a specific part of your project and you want to make sure Claude doesn't lose the thread on that particular thing.

[NOTE: Talking head moment]

Let me give you a real example of when to use this. Say you've been going back and forth with Claude for 30 minutes. You've explored a few ideas, gone down some dead ends, and finally landed on an approach. Now you want Claude to actually build it. That's a perfect time to compact. Get rid of all that exploration. Keep the final decision. And now Claude has a clean, focused context to work from.

[SHOW: Ask Claude something after compaction, show improved output quality]

See? The output is better now. More focused. More accurate. Because Claude's context is clean.

---

## SECTION 5: /clear - The Fresh Start (9:00 - 10:30) ~1.5 min

[SHOW: Terminal]

Command number two. Slash clear.

[SHOW: Type `/clear` and press enter]

This one's simpler. It just... wipes everything. Complete fresh start. Like opening a brand new conversation.

[SHOW: Context bar reset to zero, clean terminal]

Zero context used. Claude remembers nothing from before. This is useful when you're switching to a completely different task. Like if you were working on your backend and now you want to work on your landing page. Just clear and start fresh.

[NOTE: Quick talking head]

Here's how I think about it. Compact is like cleaning your desk. You keep the important papers, file away the rest. Clear is like getting a brand new desk entirely. Both are useful. It just depends on the situation.

---

## SECTION 6: Auto-Compaction (10:30 - 11:15) ~45 sec

[SHOW: Terminal]

One more thing you should know. Claude Code actually has auto-compaction built in.

When your context gets to about 85 to 95 percent full, Claude will automatically compact for you. You'll see a message that says something like "auto-compacting conversation."

[SHOW: If possible, trigger auto-compaction or show a screenshot/example]

This is great as a safety net. But I don't recommend relying on it. By the time auto-compaction kicks in, you've already been in the degradation zone for a while. Your outputs have probably already gotten worse.

It's better to compact proactively. When you see that bar hitting 60 or 70 percent, just do it yourself. Stay ahead of it.

---

## SECTION 7: Recap & Next Episode (11:15 - 12:00) ~45 sec

[NOTE: Talking head to camera]

Alright, let's recap. The context window is Claude's short-term memory. It fills up as you talk. When it gets too full, outputs degrade. That's context rot.

Two commands fix it. Slash compact compresses the conversation but keeps the important stuff. You can even tell it what to focus on. Slash clear wipes everything for a fresh start. And auto-compaction is your safety net, but don't rely on it.

Monitor that context bar. Compact proactively. And you'll get way better results from Claude Code.

In the next episode, we're talking about permissions and safety. I'll show you how to make Claude Code faster by pre-approving safe actions. And how to protect yourself from anything dangerous. I'll see you there.

[SHOW: End screen with subscribe button and next episode link]

[NOTE: Add end screen elements in post, 20 seconds]
