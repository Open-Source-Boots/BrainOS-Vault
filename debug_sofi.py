# debug_sofi.py — run once, paste output here
import pdfplumber
import sys
from pathlib import Path

pdf_path = Path(sys.argv[1])
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        text = page.extract_text()
        if not text:
            continue
        print(f"\n{'='*60}")
        print(f"PAGE {i}")
        print('='*60)
        for line in text.split('\n'):
            print(repr(line))  # repr shows exact whitespace and chars