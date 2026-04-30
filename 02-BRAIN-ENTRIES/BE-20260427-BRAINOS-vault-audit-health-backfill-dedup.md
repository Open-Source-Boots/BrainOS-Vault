---
title: "BrainOS Vault Audit — Gitignore, Health Check, Dedup, Backfill, OQ Injection"
filename: BE-20260427-BRAINOS-vault-audit-health-backfill-dedup.md
date: 2026-04-27
domain: BRAINOS
slug: vault-audit-health-backfill-dedup
status: active
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
tags: [brainos, vault, git, gitignore, health-check, dedup, backfill, open-questions, syncthing, automation]
open_questions:
  - id: OQ-20260427-001
    question: "Does the current log_dedup_fix.py plan correctly handle the case where the same OQ ID was answered under two different canonical targets — and should the newer or older answer be preserved as canonical?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-002
    question: "Should GOODLIFE-UNION-answers.md be fully migrated into ACTIVE-PROJECTS-answers.md, or should its content be split between ACTIVE-PROJECTS.md and FINANCIAL-SNAPSHOT.md based on question type?"
    canonical_target: ACTIVE-PROJECTS.md
    status: CLOSED
  - id: OQ-20260427-003
    question: "What is the exact trigger condition that should flip SCHEDULED_ACTIVATION = True in review_financial_questions.py — a specific dollar threshold in FINANCIAL-SNAPSHOT, a transaction pipeline being live, or both?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260427-004
    question: "Should vault_health_check.py be added to a scheduled task or git hook so it runs automatically before every commit, rather than manually?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-005
    question: "Are the 7 malformed YAML files safe to repair by wrapping colon-containing values in quotes, or do any of them contain content that would change meaning when quoted?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260427-006
    question: "Is .smart-env/event_logs/event_logs.ajson generated fresh each session, or does Smart Connections depend on its persisted history for any RAG or memory function?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED
  - id: OQ-20260427-007
    question: "Should the BEUNASSIGNED_ and Brain_Entry_00X files be formally renamed to the canonical BE-YYYYMMDD-DOMAIN-slug.md format, and is there a safe automated rename + CSV update path?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-008
    question: "Does Mobius Sync on iPhone interact with .stfolder differently than Syncthing does on desktop — specifically, does it create its own marker files that should also be gitignored?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED
  - id: OQ-20260427-009
    question: "What is the minimum viable FINANCIAL-SNAPSHOT.md structure needed before review_financial_questions.py can go live — which specific fields must be confirmed non-empty?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260427-010
    question: "If inject_open_questions.py re-routes a question's canonical_target after an answer has already been logged under the old target, what is the correct reconciliation protocol — move the answer log entry, leave it, or flag it?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-011
    question: "Should log_dedup_fix.py preserve the timestamp of the first occurrence of a duplicate OQ entry, or should it use the most recent one as canonical?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-012
    question: "Is the double-extension file BE-20260427-BRAINOS-canonical-compilation-business-architecture.md.md a one-off naming error or evidence of a pattern in how a specific device or tool creates files?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260427-013
    question: "Should workspace-mobile.json be gitignored globally or only per-device via a local .git/info/exclude so iPhone and iPad Obsidian state is never accidentally committed from any machine?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260427-014
    question: "At what vault size (number of BEs, canonical files, or OQ count) does the current single-pass Python script architecture become a performance bottleneck that warrants moving to a SQLite-backed index?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260427-015
    question: "Does the current backfill_frontmatter.py correctly handle files where frontmatter exists but is partially malformed — does it skip the whole file or attempt partial repair?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---

## KEY FACTS

- Vault state at session start: 59 BEs on disk, 55 in MASTER-INDEX.csv, 4 unindexed
- `backfill_frontmatter.py` ran successfully: Modified 50, Skipped 5, Not Found 0
- `inject_open_questions.py` ran successfully: Modified 55, Skipped 0, Not Found 0
- `log_dedup.py` found 29 duplicate OQ IDs across 54 total unique IDs in 06-ANSWERS
- 7 malformed YAML files identified — all unresolved, queued for tomorrow
- `vault_health_check.py` found 49 files missing required frontmatter fields, 7 malformed YAML, 7 orphaned OQs
- All orphaned OQs target either `GOODLIFE-UNION.md` (dead) or `GLWC-PROJECT.md` (dead) — correct target is `ACTIVE-PROJECTS.md`
- Final commit of session: `cd253a2` — untracked `workspace.json` and `event_logs.ajson` from Git

## TIMELINE MARKERS

