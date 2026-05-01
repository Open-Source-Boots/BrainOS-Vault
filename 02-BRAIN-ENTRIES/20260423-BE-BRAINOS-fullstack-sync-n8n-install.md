---
title: BrainOS Full Stack Setup — Git, Google Drive, n8n Install Completed
filename: BE-20260423-BRAINOS-fullstack-sync-n8n-install.md
thread_date: 2026-04-23
domain: BRAINOS-SYSTEM
slug: fullstack-sync-n8n-install
status: ACTIVE
priority: 1
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
generated_by_skill: manual
tags: ['obsidian-git', 'github', 'google-drive-sync', 'ogd-sync', 'n8n', 'local-rest-api', 'node-js', 'brainos', 'automation', 'sync', 'security', 'standing-rules']
date: 2026-04-23
canonicalfile: BRAINOS-SYSTEM.md
notes: n8n installed but zero workflows built; do not treat as active infrastructure yet
open_questions:
  - id: OQ-20260423-001
    question: "n8n workflows deprioritized — resume only after daily note habit established and Ollama running on desktop"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: CLOSED
---
KEY FACTS ESTABLISHED THIS THREAD
Git — FULLY OPERATIONAL ✓
Vault path (final): C:\Users\brayd\Desktop\Open-Source AI\BrainOS Vault

GitHub repo: github.com/Open-Source-Boots/BrainOS-Vault

Branch: main

Credentials: Windows Credential Manager, Open-Source-Boots only

Auto-commit + push: every 10 minutes (autoSaveInterval: 10)

Auto-pull: every 10 minutes (autoPullInterval: 10)

Pull on boot: ON (autoPullOnBoot: true)

commit + push fire together — differentIntervalCommitAndPush: false (auto-push grayed out by design, correct)

credential.helper: set to manager (not manager-core — that binary doesn't exist on this machine)

.gitignore confirmed containing all three lines:

text
.smart-env/
.obsidian/workspace.json
.obsidian/plugins/google-drive-sync/
Security Incidents — Both Resolved
Incident 1: GitHub PAT pasted into chat → revoked immediately → new token stored in Windows Credential Manager

Incident 2: Google OAuth refresh token committed to Git twice across two vault initializations → both resolved via git filter-branch history rewrite + git push --force + GitHub bypass approval

Root cause: OGD Sync plugin stores refresh token in .obsidian/plugins/google-drive-sync/data.json in plain text — this file must always be in .gitignore before first git add .

Standing rule: .gitignore must exist and contain the google-drive-sync line BEFORE running git init + git add . on any new vault

Google Drive Sync (OGD Sync) — OPERATIONAL ✓
Plugin: OGD Sync by richardxiong

Drive folder: BrainOS Vault

Token: locally stored, blocked from Git ✓

Known behavior: new files in subfolders may land at Drive root — drag to correct subfolder manually after creation

Edit detection: works correctly — detects file edits, confirms deletion of old version, pushes new version

OGD Sync setup procedure for existing vaults:

Create completely new blank vault

Copy folders in one at a time with a Drive push between each

Never batch-paste all folders at once

Never use Google Drive for Desktop alongside OGD Sync — they conflict

Node.js + n8n — INSTALLED ✓
Node.js version: v24.15.0

npm version: 11.12.1

n8n version: 2.17.6

Install method: npm install -g n8n (global install — NOT npx n8n which fails with missing enterprise modules)

Start command: n8n start

n8n URL: http://localhost:5678

Status: Running, account created as "Brayden", canvas confirmed open ✓

Note: n8n currently runs on laptop only — needs to be migrated to desktop for 24/7 operation

Local REST API Plugin — INSTALLED ✓
Port: 27124

API key: regenerated after accidental chat exposure — stored in Obsidian only

Standing rule: API key never shared in chat — reference by name only

BRAINOS-SYSTEM.md — FULLY WRITTEN
Complete canonical file written this thread covering: vault identity, folder structure, canonical files list, sync architecture (all 4 layers), .gitignore contents + rationale, naming conventions, mdsummary YAML format, all standing rules, plugin install order, open questions

Save to: CANONICAL/BRAINOS-SYSTEM.md

STANDING RULES CONFIRMED THIS THREAD
NEVER paste credentials in chat — PATs, OAuth tokens, API keys, passwords — Windows Credential Manager or app settings only

GitHub account: Open-Source-Boots always — delete any BraydenBoots github.com entry from Credential Manager if prompt reappears

.gitignore first rule: gitignore must exist with google-drive-sync line BEFORE first git add . on any vault

OGD Sync + Google Drive for Desktop must never run simultaneously — they conflict

Vault stores outputs only — raw PDFs, videos, source files go to external drives, never the vault

n8n install: always npm install -g n8n, never npx n8n

n8n start: n8n start from any directory after global install

OPEN QUESTIONS FOR NEXT THREAD
Build Workflow 1 in n8n: Brain Entry auto-filer + Master Index updater

Build Workflow 2: Inbox processor for non-MD files (PDFs, books, video URLs)

Migrate n8n from laptop to desktop for 24/7 operation

Connect Syncthing between laptop and desktop

Configure SmartConnections after desktop Ollama is confirmed running

Is Ollama installed on the desktop already?

Is the desktop always-on or manually woken?

CANONICAL FILES TO UPDATE
CANONICAL/BRAINOS-SYSTEM.md → paste the full version written earlier in this thread

BE-20260405-TOOL-local-ai-stack-device-ecosystem.md → add: new vault path, n8n installed globally on laptop, Local REST API on port 27124, Node.js v24.15.0

Master Index (Google Drive CSV) → add rows for both Brain Entries from this thread

NEW FILES TO CREATE
BE-20260423-BRAINOS-fullstack-sync-n8n-install.md ← this file

BE-20260423-BRAINOS-inbox-automation-architecture.md ← from earlier in thread

COMPILATION STATUS
Ready to file. Save both Brain Entries to BrainOS Vault/BRAIN-ENTRIES/. Update Master Index. Paste BRAINOS-SYSTEM.md into CANONICAL/. Start new thread titled "n8n Workflow Build — Brain Entry Auto-Filer + Master Index Updater".