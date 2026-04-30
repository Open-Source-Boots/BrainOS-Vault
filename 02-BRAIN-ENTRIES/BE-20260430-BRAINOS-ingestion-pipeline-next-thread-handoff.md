---
title: "BrainOS Ingestion Pipeline — next-thread handoff and device ecosystem expansion"
filename: "BE-20260430-BRAINOS-ingestion-pipeline-next-thread-handoff.md"
date: 2026-04-30
domain: BRAINOS-SYSTEM
slug: ingestion-pipeline-next-thread-handoff
status: ACTIVE
compilation_status: COMPLETE
supersedes: null
superseded_by: null
canonical_file: BRAINOS-SYSTEM.md
tags:
  - brainos
  - ingestion
  - automation
  - rag
  - ai-workflow
  - device-ecosystem
  - obsidian
  - google-drive
  - git
  - local-ai
  - next-thread
open_questions:
  - id: OQ-20260430-013
    question: "What is the first source type we should automate end-to-end in the intake pipeline: receipts, bank statements, legal forms, transcripts, or books?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260430-014
    question: "What should the universal inbox folder be named and where should it live in the vault so capture is fastest from all devices?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-015
    question: "Which extraction method should be canonical for scanned documents on desktop first: OCR to text, OCR plus summary, or OCR plus structured field extraction?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260430-016
    question: "Which device should own the first always-on automation trigger for new intake files: desktop, laptop, iPhone, or iPad?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260430-017
    question: "Should Brain Entries remain the primary durable memory layer, or should a separate extracted-knowledge layer be added for long-term RAG retrieval?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-018
    question: "Which metadata fields are mandatory on every inbound file so the system can route, classify, and learn from it without manual reformatting?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260430-019
    question: "Should the iPad Air 5th generation be treated primarily as a capture, reading, or review device in the four-device ecosystem?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260430-020
    question: "What is the minimum viable local-AI task each device should own first so the ecosystem is distributed by function instead of duplicated?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---
KEY FACTS
BrainOS should now be treated as an ingestion pipeline, not just a note archive.
The suggested next update path is: BRAINOS-SYSTEM.md first, AI-WORKFLOW-RULES.md second, DEVICE-ECOSYSTEM.md third.
The intake goal is to make it easy to feed receipts, bank statements, legal forms, research, books, transcripts, and documents into the system with minimal formatting friction.
The four-device ecosystem should be organized around distinct roles: laptop, desktop/PC, iPhone, and iPad Air 5th generation.
The desktop/PC is the long-term primary local-AI host, but it is not yet fully set up.
The iPhone and laptop currently have the most infrastructure in place.

TIMELINE MARKERS
2026-04-30 09:43 — BRAINOS system canonical updated for index automation and Shell Commands path.
2026-04-30 12:55 — User requested automation expansion and multi-device AI ecosystem direction.
2026-04-30 13:02 — User requested /mdsummary handoff for the next thread.

UPDATES TO CANONICAL FILES
BRAINOS-SYSTEM.md should gain an ingestion architecture section: universal inbox, auto-digest, canonical memory, and review loop.
AI-WORKFLOW-RULES.md should gain rules for low-friction intake, source-type handling, and RAG-ready extraction without forcing format upfront.
DEVICE-ECOSYSTEM.md should be updated to reflect iPad Air 5th generation and a four-device ecosystem with different roles and future local-model responsibilities.
The suggested update path should be preserved explicitly so the next thread can continue without re-discovery: BRAINOS-SYSTEM first, AI-WORKFLOW-RULES second, DEVICE-ECOSYSTEM third.

CONTRADICTIONS
The earlier assumption that the iPad was a 5th gen standard iPad is now superseded by the new confirmation that it is an iPad Air 5th generation.
The system should not assume the desktop is already the primary AI node; it is the intended future host, not the current operational center.

INSIGHTS & PATTERNS
The real bottleneck is not model intelligence but intake friction: if capture requires too much formatting, the system will fail before retrieval matters.
The best architecture is to accept messy raw inputs first and let automation normalize them later, which matches BrainOS’s existing map → triage → compile → update → index → plan sequence.
This is the right time to define one universal intake path before expanding into multiple source-specific pipelines, because that reduces re-entry cost and keeps the next thread focused.
The next thread should not reopen strategy from scratch; it should start by drafting canonical edits and choosing the first source type to automate end-to-end.

TOOLS & RESOURCES REFERENCED
Shell Commands Obsidian plugin for desktop-triggered automation.

utils/rebuild_index.py as the confirmed working index generator.

CROSS-REFERENCES
BRAINOS-SYSTEM.md — architecture, ingestion, index generation, and build sequence.
AI-WORKFLOW-RULES.md — operational guardrails for intake, file writes, and automation.
DEVICE-ECOSYSTEM.md — device roles, AI placement, and hardware readiness.
FINANCIAL-SNAPSHOT.md — eventually relevant if intake extends to statements and financial documents, but not updated in this thread.

RAW HIGHLIGHTS
“The brain entries feeding things.”
“Plug in receipts, bank statements, legal forms, research, documents, books, transcripts.”
“Easily feed data and info, without spending too long trying to format or index it correctly.”
“The second brain digest and learn from the data points, remembering everything with the RAG system.”
“Eventually local, open-source ai models will run primarily through the desktop/pc.”
“The laptop and iphone are about the only things with any infrastructure right now.”
“Each of those four devices [should] run their own local ai models, suited to their respective strengths.”