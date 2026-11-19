#!/usr/bin/env python3
"""Render Instagram carousel posts (1080x1350 PNG slides) from ops/instagram/posts.json.

Each post: {"slug", "week" (YYYY-MM-DD), "theme" (sage|clay|oat|pine), "photo" (file in static/photos, cover),
            "label", "headline", "sub", "tips": [{"title","text","photo"?}, ...] (3-6; tip photo optional, shown top half), "guide", "caption"}
            optional "story_hook" (one line under "Tap the link below" on the Story; defaults to "sub")
Output: static/social/<week>/<slug>/01.png ... + story.png (1080x1920 Story for a Link sticker) + caption.txt,
        and static/social/index.html (phone-friendly page for Dylan)
Run: python3 tools/make_ig.py [slug ...]            slides + story (needs Playwright + Chromium)
     python3 tools/make_ig.py --story [slug ...]    story.png only (skips posts with a hand-made "story" unless named)
"""
import base64
import datetime as dt
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
    "pop": ("#ff5c8a", "#1d1b3a"),
    "halloween": ("#ff7518", "#16121c"),
}
POP = [("#ff5c8a", "#1d1b3a"), ("#ffb627", "#1d1b3a"), ("#3d6bff", "#ffffff"), ("#c6f432", "#1d1b3a"),
       ("#8b5cf6", "#ffffff"), ("#ff7a3d", "#1d1b3a")]  # theme "pop": bright, one colour per slide
SPOOKY = [("#ff7518", "#16121c"), ("#6b2fd6", "#ffffff"), ("#a3ff3c", "#16121c"), ("#16121c", "#ff7518"),
          ("#e0218a", "#ffffff"), ("#ffd23f", "#16121c")]  # theme "halloween"
CYCLES = {"pop": POP, "halloween": SPOOKY}
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


def tip(i, n, t, a, b, pop=None):
    bg, fg, sub = "#faf6ef", "#2b2a27", "#4a4740"
    if pop:
        bg, fg = pop[(i - 1) % len(pop)]
        sub = fg
    foot = f'''<div class="foot" style="justify-content:space-between;color:{fg};"><span style="display:flex;align-items:center;gap:16px;">{LOGO}The Rented Nest</span><span style="opacity:.75;">{i}/{n}</span></div>'''
    badge_bg, badge_fg, badge_bd = ("#ffffff", "#1d1b3a", "#1d1b3a") if pop else ("#faf6ef", b, a)
    if t.get("photo"):  # photo top, text below
        return wrap(f"""
<div class="s" style="background:{bg};">
  <div style="height:780px;{photo_css(t['photo'])}position:relative;">
    <div class="num" style="position:absolute;left:70px;bottom:-60px;background:{badge_bg};color:{badge_fg};font-size:110px;width:170px;height:170px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:8px solid {badge_bd};transform:rotate(-8deg);">{i}</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;padding:130px 80px 70px;color:{fg};">
    <h2 style="font-size:72px;">{html.escape(t['title'])}</h2>
    <p style="color:{sub};font-size:42px;margin-top:28px;">{html.escape(t['text'])}</p>
    <div style="flex:1"></div>
    {foot}
  </div>
</div>""")
    return wrap(f"""
<div class="s" style="background:{bg};color:{fg};padding:110px 90px 80px;">
  <div style="flex:.6"></div>
  <div class="num" style="background:{badge_bg};color:{badge_fg};width:200px;height:200px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:8px solid {badge_bd};transform:rotate(-8deg);">{i}</div>
  <h2 style="font-size:84px;margin-top:50px;">{html.escape(t['title'])}</h2>
  <p style="color:{sub};font-size:46px;margin-top:40px;">{html.escape(t['text'])}</p>
  <div style="flex:1"></div>
  {foot}
</div>""")


