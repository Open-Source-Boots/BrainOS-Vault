---
name: mdreference
version: 1.1
created: 2026-04-26
canonical_targets: [BRAINOS-SYSTEM.md, ACTIVE-PROJECTS.md, SKILLS-EDUCATION.md, DEVICE-ECOSYSTEM.md, GLWC-PROJECT.md]
generates_questions: true
question_range: [3, 5]
financial_questions: false
output_folder: 02-BRAIN-ENTRIES
filename_pattern: "BE-[YYYYMMDD]-SOURCE-[slug].md"
label_vocabulary: [CONFIRMED, UNCONFIRMED, CONTRADICTION, NOTE]
description: pulling inspiration, capturing ideas, unfriendly files
---

# SKILL — /mdreference

## Purpose
Process a research document, article, guide, PDF, or external reference into a structured Brain Entry that extracts actionable facts and connects them to active projects and canonical files.

## Trigger
User types `/mdreference` with a document attached, URL pasted, or content quoted.

## Output Sections (in order)
1. `## SOURCE INFO` — title, author or organization, publication date if known, URL or file reference, document type (article / PDF / guide / regulation / other)
2. `## KEY FACTS` — bulleted list of factual claims extractable from the source. Each fact gets: the fact itself, direct relevance to Brayden's projects or canonical files, confidence level (HIGH / MEDIUM / LOW)
3. `## RELEVANT QUOTES` — verbatim excerpts worth preserving. Label each with page or section number if available.
4. `## HOW THIS CONNECTS` — explicit links to active projects, canonical files, or open questions this source informs. Be specific — name the file and the section it updates.

## Open Questions Rules
- Generate 3-5 questions
- Questions must be about how to act on this information, not about the document itself
- canonical_target based on subject matter — default to BRAINOS-SYSTEM.md if unclear
- Never generate financial questions

## Standing Rules
- Distinguish between facts stated in the source vs. interpretations drawn from it
- Flag any claim that contradicts existing canonical file content as a CONTRADICTION
- If the source is a legal regulation, cross-reference with mdlegal skill rules
- If the source is tool documentation, canonical_target defaults to DEVICE-ECOSYSTEM.md
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

[CONFIRMED] — fact verified in source document
[UNCONFIRMED] — fact inferred, estimated, or not directly stated
[RISK] — creates personal exposure
[PROTECTION] — mitigates exposure
[CONTRADICTION] — conflicts with existing canonical file
[DECISION] — explicit choice stated by Brayden
[NOTE] — requires human attention before acting