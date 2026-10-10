#!/usr/bin/env python3
"""Render pin graphics (1000x1500 PNG) from tools/pins.json into docs/pins/.

Each pin entry: slug, headline, sub, label, theme (sage|clay|oat|pine), layout (a|b|c), guide.
Run: python3 tools/make_pins.py   (needs Playwright + Chromium)
"""
import html
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "pins"
LOGO = (ROOT / "static" / "logo.svg").read_text()

THEMES = {
    "sage": ("#a9b89b", "#6f8261", "#faf6ef", "#2b2a27"),
    "clay": ("#e8b799", "#b9643f", "#fffaf4", "#2b2a27"),
    "oat":  ("#f1e6d3", "#d2bd98", "#2b2a27", "#2b2a27"),
    "pine": ("#7f9a83", "#34503f", "#faf6ef", "#2b2a27"),
}

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@500;700&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1000px; height:1500px; font-family:Inter, sans-serif; }
.pin { width:1000px; height:1500px; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.label { font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:30px; }
h1 { font-family:Fraunces, Georgia, serif; font-weight:700; line-height:1.03; letter-spacing:-.02em; }
.sub { font-size:40px; line-height:1.35; font-weight:500; }
.foot { display:flex; align-items:center; gap:18px; font-size:34px; font-weight:700; }
.foot svg { width:70px; height:70px; }
"""


def render(p):
    a, b, light, dark = THEMES[p["theme"]]
    head = html.escape(p["headline"])
    sub = html.escape(p["sub"])
    label = html.escape(p["label"])
    ink = light if p["theme"] != "oat" else dark
    if p["layout"] == "a":
        body = f"""
<div class="pin" style="background:linear-gradient(160deg,{a},{b});color:{ink};padding:110px 90px 90px;">
  <div class="label" style="opacity:.85">{label}</div>
  <h1 style="font-size:118px;margin-top:60px;">{head}</h1>
  <p class="sub" style="margin-top:50px;opacity:.92;max-width:760px;">{sub}</p>
  <div style="flex:1"></div>
  <div class="foot">{LOGO}<span>therentednest.co.uk</span></div>
</div>"""
    elif p["layout"] == "b":
        body = f"""
<div class="pin" style="background:#faf6ef;color:{dark};">
  <div style="height:640px;background:linear-gradient(150deg,{a},{b});padding:90px;display:flex;align-items:flex-end;">
    <div class="label" style="background:#faf6ef;color:{dark};padding:16px 30px;border-radius:999px;">{label}</div>
  </div>
  <div style="padding:70px 90px 90px;display:flex;flex-direction:column;flex:1;">
    <h1 style="font-size:96px;">{head}</h1>
    <p class="sub" style="margin-top:36px;color:#6b665d;">{sub}</p>
    <div style="flex:1"></div>
    <div class="foot">{LOGO}<span>therentednest.co.uk</span></div>
  </div>
</div>"""
    else:
        body = f"""
<div class="pin" style="background:{b};padding:70px;">
  <div style="background:#faf6ef;color:{dark};border-radius:36px;flex:1;padding:100px 80px 80px;display:flex;flex-direction:column;">
    <div class="label" style="color:{b};">{label}</div>
    <h1 style="font-size:104px;margin-top:50px;">{head}</h1>
    <div style="width:140px;height:10px;background:{a};border-radius:10px;margin:56px 0;"></div>
    <p class="sub" style="color:#6b665d;">{sub}</p>
    <div style="flex:1"></div>
    <div class="foot">{LOGO}<span>therentednest.co.uk</span></div>
  </div>
</div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def main():
    pins = json.loads((ROOT / "tools" / "pins.json").read_text())
    only = set(sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 1500})
        for p in pins:
            if only and p["slug"] not in only:
                continue
            page.set_content(render(p), wait_until="networkidle")
            page.wait_for_timeout(300)
            page.screenshot(path=str(OUT / f"{p['slug']}.png"))
            print("rendered", p["slug"])
        browser.close()


if __name__ == "__main__":
    main()
