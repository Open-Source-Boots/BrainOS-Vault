---
title: Master Index — BrainOS Vault
filename: MASTER-INDEX.md
updated: 2026-04-27
status: INDEX
tags: [index, dataview, canonical, brainos]
note: "This file is read-only navigation. All edits flow into Brain Entries and Canonical files — not here. Powered by Dataview plugin."
cross-references:
  - "[[BRAINOS-SYSTEM]]"
  - "[[BRAYDEN-IDENTITY]]"
  - "[[ACTIVE-PROJECTS]]"
  - "[[FINANCIAL-SNAPSHOT]]"
  - "[[DEVICE-ECOSYSTEM]]"
  - "[[SKILLS-EDUCATION]]"
  - "[[AI-WORKFLOW-RULES]]"
---

# 🗂️ BrainOS — Master Index

> Navigation hub for the full vault. Read-only — edit the source files, not this one.
> Canonical files: [[BRAINOS-SYSTEM]] · [[BRAYDEN-IDENTITY]] · [[ACTIVE-PROJECTS]] · [[FINANCIAL-SNAPSHOT]] · [[DEVICE-ECOSYSTEM]] · [[SKILLS-EDUCATION]] · [[AI-WORKFLOW-RULES]]

---

## 🔴 Action Required — Priority 1 (Active, Unresolved)

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(thread_date, "—") AS "Date",
  default(domain, "—") AS "Domain",
  default(action_required, "—") AS "Next Action"
FROM "02-BRAIN-ENTRIES"
WHERE status = "ACTIVE"
  AND priority = 1
  AND file.name != "BE-TEMPLATE"
SORT thread_date DESC
```

---

## 🟡 Active — All Entries

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(thread_date, "—") AS "Date",
  default(domain, "—") AS "Domain",
  default(priority, "—") AS "P",
  default(action_required, "—") AS "Next Action"
FROM "02-BRAIN-ENTRIES"
WHERE status = "ACTIVE"
  AND file.name != "BE-TEMPLATE"
SORT priority ASC, thread_date DESC
```

---

## ✅ Canonical Entries

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(thread_date, "—") AS "Date",
  default(domain, "—") AS "Domain",
  default(canonical_file, "—") AS "Lives In"
FROM "02-BRAIN-ENTRIES"
WHERE status = "CANONICAL"
  AND file.name != "BE-TEMPLATE"
SORT thread_date DESC
```

---

## 📊 Domain Breakdown

```dataview
TABLE WITHOUT ID
  domain AS "Domain",
  length(rows) AS "Total Entries",
  length(filter(rows, (r) => r.status = "ACTIVE")) AS "Active",
  length(filter(rows, (r) => r.status = "CANONICAL")) AS "Canonical",
  length(filter(rows, (r) => r.status = "SUPERSEDED")) AS "Superseded"
FROM "02-BRAIN-ENTRIES"
WHERE file.name != "BE-TEMPLATE"
GROUP BY domain
SORT length(rows) DESC
```

---

## 🗄️ Canonical Files

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  default(status, "—") AS "Status",
  file.mtime AS "Last Modified"
FROM "04-CANONICAL"
SORT file.name ASC
```

---

## 🛄 Project Files

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  default(status, "—") AS "Status",
  file.mtime AS "Last Modified"
FROM "03-PROJECTS"
SORT file.mtime DESC
```

---

## 🔍 Full Archive (All Brain Entries)

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(thread_date, "—") AS "Date",
  default(domain, "—") AS "Domain",
  default(status, "—") AS "Status",
  default(priority, "—") AS "P"
FROM "02-BRAIN-ENTRIES"
WHERE file.name != "BE-TEMPLATE"
SORT thread_date DESC
```
