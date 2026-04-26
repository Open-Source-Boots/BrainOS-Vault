---
open_questions:
  - id: OQ-20260306-001
    question: "Confirm all 5 DNS records show green in Zoho"
    canonical_target: ACTIVE-PROJECTS.md
    status: OPEN
  - id: OQ-20260306-002
    question: "confirm Zoho username is 'support' not 'braydenboots'"
    canonical_target: ACTIVE-PROJECTS.md
    status: CLOSED
---
## STEP 1 — PRE-ENTRY ASSESSMENT

**1. Approximate date of this thread:**
March 6, 2026 — confirmed by the Shopify domain registration confirmation email shown in thread (dated March 6, 2026) and system-reminder timestamps throughout.

**2. Type(s) of content:**
PROJECT / TOOL — primarily a technical setup walkthrough for a specific business project (Ctrl+You Shopify store email infrastructure). Secondary skill capture (DNS configuration, Zoho Mail setup).

**3. New information, correction, or both:**
Introduces new information — documents the initial setup of `ctrlplusyou.com` email infrastructure, DNS configuration decisions, and email strategy for a dropshipping business. No corrections to prior entries visible in this thread.

**4. Most directly feeds:**
**CTRL-YOU-STATUS** — this thread is entirely about infrastructure decisions for the Ctrl+You Shopify store. Also partially feeds a potential new file: **CTRL-YOU-INFRASTRUCTURE** or folds into CTRL-YOU-STATUS under a technical/DNS section.

***

## STEP 2 — BRAIN ENTRY

```
date_logged: 2026-04-16
source_thread_date: 2026-03-06
source_thread_title: "I just purchased the domain ctrlplusyou.com from shopify, I want to make a gmail/email for my business"
entry_type: PROJECT / TOOL
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: CTRL-YOU-STATUS
context_available: none — isolated thread
tags: [ctrl-you, shopify, zoho-mail, dns, email-setup, dropshipping, ctrlplusyou.com, business-email]
```

***

# Brain Entry — Ctrl+You Business Email Setup via Zoho Mail Free Plan (March 6, 2026)

## CONFIRMED FACTS
Only facts explicitly stated in this thread. Nothing inferred.

- Domain name | `ctrlplusyou.com` | Shopify domain registration email shown in thread
- Domain registered through | Shopify | Shopify confirmation email dated March 6, 2026
- Domain registration cost | $16 (user stated) | User's opening message
- Domain registration confirmation date | March 6, 2026 | Shown in Shopify email screenshot
- Domain auto-renewal date | March 6, 2027 | Shopify confirmation email
- Domain nameservers | `ns-cloud-c1.googledomains.com` through `ns-cloud-c4.googledomains.com` | DNSchecker.org screenshot shown in thread
- DNS is managed by | Shopify (using Google nameserver infrastructure on backend) | Confirmed via Shopify DNS Settings page appearing in thread and Perplexity clarification
- Shopify store name/brand | Ctrl+You | Shown on store "Opening soon" page screenshot
- Shopify store status at time of thread | "Opening soon" / password protected | Screenshot shown
- Shopify store sub-domains connected | `u0111e-07.myshopify.com`, `ctrl-you.myshopify.com`, `www.ctrlplusyou.com`, `account.ctrlplusyou.com` | Shopify Domains screenshot
- Google Workspace pricing shown | $22.44/user/month (Business Plus, 15% off for 1 month, regular $26.40) | Screenshot in thread — user declined this
- Zoho Mail free plan | Accessed via direct URL `https://mail.zoho.com/signup?type=org&plan=free` | Confirmed working per thread progression
- Zoho free plan limit | 5 users, 5GB per user | Referenced in thread
- Zoho domain verification method used | TXT record | Zoho Domain Verification screenshot
- Zoho TXT verification value | `zoho-verification=zb75991258.zmverify.zoho.com` | Zoho Domain Verification screenshot
- Zoho TXT verification host | `@` | Zoho Domain Verification screenshot
- Domain ownership verified in Zoho | Yes — "You have now verified your domain ownership" | Account Creation success screenshot
- Zoho account role | Super Administrator | Account Creation screenshot
- Auto-filled username in Zoho at verification | `braydenboots` | Account Creation screenshot — Perplexity advised changing this to `support`
- Recommended primary email address | `support@ctrlplusyou.com` | Perplexity recommendation in thread
- Reason for `support@` recommendation | Universally trusted by customers, best for dropshipping contact | Perplexity explanation
- Zoho MX records to add | `mx.zoho.com` (priority 10), `mx2.zoho.com` (priority 20), `mx3.zoho.com` (priority 50) | Zoho DNS Mapping screenshot
- Zoho SPF record to add | TXT, host `@`, value `v=spf1 include:zohomail.com ~all` | Zoho DNS Mapping screenshot
- Zoho DKIM record to add | TXT, host `zmail._domainkey`, value = long DKIM string shown in Zoho | Zoho DNS Mapping screenshot
- Shopify DNS Settings location | Shopify Admin → Settings → Domains → ctrlplusyou.com → DNS Settings | Confirmed via DNS Settings screenshot shown
- Shopify DNS supports record types | A, AAAA, CNAME, MX, TXT, SRV | Dropdown shown in DNS Settings screenshot
- SPF and DKIM are both added as | TXT records in Shopify DNS | Confirmed in thread
- Zoho Mail free plan was NOT visible on main pricing page at time of thread | Confirmed — pricing page only showed Mail Lite ($1.25), Mail Premium ($4), Standard ($3), Professional ($6) | Zoho pricing screenshot
- Squarespace Domains (formerly Google Domains) | `ctrlplusyou.com` was NOT found here — wrong account | Squarespace Domains screenshot showed "There are no domains" under initials "BB"
- Email addresses discussed for business use | `support@`, `admin@`, `hello@`, `orders@` | Thread discussion
- Brayden's Zoho account initials shown | CTR | Zoho interface screenshots

