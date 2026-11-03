#!/usr/bin/env python3
"""Render pin graphics (1000x1500 PNG) from tools/pins.json into docs/pins/.

Each pin entry: slug, headline, sub, label, guide, layout, photo.
  Old layouts (photo2|photo|a|b|c) use theme (sage|clay|oat|pine).
  v3 layouts (overlay|split|poster|checklist|frame|numbered|arch|duo|script) use palette + font;
  checklist needs points [3-4 short strings], numbered needs num, duo needs photo_b, script takes kicker.
Run: python3 tools/make_pins.py [slugs] [--file other.json] [--out dir]   (needs Playwright + Chromium)
Then: python3 tools/check_pin_variety.py
"""
import base64
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

# ---------------------------------------------------------------------------
# v3 styles (added 3 Nov 2026 after Dylan: "the pins all look the same").
# Each pin picks a layout + palette + font; tools/check_pin_variety.py enforces rotation.
# palette: (background, ink on background, accent, soft tint)
PALETTES = {
    "terracotta": ("#c4572f", "#fff7ee", "#f6c89f", "#f3dccb"),
    "navy":       ("#1f2d4a", "#f5efe4", "#e9b949", "#d6dbe6"),
    "mustard":    ("#e3a92b", "#2a2118", "#fff4dc", "#f7e3b4"),
    "forest":     ("#2f4a3a", "#f4efe3", "#e8a27c", "#d4dfd6"),
    "blush":      ("#f2cfc4", "#3a2320", "#b5473a", "#f8e4dd"),
    "cobalt":     ("#2747a6", "#ffffff", "#ffd166", "#dbe2f5"),
    "charcoal":   ("#262626", "#fafafa", "#ff8a5b", "#e4e4e4"),
    "berry":      ("#8e1f2f", "#fff3e6", "#e6c36a", "#f2d9d6"),
    "mint":       ("#cfe6d8", "#1f3a2e", "#2f7d5b", "#e6f2ea"),
    "lilac":      ("#d9cdea", "#2c2440", "#6b4fa0", "#ece6f4"),
    "cream":      ("#f6efe2", "#2b2a27", "#c4572f", "#fbf7f0"),
    "teal":       ("#1d6a6a", "#f2fbf9", "#ffcf99", "#d2e8e6"),
}
FONTS = {  # heading font, weight, letter-spacing, line-height
    "fraunces": ("'Fraunces', Georgia, serif", 700, "-.02em", 1.03),
    "dmserif":  ("'DM Serif Display', Georgia, serif", 400, "-.01em", 1.02),
    "archivo":  ("'Archivo Black', Impact, sans-serif", 400, "-.02em", 1.0),
    "playfair": ("'Playfair Display', Georgia, serif", 800, "-.01em", 1.05),
    "space":    ("'Space Grotesk', Inter, sans-serif", 700, "-.03em", 1.0),
    "bricolage":("'Bricolage Grotesque', Inter, sans-serif", 800, "-.03em", 0.98),
}
V3_FONTS_CSS = ("@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bricolage+Grotesque:opsz,wght@12..96,800"
                "&family=Caveat:wght@700&family=DM+Serif+Display&family=Playfair+Display:wght@800&family=Space+Grotesk:wght@700&display=swap');")
V3_LAYOUTS = {"overlay", "split", "poster", "checklist", "frame", "numbered", "arch", "duo", "script"}


def _img(name):
    return "data:image/jpeg;base64," + base64.b64encode((ROOT / "static" / "photos" / name).read_bytes()).decode()


