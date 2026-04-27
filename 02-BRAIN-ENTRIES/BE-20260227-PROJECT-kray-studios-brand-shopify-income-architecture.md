---
filename: BE-20260227-PROJECT-kray-studios-brand-shopify-income-architecture.md
thread_date: 2026-02-27
domain: ONLINE-BUSINESS
status: SUPERSEDED
priority: 3
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: FINANCIAL-SNAPSHOT.md
generated_by_skill: manual
tags: []
notes: Kray Studios survives only as parent company name; CtrlYou is the active consumer brand
open_questions:
  - id: OQ-20260227-001
    question: "None — brand deprecated March 14 2026"
    canonical_target: ACTIVE-PROJECTS.md
    status: OPEN
---
date_logged: 2026-04-16
source_thread_date: 2026-02-27
source_thread_title: "If I asked you to completely build Cray Studios' brand website — everything that we've talked about during this space"
entry_type: mixed (project / financial / skill / tool)
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: KRAY-STUDIOS-CONTENT (primary); FINANCIAL-SNAPSHOT; SKILLS-EDUCATION; BRAYDEN-IDENTITY; BRAINOS-SYSTEM
context_available: Hub-Version-Spec.md, Swatch-Name-Hex-Role.csv, when-i-click-download-as-html-where-is-that-going.docx, So-lets-begin.md, business-planning-fmkToKDzTSWdkBkw2Pwspw.md — all visible in Space at time of entry
tags: [kray-studios, shopify, nxe-design, income-streams, ad-consulting, dropshipping, brand-identity, hub-dashboard, adhd, cashflow, debt-snowball, owner-dashboard]

---

# Brain Entry — Kray Studios website build, NXE brand identity, income stream architecture, and owner hub development (Feb 2026)

## CONFIRMED FACTS

### Identity / Project
- Business name: Kray Studios | stated in thread
- Shopify store URL: fyti4j-00.myshopify.com | stated in thread
- Shopify theme installed: Publisher | stated in thread
- Shopify Dawn theme was discussed as initial option but Publisher confirmed as active | stated in thread
- Kray Studios is a tech/gaming-adjacent dropshipping and brand store | stated in thread
- Brand aesthetic: Xbox 360 NXE (New Xbox Experience) 2008–2010 dashboard style | stated in thread
- Secondary aesthetic inspiration: Concertina/Blades early Xbox 360 dashboard | stated in thread
- Windows Media Center (Vista era) also cited as NXE visual reference | stated in thread
- Business bank account: US Bank business account | stated in thread
- Business location: Lawrence, Kansas | stated in thread

### Brand Identity (CONFIRMED)
- Primary color — NXE Green: #52B043 | Swatch-Name-Hex-Role.csv
- Secondary color — Amber Gold: #F5A623 | Swatch-Name-Hex-Role.csv
- Neutral Dark — Deep Charcoal: #1A1F1A | Swatch-Name-Hex-Role.csv
- Neutral Light — Sage: #D8E8D0 | Swatch-Name-Hex-Role.csv
- Text Primary — Off White: #F0F0F0 | Swatch-Name-Hex-Role.csv
- Text Muted — Cool Gray: #8A9A8A | Swatch-Name-Hex-Role.csv
- Logo font (display/wordmark): Orbitron Black/ExtraBold | stated in thread
- Body/UI font: Exo 2 SemiBold/Bold | stated in thread
- Label/badge font: Rajdhani SemiBold 600 | stated in thread
- Brand tagline mentioned: "Built Different" | stated in thread
- Brand founding marker: EST. 2026 | stated in thread

### Financial (CONFIRMED — stated explicitly in thread)
- Monthly income from Goodlife Innovations only: $2,400/month | stated in thread
- No other confirmed income sources at time of thread | stated in thread
- OneMain Loan minimum: $515/month | stated in thread
- BestEgg Loan minimum: $411/month | stated in thread
- Car payment: $350/month, due on the 15th | stated in thread
- Insurance estimate: ~$120/month [flagged as estimate in thread — confirm real number] | stated in thread
- Phone/WiFi estimate: ~$80/month [flagged as estimate in thread] | stated in thread
- Affirm estimate: ~$50/month [flagged as estimate in thread] | stated in thread
- Card minimums combined: $205/month across 5 cards | stated in thread
- Total obligations: $1,731/month [sum stated in thread — AI calculated, not Brayden confirmed] | stated in thread
- True free cash remainder: $669/month [AI calculated — flag for Brayden to verify] | stated in thread

