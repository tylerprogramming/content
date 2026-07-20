# Hooks: Email System (revised)

**Revision goal:** Show the receipts in the first 5 seconds. Match Tyler's AntiGravity pattern — empty-folder → finished-app structure becomes ConvertKit-pricing → terminal-running-drip-campaign.

---

## Hook A (RECOMMENDED) — Pricing Page → Receipt

[SHOW: Browser tab on ConvertKit pricing page — $50/mo highlighted. Cursor moves to close button. Cut to terminal showing `python3 email_campaign.py` running — output shows "6 emails sent: 3 to step 1, 2 to step 2, 1 to step 3."]

> *(VO at 0:03)*
> Most creators in my space pay 50 to 200 bucks a month to send emails. I pay zero.

> *(at 0:08)*
> Here's the entire system. Claude Code skill, Resend API, SQLite database. Sends drip campaigns, blasts my list, runs welcome sequences. Free.

> *(at 0:15)*
> I'll walk you through the architecture, three live demos, and exactly how to build your own.

**Why it works:**
- **Pricing page → receipt** in first 8 seconds = AntiGravity hook pattern
- **Specific dollar range** (50-200) is verifiable — anyone can check ConvertKit/Beehiiv pricing
- **Three promises** at the end gives the viewer a reason to stay

---

## Hook B — The Receipt First

[SHOW: SQLite query running in TablePlus — `SELECT COUNT(*) FROM email_sends WHERE sent_at > date('now', '-30 days')` returning a real number like 1,247]

> 1,247 emails sent in the last 30 days. Total cost — zero dollars. This is the system. Let me show you.

**Why:** Raw receipt. Highest verifiability. Best for technical audience. Use only if the number is real and impressive.

---

## Hook C — Skool Trigger Story

[SHOW: Browser tab on Skool dashboard with a new member just joined. Cut to terminal seconds later — campaign runner fires, "1 email sent: alice@example.com / welcome step 1"]

> Someone just joined my Skool community. Two seconds later, they got a welcome email. 24 hours from now they'll get the next one. 72 hours after that, the third. I don't touch a single button. Here's the whole system.

**Why:** Causal story — new member → automatic email → continued sequence. Easy to understand, easy to verify, easy to want.

---

## Hook D — The Stack Reveal

[SHOW: Terminal with three commands typed in sequence — `/email send`, `/email blast`, `/email campaign` — but not yet executed. Cursor blinks on the last one.]

> Three commands. Send a one-off, blast my list, run a multi-step drip campaign. All from my terminal, all powered by Claude Code, all costing me nothing. Watch.

**Why:** Quick visual scope-set. Tells viewer what they're getting in 10 seconds.

---

## Recommendation

**Use Hook A.** It mirrors AntiGravity's "empty folder → finished app" beat structure — close pricing tab → see real campaign running. Test Hook B if the technical audience leans in more than expected.

**Avoid Hook D as the cold open** — it's a list, not a story. Better as the second beat at 0:30.
