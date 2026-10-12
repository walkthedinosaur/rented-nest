#!/usr/bin/env python3
"""Build The Rented Nest static site.

Content lives in content/ as HTML fragments with a small header block:

    title: Page title
    description: One-line summary for search and Pinterest
    kind: guide | page | home
    card: sw-sage            (guides only: card colour)
    date: 2026-10-10         (guides only)
    ---
    <p>Body HTML...</p>

Run `python3 build.py`; output goes to docs/, which GitHub Pages serves.
"""
import html
import json
import re
import shutil
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"
SITE = "https://therentednest.co.uk"
LOGO = (ROOT / "static" / "logo.svg").read_text()

DISCLOSURE = (
    '<p class="disclosure"><strong>Ad</strong> – this guide contains affiliate links. '
    'If you buy through them we may earn a small commission, at no extra cost to you. '
    '<a href="/disclosure.html">How we make money</a>.</p>'
)


AMAZON_TAG = "therentednest-21"
SHORTCODE = re.compile(r"\{\{amazon:([^|}]+)\|([^}]+)\}\}")


def amazon_link(m):
    query = urllib.parse.quote_plus(m.group(1).strip())
    label = html.escape(m.group(2).strip())
    url = f"https://www.amazon.co.uk/s?k={query}&tag={AMAZON_TAG}"
    return f'<a href="{url}" rel="sponsored nofollow noopener" target="_blank">{label} →</a>'


def parse(path):
    raw = SHORTCODE.sub(amazon_link, path.read_text())
    head, body = raw.split("\n---\n", 1)
    meta = {}
    for line in head.strip().splitlines():
        key, _, val = line.partition(":")
        meta[key.strip()] = val.strip()
    meta["body"] = body
    rel = path.relative_to(CONTENT).with_suffix(".html")
    meta["url"] = "/" + str(rel).replace("index.html", "")
    meta["out"] = OUT / rel
    return meta


def page(meta, inner):
    title = meta["title"]
    full_title = title if meta.get("kind") == "home" else f"{title} | The Rented Nest"
    desc = html.escape(meta.get("description", ""))
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{desc}">
<meta name="p:domain_verify" content="9048703ba3079bac67a31789bf0f19ed"/>
<link rel="canonical" href="{SITE}{meta['url']}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{'article' if meta.get('kind') == 'guide' else 'website'}">
<meta property="og:url" content="{SITE}{meta['url']}">
<meta property="og:site_name" content="The Rented Nest">
{f'<meta property="og:image" content="{SITE}/photos/{meta["hero"]}">' if meta.get("hero") else f'<meta property="og:image" content="{SITE}/profile-picture.png">'}
{jsonld(meta)}
<link rel="icon" href="/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/">{LOGO}<span>The Rented Nest</span></a>
  <nav class="nav" aria-label="Main">
    <a href="/#guides">Guides</a>
    <a href="/about.html">About</a>
    <a href="/disclosure.html">How we make money</a>
  </nav>
</div></header>
<main>
{inner}
</main>
<footer class="site-footer"><div class="wrap">
  <div>© 2026 The Rented Nest · Small-space ideas for UK renters<br>As an Amazon Associate we earn from qualifying purchases.</div>
  <nav aria-label="Footer">
    <a href="/about.html">About</a>
    <a href="/disclosure.html">Affiliate disclosure</a>
    <a href="/editorial-policy.html">Editorial policy</a>
    <a href="/privacy.html">Privacy</a>
  </nav>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "20c59278defa48748115ad49217b7e0d"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""


GROUPS = [("dehumidifier", "airer", "warm"), ("christmas", "santa", "gift"), ("storage", "living-room")]


def group_of(url):
    for i, keys in enumerate(GROUPS):
        if any(k in url for k in keys):
            return i
    return -1


