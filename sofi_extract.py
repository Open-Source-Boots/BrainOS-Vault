import pdfplumber
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime


# ── Patterns ────────────────────────────────────────────────────────────────

acct_header    = re.compile(r'^(Checking Account|Savings Account)\s*[-–]\s*(\d+)$')
balance_labels = re.compile(
    r'^(Current Balance|Beginning Balance|Current Interest Rate'
    r'|Monthly Interest Paid|Annual Percentage Yield|Year-to-date Interest Paid)',
    re.IGNORECASE
)
txn_row        = re.compile(r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}')
period_pattern = re.compile(
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}'
    r'\s*[-–]\s*'
    r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+(\d{4})'
)
amount_re      = re.compile(r'(-?\$[\d,]+\.\d{2})\s+(-?\$[\d,]+\.\d{2})\s*$')

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
    r'DATE\s+TYPE\s+DESCRIPTION)',
    re.IGNORECASE
)

CATEGORY_RULES = [
    (re.compile(r'GOODLIFE|PAYROLL|PAYACTIV', re.I),        'income'),
    (re.compile(r'AFFIRM|DISCOVER|CHASE|BEST EGG|ONEMAIN|CAPITAL ONE|AMAZON.*SYF|PAYPAL', re.I), 'debt-payment'),
    (re.compile(r'ALLSTATE|ATT|AT&T', re.I),                'insurance-utilities'),
    (re.compile(r'ROBINHOOD', re.I),                        'investing'),
    (re.compile(r'TACO BELL|McDONALD|BURGER KING|LITTLE CAESARS|CASEYS|HY-VEE|DOMINO|SUBWAY|CHIPOTLE|SONIC|WENDYS|POPEYES', re.I), 'food'),
    (re.compile(r'QT|QUIK TRIP|SHELL|PHILLIPS|KUM.*GO|CASEY', re.I), 'gas'),
    (re.compile(r'NETFLIX|SPOTIFY|HULU|DISNEY|XBOX|STEAM|PEBBLEHOST|ROKU|APPLE.*CASH|FANDUEL|SMARTARB', re.I), 'subscriptions-entertainment'),
    (re.compile(r'WILDSIDE|SMOKE|TOBACCO|VAPE|LIQUOR|MYERS', re.I), 'smoke-alcohol'),
    (re.compile(r'From Savings|To Savings|To Checking|From Checking', re.I), 'internal-transfer'),
    (re.compile(r'VENMO', re.I),                            'transfer-p2p'),
]

def categorize(description):
    for pattern, label in CATEGORY_RULES:
        if pattern.search(description):
            return label
    return 'other'

def parse_amount(s):
    try:
        return float(s.replace('$', '').replace(',', ''))
    except Exception:
        return 0.0


# ── Core extraction ──────────────────────────────────────────────────────────

def extract_sofi_statement(pdf_path):
    accounts      = {}
    acct_order    = []
    statement_period = None
    current_account  = None
    in_transactions  = False

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
                if not line or skip_patterns.search(line):
                    continue

                m = acct_header.match(line)
                if m:
                    acct_name = f"{m.group(1)} - {m.group(2)}"
                    if acct_name == current_account:
                        continue
                    current_account = acct_name
                    in_transactions = False
                    if acct_name not in accounts:
                        accounts[acct_name] = {'balance_lines': [], 'transactions': []}
                        acct_order.append(acct_name)
                    continue

                if current_account and not in_transactions and balance_labels.match(line):
                    accounts[current_account]['balance_lines'].append(line)
                    continue

                if current_account and txn_row.match(line):
                    in_transactions = True
                    am = amount_re.search(line)
                    if am:
                        amount_str  = am.group(1)
                        balance_str = am.group(2)
                        prefix      = line[:am.start()].strip()
                    else:
                        amount_str  = '[UNCONFIRMED]'
                        balance_str = '[UNCONFIRMED]'
                        prefix      = line

                    date_m = re.match(
                        r'^((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4})\s+(\S+(?:\s+\S+)?)\s+(.+)$',
                        prefix
                    )
                    if date_m:
                        date  = date_m.group(1)
                        ttype = date_m.group(2)
                        desc  = date_m.group(3).strip()
                    else:
                        date  = prefix[:12].strip()
                        ttype = ''
                        desc  = prefix

                    accounts[current_account]['transactions'].append(
                        (date, ttype, desc, amount_str, balance_str, categorize(desc))
                    )
                    continue

    return accounts, acct_order, statement_period


