"""vault_rename.py — BrainOS vault-wide naming convention enforcer

Convention:
  Dated files:     YYYYMMDD-DOMAIN-slug-TYPE.md    (Brain Entries, logs, answers, refs)
  Monthly files:   YYYYMM-DOMAIN-slug-TYPE.md      (Finance extracts, monthly reviews)
  Daily notes:     YYYYMMDD-DAILY.md               (no slug, no type tag needed)
  Canonical files: DOMAIN-DESCRIPTOR.md            (no date, no type — never renamed)

Approved TYPE tags (tail only, always uppercase):
  -BE      Brain Entry
  -DAILY   Daily note
  -STMT    Financial statement extract
  -ANS     Answer file (closed open questions)
  -LOG     Freeform log or event record
  -REF     Reference / research harvest
  -PLAN    Planning document or project stub
  -LEGAL   Legal or compliance document

Skipped automatically:
  - Files in 04-CANONICAL (protected by name list)
  - *.sync-conflict-* files (require manual resolution pass)
  - BEUNASSIGNED* files (flagged for manual review — no reliable date)
  - Files whose names already match the convention

Usage:
  python vault_rename.py --dry-run     # preview all renames, no changes made
  python vault_rename.py --apply       # apply renames (filesystem only, no git)
  python vault_rename.py --git         # apply renames AND run git mv
"""

import re
import sys
import subprocess
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.resolve()

# Folders to process
FOLDERS = [
    '00-INBOX',
    '01-DAILY',
    '02-BRAIN-ENTRIES',
    '03-PROJECTS',
    '06-ANSWERS',
]

# Canonical files — never renamed, never touched
CANONICAL_PROTECTED = {
    'FINANCIAL-SNAPSHOT.md', 'BRAINOS-SYSTEM.md', 'BRAYDEN-IDENTITY.md',
    'ACTIVE-PROJECTS.md', 'SKILLS-EDUCATION.md', 'DEVICE-ECOSYSTEM.md',
    'AI-WORKFLOW-RULES.md', 'OPEN-QUESTIONS.md', 'BRAINOS-CHECKPOINT-LOG.md',
    'MASTER-INDEX.md', 'MASTER-INDEX.csv', 'README.md', 'NAMING-CONVENTION.md',
    'WORKFLOW-LOG.md', 'SESSION-CONTEXT.md',
}

# Approved TYPE tags
VALID_TYPES = {'BE', 'DAILY', 'STMT', 'ANS', 'LOG', 'REF', 'PLAN', 'LEGAL'}


def already_valid(filename):
    """Return True if the filename already matches the convention."""
    # YYYYMMDD-DOMAIN-slug-TYPE.md
    if re.match(r'^\d{8}-[A-Z]+-[a-z0-9][a-z0-9\-]*-[A-Z]+\.md$', filename):
        # Confirm TYPE is from approved vocab
        parts = filename.replace('.md', '').split('-')
        return parts[-1] in VALID_TYPES
    # YYYYMM-DOMAIN-slug-TYPE.md
    if re.match(r'^\d{6}-[A-Z]+-[a-z0-9][a-z0-9\-]*-[A-Z]+\.md$', filename):
        parts = filename.replace('.md', '').split('-')
        return parts[-1] in VALID_TYPES
    # YYYYMMDD-DAILY.md (no slug or type needed)
    if re.match(r'^\d{8}-DAILY\.md$', filename):
        return True
    return False


