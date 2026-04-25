entry_id: [UNASSIGNED — assign when compiled with other entries]
date_logged: 2026-04-16
source_thread_date: 2026-04-16
source_thread_title: "Accessing n8n for the first time — Source Media automation and video pipeline"
entry_type: tool / ai-system / project / skill
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: KRAY-STUDIOS-CONTENT / AI-WORKFLOW-RULES / [NEW: N8N-AUTOMATION-PIPELINE]
context_available: none — isolated thread
tags: [n8n, automation, video-pipeline, media-sourcing, public-domain, faceless-youtube, voiceover, scripting, google-sheets]

---

# Brain Entry [UNASSIGNED] — First n8n session: media scraping, repository building, and automated video pipeline planning

---

## 🔒 CONFIRMED FACTS (explicitly stated in this thread only)

| Fact | Value | Where in Thread |
|------|-------|----------------|
| Brayden's first time using n8n | Confirmed — first-time user as of this thread | Thread opening |
| Access device | iPad | Thread opening |
| First node placed | HTTP Request node pointed at a Wikipedia URL | Brayden's message |
| Target repository | Google Sheets | Brayden's message |
| Content sourcing principle | Free and open source only | Brayden's message |
| Intended output | Automated video creation, editing, and posting | Brayden's message |
| Scripting tool recommended | OpenAI GPT-4o via native n8n node | AI response |
| Voiceover option 1 | ElevenLabs API — $0.30/1,000 characters | AI response |
| Voiceover option 2 | OpenAI TTS — $0.015/1,000 characters | AI response |
| Voiceover option 3 (FOSS) | PiperTTS — self-hosted, free | AI response |
| Image generation option 1 | DALL-E 3 — $0.04/image | AI response |
| Image generation option 2 | Flux via Replicate — $0.10/image | AI response |
| Image generation option 3 (FOSS) | Stable Diffusion — free, local setup | AI response |
| Video assembly option 1 | Creatomate — REST API, template-based | AI response |
| Video assembly option 2 | JSON2Video — JSON-driven REST API | AI response |
| Video assembly option 3 (FOSS) | OpenShot Cloud API — free | AI response |
| Google Sheets credential setup | Requires Google Cloud Console OAuth 2.0 — Sheets API + Drive API | AI response |
| Public domain sources recommended | Wikimedia Commons, Internet Archive, Pexels, Pixabay, Prelinger Archives, Library of Congress, Vidsplay, Mazwai, Openverse, NPS B-Roll | AI response |
| Trend API sources recommended | Google Trends API, SearchAPI, BrightData, SerpAPI | AI response |
| Implementation roadmap length | 4 phases across approximately 8 weeks | AI response |
| Thumbnail generation recommended | DALL-E 3 integrated via n8n | AI response |
| SEO automation approach | GPT-4o titles + Google Trends keywords + YouTube Analytics API | AI response |

---

## 🕐 TIMELINE MARKERS

- **2026-04-16** — First n8n session initiated on iPad; HTTP Request node placed with Wikipedia URL; Google Sheets chosen as repository target
- **[UNCONFIRMED]** — No prior n8n experience stated; this appears to be Day 1 of this workflow system
- **Phase roadmap suggested**: Weeks 1–2 basic automation, Weeks 3–4 advanced features, Weeks 5–6 optimization, Weeks 7–8 scale — all prospective/planned, none confirmed as started

---

## 📋 UPDATES TO CANONICAL FILES

- **KRAY-STUDIOS-CONTENT:** Add section documenting n8n as the automation backbone for video creation; log the planned pipeline (scrape → repository → script → voiceover → video assembly → publish); note FOSS-first sourcing principle
- **AI-WORKFLOW-RULES:** Add n8n node architecture notes — HTTP Request → Function → IF → Google Sheets flow; document expression syntax `{{ $json.fieldName }}`; add credential management rule (store in n8n credential system, never inline); add testing rule (test node-by-node before activating)
- **[NEW: N8N-AUTOMATION-PIPELINE]:** Create this file. Should contain full node map, credential requirements, public domain source URLs, trend API URLs, video assembly options, voiceover options, scripting prompts, SEO automation logic, and 8-week implementation roadmap

---

## ⚠️ CONTRADICTIONS

- Cannot assess — thread is isolated. Flag for review during compilation.
- **Potential flag**: Thread recommends OpenAI GPT-4o and commercial APIs (ElevenLabs, Creatomate, DALL-E) alongside FOSS alternatives. Brayden explicitly stated "free and open source" as a principle. This tension between cost-incurring tools and FOSS principle should be flagged for Brayden to resolve — decide which tools are acceptable spend vs. which must be replaced with FOSS equivalents.

