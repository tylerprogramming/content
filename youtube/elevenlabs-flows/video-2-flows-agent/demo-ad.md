# The Ad You'll Build On Camera (Flows Agent demo)

> For the Flows Agent video: you type ONE prompt, the agent builds the whole node graph and runs it.
> Product is swappable - upload your own product/character image and change the script. This is the default demo.

## Creative decision: 6 separate shots, NOT a 9-card grid
Have the agent generate **6 distinct shot images** (each its own image node -> its own video node -> all into one Composition). Do NOT ask for one "9-card grid image then split it" - grid-splitting isn't a native node and image models frame grid cells inconsistently. 6 separate shots = reliable, consistent (feed the uploaded product into each so it stays the same product), and each becomes real ad footage. 6 clips x ~4-5s = a tight 30s ad.

## The product (default: APEX running sneaker - swap freely)
Upload: a product photo (a sneaker) and optionally a character (a runner). The agent uses these as references so the product stays consistent across shots.

Alternates if you'd rather: a cold brew coffee can, a skincare serum bottle, a candle, an energy drink. Any product with a clean photo works. Pick one you can upload a real image of.

## The 6-shot storyboard
1. **Hero** - the sneaker rotating slowly on a dark gradient, dramatic rim light
2. **Detail** - extreme close-up of the sole tread and laces, texture
3. **Lace-up** - a runner lacing the shoe at dawn (character reference)
4. **Action** - the shoe mid-stride on a trail, dust kicking up
5. **Mood** - the runner cresting a hill at sunrise, wide
6. **End card** - the sneaker with the word APEX and the tagline

## The voiceover script (Eleven v3, ~25-30s)
"Every morning, the trail asks the same question.
How far?
APEX was built to answer it.
Lighter. Grippier. Ready before you are.
APEX. Go find your limit."

## Music direction
Uplifting cinematic build - warm and quiet under the first lines, light percussion entering at the action shot (#4), lifting to a full swell on the end card. Instrumental, no vocals.

## THE PROMPT you type into the Flows Agent (word for word)
> "Build me a 30 second cinematic product ad for a running sneaker called APEX. I've uploaded the product photo and a runner photo as references - keep the same shoe across every shot. Create a 6 shot storyboard: 1) a hero shot of the sneaker rotating slowly on a dark gradient with dramatic rim light, 2) an extreme close-up of the sole tread and laces, 3) a runner lacing the shoe up at dawn, 4) the shoe mid-stride on a trail with dust kicking up, 5) the runner cresting a hill at sunrise, wide, 6) an end card with the sneaker and the word APEX. Turn each shot into a short video clip. Add a warm cinematic voiceover with Eleven v3 reading exactly: 'Every morning, the trail asks the same question. How far? APEX was built to answer it. Lighter. Grippier. Ready before you are. APEX. Go find your limit.' Add uplifting cinematic instrumental music that builds. Assemble everything into one 30 second ad in a Composition node."

## Answer its clarifying questions (likely)
- Length: 30 seconds
- Tone: cinematic, aspirational
- Voice: warm, confident male or female (your pick)
- Keep the uploaded product consistent across all shots: yes

## Iteration prompts (to show non-destructive editing live)
- "Make shot 4 slower and more dramatic."
- "Use a warmer voice for the voiceover."
- "Swap the music for something more energetic."
- "Give me a Spanish version of the voiceover." (nice bridge - ties to the Dubbing video)

## Honest beats to keep in (on brand + brief-compliant)
- Every generation costs credits; re-running a shot re-charges. Set Assist mode to auto-under-threshold first.
- It's in alpha - a shot may fail and you re-run it. Leave that in, it's real.
- The agent picks sensible models; you can override by asking (Veo 3, Kling, etc.).
