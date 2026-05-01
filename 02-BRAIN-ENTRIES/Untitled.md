---
title: "BrainOS Naming Convention, vault_rename.py, sofi_extract v3 RAG Format"
filename: "20260501-BE-naming-convention-sofi-extract-v3-rag-format.md"
date: 2026-05-01
domain: BRAINOS
slug: naming-convention-sofi-extract-v3-rag-format
status: ACTIVE
compilation_status: CURRENT
supersedes: []
superseded_by: []
canonical_file: BRAINOS-SYSTEM.md
tags:
  - brainos
  - naming-convention
  - sofi
  - rag
  - dataview
  - smart-connections
  - obsidian
  - vault-rename
open_questions:
  - id: OQ-20260501-001
    question: "Does vault_rename.py --dry-run produce any unexpected renames for files in 03-PROJECTS that should be protected?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-002
    question: "Should 03-PROJECTS files ever carry a date prefix, or are project files always treated as canonical/evergreen like 04-CANONICAL?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-003
    question: "Does the Dataview plugin currently index inline fields (account::, net-change::) from files in 00-INBOX, or does it require files to be moved to a permanent folder first?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-004
    question: "What is the Smart Connections chunk size setting currently configured to — does it split on headings (##), paragraphs, or fixed token count?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-005
    question: "After vault_rename.py --git runs, do any Obsidian internal links (wikilinks) break because they reference old filenames?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-006
    question: "The category engine in sofi_extract.py uses regex keyword matching — what percentage of April 2025 transactions landed in 'other' vs a named category?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260501-007
    question: "Should YYYYMM-FINANCE-sofi-extract.md files live permanently in 00-INBOX after canonical update, or migrate to a dedicated 02-BRAIN-ENTRIES/FINANCE/ subfolder?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-008
    question: "Can a Dataview TABLE query aggregate net-change:: across all 202501–202603 FINANCE extracts into a monthly trend table without custom JS?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-009
    question: "Is the category rule for 'gas' too broad — does 'CASEYS' appear in both food and gas rules, causing double-match ambiguity?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-010
    question: "What happens to the old space-named FINANCE-EXTRACT-SOFI-June 25.md files in 00-INBOX after the batch re-run — are they deleted automatically or left as orphans?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-011
    question: "Does a local RAG model (Qwen2.5-7B via LM Studio) produce meaningfully better financial answers when given the semantic summary paragraph vs the raw transaction table alone?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260501-012
    question: "Is vault_rename.py safe to run repeatedly — does it correctly skip files that already match the convention, or will it re-rename on every pass?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-013
    question: "Should the opening-balance:: field be sourced from the 'Beginning Balance' line (start of period) or the first transaction's balance column (first recorded state)?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260501-014
    question: "At what point does a FINANCE extract file graduate from PENDING-UPDATE to COMPILED — after FINANCIAL-SNAPSHOT.md is updated, or after rebuild_index.py runs?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260501-015
    question: "Does embedding a natural language RAG summary paragraph alongside a structured markdown table improve retrieval recall for amount-specific queries in a local FAISS or ChromaDB index?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
---

## KEY FACTS

