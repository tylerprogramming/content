# WhatsApp Setup - Pre-Shoot Checklist (do days ahead, not on film day)

> Tyler has historically hit friction with WhatsApp Business. This is the de-risked path.
> WhatsApp is NOT blocking any other video - do it only when you're ready. No deadline on this brief.
> Docs: https://elevenlabs.io/docs/eleven-agents/whatsapp | Announcement: https://elevenlabs.io/blog/elevenlabs-agents-whatsapp-support

## Why it always fought you: two different products
- ❌ **WhatsApp Business App** (green phone app) - NOT this. If your number is on it, it BLOCKS the API setup.
- ✅ **WhatsApp Business Platform / Cloud API** = a WhatsApp Business Account (WABA) in Meta Business. THIS is what ElevenAgents connects to.

## The unlock
ElevenLabs' "Import account" uses Meta's **Embedded Signup** - a guided popup that can CREATE the whole WABA inline. You do NOT have to pre-build it in Meta Business Manager. You mainly need a clean phone number.

## Phase 1 - Meta side (do a few days BEFORE filming)
1. Have a Meta/Facebook account (the flow will prompt you to create a free Business if needed).
2. **Get a dedicated phone number that is NOT on any WhatsApp app** and can receive an SMS or call code.
   - Easiest: a free **Google Voice** number, a spare SIM, or a Twilio number.
   - GOTCHA: if the number is already registered on WhatsApp or WhatsApp Business App, delete that account first or use a different number. This is the #1 blocker.
3. Run the Embedded Signup (via the ElevenLabs import in Phase 2, or from Meta Business), set a display name + profile pic.
4. Let Meta business verification clear (can take a few days - hence doing this ahead).

## Phase 2 - ElevenLabs side (2 minutes, this is the on-camera part)
1. ElevenAgents -> **Integrations** -> **Add integration** -> **WhatsApp**
2. **Import account** -> Meta authorization popup -> select account, grant permission
3. On the settings page, **ASSIGN YOUR AGENT** (critical - skip this and inbound messages are ignored)
4. Text the number -> your agent replies. That's the demo shot.

## Gotchas that save the shoot
- **No payment method needed for the demo.** Billing is only for OUTBOUND calls. Your video = agent ANSWERING inbound messages, so no card required.
- **No third-party manager on the number** (Gupshup/Twilio owning the WABA blocks the ElevenLabs import). Use a clean number.
- **Zero-Retention Mode ignores messages** - make sure it's off for the demo.
- Meta verification lead time is the reason to do Phase 1 early.

## If WhatsApp stays painful: fallback options
- The ElevenAgents brief allows 2 videos. You could make the SECOND ElevenAgents video a non-WhatsApp deployment (web chat widget or a phone/voice agent) if WhatsApp keeps fighting - still on-brief for "how to best use ElevenAgents," just confirm with connie@elevenlabs.io since the brief names WhatsApp specifically.
- Or simply skip this brief and put the energy into Flows + Dubbing, which need no WhatsApp.
