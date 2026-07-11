# The Ad You'll Build On Camera (Flows Agent demo) - EMBER Coffee

> For the Flows Agent video: you type ONE prompt, the agent builds the node graph and runs it.
> Structure Tyler likes: a script in parts + several reference images fed into a single video node,
> so the product and look stay consistent and the video is built FROM your real assets.
> Product/script swappable. Flows is alpha - verify the node behavior live.

## The structure (Tyler's approach) - one idea, the Agent fans it out
1. **You give ONE idea** (a cozy premium coffee brand, EMBER, warm morning ritual).
2. The **Flows Agent writes 6 image prompts from that idea** and builds **6 Image Generation nodes**, one per shot - you never write the shots yourself. (This prompt-fanout is exactly what the Agent is for. If you want it as an explicit in-graph node - a text node that outputs the 6 prompts - check the live node menu; the Agent does the fanout natively either way. Verify live.)
3. Those 6 generated images feed into **one Video node as reference images** so the ad is built from them (consistent product + look).
4. **Eleven v3 voiceover** reads the script (in parts), **Music node** underneath.
5. Everything into a **Composition node** -> one finished 30s ad.

So the graph is:
[Your idea] -> Agent writes 6 prompts -> [Image][Image][Image][Image][Image][Image] -> [Video node] -> \
plus [Text to Speech] and [Music] -> [Composition].

This is the money shot of the whole video: you typed an IDEA, and it came back with six shots, generated them, and turned them into an ad. Optional: upload your own real product image and let it generate the other 5 shots around it. Otherwise it is 100% generated on the canvas - the more impressive demo.

(Accuracy note: whether one video node takes multiple references depends on the model the Agent picks - some, like Kling "elements", take several; others take one start frame plus style refs. Let the Agent choose; if a model only takes one image, it uses the strongest shot as the key reference and the rest guide the look. Verify live.)

## The product: EMBER Coffee (swap freely)
A premium small-batch coffee brand. Cozy, warm, morning-ritual energy. Upload or generate the reference images below.

Alternates: cold brew can, a cafe, a skincare serum, a candle. Any product you can supply reference images for.

## Reference images to feed the video node
1. **Product** - an EMBER coffee bag, matte, warm earthy tones
2. **The cup** - a steaming ceramic mug of black coffee, close
3. **Beans** - coffee beans scattered with a wooden scoop
4. **Character** - a person in a cozy sweater holding the mug by a window in warm morning light
5. **Scene/mood** - a warm kitchen, soft golden morning light

(Generate these with an image node first, or upload your own. They become the references.)

## The script, in parts (Eleven v3 voiceover, ~25-30s)
Part 1: "Some mornings you wake up. Others, you rise."
Part 2: "EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands."
Part 3: "Rich. Warm. Unhurried."
Part 4: "EMBER. Mornings worth waking up for."

## Music direction
Gentle, warm, unhurried instrumental. Soft piano or acoustic, low and cozy, a small lift on the final line. No vocals.

## THE PROMPT you type into the Flows Agent (word for word)
> "Build me a 30 second cinematic ad for a cozy small batch coffee brand called EMBER, warm morning ritual vibe, golden light, unhurried. Come up with six shots for it yourself and write the image prompts - I'm thinking a hero product shot, a steaming mug, the beans, a person enjoying it, a mood shot, and an end card, but you choose. Generate an image for each of those six shots, then feed those images into a video node as references and generate the ad video from them so the product and look stay consistent. Add a warm voiceover with Eleven v3 reading exactly: 'Some mornings you wake up. Others, you rise. EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands. Rich. Warm. Unhurried. EMBER. Mornings worth waking up for.' Add gentle warm instrumental music with a small lift at the end. Assemble everything into one 30 second ad in a Composition node."

The shot list below is what you EXPECT it to come up with - use it to sanity-check what the Agent generates, and to tweak any shot with a follow-up ("make shot 4 a close-up of hands around the mug").

## Answer its clarifying questions (likely)
- Length: 30 seconds
- Tone: warm, cinematic, cozy
- Voice: warm, calm (your pick)
- Use the uploaded images as references, keep the product consistent: yes

## Iteration prompts (show non-destructive editing live)
- "Use warmer morning light in the video."
- "Use a calmer, lower voice for the voiceover."
- "Make the music softer under the first line."
- "Give me a Spanish version of the voiceover." (bridge to the Dubbing video)

## Honest beats to keep in (on brand + brief-compliant)
- Every generation costs credits; re-running re-charges. Set Assist mode to auto-under-threshold first.
- Alpha - a generation may fail and you re-run it. Leave that in, it is real.
- The agent picks sensible models; you can override by asking.
