# Playbook: Content production run
Trigger: Tuesday and Friday ~10:30 UK.
Inputs: latest ops/reports/growth-*.md plan, ops/playbooks/05-plan-register.md, unwritten briefs in ops/seo/briefs/,
tools/pins.json, Tailwind schedule and usage.
Output: new pins queued to ~6 days ahead, up to 2 new pages live, owned register items done and ticked, one log entry.
(Restructured 19 Oct 2026: one action per step, so nothing gets skipped inside a long step. Same rules as before.)

## A. Read
1. Read 00-standing-context.md and ops/plan/growth-plan-2026q4.md.
2. Read 05-plan-register.md. List every OPEN item owned by CONTENT that is due by the next content run – these come
   first, before the routine work below.
3. Read the latest growth review plan (its numbered list is this run's to-do list) and any unwritten briefs in
   ops/seo/briefs/.

2a. Watchdog (added 28 Oct): check the last 8 days have a ops/reports/ceo-*.md and a ops/reports/growth-*.md, and
   that Tailwind credits and the queue look sane. If either report is missing, send Dylan ONE line: "<report> didn't
   run – check the scheduled task is enabled". (26 Oct: CEO + growth tasks were auto-disabled for 9 days when the
   computer was offline and nobody noticed.)

## B. Register items
4. Do each due CONTENT item from step 2 (e.g. timeslots, boards, guide fixes, Awin gaps). Tick each in the register
   in the same commit as the work ("DONE <date> – what was done"). If one can't be done, write why in its Status.

## C. Pages (up to 2 per run – SEO briefs and plan topics first, target 3–4 a week across all runs)
5. Pick the topics: unwritten SEO briefs first (PRIORITY lowest number first), then the growth review's topics.
   Skip anything the Thursday run already published (check content/guides/ and the [x] marks).
6. Research: gather the facts and sources for each page. Price bands only from a source checked today, written as
   "typically around £X–£Y at the time of writing – check current price".
