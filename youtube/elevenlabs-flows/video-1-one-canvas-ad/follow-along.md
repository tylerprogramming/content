# Follow Along: Build a Full Video Ad in One Canvas with ElevenLabs Flows

> This is the exact recipe from the video. Keep it open on the side and build alongside me.
> Flows in ElevenCreative is currently in alpha, so a button may move, but the steps are the same.
>
> **Try it free:** https://try.elevenlabs.io/8n9sgoi23fkk
> **Turn this into the on-screen "one screen" graphic + the public Google Doc lead magnet.**

## What you need before you start
- An ElevenCreative account (trial link above)
- ONE product photo (that is the only asset you bring)
- A short ad script (2-3 sentences of voiceover)

## The whole flow on one screen (6 steps)
```
[Product Photo] -> [Image node] -> [Video node] -> \
                                                     [Composition] -> finished ad
[Text to Speech (Eleven v3)] -> [Lipsync] ---------/
[Music]  ---------------------------------------->/
[Sound Effects] ---------------------------------/
```

## Step by step

**1. New Flow.** ElevenCreative dashboard -> New Flow -> blank canvas. Add nodes by right-clicking the canvas or the toolbar. Every node shows its credit cost when you hover Run - watch it, this is not free.

**2. Upload Media node.** Drop in your product photo.

**3. Image Generation node.** Drag from the photo's output port (Flows suggests compatible next nodes). Pick a model - you get 50+ image and video models (Veo 3, Sora 2, Kling, Flux, Seedance, Nano Banana). Prompt a cleaner, art-directed version of the shot. Run.

**4. Video Generation node.** Connect the image into it. Pick a video model (Veo 3 or Kling). Prompt the camera move (e.g. slow push-in). Run.

**5. Text to Speech node (Eleven v3).** Type your ad script, pick a voice, model = Eleven v3 (most expressive). Run. This is your voiceover.

**6. Lipsync node** (only if there's a talking character). Connect the video + the voiceover into it. Syncs lips to audio.

**7. Music node** -> royalty-free background track. **Sound Effects node** -> accents (whoosh, click). Run both.

**8. Composition node.** Wire everything into it. This is the centralized preview. Press play - watch the whole ad assemble in one place. Download the assets, download the final composition, or export to Studio (the timeline editor) for final polish.

## The money move: swap one node, re-run one branch
Want a different voice or a Spanish version? Go to ONLY the Text to Speech node, swap the voice or change the language, and re-run just that node + everything downstream of it. Your image and video do NOT regenerate - they didn't change.
- **Honest note:** re-running a node is a new generation = new credits. It is not free re-rolls. What you save is the credits/time on the image and video you did NOT have to redo. You only pay to redo the part that changed.
- Do it 2-3 times = 3 versions of the ad, same visuals, different voices, built by touching one node.

## Naming (so you sound like you know it)
- Platform = **ElevenCreative**. Feature = **Flows**. One pipeline = "a Flow." Never call the product "Flow."

## Homework
Build one rough ad tonight. Your first one will be ugly. That is the point - you will understand this better than any video can teach you.
