# Video Script: Claude Code + Remotion: Automate Video Editing with AI

---

## [0:00 - 1:00] CONTRARIAN HOOK

> Every creator I talk to is paying $30 a month for CapCut or Premiere just to add text overlays to their shorts. I haven't opened a video editor in months.
>
> I use Claude Code and a free open-source tool called Remotion to generate animated text overlays, render them from my terminal, and push them straight into my content pipeline. 30 seconds, done.
>
> My name's Tyler. I've built AI automations for Fortune 500 companies and helped a YouTuber with 150,000 subscribers publish over 30 pieces of content a week, some going viral. I run 43 Claude Code skills that automate my entire content pipeline.
>
> Today I'm going to show you my Code-to-Content system. By the end of this video, you'll have animated text overlays for your shorts that you can render in 30 seconds from your terminal.
>
> And if you want the full component library, the templates, and the pipeline setup, I share all of it inside my Skool community. Link's in the description.

[SHOW: Quick montage - terminal rendering a video, the finished animated short playing, then the Remotion Studio preview]

[NOTE: Energy is HIGH. Confident, fast. The 30-second render claim is the hook within the hook. Make sure you have a finished short ready to flash before you record this.]

---

## [1:00 - 2:00] SHOW RESULT FIRST

> Before I show you how to build this, let me show you what we're building.

[SHOW: Open Remotion Studio at localhost:3000. Play one of the existing compositions, like SevenPlatforms or TerminalType]

> This is a YouTube Short I rendered entirely from my terminal. Animated text, smooth transitions, branded colors. No video editor touched this.

[SHOW: Play a second composition, maybe BlotaMCP]

> And this one. Different style, different animations, same system. I've got seven of these compositions built. Each one uses reusable components that I can mix and match.

> Let me show you the component library real quick.

[SHOW: Open the components folder in VS Code - show WordByWord.tsx, SlamText.tsx, HighlightText.tsx, CountUp.tsx, GradientReveal.tsx, StrikeReplace.tsx]

> WordByWord - animates text one word at a time. SlamText - big bold words that slam in. HighlightText - highlights key phrases. CountUp - animated numbers. GradientReveal - text that fades in with a gradient. StrikeReplace - crosses out text and replaces it.

> These are React components. Claude Code built all of them. And once they exist, I can use them in any new composition in seconds.

> Okay. Let me show you how to set this up from scratch.

[NOTE: This section sells the dream before the tutorial. Show the BEST looking compositions. Spend time here, this is what keeps people watching.]

---

## [2:00 - 5:00] SETUP

> Alright, let's start from zero. You need two things. Node.js and Claude Code. If you've got both, we're good.

[SHOW: Terminal - check node version, check Claude Code is installed]

> First, let's create a new Remotion project. Open your terminal and run this.

[SHOW: Type `npx create-video@latest my-video` in terminal]

> That's it. One command. Remotion scaffolds the entire project for you. React, TypeScript, everything wired up.

> Let's see what it created.

[SHOW: `cd my-video && ls` - show the file structure]

> You've got your src folder with your compositions, a package.json, and the Remotion config. Standard stuff.

> Now let's open this in Claude Code.

[SHOW: `claude` in the my-video directory]

> And let's also fire up Remotion Studio so we can preview what we build in real time.

[SHOW: `npx remotion studio` in a second terminal tab - Remotion Studio opens in browser]

> This is Remotion Studio. It's like a local video editor running in your browser. You can preview compositions, scrub through the timeline, and see changes instantly.

[SHOW: Click around Remotion Studio - show the timeline, the preview panel, the composition selector]

> The default template has a simple "Hello World" composition. We're going to replace this with something actually useful.

> One quick thing. If you're on the Remotion website, you'll see they have a skill you can install. But honestly, you don't need it. Claude Code already knows how to work with Remotion projects out of the box. The React components, the composition structure, the rendering commands. It handles all of it.

[NOTE: Keep setup FAST. Nobody watches a tutorial for the install. Get through this in under 3 minutes. Speed up any terminal waiting in post.]

---

## [5:00 - 7:00] FRAMEWORK / CONCEPT

> Okay, before we start building, let me explain how Remotion works. Because once you get this, everything else clicks.

> Remotion is React for video. That's the whole concept. Instead of dragging clips around a timeline, you write React components. Each component is a scene. You compose scenes into a video. And you render it with a single command.

[SHOW: Simple diagram or whiteboard - "React Components -> Compositions -> Render -> MP4"]

> Why does this matter for creators? Three reasons.

> One, it's programmatic. You can change text, colors, timing with variables. Want to make 5 versions of the same short with different hooks? Change one string. Render. Done.

> Two, it's reusable. Build a text animation component once, use it in every video forever. That's what my component library is. WordByWord, SlamText, GradientReveal. Build once, reuse forever.

> Three, it's automatable. Since everything is code, Claude Code can generate new compositions, swap text, adjust timing, and render, all from the terminal. No GUI, no clicking, no exporting. Just a command.

