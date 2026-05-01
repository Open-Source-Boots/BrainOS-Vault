import pdfplumber
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime


# ── Patterns ────────────────────────────────────────────────────────────────

acct_header = re.compile(r'^(Checking Account|Savings Account)\s*[-–]\s*(\d+)$')

balance_labels = re.compile(
    r'^(Current Balance|Beginning Balance|Current Interest Rate'
    r'|Monthly Interest Paid|Annual Percentage Yield|Year-to-date Interest Paid)',
    re.IGNORECASE
)

txn_row = re.compile(
    r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}'
)

period_pattern = re.compile(
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}'
    r'\s*[-–]\s*'
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+(\d{4})'
)

skip_patterns = re.compile(
    r'(SoFi checking|SoFi Bank|Member FDIC|Page \d+ of|Important Information|'
    r'Insured Deposit|FDIC insurance|Payable on Death|Participating banks|'
    r'Deposit Agreement|Questions About|Reporting Other|Interest/Dividends|'
    r'How to Contact|Contact Information|Mailing Address|Transaction ID:|'
    r'Transaction Details|Balances below|Current balances include|'
    r'2021 SoFi|SoFi Technologies|Annual Percentage Yield Earned|'
    r'accrues daily|Customer Agreement|rate sheet|Travel Vault|'
    r'Primary Account Holder|Member since|Account Number|Monthly Statement Period|'
    r'Website|www\.so|855|Cottonwood|Utah|'
    r'DATE\s+TYPE\s+DESCRIPTION)',  # skip repeat table headers on continuation pages
    re.IGNORECASE
)


# ── Core extraction ──────────────────────────────────────────────────────────

def extract_sofi_statement(pdf_path):
    results = []
    accounts_found = []       # ordered list, may contain duplicates across pages
    seen_accounts = set()     # track unique accounts for frontmatter
    statement_period = None
    current_account = None    # tracks which account is active RIGHT NOW
    in_transactions = False

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            if statement_period is None:
                m = period_pattern.search(text)
                if m:
                    statement_period = m.group(0).strip()

            for line in text.split('\n'):
                line = line.strip()
                if not line:
                    continue
                if skip_patterns.search(line):
                    continue

                # — Account header detection —
                m = acct_header.match(line)
                if m:
                    acct_name = f"{m.group(1)} - {m.group(2)}"

                    if acct_name == current_account:
                        # Continuation page for the same account:
                        # stay in transaction mode, do NOT reset, do NOT re-emit header
                        continue

                    # New account section
                    current_account = acct_name
                    if acct_name not in seen_accounts:
                        seen_accounts.add(acct_name)
                        accounts_found.append(acct_name)

                    results.append(f"\n## {acct_name}")
                    # Reset transaction mode — wait for first txn row or summary fields
                    in_transactions = False
                    continue

                # — Balance summary fields (only before transactions start) —
                if not in_transactions and balance_labels.match(line):
                    results.append(line)
                    continue

                # — Transaction rows —
                # Turn on in_transactions the moment we see the first dated row
                # This handles both:
                #   (a) pages that have the DATE/TYPE/DESCRIPTION header (already skipped above)
                #   (b) continuation pages that jump straight into transactions
                if current_account and txn_row.match(line):
                    if not in_transactions:
                        # First transaction row for this account — emit table header once
                        results.append("\nDATE | TYPE | DESCRIPTION | AMOUNT | BALANCE")
                        results.append("-----|------|-------------|--------|--------")
                        in_transactions = True
                    results.append(line)
                    continue

    body = '\n'.join(results)
    return body, statement_period, accounts_found


# ── Frontmatter builder ──────────────────────────────────────────────────────

