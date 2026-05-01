---
title: YouTube Project
filename: YOUTUBE-PROJECT.md
updated: 2026-04-30
status: ACTIVE
domain: YOUTUBE
priority: 2
tags: youtube, braydondon, faceless, content, commongrounds, brainos, local-ai, video, piper-tts, whisper, n8n
canonical_file: ACTIVE-PROJECTS.md
cross-references:
  - ACTIVE-PROJECTS.md
  - BRAINOS-SYSTEM.md
  - BRAYDEN-IDENTITY.md
  - COMMONGROUNDS-PROJECT.md
  - DEVICE-ECOSYSTEM.md
note: Two active tracks. BrayDonDon is the personal channel — the honest one. Track A is the income engine. They compound each other but must be built independently.
---

## Overview

YouTube is a compound interest machine for Brayden's life, brand, and income — not a performance. The primary audience for early content is future Brayden first. Authenticity is the moat. CommonGrounds and the Skool community are downstream beneficiaries of everything this channel produces.

There are two tracks running in parallel at different priority levels:

| Track | Channel Name | Format | Status | Unlocked By |
|-------|-------------|--------|--------|-------------|
| Personal / Learn-in-Public | BrayDonDon | Screen capture, voiceover, face optional | Planned — first video blocked on Whisper install | Whisper running locally |
| Faceless AI-Assisted | TBD | n8n pipeline, auto-scripted, auto-assembled | Planned — blocked on n8n + Ollama desktop | Daily note habit + Ollama confirmed on desktop |

---

## Track 1 — BrayDonDon (Personal Channel)

### What It Is

Learn-in-public documentation of building BrainOS, running a local AI stack as a DSP/caregiver, and living the system. This is the honest channel — not a tutorial factory. Content is real-time, imperfect, and compound.

The channel is a creative identity vehicle first, income vehicle second. The worldview IS the identity. No polished personal brand required early.

### Format Notes

- Faceless or face — your call. Screen recordings + voiceover work completely.
- PiperTTS flagged for free local voiceover — not yet installed.
- No studio required. Garage right side (rug zone) earmarked as filming/relaxing space. Back wall planned as green screen wall — not yet built.
- No editing suite required for first video. OBS + screen capture is enough.

### Existing Raw Footage

| File | Type | Status |
|------|------|--------|
| Garage cleanup timelapse | OBS recording — long, unedited | RAW — not indexed |
| OBS screen recordings | Long, silent, uncut | RAW — not indexed |
| iPhone screen recordings | Silent, long, visually flat | RAW — not indexed |

None of these are broken. They are unprocessed. The friction is a pipeline problem, not a content problem.

### Status

| Item | Status |
|------|--------|
| Channel created | UNCONFIRMED |
| First video concept chosen | NOT DONE |
| Whisper installed | NOT INSTALLED — this is the gate |
| PiperTTS installed | NOT INSTALLED |
| Garage filming wall | PLANNED — not built |

### Next 3 Steps (in order)

1. Install Whisper locally on laptop (estimate: one afternoon, ~2 hours)
2. Choose ONE anchor concept — write one paragraph pitching it
3. Record first video — screen capture of Whisper setup with honest commentary

---

## Track 2 — Faceless AI-Assisted (Automation Pipeline)

### What It Is

A 5-phase n8n automation pipeline: trend scrape → script generation → voiceover → video assembly → publish. Target: 35 minutes/day human time after setup. Income-focused. Feeds the CtrlYou Shopify ecosystem and CommonGrounds brand downstream.

### Pipeline Architecture (Planned)

```
Trend Scrape → Script Gen (Ollama) → Voiceover (PiperTTS) → Video Assembly → Auto-Publish
```

### Blockers (hard — do not start until cleared)

- Daily note habit established in Obsidian
- Ollama confirmed running on desktop (Ryzen 7 7700X, RTX 3060 12GB)
- n8n has zero active workflows as of 2026-04-30 — not yet operational

### Status

| Item | Status |
|------|--------|
| n8n installed | YES — v2.17.6 |
| Ollama on desktop | Downloaded — install UNCONFIRMED |
| Daily note habit | NOT ESTABLISHED |
| Any workflows active | NO |
| First workflow designed | NO |

### Next Step

Do not build. Establish daily note habit first. This track unlocks after that.

---

## How the Two Tracks Connect

