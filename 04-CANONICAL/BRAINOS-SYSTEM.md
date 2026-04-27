---
title: BrainOS System
filename: BRAINOS-SYSTEM.md
updated: 2026-04-27
status: CANONICAL
domain: BRAINOS-SYSTEM
note: This is a canonical file. Updates flow INTO it from brain entries, not out of it.
---

# BrainOS System — Canonical Reference

BrainOS is a local-first second brain built in Obsidian, synced via Git + Google Drive, designed around ADHD execution patterns. The goal is to reduce re-entry cost to near zero — every session should be reloadable in under 5 minutes from any device.

---

## What BrainOS Is

BrainOS is not a note-taking system. It is an operating system for Brayden's life, projects, decisions, and identity. It captures raw sessions from AI threads, distills them into structured Brain Entries, compiles confirmed facts into canonical files, and uses open questions to close knowledge gaps over time.

The endgame is CommonGrounds — a commercialized version of BrainOS that other people can run. Everything built here is also the product.

---

## Vault Folder Structure

| Folder | Purpose |
|---|---|
| `00-INBOX` | Raw captures, unsorted notes, unprocessed inputs |
| `01-DAILY` | Daily notes — habit anchor, re-entry point each day |
| `02-BRAIN-ENTRIES` | Compiled session records — the archive core |
| `03-PROJECTS` | Active project files (GLWC, CommonGrounds, Electrician, etc.) |
| `04-CANONICAL` | Source-of-truth files — updated FROM brain entries, never directly |
| `05-INDEX` | MASTER-INDEX.csv, MASTER-INDEX.md, open questions |
| `06-ANSWERS` | Closed open question answer files, organized by canonical domain |
| `07-TEMPLATE` | Brain Entry and other templates |
| `99-OUTBOX` | Files staged for export, sharing, or external use |

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

## Sync Stack

| Layer | Tool | Status |
|---|---|---|
| Version control | Git → github.com/Open-Source-Boots/BrainOS-Vault | Active, auto-commit every 10min |
| Cloud backup | Google Drive for Desktop | Active — syncs vault folder |
| Cross-device mobile | Möbius Sync (iOS) | Active on iPhone |
| Local AI | Obsidian Git plugin | Auto-pull on boot, auto-push on interval |

**Standing rules:**
- Never use Google Drive for Desktop alongside OGD Sync plugin simultaneously — they conflict
- Never embed PATs in chat. Store in Windows Credential Manager only
- iPhone GitHub PAT expires May 22, 2026 — renew before that date
- `.git` folder should be excluded from Google Drive's watch scope to prevent `desktop.ini` injection

---

## Device Stack

| Device | Role | Key Specs |
|---|---|---|
| Desktop | Primary AI workstation | Ryzen 7 7700X, RTX 3060 12GB, 64GB RAM, Windows 11 |
| Laptop | Mobile workhorse | Intel Iris Xe, 8GB RAM, Windows |
| iPhone 15 | Mobile capture, Obsidian mobile | 128GB, Möbius Sync active |
| iPad (5th gen) | Spacedesk second monitor, Procreate | 64GB, A9 chip |

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

## Automation Scripts (Root of Vault)

Three Python scripts are committed at vault root — these are real, working tools:

| Script | Purpose |
|---|---|
| `backfill_frontmatter.py` | Adds missing frontmatter fields to existing Brain Entries |
| `inject_open_questions.py` | Injects open questions into Brain Entry frontmatter |
| `review_questions.py` | Interactive CLI for reviewing and answering open questions |

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

## AI Session Standing Rules

These rules are non-negotiable in every AI session. Full list in `AI-WORKFLOW-RULES.md`.

- **AI writes structure, Brayden fills numbers** — never invent financial figures, debt balances, income, dates, or device specs
- **Single scoped task before starting** — define the task, then execute
- **Checkpoint every 2–3 actions** — especially in browser automation
- **Prefer reversible actions** — stop and reassess if drifting
- **Never fabricate** — three Google Drive docs (Master Context v3, Cash Flow v3, Command Hub v3) contain AI-invented figures — DO NOT USE
- **Employer is GoodLife Innovations** — not GoodLife Fitness. This error originated in early threads and is fully resolved.

---

## Browser Automation Guardrails

Origin: BE-20260301 (Shopify era), still canonical.

1. Always duplicate theme before editing code
2. Never delete core Liquid files without explicit approval
3. Stop-and-ask on any ambiguous edit

---

## Known Vault Bugs (as of 2026-04-27)

- `desktop.ini` files committed into repo subdirectories — need `git rm --cached` purge
- `.gitignore` already includes `desktop.ini` but subdirectory copies slipped through before rule was active
- One Syncthing conflict file committed: `BE-20260425-BRAINOS-triage-shiftmind-founding.sync-conflict-20260425-230026-QH2DFIH.md` — needs comparison and deletion
- Add `*.sync-conflict-*` to `.gitignore`
- Early Brain Entries use `Brain_Entry_001.md` naming (underscores, no date) — Dataview queries must account for both naming patterns until rename pass is done
- `BE[UNASSIGNED]_20260416_TOOL_n8n-video-pipeline-setup.md` has literal brackets in filename — should be renamed
- `BRAINOS-SYSTEM.md` was a stub until 2026-04-27 — this compilation session closes that gap
- `Smart Connections` plugin indexing stale — reload vault to trigger re-index

---

## Key Origin Threads

| Entry | What It Established |
|---|---|
| BrainEntry001 | First Brain Entry — origin of thread-harvesting methodology |
| BrainEntry002 | AI browser automation rules, 6-step build sequence |
| BrainEntry006 | AI fabrication incident — origin of "AI writes structure" rule |
| BrainEntry007 | Master canonical reset — supersedes all prior entries on conflict |
| BE-20260405 | BrainOS and Obsidian origin — overnight install session |
| BE-20260422 | Vault folder structure finalized, sync stack confirmed |
| BE-20260423 | Git setup complete, 151 files, Obsidian Git operational |
| BE-20260424 | iPhone Obsidian live, Möbius Sync active |
| BE-20260425 | CommonGrounds concept born, MASTER-INDEX migration complete |