- ~01:35 CDT — Session opened, vault audit tasked
- ~01:40 CDT — `.gitignore` device-aware overhaul pushed, `review_financial_questions.py` scaffold pushed
- ~01:42 CDT — `git pull` confirmed clean on Desktop, all 6 new files landed
- ~01:43 CDT — `vault_health_check.py` first run, full report captured
- ~01:45 CDT — `backfill_frontmatter.py` and `inject_open_questions.py` both run successfully
- ~01:46 CDT — `log_dedup.py` run, 29 duplicate IDs identified, report saved
- ~01:47 CDT — Full session commit pushed: `6333e29`, 58 files, 469 insertions
- ~01:49 CDT — `workspace.json` and `event_logs.ajson` untracked from Git: `cd253a2`
- ~01:50 CDT — Session closed

## UPDATES TO CANONICAL FILES

- **BRAINOS-SYSTEM.md** — Add: `utils/log_dedup_fix.py` is planned but not yet built; answer log dedup is a known open problem. Add: recommended post-session script run order is documented in `utils/README.md`.
- **DEVICE-ECOSYSTEM.md** — Add: `.gitignore` now has device-specific sections for Windows, macOS/iPhone/iPad, iCloud, and Syncthing. `workspace-mobile.json` explicitly ignored for iPhone/iPad Obsidian state. `.stfolder` and `.stfolder.removed-*` must never be deleted from local filesystem.
- **FINANCIAL-SNAPSHOT.md** — Add: `review_financial_questions.py` exists at repo root with `SCHEDULED_ACTIVATION = False` gate. Three activation criteria documented in file.

## CONTRADICTIONS

- `inject_open_questions.py` was fixed earlier in this session to route GOODLIFE/GLWC keywords to `ACTIVE-PROJECTS.md`, but 7 OQs already written directly into frontmatter by hand still target dead files. The script fix is live; the legacy OQs are not yet patched.
- `log_dedup.py` reports 29 duplicate IDs, but the majority are caused by `review_questions.py` appending the same answer block multiple times — not by genuinely conflicting answers. The dedup count overstates actual data conflict severity.

## INSIGHTS & PATTERNS

- The vault's oldest files (`Brain_Entry_001–010`, `BEUNASSIGNED_*`) predate the current frontmatter spec entirely and represent accumulated technical debt from BrainOS v1. The backfill pass addressed most of them structurally but they still need YAML repair and proper renaming.
- Duplicate OQ IDs in answer logs are a `review_questions.py` write-logic bug, not a data integrity failure. The fix is straightforward: check for existing ID before appending. This is the highest-priority script fix for next session.
- The `.obsidian/workspace.json` and `.smart-env/event_logs/` files being tracked by Git were silently generating commit noise on every device. Untracking them eliminates a whole class of cross-device conflict risk.
- Pattern B duplicates (same ID, different canonical target files) are a migration artifact from canonical target re-routing. A protocol needs to be established: when `inject_open_questions.py` changes a `canonical_target`, it should emit a migration notice so the answer log entry can follow.

## TOOLS & RESOURCES REFERENCED

- `utils/vault_health_check.py` — structural integrity check, read-only
- `utils/log_dedup.py` — answer log duplicate OQ ID scanner, read-only
- `utils/README.md` — script documentation, run order, activation gate notes
- `backfill_frontmatter.py` — fills missing frontmatter from MASTER-INDEX.csv
- `inject_open_questions.py` — rewrites OQ blocks from CSV `action_required` column
- `review_financial_questions.py` — inactive scaffold, `SCHEDULED_ACTIVATION = False`
- GitHub repo: https://github.com/Open-Source-Boots/BrainOS-Vault

## CROSS-REFERENCES

- BE-20260425-BRAINOS-open-questions-automation-quiz-build.md — OQ automation pipeline origin
- BE-20260425-BRAINOS-master-index-migration-complete.md — CSV migration that preceded this audit
- BE-20260427-BRAINOS-repo-audit-canonical-compilation.md — parallel session BE, same date
- BRAINOS-SYSTEM.md — primary canonical target for system architecture decisions
- DEVICE-ECOSYSTEM.md — device-specific gitignore and sync protocol decisions
- FINANCIAL-SNAPSHOT.md — activation target for financial question review pipeline

## RAW HIGHLIGHTS

- "58 files changed, 469 insertions(+), 195 deletions(-)" — largest single commit of BrainOS build to date
- vault_health_check output: "Brain Entries on disk: 59 / Entries in MASTER-INDEX.csv: 55 / Stale CSV rows: 0"
- log_dedup output: "Total unique OQ IDs found: 54 / Duplicate IDs: 29"
- OQ-20260425-001 appeared 19 times across answer logs — single most-duplicated ID in vault
- `.stfolder` rule confirmed: never delete from local filesystem, Syncthing ownership marker