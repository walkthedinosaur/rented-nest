# Growth plan Q4 2026 – agreed at the board meeting, 12 Oct 2026
Board doc: https://claude.ai/code/artifact/90711058-0ed7-4f5e-ae04-849400527272
Every scheduled agent reads this and works its part. The CEO report tracks each engine weekly.

## Engine 1 – Pinterest (Content + Growth)
- **Volume – RESET 30 Oct 2026 (board meeting, approved by Dylan).** The 8/day ramp (from 20 Oct) was followed by
  Pinterest all but stopping distribution: every new pin since ~20 Oct got 2–3 impressions in total, outbound clicks
  went 19 (11–15 Oct) → 6 (16–23 Oct) → 1 (24–28 Oct). Tailwind's own guidance for NEW accounts is 3–5 fresh pins a
  WEEK and a 7-day gap between pins to the same URL; we were at ~56/week with no gap (10 pins to one guide in 14 days).
  **Now: 1 pin a day (7 a week), 1 Tailwind slot a day at ~19:00.** 51 queued pins were moved back to drafts – reuse
  them first (scheduling a draft costs 1 credit).
- **Spacing rule (hard):** never schedule a pin whose destination page (URL without the #anchor) has a pin published
  or queued in the last/next 7 days. Check tools/tailwind_queue.json and list_posts (queued + sent, last 7 days)
  before every create_post/schedule_post. Tailwind's own Pin Spacing (7 days) to be switched on by Dylan (register #53).
- **Recovery gate (Growth review, weekly):** average impressions per pin in its first 7 days, for pins published that
  week. Step up to 2/day only if it is ≥15 for two weeks running AND outbound clicks are rising; to 3/day after two
  more good weeks. Never above 3/day before the January review. Drop back to 1/day if it falls under 5.
- No engagement swaps or bulk saving of other creators' pins (Tailwind Turbo/"Quick saves") – Pinterest treats
  artificial engagement as spam. Pause everything and tell Dylan if Pinterest shows any warning.
- Variety: 3–5 different designs per guide (different photo, headline angle, keyword, anchor). Never reuse an image.
- Boards: grow from 6 to 12–15 keyword-named boards (e.g. "Condensation & Damp Fixes UK", "Small Bedroom Storage
  Ideas", "Renting Tips UK", "Black Friday Home Deals UK", "Student House Share Ideas"), 2 per content run until done.
- Topics: pick new guides from Pinterest Trends + Search Console.
- Pinterest Ads test: DECLINED by Dylan (12 Oct 2026). Do not propose paid ads again unless organic data shows a clear case.

## Engine 2 – Search (SEO)
- Bing Webmaster Tools verified 12 Oct 2026 (imported from Search Console). Bing/IndexNow live: after every publish run `python3 tools/indexnow.py <new/changed URLs>` (key in tools/).
- Trust layer live (About + /editorial-policy.html). Keep "last reviewed" dates current. Never invent authors.
- Cluster: 5–6 renter-question pages a week (Tue + Fri content runs, plus Thursday "renter questions" run added 15 Oct) from ops/seo/target-queries.md (damp, deposits, storage rules, Renters'
  Rights Act changes from 1 May 2026) – target 30–50 pages by mid-January. Answer first, sources, next steps. No
  legal advice – link Shelter / Citizens Advice / GOV.UK.
- Monthly re-check (first run of each month): /guides/renters-rights-act-what-changed-uk.html and /guides/ask-landlord-for-a-pet-england.html against GOV.UK (database roll-out, ombudsman, Awaab's Law PRS consultation closes 18 Dec 2026, Decent Homes) – update facts and the "Last reviewed" date.
- Link magnets: (a) running-cost calculator heated airer v tumble dryer v dehumidifier (Ofgem cap rate; update when
  the January 2027 cap is announced, expected late Nov) – LIVE 15 Oct at /tools/drying-heating-cost-calculator.html (default 26.32p/kWh, Oct–Dec 2026 cap; update the default rate, the 54.83p standing charge line and the worked examples when the Jan–Mar 2027 cap is announced); (b) "Renter winter damp" data page from the
  English Housing Survey – by 2 Nov.

## Engine 3 – Owned audience (LIVE 12 Oct 2026 – Kit free plan; end-to-end test passed 12 Oct, Dylan)
- Kit inline form 10035184 "Winter damp & warmth checklist" (embed uid 20b07e3af6), double opt-in, confirm redirects to
  /checklists/winter-damp-warmth.html (PDF download). Embedded on dehumidifiers, heated airers, stay-warm and Black Friday guides.
- Checklist source: tools/checklists/*.html -> `python3 tools/checklists/render.py` -> static/checklists/*.pdf.
- Footer postal address: Kit's own mailing address (Dylan's choice, 12 Oct). Kit time zone: London, default send 8am.
- Next: draft a 2–3 email welcome sequence in Kit (drafts only) for Dylan to review before it's switched on.
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
