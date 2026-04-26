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
    for root, dirs, files in os.walk(os.path.join(VAULT_ROOT, folder)):
        if filename in files:
            return os.path.join(root, filename)
    return None

def extract_date_from_filename(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return match.group(1)
    return datetime.now().strftime("%Y%m%d")

def get_canonical_target(filename):
    fname_lower = filename.lower()
    if "goodlife" in fname_lower or "glwc" in fname_lower or "union" in fname_lower:
        return "GOODLIFE-UNION.md"
    elif "financial" in fname_lower or "cashflow" in fname_lower or "debt" in fname_lower:
        return "FINANCIAL-SNAPSHOT.md"
    elif "peaslee" in fname_lower or "skill" in fname_lower or "education" in fname_lower:
        return "SKILLS-EDUCATION.md"
    elif "device" in fname_lower or "stack" in fname_lower:
        return "DEVICE-ECOSYSTEM.md"
    elif "identity" in fname_lower or "brayden" in fname_lower:
        return "BRAYDEN-IDENTITY.md"
    elif "project" in fname_lower or "ctrlplusyou" in fname_lower or "kray" in fname_lower:
        return "ACTIVE-PROJECTS.md"
    return "BRAINOS-SYSTEM.md"

def build_clean_oq_block(filename, action_required):
    date_str = extract_date_from_filename(filename)
    canonical = get_canonical_target(filename)
    raw_questions = re.split(r'[;\n]+', action_required)
    questions = [q.strip() for q in raw_questions if q.strip() and len(q.strip()) > 10]
    if not questions:
        return None
    lines = ["open_questions:"]
    for i, q in enumerate(questions, 1):
        q_clean = q.replace('"', "'").replace('\\', '')
        lines.append(f'  - id: OQ-{date_str}-{i:03d}')
        lines.append(f'    question: "{q_clean}"')
        lines.append(f'    canonical_target: {canonical}')
        lines.append(f'    status: OPEN')
    return "\n".join(lines)

def strip_all_frontmatter(content):
    """Remove entire existing frontmatter block and return clean body."""
    content = content.strip()
    if not content.startswith("---"):
        return content
    # Find closing ---
    rest = content[3:]  # skip opening ---
    close_pos = rest.find("\n---")
    if close_pos == -1:
        return content  # malformed, return as-is
    body = rest[close_pos + 4:].strip()  # skip past closing ---
    return body

def build_full_file(body, oq_block, existing_meta):
    """Wrap body with clean frontmatter containing OQ block plus preserved metadata."""
    fm = "---\n"
    if existing_meta:
        fm += existing_meta.strip() + "\n"
    fm += oq_block + "\n"
    fm += "---\n"
    return fm + body

def extract_existing_meta(content):
    """Pull out existing frontmatter fields except open_questions."""
    content = content.strip()
    if not content.startswith("---"):
        return ""
    rest = content[3:]
    close_pos = rest.find("\n---")
    if close_pos == -1:
        return ""
    fm_block = rest[:close_pos].strip()
    # Remove any existing open_questions lines
    lines = fm_block.split("\n")
    clean_lines = []
    in_oq = False
    for line in lines:
        if line.strip().startswith("open_questions:"):
            in_oq = True
            continue
        if in_oq:
            if line and not line.startswith(" "):
                in_oq = False
                clean_lines.append(line)
            continue
        clean_lines.append(line)
    result = "\n".join(clean_lines).strip()
    return result + "\n" if result else ""

def main():
    rows = load_csv(CSV_PATH)
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

        oq_block = build_clean_oq_block(filename, action_required)
        if not oq_block:
            skipped.append(f"SKIP (questions too short): {filename}")
            continue

        existing_meta = extract_existing_meta(content)
        body = strip_all_frontmatter(content)
        new_content = build_full_file(body, oq_block, existing_meta)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        modified.append(f"MODIFIED: {filename}")

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write("=== INJECT OPEN QUESTIONS LOG (FULL REWRITE) ===\n")
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