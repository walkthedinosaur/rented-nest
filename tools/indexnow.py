#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam, Naver, Yep...) with every URL in the sitemap, or the URLs given.
Run after a push once the site is live:  python3 tools/indexnow.py [url ...]"""
import json, re, sys, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
KEY = (ROOT / "tools" / "indexnow_key.txt").read_text().strip()
HOST = "therentednest.co.uk"
urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "docs" / "sitemap.xml").read_text())
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow", r.status, len(urls), "urls")
except Exception as e:
    print("IndexNow failed:", e)
