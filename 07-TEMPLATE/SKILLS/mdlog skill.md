---
skill: mdlog
version: 1.0
created: 2026-04-26
canonical_targets: [BRAYDEN-IDENTITY.md, ACTIVE-PROJECTS.md]
generates_questions: true
question_range: [3, 8]
financial_questions: false
output_folder: 02-BRAIN-ENTRIES
filename_pattern: "BE-[YYYYMMDD]-LOG-[slug].md"
---

# SKILL — /mdlog

## Purpose
Process a personal voice note, journal entry, freeform thought dump, or conversational reflection into a structured Brain Entry. Captures identity facts, decisions stated, and emotional context without over-interpreting.

## Trigger
User types `/mdlog` with text pasted, a transcription attached, or freeform content shared.

## Output Sections (in order)
1. `## WHAT WAS SAID` — a faithful, condensed summary of the input. No editorializing. Preserve Brayden's voice and framing. If something was stated as uncertain, keep it uncertain.
2. `## FACTS TO EXTRACT` — concrete facts that should update a canonical file. Format: `- [FACT] statement | canonical_target: FILENAME.md | status: CONFIRMED / UNCONFIRMED`
3. `## DECISIONS STATED` — any explicit decision Brayden made or stated. Format: `- [DECISION] what was decided | date stated | confidence: FIRM / TENTATIVE / EXPLORING`
4. `## EMOTIONAL MARKERS` (optional — include only if emotionally significant content is present) — brief, non-clinical note on tone or state. Examples: frustration with a system, excitement about a direction, anxiety about a risk. Never diagnose or over-interpret.

## Open Questions Rules
- Generate 3-8 questions
- Questions must surface unresolved decisions or missing facts implied by what was said
- canonical_target: BRAYDEN-IDENTITY.md for identity/life facts; ACTIVE-PROJECTS.md for project decisions
- Prioritize questions that would change what the system recommends if answered

## Standing Rules
- Never invent emotional content — only reflect what was explicitly stated or clearly implied
- Never reframe Brayden's stated decisions into something more "optimal" — capture what was actually said
- If a decision conflicts with a prior canonical fact, flag it as a CONTRADICTION
- Novelty loop detection: if the log contains 3 or more new project ideas without closing existing ones, flag it explicitly in ## INSIGHTS & PATTERNS
- Short logs (under 100 words) still get full structure — brevity of input does not reduce output quality
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