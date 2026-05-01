---
title: NAMING-CONVENTION
filename: NAMING-CONVENTION.md
date: 2026-05-01
domain: SYSTEM
status: ACTIVE
compilation_status: CURRENT
tags:
  - system
  - naming
  - brainos
---

# BrainOS Vault — Naming Convention

Obsidian sorts A→Z by default. This convention turns that into chronological sort automatically. The design principle is **sidebar-first**: the most useful information (when + what) must be readable from the left bar without opening the file. Type identifiers go at the tail — they are metadata, not navigation.

## The Rule

```
Dated files:     YYYYMMDD-DOMAIN-slug.md
Dated BE files:  YYYYMMDD-DOMAIN-slug-BE.md
Monthly files:   YYYYMM-DOMAIN-descriptor.md
Canonical files: DOMAIN-DESCRIPTOR.md          ← no date, never rename
```

- **Date first** — always. YYYYMMDD or YYYYMM only. No dashes inside the date block.
- **DOMAIN second** — uppercase. Matches vault domain taxonomy: FINANCE, DAILY, BRAINOS, GLWC, etc.
- **slug third** — lowercase, hyphen-separated words. Short. Describes the content, not the format.
- **Type tag last** — `BE` at the tail identifies Brain Entries. Other types do not use a tail tag.

## Brain Entry Filenames

Brain Entries use `-BE` as a suffix so the date and topic are sidebar-readable first, and the file type is queryable at the tail.

```
Old (retired):  BE-20260430-BRAINOS-csv-push-failure-index-automation.md
New (canonical): 20260430-BRAINOS-csv-push-failure-BE.md
```

Dataview queries for Brain Entries use `WHERE contains(file.name, "-BE")` or `FROM "02-BRAIN-ENTRIES"` — both work after the rename pass.

## Examples

| File type | Correct name |
|-----------|-------------|
| Brain Entry | `20260501-BRAINOS-sofi-pipeline-BE.md` |
| Daily note | `20260501-DAILY.md` |
| Finance extract | `202506-FINANCE-sofi-checking-extract.md` |
| Project note | `20260501-GLWC-scheduling-conflict.md` |
| Answer file | `20260501-ANSWERS-electrician-path.md` |

## Canonical Files (never dated)

These live in `04-CANONICAL/` and are never prefixed or renamed:

```
FINANCIAL-SNAPSHOT.md
BRAINOS-SYSTEM.md
BRAYDEN-IDENTITY.md
ACTIVE-PROJECTS.md
SKILLS-EDUCATION.md
DEVICE-ECOSYSTEM.md
AI-WORKFLOW-RULES.md
```

## GLWC Canonical Target

All open questions and Brain Entries referencing GLWC/GoodLife union work must use `GLWC-PROJECT.md` as the canonical target. `GOODLIFE-UNION.md` does not exist and is a dead reference — any occurrence is a bug.

## Enforcement

Run `vault_rename.py` from vault root to audit and fix naming across all dated folders:

```bash
python vault_rename.py --dry-run    # preview only
python vault_rename.py --git        # rename + git mv in one step
```

After `--git`:
```bash
git commit -m "SYSTEM rename enforce naming convention"
git push origin main
```