## TIMELINE MARKERS
- March 6, 2026, ~10:20 AM — Shopify domain registration confirmation email received
- March 6, 2026, 10:27 AM — First message in thread (Google Workspace screenshot)
- March 6, 2026, 10:30 AM — Zoho Mail pricing page screenshot (no free plan visible)
- March 6, 2026, 10:32 AM — Zoho Domain Verification page shown (TXT method)
- March 6, 2026, 10:33 AM — Shopify Domains page showing "Needs verification" for ctrlplusyou.com
- March 6, 2026, 10:46 AM — TXT Verification failure shown in Zoho
- March 6, 2026, 10:48 AM — DNSchecker results shown (ns-cloud.googledomains.com)
- March 6, 2026, 10:50 AM — Shopify Domains now showing all "Connected" (Shopify verified)
- March 6, 2026, 10:52 AM — Squarespace Domains login — domain not found (wrong account)
- March 6, 2026, 10:54 AM — DNSchecker + Shopify registration email shown to confirm domain is Shopify-managed
- March 6, 2026, 10:57 AM — Zoho "You have now verified your domain ownership" — SUCCESS
- March 6, 2026, 10:59 AM — Zoho DNS Mapping page with MX/SPF/DKIM shown (all red ❗ — not yet added)
- March 6, 2026, 11:02 AM — Shopify DNS Settings page shown — user ready to add records

## UPDATES TO CANONICAL FILES

- **CTRL-YOU-STATUS**: Add section for email/DNS infrastructure. Log that `ctrlplusyou.com` domain is registered via Shopify for $16/year, auto-renews March 6, 2027. Log that Zoho Mail free plan is in use. Log `support@ctrlplusyou.com` as primary business email. Log that domain verification completed March 6, 2026. Log DNS records pending (MX/SPF/DKIM) as of end of thread — status of final DNS records is [UNCONFIRMED — fill in after DNS propagated].
- **CTRL-YOU-STATUS**: Note that Google Workspace was evaluated and declined due to cost ($22.44/mo Business Plus).
- **BRAYDEN-IDENTITY**: Note that Brayden owns `ctrlplusyou.com` as a Shopify dropshipping store brand. Store was in "Opening soon" state as of March 6, 2026.

## CONTRADICTIONS
- Cannot fully assess — thread is isolated. Flag for review during compilation.
- One potential flag: Other brain entries reference "Kray Studios" as the Shopify store brand. This thread references a **separate** store/brand called **Ctrl+You** at `ctrlplusyou.com`. These appear to be two distinct projects. Flag for Brayden to confirm whether Ctrl+You and Kray Studios are the same store, separate stores, or one replaced the other.

## INSIGHTS & PATTERNS

