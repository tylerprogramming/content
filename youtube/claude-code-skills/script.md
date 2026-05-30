# Video Script: Claude Code Skills Changed How I Use AI

---

## [0:00 - 0:30] Hook

> I transcribe YouTube videos in seconds. I journal every day without opening an app, and I also have claude help me script out my videos in seconds, just like I did for this one.
>
> And I built each one of these in about a minute.
>
> They're called skills. Let me show you how they work — and then I'll show you how to build your own.

[SHOW: Quick montage — terminal showing `/resize`, output files appearing, `/transcribe` running, `/journal` conversation. Fast cuts, 2-3 seconds each.]

[NOTE: Energy is high here. Speak with confidence. Each demo clip should be just long enough to see the command and the result.]

---

## [0:30 - 2:30] Demo 1: Resize

> Alright, first one. I make YouTube videos, so I'm constantly needing images in different sizes. Instagram wants a square, Twitter wants a landscape, YouTube wants a thumbnail.
>
> So I built a skill called resize. Watch this.
>
> I open Claude Code, type slash resize, point it at a folder of images, and that's it.

[SHOW: Screen recording — open Claude Code, type `/resize ~/images/photos`, watch it process.]

> And here's what I get back.

[SHOW: Open the output folder `~/images/resized/`. Show the subfolder for one image with all the different sizes — instagram_post, twitter_x_post, youtube_thumbnail, etc.]

> Every social media size. From one folder of images. One command.
>
> I didn't install Photoshop. I didn't open Canva. I just talked to Claude and it handled it.

[NOTE: Let the file list sit on screen for a beat. The visual of 7 perfectly named files does the selling.]

---

## [2:30 - 4:30] Demo 2: Transcribe

> Here's another one. I watch a lot of YouTube videos for research. And I always want the full transcript, not the auto-generated YouTube captions — an actual clean transcript.
>
> So I built a skill for that too.

[SHOW: Screen recording — type `/transcribe` and paste a YouTube URL.]

> Slash transcribe, paste the URL, and it goes.

[SHOW: The script running — downloading audio, sending to Whisper, saving the file.]

> It downloads the audio, sends it to Whisper for transcription, and saves a clean text file with timestamps.

[SHOW: Open the transcript file in the editor. Scroll through it briefly.]

> Full transcript. Timestamped. Saved to a file I can actually use later.
>
> This is one I use constantly. Research, show prep, pulling quotes — it all starts with a transcript.

