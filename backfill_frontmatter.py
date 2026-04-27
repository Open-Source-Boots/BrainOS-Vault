import csv
import os
import re
import yaml
from datetime import datetime

VAULT_ROOT = os.path.dirname(os.path.abspath(__file__))
BRAIN_ENTRIES_FOLDER = "02-BRAIN-ENTRIES"
CSV_PATH = os.path.join(VAULT_ROOT, "05-INDEX", "MASTER-INDEX.csv")
LOG_PATH = os.path.join(VAULT_ROOT, "05-INDEX", "backfill_frontmatter_log.txt")

def load_csv(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def find_file(filename, folder):
    target = os.path.join(VAULT_ROOT, folder, filename)
    if os.path.exists(target):
        return target
    for root, dirs, files in os.walk(os.path.join(VAULT_ROOT, folder)):
        if filename in files:
            return os.path.join(root, filename)
    return None

def extract_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    rest = content[3:]
    close = rest.find("\n---")
    if close == -1:
        return {}, content
    fm_text = rest[:close]
    body = rest[close + 4:].strip()
    try:
        fm = yaml.safe_load(fm_text) or {}
    except:
        fm = {}
    return fm, body

def build_frontmatter(fm_dict):
    lines = ["---"]
    field_order = [
        "title", "filename", "thread_date", "domain", "slug",
        "status", "priority", "compilation_status",
        "supersedes", "superseded_by", "canonical_file",
        "generated_by_skill", "skill_version",
        "tags", "open_questions"
    ]
    written = set()
    for key in field_order:
        if key in fm_dict:
            val = fm_dict[key]
            if isinstance(val, list):
                if key == "open_questions" and val:
                    lines.append("open_questions:")
                    for oq in val:
                        if isinstance(oq, dict):
                            lines.append(f"  - id: {oq.get('id','')}")
                            lines.append(f"    question: \"{oq.get('question','')}\"")
                            lines.append(f"    canonical_target: {oq.get('canonical_target','')}")
                            lines.append(f"    status: {oq.get('status','OPEN')}")
                elif key == "tags":
                    lines.append(f"tags: {val}")
                else:
                    lines.append(f"{key}: []")
            elif val is None or val == "":
                lines.append(f"{key}:")
            else:
                if isinstance(val, str) and any(c in val for c in [':', '#', '[', ']', '{']):
                    lines.append(f'{key}: "{val}"')
                else:
                    lines.append(f"{key}: {val}")
            written.add(key)
    for key, val in fm_dict.items():
        if key not in written:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)

def main():
    rows = load_csv(CSV_PATH)
    modified = []
    skipped = []
    not_found = []

    for row in rows:
        filename = row.get("filename", "").strip()
        if not filename or not filename.endswith(".md"):
            continue

        filepath = find_file(filename, BRAIN_ENTRIES_FOLDER)
        if not filepath:
            not_found.append(f"NOT FOUND: {filename}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm, body = extract_frontmatter(content)

        csv_fields = {
            "thread_date": (row.get("thread_date") or "").strip(),
            "domain": (row.get("domain") or "").strip(),
            "status": (row.get("status") or "draft").strip(),
            "priority": (row.get("priority") or "").strip(),
            "canonical_file": (row.get("canonical_file") or "").strip(),
            "notes": (row.get("notes") or "").strip(),
        }
        changed = False
        for field, csv_val in csv_fields.items():
            if csv_val and not fm.get(field):
                fm[field] = csv_val
                changed = True

        defaults = {
            "filename": filename,
            "compilation_status": fm.get("compilation_status", "pending"),
            "supersedes": fm.get("supersedes", "none"),
            "superseded_by": fm.get("superseded_by", "none"),
            "generated_by_skill": fm.get("generated_by_skill", "manual"),
            "tags": fm.get("tags", []),
        }
        for field, default_val in defaults.items():
            if field not in fm:
                fm[field] = default_val
                changed = True

        if not changed:
            skipped.append(f"SKIP (already complete): {filename}")
            continue

        new_content = build_frontmatter(fm) + "\n" + body

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        modified.append(f"MODIFIED: {filename}")

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write("=== BACKFILL FRONTMATTER LOG ===\n")
        f.write(f"Run at: {datetime.now()}\n\n")
        f.write(f"--- MODIFIED ({len(modified)}) ---\n")
        f.write("\n".join(modified) + "\n\n")
        f.write(f"--- SKIPPED ({len(skipped)}) ---\n")
        f.write("\n".join(skipped) + "\n\n")
        f.write(f"--- NOT FOUND ({len(not_found)}) ---\n")
        f.write("\n".join(not_found) + "\n")

    print(f"Done. Modified: {len(modified)} | Skipped: {len(skipped)} | Not found: {len(not_found)}")
    print(f"Log: {LOG_PATH}")

if __name__ == "__main__":
    main()
