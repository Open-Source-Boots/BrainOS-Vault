---
title: AI Workflow Rules
filename: AI-WORKFLOW-RULES.md
updated: 2026-04-30
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
