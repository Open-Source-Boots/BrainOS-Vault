---
title: "BrainOS Triage Layer + ShiftMind Founding Thread"
filename: "BE-20260425-BRAINOS-triage-shiftmind-founding.md"
date: 2026-04-25
domain: BRAINOS-SYSTEM
slug: triage-shiftmind-founding
status: ACTIVE
canonicalfile: "BRAINOS-SYSTEM.md"
tags: [brainos, triage, vision, shiftmind, whisper, local-ai, residential-care, obsidian, groundwork, naming, python, voice-transcription, hipaa, goodlife, proof-of-concept, business]
open_questions:
  - id: OQ-20260425-001
    question: "Run first Whisper test"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-002
    question: "create COMMONGROUNDS-PROJECT.md"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-003
    question: "update all canonical files from this session"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---
Key Facts
BrainOS diagnosis confirmed: System was growing laterally (more files, more schemas, more tools) without growing deeper into actual use; no declared endgame existed until this thread

Three canonical files that operationally matter: BRAYDEN-IDENTITY.md ✅, FINANCIAL-SNAPSHOT.md ✅, ACTIVE-PROJECTS.md ❌ still needs creation

File-move sync bug: git add -A (not git add .) required after every Obsidian file move to capture renames and deletions the plugin misses

n8n formally deprioritized — installed but no workflows; do not build until daily note habit exists

Obsidian explained at highest level: A map of relationships between ideas, not just a file editor; Dataview turns vault into a live personal database; Smart Connections uses RAG to give a local LLM targeted access to relevant files without hitting context window limits

Context window reality: Local models max at 8k–32k tokens; Smart Connections RAG retrieves only the 5–10 most relevant files per query — vault can scale to thousands of notes safely

Python confirmed installed: Python 3.14.4 on laptop ✅

Whisper: OpenAI open-source transcription model, fully local, no internet required; install via pip install -U openai-whisper after FFmpeg is installed via Chocolatey; start with base model on laptop CPU

ShiftMind concept born this thread: Local-first, voice-first care intelligence system for residential homes; staff leave voice memos → Whisper transcribes → filed to Obsidian vault → Ollama answers staff questions from accumulated shift history; HIPAA-safe, zero cloud, everything stays in the building

ShiftMind selling points: HIPAA-local argument, staff turnover knowledge retention, audit-ready timestamped documentation, complementary to GoodLife's existing iLink system (not competitive)

ShiftMind phases confirmed: Phase 1 proof of concept at 602 N. Wrigley; Phase 3 paid implementation services to GoodLife homes and comparable providers

Name "ShiftMind" rejected by Brayden — terms like "AI" and "Open-source" alienating; "local" derivatives preferred

"Groundwork" name conflict: Groundwork AI (Brooklyn, active), thegroundwork.ai (active), GroundWork Open Source (acquired 2022) — plain "Groundwork" and "Groundwork AI" are taken; modifier required

10 alternative name directions generated — Brayden's favorites undecided; Groundwork Care, Groundwork Home, Groundwork Local, CommonGrounds, HomeGrounds, Groundkeep, TrueGround, RootWork, Groundwell, LayGrounds all generated this thread

Name legal check required: USPTO TESS search at tmsearch.uspto.gov, Class 42 (software) and Class 44 (healthcare) before committing to any name or purchasing a domain

Core business insight: Every frustration building BrainOS for yourself is R&D for ShiftMind; document what breaks, what got simplified, what got abandoned — that becomes the product's foundation

CtrlYou confirmed dormant — no outreach sent, no products established, no active direction as of this thread

Open Questions
Which name direction feels right for ShiftMind — warm/human, institutional/trustworthy, or minimal/plain? Does "Groundwork + X" stay the leading candidate?

Have you run the first Whisper test yet — record 60 seconds, transcribe locally, check accuracy?

Is ACTIVE-PROJECTS.md going to be created this session, or deferred?

Which projects are genuinely active right now vs. dormant — ShiftMind and Electrician path appear active; GLWC paused; CtrlYou/YouTube dormant. Is that accurate?

Has a daily note habit started in Obsidian even once since this conversation began?

Do you want to keep the Hostinger VPS subscription or let it expire and redirect those funds/energy toward local-only infrastructure?

Canonical Files to Update
BRAINOS-SYSTEM.md — add endgame vision (daily note → 3 canonical files → local AI answers questions); git add -A rule; n8n deprioritized; Obsidian/Dataview/Smart Connections explanations; context window reality and RAG explanation

ACTIVE-PROJECTS.md — create this file; add ShiftMind as Phase 1 active, next action: run first Whisper test; add Electrician/Peaslee as active, next action: follow up on waitlist and Phyllis Gingette WIOA call

BRAYDEN-IDENTITY.md — add ShiftMind as new active project and business concept; add Python 3.14.4 confirmed on laptop; add Whisper not yet installed but setup steps confirmed

New File to Consider
SHIFTMIND-PROJECT.md in CANONICAL/ — stub file, create after first Whisper test confirms feasibility; full framing document generated in this thread and ready to paste

Cross-Reference Note
ShiftMind is a parallel track to GLWC — both emerge from the same lived experience at GoodLife, but operate on completely different postures: GLWC is advocacy, ShiftMind is innovation. Keep them logically separated in the vault and in any GoodLife-facing conversations

ShiftMind cross-links to: BE-20260327-PROJECT-goodlife-union-founding-research.md (GoodLife iLink context), BE-20260411-PROJECT-glwc-doclog-space-audit.md (care documentation gaps), BE-20260405-TOOL-local-ai-stack-device-ecosystem.md (Ollama, Obsidian stack)

Compilation Status
READY TO SAVE. Paste into 00-inbox as BE-20260425-BRAINOS-triage-shiftmind-founding.md. Primary actions before next thread: (1) create ACTIVE-PROJECTS.md, (2) run first Whisper test, (3) add Master Index row for this entry and for the ShiftMind project stub.