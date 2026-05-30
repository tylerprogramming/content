# Knowledge Base: Tech Stack Setup
## Launch OS — Videos 4, 5 & 6

---

## The Full Tech Stack

Launch OS uses these tools together:

| Tool | Purpose |
|------|---------|
| **Skool** | Free + paid community, classroom, course delivery |
| **GoHighLevel (GHL)** | CRM, email marketing, funnels, calendar, automations |
| **Google Workspace** | Professional email (@yourdomain.com), Google Meet for calls |
| **Zapier** | Connects Skool → GoHighLevel (triggers automations) |
| **Mailgun** | Email sending infrastructure (plugged into GHL) |
| **Tella** | Screen recording, VSL creation, editing |
| **Trello** | Course planning and content organization |

---

## GoHighLevel (GHL) Overview (Video 4)

GoHighLevel is the backbone of your business automation. It handles:
- Contact management (CRM)
- Email sequences and broadcasts
- Sales funnels and landing pages
- Calendar and appointment booking
- Sales pipeline tracking
- Automations (trigger-based workflows)

**Two ways to use GHL:**
1. **Sub-account** — you're inside someone else's agency account. Cheaper/free via Kourse snapshot
2. **Agency view** — you have your own GHL agency account ($297/month). Unlocks white-labeling and creating sub-accounts for clients

For Launch OS, you start with a **sub-account** provided via the Kourse snapshot. This gives you a pre-configured account with everything already set up.

### The Kourse Snapshot
A snapshot is a pre-built GHL account configuration. The Kourse snapshot includes:
- Pre-built funnels (VSL opt-in page, thank you page, sales page)
- Pre-written email sequences
- Pre-configured pipelines
- Automation workflows ready to customize

**How to load a snapshot:**
1. Get the snapshot link from Max in the community
2. In your GHL account → Settings → Snapshots → Import Snapshot
3. Follow the prompts — it loads all the pre-built assets into your account

---

## GoHighLevel Account Setup (Video 4)

### Initial Setup Checklist
1. **Business Info** — name, address, phone, timezone
2. **Connect your domain** — so your funnels use your custom URL
3. **Set up email sending** — connect Mailgun for deliverability (see Video 5)
4. **Calendar setup** — configure your availability for sales calls
5. **Pipeline setup** — your sales stages (comes pre-built in the snapshot)

### The Sales Pipeline
The pipeline tracks where every lead is in your funnel:

```
Free Course → VSL Opt-in → Booked Call → No Show → Follow Up → Closed/Won
```

- **Free Course** — they joined your free Skool community
- **VSL Opt-in** — they clicked and opted in to watch your VSL
- **Booked Call** — they scheduled a sales call with you
- **No Show** — they booked but didn't show up (automated follow-up sequence fires)
- **Follow Up** — active conversation, close in progress
- **Closed/Won** — they bought. Move to paid community

