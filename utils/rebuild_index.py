import os
import csv
import yaml

ENTRY_DIRS = ["02-BRAIN-ENTRIES", "03-PROJECTS", "04-CANONICAL", "06-ANSWERS"]
OUTPUT_CSV = "05-INDEX/MASTER-INDEX.csv"
FIELDS = ["filename", "path", "thread_date", "domain", "status", "priority",
          "key_facts", "canonical_file", "action_required", "last_verified", "notes"]

SKIP_FILES = {"BE-TEMPLATE.md"}
SKIP_DIRS = {"07-TEMPLATE", "08-ATTACH", "99-OUTBOX", "00-INBOX", ".obsidian", ".smart-env", "utils"}

def read_frontmatter(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None  # explicitly None = no frontmatter
    try:
        end = content.index("---", 3)
        return yaml.safe_load(content[3:end]) or {}
    except Exception:
        return {}

rows = []
for folder in ENTRY_DIRS:
    if not os.path.exists(folder):
        continue
    for dirpath, dirnames, filenames in os.walk(folder):
        # Prune skipped directories in-place so os.walk won't descend into them
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            if fname in SKIP_FILES:
                continue
            filepath = os.path.join(dirpath, fname)
            rel_path = filepath.replace("\\", "/")
            fm = read_frontmatter(filepath)

            if fm is None:
                # File exists but has no frontmatter — log as UNPROCESSED
                rows.append({
                    "filename": fname,
                    "path": rel_path,
                    "thread_date": "",
                    "domain": "",
                    "status": "UNPROCESSED",
                    "priority": "",
                    "key_facts": "",
                    "canonical_file": "",
                    "action_required": "Add frontmatter",
                    "last_verified": "",
                    "notes": "No frontmatter detected — file is unprocessed",
                })
            else:
                rows.append({
                    "filename": fname,
                    "path": rel_path,
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

unprocessed = sum(1 for r in rows if r["status"] == "UNPROCESSED")
print(f"Rebuilt MASTER-INDEX.csv — {len(rows)} entries ({unprocessed} UNPROCESSED)")
