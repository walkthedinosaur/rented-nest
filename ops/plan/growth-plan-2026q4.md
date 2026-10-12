# Growth plan Q4 2026 – agreed at the board meeting, 12 Oct 2026
Board doc: https://claude.ai/code/artifact/90711058-0ed7-4f5e-ae04-849400527272
Every scheduled agent reads this and works its part. The CEO report tracks each engine weekly.

## Engine 1 – Pinterest (Content + Growth)
- Volume (approved by Dylan 12 Oct): 5/day now; **8/day from Mon 19 Oct; 10/day from Mon 2 Nov** (= ~300 credits/month,
  no extra cost). The first content run on/after each date adds Tailwind timeslots (create_timeslot, spread across
  07:00–22:00 UK, never two within 60 min) to reach the new daily count. Above 10/day needs Dylan (more credits).
  Pause increases if Pinterest shows any spam warning.
- Variety: 3–5 different designs per guide (different photo, headline angle, keyword, anchor). Never reuse an image.
- Boards: grow from 6 to 12–15 keyword-named boards (e.g. "Condensation & Damp Fixes UK", "Small Bedroom Storage
  Ideas", "Renting Tips UK", "Black Friday Home Deals UK", "Student House Share Ideas"), 2 per content run until done.
- Topics: pick new guides from Pinterest Trends + Search Console.
- Pinterest Ads test: DECLINED by Dylan (12 Oct 2026). Do not propose paid ads again unless organic data shows a clear case.

## Engine 2 – Search (SEO)
- Bing Webmaster Tools verified 12 Oct 2026 (imported from Search Console). Bing/IndexNow live: after every publish run `python3 tools/indexnow.py <new/changed URLs>` (key in tools/).
- Trust layer live (About + /editorial-policy.html). Keep "last reviewed" dates current. Never invent authors.
- Cluster: 3–4 renter-question pages a week from ops/seo/target-queries.md (damp, deposits, storage rules, Renters'
  Rights Act changes from 1 May 2026) – target 30–50 pages by mid-January. Answer first, sources, next steps. No
  legal advice – link Shelter / Citizens Advice / GOV.UK.
- Link magnets: (a) running-cost calculator heated airer v tumble dryer v dehumidifier (Ofgem cap rate; update when
  the January 2027 cap is announced, expected late Nov) – by 26 Oct; (b) "Renter winter damp" data page from the
  English Housing Survey – by 2 Nov.

## Engine 3 – Owned audience (LIVE 12 Oct 2026 – Kit free plan)
- Kit inline form 10035184 "Winter damp & warmth checklist" (embed uid 20b07e3af6), double opt-in, confirm redirects to
  /checklists/winter-damp-warmth.html (PDF download). Embedded on dehumidifiers, heated airers, stay-warm and Black Friday guides.
- Checklist source: tools/checklists/*.html -> `python3 tools/checklists/render.py` -> static/checklists/*.pdf.
- NO broadcasts/sequences until Dylan resolves the postal address Kit requires in email footers (not his home address).
- Never store Kit API keys or webhook URLs in this repo.
- Next: "Move-out deposit checklist" lead magnet for storage/decor guides. Price-drop alert sign-up later.

## Engine 4 – Short video (blocked until Dylan sets up Buffer + IG/TikTok/YouTube and sends an API key)
- Prepare 3 test slideshow videos (python/ffmpeg from our photos + copy, "Ad" label first). 60-day test once live.

## Engine 5 – Revenue per visitor
- Black Friday page live (/guides/black-friday-deals-renters-uk.html). From 20 Nov: daily content runs add live
  deals (only real, checked prices with date stamps). January sales page by 22 Dec.
- On Awin approvals: swap/add retailer links; draft discount-code requests (Meaco, Ebac, Beldray, Pro Breeze) for
  Dylan to send.
- Sovrn Commerce: apply when ~20 guides are live (Dylan approves terms).
- Weekly: 10 open Reddit/Quora renter questions with link-free draft answers in ops/reports/community-*.md (Dylan
  posts only if he wants; agents never post under a persona).