[NOTE: Don't rush this one. Let the viewer see the actual transcript output. The timestamps make it feel professional and useful.]

---

## [4:30 - 6:00] Demo 3: Journal

> Okay, last demo. This one's personal.
>
> I wanted a simple daily journal. Not an app, not a subscription, not something I'd forget about in two weeks. Just something that asks me a few questions and saves my answers.

[SHOW: Screen recording — type `/journal`.]

> Slash journal. That's it.

[SHOW: Claude asking "What did you accomplish today?" — type a short answer. Then "What are you planning to work on next?" — type another. Then "Any blockers?" — type "nope".]

> It asks me what I got done, what's next, any blockers. I answer. It saves a clean markdown file dated today.

[SHOW: Open `~/content/journal/` folder, show a few dated files. Open today's entry.]

> And if I say slash journal summary, it reads the last week of entries and gives me a recap.
>
> This whole thing took about a minute to set up. And I've used it every day since.

[NOTE: Keep this conversational. The journal skill is the most personal one — let that come through in your tone.]

---

## [6:00 - 8:00] What Is a Skill?

> So what are these things?
>
> A skill is basically a saved way of working with Claude. That's it.
>
> Instead of explaining what you want every single time, you write it down once, and Claude remembers.

[SHOW: VS Code with file explorer open. Navigate to `~/.claude/skills/`.]

> Let me show you what one actually looks like. Here's my skills folder.

[SHOW: Expand the folder — journal, resize, rmbg, transcribe, etc.]

> Each skill is just a folder. And inside each folder is a file called SKILL.md. Let me open the resize one.

[SHOW: Open `~/.claude/skills/resize/SKILL.md`. Show the full file.]

> That's it. That's the whole skill. It's a markdown file.
>
> At the top you've got a name, what arguments it takes, and what tools it's allowed to use. Below that is just instructions. Plain English. "Resize all images in the given folder to social media preset dimensions."
>
> There's no code here. No configuration file. No plugin system. It's a prompt with structure.

[NOTE: Let the file sit on screen. Give the viewer time to read it. This is the moment that demystifies skills — don't rush past it.]

> And some skills have a Python script next to them that does the actual work.

[SHOW: Show `resize_images.py` in the file list. Briefly open it — don't linger.]

> But the skill itself? It's just the markdown file telling Claude what to do and how to do it.
>
> Now here's the thing that makes this really powerful. You can put skills in two places.
>
> If you put a skill inside a project's dot claude folder, it only works in that project.
>
> But if you put it in your home directory's dot claude skills folder — like mine are — it works everywhere. Every project. Every conversation.

[SHOW: Briefly show the path `~/.claude/skills/` in the terminal or file explorer.]

> That's what makes these feel like superpowers. They follow you around.

---

## [8:00 - 9:00] Why Skills Matter

> So why bother?
>
> Because without skills, you're starting from zero every time. You open Claude, you explain what you want, you get a result, and then tomorrow you do it all over again.
>
> With skills, you explain it once. And from that point on, it's one command.
>
> Slash resize. Slash transcribe. Slash journal.
>
> And the best part — you can update them anytime. If your journal skill doesn't ask the right questions, just say "hey, update the journal skill to also ask about my mood." And it does.
>
> You're building tools that grow with you.

[SHOW: Nothing fancy needed here. Talking head or simple text overlay with the three slash commands.]

[NOTE: Keep this section tight. 60 seconds max. The demos already did the convincing — this just names the principle.]

---

## [9:00 - 13:00] Build One Live: Meal Planner

> Alright. You've seen three skills. You know what they look like under the hood. Now let's build one together from scratch.
>
> I've got a folder of recipes here. Just markdown files — ingredient lists, instructions, serving sizes.

[SHOW: Open a folder with recipe files. Click through 1-2 of them briefly.]

> And I want a meal planner. Something that reads my recipes, gives me a plan for the week, and generates a shopping list.
>
> Let's just ask Claude to do it first, and then we'll turn it into a skill.

[SHOW: Open Claude Code in the recipes folder. Type something like: "Give me a meal plan for the week. Tuesday is taco night. Friday is movie night so we need finger food. Sunday is pizza night. Give me a meal plan and a shopping list as separate files."]

> There we go. Meal plan, shopping list, done.
>
> But here's the thing. Next week I'd have to explain taco Tuesday and movie Friday all over again. So let's make this a skill.

[SHOW: Type something like: "I want to turn this into a skill. I want it to remember my weekly rules, track which recipes we've used, and always give me a meal plan and shopping list."]

[NOTE: This is the key moment. Let Claude build the skill. Show the process — it will create the SKILL.md, maybe some supporting structure. Don't fast-forward through this. The viewer needs to see it happen.]

> And there it is. It created a skill.

[SHOW: Open the SKILL.md file that was created. Show the contents.]

> Look at that. It's got my rules in there. Taco Tuesday, movie night finger food, pizza Sunday. It knows where to find my recipes. It knows to generate a shopping list.
>
> Now let's test it.

[SHOW: Clear the conversation or start a new one. Type `/mealplan`.]

> Slash mealplan. That's it. One command.

[SHOW: Watch it generate the plan. Open the output files.]

> Meal plan for the week. Shopping list. All from my actual recipes. And I didn't have to explain anything.
>
> That took — what — a couple minutes? And now I have it forever.

[NOTE: If anything goes wrong during the live build, keep it in. Authenticity matters more than perfection. Just fix it on camera and move on.]

---

## [13:00 - 14:00] Recap + CTA

> So that's skills. You saw three of mine — resize, transcribe, journal. You saw what they look like under the hood. And you watched me build a brand new one in a couple minutes.
>
> The pattern is simple. Do something with Claude. Like the result. Say "make a skill out of this." Done.
>
> If you're using Claude Code and you're not using skills yet, you're working way too hard.
>
> Go build one. Pick something you do all the time. Turn it into a slash command. It'll take you a minute.
>
> If you found this useful, subscribe. I make stuff like this regularly.
>
> Thanks for watching. I'll see you in the next one.

[SHOW: Quick montage callback — same clips from the hook. `/resize`, `/transcribe`, `/journal`, `/mealplan`. Fast cuts.]

[NOTE: End on energy. The callback montage mirrors the opening and gives a sense of completion.]
