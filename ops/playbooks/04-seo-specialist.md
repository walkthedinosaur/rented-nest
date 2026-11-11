# Playbook: SEO Specialist weekly run
Trigger: every Wednesday ~10:30 UK.
Inputs: Google Search Console (built-in browser: search.google.com/search-console, property therentednest.co.uk),
ops/seo/target-queries.md, content/guides/, GoatCounter top pages (https://therentednest.goatcounter.com, public).

Goal: grow free Google traffic by owning narrow, renter-specific UK questions the big publishers ignore.
We cannot outrank Which?/Ideal Home on "best X UK" – target the long tail instead.

Steps
1. Read 00-standing-context.md, ops/seo/target-queries.md and last week's ops/reports/seo-*.md.
1b. Read 05-plan-register.md and do every OPEN item owned by SEO that is due by next Wednesday (tick each in the
   same commit). Also read the latest community-*.md – real renter questions are good brief candidates.
2. Search Console (last 28 days): queries and pages with impressions, clicks, CTR, average position; Pages report for
   indexing problems; Sitemaps status. If not signed in or unreachable, note it and continue with steps 4–6.
2a. URL Inspection (added 21 Oct: the Pages report lagged 9 days and hid unindexed pages): inspect every page published
   or materially updated since the last SEO run. "Unknown to Google" or changed → Request indexing (keep to ≤8 a day;
   requesting is free and changes no settings). Note each result in the report.
   Only log "requested" when Search Console shows its "Indexing requested" confirmation (28 Oct: with the pane hidden the
   live-test dialog closed with no result – log it as "attempted, unconfirmed" and re-try next run). Use the top search box;
   inspect/?id= URLs can't be typed directly (404).
   4 Nov: (a) the request only completes while the browser pane is DISPLAYED – when hidden, the live test's status polls are
   aborted and the dialog closes with no result. Check tabs_context first; if hidden, don't retry – log "not requested – pane
   hidden" and rely on the sitemap (check its "Last read" date). (b) On the inspection page, clicking by ref lands off-target;
   take a screenshot and click by coordinate. Read results with javascript_tool (page text returns the old report).
   11 Nov: a newline typed into the search box does NOT submit – type the URL, then send the Enter key as a separate
   key action. Confirm each result is new (the inspect?id= value in location.search changes per URL) before logging it.
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
