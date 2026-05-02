---
title: "Laptop Optimization, LM Studio 0.4.12 Config, and Financial Extraction Architecture"
filename: "20260502-BRAINOS-laptop-lmstudio-mdfinancial-architecture-BE.md"
date: 2026-05-02
domain: BRAINOS-SYSTEM
slug: laptop-lmstudio-mdfinancial-architecture
status: COMPILED
compilation_status: COMPLETE
supersedes: 20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md
superseded_by: null
canonical_file: DEVICE-ECOSYSTEM.md, AI-WORKFLOW-RULES.md
tags: [laptop, lm-studio, optimization, mdfinancial, token-budget, system-prompt, qwen, windows, powershell, financial-extraction]
open_questions:
  - id: OQ-20260502-001
    question: "What is the actual logical processor count shown in Task Manager → Performance → CPU → Logical Processors on the laptop?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-002
    question: "Did setting the pagefile to Initial 4096 / Max 16384 MB get applied before reboot on 2026-05-02?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-003
    question: "After running brainos-laptop-optimize.ps1, what was the idle RAM usage in Task Manager post-reboot?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-004
    question: "At 6 CPU threads vs 4, does Qwen2.5-7B produce measurably higher t/s without thermal throttle on the laptop?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-005
    question: "Does the compressed-mdfinancial prompt produce clean structured output on the first live SoFi statement test?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260502-006
    question: "What is the average token length of a single SoFi monthly statement when converted to plain text?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260502-007
    question: "Should Robinhood extraction get its own compressed prompt variant before or after the first bank statement pipeline is proven stable?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260502-008
    question: "At what point does FINANCIAL-SNAPSHOT.md transition from manual canonical updates to a script-aggregated ledger (Stage 2)?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260502-009
    question: "Is there a consistent naming convention for LM Studio extracted output files saved to 05-FINANCE/ before that folder exists?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260502-010
    question: "Can a single n8n workflow eventually watch a folder, detect new extracted .md files, and auto-append to FINANCIAL-SNAPSHOT.md?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260502-011
    question: "Does ISLC need to be set to run at startup, or is it manually triggered before each LM Studio session?"
    canonical_target: DEVICE-ECOSYSTEM.md
    status: OPEN
  - id: OQ-20260502-012
    question: "What is the token count of the full SKILL-MDFINANCE.md file, and does it need to be archived rather than kept as active reference?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260502-013
    question: "Should brainos-laptop-optimize.ps1 be version-controlled in utils/ and run on a schedule, or only manually on demand?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260502-014
    question: "Will the financial extraction pipeline eventually need a dedicated 05-FINANCE/ folder with subfolders per institution or per month?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260502-015
    question: "Is the BE-at-tail naming convention retroactively applied to existing mis-named BEs, or only enforced going forward?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
---

## KEY FACTS
- Laptop confirmed: Intel i5-1135G7, 8GB RAM, Iris Xe, Windows 10 Pro, LM Studio **0.4.12**
- `brainos-laptop-optimize.ps1` ran successfully 2026-05-02 — Intel DSA, Lenovo Vantage, OneDrive startup, gaming launchers disabled; GamingServices and DoSvc access-denied errors are non-blocking
- Active model confirmed: **Qwen2.5-7B-Instruct Q4_K_M**
- Canonical LM Studio settings locked: 4096 context, 0 GPU layers, 4 CPU threads (6 testable via manual type), 128 eval batch, Flash Attention ON, KV Q4_0, mmap ON, mlock OFF
- Pagefile recommended: Initial 4096 MB / Max 16384 MB on C: drive
- ISLC free memory threshold: 2048 MB; list size: 1024 MB
- Compressed mdfinancial prompt: ~420 tokens — `07-TEMPLATE/compressed-mdfinancial.md`
- System prompt rule established: ≤500 tokens, behavioral directives only
- Tiered token budget: Tier 1 ≤500 / Tier 2 ~2,500–3,000 / Tier 3 ~500–1,000
- LM Studio is extract-only — Perplexity handles all vault updates
- mdfinancial prompt covers: bank statements fully; debt/paystubs/Robinhood need dedicated compressed variant files
- Financial extraction roadmap: Stage 1 (manual extract now) → Stage 2 (script aggregation) → Stage 3 (RAG query layer)
- BE naming convention confirmed: `YYYYMMDD-[DOMAIN]-[slug]-BE.md` — BE at tail, date leads
- This BE supersedes: `20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md` (earlier partial summary from same thread)

