"""Render checklist HTML sources in tools/checklists/ to PDFs in static/checklists/."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "tools" / "checklists"
OUT = ROOT / "static" / "checklists"
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for f in SRC.glob("*.html"):
        pg.goto(f.as_uri())
        pg.pdf(path=str(OUT / f"{f.stem}-checklist.pdf"), format="A4", print_background=True)
        print("wrote", f.stem)
    b.close()