def render_v3(p):
    bg, ink, acc, tint = PALETTES[p.get("palette", "cream")]
    fam, wt, ls, lh = FONTS[p.get("font", "fraunces")]
    head = html.escape(p["headline"])
    sub = html.escape(p.get("sub", ""))
    label = html.escape(p.get("label", ""))
    size = p.get("size")
    H = lambda px, extra="": f'<h1 style="font-family:{fam};font-weight:{wt};letter-spacing:{ls};line-height:{lh};font-size:{size or px}px;{extra}">{head}</h1>'
    url = '<span style="font-size:28px;font-weight:700;">therentednest.co.uk</span>'
    lay = p["layout"]
    photo = _img(p["photo"]) if p.get("photo") else None
    if lay == "overlay":   # full-bleed photo, dark fade, big light type at the bottom
        body = f"""
<div class="pin" style="background:url({photo}) center/cover;color:#fff;">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.25) 50%,rgba(0,0,0,.82) 100%);"></div>
  <div style="position:relative;margin:60px 0 0 60px;align-self:flex-start;background:{acc};color:#1d1b18;padding:14px 28px;border-radius:999px;" class="label">{label}</div>
  <div style="flex:1"></div>
  <div style="position:relative;padding:0 70px 70px;">
    {H(118, 'text-shadow:0 2px 24px rgba(0,0,0,.35);')}
    <p class="sub" style="margin-top:26px;font-size:38px;color:#f3efe8;">{sub}</p>
    <div style="margin-top:40px;display:flex;align-items:center;gap:16px;"><div style="width:60px;height:6px;background:{acc};"></div>{url}</div>
  </div>
</div>"""
    elif lay == "split":   # photo top, solid colour block bottom
        body = f"""
<div class="pin" style="background:{bg};color:{ink};">
  <div style="height:820px;background:url({photo}) center/cover;"></div>
  <div style="flex:1;padding:60px 70px 56px;display:flex;flex-direction:column;">
    <div class="label" style="color:{acc};">{label}</div>
    {H(98, 'margin-top:20px;')}
    <p class="sub" style="margin-top:22px;font-size:36px;opacity:.9;">{sub}</p>
    <div style="flex:1"></div>{url}
  </div>
</div>"""
    elif lay == "poster":  # colour poster: huge type, tilted photo card, round sticker
        body = f"""
<div class="pin" style="background:{bg};color:{ink};padding:80px 70px 60px;">
  {H(128)}
  <p class="sub" style="margin-top:26px;font-size:38px;opacity:.9;max-width:820px;">{sub}</p>
  <div style="position:relative;flex:1;margin-top:50px;">
    <div style="position:absolute;inset:0 30px 70px 30px;background:url({photo}) center/cover;border:16px solid #fff;border-radius:8px;transform:rotate(-2.5deg);box-shadow:0 18px 40px rgba(0,0,0,.25);"></div>
    <div style="position:absolute;right:0;top:-40px;width:210px;height:210px;border-radius:50%;background:{acc};color:#1d1b18;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:700;font-size:28px;line-height:1.15;padding:24px;transform:rotate(8deg);text-transform:uppercase;letter-spacing:.06em;">{label}</div>
  </div>
  <div style="margin-top:6px;">{url}</div>
</div>"""
    elif lay == "checklist":  # list pin: headline + ticked points (+ photo strip)
        pts = "".join(f'<li style="display:flex;gap:26px;align-items:flex-start;margin-top:34px;"><span style="flex:none;width:60px;height:60px;border-radius:50%;background:{acc};color:{bg};display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:700;">✓</span><span>{html.escape(t)}</span></li>' for t in p["points"])
        strip = f'<div style="flex:1;min-height:300px;margin:40px -70px 0;background:url({photo}) center/cover;"></div>' if photo else '<div style="flex:1"></div>'
        body = f"""
<div class="pin" style="background:{bg};color:{ink};padding:80px 70px 0;">
  <div class="label" style="color:{acc};">{label}</div>
  {H(96, 'margin-top:22px;')}
  <ul style="list-style:none;margin-top:30px;font-size:46px;font-weight:500;line-height:1.22;">{pts}</ul>
  {strip}
  <div style="padding:28px 0;">{url}</div>
</div>"""
    elif lay == "frame":   # photo in a thick coloured mat, white card overlapping
        body = f"""
<div class="pin" style="background:{bg};padding:46px;">
  <div style="flex:1;background:url({photo}) center/cover;border-radius:22px;position:relative;display:flex;flex-direction:column;justify-content:flex-end;">
    <div style="margin:0 40px -10px;background:#fffdf8;color:#24221f;border-radius:22px;padding:50px 54px 46px;box-shadow:0 20px 50px rgba(0,0,0,.22);text-align:center;">
      <div class="label" style="color:{bg if bg not in ('#f6efe2','#cfe6d8','#d9cdea','#f2cfc4') else acc};font-size:26px;">{label}</div>
      {H(86, 'margin-top:18px;')}
      <p class="sub" style="margin-top:18px;font-size:32px;color:#6b665d;">{sub}</p>
    </div>
  </div>
  <div style="text-align:center;color:{ink};padding-top:36px;">{url}</div>
</div>"""
    elif lay == "numbered":  # giant number + headline, photo below
        body = f"""
<div class="pin" style="background:{bg};color:{ink};">
  <div style="padding:70px 70px 40px;display:flex;gap:36px;align-items:flex-start;">
    <div style="font-family:{fam};font-weight:{wt};font-size:300px;line-height:.8;color:{acc};">{html.escape(str(p["num"]))}</div>
    <div style="padding-top:18px;"><div class="label" style="opacity:.8;font-size:26px;">{label}</div>{H(84, 'margin-top:14px;')}</div>
  </div>
  <p class="sub" style="padding:0 70px;font-size:36px;opacity:.9;">{sub}</p>
  <div style="flex:1;margin:44px 70px 0;background:url({photo}) center/cover;border-radius:28px 28px 0 0;"></div>
  <div style="padding:26px 70px;">{url}</div>
</div>"""
    elif lay == "arch":    # photo in an arch window on a tinted background
        body = f"""
<div class="pin" style="background:{tint};color:#24221f;align-items:center;padding:70px 80px 56px;text-align:center;">
  <div class="label" style="color:{acc if bg in ('#f6efe2','#cfe6d8','#d9cdea','#f2cfc4','#e3a92b') else bg};">{label}</div>
  {H(92, 'margin-top:20px;')}
  <div style="flex:1;width:100%;margin-top:44px;background:url({photo}) center/cover;border-radius:420px 420px 24px 24px;border:14px solid {bg};"></div>
  <p class="sub" style="margin-top:30px;font-size:34px;color:#5b564e;">{sub}</p>
  <div style="margin-top:18px;">{url}</div>
</div>"""
    elif lay == "duo":     # two photos with a colour band between
        photo_b = _img(p["photo_b"])
        body = f"""
<div class="pin" style="background:{bg};color:{ink};">
  <div style="height:520px;background:url({photo}) center/cover;"></div>
  <div style="padding:46px 64px 42px;">
    <div class="label" style="color:{acc};font-size:26px;">{label}</div>
    {H(88, 'margin-top:14px;')}
    <p class="sub" style="margin-top:16px;font-size:32px;opacity:.9;">{sub}</p>
  </div>
  <div style="flex:1;background:url({photo_b}) center/cover;position:relative;">
    <div style="position:absolute;left:48px;bottom:40px;background:rgba(255,253,248,.95);color:#24221f;border-radius:999px;padding:12px 28px;">{url}</div>
  </div>
</div>"""
    else:  # "script": handwritten kicker over a photo with a colour panel
        body = f"""
<div class="pin" style="background:{bg};color:{ink};">
  <div style="padding:80px 70px 50px;">
    <div style="font-family:'Caveat',cursive;font-size:76px;line-height:1;color:{acc};transform:rotate(-3deg);transform-origin:left;">{html.escape(p.get("kicker", label))}</div>
    {H(104, 'margin-top:20px;')}
    <p class="sub" style="margin-top:24px;font-size:36px;opacity:.9;">{sub}</p>
  </div>
  <div style="flex:1;margin:0 70px;background:url({photo}) center/cover;border-radius:999px 999px 0 0;"></div>
  <div style="padding:28px 70px;">{url}</div>
</div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{V3_FONTS_CSS}{CSS}</style></head><body>{body}</body></html>"


def render(p):
    if p.get("layout") in V3_LAYOUTS:
        return render_v3(p)
    a, b, light, dark = THEMES[p["theme"]]
    head = html.escape(p["headline"])
    sub = html.escape(p["sub"])
    label = html.escape(p["label"])
    ink = light if p["theme"] != "oat" else dark
    if p["layout"] == "photo2":
        img = base64.b64encode((ROOT / "static" / "photos" / p["photo"]).read_bytes()).decode()
        body = f"""
