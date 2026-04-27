---
title: Master Index — BrainOS Vault
filename: MASTER-INDEX.md
updated: 2026-04-26
status: INDEX
---

# 🗂 BrainOS — Master Index

---

## 📋 All Brain Entries

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(thread_date, "—") AS "Date",
  default(domain, "—") AS "Domain",
  default(status, "—") AS "Status",
  default(priority, "—") AS "Priority",
  default(generated_by_skill, "manual") AS "Source"
FROM "02-BRAIN-ENTRIES"
WHERE file.name != "BE-TEMPLATE"
SORT default(thread_date, file.ctime) DESC
```

---

## 🔴 Needs Attention

```dataview
TABLE WITHOUT ID
  file.link AS "Entry",
  default(domain, "—") AS "Domain",
  default(compilation_status, "—") AS "Compilation Status"
FROM "02-BRAIN-ENTRIES"
WHERE status = "draft"
  AND file.name != "BE-TEMPLATE"
SORT file.mtime DESC
```

---

## ✅ Active Projects

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  default(status, "—") AS "Status",
  file.mtime AS "Last Updated"
FROM "03-PROJECTS"
SORT file.mtime DESC
```

---

## 📁 Canonical Files

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  default(status, "—") AS "Status",
  file.mtime AS "Last Updated"
FROM "04-CANONICAL"
SORT file.name ASC
```

---

## 📊 Vault Stats

```dataview
TABLE WITHOUT ID
  length(rows) AS "Count",
  domain AS "Domain"
FROM "02-BRAIN-ENTRIES"
WHERE file.name != "BE-TEMPLATE"
GROUP BY domain
SORT length(rows) DESC
```