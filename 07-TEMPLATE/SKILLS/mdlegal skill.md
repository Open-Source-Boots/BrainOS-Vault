---
skill: mdlegal
version: 1.0
created: 2026-04-26
canonical_targets: [GLWC-PROJECT.md, BRAYDEN-IDENTITY.md]
generates_questions: true
question_range: [5, 10]
financial_questions: false
output_folder: 02-BRAIN-ENTRIES
filename_pattern: "BE-[YYYYMMDD]-LEGAL-[slug].md"
---

# SKILL — /mdlegal

## Purpose
Process a legal document — contract, lease, MOU, agreement, or regulatory text — into a structured Brain Entry that maps risk, protections, key parties, and unresolved clauses.

## Trigger
User types `/mdlegal` with a document attached or content pasted.

## Output Sections (in order)
1. `## PARTIES & DATES` — full names of all signing parties, effective dates, expiration dates, governing law
2. `## KEY CLAUSES` — verbatim quotes of clauses that create obligation, restriction, or risk. Never paraphrase critical language. Label each clause with its section number if available.
3. `## RISK FLAGS` — clauses that create personal exposure for Brayden. Each flag gets: clause name, verbatim excerpt, risk assessment, mitigation status (OPEN / MITIGATED / RESOLVED)
4. `## PROTECTIONS` — clauses, regulations, or legal frameworks that protect Brayden or persons served. Include federal and state references where applicable.
5. `## UNCONFIRMED — needs verification` — any clause whose full language was not available in this document, any date or figure that could not be confirmed, any legal interpretation that requires a real attorney.
6. `## CROSS-REFERENCES` — other Brain Entries, canonical files, or legal references this document connects to.

## Open Questions Rules
- Generate 5-10 questions
- Every question must target a real unresolved clause, date, or legal interpretation
- canonical_target: GLWC-PROJECT.md for GoodLife/employment documents; BRAYDEN-IDENTITY.md for personal/household documents
- Never generate a question about a fact already confirmed verbatim in this document
- Never generate financial questions

## Standing Rules
- Quote clauses verbatim — never paraphrase away from exact language
- Label every quote with its source section if known
- Flag any NDA, non-compete, arbitration, or termination clause as a RISK FLAG automatically
- Apply Two-Hat principle: distinguish DSP (W2/NLRA) exposure from PFT (contractor) exposure
- If a clause conflicts with a federal or state regulation, note the tension explicitly
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