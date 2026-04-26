---
skill: mdfinancial
version: 1.0
created: 2026-04-26
canonical_targets: [FINANCIAL-SNAPSHOT.md]
generates_questions: false
question_range: [0, 0]
financial_questions: false
output_folder: 02-BRAIN-ENTRIES
filename_pattern: "BE-[YYYYMMDD]-FINANCIAL-[slug].md"
---

# SKILL — /mdfinancial

## Purpose
Process a financial document — bank statement, pay stub, Affirm statement, receipt, invoice — into a structured Brain Entry containing only confirmed figures. No narrative. No interpretation. Numbers and dates only.

## Trigger
User types `/mdfinancial` with a document attached or content pasted.

## Output Sections (in order)
1. `## DOCUMENT TYPE & PERIOD` — document type, issuing institution, period covered (start date → end date), account or reference number if present
2. `## CONFIRMED FIGURES` — every dollar amount, date, and quantity extractable from the document. Format: `- [CONFIRMED] $X.XX | description | date | source line`
3. `## DISCREPANCIES` — any figure that conflicts with a previously confirmed number in FINANCIAL-SNAPSHOT.md. Format: `- Prior: $X | This document: $Y | Source: [filename] | Status: UNRESOLVED`
4. `## NOTES` — anything that requires human attention before the figure can be trusted. Examples: partial period, estimated figure, unclear category.

## Standing Rules
- Never generate open questions — financial questions are handled through the dedicated financial pipeline
- Never interpret or narrate figures — extract and label only
- Every figure gets one of two labels: [CONFIRMED] or [UNCONFIRMED]
- [CONFIRMED] = number appears explicitly in the source document
- [UNCONFIRMED] = number was calculated, estimated, or inferred
- If a pay stub shows gross and net, list both — never assume which applies
- Rent deduction mechanism: $500 deducted at source per pay period (2x/month = $1,000/month total) — flag if this does not match document
- Do not round figures — preserve exact cents
- Flag any figure that differs from FINANCIAL-SNAPSHOT.md by more than $50
## Output Frontmatter (exact order, every file)
title:
filename:
date:
domain:
slug:
status: draft
compilation_status: pending
supersedes: none
superseded_by: none
canonical_file:
generated_by_skill:
skill_version:
tags: []
open_questions: []