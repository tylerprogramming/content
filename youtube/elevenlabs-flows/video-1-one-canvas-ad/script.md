# Script - "I Built an Entire Video Ad in One Canvas with ElevenLabs Flows"

Target: 12-16 minutes. Horizontal. Word-for-word cold open, then talk-to-demo. No em dashes anywhere. Full product name in the first 5 seconds. Multiple CTAs to the PartnerStack trial. Everything below obeys the accuracy guardrails in analysis.md.

PartnerStack link (filled): https://try.elevenlabs.io/8n9sgoi23fkk - link-only, no separate code.

Timing is a guide, not a hard cut list.

---

## 0:00 - 0:20 | COLD OPEN (word-for-word)

[B-roll: the FINISHED video ad plays full screen for about 3 seconds - product shot, voiceover, music]

TYLER (on camera):
"That whole ad you just watched? The visuals, the voice, the lip-sync, the music. I built all of it in one canvas with Flows in ElevenCreative. No timeline, no ten different tabs. And I put the exact node by node recipe in a free doc, link is in the description, so open it up and build this alongside me. Let me show you exactly how."

---

## 0:20 - 1:10 | WHAT THIS IS + FIRST CTA

"Okay so quick context. This is a paid partnership with ElevenLabs, I am one of their ambassadors, and I am going to be straight with you the whole way through, including the stuff that costs credits and the stuff that is still rough. That is the deal.

The platform is called ElevenCreative. It is their all-in-one place for generating and editing audio and video. And the specific feature I am obsessed with right now is called Flows. Flows is a node based canvas. Think of an infinite whiteboard where each box is one AI step. One box generates an image, the next turns it into video, the next one is the voiceover, the next does lip-sync, and so on. You connect them, you press run, and the whole pipeline executes in one place.

One quick honesty note before we build: Flows is currently in alpha, so the exact buttons might move around a little after I post this. The idea is what matters.

If you want to follow along in your own account, I will drop a link in the description that gets you into a trial. Link is https://try.elevenlabs.io/8n9sgoi23fkk. Go make an account and come back, because the best way to learn this is to build one with me.

And two things are waiting for you in that description. The trial link so you can actually build in Flows, and a free doc that has this entire recipe written out, every node in order with the exact settings I use, so you are never lost. It is also pinned in the top comment. Grab it, keep it open on the side, and follow along."

---

## 1:10 - 2:10 | THE MENTAL MODEL (Flows vs Studio)

"Two things live inside ElevenCreative that people mix up, so let me clear it up fast.

Studio is a timeline editor. It is the classic left to right track view. Great for precise editing, captions, layering.

Flows is the node canvas. It is not a timeline, it is a map of your production. You are wiring up the logic of how the ad gets made, not scrubbing a playhead.

And here is the connection: when you finish a Flow, you can export the output into Studio to do your final polish. So Flows builds the thing, Studio finishes the thing. Today we are living in Flows.

The reason this matters: instead of generating an image in one tool, downloading it, uploading it to a video tool, downloading that, opening a voice tool, and stitching it all together by hand, the entire chain sits on one canvas and runs together. That is the pitch. Let me prove it."

---

## 2:10 - 2:40 | THE WHOLE FLOW ON ONE SCREEN (the anchor)

[Show the FULL finished node graph as a single map, zoomed out. This is the graphic you cut back to throughout the build.]

"Before we touch a single node, here is the whole thing on one screen, so you always know where we are. Six steps, left to right. Product photo, into an image node, into a video node. Then the voice, then lip-sync, then music and sound effects. Everything flows into one Composition node at the end that assembles the ad.

This exact map is step one in the free doc, so if you ever lose the thread, look at the doc, look at this picture, you are in the same place. We are going to build it left to right, one node at a time. Follow along."

---

## 2:10 - 3:00 | THE INGREDIENT: ONE PRODUCT PHOTO

"Here is my one input. A single product photo. [show the photo] This is the only asset I am bringing. Everything else, the video motion, the voice, the music, the sound design, is going to get generated on the canvas.

I am going to start a new Flow. From the ElevenCreative dashboard I click New Flow, and I get this blank canvas. To add a node I can right click the canvas or use the toolbar. Watch the bottom of the screen too, because every node shows you a credit cost before you run it, and I want you to see that the whole time so nobody thinks this is free."

---

## 3:00 - 5:00 | BUILD, NODE BY NODE (part 1: image -> video)

"First node, Upload Media. I drop my product photo in. [do it]

Next I want a cleaner, more art-directed version of this shot, so I am adding an Image Generation node and connecting my photo into it. And here is a detail I love: when I drag a connection off the output port of my photo node, ElevenCreative suggests the nodes that make sense to connect next. So it is guiding me toward the right pipeline instead of making me guess.

Inside the Image Generation node I get a menu of models. This is a big deal, so let me say it accurately. Flows gives you 50 plus image and video models, plus ElevenLabs' own full audio stack. On the image and video side you will see names like Veo 3, Sora 2, Kling, Flux, Seedance, Nano Banana. I will pick one here for the product shot. [pick one, write the prompt, run it]

While that runs, notice I did not leave the canvas. Okay, image is back.

Now the motion. I add a Video Generation node and connect my image into it. I will choose a video model, something like Veo 3 or Kling, and prompt the camera move I want, a slow push in on the product. [run it] This is the step that used to mean exporting an image and re-uploading it somewhere else. Here it is just the next box."

---

## 5:00 - 7:00 | BUILD (part 2: voice, lip-sync, audio)

