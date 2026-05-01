# debug_focused.py
import pdfplumber
import sys
from pathlib import Path

pdf_path = Path(sys.argv[1])
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        text = page.extract_text()
        if not text:
            continue
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        print(f"\n=== PAGE {i} — first 4 lines ===")
        for l in lines[:4]:
            print(repr(l))
        print(f"=== PAGE {i} — last 4 lines ===")
        for l in lines[-4:]:
            print(repr(l))