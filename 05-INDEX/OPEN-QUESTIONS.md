---
title: Open Questions
filename: OPEN-QUESTIONS.md
updated: 2026-04-26
status: IDEATION
---

# 🧠 BrainOS — Open Questions

> Live table. Questions auto-populate from Brain Entry frontmatter across the entire vault.
> To close a question: open the source file → find the matching `open_questions` block → change `status: OPEN` to `status: CLOSED`. It disappears from the OPEN table on next refresh and appears in the CLOSED table below.

---

## ❓ Open

```dataview
TABLE WITHOUT ID
  oq.id AS "ID",
  oq.question AS "Question",
  oq.canonical_target AS "Target File",
  file.link AS "Source Entry",
  file.mtime AS "Last Modified"
FROM "02-BRAIN-ENTRIES"
FLATTEN open_questions AS oq
WHERE oq.status = "OPEN"
  AND oq.question != null
  AND oq.question != ""
  AND !contains(lower(oq.question), "none")
SORT file.mtime DESC
```

---

## ✅ Closed

```dataview
TABLE WITHOUT ID
  oq.id AS "ID",
  oq.question AS "Question",
  oq.canonical_target AS "Target File",
  file.link AS "Source Entry"
FROM "02-BRAIN-ENTRIES"
FLATTEN open_questions AS oq
WHERE oq.status = "CLOSED"
  AND oq.question != null
  AND oq.question != ""
SORT file.mtime DESC
```