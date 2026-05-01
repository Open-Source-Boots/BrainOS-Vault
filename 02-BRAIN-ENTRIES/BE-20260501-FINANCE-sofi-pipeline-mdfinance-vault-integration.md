---
title: "BrainOS Financial Pipeline — sofi_extract, mdfinance skill v2, vault integration"
filename: "BE-20260501-FINANCE-sofi-pipeline-mdfinance-vault-integration.md"
date: 2026-05-01
domain: FINANCE
slug: sofi-pipeline-mdfinance-vault-integration
status: ACTIVE
compilation_status: CURRENT
supersedes: []
superseded_by: []
canonical_file: FINANCIAL-SNAPSHOT.md
tags:
  - finance
  - sofi
  - pipeline
  - mdfinance
  - pdfplumber
  - obsidian
  - brainos
  - git
  - pocketpal
open_questions:
  - id: OQ-20260430-001
    question: "What is the current status of the Best Egg account — closed, rolled into DMP, or still active as of May 2026?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-002
    question: "Why did the Apr 2, 2025 GoodLife paycheck deposit as $179.44 instead of the expected ~$658.39 baseline?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-003
    question: "Is the SmartArb transaction on Apr 26 ($39.99 debit + $39.99 credit same day) a refund, a wash trade, or an error?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-004
    question: "What Affirm loan corresponds to the $99.62/month payment (ID R5WSGIGR) — what was purchased and what is the remaining balance?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-005
    question: "What Affirm loan corresponds to the $105.86/month payment (ID L2SE52P3) — what was purchased and what is the remaining balance?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-006
    question: "The Venmo payment of $350.00 on Apr 16, 2025 — who was this to and what was it for?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-007
    question: "PayActiv $183.00 appears Apr 10 as a debit card credit — is this a wage advance that gets auto-repaid, and does it appear regularly in other months?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-008
    question: "PebbleHost ($11.50/month) — what is this server hosting and is it tied to an active project or a recurring forgotten subscription?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-009
    question: "Allstate was $83.99/month in April 2025 vs $253.95 now — on what exact date did the premium increase and was it solely due to the Sienna WAV addition?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-010
    question: "sofi_extract.py outputs filenames like 'FINANCE-EXTRACT-SOFI-April 25.md' with spaces — should the script be updated to use slug format (April-25 → 202504) for consistent Obsidian indexing?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-011
    question: "Does the Syncthing conflict that corrupted sofi_extract.py indicate that Python scripts at vault root should be excluded from Syncthing via .stignore to prevent future merge conflicts?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260430-012
    question: "The 15 SoFi extract files in 00-INBOX cover Jan 2025–Mar 2026 — is April 2026 the most recent statement available, and is there a May 2026 statement yet?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
  - id: OQ-20260430-013
    question: "Can a model operating entirely offline on PocketPal (Qwen2.5-7B) reliably produce YAML-formatted open questions that pass inject_open_questions.py validation without correction?"
    canonical_target: AI-WORKFLOW-RULES.md
    status: OPEN
  - id: OQ-20260430-014
    question: "Git tracked ~8MB of PDFs in the push before .gitignore was updated — should git filter-repo be run to purge binary history from the repo, or is the repo size acceptable as-is?"
    canonical_target: BRAINOS-SYSTEM.md
    status: OPEN
  - id: OQ-20260430-015
    question: "Does the $1,031.80 sent to Robinhood in April 2025 reflect a consistent investing behavior across other months, or was April 2025 an outlier?"
    canonical_target: FINANCIAL-SNAPSHOT.md
    status: OPEN
---

## KEY FACTS

