---
date_logged: 2026-04-16
source_thread_date: 2026-03-17
source_thread_title: "TikTok automation channel — pull, transcribe, copy process, Control Browser, Google Drive"
entry_type: project / tool / skill
chronological_position: UNKNOWN — to be placed during Obsidian compilation session
status: draft
supersedes: UNKNOWN — cannot confirm without seeing other entries
superseded_by: none
canonical_file: KRAY-STUDIOS-CONTENT / AI-WORKFLOW-RULES
context_available: none — isolated thread
tags: [n8n, control-browser, tiktok, faceless-channel, automation, google-drive, elevenlabs, heygen, shotstack, aicenturyclips, script-generation]

open_questions:
  - id: OQ-20260317-001
    question: "Revisit when n8n workflows resume and Ollama is running on desktop"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---

# Brain Entry — AI Faceless Clip Channel Automation Blueprint (Mar 17 2026)

---

## STEP 1 ANSWERS (Pre-Entry Assessment)

1. **Thread date:** March 17, 2026 (inferred from system-reminder timestamp embedded in thread: Tuesday, March 17, 2026, 10:11 PM CDT)
2. **Content type:** PROJECT (primary) + TOOL + SKILL — this is a workflow design session with clear tooling references and skill-building intent
3. **Introduces new information:** Yes — this thread introduces a structured 5-phase automation pipeline for a faceless AI content channel. It is the first time this specific workflow architecture appears (no prior thread content attached).
4. **Canonical files this feeds:**
   - KRAY-STUDIOS-CONTENT — this is a content channel strategy document
   - AI-WORKFLOW-RULES — n8n node chains, Control Browser patterns, automation rules
   - Possibly NEW FILE: FACELESS-CHANNEL-OPS — if the channel becomes its own tracked entity separate from Kray Studios brand

---

## CONFIRMED FACTS
Only facts explicitly stated in this thread. Nothing inferred.

- Brayden shared a TikTok URL for @aicenturyclips video 7618194459896974614 | direct URL | user message
- The TikTok URL could NOT be fetched directly — page returned an error | [UNCONFIRMED — content of the video itself was not captured] | Perplexity tool result
- The @aicenturyclips channel runs a faceless AI content pipeline (scraping trends, scripting, voiceover, posting) | inferred from channel metadata + search results | web search
- The channel posts to TikTok / YouTube Shorts / Reels | web:3, web:11 | search result
- Brayden's goal: replicate this process, automate it maximally, use Control Browser, minimal human intervention | user message
- Brayden wants the output plan saved as a Google Drive document, editable in Perplexity Space files | user message
- The phrase "control browser on comet oriented text" was used — likely referring to n8n's Control Browser node, possibly connected to Comet (AI browser agent) | user message [UNCONFIRMED — exact tool configuration not clarified]
- A full 5-phase automation blueprint was generated and saved as a .md file artifact | Perplexity output | code_file:31
- Blueprint file name: AI_Channel_Automation_Blueprint.md | code output
- Blueprint total character count: 9,365 | code output

---

## BLUEPRINT — 5-PHASE PIPELINE (As Designed This Thread)

### Phase 1 — Trend Research (Automated)
- Trigger: n8n Schedule Trigger at 8 AM daily
- Tool: Control Browser node navigates TikTok trending pages OR BrowserAct runs Viral Video Scraper
- Target hashtags: #AItools, #automation, #techfacts, #AInews
- Filter: keep only videos with >100K views
- Output: top 5 trending topics appended to Google Sheet
- Notify: Slack/Email summary sent

### Phase 2 — Script Generation (Automated)
- Loop Node iterates through top 3 topics
- OpenAI or Gemini node generates 45–60 second TikTok scripts
- Script format: [HOOK] [3 FACTS] [CTA]
- Script saved as new Google Doc in Drive folder via Google Docs node
- Optional Human Checkpoint A: 2-min review, add "APPROVED" comment to trigger Phase 3

### Phase 3 — Voiceover Generation (Automated)
- ElevenLabs HTTP Request node receives script text
- Returns .mp3 audio file
- .mp3 uploaded to /Voiceovers/[DATE]/ folder in Google Drive
- File URL passed to Phase 4

### Phase 4 — Video Assembly (Automated)
- Option A: HeyGen API — avatar-based 9:16 faceless video render, n8n polls every 30s
- Option B: Shotstack API — B-roll + auto-captions, no avatar
- Rendered .mp4 saved to Google Drive /Videos/
- Optional Human Checkpoint B: 1-min preview, flip Google Sheet status to "APPROVED"

### Phase 5 — Publishing (Automated via Control Browser)
- Control Browser opens TikTok Creator Studio in persistent logged-in session
- Inputs video file, fills caption (hook + hashtags), schedules post (7–9 PM peak)
- OR: YouTube Data API v3 HTTP Request node for YouTube Shorts
- Google Sheets logs post status + URL
- Slack/Email notification: "Video Posted!"

