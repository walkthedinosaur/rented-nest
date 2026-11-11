# Playbook: Growth Marketer weekly review
Trigger: every Sunday ~18:00 UK.
Inputs: Tailwind pin analytics, GoatCounter top pages/referrers (API – read-only token in the scheduled-task prompt, never in the repo), Search Console queries (built-in browser,
search.google.com/search-console), guide list in content/guides/, real renter questions (Reddit/Quora).
Output: ops/reports/growth-YYYY-MM-DD.md with a numbered plan the Tue/Thu/Fri runs follow, plus any owned register
items (e.g. #7 welcome emails, #9 community answers) done and ticked.

## A. Read
1. Read 00-standing-context.md, ops/plan/growth-plan-2026q4.md, last week's growth review and the latest ceo-*.md
   (its focus-metric recommendation, if any, goes into this week's plan).
2. Read 05-plan-register.md and list every OPEN item owned by GROWTH that is due by next Sunday. Do them in this run.

## B. Measure
3. Rank pins by outbound clicks, then saves. Then the RECOVERY GATE (growth plan Engine 1): for pins published in the
   last 7 days, average impressions per pin (get_pin_analytics or list_top_pins IMPRESSION) – record it in the report
   and decide: hold 1/day, step up (≥15 two weeks running and clicks rising – add slots with create_timeslot), or drop
   back. Write the decision as a numbered plan item.
   Timeslot rule for any step-up (added 2 Nov 2026): run list_timeslots first and place each new slot so every day's
   times stay between 07:00 and 22:00 UK and at least 60 minutes apart – never two inside the same hour. Re-run
   list_timeslots after the change and record the day's times in the report. Never use rebuild_schedule (it discards
   every existing time). For a drop-back, delete the slots added last.
4. Rank guides by visits and affiliate-link clicks (Awin/Amazon where visible). Mark the top 3 guides for Amazon
   clicks – they matter most for the 3-sale deadline.
5. Search Console: note queries with impressions; flag pages with impressions but low clicks (title/description fixes).

## C. Listen
6. Find 10 open Reddit/Quora renter questions and write link-free draft answers in
   ops/reports/community-YYYY-MM-DD.md (register #9 – never post). Note the exact wording renters use – it feeds
   topics and titles.
   Access (22 Oct 2026): Reddit is blocked for WebFetch and the built-in browser. Use Quora search in the built-in
   browser (https://www.quora.com/search?q=<terms>&type=question; read question links with javascript_tool), plus
   Google "People also ask" for target queries. Skip US/Canada questions.
   Update 10 Nov 2026: Quora now shows a Cloudflare "Just a moment…" check (403) in the built-in browser – agents
   can't pass it. Try Quora once; if blocked, use the MoneySavingExpert forum board via WebFetch:
   https://forums.moneysavingexpert.com/categories/house-buying-renting-selling (and /p2, /p3, /p4 – mostly buyers
   and landlords, pick the tenant threads), then WebFetch each thread for date, facts and the renter's own words.
   Top up with WebSearch for "forums.moneysavingexpert.com tenant <topic>". Record which source was used.
6b. Pinterest Trends (added 19 Oct 2026; URL fixed 10 Nov 2026): the UK region code is **GB+IE**, not GB (country=GB
   gave the blank/"unavailable" pages of 22 Oct and 2 Nov). Most single keywords in the fixed list still say "Keyword
   unavailable for this region" on detail pages, and detail pages show a graph but no % figures. So in the built-in
   browser open the search page filtered by word –
   https://trends.pinterest.com/search/?country=GB%2BIE&keywordsToInclude=<word> – for each filter word in
   ops/seo/pinterest-trends-keywords.md (wait ~5 s, read the table with javascript_tool: keyword | weekly | monthly |
   yearly). It lists only GROWING keywords containing that word; a fixed-list keyword that doesn't appear is "not
   shown", not falling. (Detail pages, if needed: /detail/?country=GB%2BIE&terms=<kw>&dateRange=365D&aggregationLevel=2.)
   Also check the fixed list plus up to 3 new candidates from steps 5–6. For each, record
   in a "Pinterest Trends" table in this week's growth review: keyword, weekly/monthly/yearly change as shown, and
   rising/flat/falling. Only record numbers you can see on the page – never estimate. Add any keyword that shows as
   rising to the fixed list. If Trends doesn't load (blank page, signed out, unreachable), write "Trends: not
   checked – <reason>" and carry on; the CEO report flags it if it happens two weeks running.

## D. Decide
7. List 3–5 candidate new topics from Search Console queries, the community questions and the Pinterest Trends table
   (step 6b). For each,
   note the evidence (impressions, how often it's asked, gap vs existing guides). Pick the best 1–2 – don't just take
   the first idea.
8. Decide the pin mix: which guides get new pins (winners by outbound clicks get more; Amazon-click guides first if
   the CEO report says sales are behind), plus any title/description rewrites, and whether volume can step up per
   the growth plan.

## E. Write
9. Write ops/reports/growth-YYYY-MM-DD.md: top/bottom performers, the plan for the week (numbered, specific, one
   action per line), the chosen topics with their evidence, and any approved Awin retailer whose links should be
   added. Add a register row for any new commitment that has a date.
10. Commit and push. No message to Dylan (the CEO report carries it).

## Instagram (added 30 Oct 2026)
- Record weekly: followers, posts published, Instagram visits in GoatCounter (utm_source=instagram, l.instagram.com referrer), and which post's guide got the most Instagram visits. Recommend next week's 3 Instagram topics (Mon/Wed/Fri) in the plan – favour what drove visits and anything seasonal.
- Site also links to Instagram/Pinterest from every footer and a follow line under each guide (utm_source=site) – note if site→Instagram clicks appear.
