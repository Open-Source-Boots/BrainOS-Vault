---
title: mdfinancial Skill Overhaul + LM Studio Laptop Optimization
filename: 20260501-FINANCE-mdfinancial-skill-overhaul-BE.md
date: 2026-05-01
domain: FINANCE
slug: mdfinancial-skill-overhaul
status: ACTIVE
compilation_status: CURRENT
supersedes: ""
superseded_by: ""
canonical_file: FINANCIAL-SNAPSHOT.md
tags:
  - finance
  - mdfinancial
  - lm-studio
  - brainos
  - skill
  - device
  - qwen
  - system
open_questions:
  - id: OQ-20260501-001
    question: "What is the actual logical processor count on the laptop's i5-1135G7 as reported by Task Manager > Performance > Logical processors?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-002
    question: "After applying the canonical LM Studio settings, what is the actual estimated memory usage reported by LM Studio for Qwen 3.5 9B Q4_K_M?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-003
    question: "What is the tokens-per-second output speed for Qwen 3.5 9B at the canonical settings on the laptop?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-004
    question: "Has the first SoFi bank statement been processed through mdfinancial v2.3 and confirmed into FINANCIAL-SNAPSHOT.md yet?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260501-005
    question: "Does FINANCIAL-SNAPSHOT.md currently contain a confirmed bill schedule with due dates accurate enough to generate a valid Section 9 projection without [UNCONFIRMED] placeholders?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260501-006
    question: "Is the laptop CPU spec confirmed as Intel Core i5-1135G7 @ 2.40GHz, or does a different model appear in Device Manager / System Information?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-007
    question: "When K and V cache quantization are both set to Q4_0 in LM Studio, does output quality for structured markdown tables degrade noticeably compared to no quantization?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-008
    question: "At what context length does Qwen 3.5 9B start to lose coherence on multi-section mdfinancial output on the laptop — 4k, 8k, or higher?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-009
    question: "Is there a meaningful quality difference between running Qwen 3.5 with thinking OFF vs ON for the mdfinancial structured extraction task, or does thinking ON produce more accurate delta calculations?"
    canonical_target: AI-WORKFLOW-RULES
    status: OPEN
  - id: OQ-20260501-010
    question: "What is the theoretical maximum token throughput of the i5-1135G7's integrated memory bandwidth, and does it impose a hard ceiling below what Qwen 3.5 9B can achieve?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260501-011
    question: "Does the period-over-period delta table in Section 10 of mdfinancial produce actionable insight at the 1-month mark, or does it require 3+ months of data to surface meaningful patterns?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260501-012
    question: "If the KV cache is fully offloaded to CPU (Offload KV Cache to GPU = Off) and GPU Offload Layers = 0, what fraction of inference time is spent on memory-bound operations vs compute-bound on this CPU?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
---

## KEY FACTS

- Session date: 2026-05-01
- Laptop hostname confirmed: DESKTOP-QS71AHN (default Windows name, not yet renamed)
- Laptop specs: Intel Core i5-1135G7, Intel Iris Xe integrated GPU, 8GB RAM [UNCONFIRMED exact CPU model]
- LM Studio version on laptop: 0.4.9
- Models installed: Qwen 3.5 9B Q4_K_M (structured output), Gemma 4 E4B Instruct Q4_K_M (general sessions)
- Previous misconfigured LM Studio memory estimate: 16.80GB (over laptop ceiling)
- Canonical optimized memory estimate: ~3.5–5GB
- mdfinancial skill upgraded from v2.0 → v2.3 across this session
- FINANCE-REGISTER.md created as new index file in 05-INDEX/
- NAMING-CONVENTION.md updated with BE-at-tail format and sidebar-first principle
- All 6 commits pushed to Open-Source-Boots/BrainOS-Vault main branch

## TIMELINE MARKERS

