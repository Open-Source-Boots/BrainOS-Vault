---
title: BrainOS System
filename: BRAINOS-SYSTEM.md
updated: 2026-04-30
status: CANONICAL
domain: BRAINOS-SYSTEM
note: This is a canonical file. Updates flow INTO it from brain entries, not out of it.
---

# BrainOS System — Canonical Reference

BrainOS is a local-first second brain built in Obsidian, synced via Git + Google Drive, designed around ADHD execution patterns. The goal is to reduce re-entry cost to near zero — every session should be reloadable in under 5 minutes from any device.

---

## What BrainOS Is

BrainOS is not a note-taking system. It is an operating system for Brayden's life, projects, decisions, and identity. It captures raw sessions from AI threads, documents, statements, transcripts, and more, distills them into structured Brain Entries, compiles confirmed facts into canonical files, and uses open questions to close knowledge gaps over time.

---

## Vault Folder Structure

| Folder             | Purpose                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `00-INBOX`         | Raw captures, unsorted notes, unprocessed inputs                                               |
| `01-DAILY`         | Daily notes — habit anchor, re-entry point each day                                            |
| `02-BRAIN-ENTRIES` | Compiled session records — the archive core                                                    |
| `03-PROJECTS`      | Active project files (GLWC, CommonGrounds, Electrician, etc.)                                  |
| `04-CANONICAL`     | Source-of-truth files — updated FROM brain entries and other files, never directly             |
| `05-INDEX`         | MASTER-INDEX.csv, MASTER-INDEX.md, open questions, BrainOS Checkpoints                         |
| `06-ANSWERS`       | Closed open question answer files, organized by canonical domain                               |
| `07-TEMPLATE`      | Brain Entry and other templates                                                                |
| `08-ATTACH`        | PDFs, Images, Voice Memos, Transcripts, Links; Anything that is not easily indexed by Obsidian |
| `99-OUTBOX`        | Files staged for export, sharing, or external use                                              |
| `utils`            | Scripts, Automation, other programs that serve unique functions                                |

**Rule:** Before recommending any file path in any session, verify actual folder structure using the GitHub MCP tool. Do not assume folders exist. (Origin: BE-20260430)

---

## Canonical Files

These are the seven files that hold confirmed, verified facts. They outrank everything else in the vault on any conflict.

| File | Domain |
|---|---|
| `BRAYDEN-IDENTITY.md` | Who Brayden is — identity, history, cognition, values |
| `BRAINOS-SYSTEM.md` | How BrainOS works — this file |
| `ACTIVE-PROJECTS.md` | What's being worked on and at what priority |
| `FINANCIAL-SNAPSHOT.md` | Income, debt, bills, projections — numbers only Brayden confirms |
| `SKILLS-EDUCATION.md` | Education path, credentials, skills being built |
| `DEVICE-ECOSYSTEM.md` | Hardware, software stack, install status per device |
| `AI-WORKFLOW-RULES.md` | Standing rules for AI sessions — fabrication prevention, scope control |

**Rule:** AI writes structure, Brayden fills numbers. Never the reverse. If a number is needed and not confirmed, mark it `[UNCONFIRMED]`. (Origin: BrainEntry006, April 2026)

---

## Brain Entry Format

Brain Entries are compiled session records. Every AI thread that produces confirmed facts gets harvested into a Brain Entry and indexed in MASTER-INDEX.csv.

### Filename Convention
```
BE-[YYYYMMDD]-[DOMAIN]-[slug].md
```
Example: `BE-20260425-BRAINOS-architecture-sync-fixes.md`

### Frontmatter Fields (in order)
```yaml
title:
filename:
date:
domain:
slug:
status:
compilation_status:
supersedes:
superseded_by:
canonical_file:
tags:
open_questions:
```

### Body Sections (in order)
1. `## KEY FACTS`
2. `## TIMELINE MARKERS`
3. `## UPDATES TO CANONICAL FILES`
4. `## CONTRADICTIONS` (if any)
5. `## INSIGHTS & PATTERNS`
6. `## TOOLS & RESOURCES REFERENCED` (if any)
7. `## CROSS-REFERENCES`
8. `## RAW HIGHLIGHTS`

### Open Questions Rules
- Every question goes in frontmatter `open_questions:` YAML block — never in the body
- Generate 5–15 questions per session depending on depth
- Each question must be concrete, answerable with a single response, tied to a real next action or unresolved fact
- Each question requires: `id` (OQ-[YYYYMMDD]-[NNN]), `question`, `canonical_target`, `status: OPEN`
- Valid canonical targets: BRAINOS-SYSTEM.md, BRAYDEN-IDENTITY.md, ACTIVE-PROJECTS.md, SKILLS-EDUCATION.md, DEVICE-ECOSYSTEM.md, AI-WORKFLOW-RULES.md, FINANCIAL-SNAPSHOT.md