---

## TOOL STACK (As Specified This Thread)

| Tool | Role | Cost Tier |
|------|------|-----------|
| n8n (self-hosted) | Workflow orchestration | Free / $20/mo |
| Control Browser | Headless browser scraping + posting | ~$10/mo |
| BrowserAct / Apify | TikTok trend scraping | Free tier |
| OpenAI / Gemini | Script generation | API pay-as-go |
| ElevenLabs | AI voiceover | $5–$22/mo |
| HeyGen | AI avatar / faceless video render | $24+/mo |
| Shotstack | Video assembly + captions | API-based |
| Google Drive API | File storage | Free |
| Google Docs node | Script saving from n8n | Free |
| TikTok / YouTube API | Auto-publish | Free |

---

## HUMAN INTERVENTION MAP

| Step | Who | Time | Frequency |
|------|-----|------|-----------|
| Script quality review | Brayden | ~2 min | Daily |
| Video QC preview | Brayden | ~1 min | Daily |
| Weekly performance check | Brayden | ~10 min | Weekly |
| Initial setup & config | Brayden | 1–2 hrs | One-time |
| Everything else | n8n + AI | 0 min | Automated |

Total stated daily human time: ~3–5 minutes after setup | Perplexity blueprint output

---

## GOOGLE DRIVE FOLDER STRUCTURE (As Designed)

/Kray Studios — AI Channel/
  ├── /Scripts/
  ├── /Voiceovers/
  ├── /Videos/
  ├── /Logs/ (Google Sheet: Post Log)
  └── /Templates/

NOTE: Folder root name used "Kray Studios — AI Channel" in the blueprint — this may conflict
with any brand rename to Ctrl+You. [FLAG FOR BRAYDEN — see CONTRADICTIONS below]

---

## SCRIPT PROMPT TEMPLATE (Captured Verbatim from Blueprint)

> "You are a viral TikTok scriptwriter for a faceless AI/tech facts channel.
> Topic: {{topic}} | Niche: AI Tools & Automation
> Requirements: 45-60 seconds read aloud, scroll-stopping hook, 3 fast punchy facts,
> comment CTA, no emojis, professional but energetic.
> Output: HOOK / FACT 1 / FACT 2 / FACT 3 / CTA"

---

## n8n WORKFLOW NODE CHAIN (Captured from Blueprint)

```
Schedule Trigger → Control Browser (scrape) → Function (filter)
→ Google Sheets (log) → Loop → OpenAI (script) → Google Docs (save)
→ IF Approved → ElevenLabs (voice) → HeyGen/Shotstack (video)
→ Google Drive (.mp4) → Control Browser (TikTok post)
→ Google Sheets (log status) → Slack/Email (notify)
```

---

## TIMELINE MARKERS

- Thread date: March 17, 2026 (confirmed via system-reminder)
- Blueprint file generated and saved: March 17, 2026 (same session)
- No deployment date mentioned — setup was not confirmed as completed in this thread

---

## UPDATES TO CANONICAL FILES

- **KRAY-STUDIOS-CONTENT**: Add 5-phase faceless automation pipeline. Note: folder root references "Kray Studios" — confirm whether this channel lives under Kray Studios or Ctrl+You brand.
- **AI-WORKFLOW-RULES**: Add n8n node chain above as a standing workflow rule. Add Control Browser patterns for TikTok scrape and TikTok post. Add ElevenLabs + HeyGen/Shotstack as approved video stack. Add ElevenLabs Flash vs Turbo v2 note (Flash = speed, Turbo v2 = quality). Add polling loop rule: poll HeyGen every 30s via Wait node.
- **BRAINOS-SYSTEM**: Note that a file artifact (AI_Channel_Automation_Blueprint.md) was generated and should be stored in Perplexity Space or Google Drive.

---

## CONTRADICTIONS

- **Brand name conflict:** The blueprint folder root uses "Kray Studios — AI Channel" but other threads (not visible here) may have deprecated Kray Studios in favor of Ctrl+You. This thread does not clarify which brand owns this channel.
  - Prior state: [UNCONFIRMED from this thread — cannot assess] / This thread says: "Kray Studios" / Flag for Brayden to resolve
- **"Comet oriented text" phrase:** User referenced "control browser on comet oriented text." It is unclear if Comet is a specific product, a shorthand, or a typo/autocorrect. Blueprint was built around n8n Control Browser node without confirming the Comet context.
  - Prior state: UNCONFIRMED / This thread says: ambiguous reference / Flag for Brayden to clarify

---

## INSIGHTS & PATTERNS