"Now the part ElevenLabs is genuinely best in the world at, the audio.

I add a Text to Speech node. Inside it I can pick a voice and I am using Eleven v3, which is their latest and most expressive voice model. I type my ad script, choose the voice, and run it. [do it] That is my voiceover, generated right on the canvas.

If I have a character or a spokesperson in the video and I want the mouth to match the voice, there is a dedicated Lipsync node. I connect my video and my voiceover into it and it syncs the lips to the audio. [show it]

Then the vibe. I add a Music node to generate a royalty free background track, and a Sound Effects node for the little accents, a whoosh, a click, whatever the ad needs. Both are just more boxes on the same canvas. [run them]

So take a step back and look at the canvas. Photo, image, video, voice, lip-sync, music, sound effects. Every piece of this ad is one connected graph."

---

## 7:00 - 8:30 | COMPOSITION + THE FINISHED AD + SECOND CTA

"Last node, Composition. This is the centralized preview. I wire everything into it and it assembles the pieces so I can watch the whole ad in one place. [press play on the composition]

[the finished ad plays]

That is it. One product photo in, a finished video ad out, and I never left the canvas. From here I can download the individual assets, download the final composition, or export it into Studio if I want to fine tune the edit on a timeline.

Quick pause for a real talk moment. This is exactly the kind of thing the free trial is for. Go build one bad ad. Seriously, your first one will be rough, mine always are. The link is in the description, https://try.elevenlabs.io/8n9sgoi23fkk. Build one ugly ad tonight and you will understand this better than any video can teach you.

But I promised you the real magic is not the first ad. Here it comes."

---

## 8:30 - 10:30 | THE MONEY MOMENT: SWAP AND RE-RUN ONE BRANCH

"Say the ad worked, but I want a version with a different voice. Or a Spanish version for a different audience. In a normal workflow that means basically starting over.

In Flows, I go to just the Text to Speech node. I swap the voice, or I change the language of the script. And here is the whole point of a node canvas: I only re-run that node and the nodes downstream of it. My image and my video do not regenerate, because they did not change. Only the branch that changed re-runs.

[swap the voice, hit run on that node, show only the audio and downstream lip-sync updating]

Let me be honest about cost right here, because this is where people get the wrong idea. Re-running a node is a new generation, and a new generation costs credits. This is not free re-rolls. What you are saving is not money on that node, it is all the credits and time you would have burned re-generating the image and the video that did not need to change. You only pay to redo the part that actually changed. That is the real value.

Now watch me do it again. I swap the voice one more time for a third version. [run] So now I have three versions of this ad, same visuals, three different voices, and I built them by touching one node three times instead of rebuilding the whole thing three times.

Here is where my brain goes with this, and I want to be clear this is my idea, not an official ElevenLabs number. Imagine you had ten different hook lines and you wanted each one in three languages. That is thirty ad variations. On a canvas like this, that is one Flow where you swap the script input and the voice, and re-run just those branches. You are not running thirty separate productions. That is the scaling story, and that is why teams are looking at this."

---

## 10:30 - 12:00 | HONEST LIMITATIONS

"Let me give you the straight version of what is and is not true here, because that is the only kind of review worth watching.

One. It is in alpha. Things will move, some runs will fail and you re-run them, and the polish is not final. Go in with that expectation.

Two. It is not free and it is not magic. Every node that runs costs credits, and re-running costs credits again. The savings is in not re-doing the parts that did not change, not in some infinite free generation. Watch that credit cost that shows up when you hover the run button. It keeps you honest.

Three. There is a Flows Agent where you can describe what you want in plain language and it builds the node graph for you. That is real and it is impressive, and I will probably do a whole video on it. And there is an API for programmatic runs that is coming soon, so it is not live yet. I am not going to demo something that is not shipped.

Four. For localization, I did it the honest way, by swapping the voice and language input on the canvas and re-running that branch. If you see other localization tooling in your node menu, use it, but the reliable path today is swap and re-run.

That is the real picture. It is early, it costs credits, and it is still one of the more genuinely useful AI production tools I have touched, because the one-canvas thing actually removes work."

---

## 12:00 - 13:00 | RECAP + FINAL CTA

"So to recap the system. One product photo. Image node, video node, that is your visuals. Text to speech with Eleven v3, that is your voice. Lip-sync, music, sound effects, that is your audio. Composition node to preview and export. And then the part that makes it a system instead of a one-off, swap a single node and re-run just that branch to spin up as many versions as you need.

If you want to actually build this, two things are in the description and pinned in the top comment. The free recipe doc with every node and setting so you can rebuild this exactly, and the trial link, https://try.elevenlabs.io/8n9sgoi23fkk. Grab the doc, get the trial, build one rough ad this week. That is the whole homework.

If this was useful, subscribe, because I am doing more of these ElevenCreative deep dives, including the Flows Agent one where the AI wires the whole canvas for you. I will see you in that one."

[End card: subscribe + the finished ad looping]

---

## CTA checklist (all present)
- Intro CTA at ~1:00 (link + code, go make an account)
- Mid CTA at ~8:00 (build one rough ad, link + code)
- Final CTA at ~12:30 (get the trial, link + code, homework)

## Accuracy self-check before filming
- [ ] Full product name said before 0:05
- [ ] "Flows in ElevenCreative" / "ElevenCreative Flows," never bare "Flow"
- [ ] "50+ models" language, named real models only
- [ ] "currently in alpha" said once
- [ ] Credits framed as not free, re-run costs again
- [ ] API described as coming soon, not demoed
- [ ] No competitors, no money claims, no em dashes