[SHOW: Quick terminal demo - `npx remotion render src/index.ts SevenPlatforms out/seven-platforms.mp4` - show it rendering]

> See that? One command. It just rendered a finished MP4. That's the power move.

> And when you pair this with Claude Code's ability to write React components, you get an AI that can build video content for you. Not generate blurry AI video. Actually write the code that produces clean, professional animated content.

> Okay. Let's build something.

[NOTE: This is the conceptual section. Keep it visual. The diagram helps. The terminal render command is the key moment, make sure the render completes successfully before filming.]

---

## [7:00 - 12:00] LIVE BUILD - Part 1: Text Overlay Component

> Here's what we're building. An animated text overlay for a YouTube Short. The kind of thing you'd put over a talking head clip. Big text that slams in word by word, holds for a beat, then transitions out.

> Let's ask Claude Code to build it.

[SHOW: In Claude Code, type the prompt:]

```
Create a new Remotion composition called "HookOverlay" for a 9:16 YouTube Short (1080x1920).

It should:
- Display a hook phrase word by word with a slam animation
- Each word should scale up from 0 to full size with a slight bounce
- Use white text with a subtle drop shadow on a transparent background
- Hold the full phrase for 2 seconds at the end
- Total duration: 5 seconds at 30fps (150 frames)
- The hook text should be configurable as a prop

Use the same animation style as my existing SlamText component.
```

> Watch what Claude does here.

[SHOW: Claude Code reading the existing SlamText component, understanding the animation pattern, then creating a new HookOverlay.tsx file]

> See that? It didn't start from scratch. It read my existing SlamText component, understood the animation pattern, and used it as the foundation for the new composition. That's the beauty of having a component library. Claude Code builds on top of what already exists.

> Let's check the code real quick.

[SHOW: Open HookOverlay.tsx - scroll through it briefly, point at key parts: the spring animation, the word-by-word mapping, the configurable text prop]

> Nice. Spring animation on each word, configurable text prop so we can swap the hook without touching the code.

> Now let's register it as a composition.

[SHOW: Claude Code updates Root.tsx to add the new HookOverlay composition]

> And let's preview it in Remotion Studio.

[SHOW: Refresh Remotion Studio, select HookOverlay from the composition dropdown, play it]

> There it is. Word by word, slam animation, clean. And this took, what, 60 seconds?