BrayDonDon content (honest, personal, skill-documenting) organically builds the audience that Track A monetizes. CommonGrounds packages the system BrayDonDon documents. Skool sells the community. Everything compounds — but only if BrayDonDon starts first.

```
BrayDonDon (trust) → CommonGrounds (system) → Skool (community + revenue)
                    ↘ Track A (volume + reach) ↗
```

---

## Open-Source Local AI Stack for Video Production

| Tool | Purpose | Status |
|------|---------|--------|
| Whisper / faster-whisper | Transcription, timestamped indexing of all footage | NOT INSTALLED — primary gate |
| Auto-Editor | Silence removal, dead air compression — no timeline scrubbing | NOT INSTALLED |
| FFmpeg | Backbone — cutting, merging, transcoding, subtitle injection | UNCONFIRMED |
| LLaVA / Moondream | Vision LLM — analyze frames, describe scenes, extract on-screen text | NOT INSTALLED |
| Ollama + local LLM | Script structuring from transcripts (Mistral 7B, LLaMA 3) | Desktop install UNCONFIRMED |
| ComfyUI + Flux.1 | Thumbnail and graphic generation | Desktop — pending full setup |
| PiperTTS | Free local voiceover generation | NOT INSTALLED |
| n8n v2.17.6 | Eventual automation layer connecting full pipeline | INSTALLED — zero active workflows |
| DaVinci Resolve (free) | Full GUI editing suite, best-in-class color grading | UNCONFIRMED |

### The Full Pipeline Vision

```
Record → Auto-Editor (silence removal) → Whisper (transcription + timestamps)
→ LLM (chapters + descriptions) → FFmpeg (final assembly) → ComfyUI (thumbnail)
→ n8n (publish + schedule)
```

Every piece is free, local, and runs on hardware already owned. Setup time is also content for BrayDonDon.

---

## Footage Management System

### Capture Rules (apply immediately after every recording)

1. **Rename the file** — format: `YYYYMMDD-topic-device.mp4` (e.g. `20260430-garage-timelapse-obs.mp4`)
2. **Voice-stamp the opening** — say out loud what the recording is, even if silent after. Whisper will index it.
3. **Drop in RAW-FOOTAGE** — single folder on the 2TB external drive. Nothing gets sorted until Whisper processes it.

### The Silent Video Problem — Two Solutions

**Option 1 — Post-narration:** Record screen, then play it back and talk over it like a director's commentary. FFmpeg merges audio and video in ~30 seconds.

**Option 2 — Auto-Editor first:** Run Auto-Editor on the long file before watching it. Removes dead air based on audio thresholds. A 60-minute silent OBS recording can compress to 10–15 minutes of actual activity. Then decide if it's worth narrating.

### Whisper as Filing System (once installed)

1. Drop raw file in `RAW-FOOTAGE`
2. Run Whisper — catches spoken words, system sounds, voice stamp
3. Whisper outputs timestamped `.txt` and `.srt` alongside the video
4. Read the transcript in 60 seconds instead of watching 45 minutes
5. Decide: clip it, narrate it, or archive it

### Storage Architecture

| Layer | Location | Purpose |
|-------|----------|---------|
| Working files | 2TB external drive — `RAW-FOOTAGE/` | Primary capture destination |
| Long-term backup | TBD — redundant solution needed | External drives are not safe as sole backup |
| Archive / cloud | 2TB iCloud — keep subscription for now | Exit after local backup workflow is confirmed |

**iCloud note:** Do not cancel the iCloud subscription until a confirmed, tested local backup workflow exists. Finance section conversation — low priority right now.

---

## Income Projection

Track A is the income-first track. No confirmed figures yet — projections require channel niche, upload cadence, and monetization path to be defined first.

CommonGrounds Skool downstream potential (from ACTIVE-PROJECTS.md):
- Free tier → 3% conversion → 24 paid members at $49 = **$1,176 MRR passively**
- One 10-day challenge event at $67, 8% conversion = **~$8,000 weekend**

YouTube ad revenue is downstream of these — not the primary income mechanism in Phase 1.

---

## Shelved / Superseded

| Item | Reason |
|------|--------|
| Kray Studios brand | Replaced by CtrlYou, March 14, 2026 |
| AIChannelAutomationBlueprint | Revisit when n8n workflows resume |
