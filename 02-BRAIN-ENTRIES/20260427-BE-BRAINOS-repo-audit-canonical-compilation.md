---
title: "BrainOS Repo Audit and Canonical Compilation — April 27 2026"
filename: "BE-20260427-BRAINOS-repo-audit-canonical-compilation.md"
date: 2026-04-27
domain: BRAINOS
slug: repo-audit-canonical-compilation
status: COMPILED
compilation_status: COMPLETE
supersedes: ""
superseded_by: ""
canonical_file: BRAINOS-SYSTEM.md
tags:
  - brainos
  - repo-audit
  - canonical
  - desktop-ini
  - git-cleanup
  - sync
  - gdrive
open_questions:
  - id: OQ-20260427-001
    question: "Should the vault ever be moved out of the Google Drive-synced folder once a dedicated mobile sync pipeline (e.g. Syncthing or n8n) is operational?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-002
    question: "What is the current status of Ollama on the desktop — is it installed and running, or only downloaded?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED
  - id: OQ-20260427-003
    question: "Does the iPhone PAT for GitHub expire May 22, 2026, and has a renewal reminder been set?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED
  - id: OQ-20260427-004
    question: "Are the three automation scripts (backfill_frontmatter.py, inject_open_questions.py, review_questions.py) functional and tested, or committed but untested?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-005
    question: "What files actually exist inside 03-PROJECTS subfolders (CTRL-YOU, GLWC, ELECTRICIAN, YOUTUBE, HOMESTEAD) beyond placeholder structure?"
    canonical_target: ACTIVE-PROJECTS.md
    status: CLOSED
  - id: OQ-20260427-006
    question: "Does the MASTER-INDEX.csv currently contain entries for all 48 Brain Entries, or are early Brain_Entry_001–010 and BEUNASSIGNED files missing from the index?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-007
    question: "Is the naming inconsistency between Brain_Entry_001–010 and BE-YYYYMMDD format causing any Dataview query failures in Obsidian right now?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-008
    question: "What is the threshold at which Google Drive sync becomes incompatible with Git-based workflows — is there a file count, repo size, or conflict rate that would force a migration?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-009
    question: "If BrainOS is eventually packaged as CommonGrounds, what is the minimum viable feature set that distinguishes it from a plain Obsidian vault with Git sync?"
    canonical_target: ACTIVE-PROJECTS.md
    status: CLOSED
  - id: OQ-20260427-010
    question: "What does a 'ShiftMind' triage system mean — what was the founding concept in BE-20260425-BRAINOS-triage-shiftmind-founding.md?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-011
    question: "Is there a meaningful difference between how BrainOS handles identity data versus project data in terms of update frequency and access patterns?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260427-012
    question: "At what point does a local LLM (Ollama/LM Studio) replace cloud AI (Perplexity) as the primary session tool — what capability gap remains?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED

---

## KEY FACTS

- BrainOS Vault repo at `github.com/Open-Source-Boots/BrainOS-Vault` confirmed clean and fully synced as of 2026-04-27
    
- 48 Brain Entries committed spanning 2026-02-21 through 2026-04-25
    
- `BRAINOS-SYSTEM.md` was a 3-line stub — compiled into full canonical reference (9,998 bytes) this session, commit `9b9c773`
    
- 19 tracked `desktop.ini` files purged from all vault subdirectories, commit `33ee81c`
    
- 1 Syncthing conflict file deleted: `BE-20260425-BRAINOS-triage-shiftmind-founding.sync-conflict-20260425-230026-QH2DFIH.md`
    
- `.gitignore` updated to include `*.sync-conflict-*` and `**/desktop.ini`
    
- `git gc` generates `bad sha1` warnings from Drive-injected `desktop.ini` files inside `.git/objects` — confirmed cosmetic only, not corruption
    
- Decision: Option 3 — live with the noise, Drive sync stays active because it bridges iPhone vault access via Möbius Sync
    

## TIMELINE MARKERS

- 2026-04-27 00:14 CDT — Session opened, repo audit requested
    
- 2026-04-27 00:24 CDT — `BRAINOS-SYSTEM.md` fully compiled and pushed
    
- 2026-04-27 00:29 CDT — `desktop.ini` purge pass 1 (19 files, all vault subdirs)
    
- 2026-04-27 00:32 CDT — `git gc` run, revealed `.git/objects` contamination
    
- 2026-04-27 00:44 CDT — Decision to keep Drive sync, treat bad sha1 as known noise
    

## UPDATES TO CANONICAL FILES

- **BRAINOS-SYSTEM.md** — Fully rebuilt this session. Now contains: vault structure, canonical file list, Brain Entry format, MASTER-INDEX schema, sync stack, device stack, local AI stack, automation scripts, 6-step build sequence, AI session rules, browser automation guardrails, known vault bugs, key origin threads
    
- **BRAINOS-SYSTEM.md** — Should receive one more update: add `desktop.ini / bad sha1` standing rule to Known Vault Bugs section (deferred to batch update)
    

## INSIGHTS & PATTERNS

- The vault is structurally sound but canonically thin — most canonical files exist as shells. `BRAINOS-SYSTEM.md` was the most critical gap and is now closed.
    
- Google Drive injecting into `.git/objects` is a known, permanent condition of the current sync setup. It is noise, not risk.
    
- `03-PROJECTS` subfolders exist in the repo but their contents are unknown — this is the next audit layer worth pulling.
    
- BrainOS has accumulated 48 Brain Entries in ~65 days, averaging roughly one session every 1.3 days. The system is being used.
    
- Two naming conventions coexist in `02-BRAIN-ENTRIES` — old numeric format and new dated format. Dataview queries need to account for both until a rename pass is done.
    

## TOOLS & RESOURCES REFERENCED

- `git rm --cached` — untrack files without deleting them locally
    
- `git ls-files | findstr desktop.ini` — find all tracked junk files
    
- `Get-ChildItem -Recurse -Filter "desktop.ini" | Remove-Item -Force` — bulk delete from `.git/objects`
    
- `git gc --prune=now` — pack objects and surface bad sha1 warnings
    
- Obsidian Git plugin — auto-commit/push every 10 min
    

## CROSS-REFERENCES

- BE-20260423-BRAINOS-git-gdrive-sync-completed.md — Git setup origin
    
- BE-20260424-BRAINOS-full-build-session.md — iPhone Obsidian live
    
- BE-20260425-BRAINOS-architecture-sync-fixes.md — sync conflict origin
    
- DEVICE-ECOSYSTEM.md — full device/tool install status
    
- AI-WORKFLOW-RULES.md — fabrication prevention rules
    

## RAW HIGHLIGHTS

- "bad sha1 file: .git/objects/xx/desktop.ini" — confirmed cosmetic, Drive-injected, not Git corruption
    
- BRAINOS-SYSTEM.md was 72 bytes (3 lines) at session open, 9,998 bytes at session close
    
- `git gc` output: "Total 3,216 (delta 1,069)" — all real objects healthy
    
- Commit chain this session: `9b9c773` → `daed53b` → `33ee81c`