- `sofi_extract.py` was built, conflict-resolved, and pushed to [Open-Source-Boots/BrainOS-Vault](https://github.com/Open-Source-Boots/BrainOS-Vault/blob/main/sofi_extract.py)
- Script successfully extracted 15 months of SoFi statements (Jan 2025 – Mar 2026) in a single batch run
- Extracted `.md` files now sit in `00-INBOX/` with BrainOS frontmatter, ready for canonical update
- `requirements.txt` created — `pip install -r requirements.txt` eliminates manual dependency failure on any device
- `.gitignore` updated — PDFs in `08-ATTACH/FINANCE/` excluded from Git; text extracts in `00-INBOX/` remain tracked
- `SKILL-MDFINANCE.md` v2 written — self-contained, portable to any model including PocketPal offline
- April 2025 SoFi statement (checking -7148 + savings -3045) fully analyzed and categorized
- **Best Egg $410.24/month** active in Apr 2025 — not present in current FINANCIAL-SNAPSHOT.md; status unknown
- **Robinhood: $1,031.80** sent in April 2025 alone while checking ended at $42.93 — primary stress signal
- GoodLife paycheck variance confirmed: Apr 2025 paychecks ranged $179.44–$658.39 across 4 deposits
- Allstate was $83.99/month in Apr 2025 vs $253.95 now — tripled after Sienna WAV purchase (~Mar 2026)
- `08-ATTACH/FINANCE/STATEMENTS/`, `PAYSTUBS/`, `DEBT/`, `LEGAL/`, `PROCESSED/` subfolder structure defined

## TIMELINE MARKERS

- **2026-04-30 ~10:00 PM** — Session began: question about circumventing Perplexity file upload limits
- **2026-04-30 ~11:09 PM** — April 2025 SoFi PDF uploaded and fully parsed in-thread
- **2026-04-30 ~11:29 PM** — mdfinance skill v2 written with YAML open questions, Obsidian frontmatter, canonical update block
- **2026-05-01 ~12:14 AM** — sofi_extract.py v1 generated and committed
- **2026-05-01 ~12:34 AM** — Output path updated to `00-INBOX/`, archive to `08-ATTACH/` added
- **2026-05-01 ~12:37 AM** — Syncthing conflict resolved; `pip install pdfplumber` identified as needed
- **2026-05-01 ~12:42 AM** — `.gitignore` and `requirements.txt` pushed; sofi_extract.py v2 committed
- **2026-05-01 ~12:47 AM** — Batch run complete: 15 months extracted, `00-INBOX/` populated

## UPDATES TO CANONICAL FILES

**FINANCIAL-SNAPSHOT.md:**
- ADD: Best Egg was active Apr 2025 at $410.24/month — confirm current status before adding to debt table
- ADD: Allstate was $83.99 in Apr 2025; increase to $253.95 tied to Sienna WAV (~Mar 2026)
- ADD: GoodLife paycheck variance is real and documented — do not assume $600 flat every Thursday
- ADD: PayActiv wage advance ($183.00) used in Apr 2025 — pattern to watch across other months
- ADD: AT&T confirmed ~$147.65 total in Apr 2025 (two lines); current is $157.98 — minor increase
- FLAG: Robinhood activity ($1,031.80 in one month) needs review across all 15 months

**BRAINOS-SYSTEM.md:**
- ADD: `sofi_extract.py` to Automation Scripts table (vault root, batch-capable, outputs to `00-INBOX/`)
- ADD: `requirements.txt` exists at vault root — run before any script on a new device
- ADD: `08-ATTACH/FINANCE/` subfolder structure (STATEMENTS, PAYSTUBS, DEBT, LEGAL, PROCESSED)

**AI-WORKFLOW-RULES.md:**
- ADD: Python scripts at vault root are vulnerable to Syncthing conflicts — consider `.stignore` exclusion for `.py` files
- ADD: PowerShell does not support `2>/dev/null` — use bare `git` commands without Unix redirection on Windows

## CONTRADICTIONS

- None in canonical files. Best Egg absence from FINANCIAL-SNAPSHOT is a gap, not a contradiction — status unconfirmed.

## INSIGHTS & PATTERNS

- The core insight of this session: **one well-structured pipeline eliminates the file upload problem entirely** — the question was never "how do I upload more files" but "how do I produce less noise per file"
- April 2025 shows a pattern of extreme savings-to-checking transfers (14 transfers) to cover spending that exceeded available checking balance — the savings account was being used as a buffer, not a savings vehicle
- $1,031.80 to Robinhood in a month where checking ended at $42.93 is the clearest financial stress signal in the dataset — this behavior, if consistent, is the primary obstacle to debt payoff progress
- PocketPal + mdfinance skill as system prompt is a viable offline-first mobile pipeline for statement extraction when the input is clean text (CSV export or digital PDF)
- Syncthing + Git operating on the same files without coordination is a confirmed conflict risk — scripts should be excluded from Syncthing or Syncthing should be paused before Git operations

## TOOLS & RESOURCES REFERENCED

- `sofi_extract.py` — vault root, batch PDF extractor for SoFi statements
- `requirements.txt` — vault root, `pip install -r requirements.txt`
- `pdfplumber` — Python library for PDF text extraction
- `SKILL-MDFINANCE.md` v2 — portable financial document parser instructions
- PocketPal (iPhone) — local model runner, Qwen2.5-7B installed
- `inject_open_questions.py` — vault root, injects OQ YAML into Brain Entry frontmatter
- `rebuild_index.py` — `utils/`, regenerates MASTER-INDEX.csv
- [Open-Source-Boots/BrainOS-Vault](https://github.com/Open-Source-Boots/BrainOS-Vault) — GitHub repo, primary sync source

## CROSS-REFERENCES

- FINANCIAL-SNAPSHOT.md — canonical target for all extract updates
- BE-20260430-BRAINOS-csv-push-failure-index-automation.md — prior session establishing CSV generation rules
- BRAINOS-SYSTEM.md — Automation Scripts table needs sofi_extract.py added
- AI-WORKFLOW-RULES.md — PowerShell behavior and Syncthing conflict rules to add

## RAW HIGHLIGHTS

- "The answer isn't how do I upload more files — it's how do I produce one clean file instead of fifty noisy ones"
- 15 months extracted in a single batch run from `08-ATTACH/FINANCE/STATEMENTS/`
- sofi_extract.py survived: merge conflict resolution, missing module error, PowerShell redirection incompatibility, and batch mode — all in one session
- April 2025 combined SoFi balance: opened at $1,003.68, closed at $259.77 — net loss of $743.91 in one month