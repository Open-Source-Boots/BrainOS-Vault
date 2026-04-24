---
title: "Master Index Audit & Redesign Brief"
filename: "BE-20260424-BRAINOS-master-index-audit-redesign.md"
date: 2026-04-24
domain: BRAINOS-SYSTEM
slug: master-index-audit-redesign
status: ACTIVE
canonicalfile: "Master-Index.csv"
tags: [brainos, master-index, sync, audit, schema, automation]
---
Key Facts

Master Index current schema: 10 columns (Original Filename, Suggested Filename, Domain, Status, Key Facts, Open Questions, Canonical Files to Update, New File to Consider, Cross-Reference Note, Compilation Status)

Primary problems: Key Facts cells are 800–1,000 word prose blobs; filename column is aspirational not actual; no Last Verified Date; no Priority field; no auto-population from YAML frontmatter

Sync bug noted: file moves in Obsidian not reflected in Google Drive or Git repo — root cause likely Obsidian Git staging gap on delete+add pairs from moves; run git status after moves before pushing

n8n setup described as "largely a failure" — deprioritize; Syncthing (laptop) and Mobius Sync (iPhone) confirmed working

Recommended v2 schema: filename | thread_date | domain | status | priority | key_facts (3-5 bullets) | open_questions (max 5) | canonical_file | action_required | last_verified | notes

Open Questions

Which column in the current index is being used as the primary lookup key — Original Filename or Suggested Filename?

Has the renaming pass (Original → Suggested Filename) ever been executed in the actual vault, or only in the index?

Is Google Sheets the long-term home for Master Index, or should it migrate to a CSV in the vault (importable by local AI)?

What triggered the "project growing too quickly" feeling — volume of entries, lack of checkpoints, or the sync failures?

Should n8n be formally deprioritized/removed from the active stack until a stable checkpoint is reached?

Canonical files to update

Master-Index.csv — schema redesign per v2 above; collapse Original/Suggested Filename into single filename column; add last_verified, priority, action_required columns; truncate Key Facts and Open Questions to max 5 items per row

BE-20260405-TOOL-local-ai-stack-device-ecosystem.md — note n8n deprioritized; Syncthing and Mobius Sync confirmed working

AI-WORKFLOW-RULES — add file-move sync bug note: always run git status after moves in Obsidian before pushing

New file to consider

BRAINOS-CHECKPOINT-LOG.md — a short running log of what was actually completed at each session, not planned; directly addresses "growing too fast without tangible checkpoints" concern

Cross-reference note

BE-20260423-BRAINOS-fullstack-sync-n8n-install.md — previous sync session; n8n install attempted, largely failed; Obsidian Git confirmed operational

BrainOS-Open-Questions-Worksheet.md — 107 open questions; many overlap with Master Index open question cells; these two documents are doing redundant work and should be reconciled

Compilation Status
DRAFT — awaiting Brayden's decisions on: (1) Google Sheets vs. CSV as Master Index home; (2) whether to run the rename pass before or after schema redesign; (3) n8n formal deprioritization; (4) whether to create BRAINOS-CHECKPOINT-LOG.md as a new file.