---

## 🧠 INSIGHTS & PATTERNS

- Brayden is approaching this system from scratch with no prior n8n experience — documentation and step-by-step node instructions are essential scaffolding for this project
- The FOSS principle is a stated constraint, but the recommended stack includes paid APIs — this is a recurring pattern worth watching: ideal vs. practical tooling tension
- This pipeline (scrape → sort → script → voice → assemble → publish) is a significant infrastructure build; breaking into phases is consistent with Brayden's documented project management style
- Google Sheets is being used as an interim database — this may need to upgrade to Airtable or a proper database if volume scales
- Brayden's use of "second-brain archivist" framing confirms active BrainOS system is in use and this thread should be compiled into it

---

## 🔧 TOOLS / RESOURCES REFERENCED

| Tool / Resource | Status | Notes |
|----------------|--------|-------|
| n8n | In use — Day 1 | Browser-based, accessed via iPad |
| HTTP Request Node | Placed — Wikipedia URL | First node configured |
| Google Sheets | Target repository | OAuth credentials required |
| Google Cloud Console | Setup required | OAuth 2.0 for Sheets + Drive API |
| OpenAI GPT-4o | Recommended | Scriptwriting via native n8n node |
| ElevenLabs API | Recommended (paid) | Voiceover — $0.30/1k chars |
| OpenAI TTS | Recommended (paid) | Voiceover — $0.015/1k chars |
| PiperTTS | Recommended (FOSS) | Self-hosted voiceover |
| DALL-E 3 | Recommended (paid) | Thumbnails — $0.04/image |
| Stable Diffusion | Recommended (FOSS) | Local image generation |
| Creatomate | Recommended (paid) | Video assembly REST API |
| OpenShot Cloud API | Recommended (FOSS) | Video assembly |
| JSON2Video | Recommended | REST API video generation |
| Wikimedia Commons | Sourcing URL confirmed | Public domain video/images |
| Internet Archive | Sourcing URL confirmed | Public domain films |
| Pexels | Sourcing URL confirmed | Royalty-free video |
| Pixabay | Sourcing URL confirmed | Free video library |
| Prelinger Archives | Sourcing URL confirmed | Historical public domain films |
| Library of Congress | Sourcing URL confirmed | National Screening Room |
| Mazwai | Sourcing URL confirmed | Creative Commons HD clips |
| Openverse | Sourcing URL confirmed | Creative Commons search |
| SerpAPI | Trend data | Google Trends via API |
| Google Trends API | Trend data | Native Google developer API |
| YouTube Analytics API | Analytics | Free — performance feedback loop |

---

## ❓ OPEN QUESTIONS

- Which tools in the stack will Brayden commit to — full FOSS or hybrid paid/free?
- Has Google Cloud Console OAuth been set up yet, or is this still pending?
- What niche(s) will the first Kray Studios video channel target?
- Will the Google Sheets repository be the permanent solution or a stepping stone to Airtable/database?
- Has PiperTTS or Stable Diffusion been installed locally, or are these still theoretical?
- Which phase of the 8-week roadmap is Brayden starting on as of this thread?
- Where will assembled video files be stored before upload — local iPad, Google Drive, or cloud bucket?
- What platforms beyond YouTube are in scope for automated publishing?

---

## 🔗 CROSS-REFERENCES

- Feeds into: `KRAY-STUDIOS-CONTENT`, `AI-WORKFLOW-RULES`, `[NEW: N8N-AUTOMATION-PIPELINE]`
- Possible links to: Any prior entries covering Kray Studios content strategy, Shopify/dropshipping pipeline, or AI tool usage — confirm during compilation

---

## 📥 RAW HIGHLIGHTS

> "I put the Wikipedia link into the http request, but I do not know what to do beyond this point to start collecting a repository on Google Sheets to save relevant film and media in an organized way so I can begin the next step of editing and posting these videos." — Brayden, establishing current skill level and goal

> "I want to just get to where n8n is compiling educated media in the repository, but I want you to consider what nodes we will add after this to begin an automated editing process." — Brayden, defining scope

> "Again, this should be on the principles of free and open source for the sourcing, automation, and posting these videos." — Brayden, stating core constraint

> "You are acting as my second-brain archivist." — Brayden, confirming BrainOS system is active

---

> ⚙️ This entry was generated in an isolated thread. `entry_id`, `supersedes`, `chronological_position`, and cross-references are unconfirmed until the full compilation session. During that session: assign ID by thread date, resolve contradictions, deduplicate facts, and update canonical files.