# BrainOS Utility Scripts

All scripts in `utils/` are read-only diagnostic tools.
They never modify vault files — they only read and report.
Run them from the vault root:

```bash
python utils/vault_health_check.py
python utils/log_dedup.py
```

Root-level scripts modify vault files and should be run intentionally:

| Script | What it does | Modifies files? |
|---|---|---|
| `backfill_frontmatter.py` | Fills missing frontmatter fields in Brain Entries from MASTER-INDEX.csv | ✅ Yes |
| `inject_open_questions.py` | Rewrites open_questions blocks in Brain Entry frontmatter from CSV `action_required` column | ✅ Yes |
| `review_questions.py` | Interactive CLI to answer/skip/close open questions (excludes Financial) | ✅ Yes |
| `review_financial_questions.py` | Interactive CLI for FINANCIAL-SNAPSHOT.md questions only | ⚠️ Inactive until activated |
| `utils/vault_health_check.py` | Structural integrity check — files vs CSV vs frontmatter vs orphaned OQs | ❌ Read-only |
| `utils/log_dedup.py` | Scans answer logs for duplicate OQ IDs | ❌ Read-only |

## Recommended Run Order (after a big session)

1. `python utils/vault_health_check.py` — confirm no drift before touching anything
2. `python backfill_frontmatter.py` — fill gaps from CSV
3. `python inject_open_questions.py` — sync open questions from CSV
4. `python review_questions.py` — work through the question queue
5. `python utils/log_dedup.py` — verify no duplicate OQ IDs crept in

## Activation Gate

`review_financial_questions.py` will print a clear status message
if run before FINANCIAL-SNAPSHOT.md is ready. Set
`SCHEDULED_ACTIVATION = True` inside that file when:
- Real verified numbers exist in FINANCIAL-SNAPSHOT.md
- A transaction input pipeline is in place
- $100k/year and debt payoff milestones are defined

## Notes on .stfolder and Syncthing Artifacts

`.stfolder` and `.stfolder.removed-*` directories **must not be
deleted from the local filesystem**. They are Syncthing's internal
folder markers. Deleting them locally will cause Syncthing to
treat the folder as uninitialized and may trigger conflict storms
across Desktop, Laptop, iPhone, and iPad.

They are excluded from Git via `.gitignore`. Leave them on disk.
