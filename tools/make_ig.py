#!/usr/bin/env python3
"""Render Instagram carousel posts (1080x1350 PNG slides) from ops/instagram/posts.json.

Each post: {"slug", "week" (YYYY-MM-DD), "theme" (sage|clay|oat|pine), "photo" (file in static/photos, cover),
            "label", "headline", "sub", "tips": [{"title","text","photo"?}, ...] (3-6; tip photo optional, shown top half), "guide", "caption"}
Output: static/social/<week>/<slug>/01.png ... + caption.txt, and static/social/index.html (phone-friendly page for Dylan)
Run: python3 tools/make_ig.py [slug ...]   (needs Playwright + Chromium)
"""
import base64
import html
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "social"  # served at /social/ (noindex, robots-disallowed)
LOGO = (ROOT / "static" / "logo.svg").read_text()
THEMES = {
    "sage": ("#a9b89b", "#6f8261"),
    "clay": ("#e8b799", "#b9643f"),
    "oat": ("#f1e6d3", "#8a6d45"),
    "pine": ("#7f9a83", "#34503f"),
}
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@500;700&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1080px; height:1350px; font-family:Inter, sans-serif; color:#2b2a27; }
.s { width:1080px; height:1350px; position:relative; overflow:hidden; display:flex; flex-direction:column; }
.label { font-weight:700; letter-spacing:.16em; text-transform:uppercase; font-size:28px; }
h1, h2 { font-family:Fraunces, Georgia, serif; font-weight:700; line-height:1.05; letter-spacing:-.02em; }
p { font-size:40px; line-height:1.4; font-weight:500; }
.foot { display:flex; align-items:center; gap:16px; font-size:30px; font-weight:700; }
.foot svg { width:60px; height:60px; }
.num { font-family:Fraunces, Georgia, serif; font-weight:700; font-size:150px; line-height:1; }
"""


def wrap(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"


def cover(p, a, b):
    img = ""
    if p.get("photo"):
        data = base64.b64encode((ROOT / "static" / "photos" / p["photo"]).read_bytes()).decode()
        img = f"background:url(data:image/jpeg;base64,{data}) center/cover;"
    return wrap(f"""
<div class="s" style="{img or f'background:{a};'}">
  <div style="background:#faf6ef;margin:70px;padding:64px 60px;border-radius:32px;border-bottom:12px solid {b};">
    <div class="label" style="color:{b};">{html.escape(p['label'])}</div>
    <h1 style="font-size:{p.get('size', 96)}px;margin-top:24px;">{html.escape(p['headline'])}</h1>
    <p style="margin-top:24px;color:#6b665d;font-size:36px;">{html.escape(p['sub'])}</p>
  </div>
  <div style="flex:1"></div>
  <div class="foot" style="margin:0 0 56px 70px;align-self:flex-start;background:rgba(250,246,239,.95);border-radius:999px;padding:12px 28px 12px 14px;">{LOGO}<span>Swipe for the list →</span></div>
</div>""")


def photo_css(name):
    data = base64.b64encode((ROOT / "static" / "photos" / name).read_bytes()).decode()
    return f"background:url(data:image/jpeg;base64,{data}) center/cover;"


def tip(i, n, t, a, b):
    foot = f'''<div class="foot" style="justify-content:space-between;"><span style="display:flex;align-items:center;gap:16px;">{LOGO}The Rented Nest</span><span style="color:#8a857b;">{i}/{n}</span></div>'''
    if t.get("photo"):  # photo top, text below
        return wrap(f"""
<div class="s" style="background:#faf6ef;">
  <div style="height:780px;{photo_css(t['photo'])}position:relative;">
    <div class="num" style="position:absolute;left:70px;bottom:-60px;background:#faf6ef;color:{b};font-size:110px;width:170px;height:170px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:8px solid {a};">{i}</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;padding:130px 80px 70px;">
    <h2 style="font-size:72px;">{html.escape(t['title'])}</h2>
    <p style="color:#4a4740;font-size:42px;margin-top:28px;">{html.escape(t['text'])}</p>
    <div style="flex:1"></div>
    {foot}
  </div>
