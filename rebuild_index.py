import os
import csv
import yaml

ENTRY_DIRS = ["02-BRAIN-ENTRIES", "03-PROJECTS"]
OUTPUT_CSV = "05-INDEX/MASTER-INDEX.csv"
FIELDS = ["filename", "thread_date", "domain", "status", "priority",
          "key_facts", "canonical_file", "action_required", "last_verified", "notes"]

def read_frontmatter(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    try:
        end = content.index("---", 3)
        return yaml.safe_load(content[3:end]) or {}
    except Exception:
        return {}

rows = []
for folder in ENTRY_DIRS:
    if not os.path.exists(folder):
        continue
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".md") or fname == "BE-TEMPLATE.md":
            continue
        fm = read_frontmatter(os.path.join(folder, fname))
        rows.append({
            "filename": fname,
            "thread_date": fm.get("thread_date", fm.get("date", "")),
            "domain": fm.get("domain", ""),
            "status": fm.get("status", ""),
            "priority": fm.get("priority", ""),
            "key_facts": "",
            "canonical_file": fm.get("canonical_file", fm.get("canonicalfile", "")),
            "action_required": fm.get("action_required", ""),
            "last_verified": fm.get("last_verified", ""),
            "notes": fm.get("notes", ""),
        })

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)

print(f"Rebuilt MASTER-INDEX.csv — {len(rows)} entries")