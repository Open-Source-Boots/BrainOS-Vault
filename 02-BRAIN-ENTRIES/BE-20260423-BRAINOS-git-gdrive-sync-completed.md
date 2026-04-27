---
title: BrainOS Vault Git + Google Drive Sync Setup — Completed
filename: BE-20260423-BRAINOS-git-gdrive-sync-completed.md
thread_date: 2026-04-23
domain: BRAINOS-SYSTEM
slug: git-gdrive-sync-completed
status: ACTIVE
priority: 1
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file: BRAINOS-SYSTEM.md
generated_by_skill: manual
tags: ['obsidian-git', 'github', 'google-drive-sync', 'ogd-sync', 'vault-sync', 'automation', 'brainos', 'open-source', 'standing-rule']
date: 2026-04-23
canonicalfile: BE-20260405-TOOL-local-ai-stack-device-ecosystem.md
notes: Continues from BE-20260422; Syncthing laptop↔desktop deprioritized — Git + Drive cover cross-device sync
open_questions:
  - id: OQ-20260423-001
    question: "Confirm Drive folder fully populated with all subfolders"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260423-002
    question: "delete empty Obsidian folder in Drive"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260423-003
    question: "install Local REST API plugin"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---
KEY FACTS ESTABLISHED THIS THREAD
Git — COMPLETED ✓
Vault path confirmed: C:\Users\brayd\Desktop\Open-Source AI\BrainOS\BrainOS Vault\BrainOS Vault

GitHub repo live: github.com/Open-Source-Boots/BrainOS-Vault

Git version: 2.50.1.windows.1

Initial commit: 151 files, all vault contents pushed successfully

Branch renamed master → main before push

Credentials stored via Windows Credential Manager under account Open-Source-Boots

.gitignore created via File Explorer (dot-trick method: .gitignore. → saves as .gitignore)

.gitignore contents: .smart-env/ and .obsidian/workspace.json — excludes SmartConnections cache from commits

Auto-commit interval: 10 minutes ✓

Auto-pull on boot: ON ✓

Base path: blank ✓

differentIntervalCommitAndPush: false — commit and push fire together as one action (correct, auto-push grayed out by design)

Standing rule: Never embed PAT token in chat — use Windows Credential Manager only

Google Drive Sync (OGD Sync) — COMPLETED ✓
Plugin: OGD Sync by richardxiong

Refresh token obtained from ogd.richardxiong.com and saved in plugin settings

Critical lesson: Plugin requires empty vault at first setup — existing files must be moved out temporarily, token saved, Obsidian restarted, then files moved back

Workaround used: moved all content folders to Desktop\BrainOS-Temp-Backup, initialized plugin, restarted Obsidian, moved files back

BrainOS Vault folder confirmed created in Google Drive ✓

.obsidian config file visible in Drive ✓

Empty Obsidian folder also created in Drive — harmless, can be deleted

Manual push command run: Google Drive Sync: Push to Google Drive — confirmed working

OGD Sync has no persistent status bar indicator — success = no error on push command

Standing rule: Do NOT use Google Drive for Desktop alongside OGD Sync — they will conflict

Standing rule: Do not manually upload files into the OGD Sync Drive folder

OGD Sync is NOT end-to-end encrypted — vault content visible in Google Drive (acceptable for BrainOS use case)

Security Incident — RESOLVED
A live GitHub PAT was accidentally pasted into the Perplexity chat during this session

Token was immediately revoked at github.com/settings/tokens

New token generated and stored correctly via Windows Credential Manager

Standing rule: PATs and credentials are NEVER to be pasted into any chat interface — always use OS credential storage

OPEN QUESTIONS
Has the BrainOS Vault folder in Google Drive fully populated with all subfolders (BRAIN-ENTRIES, CANONICAL, INDEX, etc.)?

Should the empty "Obsidian" folder in Google Drive be deleted?

Has the Local REST API plugin been installed in Obsidian yet? (next step)

Has n8n been installed on the desktop?

Has Syncthing been connected between laptop and desktop?

CANONICAL FILES TO UPDATE
BE-20260405-TOOL-local-ai-stack-device-ecosystem.md → add: confirmed vault path, Git repo URL, OGD Sync setup process, empty-vault workaround, .gitignore contents, PAT security rule

BRAINOS-SYSTEM.md → add all standing rules from this session as permanent system rules

Master Index (Google Drive CSV) → add new row for this Brain Entry

NEW FILES TO CONSIDER
BRAINOS-SYSTEM.md — this thread + BE-20260422 now provide enough content to fully populate it; seed content includes: vault path, repo URL, plugin install order, standing rules, sync architecture

CROSS-REFERENCE NOTES
Continues directly from BE-20260422-BRAINOS-live-sync-vault-financial-setup.md and BE-20260422-BRAINOS-git-config-fix-autosync.md

Next thread should cover: Local REST API plugin → n8n install on desktop → Master Index auto-update workflow

Syncthing laptop ↔ desktop still pending — low priority now that Git + Drive cover cross-device sync

COMPILATION STATUS
Ready to file. Save to BrainOS Vault/BRAIN-ENTRIES/. Add row to Master Index. Update BRAINOS-SYSTEM.md with all standing rules.