### Debt Snowball Order (CONFIRMED from Hub-Version-Spec.md)
1. Amazon Store Card — $147 balance, $59 utilization — KILL FIRST | stated in file
2. PayPal Cashback MC — $489 — Kill second | stated in file
3. Amazon Prime Visa — $1,299, 100% utilization — Kill third | stated in file
4. Discover it Cash Back — $2,767, 101% utilization — Kill fourth | stated in file
5. Capital One VentureOne — $3,161, 102% utilization — Kill fifth | stated in file
6. BestEgg Loan — $7,693, $411/month minimum | stated in file
7. OneMain Loan — $14,417, $515/month minimum | stated in file
- Total debt stated: $29,973 | stated in file

### Project — Shopify Build
- kray-hero.liquid created as a custom Shopify section for Publisher theme | stated in thread
- Section structure: scrolling ticker bar, hero, trust bar, product shelf, featured product, brand story, email capture, toast notifications | stated in thread
- Product shelf is drag-scrollable with momentum (NXE horizontal scroll style) | stated in thread
- Section is drag-and-droppable in Shopify Customize once installed | stated in thread
- Bug fixed: invalid Liquid date pipe chain on line 480 removed in v2 | stated in thread
- Google Fonts import moved to layout/theme.liquid to resolve linter warning | stated in thread
- Two separate deliverables created: customer storefront + owner dashboard | stated in thread
- Storefront filename (latest version referenced): kraystudiosstorefrontv3.html | stated in thread
- Owner dashboard filename (latest version referenced): kraystudioshubv3.html / kray-studios-hub-v4.html | stated in thread (versions referenced interchangeably — flag for resolution)
- Hub uses localStorage with key prefix: kray- | Hub-Version-Spec.md
- Hub has 12 navigation panels in latest described version | stated in thread
- Hub panels: Dashboard, Tasks, Cash Flow, Shopify Setup, Sourcing, Dennis DeMarino, Facebook Ads, Kalodata, Ad Consulting, Tools, Finances, Palette | stated in thread
- Hub persists: checkboxes, debt paid status, achievement log, last active tab, wins log | Hub-Version-Spec.md
- Facebook Ads tab locked until first organic sale | stated in thread
- Hub restoreAll() must run on DOMContentLoaded | Hub-Version-Spec.md
- saveCheck fires on every checkbox change | Hub-Version-Spec.md
- Bottom bar shows: Next Bill name/amount/days, Free Cash, Income | Hub-Version-Spec.md

### Project — Income Streams
- Stream 1: Ad Consulting — fastest path, leverages Logical Position background | stated in thread
- Stream 2: Kray Studios Dropshipping — Shopify/CJ Dropshipping, sleep revenue | stated in thread
- Stream 3: Digital Products — future play, not yet active | stated in thread
- POD (Print on Demand) explicitly removed from plan | stated in thread
- Ad consulting offer: free 30-day trial, client controls budget, Looker Studio reporting | stated in thread
- Target retainer after free month: $500–$1,000/month per client | stated in thread
- Ad consulting certifications needed: Google Ads Search (free, Skillshop, 3–5 hrs) + Meta Blueprint | stated in thread
- CRM recommended: HubSpot free tier | stated in thread
- Prospecting target: 10 Lawrence KS businesses per week | stated in thread
- Follow-up rule: 80% of sales happen between 5th–12th contact | stated in thread

### Project — Kalodata Workflow (CONFIRMED from Hub-Version-Spec.md)
- Filter: Category, Units Sold 100+/month | stated in file
- Filter: Growth Rate 20%+ | stated in file
- Filter: Listing Age under 90 days | stated in file
- Filter: Creator Count 5+ | stated in file
- Filter: Price $15–$60 | stated in file
- Cross-validate on Amazon: 200+ reviews required | stated in file
- Source on CJ Dropshipping, confirm US warehouse | stated in file
- Kalodata platform score noted: 8.5/10 ease of use, 8/10 ad spy — from cited review dated Feb 22, 2026 | stated in thread
- Kalodata paid plan: ~$50/month (free trial sufficient for first 3–5 product validations per thread) | stated in thread

