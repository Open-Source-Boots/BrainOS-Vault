import pdfplumber
import re
import sys
from pathlib import Path

def extract_sofi_statement(pdf_path):
    results = []
    current_account = None
    in_transactions = False
    
    # Patterns
    acct_header = re.compile(r'^(Checking Account|Savings Account)\s*[-–]\s*(\d+)$')
    balance_labels = re.compile(
        r'^(Current Balance|Beginning Balance|Current Interest Rate|Monthly Interest Paid|Annual Percentage Yield|Year-to-date Interest Paid)',
        re.IGNORECASE
    )
    # Transaction row: date, type, description, amount, balance
    txn_row = re.compile(
        r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}'
    )
    skip_patterns = re.compile(
        r'(SoFi checking|SoFi Bank|Member FDIC|Page \d+ of|Important Information|'
        r'Insured Deposit|FDIC insurance|Payable on Death|Participating banks|'
        r'Deposit Agreement|Questions About|Reporting Other|Interest/Dividends|'
        r'How to Contact|Contact Information|Mailing Address|Transaction ID:|'
        r'Transaction Details|Balances below|Current balances include|'
        r'2021 SoFi|SoFi Technologies|Annual Percentage Yield Earned|'
        r'accrues daily|Customer Agreement|rate sheet|Travel Vault)',
        re.IGNORECASE
    )
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split('\n'):
                line = line.strip()
                if not line:
                    continue
                if skip_patterns.search(line):
                    continue
                
                # Detect account section header
                m = acct_header.match(line)
                if m:
                    current_account = f"{m.group(1)} - {m.group(2)}"
                    results.append(f"\n## {current_account}")
                    in_transactions = False
                    continue
                
                # Detect account summary fields
                if balance_labels.match(line):
                    results.append(line)
                    continue
                
                # Detect start of transaction table
                if re.match(r'^DATE\s+TYPE\s+DESCRIPTION', line, re.IGNORECASE):
                    results.append("\nDATE | TYPE | DESCRIPTION | AMOUNT | BALANCE")
                    results.append("-----|------|-------------|--------|--------")
                    in_transactions = True
                    continue
                
                # Transaction rows
                if in_transactions and txn_row.match(line):
                    results.append(line)
                    continue
    
    return '\n'.join(results)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python sofi_extract.py <statement.pdf>")
        sys.exit(1)
    
    pdf_file = Path(sys.argv[1])
    output_file = pdf_file.with_suffix('.md')
    
    extracted = extract_sofi_statement(pdf_file)
    output_file.write_text(extracted)
    print(f"Extracted to: {output_file}")
    print(extracted)