### Contacts & CRM
Every lead that opts in gets a contact record in GHL with:
- Name and email
- Source (where they came from)
- Tags (what they've done — opted in, booked call, bought)
- Timeline of all interactions

---

## Domain & Email Setup (Video 5)

Professional email is non-negotiable. No @gmail.com — you need @yourdomain.com.

### Step 1: Buy a Domain
- Use GoDaddy, Namecheap, or Google Domains
- Choose: yourniche.com or yourname.com
- Keep it short, memorable, easy to spell
- .com is still the gold standard

### Step 2: Google Workspace Setup
Google Workspace gives you:
- Professional email (you@yourdomain.com)
- Google Drive, Docs, Sheets
- Google Meet for video calls
- Google Calendar sync

**Setup steps:**
1. Go to workspace.google.com → Start free trial
2. Connect your domain
3. Verify ownership by adding a TXT record to your DNS (Google walks you through this)
4. Create your email: hello@yourdomain.com, max@yourdomain.com, etc.

### Step 3: Email Deliverability Setup

This is critical. Without proper setup, your emails go to spam.

**Three DNS records you MUST set up:**

**SPF (Sender Policy Framework)**
- Tells email servers which services are allowed to send email on your behalf
- Without SPF: your emails look suspicious and get flagged
- Add as a TXT record in your domain's DNS settings
- GHL provides the exact SPF record to add

**DKIM (DomainKeys Identified Mail)**
- A digital signature on every email you send
- Proves the email actually came from you and wasn't tampered with
- GHL generates DKIM keys — you add them as DNS records
- Takes 24-48 hours to propagate

**DMARC (Domain-based Message Authentication)**
- Tells email servers what to do if SPF/DKIM fail
- Protects your domain from being spoofed/impersonated
- Standard DMARC record: `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com`
- Start with `p=none` (monitor mode), then move to `p=quarantine` or `p=reject`

**Why all three matter:**
Gmail and other providers now require SPF + DKIM + DMARC to deliver emails to the inbox. Without them, you're going to spam — guaranteed.

### Step 4: Mailgun Setup

Mailgun is a dedicated email sending infrastructure service. You connect it to GoHighLevel so your emails go through Mailgun's servers (which have great deliverability reputation).

**Why Mailgun instead of sending directly through GHL?**
- Mailgun has dedicated IP addresses with established sending reputation
- Better deliverability — more emails land in inbox, not spam
- Detailed sending analytics

**Setup steps:**
1. Create a Mailgun account (mailgun.com)
2. Add your domain to Mailgun
3. Mailgun gives you DNS records to add (for DKIM and tracking)
4. In GHL → Settings → Email Services → Connect Mailgun
5. Enter your Mailgun API key and domain

### Step 5: Email Warm-Up

A new email domain has zero reputation. If you immediately start sending 500 emails/day, you'll get flagged.

**Warm-up process:**
- Week 1: Send to 20-30 contacts/day max
- Week 2: Increase to 50-75/day
- Week 3: Increase to 100-150/day
- Week 4+: Increase gradually toward your target volume

**During warm-up:**
- Send to your most engaged contacts first (people who know you)
- Ask them to reply, open, and mark as "not spam" if needed
- Monitor your spam score (Mailgun has built-in analytics)

---

## Zapier: Connecting Skool to GoHighLevel (Video 6)

Zapier is the bridge between Skool and GoHighLevel. When someone joins your free Skool community, Zapier automatically creates a contact in GHL and triggers your email welcome sequence.

### The Core Zap: New Skool Member → GHL Contact

**Trigger:** New member joins your free Skool community
**Action:** Create or update a contact in GoHighLevel + add tag "free-community-member"

**Step-by-step:**
1. Go to zapier.com → Create Zap
2. **Trigger:** Skool → "New Community Member"
   - Connect your Skool account
   - Select your free community
3. **Action 1:** GoHighLevel → "Create/Update Contact"
   - Map: First Name, Last Name, Email from Skool to GHL fields
4. **Action 2:** GoHighLevel → "Add Tag"
   - Tag: `free-community-joined`
   - This tag triggers your welcome email automation in GHL

**Important:** In GHL, you'll have an automation set to fire when the tag `free-community-joined` is added. That's how the email sequence starts automatically.

### Skool Zapier Plugin
You also need to enable the Zapier plugin inside Skool:
1. In your Skool community → Settings → Plugins
2. Find Zapier → Enable
3. This allows Zapier to connect to your Skool community

### The SAP Integration
SAP stands for Skool-Automation-Pipeline. This is the full connected system:
- **S**kool: member joins free community
- **A**utomation: Zapier fires, GHL contact created, email sequence starts
- **P**ipeline: contact is moved into the sales pipeline at "Free Course" stage

This is the system that runs your marketing 24/7 without you having to manually follow up with everyone.

---

## VSL Funnel Setup (Video 6)

The VSL (Video Sales Letter) funnel is two pages:

### Page 1: Opt-in Page
A simple page with:
- **Headline:** Clear promise / what they're getting access to
- **VSL video** (your talking-head sales video)
- **Opt-in form:** Name + Email
- Call to action: "Watch the Free Training" or "Get Instant Access"

The opt-in page is built inside GoHighLevel using the pre-built funnel from the Kourse snapshot.

### Page 2: Thank You / Booking Page
After they opt in, redirect them to:
- A thank you message
- Your VSL video (if they haven't watched it yet)
- A clear CTA to book a call: "Schedule Your Free Strategy Call"
- Embed your GHL calendar for direct booking

**The logic:**
- They opt in → they're now in your GHL CRM
- Welcome email sequence starts immediately
- They can book a call right from the thank you page (or from the email)

### Creating Your VSL with Tella
Tella is the recommended tool for recording your VSL:
- Records your screen + webcam simultaneously
- Adds professional backgrounds and branding automatically
- Includes basic editing (trim, cut, add transitions)
- Exports in high quality

**VSL structure (2-4 minutes):**
1. Hook: Call out your ideal person and their problem (first 15 seconds)
2. Credibility: Who you are, why you can help
3. Content preview: What they'll learn/get on the call or in the paid program
4. Social proof: Results you've gotten for others
5. CTA: "Book your free call below" — direct, clear

---

## Website Setup

Your website is simpler than you think. For most people starting out, you don't need a complex website — you just need:

1. **Home page** — introduces you and your offer, directs to VSL funnel
2. **VSL opt-in page** (inside GHL)
3. **Booking page** (inside GHL, calendar embed)

You can build a simple home page inside GoHighLevel using their website builder, or use a separate tool like Carrd (simple), Webflow (professional), or WordPress.

**For most Launch OS users:** Start with GHL for everything. The snapshot includes page templates you can customize.