# ── Output formatter ──────────────────────────────────────────────────────────

def format_body(accounts, acct_order, statement_period, slug_date):
    sections = []
    for acct_name in acct_order:
        data = accounts[acct_name]
        txns = data['transactions']

        income    = sum(parse_amount(t[3]) for t in txns if t[5] == 'income')
        debt      = sum(parse_amount(t[3]) for t in txns if t[5] == 'debt-payment')
        investing = sum(parse_amount(t[3]) for t in txns if t[5] == 'investing')
        food      = sum(parse_amount(t[3]) for t in txns if t[5] == 'food')
        gas       = sum(parse_amount(t[3]) for t in txns if t[5] == 'gas')
        subs      = sum(parse_amount(t[3]) for t in txns if t[5] == 'subscriptions-entertainment')
        smoke     = sum(parse_amount(t[3]) for t in txns if t[5] == 'smoke-alcohol')
        transfers = sum(parse_amount(t[3]) for t in txns if t[5] in ('internal-transfer', 'transfer-p2p'))
        other     = sum(parse_amount(t[3]) for t in txns if t[5] == 'other')
        net       = sum(parse_amount(t[3]) for t in txns)

        opening = '[UNCONFIRMED]'
        closing = '[UNCONFIRMED]'
        for bl in data['balance_lines']:
            if 'beginning balance' in bl.lower():
                bm = re.search(r'\$[\d,]+\.\d{2}', bl)
                if bm: opening = bm.group(0)
            if 'current balance' in bl.lower():
                bm = re.search(r'\$[\d,]+\.\d{2}', bl)
                if bm: closing = bm.group(0)

        out = [f"## {acct_name}", ""]
        out += [
            f"- account:: {acct_name}",
            f"- period:: {statement_period or '[UNCONFIRMED]'}",
            f"- opening-balance:: {opening}",
            f"- closing-balance:: {closing}",
            f"- net-change:: {'${:,.2f}'.format(net)}",
            f"- total-income:: {'${:,.2f}'.format(income)}",
            f"- total-debt-payments:: {'${:,.2f}'.format(debt)}",
            f"- total-investing:: {'${:,.2f}'.format(investing)}",
            f"- transaction-count:: {len(txns)}",
            ""
        ]

        summary_parts = []
        if income > 0:     summary_parts.append(f"income of ${income:,.2f}")
        if debt < 0:       summary_parts.append(f"debt payments totaling ${abs(debt):,.2f}")
        if investing < 0:  summary_parts.append(f"investing activity of ${abs(investing):,.2f} (Robinhood)")
        if food < 0:       summary_parts.append(f"food spending of ${abs(food):,.2f}")
        if gas < 0:        summary_parts.append(f"gas of ${abs(gas):,.2f}")
        if subs < 0:       summary_parts.append(f"subscriptions/entertainment of ${abs(subs):,.2f}")
        if smoke < 0:      summary_parts.append(f"smoke/alcohol of ${abs(smoke):,.2f}")
        if transfers != 0: summary_parts.append(f"internal transfers net of ${transfers:,.2f}")
        if other < 0:      summary_parts.append(f"other spending of ${abs(other):,.2f}")

        direction = 'increased' if net >= 0 else 'decreased'
        summary = (f"During {statement_period or slug_date}, this account {direction} "
                   f"by ${abs(net):,.2f} (from {opening} to {closing}). "
                   + ('Activity included: ' + ', '.join(summary_parts) + '.' if summary_parts else ''))
        out += [f"> {summary}", ""]

        out += ["### Spending by Category", "", "| Category | Total |", "|----------|-------|"]
        cat_totals = {}
        for t in txns:
            cat_totals.setdefault(t[5], 0.0)
            cat_totals[t[5]] += parse_amount(t[3])
        for cat, total in sorted(cat_totals.items(), key=lambda x: x[1]):
            out.append(f"| {cat} | {'${:,.2f}'.format(total)} |")
        out.append("")

        out += ["### All Transactions", "",
                "| Date | Type | Description | Amount | Balance | Category |",
                "|------|------|-------------|--------|---------|----------|"
               ]
        for date, ttype, desc, amount, balance, cat in txns:
            out.append(f"| {date} | {ttype} | {desc} | {amount} | {balance} | {cat} |")
        out.append("")

        sections.append('\n'.join(out))

    return '\n---\n\n'.join(sections)