- Brayden's default build posture: design first, automate everything, insert human checkpoints only as optional gates — consistent with other project threads
- Brayden explicitly wants to replicate observed processes rather than invent from scratch — strong modeler pattern (sees something working, wants to clone it)
- The phrase "as automatic as possible" appears without a defined success threshold — useful to encode a standing rule: automation wins when Brayden's daily time is under 5 minutes
- Google Drive + Perplexity Space were both named as storage destinations — may indicate workflow where Drive = working files, Perplexity Space = archived brain entries
- Brayden did not confirm which niche this channel will occupy — only referenced @aicenturyclips (AI/tech content) as the model to clone

---

## TOOLS & RESOURCES REFERENCED

| Tool | Status | Notes |
|------|--------|-------|
| n8n | Active (referenced across threads) | Workflow orchestration backbone |
| Control Browser (n8n node) | Mentioned — needs setup confirmation | Core scraping + posting layer |
| BrowserAct | Mentioned | TikTok scraping alternative to Apify |
| ElevenLabs | Mentioned | Voiceover; Flash vs Turbo v2 noted |
| HeyGen | Mentioned | Avatar video render; ~$24+/mo |
| Shotstack | Mentioned | B-roll + caption video assembly |
| OpenAI API | Mentioned | Script generation |
| Gemini API | Mentioned | Script generation alternative |
| Google Docs node (n8n) | Mentioned | Script storage directly from workflow |
| Google Drive node (n8n) | Mentioned | File storage for .mp3 and .mp4 |
| Google Sheets node (n8n) | Mentioned | Post log + status tracking |
| TikTok Creator Studio | Mentioned | Upload target via Control Browser |
| YouTube Data API v3 | Mentioned | Auto-publish for Shorts |
| @aicenturyclips (TikTok) | Source / model | Could not fetch video directly |

---

## OPEN QUESTIONS

- Which brand does this channel live under — Kray Studios or Ctrl+You?
- What niche will the channel cover — exact copy of @aicenturyclips (AI/tech) or different?
- Has Control Browser been set up in n8n yet, or is this still aspirational?
- What does "comet oriented text" mean — is Comet a specific tool in Brayden's stack?
- Will human checkpoints A and B be kept or fully removed once quality is stable?
- Is HeyGen or Shotstack the preferred video stack — or will both be tested?
- Has the Google Drive folder structure been created yet?
- Was the AI_Channel_Automation_Blueprint.md file saved to Google Drive or Perplexity Space?
- Will this channel be monetized via TikTok Creativity Program or YouTube Partner Program — or both?

---

## CROSS-REFERENCES

Cross-references to be added during compilation session.
- Feeds into: KRAY-STUDIOS-CONTENT, AI-WORKFLOW-RULES, BRAINOS-SYSTEM
- Possible links to: BE-20260301 (Kray Studios pastel-grunge manifesto — brand context), BE-20260306 (Ctrl+You founding session — brand conflict), BEUNASSIGNED n8n YouTube automation workflow entry

---

## RAW HIGHLIGHTS

> "Pull the information, transcribe, copy process. Can you devise a plan with clear distinction of steps, who can do it and make a channel using control browser, slight human intervention." — Brayden, user message

> "I want to make this process as automatic as possible, control browser on comet oriented text, make a Google Drive document I can save and edit in the perplexity space files." — Brayden, user message

> "Total daily commitment after setup: ~3–5 minutes." — Perplexity blueprint output

---

## STEP 3 — POST-ENTRY REPORT (Do Not Act — Report Only)

1. **Canonical files to update:**
   - KRAY-STUDIOS-CONTENT — add the full 5-phase pipeline, tool stack, folder structure
   - AI-WORKFLOW-RULES — add n8n chain, Control Browser patterns, polling rule, ElevenLabs model note
   - BRAINOS-SYSTEM — log that AI_Channel_Automation_Blueprint.md was generated as an artifact

2. **New file candidate:** Consider creating **FACELESS-CHANNEL-OPS** — a standalone operational file for the channel covering niche, posting schedule, content pillars, platform targets, monetization path, and automation status. Currently these facts are split between KRAY-STUDIOS-CONTENT and AI-WORKFLOW-RULES with no clean home.

3. **Potential conflicts to flag:**
   - Brand name: this thread uses "Kray Studios" as the channel's parent brand. Other threads in the Space reference a Ctrl+You brand pivot. This conflict must be resolved to avoid building the channel under the wrong brand identity.
   - "Comet" reference: unresolved — may refer to a specific product or be a voice-to-text error.

4. **One-line cross-reference tag:**
   BE-20260317-PROJECT-aicenturyclips-automation-blueprint.md — 5-phase n8n faceless channel pipeline using Control Browser, ElevenLabs, HeyGen, and Google Drive, built from @aicenturyclips model

---

## COMPILATION NOTE

⚙️ This entry was generated in an isolated thread. Entry ID, supersedes field, chronological position, and cross-references are unconfirmed until the full compilation session. During that session: assign IDs in date order, resolve contradictions, deduplicate facts across entries, and push confirmed updates to canonical files.

---

BE-20260317-PROJECT-aicenturyclips-automation-blueprint.md