def build_frontmatter(pdf_stem, statement_period, accounts_found):
    today = datetime.today().strftime('%Y-%m-%d')

    slug_date = today.replace('-', '')[:6]
    for fmt in ('%B-%y', '%b-%y', '%B %y', '%b %y', '%B-%Y', '%b-%Y', '%B %Y', '%b %Y'):
        try:
            parsed = datetime.strptime(pdf_stem.strip(), fmt)
            slug_date = parsed.strftime('%Y%m')
            break
        except ValueError:
            continue

    unique_accounts = list(dict.fromkeys(accounts_found))  # preserve order, deduplicated
    acct_tags = [a.replace(' ', '-').lower() for a in unique_accounts]
    tags_yaml = '\n'.join(f'  - {t}' for t in ['finance', 'statement', 'sofi', slug_date] + acct_tags)

    accts_str = ', '.join(unique_accounts) if unique_accounts else '[UNCONFIRMED]'
    period_str = statement_period if statement_period else '[UNCONFIRMED]'

    frontmatter = f"""---
title: FINANCE-EXTRACT-SOFI-{slug_date}
filename: FINANCE-EXTRACT-SOFI-{slug_date}.md
date: {today}
domain: FINANCE
status: PENDING-UPDATE
compilation_status: CURRENT
canonical_file: FINANCIAL-SNAPSHOT.md
source_institution: SoFi Bank
accounts: {accts_str}
statement_period: {period_str}
tags:
{tags_yaml}
---

# SoFi Statement Extract — {period_str}
> Source: `{pdf_stem}.pdf`
> Extracted: {today}
> Status: PENDING canonical update to FINANCIAL-SNAPSHOT.md
"""
    return frontmatter


# ── File routing ─────────────────────────────────────────────────────────────

def archive_pdf(pdf_path, vault_root):
    dest_dir = vault_root / "08-ATTACH" / "FINANCE" / "STATEMENTS"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / pdf_path.name
    if not dest.exists():
        shutil.copy2(pdf_path, dest)
        print(f"  Archived PDF → {dest.relative_to(vault_root)}")
    else:
        print(f"  PDF already archived at {dest.relative_to(vault_root)}")


def write_extract(frontmatter, body, pdf_stem, vault_root):
    inbox = vault_root / "00-INBOX"
    inbox.mkdir(parents=True, exist_ok=True)
    output_file = inbox / f"FINANCE-EXTRACT-SOFI-{pdf_stem}.md"
    output_file.write_text(frontmatter + body, encoding='utf-8')
    print(f"  Extract → {output_file.relative_to(vault_root)}")
    return output_file


# ── Entry point ───────────────────────────────────────────────────────────────

def process_pdf(pdf_path, vault_root):
    pdf_path = Path(pdf_path).resolve()
    if not pdf_path.exists():
        print(f"  ERROR: File not found: {pdf_path}")
        return

    print(f"\nProcessing: {pdf_path.name}")
    body, period, accounts = extract_sofi_statement(pdf_path)
    frontmatter = build_frontmatter(pdf_path.stem, period, accounts)

    archive_pdf(pdf_path, vault_root)
    out = write_extract(frontmatter, body, pdf_path.stem, vault_root)

    print(f"  Period detected: {period or '[not found]'}")
    print(f"  Accounts found: {', '.join(accounts) or '[none]'}")
    print(f"  Done.\n")


if __name__ == '__main__':
    vault_root = Path(__file__).parent.resolve()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:  python sofi_extract.py 'June 25.pdf'")
        print("  Folder:       python sofi_extract.py 08-ATTACH/FINANCE/STATEMENTS/")
        sys.exit(1)

    target = Path(sys.argv[1])

    if target.is_dir():
        pdfs = sorted(target.glob("*.pdf"))
        if not pdfs:
            print(f"No PDFs found in {target}")
            sys.exit(1)
        print(f"Batch mode: {len(pdfs)} PDFs found in {target}")
        for pdf in pdfs:
            process_pdf(pdf, vault_root)
    elif target.suffix.lower() == '.pdf':
        process_pdf(target, vault_root)
    else:
        print(f"ERROR: {target} is not a PDF or directory.")
        sys.exit(1)