---

## MASTER-INDEX Schema

The MASTER-INDEX.csv is the vault's wiki — machine-readable, 10-column schema:

```
filename | threaddate | domain | status | priority | keyfacts | canonicalfile | actionrequired | lastverified | notes
```

- `MASTER-INDEX.csv` — machine-readable source of truth
- `MASTER-INDEX.md` — human-readable Dataview dashboard (queries live here)
- Legacy Google Sheet renamed `MASTER-INDEX-LEGACY` — do not use

---

## Index Generation (MASTER-INDEX.csv)

**Rule: MASTER-INDEX.csv is a generated output. It is never manually edited and never AI-rewritten.**

The correct workflow:
1. Run `utils/rebuild_index.py` locally from the vault root
2. The script scans `02-BRAIN-ENTRIES/` and `03-PROJECTS/` for frontmatter
3. It outputs `05-INDEX/MASTER-INDEX.csv` — 60 entries as of 2026-04-30
4. Commit and push the regenerated CSV via Obsidian Git or terminal

### Why AI cannot rewrite the CSV
The MCP tool `create_or_update_file` has a practical content payload ceiling of approximately 8KB. MASTER-INDEX.csv is currently ~38KB. Any attempt to AI-rewrite the full CSV will fail silently with a payload error. The only safe write path is local script execution. (Origin: BE-20260430)

### Shell Commands Plugin — Windows Automation Path
Pre-commit Git hooks cannot be made executable on Windows without WSL. The Shell Commands Obsidian plugin is the confirmed replacement automation path for triggering `rebuild_index.py` on Windows.

- Plugin repo: https://github.com/Taitava/obsidian-shellcommands
- Trigger options: vault open, file save, manual hotkey — configure per workflow needs
- Command: `python utils/rebuild_index.py` run from vault root

**Standing rule:** Do not attempt to write shell scripts via PowerShell `Out-File -Encoding utf8` — it writes a BOM that breaks shebangs in Git Bash. Use `[System.IO.File]::WriteAllText()` instead. (Origin: BE-20260430)

---

## Sync Stack

| Layer           | Tool         | Role                                      | Canonical?         |
| --------------- | ------------ | ----------------------------------------- | ------------------ |
| Version control | Git          | Full history, diff, rollback              | YES — primary      |
| Cloud mirror    | Google Drive | Cross-device access, Drive backup         | YES — secondary    |
| Local sync      | Syncthing    | LAN peer-to-peer between desktop ↔ laptop | YES — <br>Tertiary |

**Rule**: Git is the ground truth. Drive mirrors Git. Drive never overrides Git.
Git Sync Rules — HARDENED
Commit Protocol
Commit scope: One logical change per commit. Do not batch unrelated files.

Commit message format: [DOMAIN] verb: short description

Examples: [IDENTITY] update: add GLWC two-hat note, [FINANCE] add: April income entry, [SYSTEM] harden: git + drive sync rules

Commit frequency: At minimum, commit at the end of every working session. Intra-session commits are encouraged after any canonical file edit.

Never force-push to main. If rebase is needed, branch first, rebase, then fast-forward merge.

Branch strategy:

main = stable vault state. Always functional.

draft/[slug] = experimental restructures or bulk edits in progress.

Merge to main only when the draft is clean and tested in Obsidian.

.gitignore (Mandatory)
The following must always be ignored:

