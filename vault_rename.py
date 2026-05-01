"""vault_rename.py — BrainOS vault-wide naming convention enforcer

Convention:
  Dated files:     YYYYMMDD-DOMAIN-descriptor.md   (Brain Entries, Dailies)
  Monthly files:   YYYYMM-DOMAIN-descriptor.md     (Finance extracts)
  Canonical files: DOMAIN-DESCRIPTOR.md            (no date prefix — unchanged)

Usage:
  python vault_rename.py --dry-run     # preview all renames, no changes made
  python vault_rename.py --apply       # apply renames and print git mv commands
  python vault_rename.py --git         # apply renames AND run git mv
"""

import re
import sys
import subprocess
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.resolve()

# Folders to process (canonical files in 04-CANONICAL are skipped by rule below)
FOLDERS = [
    '00-INBOX',
    '01-DAILY',
    '02-BRAIN-ENTRIES',
    '03-PROJECTS',
    '06-ANSWERS',
]

# Files that must never be renamed
CANONICAL_PROTECTED = {
    'FINANCIAL-SNAPSHOT.md', 'BRAINOS-SYSTEM.md', 'BRAYDEN-IDENTITY.md',
    'ACTIVE-PROJECTS.md', 'SKILLS-EDUCATION.md', 'DEVICE-ECOSYSTEM.md',
    'AI-WORKFLOW-RULES.md', 'OPEN-QUESTIONS.md', 'BRAINOS-CHECKPOINT-LOG.md',
    'MASTER-INDEX.md', 'MASTER-INDEX.csv', 'README.md',
}

# ── Rename rules (applied in order, first match wins) ────────────────────────

def desired_name(filename):
    """Return the desired filename string, or None if no change needed."""
    stem = filename.replace('.md', '')

    # Already correct: starts with 6-8 digit date prefix
    if re.match(r'^\d{6,8}-', filename):
        # Normalise: ensure domain is uppercase, descriptor is lowercase
        parts = filename.replace('.md', '').split('-', 2)
        if len(parts) >= 2:
            normalised = parts[0] + '-' + parts[1].upper() + ('-' + parts[2].lower() if len(parts) > 2 else '') + '.md'
            return normalised if normalised != filename else None
        return None

    # BE-YYYYMMDD-domain-descriptor → YYYYMMDD-BE-domain-descriptor
    m = re.match(r'^BE-(\d{8})-(.+)\.md$', filename, re.IGNORECASE)
    if m:
        return f"{m.group(1)}-BE-{m.group(2).lower()}.md"

    # FINANCE-EXTRACT-SOFI-YYYYMM → YYYYMM-FINANCE-sofi-extract
    m = re.match(r'^FINANCE-EXTRACT-SOFI-(\d{6})\.md$', filename, re.IGNORECASE)
    if m:
        return f"{m.group(1)}-FINANCE-sofi-extract.md"

    # FINANCE-EXTRACT-SOFI-Month YY (old space-based names)
    m = re.match(r'^FINANCE-EXTRACT-SOFI-(.+)\.md$', filename, re.IGNORECASE)
    if m:
        raw = m.group(1).strip()
        from datetime import datetime
        for fmt in ('%B %y', '%b %y', '%B-%y', '%b-%y', '%B %Y', '%b %Y'):
            try:
                slug = datetime.strptime(raw, fmt).strftime('%Y%m')
                return f"{slug}-FINANCE-sofi-extract.md"
            except ValueError:
                continue
        return f"000000-FINANCE-sofi-extract-{raw.lower().replace(' ', '-')}.md"

    # Daily notes: YYYY-MM-DD → YYYYMMDD-DAILY
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})\.md$', filename)
    if m:
        return f"{m.group(1)}{m.group(2)}{m.group(3)}-DAILY.md"

    # No rule matched
    return None


def collect_renames():
    renames = []  # list of (old_path, new_path)
    for folder in FOLDERS:
        folder_path = VAULT_ROOT / folder
        if not folder_path.exists():
            continue
        for f in sorted(folder_path.rglob('*.md')):
            if f.name in CANONICAL_PROTECTED:
                continue
            new_name = desired_name(f.name)
            if new_name and new_name != f.name:
                renames.append((f, f.parent / new_name))
    return renames


def main():
    mode = '--dry-run'
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    renames = collect_renames()

    if not renames:
        print("No renames needed. Vault naming is consistent.")
        return

    print(f"{'DRY RUN — ' if mode == '--dry-run' else ''}Found {len(renames)} files to rename:\n")
    for old, new in renames:
        print(f"  {old.relative_to(VAULT_ROOT)}")
        print(f"    → {new.relative_to(VAULT_ROOT)}")

    if mode == '--dry-run':
        print("\nRun with --apply or --git to execute.")
        return

    print()
    errors = []
    for old, new in renames:
        if new.exists():
            print(f"  SKIP (target exists): {new.name}")
            errors.append(old)
            continue
        if mode == '--git':
            result = subprocess.run(['git', 'mv', str(old), str(new)], cwd=VAULT_ROOT, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"  git mv FAILED: {old.name} → {result.stderr.strip()}")
                errors.append(old)
            else:
                print(f"  git mv: {old.name} → {new.name}")
        else:
            old.rename(new)
            print(f"  Renamed: {old.name} → {new.name}")

    if not errors:
        if mode == '--git':
            print("\nAll renames complete. Run:")
            print('  git commit -m "[SYSTEM] rename: enforce YYYYMM/YYYYMMDD-DOMAIN-descriptor convention"')
            print('  git push origin main')
        else:
            print("\nAll renames complete. Stage with:")
            print('  git add -A')
            print('  git commit -m "[SYSTEM] rename: enforce YYYYMM/YYYYMMDD-DOMAIN-descriptor convention"')
            print('  git push origin main')
    else:
        print(f"\n{len(errors)} file(s) had errors — review above.")


if __name__ == '__main__':
    main()
