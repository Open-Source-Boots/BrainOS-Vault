---
title: "CSV Push Failure — Index Automation & Git Hook Debugging"
filename: "BE-20260430-BRAINOS-csv-push-failure-index-automation.md"
date: 2026-04-30
domain: BRAINOS-SYSTEM
slug: csv-push-failure-index-automation
status: ACTIVE
compilation_status: COMPLETE
supersedes: null
superseded_by: null
canonical_file: BRAINOS-SYSTEM.md
tags:
  - brainos
  - master-index
  - automation
  - git
  - python
  - windows
  - debugging
  - rebuild-index
  - pre-commit-hook
  - shell-commands
open_questions:
  - id: OQ-20260430-001
    question: "Does the Shell Commands plugin support running a Python script on vault open as a trigger event, without requiring a hotkey press?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-002
    question: "Is yaml available in Python 3.14 by default, or does rebuild_index.py require a pip install yaml step before it will run on a fresh machine?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-003
    question: "What is the exact path Git on Windows uses to resolve core.hooksPath when it is set explicitly — does it resolve relative to vault root or the .git directory?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-004
    question: "Does Obsidian Git's auto-commit fire before or after Shell Commands plugin hooks, and can the order be controlled?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-005
    question: "How many brain entries currently have missing or malformed frontmatter fields that would cause rebuild_index.py to produce blank rows in the CSV?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260430-006
    question: "Is the desktop.ini corruption in .git/refs a result of Google Drive syncing .git internals — and should .git/ be explicitly excluded from Google Drive sync?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-007
    question: "Can a PowerShell script be placed in the vault root and run via Task Scheduler on Windows to replace the pre-commit hook entirely — triggering rebuild_index.py on a timer?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-008
    question: "If rebuild_index.py is run from a directory other than the vault root, will the relative paths ENTRY_DIRS and OUTPUT_CSV still resolve correctly?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-009
    question: "What is the threshold at which MASTER-INDEX.csv will become too large for Obsidian's Dataview plugin to render efficiently — and is there a pagination strategy for the index view?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260430-010
    question: "Should key_facts be intentionally left blank in the CSV, or is there a lightweight way to auto-populate it from the first KEY FACTS bullet in each brain entry's body?"
    canonical_target: BRAINOS-SYSTEM.md
    status: CLOSED
  - id: OQ-20260430-011
    question: "Does the MCP tool file size ceiling apply per-call or per-session — and is there a chunked write pattern that would allow AI to update large files safely?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: CLOSED
  - id: OQ-20260430-012
    question: "Would WSL (Windows Subsystem for Linux) resolve the Git hook executable bit problem permanently, and is it worth installing for BrainOS tooling purposes?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---
KEY FACTS
MCP tool create_or_update_file has a practical content size ceiling — full CSV rewrites (~38KB+) fail silently with a payload error

MASTER-INDEX.csv should never be AI-rewritten; it is a generated output rebuilt from frontmatter by utils/rebuild_index.py

utils/rebuild_index.py now exists in the repo, confirmed working — outputs Rebuilt MASTER-INDEX.csv - 60 entries

Git pre-commit hooks cannot be made executable on Windows without WSL or Git Bash with Unix permissions — chmod and icacls both failed

The Shell Commands Obsidian plugin is the correct Windows replacement for the hook automation

desktop.ini corruption exists across multiple .git/refs/ subdirectories — likely caused by Google Drive syncing .git/ internals

A stray pre-commit file was accidentally committed to vault root and was cleaned up (git rm pre-commit)

Confirmed vault folder structure from GitHub: 00-INBOX, 01-DAILY, 02-BRAIN-ENTRIES, 03-PROJECTS, 04-CANONICAL, 05-INDEX, 06-ANSWERS, 07-TEMPLATE, 08-ATTACH, utils/

TIMELINE MARKERS
2026-04-30T08:03 — Session opened; CSV push failure diagnosed

2026-04-30T08:20 — AI fabricated 06-SCRIPTS/ folder; corrected after vault structure verified via GitHub MCP

2026-04-30T09:12 — rebuild_index.py pushed to GitHub via MCP tool

2026-04-30T09:24 — Script confirmed working locally: 60 entries

2026-04-30T09:36 — Hook deleted after blocking all commits; repo cleaned

2026-04-30T09:38 — Session closed; Shell Commands plugin identified as next action

UPDATES TO CANONICAL FILES
BRAINOS-SYSTEM.md — Add: CSV write rule, file size rule for MCP writes, vault path verification rule, rebuild_index.py location and usage

AI-WORKFLOW-RULES.md — Add: MCP tool file size ceiling (~8KB), CSV append-only rule, path verification before any file write

DEVICE-ECOSYSTEM.md — Note: Windows Git hooks require WSL for executable bit; Shell Commands plugin is current automation path

CONTRADICTIONS
Space instructions referenced 06-SCRIPTS/ as a scripts folder — does not exist; corrected to utils/ and vault root

INSIGHTS & PATTERNS
The fabricated folder path (06-SCRIPTS/) is a clear example of AI confident hallucination on infrastructure details — the vault path verification rule directly addresses this pattern

The desktop.ini corruption cascaded across refs/remotes/, refs/heads/, and refs/original/ — Google Drive likely syncs .git/ internals which Windows then injects desktop.ini into; .git/ should be excluded from Drive sync

The CSV-as-generated-output architecture (frontmatter → script → CSV) is the correct long-term design; manual maintenance of any index that grows unboundedly will always fail

PowerShell's Out-File -Encoding utf8 writes a BOM that breaks shell script shebangs — always use [System.IO.File]::WriteAllText() for shell scripts on Windows

TOOLS & RESOURCES REFERENCED
utils/rebuild_index.py — vault root script, scans 02-BRAIN-ENTRIES and 03-PROJECTS, outputs 05-INDEX/MASTER-INDEX.csv

Shell Commands Obsidian plugin — https://github.com/Taitava/obsidian-shellcommands

GitHub MCP tool create_or_update_file — confirmed ~8KB practical ceiling for content payload

PowerShell [System.IO.File]::WriteAllText() — correct method for writing shell scripts without BOM on Windows

CROSS-REFERENCES
vault_health_report.txt — desktop.ini ref corruption previously documented

AI-WORKFLOW-RULES.md — file write rules need updating from this session

BRAINOS-SYSTEM.md — rebuild_index workflow needs documenting

BE-20260427-BRAINOS-vault-audit-health-backfill-dedup.md — prior session that identified desktop.ini as tracked file

RAW HIGHLIGHTS
"The CSV should never be manually maintained at all."
"Files over ~8KB require either a targeted patch or a locally-run script."
"Before recommending any file path, verify the actual folder structure using the GitHub MCP tool."
"Out-File -Encoding utf8 adds a byte-order mark that breaks shell scripts on Windows Git Bash."