### Tools Referenced
- CJ Dropshipping: primary supplier, free, US warehouse | stated in thread
- Zendrop: backup supplier, Free/$49 | stated in thread
- Trendsi: fashion/accessories, free | stated in thread
- Spocket: $39.99/month | stated in thread
- Faire: wholesale, net-60 terms, free | stated in thread
- AutoDS: $26.90/month, multi-source | stated in thread
- Snaptik.app: TikTok video downloader, free | stated in thread
- ezgif.com: video to GIF converter, free | stated in thread
- Erank.com: Etsy SEO keyword research, free | stated in thread
- Looker Studio: Google reporting tool for ad consulting client dashboards | stated in thread
- HubSpot CRM: free tier, prospect tracking | stated in thread
- Judge.me: review app, free tier | stated in thread
- Loox: review app | stated in thread
- EffortlessPOD: POD automation tool (noted but POD removed from plan) | stated in thread
- Canva: design tool, free tier | stated in thread

### Dennis DeMarino Video Lessons (confirmed from thread)
- Source: YouTube channel TheDennisDeMarino | stated in thread
- Video 1 (6K05O7cb0vk): Shopify landing page 3-part framework | stated in thread
- 3-part formula: The Fold / The Sell / The Trust | stated in thread
- Rule: never use emojis in headlines | stated in thread
- Rule: never end a headline with punctuation | stated in thread
- Rule: GIFs must be square format | stated in thread
- Video 2 (9NWSev70M0): "The Simplest Facebook Ads Strategy In 2025 To Scale To $50,000/Month As A Complete Beginner" | stated in thread (title confirmed by Brayden)
- Facebook Ads core: CBO campaign, broad targeting, $50–$100/day test budget | stated in thread
- Duplicate winning ad sets to scale — do not raise budget on existing winner | stated in thread

---

## TIMELINE MARKERS
- Thread date: February 27, 2026 (confirmed by system reminder) — 12:13 PM CST first message, 12:16 PM CST second message
- Shopify 3-day trial was active at time of thread (3 days remaining stated)
- $1/3-month Shopify offer mentioned as next step after trial
- kray-hero.liquid v2 bug fix occurred within this thread's session
- Hub v3 and v4 were both generated within this thread session
- Dennis DeMarino video summaries occurred in this session
- Storefront v3 generated in this session

---

## UPDATES TO CANONICAL FILES

- **KRAY-STUDIOS-CONTENT**: Add full brand identity (colors, fonts, tagline, aesthetic DNA). Add Shopify store URL and theme. Add two-file system (storefront vs. owner hub). Add Dennis DeMarino framework. Add Kalodata 8-step workflow. Add supplier stack. Add income stream prioritization (consulting first, dropshipping second, digital products third). Add hub panel list and localStorage spec.
- **FINANCIAL-SNAPSHOT**: Add debt snowball order with exact figures. Add cashflow obligations breakdown with due dates. Add true remainder $669 (flag as AI-calculated — needs Brayden verification). Flag Insurance, Phone/WiFi, Affirm as estimates.
- **BRAYDEN-IDENTITY**: Add ADHD-specific execution gaps (time blindness, follow-up failure, imposter syndrome pattern, avoidance of scary outreach). Add 25-minute Pomodoro structure as recommended daily workflow. Add accountability need noted.
- **SKILLS-EDUCATION**: Add Google Ads Search certification as pending (Skillshop, free, 3–5 hours). Add Meta Blueprint as next after that. Add HubSpot CRM setup as tool skill to acquire. Add Kalodata as active product research skill.
- **BRAINOS-SYSTEM**: Add hub architecture spec: localStorage key prefix kray-, restoreAll on DOMContentLoaded, saveCheck on every checkbox, two-file split (customer vs. owner). Add note that hub is device/browser specific — not cross-device without re-downloading.

---

## CONTRADICTIONS
- Cannot fully assess — thread is partially isolated. However:
- **Hub version naming**: Thread references both "v3" and "v4" as the most recent version at different points. The v4 is described as the latest with all features merged, but v3 is described as Brayden's "visual favorite." Which is the canonical current file is unresolved. Flag for Brayden to confirm which file is active.
- **Storefront vs. Hub filename**: kraystudioshubv3.html and kray-studios-hub-v4.html are both referenced — possible that these are different iterations from within the same session but the naming is inconsistent. Flag.
- **$669 free cash**: AI-calculated figure, not Brayden-confirmed. Insurance, Phone/WiFi, and Affirm are flagged as estimates within the thread itself. Do not treat as canonical until Brayden confirms.
- **Debt total $29,973**: Stated in Hub-Version-Spec.md file in the Space. Not independently re-confirmed by Brayden verbally in this thread. Carry with caution — cross-check at compilation.
- **Prior entries (Brain_Entry_007.md) state debt as "~$36k"** — this thread's Hub-Version-Spec.md states $29,973. Conflict exists. Flag for Brayden to resolve. Do not average or assume which is correct.

---

