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

Obsidian sorts A→Z by default. This convention turns alphabetical sort into chronological sort automatically for all dated files.

## The Rule

```
Dated files:     YYYYMMDD-DOMAIN-descriptor.md
Monthly files:   YYYYMM-DOMAIN-descriptor.md
Canonical files: DOMAIN-DESCRIPTOR.md          ← no date, never rename
```

- **Date first** — always. YYYYMMDD or YYYYMM only. No dashes inside the date block.
- **DOMAIN second** — uppercase. Matches vault domain taxonomy: FINANCE, BE, DAILY, BRAINOS, GLWC, etc.
- **descriptor last** — lowercase, hyphen-separated words. Short. Describes the content, not the format.

## Examples

| File type | Correct name |
|-----------|-------------|
| Brain Entry | `20260501-BE-sofi-pipeline-session.md` |
| Daily note | `20260501-DAILY.md` |
| Finance extract | `202506-FINANCE-sofi-extract.md` |
| Project note | `20260501-GLWC-scheduling-conflict.md` |
| Answer file | `20260501-ANSWERS-electrician-path.md` |

## Canonical Files (never dated)

These live in `04-CANONICAL/` and are never prefixed:

```
FINANCIAL-SNAPSHOT.md
BRAINOS-SYSTEM.md
BRAYDEN-IDENTITY.md
ACTIVE-PROJECTS.md
SKILLS-EDUCATION.md
DEVICE-ECOSYSTEM.md
AI-WORKFLOW-RULES.md
```

## Enforcement

Run `vault_rename.py` from vault root to audit and fix naming across all dated folders:

```bash
python vault_rename.py --dry-run    # preview only
python vault_rename.py --git        # rename + git mv in one step
```

After `--git`:
```bash
git commit -m "[SYSTEM] rename: enforce naming convention"
git push origin main
```
