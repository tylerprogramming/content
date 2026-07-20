# Follow Along: Let the ElevenLabs Flows Agent Build a 30-Second Ad From One Prompt

> The exact prompt, answers, and settings from the video. Copy it move for move.
> Flows in ElevenCreative is currently in alpha, so a button may move, but the steps are the same.
>
> **Try it free:** https://try.elevenlabs.io/8n9sgoi23fkk
> **My example Flow (shown in the video):** https://elevenlabs.io/app/flows/rLP9x4JJoyjN2F5frt3P (set sharing to "Link only" so it opens for you)

## The 3 names (so you don't mix them up)
- **ElevenCreative** = the platform
- **Flows** = the node canvas
- **Flows Agent** = the AI that builds the Flow for you (this video). NOT "ElevenAgents" (a different product).

## What we're building
You upload ONE real product photo. The Flows Agent generates 5 more images that MATCH it (same palette, lighting, mood), feeds all 6 into a video node, adds an Eleven v3 voiceover and music, and assembles one finished 30-second ad. You type one prompt; the agent picks the models, creates the nodes, wires them, and runs them.

## Step 1: Open the agent
ElevenCreative -> Flows -> New Flow -> open the **Flows Agent** chat panel on the right.

## Step 2: Upload your real product image
Upload your actual product photo (a coffee bag, can, cup, bottle, whatever you sell). This becomes the style anchor for everything the agent generates.

## Step 3: The prompt I typed (copy this, swap the product)
> "I've uploaded my real product photo - a coffee bag for a small batch brand called EMBER. Use it as the style reference and generate 5 more images that MATCH its design, color palette, lighting, and mood, so they look like the same brand campaign, but showing different subjects: coffee beans on warm wood, a cozy coffee house interior, a person in a cozy sweater holding a mug in morning light, a close-up pour with steam rising, and a warm windowsill at sunrise. Keep all 5 consistent with my uploaded product's look. Then feed all 6 images into a video node as references and generate a 30 second cinematic ad from them, warm and unhurried, golden morning light. Add a warm voiceover with Eleven v3 reading exactly: 'Some mornings you wake up. Others, you rise. EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands. Rich. Warm. Unhurried. EMBER. Mornings worth waking up for.' Add gentle warm instrumental music with a small lift at the end. Assemble everything into one 30 second ad in a Composition node."

The 5 generated shots are a GUIDE, not hardcoded. The agent matches them to YOUR product's look.

## Step 4: Answer its clarifying questions
It asks BEFORE it spends (length, tone, voice, structure). My answers:
- Length: 30 seconds
- Tone: warm, cinematic, cozy
- Voice: warm, calm (your pick)
- Use the uploaded image as the style reference, keep the product consistent: yes

Then watch it build on its own: it generates the 5 matching shots, adds a video node, a Text to Speech node (Eleven v3), a music node, and wires them all into a Composition node. It selects the models, creates the nodes, connects them, and runs them.

## Step 5: Iterate by talking (non-destructive)
Just type the change, it re-runs only that branch:
- "Use warmer morning light in the video." -> redoes the video branch only
- "Use a calmer, lower voice for the voiceover." -> redoes the voice + downstream only
- "Make the music softer under the first line." -> just the music
- "Give me a Spanish version of the voiceover." -> dubs it
Shots that didn't change do NOT regenerate. **But every re-run is a new generation = new credits. Not free.**

## Step 6: Set Assist mode BEFORE you go crazy iterating (the important one)
Agent panel -> Assist mode. Three settings:
1. **Approve each** - it asks before every generation. Safe. Start here.
2. **Auto-run** - no confirmation, it just goes. Fast, but you handed it the keys.
3. **Auto under threshold** (recommended) - runs cheap steps automatically, only stops to ask when a single action costs more than the limit you set. Speed + a guardrail on big spends.

## Step 7: The async superpower
Give it something big ("build 3 variations with different opening shots"). It runs **async, on ElevenLabs' side** - so you can **close the tab**, walk away, and come back to a finished Flow. You are not babysitting a progress bar.

## Models available
50+ image and video models (Veo 3, Sora 2, Kling, Seedance, Flux, Nano Banana) + the full audio stack (Eleven v3 TTS, voice cloning, lip-sync, sound effects, music). The agent picks a sensible default; you can override by asking.

## The honest rules (say these, they build trust)
- It's in **alpha** - things move.
- **Not free** - chat is billed on tokens, generations use credits, iterating costs each time. Set a threshold.
- Be **specific** in the first prompt = fewer re-runs = less money.
- The **API is coming soon**, not live - don't wait on it.