</div>""")
    return wrap(f"""
<div class="s" style="background:#faf6ef;padding:110px 90px 80px;">
  <div style="flex:.6"></div>
  <div class="num" style="color:{a};">{i}</div>
  <h2 style="font-size:76px;margin-top:30px;">{html.escape(t['title'])}</h2>
  <div style="width:120px;height:10px;background:{b};border-radius:10px;margin:44px 0;"></div>
  <p style="color:#4a4740;font-size:44px;">{html.escape(t['text'])}</p>
  <div style="flex:1"></div>
  {foot}
</div>""")


def end(p, a, b):
    return wrap(f"""
<div class="s" style="background:{b};color:#faf6ef;padding:120px 90px 90px;">
  <h2 style="font-size:88px;">The full guide is one tap away</h2>
  <p style="margin-top:44px;opacity:.95;">Prices, retailers and the details are on our website – tap the link in our bio.</p>
  <p style="margin-top:36px;opacity:.95;">Save this post for later ↓</p>
  <div style="flex:1"></div>
  <div class="foot" style="background:#faf6ef;color:#2b2a27;border-radius:999px;padding:12px 28px 12px 14px;align-self:flex-start;">{LOGO}<span>therentednest.co.uk</span></div>
</div>""")


def main():
    posts = json.loads((ROOT / "ops" / "instagram" / "posts.json").read_text())
    only = set(sys.argv[1:])
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        for p in posts:
            if only and p["slug"] not in only:
                continue
            a, b = THEMES[p.get("theme", "sage")]
            d = OUT / p["week"] / p["slug"]
            d.mkdir(parents=True, exist_ok=True)
            slides = [cover(p, a, b)]
            slides += [tip(i, len(p["tips"]), t, a, b) for i, t in enumerate(p["tips"], 1)]
            slides.append(end(p, a, b))
            for k, s in enumerate(slides, 1):
                page.set_content(s, wait_until="networkidle")
                page.wait_for_timeout(250)
                page.screenshot(path=str(d / f"{k:02d}.png"))
            (d / "caption.txt").write_text(p["caption"].strip() + "\n")
            print("rendered", p["slug"], len(slides), "slides")
        browser.close()
    write_index(posts)


def write_index(posts):
    """Phone page: newest week first; tap-and-hold to save each slide, caption in a box to copy."""
    blocks = []
    for p in sorted(posts, key=lambda x: x["week"], reverse=True):
        d = OUT / p["week"] / p["slug"]
        if not d.exists():
            continue
        imgs = "".join(f'<img src="{p["week"]}/{p["slug"]}/{f.name}?v={int(f.stat().st_mtime)}" loading="lazy" alt="slide {f.stem}">'
                       for f in sorted(d.glob("*.png")))
        blocks.append(f"""<section><h2>Post week of {p['week']}: {html.escape(p['headline'])}</h2>
<p class="m">{len(list(d.glob('*.png')))} slides – save them in order, post as one carousel.</p>
<div class="row">{imgs}</div>
<textarea readonly onclick="this.select()">{html.escape(p['caption'].strip())}</textarea></section>""")
    (OUT / "index.html").write_text(f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Instagram posts – The Rented Nest</title><style>
body{{font-family:system-ui,sans-serif;margin:0;padding:16px;background:#faf6ef;color:#2b2a27}}
section{{margin:0 0 40px}} h2{{font-size:18px}} .m{{color:#6b665d;font-size:14px}}
.row{{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory}} .row img{{width:78vw;max-width:360px;scroll-snap-align:start;border-radius:8px}}
textarea{{width:100%;height:220px;margin-top:10px;font:15px system-ui;padding:10px;border-radius:8px;border:1px solid #ccc;box-sizing:border-box}}
</style></head><body><h1>Instagram posts to schedule</h1>
<p class="m">Newest first. For each post: save the slides (tap and hold), then in Instagram or Meta Business Suite add them as one carousel and paste the caption.</p>
{''.join(blocks)}</body></html>""")


if __name__ == "__main__":
    main()