- ~14:57 CDT — Session opened, confirmed GOODLIFE-UNION → GLWC-PROJECT fix push successful
- ~14:59 CDT — NAMING-CONVENTION.md updated (v2, BE-at-tail, sidebar-first)
- ~15:00 CDT — mdfinancial improvement audit: 8 areas identified
- ~15:12 CDT — mdfinancial v2.1 pushed (Section 9 projection block, thinking-off instruction, granular tags)
- ~15:13 CDT — mdfinancial v2.2 pushed (running balance Sections 2–4, debt delta tracking Section 3)
- ~15:15 CDT — FINANCE-REGISTER.md created; mdfinancial v2.3 pushed (Section 10 period-over-period delta, register pointer)
- ~15:27 CDT — LM Studio optimization discussion; canonical settings determined
- ~15:55 CDT — DEVICE-ECOSYSTEM.md updated with hostname, CPU, full LM Studio canonical settings table
- ~16:16 CDT — /mdsummary triggered

## UPDATES TO CANONICAL FILES

- **NAMING-CONVENTION.md** (05-INDEX): BE-at-tail format canonized, sidebar-first principle documented, GLWC dead reference warning added
- **mdfinancial skill.md** (07-TEMPLATE/SKILLS): v2.0 → v2.3; added Sections 9 and 10, running balance, debt delta, KV cache instruction, register pointer, granular tags
- **FINANCE-REGISTER.md** (05-INDEX): New file created — statement processing ledger, one row per extract
- **DEVICE-ECOSYSTEM.md** (04-CANONICAL): Laptop hostname added, CPU spec added [UNCONFIRMED], LM Studio models table added, full 15-field advanced settings canonical config added

## CONTRADICTIONS

- None identified this session.

## INSIGHTS & PATTERNS

- The single largest memory consumer in LM Studio is context length, not model size or GPU layers. Dropping from 262k → 4k context is responsible for the majority of the 16.80GB → ~4GB reduction.
- Intel Iris Xe integrated GPU sharing system RAM means GPU offload layers provide zero memory benefit — they move pressure within the same 8GB pool, not to separate VRAM.
- KV cache quantization (Q4_0 for both K and V) is the second most impactful lever after context length, cutting cache memory by ~50–75%.
- mdfinancial is now a full financial analyst pipeline: extract → reconcile → project → compare. It was previously only an extractor.
- The FINANCE-REGISTER serves as the prerequisite gate for Section 10 period-over-period delta — the section self-disables gracefully until a second statement exists.

## TOOLS & RESOURCES REFERENCED

- LM Studio 0.4.9 (laptop)
- Qwen 3.5 9B Q4_K_M
- Gemma 4 E4B Instruct Q4_K_M
- mdfinancial skill.md (07-TEMPLATE/SKILLS)
- FINANCE-REGISTER.md (05-INDEX)
- NAMING-CONVENTION.md (05-INDEX)
- DEVICE-ECOSYSTEM.md (04-CANONICAL)
- GitHub repo: Open-Source-Boots/BrainOS-Vault

## CROSS-REFERENCES

- [[FINANCIAL-SNAPSHOT.md]] — target of all mdfinancial extracts
- [[FINANCE-REGISTER.md]] — new index, gates Section 10
- [[DEVICE-ECOSYSTEM.md]] — canonical LM Studio settings live here
- [[NAMING-CONVENTION.md]] — BE-at-tail format now canonical
- [[AI-WORKFLOW-RULES.md]] — thinking-off instruction relevant here
- [[BRAINOS-SYSTEM.md]] — skill architecture

## RAW HIGHLIGHTS

- "DESKTOP-QS71AHN is my laptop, that is just a default name"
- Previous LM Studio config: context 262144, 13 GPU layers, no KV quantization, 4 concurrent, estimated 16.80GB
- Canonical config: context 4096, 0 GPU layers, KV Q4_0, 1 concurrent, flash attention on, mmap on, keep in memory on
- mdfinancial improvements tackled one section at a time per Brayden's instruction
- FINANCE-REGISTER created before Section 10 was added so the pointer was live before the reference
