"""
utils/vault_health_check.py
-----------------------------
Runs a structural integrity check on the BrainOS vault.
Checks every Brain Entry in 02-BRAIN-ENTRIES/ against
the MASTER-INDEX.csv and reports:

  - Files in 02-BRAIN-ENTRIES/ missing from MASTER-INDEX.csv
  - Entries in MASTER-INDEX.csv with no matching .md file
  - Brain Entries missing required frontmatter fields
  - Brain Entries with malformed or unparseable YAML frontmatter
  - Orphaned open questions (canonical_target points to
    a file that does not exist in 04-CANONICAL/)

Problem it solves:
As the vault grows, drift accumulates silently — files get
created outside the index, CSV rows go stale, and frontmatter
gets partially written. This script gives you a single command
to surface all of that before it causes real issues.

Usage:
    python utils/vault_health_check.py
"""

import csv
import os
import yaml
from datetime import datetime

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAIN_ENTRIES = os.path.join(VAULT_ROOT, "02-BRAIN-ENTRIES")
CANONICAL_DIR = os.path.join(VAULT_ROOT, "04-CANONICAL")
CSV_PATH = os.path.join(VAULT_ROOT, "05-INDEX", "MASTER-INDEX.csv")
REPORT_PATH = os.path.join(VAULT_ROOT, "05-INDEX", "vault_health_report.txt")

REQUIRED_FIELDS = ["title", "filename", "domain", "status", "canonical_file"]

def load_csv():
    rows = {}
    if not os.path.exists(CSV_PATH):
        return rows
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fname = (row.get("filename") or "").strip()
            if fname:
                rows[fname] = row
    return rows

def get_brain_entry_files():
    files = set()
    for root, dirs, fnames in os.walk(BRAIN_ENTRIES):
        for f in fnames:
            if f.endswith(".md"):
                files.add(f)
    return files

def get_canonical_files():
    if not os.path.exists(CANONICAL_DIR):
        return set()
    return {f for f in os.listdir(CANONICAL_DIR) if f.endswith(".md")}

def parse_frontmatter(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith("---"):
        return None, "NO_FRONTMATTER"
    rest = content[3:]
    close = rest.find("\n---")
    if close == -1:
        return None, "UNCLOSED_FRONTMATTER"
    fm_text = rest[:close]
    try:
        fm = yaml.safe_load(fm_text) or {}
        return fm, None
    except yaml.YAMLError as e:
        return None, f"YAML_ERROR: {e}"

def main():
    csv_rows = load_csv()
    disk_files = get_brain_entry_files()
    canonical_files = get_canonical_files()

    csv_filenames = set(csv_rows.keys())

    unindexed = disk_files - csv_filenames
    stale_csv = csv_filenames - disk_files

    missing_fields = []
    malformed = []
    orphaned_oq = []

    for fname in sorted(disk_files):
        fpath = None
        for root, dirs, files in os.walk(BRAIN_ENTRIES):
            if fname in files:
                fpath = os.path.join(root, fname)
                break
        if not fpath:
            continue
        fm, err = parse_frontmatter(fpath)
        if err:
            malformed.append(f"{fname}: {err}")
            continue
        missing = [field for field in REQUIRED_FIELDS if not fm.get(field)]
        if missing:
            missing_fields.append(f"{fname}: missing {missing}")
        oqs = fm.get("open_questions", [])
        if isinstance(oqs, list):
            for oq in oqs:
                if not isinstance(oq, dict):
                    continue
                target = oq.get("canonical_target", "")
                if target and target not in canonical_files:
                    orphaned_oq.append(f"{fname} → OQ {oq.get('id','')} targets missing file: {target}")

    lines = [
        "=== BRAINOS VAULT HEALTH CHECK ===",
        f"Run at: {datetime.now()}",
        f"Brain Entries on disk: {len(disk_files)}",
        f"Entries in MASTER-INDEX.csv: {len(csv_filenames)}",
        f"Canonical files in 04-CANONICAL/: {len(canonical_files)}",
        "",
    ]

    def section(title, items):
        lines.append(f"--- {title} ({len(items)}) ---")
        lines.extend(items if items else ["  ✅ None"])
        lines.append("")

    section("UNINDEXED FILES (on disk, not in CSV)", sorted(unindexed))
    section("STALE CSV ROWS (in CSV, file missing)", sorted(stale_csv))
    section("MISSING REQUIRED FRONTMATTER FIELDS", missing_fields)
    section("MALFORMED YAML FRONTMATTER", malformed)
    section("ORPHANED OPEN QUESTIONS (dead canonical_target)", orphaned_oq)

    report = "\n".join(lines)
    print(report)

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report + "\n")

    print(f"\nReport saved to: {REPORT_PATH}")

if __name__ == "__main__":
    main()
