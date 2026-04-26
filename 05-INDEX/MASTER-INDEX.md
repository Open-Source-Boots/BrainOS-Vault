---
title: "Master Index — BrainOS Vault"
updated: 2026-04-25
---

# 🗂 Master Index

## All Brain Entries
```dataview
TABLE thread_date, domain, status, priority, action_required
FROM "02-BRAIN-ENTRIES"
SORT thread_date DESC
```

## Active Projects
```dataview
TABLE status, file.mtime AS "Last Updated"
FROM "03-PROJECTS"
SORT file.mtime DESC
```

## Canonical Files
```dataview
TABLE status, file.mtime AS "Last Updated"
FROM "04-CANONICAL"
SORT file.name ASC
```