## TIMELINE MARKERS
- ~10:00 AM: ISLC and virtual memory dialog open; optimizer script run from Desktop
- ~11:00 AM: Earlier partial BE uploaded to vault (`20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md`)
- ~12:00 PM: Full LM Studio 0.4.12 settings reference and section-by-section breakdown built
- ~3:19 PM: Conflicts identified across DEVICE-ECOSYSTEM, model names, CPU threads, LM Studio version
- ~3:26 PM: Conflicts resolved — Qwen2.5-7B confirmed, CPU thread note clarified
- ~3:30 PM: DEVICE-ECOSYSTEM.md and compressed-mdfinancial.md pushed in single commit
- ~3:39 PM: AI-WORKFLOW-RULES.md updated with system prompt architecture and LM Studio session rules
- ~4:05 PM: BE naming convention conflict identified; correct filename format confirmed
- ~4:06 PM: This BE pushed with corrected naming convention

## UPDATES TO CANONICAL FILES
- `DEVICE-ECOSYSTEM.md` — LM Studio version 0.4.9 → 0.4.12; model table corrected to Qwen2.5-7B-Instruct Q4_K_M; CPU thread note; pagefile entry; optimizer script note; four generation presets table added; RoPE notes updated for Qwen 2.5
- `AI-WORKFLOW-RULES.md` — System Prompt Architecture section added (≤500 token rule, tiered budget, compressed prompt standard); LM Studio Session Rules section added (one doc per session, pre-convert PDFs, chunking, extract-only rule, document-type→prompt mapping table); 6 new Rule Origin Index rows
- `07-TEMPLATE/compressed-mdfinancial.md` — new file created; ~420 tokens; links to full SKILL-MDFINANCE.md as read-only reference

## CONTRADICTIONS
- DEVICE-ECOSYSTEM previously listed Qwen 3.5 9B and Gemma 4 E4B as installed — confirmed incorrect; resolved to Qwen2.5-7B-Instruct Q4_K_M active, Gemma 3 1B fallback
- LM Studio version was 0.4.9 in canonical — corrected to 0.4.12
- CPU thread count: canonical said 4 (UI slider max), AI recommended 6 (manual type-in) — both preserved with benchmark test note; not yet resolved
- Earlier BE in same thread (`20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md`) was a partial summary; this BE is the complete record and supersedes it

## INSIGHTS & PATTERNS
- The mdfinancial extraction pipeline is now fully architected before first use — system prompt, token budget rules, document-type variants, and vault update workflow all defined in canonical files
- Financial extraction Stage 1→2→3 roadmap makes the current manual discipline the necessary foundation for future automation
- The optimizer script + ISLC + pagefile changes together form a complete RAM management stack for the laptop — these should be documented as a repeatable setup procedure
- BE naming convention (BE-at-tail) was violated in the earlier partial summary and caught before final push — convention is now reinforced

## TOOLS & RESOURCES REFERENCED
- ISLC (Intelligent Standby List Cleaner) — free memory threshold 2048 MB, list size 1024 MB
- `brainos-laptop-optimize.ps1` — currently at C:\Users\brayd\Desktop; needs move to `utils/`
- LM Studio 0.4.12 — Developer Mode required to expose full settings panel
- Windows Virtual Memory dialog: System Properties → Advanced → Performance → Settings → Advanced → Virtual memory
- `07-TEMPLATE/compressed-mdfinancial.md` — active LM Studio system prompt for financial extraction

## CROSS-REFERENCES
- `04-CANONICAL/DEVICE-ECOSYSTEM.md` — primary update target; all laptop + LM Studio settings live here
- `04-CANONICAL/AI-WORKFLOW-RULES.md` — system prompt architecture and LM Studio session rules added
- `07-TEMPLATE/compressed-mdfinancial.md` — new compressed prompt file
- `07-TEMPLATE/SKILL-MDFINANCE.md` — full reference skill; read-only; not for LM Studio paste
- `FINANCIAL-SNAPSHOT.md` — downstream target for first SoFi extraction output
- `05-FINANCE/FINANCE-REGISTER.md` — statement processing ledger (created 2026-05-01)
- `20260502-DEVICE-ECOSYSTEM-laptop-optimization-8gb-iris-xe-BE.md` — superseded partial BE from same thread

## RAW HIGHLIGHTS
- "LM Studio is extract-only. Perplexity updates the vault."
- "One document per session. Context will truncate early documents silently."
- "Robinhood needs its own compressed prompt — entirely different schema."
- "You're at Stage 1. The discipline you build today makes Stage 3 possible."
- "BE naming: date leads, domain second, BE at the tail."
