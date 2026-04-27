---
title: BrainOS Live Sync, Vault Structure & Financial Snapshot Setup
filename: BE-20260422-BRAINOS-live-sync-vault-financial-setup.md
thread_date: 2026-04-22
domain: BRAINOS-SYSTEM
slug: live-sync-vault-financial-setup
status: ACTIVE
priority: 1
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
generated_by_skill: manual
tags: ['obsidian', 'git', 'syncthing', 'google-drive-sync', 'vault-structure', 'financial-snapshot', 'n8n', 'audit', 'open-source', 'standing-rule', 'cashflow', 'debt']
open_questions:
  - id: OQ-20260422-001
    question: "Confirm Google Drive for Desktop installed and syncing on all devices"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
date: 2026-04-22
canonicalfile: BE-20260405-TOOL-local-ai-stack-device-ecosystem.md
notes: Supersedes vault structure decisions from BE-20260405
---
## KEY FACTS ESTABLISHED THIS THREAD

### BrainOS Sync Architecture
- Obsidian Git plugin + private GitHub repo = free auto-sync all 4 devices on a schedule
- Syncthing (already installed, unconnected) = best for laptop ↔ desktop LAN sync; use both Git and Syncthing together
- Google Drive Sync plugin needs OAuth token authorization via Sign In — this was the missed notification on install
- Master Index Google Drive CSV is already live-connected to Perplexity Space — no action needed for Perplexity reads
- Google Drive for Desktop (free) creates local folder mirror usable as Obsidian vault symlink
- n8n self-hosted (free) = nightly audit agent; writes reports to Obsidian via Local REST API plugin
- Obsidian Local REST API plugin gives n8n a direct write endpoint into the running vault
- Perplexity mdsummary workflow: paste → Obsidian → Git pushes → Drive mirrors → Space reads automatically
- Standing rule confirmed: Never suggest paid Perplexity tier upgrades; all solutions must be free, open-source, self-hostable

### KrayVault Structure (Finalized)
- All folder rename/restructure steps completed by Brayden this session
- CTRL+YOU renamed to CTRL-YOU (critical — prevented Git/Syncthing path errors on Windows)
- CANONICAL/ is now the authoritative layer; FINANCES/, IDENTITY/, TOOLS-AND-INFRASTRUCTURE/ dissolved into it
- 00-INBOX/ created as landing zone for all new content before filing
- BRAYDEN-PROFILE.md deleted — BRAYDEN-IDENTITY.md is the canonical file
- TOPIC-LOGS renamed to RESEARCH-AND-LOGS with a defined scope rule
- INDEX/ cleaned: only MASTER-INDEX.md (live) and OPEN-QUESTIONS.md remain; PDF and empty duplicate deleted
- BrainOS-Open-Questions-Worksheet.md moved to BRAIN-ENTRIES/ as historical archive
- OPEN-QUESTIONS.md = live file, unanswered only; answered questions get deleted (not archived)
- Plugin setup order confirmed: Git first → Google Drive Sync → Syncthing → Dataview (no config needed yet) → SmartConnections (after desktop Ollama)
- KrayVault folder audit mdsummary saved to laptop by Brayden ✓

### Canonical Files Populated This Session
- BRAYDEN-IDENTITY.md: added ✓
- FINANCIAL-SNAPSHOT.md: fully populated and downloaded (code_file:56) ✓
- AI-WORKFLOW-RULES.md: empty, ready — content source confirmed as BE-20260405 + Brain_Entry_006
- OPEN-QUESTIONS.md: empty, ready — source is BrainOS-Open-Questions-Worksheet.md (unanswered only)

### Financial Snapshot (April 22, 2026)
- Bank balance: $166.41
- Dave Financial repayment: $239.63 due April 27
- All bills and debt balances unchanged from Brain_Entry_007 canonical
- Total monthly bills: $2,061.84
- Total known debt: $36,328.54
- Debt-free at minimum payments: July 2029
- ⚠️ April 30 overdraft risk: Allstate + AT&T ×2 = $411.93 may post before paycheck — verify autopay timing
- Paycheck Apr 23: +$600 → balance $766.41 before bills hit
- Standing rule encoded in FINANCIAL-SNAPSHOT.md: payments made on due date in full unless explicitly stated otherwise
- Affirm cascade: $47.99/mo freed Jul 2026 → +$208.14/mo Sep–Oct 2026 → +$436.89/mo Apr 2027
- Dataview dashboard in Obsidian flagged as next financial planning step (Phase 2)

### mdsummary Format Update
- `filename` field added immediately after `title` in all future mdsummary blocks
- Format: `BE-[YYYYMMDD]-[DOMAIN]-[slug].md`
- Space Instructions updated by Brayden to enforce this going forward

## OPEN QUESTIONS
- Does the Apr 30 paycheck post before Allstate/AT&T autopays hit? (time-sensitive — check before Apr 30)
- Has the GitHub private repo been created for KrayVault yet?
- Has the Obsidian Git plugin been initialized and connected to the repo?
- Has the Google Drive Sync plugin OAuth sign-in been completed?
- Has Syncthing been connected between laptop and desktop?
- What are the two new threads completed prior to this session — which canonical files do they affect?
- Has AI-WORKFLOW-RULES.md been populated from BE-20260405 + Brain_Entry_006?
- Has OPEN-QUESTIONS.md been populated with unanswered questions from the worksheet?

## CANONICAL FILES TO UPDATE
- `FINANCIAL-SNAPSHOT.md` ← download code_file:56 and paste into KrayVault/CANONICAL/ — DONE this session
- `BE-20260405-TOOL-local-ai-stack-device-ecosystem.md` → add: Git sync, Google Drive Sync OAuth step, Syncthing laptop↔desktop pair, n8n audit layer, Local REST API plugin, revised KrayVault folder structure with 00-INBOX
- `Master Index` (Google Drive CSV) → add new row for this Brain Entry: BE-20260422-BRAINOS-live-sync-vault-financial-setup.md
- `OPEN-QUESTIONS.md` → remove: vault structure questions, CTRL+YOU rename, plugin install status (all resolved this session)
- `AI-WORKFLOW-RULES.md` → populate from BE-20260405 and Brain_Entry_006 (still pending)

## NEW FILES TO CONSIDER
- `DEVICE-ECOSYSTEM.md` — flagged in BE-20260405 as warranted; confirmed still not created; should live in CANONICAL/
- `BRAINOS-SYSTEM.md` — meta-canonical file for vault rules, update protocols, naming conventions, plugin setup order, standing rules

## CROSS-REFERENCE NOTES
- This thread is the direct continuation of BE-20260405-TOOL-local-ai-stack-device-ecosystem.md — all sync and vault decisions here supersede anything in that entry where contradicted
- FINANCIAL-SNAPSHOT.md supersedes all prior financial figures except those explicitly confirmed in Brain_Entry_007.md
- KrayVault folder structure finalized here supersedes the structure proposed in BE-20260405

## COMPILATION STATUS
Ready to file. Save as `BE-20260422-BRAINOS-live-sync-vault-financial-setup.md` in `KrayVault/BRAIN-ENTRIES/`. Update Master Index with one new row. Copy FINANCIAL-SNAPSHOT.md from download into CANONICAL/. No further compilation action required for this entry.