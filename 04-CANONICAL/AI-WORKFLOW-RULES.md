---
title: AI Workflow Rules
filename: AI-WORKFLOW-RULES.md
updated: 2026-05-02
status: CANONICAL
domain: BRAINOS-SYSTEM
note: This is a canonical file. Rules flow INTO it from brain entries, not out of it. Every rule must have an origin.
---

# AI Workflow Rules — Canonical Reference

These are the non-negotiable standing rules for every AI session inside BrainOS. When a rule is broken or a new failure mode is discovered, a brain entry is compiled and the relevant rule is added here.

---

## Core Principles

1. **AI writes structure, Brayden fills numbers.** Never invent financial figures, debt balances, income amounts, dates, or device specs. If a number is needed and not confirmed in canonical files, mark it `[UNCONFIRMED]` and ask. Exception: calculations and projections derived from Brayden-confirmed figures are allowed, clearly labeled as derived outputs. (Origin: BrainEntry006)
2. **Single scoped task before starting.** Define the task, then execute. Do not expand scope mid-session without a checkpoint.
3. **Checkpoint every 2–3 actions.** Especially in browser automation or multi-step file operations. Stop and confirm before continuing.
4. **Prefer reversible actions.** If an action cannot be undone, stop and reassess. Ask before proceeding.
5. **Never fabricate.** If a fact is not in canonical files or confirmed in the current thread, it does not exist. Do not fill gaps with plausible-sounding data.

---

## System Prompt Architecture

Origin: 2026-05-02 thread (laptop optimization + LM Studio session)

### Rule: System prompts are behavioral directives only
- A system prompt must contain **only** role definition, output format rules, and standing constraints.
- Background knowledge, domain context, and reference data are **not** system prompt content — they are injected as user-turn context or attached files.
- Target ceiling: **≤500 tokens** for any system prompt used in LM Studio at 4,096 context.
- Violating this consumes context that belongs to the document being processed.

### Rule: Token budget is tiered
At 4,096 context on the laptop, allocate as follows:

| Tier | Budget | Content |
|---|---|---|
| Tier 1 — System Prompt | ≤500 tokens | Behavioral rules, output format, standing constraints |
| Tier 2 — Document / Input | ~2,500–3,000 tokens | Attached statement, file, or pasted content |
| Tier 3 — Response | ~500–1,000 tokens | Model output |

- If Tier 2 + Tier 3 would exceed the window, chunk the input — never shrink Tier 1 to compensate.
- At higher context (8,192+), these ratios scale proportionally.

### Rule: Compressed prompts are the LM Studio standard
- The compressed mdFinancial prompt (~420 tokens) is the canonical system prompt for all financial document extraction on the laptop.
- File location: `07-TEMPLATE/compressed-mdfinancial.md`
- The full-length reference skill (`07-TEMPLATE/SKILL-MDFINANCE.md`) is for reading and editing — never paste the full skill into LM Studio.
- When new document types require extraction (debt statements, pay stubs, Robinhood), create a dedicated compressed variant in `07-TEMPLATE/` following the same pattern. Do not modify the base compressed-mdfinancial prompt to handle multiple document types.

---

## LM Studio Session Rules

Origin: 2026-05-02 thread

- **One document per session.** Do not attach multiple statements in one LM Studio chat — context will truncate early documents silently.
- **Pre-convert large PDFs to plain text** before attaching. PDF-converted token cost is significantly higher than equivalent plain text.
- **Chunk long statements by week or transaction type** if a single statement exceeds ~2,500 tokens of content.
- **LM Studio produces the extract only.** The structured markdown output gets copied into a Perplexity BrainOS session for canonical file updates — LM Studio does not update vault files directly.
- **Document type → prompt variant mapping:**

| Document Type | Prompt to Use | Notes |
|---|---|---|
| Bank statements (SoFi, checking, savings) | `compressed-mdfinancial.md` | Full coverage |
| Debt statements (credit card, loan) | `compressed-mddebt.md` (create when needed) | Needs APR, minimum due, payoff amount fields |
| Pay stubs | `compressed-mdpaystub.md` (create when needed) | Needs gross/net/YTD, deductions |
| Receipts | `compressed-mdfinancial.md` | Only Section 4 (variable spending) will populate |
| Robinhood / investment statements | `compressed-mdinvest.md` (create when needed) | Entirely different schema — do not use bank prompt |

---

## File Write Rules

