---
title: Open Questions
filename: OPEN-QUESTIONS.md
updated: 2026-04-25
status: CANONICAL
---

# ❓ Open Questions — Unanswered

> This list is auto-generated. To close a question, open its source file and change `status: OPEN` to `status: CLOSED`. It disappears from this table automatically on next refresh.

```dataview
TABLE question, canonical_target, file.link AS "Source File"
FROM ""
FLATTEN open_questions AS oq
WHERE oq.status = "OPEN"
SORT file.name ASC
```

## How to Answer a Question

1. Find the source file in the table above
2. Confirm or research the answer
3. Write the answer into the `canonical_target` file listed
4. Open the source file, find the matching `open_questions` block in frontmatter
5. Change `status: OPEN` → `status: CLOSED`
6. Table removes it on next Dataview refresh