# Filming guide - "I Built an Entire Video Ad in One Canvas with ElevenLabs Flows"

Horizontal YouTube video. Talk-to-camera cold open, then screen-recorded demo with voiceover. Everything here follows the paid brief's production rules and the accuracy guardrails in analysis.md.

---

## Production do's (from the brief - non-negotiable)
- Film HORIZONTAL (16:9). This is a long-form YouTube video, not a short.
- NO microphone visible in the shot. Use a lav hidden under the shirt, or an off-camera boom or desk mic out of frame. If the mic is in frame, reframe before you roll.
- Smart-casual clothing. No pajamas, no logo tees that clash with the ElevenLabs orange in the thumbnail.
- Good light. Natural window light or a ring/key light in FRONT of you. Do not sit backlit (no bright window behind you).
- Clean or relevant background. Tidy desk, plant, or a simple wall. Nothing distracting or messy behind you.
- AUDIO CHECK before filming. Record 15 seconds, play it back, confirm levels and no room echo/hum BEFORE you shoot the whole thing.

## Pre-record checklist
- [ ] Have ONE product photo ready on the desktop (a clean shot of a shoe, bottle, can, gadget - something simple with a clear subject).
- [ ] Logged into ElevenCreative with enough credits to run the full pipeline plus 2 voice re-runs (this is a paid demo, do not run out mid-record).
- [ ] Open a fresh, empty Flow so the New Flow / blank canvas moment is clean.
- [ ] VERIFY LIVE IN THE NODE MENU before you commit lines:
  - [ ] Confirm the exact model names you will say on camera (Veo 3, Kling, Flux, Seedance, Nano Banana, Sora 2). Only name what you actually see and use.
  - [ ] Confirm the audio stack nodes exist: Text to Speech (with Eleven v3 as a voice model option), Lipsync, Music, Sound Effects.
  - [ ] Check the localization story: do the swap-the-voice/language-and-re-run path. Do NOT claim a "Dubbing v2 node" unless you literally see it in the menu.
  - [ ] Confirm the credit cost shows when you hover the Run button (you will point to it on camera).
- [ ] Write the ad script for the voiceover node in advance (short, 2-3 sentences).
- [ ] Have the finished ad already rendered once so you can drop it into the cold open in editing.
- [ ] PartnerStack link + code pasted into your notes so you say them right: https://try.elevenlabs.io/8n9sgoi23fkk / code [CODE].

## Accuracy reminders taped to the monitor
- Say the FULL product name before 0:05: "Flows in ElevenCreative."
- Never say bare "Flow" as the product. Product = "Flows." One pipeline = "a Flow."
- Say "50+ image and video models plus ElevenLabs' full audio stack." Do NOT say "30+."
- Say "currently in alpha" once.
- Credits are NOT free. Re-running a node costs again. Say so.
- API is "coming soon." Do not demo it.
- The 10-hooks-x-3-languages line is YOUR idea, not an ElevenLabs stat. Frame it that way.
- No competitors. No money claims. No em dashes when you write on-screen text.

---

## Exact on-screen demo steps (record the screen for these)
1. ElevenCreative dashboard -> click New Flow -> blank canvas.
2. Add an Upload Media node -> drop in the product photo.
3. Drag off the photo node's output port -> show the auto-suggested next nodes -> add an Image Generation node -> connect photo in -> pick a model -> prompt -> Run (point at the credit cost on hover).
4. Add a Video Generation node -> connect the generated image in -> pick Veo 3 or Kling -> prompt a slow push-in -> Run.
5. Add a Text to Speech node -> pick a voice, choose Eleven v3 -> paste the ad script -> Run (that is the voiceover).
6. Add a Lipsync node -> connect the video and the voiceover into it -> Run (if using a spokesperson/character).
7. Add a Music node -> generate a background track. Add a Sound Effects node -> generate accents. Run both.
8. Add a Composition node -> wire everything into it -> press play -> the FINISHED ad plays. Show the download and export-to-Studio options.
9. MONEY MOMENT: go to just the Text to Speech node -> swap the voice (or change the language of the script) -> Run ONLY that node -> show that image and video do NOT regenerate, only the audio + downstream lip-sync update. Say out loud that this re-run costs credits and the savings is not re-doing the unchanged parts.
10. Repeat the swap once more for a third version. End with 3 versions side by side.

## Editing notes
- Cold open = the finished ad (same one you build) for 3-4 seconds, then cut to the talking-head hook.
- Keep the CTA card/lower-third with the link + code visible during the two demo CTAs.
- Add chapter markers, then run /yt-chapters on the final .mp4 to fill real timestamps in description.md.
- Before publishing: email the thumbnail + full video + script to ambassadors@elevenlabs.io so it is approved for payment.
