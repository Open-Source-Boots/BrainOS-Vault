---
title: FINANCE-REGISTER
filename: FINANCE-REGISTER.md
date: 2026-05-01
domain: FINANCE
status: ACTIVE
compilation_status: CURRENT
tags:
  - finance
  - index
  - register
  - brainos
note: >
  This file is a lightweight ledger of all processed financial statement
  extracts. One row per statement per account. Updated manually after each
  confirmed canonical update. Never AI-rewritten in bulk.
---

# FINANCE-REGISTER

Lightweight index of every financial statement processed through `mdfinancial`
and confirmed into `FINANCIAL-SNAPSHOT.md`. One row per statement per account.

To add a row: after confirming a canonical update, append one row below.
Do not edit existing rows. Archive column reflects move from `00-INBOX/` to `08-ATTACH/`.

---

## Processed Statements

| Institution | Account | Last 4 | Period | Closing Balance | Extract File | Archived | Notes |
|-------------|---------|--------|--------|-----------------|--------------|----------|---------|
| — | — | — | — | — | — | — | No statements processed yet |

---

## How to Add a Row

After a statement is confirmed and `FINANCIAL-SNAPSHOT.md` is updated:

1. Add one row to the table above
2. Format: `Institution | Checking/Savings | XXXX | Mon YYYY | $X,XXX.XX | [[filename]] | ✅/⏳ | any notes`
3. Move the extract file from `00-INBOX/` to `08-ATTACH/` and mark Archived `✅`
4. Commit: `FINANCE register add [institution] [account-type] [YYYYMM]`

## Register Rules

- **One row per statement per account.** Checking and savings are separate rows even if processed together.
- **Never skip a row** even if the statement had no activity — log it with `$0.00 net change` and a note.
- **Closing Balance** is the figure from Section 1 of the extract, not a calculated value.
- **Extract File** links to the archived file in `08-ATTACH/` once confirmed. Use Obsidian `[[wikilink]]` format.
- **Archived** column: `⏳` = in `00-INBOX/` (pending), `✅` = moved to `08-ATTACH/` (confirmed).

---

## Dataview Query (paste into any note to render)

```dataview
TABLE WITHOUT ID
  institution AS Institution,
  account AS Account,
  period AS Period,
  closing_balance AS "Closing Bal",
  file.link AS Extract,
  archived AS Archived
FROM "08-ATTACH"
WHERE domain = "FINANCE" AND status = "PENDING-UPDATE" OR status = "ARCHIVED"
SORT date DESC
```