- Brayden encountered friction at every step of a technical DNS setup but persisted through the full process in a single session — suggests he executes well when guided step-by-step in real time
- The Zoho free plan is hidden from the main pricing page and only accessible via direct URL — this is a non-obvious workaround worth preserving
- Shopify-registered domains use Google nameserver infrastructure but DNS is managed inside Shopify admin, not Google Domains or Squarespace — this caused significant confusion and is worth encoding as a standing rule
- The "BB" Squarespace account mismatch suggests Brayden may have multiple Google accounts — worth auditing to avoid future confusion
- Choosing `support@` over a personal name-based email (`braydenboots@`) is a deliberate professionalism decision worth preserving as a standing rule for future email setup

## TOOLS & RESOURCES REFERENCED

- Zoho Mail Free Plan | active (verified and in setup) | Access via `https://mail.zoho.com/signup?type=org&plan=free` — not shown on main pricing page
- Shopify Domain Admin | active | DNS Settings accessible at Admin → Settings → Domains → [domain] → DNS Settings
- DNSchecker.org | mentioned | Used to confirm nameservers for `ctrlplusyou.com`
- Google Workspace Business Plus | mentioned / declined | $22.44/mo with 15% discount, $26.40 regular — declined due to cost
- Squarespace Domains (fmr. Google Domains) | mentioned / not applicable | `ctrlplusyou.com` not found here — domain is Shopify-managed
- ImprovMX | mentioned only | Free email forwarding alternative — not pursued
- Cloudflare Email Routing | mentioned only | Free receive-only forwarding alternative — not pursued
- Brevo | mentioned only | Free SMTP alternative — not pursued

## OPEN QUESTIONS

- Were all 5 DNS records (3 MX + SPF + DKIM) successfully added in Shopify DNS? Thread ended before confirmation.
- Did the Zoho DNS Mapping page turn all green (verified) after records were added?
- Was the Zoho account username changed from `braydenboots` to `support` before account creation was finalized?
- Is `ctrlplusyou.com` a separate brand/store from Kray Studios, or are they the same project?
- Does Brayden have multiple Google accounts, and which one is associated with what?
- Was `support@ctrlplusyou.com` set as the Shopify store contact email?

## CROSS-REFERENCES
Cross-references to be added during compilation session.
- Feeds into: CTRL-YOU-STATUS
- Possible links to: BRAYDEN-IDENTITY (domain ownership, business projects), any Kray Studios entries (potential brand overlap/conflict)

## RAW HIGHLIGHTS

> "I don't want to subscribe to this monthly expense (at this point), what options are there to create a business email... for free, since I've already spent $16 on this domain" — Brayden's framing of the core problem

> "You have now verified your domain ownership — You are the Super Administrator of this organization, create your domain based email address" — Zoho success screen, March 6, 2026

> "The link seemed to work" — Brayden confirming the direct Zoho free plan URL worked after the main pricing page didn't show it

***

## STEP 3 — POST-ENTRY REPORT

1. **Canonical files to update:** CTRL-YOU-STATUS (primary), BRAYDEN-IDENTITY (secondary — add Ctrl+You as a confirmed business project with domain)

2. **New file needed?** Not strictly — this fits under CTRL-YOU-STATUS. However, if Ctrl+You grows in scope across multiple threads, a dedicated **CTRL-YOU-INFRASTRUCTURE.md** file covering DNS, email, hosting, and tech stack decisions would be warranted. Recommend folding into CTRL-YOU-STATUS for now and splitting later if needed.

3. **Potential conflicts to flag:**
   - **Kray Studios vs. Ctrl+You**: Multiple other brain entries reference "Kray Studios" as the primary Shopify dropshipping brand. This thread introduces `ctrlplusyou.com` as a separate Shopify store. These may be the same project under a name change, two simultaneous projects, or one replaced the other. This is the most important conflict to resolve at compilation.
   - The Shopify store "Opening soon" status here (March 6, 2026) may conflict with more developed store descriptions in other entries — check dates.

4. **One-line cross-reference tag:**
`BE-20260306-PROJECT-ctrlplusyou-email-dns-setup.md` — Ctrl+You domain registered, Zoho Mail free plan activated, DNS setup walkthrough for `support@ctrlplusyou.com`

***

## STEP 4 — FILE NAME

```
BE-20260306-PROJECT-ctrlplusyou-email-dns-setup.md
```

***

⚙️ *This entry was generated in an isolated thread. Entry ID, supersedes field, chronological position, and cross-references are unconfirmed until the full compilation session. During that session: assign IDs in date order, resolve contradictions (especially Kray Studios vs. Ctrl+You brand identity), deduplicate facts across entries, and push confirmed updates to canonical files.*