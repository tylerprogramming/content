# The Ad You'll Build On Camera (Flows Agent demo) - EMBER Coffee

> For the Flows Agent video: you type ONE prompt, the agent builds the node graph and runs it.
> Structure Tyler likes: a script in parts + several reference images fed into a single video node,
> so the product and look stay consistent and the video is built FROM your real assets.
> Product/script swappable. Flows is alpha - verify the node behavior live.

## The structure (Tyler's approach)
1. Generate or upload **several reference images** (the product, a mug, beans, a character, a cozy scene).
2. Feed ALL of them into **one Video node as reference images** so the video is generated using those exact elements (consistent product + character, not generated from nothing).
3. **Eleven v3 voiceover** reads the script (written in parts), **Music node** underneath.
4. Everything into a **Composition node** -> one finished 30s ad.

Why this beats 6 separate clips: fewer nodes, the product stays consistent because it IS the reference, and it is closer to how a real creator would do it. (Accuracy note: whether one video node takes multiple references depends on the model the agent picks - some, like Kling "elements", take several; others take one start frame plus style refs. Let the agent choose; if a model only takes one image, it will use the product as the key reference and the rest to guide the look. Verify live.)

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
> "Build me a 30 second cinematic coffee ad for a small batch brand called EMBER. I'm giving you several reference images - the coffee bag, a steaming ceramic mug, coffee beans with a scoop, and a person in a cozy sweater holding the mug by a window in warm morning light. Use these as reference images in the video node so the product and the look stay consistent, and generate the ad video from them. Warm, unhurried, golden morning light throughout. Add a warm voiceover with Eleven v3 reading exactly: 'Some mornings you wake up. Others, you rise. EMBER is slow roasted in small batches, for the cup that actually earns its place in your hands. Rich. Warm. Unhurried. EMBER. Mornings worth waking up for.' Add gentle warm instrumental music with a small lift at the end. Assemble everything into one 30 second ad in a Composition node."

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
