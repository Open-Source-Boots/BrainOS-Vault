"""
utils/log_dedup.py
-------------------
Scans BrainOS answer log files in 06-ANSWERS/ for duplicate
question IDs (same OQ-YYYYMMDD-NNN logged more than once)
and reports them. Does NOT auto-delete — outputs a report
for manual review.

Problem it solves:
If inject_open_questions.py is re-run, it rewrites OQ IDs
with a new date stamp, which can cause the same conceptual
question to accumulate multiple log entries across sessions.
This script surfaces that drift before it corrupts canonical files.

Usage:
    python utils/log_dedup.py
"""

import os
import re
from collections import defaultdict
from datetime import datetime

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANSWERS_FOLDER = os.path.join(VAULT_ROOT, "06-ANSWERS")
REPORT_PATH = os.path.join(VAULT_ROOT, "05-INDEX", "log_dedup_report.txt")

def scan_logs():
    findings = defaultdict(list)
    for root, dirs, files in os.walk(ANSWERS_FOLDER):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'##\s+(OQ-\d{8}-\d{3})', content)
            for oq_id in matches:
                findings[oq_id].append(fpath)
    return findings

def main():
    findings = scan_logs()
    duplicates = {k: v for k, v in findings.items() if len(v) > 1}
    total_scanned = len(findings)
    total_dupes = len(duplicates)

    lines = [
        "=== BRAINOS LOG DEDUP REPORT ===",
        f"Run at: {datetime.now()}",
        f"Total unique OQ IDs found: {total_scanned}",
        f"Duplicate IDs: {total_dupes}",
        "",
    ]

    if not duplicates:
        lines.append("✅ No duplicate question IDs found. Logs are clean.")
    else:
        lines.append("--- DUPLICATES ---")
        for oq_id, paths in sorted(duplicates.items()):
            lines.append(f"\n{oq_id} ({len(paths)} occurrences):")
            for p in paths:
                lines.append(f"  - {p}")

    report = "\n".join(lines)
    print(report)

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report + "\n")

    print(f"\nReport saved to: {REPORT_PATH}")

if __name__ == "__main__":
    main()
