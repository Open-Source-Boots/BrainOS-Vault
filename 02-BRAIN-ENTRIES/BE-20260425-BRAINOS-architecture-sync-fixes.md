---
title: BrainOS Architecture Redesign + Sync Fixes
filename: BE-20260425-BRAINOS-architecture-sync-fixes.md
thread_date: 2026-04-25
domain: BRAINOS-SYSTEM
slug: architecture-sync-fixes
status: ACTIVE
priority: 1
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
generated_by_skill: manual
tags: ['brainos', 'vault-structure', 'master-index', 'raw-wiki-output', 'obsidian', 'git', 'syncthing', 'token', 'n8n', 'dataview', 'CommonGrounds']
date: 2026-04-25
canonicalfile: BRAINOS-SYSTEM.md
notes: Predates this compilation session by hours — seed data drafted here was the 13-row precursor to today's full 48-row migration
open_questions:
  - id: OQ-20260425-001
    question: "Create MASTER-INDEX.md Dataview dashboard"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-002
    question: "create 99-OUTBOX/ folder"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-003
    question: "create COMMONGROUNDS-PROJECT.md stub"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260425-004
    question: "rename legacy Google Sheet to MASTER-INDEX-LEGACY in Drive"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---
Key Facts:

Raw/Wiki/Output framing confirmed as cleaner mental model than Canonical/Brain-Entry/Outbox naming; folder structure unchanged, thinking model updated

Google Drive for Desktop replaces Google Drive Sync plugin — file moves now work correctly

MASTER-INDEX.csv not visible in Obsidian — requires companion MASTER-INDEX.md with Dataview queries to display; CSV is machine-readable only

Laptop GitHub PAT: no expiration. iPhone GitHub PAT: expires May 22, 2026 — renew in Obsidian Git settings before that date

n8n formally deprioritized — no workflows until daily note habit + desktop Ollama running

New MASTER-INDEX.csv seed data drafted this session: 13 rows covering confirmed canonical entries; legacy Google Sheet migration deferred to dedicated session

Open Questions:

Is MASTER-INDEX.md (with Dataview queries) created and rendering correctly in Obsidian?

Has 99-OUTBOX/ folder been created in vault?

Has COMMONGROUNDS-PROJECT.md stub been created in 03-PROJECTS/?

Has the legacy Google Sheet been renamed to MASTER-INDEX-LEGACY in Drive?

Has the first Whisper test been run?

Canonical files to update:

BRAINOS-SYSTEM.md — add Raw/Wiki/Output mental model; n8n deprioritized rule; CSV+Dataview index pattern; Google Drive for Desktop confirmed over plugin

ACTIVE-PROJECTS.md — add CommonGrounds Phase 1 as active; Electrician path as active; all others as paused/dormant

05-INDEX/MASTER-INDEX.csv — paste seed data from this session

New files to create:

05-INDEX/MASTER-INDEX.md — Dataview dashboard (template provided above)

03-PROJECTS/COMMONGROUNDS-PROJECT.md — stub, populate after first Whisper test

Compilation status: Ready to file. Save to 02-BRAIN-ENTRIES/.