[NOTE: The preview moment is critical. Make sure this looks GOOD before filming. If the animation isn't smooth, iterate with Claude Code until it is. A janky preview kills the whole video.]

---

## [12:00 - 16:00] LIVE BUILD - Part 2: Full Short Composition

> One text overlay is cool. But a real short needs more. Let's build a complete composition with multiple scenes.

[SHOW: In Claude Code, type:]

```
Create a new composition called "ShortDemo" that's a complete YouTube Short (1080x1920, 30fps, 30 seconds).

Scene structure:
1. (0-3s) Hook text - use the WordByWord component: "Stop paying for video editors."
2. (3-6s) Problem text - use SlamText: "CapCut. Premiere. $30/month."
3. (6-9s) Solution text - use GradientReveal: "Remotion + Claude Code = Free"
4. (9-15s) Feature list - use HighlightText to show 3 bullet points one at a time:
   - "Animated text overlays"
   - "Render from terminal"
   - "Reusable components"
5. (15-20s) CountUp showing "30 seconds to render"
6. (20-25s) StrikeReplace: cross out "$360/year" and replace with "Free"
7. (25-30s) CTA using SlamText: "Link in bio"

Use a dark gradient background (#0a0a0a to #1a1a2e).
Add smooth transitions between scenes.
```

> Now watch Claude Code work through this. It's going to pull from the existing component library, compose them into scenes, and handle the timing.

[SHOW: Claude Code creating ShortDemo.tsx, importing from components, building each scene with the right frame offsets]

> Look at the imports. WordByWord, SlamText, GradientReveal, HighlightText, CountUp, StrikeReplace. Every component I've already built. Claude Code is just wiring them together.

[SHOW: Scroll through the composition code, point at the Sequence components and their frame offsets]

> Remotion uses these Sequence components to control timing. Each one gets a "from" frame and a duration. So scene 1 starts at frame 0 and runs for 90 frames, which is 3 seconds at 30fps. Scene 2 starts at frame 90. And so on.

> Let's preview it.

[SHOW: Open Remotion Studio, select ShortDemo, play the full 30-second composition]

> Okay. Look at that. Six different animation styles, smooth transitions, dark background. And every piece of text in here is a prop I can change with one line of code.

> Want a different hook? Change the string. Want different colors? Change the hex values. Want to make 5 versions for A/B testing? Duplicate the composition, swap the text.

> This is why programmatic video is so powerful. It's not a one-off. It's a template.

[NOTE: Let the full 30-second composition play uninterrupted at least once. This is the payoff. If any scene looks rough, fix it with Claude Code live on camera, that makes even better content.]

---

## [16:00 - 18:00] LIVE BUILD - Part 3: Render and Automate

> Alright, we've got a composition that looks great in the preview. Now let's render it to an actual MP4.

[SHOW: Switch to terminal]

> One command.

[SHOW: Type `npx remotion render src/index.ts ShortDemo out/short-demo.mp4`]

> That's it. No export menu. No progress bar to watch for 10 minutes. Remotion renders it locally on your machine.

[SHOW: Terminal output showing the render progress, frames being processed]

> And it's done. Let's check it.

[SHOW: Open the rendered MP4 in Finder/QuickLook - play it]

> Clean. Exactly what we saw in the preview. MP4 file, ready to upload anywhere.

> Now here's where it gets really powerful. Since this is just a terminal command, I can script it. I can have Claude Code render videos as part of a larger workflow.

> Let me show you what I mean. In my content pipeline, I have a skill that generates short-form content. It writes the script, picks the hook, and then tells Remotion to render the overlay. All from one command.

> Something like this.

[SHOW: In Claude Code, demonstrate a simple automation flow:]

```
Render the ShortDemo composition but change the hook text to "Claude Code changed everything." and the CTA to "Subscribe for more." Output to out/short-v2.mp4.
```

> Watch. Claude Code opens the composition file, swaps the text props, saves it, and runs the render.

[SHOW: Claude Code editing ShortDemo.tsx to change the text props, then running the render command]

> Version two. Different text. Same animations. Same quality. And it took, what, 30 seconds?

> This is the Code-to-Content pipeline in action. Write once, render infinitely.

[NOTE: The version-swap moment is huge. Show the two MP4s side by side if possible. Same structure, different text. This sells the "reusable" concept better than any explanation.]

---

## [18:00 - 20:00] PIPELINE INTEGRATION + BONUS

> Okay, so you've seen how to build components, compose them, and render from the terminal. Let me show you how this fits into the bigger picture.

> I have 43 Claude Code skills. They handle everything from YouTube research to script writing to SEO to social scheduling. Remotion is the rendering layer.

[SHOW: Quick screen share of the skills directory or a diagram showing the pipeline]

> Here's the flow. My /shorts skill generates 5 short-form scripts per week based on trending research. Each script has a hook, three key points, and a CTA. That's the text.

> Then Remotion takes that text, plugs it into the composition template, and renders 5 animated shorts. Same animation quality, different content each time.

> And then Blotato schedules them across YouTube Shorts, TikTok, and Instagram Reels. One pipeline. 15 pieces of short-form content per week. Without me opening a single app.

> Now here's the bonus use case that I think people are sleeping on.

[SHOW: Open one of the more complex compositions like SevenPlatforms or FiveFeatures]

> These compositions aren't just for shorts. I use them for explainer clips inside my long-form videos too. Need a quick animated graphic showing how a system works? Build a composition. Need a text callout during a tutorial? Build a composition.

> And because they're all React components, I can share them across projects. My component library works in any Remotion project. So if you build a great SlamText animation once, you have it forever.

[SHOW: Play SevenPlatforms or FiveFeatures composition as the bonus example]

> The key insight is this: Remotion turns video content into a software problem. And software problems are exactly what Claude Code was built to solve.

[NOTE: This section ties everything together. Don't rush it. The pipeline diagram or skill directory walkthrough is what separates this from every other Remotion tutorial.]

---

## [20:00 - 22:00] RECAP + WHAT YOU SHOULD DO NEXT

> Alright, let's recap what we built today.

> We started from scratch. Installed Remotion with one command. Opened Claude Code. Built an animated text overlay component in about 60 seconds. Then we composed a full 30-second YouTube Short using six different animation components from the library.

> We rendered it from the terminal. Swapped the text to create a second version. And I showed you how this plugs into a full content pipeline that produces 15 animated shorts per week automatically.

> Here's what I'd recommend you do next.

> Step one, install Remotion. Run that npx create-video command. It takes 30 seconds.

> Step two, build your first component. Start with something simple, like a WordByWord text animation. Have Claude Code build it for you.

> Step three, build three to four more components. SlamText, GradientReveal, CountUp. Once you have a library of five or six components, you can compose full shorts from them like Lego blocks.

> Step four, set up a render script. One terminal command that renders your composition to MP4. That's when it goes from "cool demo" to "actual workflow."

[SHOW: Quick recap montage - the component library, the full composition playing, the terminal render, the two different versions side by side]

---

## [22:00 - 23:00] CLOSE + CTA

> If you want the full component library, the composition templates, and the pipeline setup I use to produce content across seven platforms, I share everything inside my Skool community. Templates, skills, the whole system. Link's in the description.

> Drop a comment and let me know what kind of content you'd automate with this setup. I read every single one.

> If this was helpful, hit subscribe. I post tutorials on Claude Code and AI automation every week. And I'll see you in the next one.

[SHOW: End screen with subscribe button and link to Skool community]

[NOTE: Keep this tight. 60 seconds max. Don't repeat what they already know. The Skool CTA should feel like a natural extension, not a sales pitch.]