def desired_name(filename):
    """
    Return the desired filename string, or None if no change needed.
    Returns 'SKIP:reason' string for files that need manual handling.
    """

    # Never touch canonical protected files
    if filename in CANONICAL_PROTECTED:
        return None

    # Skip sync-conflict files entirely
    if '.sync-conflict-' in filename:
        return 'SKIP:sync-conflict — resolve manually before rename pass'

    # Flag BEUNASSIGNED files for manual review
    if filename.upper().startswith('BEUNASSIGNED') or 'BEUNASSIGNED' in filename.upper():
        return 'SKIP:BEUNASSIGNED — no reliable date, needs manual review'

    # Already valid — no change needed
    if already_valid(filename):
        return None

    stem = filename[:-3]  # strip .md

    # ── Pattern: BE-YYYYMMDD-DOMAIN-slug.md → YYYYMMDD-DOMAIN-slug-BE.md ──
    m = re.match(r'^BE-(\d{8})-([A-Za-z0-9]+)-(.+)$', stem, re.IGNORECASE)
    if m:
        date, domain, slug = m.group(1), m.group(2).upper(), m.group(3).lower()
        return f"{date}-{domain}-{slug}-BE.md"

    # ── Pattern: BE-YYYYMMDD-slug.md (no domain) → YYYYMMDD-BRAINOS-slug-BE.md ──
    m = re.match(r'^BE-(\d{8})-(.+)$', stem, re.IGNORECASE)
    if m:
        date, slug = m.group(1), m.group(2).lower()
        return f"{date}-BRAINOS-{slug}-BE.md"

    # ── Pattern: YYYYMMDD-DOMAIN-slug-BE.md (BE already at tail, domain needs uppercase) ──
    m = re.match(r'^(\d{8})-([A-Za-z0-9]+)-(.+)-BE$', stem)
    if m:
        date, domain, slug = m.group(1), m.group(2).upper(), m.group(3).lower()
        return f"{date}-{domain}-{slug}-BE.md"

    # ── Pattern: YYYYMMDD-DOMAIN-slug.md (no type tag — infer from folder or flag) ──
    m = re.match(r'^(\d{8})-([A-Za-z0-9]+)-(.+)$', stem)
    if m:
        date, domain, slug = m.group(1), m.group(2).upper(), m.group(3).lower()
        # If domain is DAILY, treat as daily note
        if domain == 'DAILY':
            return f"{date}-DAILY.md"
        # Can't safely infer type — flag for manual review
        return f"SKIP:no TYPE tag — needs manual assignment for {filename}"

    # ── Pattern: YYYY-MM-DD.md daily note ──
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', stem)
    if m:
        return f"{m.group(1)}{m.group(2)}{m.group(3)}-DAILY.md"

    # ── Pattern: YYYYMMDD.md bare date daily note ──
    m = re.match(r'^(\d{8})$', stem)
    if m:
        return f"{m.group(1)}-DAILY.md"

    # ── Pattern: YYYYMM-DOMAIN-slug-STMT or finance extract ──
    m = re.match(r'^(\d{6})-([A-Za-z0-9]+)-(.+)$', stem)
    if m:
        date, domain, slug = m.group(1), m.group(2).upper(), m.group(3).lower()
        # Already has a valid type tail
        parts = slug.split('-')
        if parts[-1].upper() in VALID_TYPES:
            return f"{date}-{domain}-{'-'.join(parts[:-1])}-{parts[-1].upper()}.md"
        return f"SKIP:no TYPE tag — needs manual assignment for {filename}"

    # No rule matched
    return f"SKIP:unrecognised pattern — needs manual review for {filename}"


def collect_renames():
    renames = []    # (old_path, new_path)
    skipped = []    # (old_path, reason)

    for folder in FOLDERS:
        folder_path = VAULT_ROOT / folder
        if not folder_path.exists():
            continue
        for f in sorted(folder_path.rglob('*.md')):
            if f.name in CANONICAL_PROTECTED:
                continue
            result = desired_name(f.name)
            if result is None:
                continue  # already valid, no action
            if isinstance(result, str) and result.startswith('SKIP:'):
                skipped.append((f, result[5:]))
            else:
                new_path = f.parent / result
                renames.append((f, new_path))

    return renames, skipped


def main():
    mode = '--dry-run'
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    renames, skipped = collect_renames()

    # ── Report skipped files ──────────────────────────────────────────────────
    if skipped:
        print(f"\n{'─'*60}")
        print(f"MANUAL REVIEW NEEDED — {len(skipped)} file(s) skipped:\n")
        for path, reason in skipped:
            print(f"  {path.relative_to(VAULT_ROOT)}")
            print(f"    ↳ {reason}")
        print(f"{'─'*60}\n")

    # ── Report renames ────────────────────────────────────────────────────────
    if not renames:
        print("No renames needed. All eligible files match the convention.")
        if skipped:
            print("(Skipped files listed above require manual handling.)")
        return

    label = 'DRY RUN — ' if mode == '--dry-run' else ''
    print(f"{label}Found {len(renames)} file(s) to rename:\n")
    for old, new in renames:
        print(f"  {old.relative_to(VAULT_ROOT)}")
        print(f"    → {new.relative_to(VAULT_ROOT)}\n")

    if mode == '--dry-run':
        print("Run with --apply or --git to execute.")
        return

    # ── Execute renames ───────────────────────────────────────────────────────
    errors = []
    for old, new in renames:
        if new.exists():
            print(f"  SKIP (target exists): {new.name}")
            errors.append(old)
            continue
        if mode == '--git':
            result = subprocess.run(
                ['git', 'mv', str(old), str(new)],
                cwd=VAULT_ROOT, capture_output=True, text=True
            )
            if result.returncode != 0:
                print(f"  git mv FAILED: {old.name} → {result.stderr.strip()}")
                errors.append(old)
            else:
                print(f"  git mv: {old.name} → {new.name}")
        else:  # --apply
            old.rename(new)
            print(f"  Renamed: {old.name} → {new.name}")

    print()
    if not errors:
        if mode == '--git':
            print("All renames complete. Commit with:")
            print('  git commit -m "[SYSTEM] rename: enforce YYYYMMDD-DOMAIN-slug-TYPE convention"')
            print('  git push origin main')
        else:
            print("All renames complete. Stage and commit with:")
            print('  git add -A')
            print('  git commit -m "[SYSTEM] rename: enforce YYYYMMDD-DOMAIN-slug-TYPE convention"')
            print('  git push origin main')
    else:
        print(f"{len(errors)} file(s) had errors — review above before committing.")


if __name__ == '__main__':
    main()
