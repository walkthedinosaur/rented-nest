# Playbook: SEO Specialist weekly run
Trigger: every Wednesday ~10:30 UK.
Inputs: Google Search Console (built-in browser: search.google.com/search-console, property therentednest.co.uk),
ops/seo/target-queries.md, content/guides/, Cloudflare top pages.

Goal: grow free Google traffic by owning narrow, renter-specific UK questions the big publishers ignore.
We cannot outrank Which?/Ideal Home on "best X UK" – target the long tail instead.

Steps
1. Read 00-standing-context.md, ops/seo/target-queries.md and last week's ops/reports/seo-*.md.
1b. Read 05-plan-register.md and do every OPEN item owned by SEO that is due by next Wednesday (tick each in the
   same commit). Also read the latest community-*.md – real renter questions are good brief candidates.
2. Search Console (last 28 days): queries and pages with impressions, clicks, CTR, average position; Pages report for
   indexing problems; Sitemaps status. If not signed in or unreachable, note it and continue with steps 4–6.
2b. Bing Webmaster Tools (built-in browser: bing.com/webmasters, property therentednest.co.uk – verified by import
   from Search Console on 12 Oct 2026): search performance, the AI Performance / Copilot citations report, crawl or
   indexing issues. Note anything Google and Bing disagree on.
3. Quick wins: for pages with impressions but CTR < 2% or position 8–20, rewrite the title (≤60 chars, query first)
   and description (≤155 chars, a clear benefit); add an FAQ section answering the exact queries seen.
4. Write briefs until at least 4 unwritten briefs are waiting in ops/seo/briefs/ (register #6 – the Tue/Thu/Fri
   runs use 5–6 a week; fixed 19 Oct: the old "ONE" let the pipeline run dry). For each, pick a target query from target-queries.md (or a new one found via Google autocomplete / "People also ask"
   checks with WebSearch). Check the current top results: if they're all big publishers answering it well, pick
   another. Write a brief in ops/seo/briefs/<slug>.md (query, intent, angle, outline, internal links, sources) for the
   next content run to write.
5. Internal links: make sure every guide links to at least 2 related guides in its body (not just the auto "More guides"
   block), using descriptive anchor text.
6. Technical check: `python3 build.py`; confirm every guide has one h1, a unique title and description, JSON-LD that
   parses, a hero alt, and appears in sitemap.xml with lastmod. Fix anything broken.
7. Commit and push changes plus ops/reports/seo-YYYY-MM-DD.md (top queries, changes made, next brief). No message
   to Dylan unless Search Console shows a manual action, security issue or indexing problem.
Rules: no keyword stuffing, no AI-spam pages, no buying links, no fake reviews or testing claims; quality over volume.
Never submit anything to Google that needs Dylan's account changes or money.
