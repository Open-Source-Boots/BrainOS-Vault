---
title: Open Questions
filename: OPEN-QUESTIONS.md
updated: 2026-04-25
status: CANONICAL
---
---
title: Open Questions
filename: OPEN-QUESTIONS.md
updated: 2026-04-25
status: CANONICAL
---

# ❓ Open Questions — Unanswered

> To close a question: open the source file, find the matching question block in frontmatter, change `status: OPEN` → `status: CLOSED`.

```dataview
TABLE rows.file.link AS "Source File", rows.open_questions AS "Questions"
FROM ""
WHERE open_questions
GROUP BY file.link
```