## INSIGHTS & PATTERNS
- Brayden built a highly detailed brand/tool system but had zero products and zero clients at thread close — execution gap is the primary blocker, not information gap
- ADHD time blindness acknowledged: realistic productive time is ~12 hours/week in 25-min blocks, not the apparent 60–70 hours of "free time"
- Pattern: seeking "perfect" (logo iterations, hub versions) before shipping — flagged in thread itself as a risk
- Hub serves as an externalized ADHD brain — dopamine via win-logging is by design, not decoration
- Follow-up discipline (5–12 touchpoints) is where most people fail; HubSpot CRM is the structural fix
- First scary step = outreach message to one business; all other systems are ready
- Accountability needs are explicit: Brayden stated he needs external check-ins to execute
- "Perfect is the enemy of launched" — stated directly in thread as a standing rule
- The gap between knowledge and action was the stated theme of the entire driving lesson

---

## TOOLS & RESOURCES REFERENCED
- Shopify (Publisher theme) | active — store live at fyti4j-00.myshopify.com | Shopify trial active at thread date
- CJ Dropshipping | active — primary supplier app | needs products imported
- Zendrop | mentioned — backup supplier | not yet installed
- Trendsi | mentioned — fashion/lifestyle option | not yet installed
- HubSpot CRM | needs setup | free tier, for ad consulting pipeline
- Kalodata | active — 8-step workflow built into hub | paid plan ~$50/month; free trial recommended for first 3–5 validations
- Google Skillshop | needs action — Google Ads Search cert | free, 3–5 hours
- Meta Blueprint | needs action — Facebook Ads cert | free, self-paced
- Looker Studio | mentioned — for client reporting | free, Google product
- Canva | active | free tier for design
- snaptik.app | mentioned — TikTok video download | free
- ezgif.com | mentioned — video to GIF | free
- Erank.com | mentioned — Etsy keyword research | free (note: POD removed from plan, may still be relevant for keyword logic)
- Judge.me | mentioned — Shopify review app | free tier
- HubSpot | needs setup | free CRM for consulting pipeline
- VS Code | recommended for HTML file editing | free

---

## OPEN QUESTIONS
- Which hub file is the canonical current version — v3 (visual favorite) or v4 (most features)?
- Have Insurance, Phone/WiFi, and Affirm amounts been confirmed since this thread?
- Has Google Ads Search certification been completed since February 27, 2026?
- Has any outreach to Lawrence KS businesses been attempted?
- Has any product been imported to the Shopify store?
- Has the store password been removed (is the store publicly accessible)?
- Is Shopify Payments connected?
- What happened with the $1/3-month Shopify trial — was it activated?
- Has any CJ Dropshipping product been sourced and validated via Kalodata?
- Has the debt total been confirmed — $29,973 (this thread) vs. ~$36k (cited in BE-007)?
- Has the Amazon Store Card ($147) been paid off since this thread?
- Was the Peaslee Tech / electrician path active at this point or did it come later?

---

## CROSS-REFERENCES
Cross-references to be added during compilation session.
- Feeds into: KRAY-STUDIOS-CONTENT, FINANCIAL-SNAPSHOT, BRAYDEN-IDENTITY, SKILLS-EDUCATION, BRAINOS-SYSTEM
- Possible links to: Brain_Entry_007.md (debt figures conflict), Brain_Entry_003.md (ctrl+you Shopify build — possible parallel Shopify project), Hub-Version-Spec.md (canonical design rules for hub), MASTER-CONTEXT.md (referenced in thread as key Space file)

---

## RAW HIGHLIGHTS

> "You have the blueprint. You have the tools. You have the brand. You have the time. What you don't have is your first client, your first sale, and your first win logged." — closing income lesson

> "Perfect is the enemy of launched." — stated as standing rule during income lesson

> "Your ADHD brain needs external accountability, body doubling, and deadline pressure." — stated directly in income lesson

> "The gap isn't knowledge — it's action." — stated directly in income lesson

> "I want the theme of Kray Studios to be like the early Xbox 360 dashboard and aesthetic." — Brayden, initiating the brand direction

> "I want whatever you generate to be transferable, automatically, to Shopify so the website can at least have a framework I can edit as I go." — Brayden, on Shopify transferability requirement

> "POD out for now, not assume we can reach goals because we said we could. Income is currently only from my job at Goodlife." — Brayden, grounding the plan in reality

> "I hate the logo. It's completely stuck on the geometric digital lettering and it needs to change." — Brayden, on logo iteration process

> "visually this was my favorite" — Brayden, referring to kraystudioshubv3.html layout