<div class="pin" style="background:url(data:image/jpeg;base64,{img}) center/cover;color:{dark};">
  <div style="background:#faf6ef;padding:62px 64px 52px;border-bottom:12px solid {b};">
    <div class="label" style="color:{b if p["theme"] != "oat" else "#8a6d45"};font-size:26px;">{label}</div>
    <h1 style="font-size:{p.get('size', 92)}px;margin-top:22px;">{head}</h1>
    <p class="sub" style="margin-top:20px;color:#6b665d;font-size:34px;">{sub}</p>
  </div>
  <div style="flex:1"></div>
  <div style="margin:0 0 48px 48px;align-self:flex-start;background:rgba(250,246,239,.94);border-radius:999px;padding:14px 30px 14px 16px;" class="foot">{LOGO}<span style="font-size:30px;">therentednest.co.uk</span></div>
</div>"""
    elif p["layout"] == "photo":
        img = base64.b64encode((ROOT / "static" / "photos" / p["photo"]).read_bytes()).decode()
        body = f"""
<div class="pin" style="background:#faf6ef;color:{dark};">
  <div style="height:880px;background:url(data:image/jpeg;base64,{img}) center/cover;position:relative;">
    <div class="label" style="position:absolute;left:60px;bottom:40px;background:#faf6ef;color:{dark};padding:14px 28px;border-radius:999px;font-size:26px;">{label}</div>
  </div>
  <div style="padding:52px 64px 56px;display:flex;flex-direction:column;flex:1;border-top:14px solid {b};">
    <h1 style="font-size:84px;">{head}</h1>
    <p class="sub" style="margin-top:22px;color:#6b665d;font-size:36px;">{sub}</p>
    <div style="flex:1"></div>
    <div class="foot">{LOGO}<span>therentednest.co.uk</span></div>
  </div>
</div>"""
    elif p["layout"] == "a":
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
    args = sys.argv[1:]
    src, out = ROOT / "tools" / "pins.json", OUT
    if "--file" in args:
        i = args.index("--file"); src = Path(args[i + 1]); del args[i:i + 2]
    if "--out" in args:
        i = args.index("--out"); out = Path(args[i + 1]); del args[i:i + 2]
    pins = json.loads(src.read_text())
    only = set(args)
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 1500})
        for p in pins:
            if only and p["slug"] not in only:
                continue
            page.set_content(render(p), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            page.screenshot(path=str(out / f"{p['slug']}.png"))
            print("rendered", p["slug"])
        browser.close()


if __name__ == "__main__":
    main()