### MCP Tool File Size Ceiling
- The `create_or_update_file` MCP tool has a practical content payload ceiling of approximately **8KB**.
- Files larger than 8KB require either a targeted patch (replacing a specific section only) or a locally-run script.
- If an update would exceed this ceiling, flag it and propose a local script approach instead.
- **Never attempt to AI-rewrite MASTER-INDEX.csv or any large generated file.** (Origin: BE-20260430)

### CSV Generation Rule
- `MASTER-INDEX.csv` is a **generated output**, not a manually maintained document.
- The correct write path is: run `utils/rebuild_index.py` locally → commit the output.
- AI must never rewrite the CSV directly, append rows manually, or attempt to reconstruct it from memory.
- If the CSV is out of date, the correct response is: "Run `utils/rebuild_index.py` from the vault root." (Origin: BE-20260430)

### Path Verification Rule
- Before referencing, writing to, or recommending any file path, verify the actual vault folder structure using the GitHub MCP tool.
- Do not assume folders exist based on naming patterns or prior context.
- If a folder or script is not confirmed in the repo, do not reference it.
- Confirmed script locations are documented in BRAINOS-SYSTEM.md under Automation Scripts. (Origin: BE-20260430 — AI fabricated `06-SCRIPTS/` folder)

### Shell Script on Windows
- Never write shell scripts via PowerShell `Out-File -Encoding utf8` — it writes a UTF-8 BOM that breaks shebangs in Git Bash.
- Use `[System.IO.File]::WriteAllText()` instead for any shell script written on Windows. (Origin: BE-20260430)

---

## Fabrication Prevention

- Three Google Drive documents contain AI-invented figures and must never be used as sources:
  - Master Context v3
  - Cash Flow v3
  - Command Hub v3
- Employer is **GoodLife Innovations** — not GoodLife Fitness. Fully resolved; flag immediately if the error recurs. (Origin: BrainEntry-early-threads)
- iPad model was incorrectly recorded as "5th gen (2017)" in early threads. Confirmed correct: **iPad Air 5th generation**. (Origin: BE-20260430)
- Folder `06-SCRIPTS/` does not exist. Scripts live at vault root or in `utils/`. (Origin: BE-20260430)

---

## ADHD Execution Rules

- Front-load the most important information in every response.
- Keep next actions small, concrete, and single-step.
- Flag explicitly when the next step is execution, not more planning.
- Call out novelty loops directly: "This looks like a novelty loop — [specific description]. Want to park it and finish what you started?"
- Do not name ADHD constantly — build structure around it instead.
- Re-entry cost reduction is a first-class design goal. Every session should be reloadable in under 5 minutes.

---

## GLWC / GoodLife Two-Hat Rule

- Brayden's DSP role (NLRA-protected employee) and PFT co-provider role (contractor, lease directly tied to the PFT contract) are legally distinct and must never be conflated.
- GLWC strategy is deliberately paced. Flag legal risk explicitly.
- Note when something needs real legal or organizing advice, not AI speculation.

---

## Credentials & Security

- No PATs, passwords, or API keys in chat. Ever.
- GitHub PAT for iPhone expires **May 22, 2026** — renew before that date.
- Store credentials in Windows Credential Manager only.
- No paid AI subscriptions active beyond Perplexity (as of 2026-04-30).

---

## Browser Automation Guardrails

Origin: BE-20260301 (Shopify era), still canonical.

1. Always duplicate theme before editing code
2. Never delete core Liquid files without explicit approval
3. Stop-and-ask on any ambiguous edit

---

## Rule Origin Index

| Rule | Origin Entry |
|---|---|
| AI writes structure / Brayden fills numbers | BrainEntry006 |
| Fabrication prevention / three bad Drive docs | BrainEntry006 |
| Browser automation guardrails | BE-20260301 |
| Employer = GoodLife Innovations | BrainEntry-early |
| MCP file size ceiling (~8KB) | BE-20260430 |
| CSV as generated output / never AI-rewritten | BE-20260430 |
| Path verification before any file write | BE-20260430 |
| PowerShell BOM / WriteAllText rule | BE-20260430 |
| iPad Air 5th gen correction | BE-20260430 |
| System prompt ≤500 tokens / behavioral only | 2026-05-02 laptop-optimization thread |
| Tiered token budget (Tier 1/2/3) | 2026-05-02 laptop-optimization thread |
| Compressed prompt as LM Studio standard | 2026-05-02 laptop-optimization thread |
| One document per LM Studio session | 2026-05-02 laptop-optimization thread |
| LM Studio extracts only / Perplexity updates vault | 2026-05-02 laptop-optimization thread |
| Document type → compressed prompt variant mapping | 2026-05-02 laptop-optimization thread |