def jsonld(meta):
    org = {"@type": "Organization", "name": "The Rented Nest", "url": SITE + "/",
           "logo": SITE + "/profile-picture.png"}
    if meta.get("kind") == "guide":
        data = [{
            "@context": "https://schema.org", "@type": "Article",
            "headline": meta["title"], "description": meta.get("description", ""),
            "datePublished": meta.get("date", ""), "dateModified": meta.get("updated", meta.get("date", "")),
            "image": [f"{SITE}/photos/{meta['hero']}"] if meta.get("hero") else [],
            "author": org, "publisher": org,
            "mainEntityOfPage": SITE + meta["url"],
        }, {
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": meta["title"], "item": SITE + meta["url"]},
            ],
        }]
    elif meta.get("kind") == "home":
        data = [dict(org, **{"@context": "https://schema.org"}),
                {"@context": "https://schema.org", "@type": "WebSite", "name": "The Rented Nest", "url": SITE + "/"}]
    else:
        return ""
    return "\n".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in data)


def related_block(g, guides):
    mine = group_of(g["url"])
    others = [o for o in guides if o["url"] != g["url"]]
    others.sort(key=lambda o: (group_of(o["url"]) != mine, o.get("date", "")), reverse=False)
    same = [o for o in others if group_of(o["url"]) == mine]
    rest = [o for o in others if group_of(o["url"]) != mine]
    pick = (same + rest)[:3]
    items = "\n".join(f'<li><a href="{o["url"]}">{html.escape(o["title"])}</a> – {html.escape(o["description"])}</li>' for o in pick)
    return f'<section class="related"><h2>More guides for renters</h2><ul>{items}</ul></section>'


def anchor_ids(body):
    def add(m):
        slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"^\d+\.\s*", "", m.group(1)).lower()).strip("-")
        return f'<h3 id="{slug}">{m.group(1)}</h3>'
    return re.sub(r"<h3>([^<]+)</h3>", add, body)


def render_guide(g, guides=()):
    hero = (f'<img class="hero" src="/photos/{g["hero"]}" alt="{html.escape(g.get("hero_alt", g["title"]))}" width="1200" height="800" loading="eager">'
            if g.get("hero") else "")
    return f"""<article><div class="narrow">
<p class="eyebrow">Guide</p>
<h1>{html.escape(g['title'])}</h1>
<p class="standfirst">{html.escape(g['description'])}</p>
{DISCLOSURE}
{hero}
{anchor_ids(g['body'])}
{related_block(g, guides)}
</div></article>"""


def render_page(p):
    return f"""<article><div class="narrow">
<h1>{html.escape(p['title'])}</h1>
{p['body']}
</div></article>"""


def render_home(home, guides):
    cards = "\n".join(
        f"""<a class="card" href="{g['url']}">
  <div class="swatch {g.get('card', 'sw-sage')}"{f' style="background:url(/photos/{g["hero"]}) center/cover"' if g.get("hero") else ""}><span>{html.escape(g.get('label', 'Guide'))}</span></div>
  <div class="body"><h3>{html.escape(g['title'])}</h3><p>{html.escape(g['description'])}</p></div>
</a>"""
        for g in guides
    )
    return f"""{home['body']}
<section class="wrap" id="guides">
<h2 class="section-title">Latest guides</h2>
<div class="grid">
{cards}
</div>
</section>"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "static", OUT, dirs_exist_ok=True)

    items = [parse(p) for p in sorted(CONTENT.rglob("*.html"))]
    guides = sorted((i for i in items if i.get("kind") == "guide"),
                    key=lambda g: g.get("date", ""), reverse=True)

    for item in items:
        kind = item.get("kind")
        if kind == "home":
            inner = render_home(item, guides)
        elif kind == "guide":
            inner = render_guide(item, guides)
        else:
            inner = render_page(item)
        item["out"].parent.mkdir(parents=True, exist_ok=True)
        item["out"].write_text(page(item, inner))

    (OUT / "CNAME").write_text("therentednest.co.uk\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        "# Search and AI answer engines are welcome\n"
        "User-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n")
    urls = "\n".join(
        f"  <url><loc>{SITE}{i['url']}</loc>"
        + (f"<lastmod>{i.get('updated', i['date'])}</lastmod>" if i.get("date") else "")
        + "</url>" for i in items)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n"
    )
    print(f"Built {len(items)} pages ({len(guides)} guides) into {OUT}")


if __name__ == "__main__":
    main()