7. Photos: one unique Unsplash photo per h2 section, downloaded into static/photos/, IDs added to CREDITS.md.
   If unsplash.com can't be fetched (cloud runs, 20 Nov 2026: WebFetch permission prompt with nobody to answer), don't
   fetch it another way: for pins use photos already in static/photos that no pin or Instagram post has used (check
   tools/pins.json + ops/instagram/posts.json by script); a new page waits for a run that can fetch Unsplash.
   24 Nov 2026: in the cloud run EVERY WebFetch failed the same way (retailer pages too), so live-price checks (#13)
   and photo-card upgrades (#97) can't be done there: keep existing date stamps as they are (never re-stamp unchecked
   prices), do the text-only parts, log it, and tell Dylan once if a dated deal page can't be re-checked.
8. Write each page in the house format (see existing guides): 900–1,400 words, answer first, 4–5 h2 sections each
   with its section photo, 8–14 .idea cards with Amazon shortcodes, renter-specific advice, a Sources list.
   Add a "Bigger buys" angle where natural.
9. Cross-link each new page from 1–2 related guides. Mark its query [x] in ops/seo/target-queries.md.

## D. Affiliate links
10. For each Awin retailer marked Approved in ops/awin-applications.xlsx that isn't yet linked where it fits, add its
    link (deep link generated in Awin – if that needs the browser and it's unavailable, skip and note it) alongside
    Amazon in the matching guides, with rel="sponsored nofollow noopener".
    Test the destination page first. Homebase and La Redoute show a bot check (403) to cloud runs, so their new
    destination URLs can't be verified here – never guess a category URL; hand it to a run with the built-in browser
    (added 23 Oct 2026).
    Cloud runs (from 13 Nov 2026) can't WebFetch an awin1.com link (permission prompt, nobody to answer): find the
    destination via WebSearch, confirm it's live with WebFetch, add the link, and leave the click-through test to the
    next run with the built-in browser (note it in register #18).

## E. Pins
11. Pin volume (reset 30 Oct – read growth-plan Engine 1): fill only the OPEN slots in the next 4 days (1 slot a day
    at present, so Tue run ≤4 pins, Fri run ≤3). Make every pin FRESH in a v3 style (step 13) –
    do NOT schedule the old Tailwind drafts: they are all the same photo2 template, and Dylan asked on 3 Nov 2026 for
    real variety. A fresh pin costs the same 1 credit as scheduling a draft. Use the growth review's pin order for
    WHICH page and hook, but render a new v3 design for it. Leave the old drafts unscheduled (don't delete them). Never add timeslots; the Growth review owns any step-up.
    If an unschedule_post (or any Tailwind write) is refused, stop filling at the last day that still has only one pin –
    useNextOpenSlot can't skip a slot, so scheduling more would double up a day. Log it, message Dylan the postIds to
    unschedule by hand, and leave the rest of the plan to the next run (added 3 Nov 2026).
12. Choose the mix: winners by outbound clicks first (gift guides in Nov–Dec), then new pages – but every pin must
    pass the 7-day spacing rule (no other pin to the same page, without #anchor, published or queued within 7 days
    either side; check tools/tailwind_queue.json + list_posts queued/sent). One pin per page per week at most.
13. Add the entries to tools/pins.json: slug v3-…, a v3 layout + palette + font (see tools/make_pins.py docstring:
    overlay, split, poster, checklist, frame, numbered, arch, duo, script; 12 palettes; 6 fonts), unique photo,
    headline ≤7 words, sub line, label, guide URL with a #anchor that exists, board, title ≤100 chars, description
    starting "Ad – " ≤500 chars, alt. Rotate hard (changed 3 Nov 2026 – Dylan: "the pins all look the same"):
    no two pins in a row share a layout, palette or font; no layout or palette more than twice per run; match the
    palette to the topic where it helps (berry/forest for Christmas, mustard/terracotta for Black Friday, teal/mint
    for damp, navy/charcoal for renting rules) but never the same one twice running. Checklist pins (3–4 short
    points) and numbered pins ("7 ways…") are the save-friendly formats – use at least one per run.
13a. Search wording (added 16 Nov 2026 – Dylan approved; Pinterest reach for new pins is ~0.5 impressions, so pins
    must be found through Pinterest SEARCH, not the feed). For every pin pick ONE exact UK search phrase people type
    (e.g. "secret santa ideas uk", "stocking fillers under 10", "christmas gifts for renters", "black friday
    dehumidifier deals", "christmas decorations rented flat") – from Pinterest Trends / the growth review / the
    guide's target query, never invented stats. Put that phrase, word for word: (1) at the START of the pin title,
    (2) in the first sentence of the description straight after "Ad – ", (3) in the headline or sub line on the image
    where it reads naturally, (4) in the alt text. Add 2–3 close variants later in the description in plain sentences
    (no hashtag lists). The board must match the phrase's topic. No two pins in one run use the same lead phrase.
    Log each pin's lead phrase in tools/pins.json as "keyword" so the growth review can compare phrases.
14. Render with tools/make_pins.py, then run `python3 tools/check_pin_variety.py <new slugs>` – it must pass. View a
    contact sheet of the batch next to the previous run's pins: text fits, nothing overlaps, and the batch looks
    clearly different from last time. Fix and re-render failures.

## F. Publish and schedule
15. `python3 build.py`, commit, push.
16. Wait ~70s, then check every new page and pin PNG returns 200.
17. Run `python3 tools/indexnow.py <new and changed page URLs>`.
18. Schedule the NEW pins in one batch (added 2 Nov 2026): Tailwind create_posts (account 1658314) with one entry per
    pin – mediaUrl https://therentednest.co.uk/pins/<slug>.png, title, description, url, boardId, altText,
    useNextOpenSlot:true. Poll get_post_batch every ~10s until completed; record each created postId in
    tools/tailwind_queue.json. For failed entries: if the reason says the Pin may exist, check list_posts first; then
    resend only those entries with retryOfBatchId. Never resend a whole batch to "retry" – an identical batch within
    7 days returns the original, and a changed one double-posts. (Drafts from step 11 still go through schedule_post.)

## F2. Instagram (Fridays only)
18a. Follow ops/playbooks/07-instagram.md – make next week's 3 Instagram carousel posts.

## G. Log
19. Append a 3-line run log to ops/reports/content-log.md: (1) pages added/changed and register items ticked,
    (2) pins scheduled and queue end date, (3) credits left and any playbook fix made this run.
20. Commit and push. No message to Dylan unless something failed or credits < 40.

## Visual standard (19 Nov 2026)
Owner feedback: guide pages felt plain and text-heavy when arriving from Pinterest. build.py now gives guides a
magazine layout (split title/hero header on desktop, wide photos, cards in a 2-column grid, photo related-guides) and
styles four markup blocks. Use them in new and refreshed guides – especially gift/product roundups:
- Product card with photo: `<div class="idea"><img class="idea-img" src="/photos/<file>.jpg" alt="…" loading="lazy"
  width="800" height="800"><span class="tag">Clever buy</span><h3>Name</h3><p>Why…</p><p class="shop">{{amazon:…|Shop
  on Amazon UK}}</p></div>`. img and tag optional (text-only cards still look fine). build.py wraps the photo and adds an
  "Illustrative photo" label automatically – use lifestyle photos, never imply the photo is the exact product.
  Consecutive cards form a 2-column grid on desktop; an odd last card (or a lone card) goes wide with photo left.
  Keep h3 text stable – Pinterest pins link to the #anchor generated from it (or set `<h3 id="x">` explicitly).
- Top-picks strip (4–8 picks, right after the intro on roundups): `<div class="picks"><a class="pick"
  href="#<h3-anchor>"><img src="/photos/…" alt="…" loading="lazy" width="600" height="600"><span>Short name</span></a>
  …</div>`. Swipe row on mobile, numbered grid on desktop (4 = 4-up, 5 = 5-up, 6 = 3-up/6-up, 7–8 = 4-up).
- Gallery (2–4 photos under an h2, for mood/room inspiration): `<div class="gallery"><img …><img …></div>` – mosaic.
- Tip callout: `<aside class="tip"><strong>Renter tip</strong> …</aside>` – one or two per guide, for renter-specific advice.
Rule of thumb: every h2 section gets at least one visual (section-img, gallery or photo cards); never three text-only
screens in a row on mobile. Always set width/height and loading="lazy" on body images; keep alt text descriptive.

## Product picks standard (19 Nov 2026)
Owner feedback (19 Nov): guides linked to products that "aren't very interesting". Every new or refreshed product guide
uses the markup contract in "Visual standard" above (photo cards, picks strip, gallery, tip callout), with at least one
card photo per two cards and every photo unique site-wide. Where the guide's angle and budget allow, at least 30% of the
picks come from the current novel-products list (ops/seo/novel-products-YYYY-MM.md – rows marked V only; budget guides
use only items seen at or under the budget). The Content run re-verifies that list on the first run of each month: open
each product's UK retailer/manufacturer page again, update price/status, mark anything gone "NOT VERIFIED", add 5+ new
finds, and save as a new month's file. Never use Amazon or retailer product images – lifestyle photos of the product
TYPE from Unsplash only.