def end(p, a, b):
    return wrap(f"""
<div class="s" style="background:{b};color:#faf6ef;padding:120px 90px 90px;">
  <h2 style="font-size:88px;">The full guide is one tap away</h2>
  <p style="margin-top:44px;opacity:.95;">{html.escape(p.get("end_text", "Prices, retailers and the details are on our website – tap the link in our bio."))}</p>
  <p style="margin-top:36px;opacity:.95;">Save this post for later ↓</p>
  <div style="flex:1"></div>
  <div class="foot" style="background:#faf6ef;color:#2b2a27;border-radius:999px;padding:12px 28px 12px 14px;align-self:flex-start;">{LOGO}<span>therentednest.co.uk</span></div>
</div>""")


def story(p, a, b):
    """1080x1920 Story: cover (no swipe chip) in the top two-thirds, then a call to tap the Link sticker.
    Safe zones: nothing important in the top 120px or bottom 250px (Instagram UI)."""
    bg = photo_css(p["photo"]) if p.get("photo") else f"background:{a};"
    hook = p.get("story_hook") or f"All {len(p['tips'])} ideas + the details in our full guide"
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS}
body {{ height:1920px; background:#faf6ef; }}</style></head><body>
<div style="width:1080px;height:1920px;position:relative;overflow:hidden;background:#faf6ef;">
  <div style="position:absolute;left:0;right:0;top:0;height:10px;background:linear-gradient(90deg,#ff5c8a 0 20%,#ffb627 20% 40%,#3d6bff 40% 60%,#c6f432 60% 80%,#8b5cf6 80%);"></div>
  <div style="position:absolute;left:40px;right:40px;top:130px;height:1110px;border-radius:44px;{bg}box-shadow:14px 14px 0 {b};overflow:hidden;">
    <div style="background:#faf6ef;margin:48px;padding:52px 52px 56px;border-radius:30px;border-bottom:12px solid {b};">
      <div class="label" style="color:{b};font-size:26px;">{html.escape(p['label'])}</div>
      <h1 style="font-size:{min(p.get('size', 96), 92)}px;margin-top:22px;">{html.escape(p['headline'])}</h1>
      <p style="margin-top:22px;color:#6b665d;font-size:34px;">{html.escape(p['sub'])}</p>
    </div>
  </div>
  <div style="position:absolute;left:70px;right:70px;top:1300px;text-align:center;">
    <h2 style="font-size:84px;color:#1d1b3a;">Tap the link below <span style="color:#ff5c8a;">↓</span></h2>
    <p style="margin-top:16px;font-size:36px;line-height:1.3;color:#1d1b3a;font-weight:700;">{html.escape(hook)}</p>
  </div>
  <div style="position:absolute;left:220px;right:220px;top:1555px;height:110px;border:5px dashed #b9b4c9;border-radius:30px;display:flex;align-items:center;justify-content:center;color:#9a95ad;font:700 34px Inter,sans-serif;">place link sticker here</div>
</div></body></html>"""


def main():
    posts = json.loads((ROOT / "ops" / "instagram" / "posts.json").read_text())
    args = sys.argv[1:]
    story_only = "--story" in args
    only = set(a for a in args if not a.startswith("--"))
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        spage = browser.new_page(viewport={"width": 1080, "height": 1920})
        for p in posts:
            if only and p["slug"] not in only:
                continue
            a, b = THEMES[p.get("theme", "sage")]
            d = OUT / p["week"] / p["slug"]
            d.mkdir(parents=True, exist_ok=True)
            if not story_only:
                slides = [cover(p, a, b)]
                slides += [tip(i, len(p["tips"]), t, a, b, CYCLES.get(p.get("theme"))) for i, t in enumerate(p["tips"], 1)]
                slides.append(end(p, a, b))
                for k, s in enumerate(slides, 1):
                    page.set_content(s, wait_until="networkidle")
                    page.wait_for_timeout(250)
                    page.screenshot(path=str(d / f"{k:02d}.png"))
                (d / "caption.txt").write_text(p["caption"].strip() + "\n")
                print("rendered", p["slug"], len(slides), "slides")
            if story_only and p.get("story") and p["slug"] not in only:
                print("kept hand-made story", p["slug"])
                continue
            spage.set_content(story(p, a, b), wait_until="networkidle")
            spage.wait_for_timeout(250)
            spage.screenshot(path=str(d / "story.png"))
            print("rendered", p["slug"], "story.png")
        browser.close()
    write_index(posts)


def write_index(posts):
    """Phone page: newest week first; tap-and-hold to save each slide, caption in a box to copy."""
    blocks = []
    for p in sorted(posts, key=lambda x: (x.get("posted", False), x.get("day", x["week"]))):
        d = OUT / p["week"] / p["slug"]
        if not d.exists():
            continue
        imgs = "".join(f'<img src="{p["week"]}/{p["slug"]}/{f.name}?v={int(f.stat().st_mtime)}" loading="lazy" alt="slide {f.stem}">'
                       for f in sorted(d.glob("[0-9]*.png")))
        st = d / "story.png"
        story_html = (f'<div class="story"><img src="{p["week"]}/{p["slug"]}/story.png?v={int(st.stat().st_mtime)}" loading="lazy" alt="Story">'
                      f'<p><b>Then the Story:</b> Post the carousel, then share a Story with a Link sticker → '
                      f'<a href="{html.escape(p["guide"])}">{html.escape(p["guide"])}</a> (the only clickable link Instagram allows). '
                      'Save this image, add it as a Story, tap the sticker icon → Link, paste the guide URL and drop the sticker on the dashed box.</p></div>'
                      if st.exists() and p.get("guide") else "")
        when = f"Post on {dt.date.fromisoformat(p['day']).strftime('%a %-d %b')}" if p.get("day") else f"Post week of {p['week']}"
        if p.get("posted"):
            when = "Posted ✓"
        blocks.append(f"""<section><h2>{when}: {html.escape(p['headline'])}</h2>
<p class="m">{len(list(d.glob('[0-9]*.png')))} slides – save them in order, post as one carousel.</p>
<div class="row">{imgs}</div>
{story_html}
{f'<p class="m"><a href="{p["week"]}/{p["slug"]}/reel.mp4" download>⬇ Reel version (video, 9:16)</a> – post it as a Reel too, a day or two after the carousel, and add a trending sound in Instagram.</p>' if (d / "reel.mp4").exists() else ""}
<textarea readonly onclick="this.select()">{html.escape(p['caption'].strip())}</textarea></section>""")
    (OUT / "index.html").write_text(f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Instagram posts – The Rented Nest</title><style>
body{{font-family:system-ui,sans-serif;margin:0;padding:16px;background:#faf6ef;color:#2b2a27}}
section{{margin:0 0 40px}} h2{{font-size:18px}} .m{{color:#6b665d;font-size:14px}}
.row{{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory}} .row img{{width:78vw;max-width:360px;scroll-snap-align:start;border-radius:8px}}
.story{{display:flex;gap:12px;align-items:flex-start;margin-top:12px;background:#fff;border-radius:10px;padding:10px}} .story img{{width:34vw;max-width:180px;border-radius:8px;flex:none}} .story p{{margin:0;font-size:14px;word-break:break-word}}
textarea{{width:100%;height:220px;margin-top:10px;font:15px system-ui;padding:10px;border-radius:8px;border:1px solid #ccc;box-sizing:border-box}}
</style></head><body><h1>Instagram posts to schedule</h1>
<p class="m">Next post first. For each post: save the slides (tap and hold), then in Instagram or Meta Business Suite add them as one carousel and paste the caption. Then share the Story image with a Link sticker to the guide – carousel slides can't carry clickable links.</p>
{''.join(blocks)}</body></html>""")


if __name__ == "__main__":
    main()
