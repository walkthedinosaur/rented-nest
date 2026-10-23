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

## B. Register items
4. Do each due CONTENT item from step 2 (e.g. timeslots, boards, guide fixes, Awin gaps). Tick each in the register
   in the same commit as the work ("DONE <date> – what was done"). If one can't be done, write why in its Status.

## C. Pages (up to 2 per run – SEO briefs and plan topics first, target 3–4 a week across all runs)
5. Pick the topics: unwritten SEO briefs first (PRIORITY lowest number first), then the growth review's topics.
   Skip anything the Thursday run already published (check content/guides/ and the [x] marks).
6. Research: gather the facts and sources for each page. Price bands only from a source checked today, written as
   "typically around £X–£Y at the time of writing – check current price".
7. Photos: one unique Unsplash photo per h2 section, downloaded into static/photos/, IDs added to CREDITS.md.
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

## E. Pins
11. Work out how many pins to make: Tailwind get_schedule (next 7 days) and get_account_usage. Make enough to fill
    every open slot to ~6 days ahead – at 8/day ~26–30 per run, at 10/day ~33–37. Then check credits: credits left
    must cover (days to the reset × daily volume). If not, make fewer, keep the rest for the most-clicked guides, and
    note it in the log.
12. Choose the mix: follow the latest growth review's per-guide split – winners (outbound clicks) get the most pins;
    new pages get 2–3 each.
13. Add the entries to tools/pins.json: slug v2-…, layout photo2, unique photo, headline ≤7 words, sub line, label,
    guide URL with a #anchor that exists, board, title ≤100 chars, description starting "Ad – " ≤500 chars, alt.
14. Render with tools/make_pins.py and view a contact sheet: text fits, nothing overlaps. Fix and re-render failures.

## F. Publish and schedule
15. `python3 build.py`, commit, push.
16. Wait ~70s, then check every new page and pin PNG returns 200.
17. Run `python3 tools/indexnow.py <new and changed page URLs>`.
18. Schedule each pin: Tailwind create_post with mediaUrl https://therentednest.co.uk/pins/<slug>.png, title,
    description, url, boardId, altText, useNextOpenSlot:true. Record post IDs in tools/tailwind_queue.json.

## G. Log
19. Append a 3-line run log to ops/reports/content-log.md: (1) pages added/changed and register items ticked,
    (2) pins scheduled and queue end date, (3) credits left and any playbook fix made this run.
20. Commit and push. No message to Dylan unless something failed or credits < 40.