- `sofi_extract.py` v3 output filename changed to `YYYYMM-FINANCE-sofi-extract.md` — consistent with new vault naming convention
- `vault_rename.py` created at vault root — enforces `YYYYMMDD-DOMAIN-descriptor` / `YYYYMM-DOMAIN-descriptor` convention across all dated folders
- `05-INDEX/NAMING-CONVENTION.md` created — canonical reference for the naming rule
- Three modes: `--dry-run` (preview), `--apply` (rename locally), `--git` (rename + git mv, preserves history)
- Protected canonical files hardcoded: will never be renamed by the script
- sofi_extract.py v3 adds: per-account Dataview inline fields, RAG semantic summary paragraph, category breakdown table, Category column in transaction table
- Category engine added with 10 rules: income, debt-payment, insurance-utilities, investing, food, gas, subscriptions-entertainment, smoke-alcohol, internal-transfer, transfer-p2p, other
- `CASEYS` appears in both food and gas rules — potential double-match bug (first match wins, so gas wins; may misclassify food purchases at Casey's)
- Old `FINANCE-EXTRACT-SOFI-June 25.md` style files in 00-INBOX are NOT auto-deleted on re-run — manual cleanup or vault_rename.py needed
- Commit SHA: `537ddd5` — [github.com/Open-Source-Boots/BrainOS-Vault](https://github.com/Open-Source-Boots/BrainOS-Vault)

## TIMELINE MARKERS

- **2026-05-01 ~1:02 AM** — June 2025 debug output provided; page continuation bug root-caused and fixed
- **2026-05-01 ~1:07 AM** — RAG/Dataview/Smart Connections output format requested
- **2026-05-01 ~1:09 AM** — sofi_extract.py v3 pushed with category engine and semantic summary
- **2026-05-01 ~1:19 AM** — Naming convention discussion; vault_rename.py requested
- **2026-05-01 ~1:24 AM** — vault_rename.py, NAMING-CONVENTION.md, and sofi_extract.py v4 filename fix pushed together

## UPDATES TO CANONICAL FILES

**BRAINOS-SYSTEM.md:**
- ADD: Naming convention rule — `YYYYMMDD-DOMAIN-descriptor.md` / `YYYYMM-DOMAIN-descriptor.md` / `DOMAIN-DESCRIPTOR.md`
- ADD: `vault_rename.py` to Automation Scripts table (vault root, `--dry-run / --apply / --git`)
- ADD: `05-INDEX/NAMING-CONVENTION.md` exists as canonical naming reference
- ADD: sofi_extract.py v3+ output format includes inline Dataview fields, RAG summary, category table, Category column
- ADD: Old space-based FINANCE extract files in 00-INBOX must be manually deleted or renamed after re-run

**AI-WORKFLOW-RULES.md:**
- ADD: RAG optimization principle — every structured data file should include a natural language summary paragraph before the table to improve embedding anchor quality

## CONTRADICTIONS

- None detected.

## INSIGHTS & PATTERNS

- Alphabetical sort = chronological sort is a zero-cost Obsidian optimization — the naming convention eliminates the need for any custom sort plugin
- The category engine's "first match wins" behavior means rule order matters — income and internal-transfer rules should always be listed before catchall rules like 'other'
- `CASEYS` in both food and gas is a real ambiguity: Casey's General Store sells both; splitting by transaction type (Debit Card vs Direct Payment) could resolve it in a future version
- vault_rename.py is idempotent by design — files already matching the convention are skipped, making it safe to run repeatedly as an audit tool

## TOOLS & RESOURCES REFERENCED

- `vault_rename.py` — vault root, `python vault_rename.py --dry-run / --apply / --git`
- `sofi_extract.py` v3 — category engine, RAG summary, Dataview inline fields, corrected output filename
- `05-INDEX/NAMING-CONVENTION.md` — naming convention reference
- Obsidian Dataview plugin — inline field syntax (`field:: value`)
- Smart Connections — semantic chunking via `##` headings

## CROSS-REFERENCES

- BE-20260501-FINANCE-sofi-pipeline-mdfinance-vault-integration.md — prior session this thread
- BRAINOS-SYSTEM.md — Automation Scripts table, naming convention
- AI-WORKFLOW-RULES.md — RAG summary paragraph principle
- FINANCIAL-SNAPSHOT.md — canonical target for all extract updates

## RAW HIGHLIGHTS

- "Alphabetical sort = chronological sort for free" — the core insight of the naming convention session
- vault_rename.py handles every legacy pattern in the vault in one pass with git mv support
- sofi_extract.py now produces files that serve Dataview queries, Smart Connections RAG, local LLM context, and human skimming simultaneously — four consumers, one output format