# ── Frontmatter ───────────────────────────────────────────────────────────────

def build_frontmatter(pdf_stem, statement_period, acct_order, slug_date):
    today = datetime.today().strftime('%Y-%m-%d')
    unique_accounts = list(dict.fromkeys(acct_order))
    acct_tags  = [a.replace(' ', '-').lower() for a in unique_accounts]
    tags_yaml  = '\n'.join(f'  - {t}' for t in ['finance', 'statement', 'sofi', slug_date] + acct_tags)
    accts_str  = ', '.join(unique_accounts) if unique_accounts else '[UNCONFIRMED]'
    period_str = statement_period if statement_period else '[UNCONFIRMED]'
    return f"""---
title: {slug_date}-FINANCE-sofi-extract
filename: {slug_date}-FINANCE-sofi-extract.md
date: {today}
statement-period: {period_str}
statement-month: {slug_date}
domain: FINANCE
status: PENDING-UPDATE
compilation_status: CURRENT
canonical_file: FINANCIAL-SNAPSHOT.md
source_institution: SoFi Bank
accounts: {accts_str}
tags:
{tags_yaml}
---

# SoFi Statement Extract — {period_str}

> **Source:** `{pdf_stem}.pdf` | **Extracted:** {today} | **Status:** PENDING canonical update

"""


# ── Slug date ─────────────────────────────────────────────────────────────────

def get_slug_date(pdf_stem, statement_period):
    for fmt in ('%B-%y', '%b-%y', '%B %y', '%b %y', '%B-%Y', '%b-%Y', '%B %Y', '%b %Y'):
        try:
            return datetime.strptime(pdf_stem.strip(), fmt).strftime('%Y%m')
        except ValueError:
            continue
    if statement_period:
        end_m = re.search(
            r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+(\d{4})\s*$',
            statement_period
        )
        if end_m:
            try:
                return datetime.strptime(f"{end_m.group(1)} {end_m.group(2)}", '%b %Y').strftime('%Y%m')
            except ValueError:
                pass
    return datetime.today().strftime('%Y%m')


# ── File routing ──────────────────────────────────────────────────────────────

def archive_pdf(pdf_path, vault_root):
    dest_dir = vault_root / "08-ATTACH" / "FINANCE" / "STATEMENTS"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / pdf_path.name
    if not dest.exists():
        shutil.copy2(pdf_path, dest)
        print(f"  Archived PDF → {dest.relative_to(vault_root)}")
    else:
        print(f"  PDF already archived at {dest.relative_to(vault_root)}")

def write_extract(content, slug_date, vault_root):
    inbox = vault_root / "00-INBOX"
    inbox.mkdir(parents=True, exist_ok=True)
    output_file = inbox / f"{slug_date}-FINANCE-sofi-extract.md"
    output_file.write_text(content, encoding='utf-8')
    print(f"  Extract → {output_file.relative_to(vault_root)}")
    return output_file


# ── Entry point ───────────────────────────────────────────────────────────────

def process_pdf(pdf_path, vault_root):
    pdf_path = Path(pdf_path).resolve()
    if not pdf_path.exists():
        print(f"  ERROR: File not found: {pdf_path}")
        return
    print(f"\nProcessing: {pdf_path.name}")
    accounts, acct_order, period = extract_sofi_statement(pdf_path)
    slug_date   = get_slug_date(pdf_path.stem, period)
    frontmatter = build_frontmatter(pdf_path.stem, period, acct_order, slug_date)
    body        = format_body(accounts, acct_order, period, slug_date)
    archive_pdf(pdf_path, vault_root)
    write_extract(frontmatter + body, slug_date, vault_root)
    print(f"  Period: {period or '[not found]'}")
    print(f"  Accounts: {', '.join(acct_order) or '[none]'}")
    print(f"  Transactions: {sum(len(accounts[a]['transactions']) for a in acct_order)}")
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
