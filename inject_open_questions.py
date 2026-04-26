import csv
import os
import re
from datetime import datetime

VAULT_ROOT = "C:/Users/brayd/Desktop/Open-Source AI/BrainOS Vault"
BRAIN_ENTRIES_FOLDER = "02-BRAIN-ENTRIES"
CSV_PATH = "05-INDEX/MASTER-INDEX.csv"
LOG_PATH = "05-INDEX/inject_open_questions_log.txt"

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
    # also search recursively in case subfolder exists
    for root, dirs, files in os.walk(os.path.join(VAULT_ROOT, folder)):
        if filename in files:
            return os.path.join(root, filename)
    return None

def already_has_open_questions(content):
    return "open_questions:" in content

def extract_date_from_filename(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return match.group(1)
    return datetime.now().strftime("%Y%m%d")

def build_oq_block(filename, action_required):
    date_str = extract_date_from_filename(filename)
    canonical = "BRAINOS-SYSTEM.md"  # default fallback
    
    # Simple domain-to-canonical mapping
    fname_lower = filename.lower()
    if "goodlife" in fname_lower or "glwc" in fname_lower or "union" in fname_lower:
        canonical = "GOODLIFE-UNION.md"
    elif "financial" in fname_lower or "cashflow" in fname_lower or "debt" in fname_lower:
        canonical = "FINANCIAL-SNAPSHOT.md"
    elif "peaslee" in fname_lower or "skill" in fname_lower or "education" in fname_lower:
        canonical = "SKILLS-EDUCATION.md"
    elif "device" in fname_lower or "stack" in fname_lower or "ai" in fname_lower:
        canonical = "DEVICE-ECOSYSTEM.md"
    elif "identity" in fname_lower or "brayden" in fname_lower:
        canonical = "BRAYDEN-IDENTITY.md"
    elif "project" in fname_lower or "ctrlplusyou" in fname_lower or "kray" in fname_lower:
        canonical = "ACTIVE-PROJECTS.md"

    # Split action_required on semicolons or newlines into multiple questions
    raw_questions = re.split(r'[;\n]+', action_required)
    questions = [q.strip() for q in raw_questions if q.strip() and len(q.strip()) > 10]

    if not questions:
        return None

    lines = ["open_questions:"]
    for i, q in enumerate(questions, 1):
        q_clean = q.replace('"', "'")
        lines.append(f'  - id: OQ-{date_str}-{i:03d}')
        lines.append(f'    question: "{q_clean}"')
        lines.append(f'    canonical_target: {canonical}')
        lines.append(f'    status: OPEN')

    return "\n".join(lines)

def inject_into_frontmatter(content, oq_block):
    # Find the closing --- of frontmatter
    lines = content.split("\n")
    if lines[0].strip() != "---":
        # No frontmatter at all — wrap content with new frontmatter
        new_fm = f"---\n{oq_block}\n---\n"
        return new_fm + content

    # Find second --- 
    close_index = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            close_index = i
            break

    if close_index is None:
        return content  # malformed frontmatter, skip

    # Insert oq_block before closing ---
    lines.insert(close_index, oq_block)
    return "\n".join(lines)

def main():
    rows = load_csv(CSV_PATH)
    log = []
    skipped = []
    modified = []
    not_found = []

    for row in rows:
        filename = row.get("filename", "").strip()
        action_required = row.get("action_required", "").strip()

        if not filename or not filename.endswith(".md"):
            continue
        if not action_required or action_required.lower() in ["none", "n/a", ""]:
            skipped.append(f"SKIP (no action): {filename}")
            continue

        filepath = find_file(filename, BRAIN_ENTRIES_FOLDER)
        if not filepath:
            not_found.append(f"NOT FOUND: {filename}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if already_has_open_questions(content):
            skipped.append(f"SKIP (already has open_questions): {filename}")
            continue

        oq_block = build_oq_block(filename, action_required)
        if not oq_block:
            skipped.append(f"SKIP (questions too short to parse): {filename}")
            continue

        new_content = inject_into_frontmatter(content, oq_block)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        modified.append(f"MODIFIED: {filename}")

    # Write log
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write("=== INJECT OPEN QUESTIONS LOG ===\n")
        f.write(f"Run at: {datetime.now()}\n\n")
        f.write(f"--- MODIFIED ({len(modified)}) ---\n")
        f.write("\n".join(modified) + "\n\n")
        f.write(f"--- SKIPPED ({len(skipped)}) ---\n")
        f.write("\n".join(skipped) + "\n\n")
        f.write(f"--- NOT FOUND ({len(not_found)}) ---\n")
        f.write("\n".join(not_found) + "\n")

    print(f"Done. Modified: {len(modified)} | Skipped: {len(skipped)} | Not found: {len(not_found)}")
    print(f"Full log written to: {LOG_PATH}")

if __name__ == "__main__":
    main()