text
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/plugins/*/data.json   # Plugin state — not vault data
.trash/
*.DS_Store
Thumbs.db
~$*.docx
*.tmp
*.log
node_modules/
.env
secrets/
The following must not be ignored (they are vault data):

text
.obsidian/app.json
.obsidian/appearance.json
.obsidian/graph.json
.obsidian/hotkeys.json
.obsidian/community-plugins.json
templates/
assets/
Conflict Resolution Protocol
Conflicts happen when Drive auto-saves diverge from Git commits. Resolution order:

Stop — do not open Obsidian until resolved.

Identify — run git status and git diff to see what changed.

Compare timestamps — check which version is newer: Drive copy or Git HEAD.

Resolve manually — open the conflicted file in a text editor, not Obsidian.

Prefer the version with more information. If both have unique content, merge manually.

Commit the resolution with message: [SYSTEM] resolve: conflict in [filename] — [brief reason]

Never accept "keep both copies" from Drive's conflict dialog without manually reviewing both.

Pre-Commit Checklist
Before every commit, verify:

No secrets, tokens, or passwords in staged files (run git diff --cached | grep -i "key\|token\|password\|secret")

MASTER-INDEX.csv updated if a new BE file was added

Canonical files updated if session changed a confirmed fact

.gitignore entries are not in the staged set

Recovery from a Bad State
bash
# See what changed since last commit
git diff HEAD

# Discard all unstaged changes (DESTRUCTIVE — confirm first)
git checkout -- .

# Undo last commit but keep changes staged
git reset --soft HEAD~1

# Nuclear reset to last clean commit (DESTRUCTIVE)
git reset --hard HEAD
git clean -fd


## Google Drive Sync Rules — HARDENED

## Drive's Role

Drive is a **read mirror and cross-device access layer** — not a version control system. It does not replace Git history.

## Sync Behavior Rules

1. **Obsidian vault folder in Drive = the only Drive folder that matters for BrainOS**. Do not scatter vault files across Drive.
    
2. **Drive sync must be active before starting an Obsidian session** on any device. Never open Obsidian on a secondary device without confirming Drive is synced.
    
3. **Close Obsidian before allowing Drive to sync large batches**. Drive syncing while Obsidian writes can corrupt the `.obsidian/workspace.json`.
    
4. **Drive is NOT a substitute for `git commit`**. A Drive sync does not create a recoverable snapshot. Always Git commit before closing a session.
    
5. **Drive conflict files** (files suffixed with device name or "(1)") must be **immediately resolved and deleted** — do not leave them sitting in the vault. They will appear as duplicate notes in Obsidian.
    
6. **Do not use Drive's "version history" as your primary rollback mechanism**. It is a last resort. Git is the rollback mechanism.
    

## Drive Folder Hygiene

- Vault folder in Drive: single, named `BrainOS Vault/` — no copies, no alternates.
    
- If Drive ever shows two copies of the vault folder: stop, audit, merge into Git HEAD, delete the older duplicate.
    
- Attachments (`08-ATTACH/`) are tracked in Git AND mirrored to Drive. Do not store assets only in Drive.

## Multi-Device Sync Order (Mandatory)

When switching from **Desktop → Laptop** (or any device transition):

1. Desktop: commit all changes to Git (`git add -A && git commit -m "..."`)
    
2. Desktop: push to remote (`git push origin main`)
    
3. Desktop: confirm Drive has synced (check Drive status indicator — wait for ✓)
    
4. Desktop: close Obsidian
    
5. Laptop: confirm Drive has synced (wait for ✓ before opening Obsidian)
    
6. Laptop: open Obsidian
    
7. Laptop (optional but recommended): `git pull origin main` to confirm Git parity
    

**Never open Obsidian on the second device before step 5 is confirmed.**

---

## Device Stack

| Device            | Role                                | Key Specs                                          |
| ----------------- | ----------------------------------- | -------------------------------------------------- |
| Desktop           | Primary AI workstation              | Ryzen 7 7700X, RTX 3060 12GB, 64GB RAM, Windows 11 |
| Laptop            | Mobile workhorse                    | Intel Iris Xe, 8GB RAM, Windows                    |
| iPhone 15         | Mobile capture, Obsidian mobile     | 128GB, Möbius Sync active                          |
| iPad Air(5th gen) | Spacedesk second monitor, Procreate | 64GB, A9 chip                                      |

Full specs and install status: see `DEVICE-ECOSYSTEM.md`

---

## Local AI Stack

| Tool | Purpose | Status |
|---|---|---|
| Obsidian | Vault interface | Installed all devices |
| LM Studio | Local model runner (laptop) | Installed, Gemma 3 1b tested |
| Ollama | Local model runner (desktop) | Downloaded, install unconfirmed on desktop |
| n8n v2.17.6 | Automation workflows | Installed, zero active workflows — deprioritized |
| ComfyUI | Image generation (Flux.1) | Desktop — pending full setup |
| PiperTTS | Free local voiceover | Flagged, not yet installed |
| Whisper | Local transcription | Not yet installed |
| PocketPal | On-device AI (iPhone) | Qwen2.5 installed |

**n8n standing rule:** No workflows until daily note habit is established and Ollama is confirmed running on desktop. Do not treat as active infrastructure.

---

## Automation Scripts

Scripts committed to the vault repository. These are real, working tools — do not invent additional script paths.

| Script | Location | Purpose |
|---|---|---|
| `backfill_frontmatter.py` | vault root | Adds missing frontmatter fields to existing Brain Entries |
| `inject_open_questions.py` | vault root | Injects open questions into Brain Entry frontmatter |
| `review_questions.py` | vault root | Interactive CLI for reviewing and answering open questions |
| `rebuild_index.py` | `utils/` | Scans 02-BRAIN-ENTRIES + 03-PROJECTS, outputs MASTER-INDEX.csv — confirmed working 2026-04-30, 60 entries |

**Rule:** If a script path is needed and not in this table, verify it exists in the repo via GitHub MCP before referencing it. (Origin: BE-20260430 — AI fabricated `06-SCRIPTS/` folder in session, corrected by vault structure verification)

---

## 6-Step BrainOS Build Sequence

Origin: BrainEntry002. This is the canonical order of operations for any build or compilation session.

1. **Map** — identify what exists, what's missing, what's stale
2. **Triage** — sort by impact, not interest
3. **Compile** — harvest confirmed facts from threads into Brain Entries
4. **Update** — push confirmed facts into canonical files
5. **Index** — update MASTER-INDEX.csv with new entries
6. **Plan** — only after the map is complete, decide next actions

**Rule:** Plan comes AFTER the map is complete. Planning before mapping is faux progress.

---
## Domain Tags

`IDENTITY` · `FINANCE` · `SKILLS` · `SYSTEM` · `PROJECTS` · `GLWC` · `ELECTRICIAN` · `COMMONGROUNDS` · `CTRL-YOU` · `YOUTUBE` · `HOMESTEAD` · `MAKER` · `HEALTH` · `AI`

---

## Status Tags

`ACTIVE` · `PAUSED` · `COMPLETE` · `ARCHIVED` · `DRAFT` · `REVIEW`

---

## Compilation Status Tags

`CURRENT` · `STALE` · `SUPERSEDED` · `PENDING-UPDATE`
---
## AI Session Standing Rules

These rules are non-negotiable in every AI session. Full list in `AI-WORKFLOW-RULES.md`.

- **AI writes structure, Brayden fills numbers** — never invent financial figures, debt balances, income, dates, or device specs
- **Single scoped task before starting** — define the task, then execute
- **Checkpoint every 2–3 actions** — especially in browser automation
- **Prefer reversible actions** — stop and reassess if drifting
- **Never fabricate** — three Google Drive docs (Master Context v3, Cash Flow v3, Command Hub v3) contain AI-invented figures — DO NOT USE
- **Employer is GoodLife Innovations** — not GoodLife Fitness. This error originated in early threads and is fully resolved.
- **MCP file size ceiling** — `create_or_update_file` has a practical limit of ~8KB. Files larger than this require either a targeted patch or a locally-run script. Never attempt to AI-rewrite MASTER-INDEX.csv or any large generated file. (Origin: BE-20260430)
- **Verify paths before writing** — check actual vault structure via GitHub MCP tool before referencing any folder or script path. (Origin: BE-20260430)

---

## Browser Automation Guardrails

Origin: BE-20260301 (Shopify era), still canonical.

1. Always duplicate theme before editing code
2. Never delete core Liquid files without explicit approval
3. Stop-and-ask on any ambiguous edit

---

## Known Vault Bugs (as of 2026-04-30)

- `desktop.ini` files committed into repo subdirectories — need `git rm --cached` purge; root cause is Google Drive syncing `.git/` internals
- `.gitignore` already includes `desktop.ini` but subdirectory copies slipped through before rule was active
- One Syncthing conflict file committed: `BE-20260425-BRAINOS-triage-shiftmind-founding.sync-conflict-20260425-230026-QH2DFIH.md` — needs comparison and deletion
- Add `*.sync-conflict-*` to `.gitignore`
- Early Brain Entries use `Brain_Entry_001.md` naming (underscores, no date) — Dataview queries must account for both naming patterns until rename pass is done
- `BE[UNASSIGNED]_20260416_TOOL_n8n-video-pipeline-setup.md` has literal brackets in filename — should be renamed
- `Smart Connections` plugin indexing stale — reload vault to trigger re-index

---

## Key Origin Threads

| Entry         | What It Established                                                                      |
| ------------- | ---------------------------------------------------------------------------------------- |
| BrainEntry001 | First Brain Entry — origin of thread-harvesting methodology                              |
| BrainEntry002 | AI browser automation rules, 6-step build sequence                                       |
| BrainEntry006 | AI fabrication incident — origin of "AI writes structure" rule                           |
| BrainEntry007 | Master canonical reset — supersedes all prior entries on conflict                        |
| BE-20260405   | BrainOS and Obsidian origin — overnight install session                                  |
| BE-20260422   | Vault folder structure finalized, sync stack confirmed                                   |
| BE-20260423   | Git setup complete, 151 files, Obsidian Git operational                                  |
| BE-20260424   | iPhone Obsidian live, Möbius Sync active                                                 |
| BE-20260425   | CommonGrounds concept born, MASTER-INDEX migration complete                              |
| BE-20260430   | rebuild_index.py confirmed, Git hook failure diagnosed, CSV generation rules established |
