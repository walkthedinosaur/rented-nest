# Playbook: Content production run
Trigger: Tuesday and Friday ~10:30 UK.
Inputs: latest ops/reports/growth-*.md plan, tools/pins.json, Tailwind schedule.

Steps
1. Read 00-standing-context.md, the latest growth review plan and any unwritten briefs in ops/seo/briefs/ (an SEO brief takes priority for the one new guide per run; mark it [x] in ops/seo/target-queries.md when published).
2. Check queue: Tailwind get_schedule for the next 7 days and get_account_usage. Target: queue covers at least the
   next 5 days at the allowed daily volume. Work out how many pins to make: enough to fill every open slot to ~6 days ahead – at 8/day that is ~26–30 per run,
   at 10/day ~33–37 (fixed 19 Oct: the old "8–15" could not keep up with the approved volume). Follow the latest growth
   review's per-guide mix – winners get more pins.
3. Write up to 2 new pages per run (SEO briefs and plan topics first – target 3–4 a week), write it in the house format (see existing guides): 900–1,400
   words, 4–5 h2 sections each with a section photo, 8–14 .idea cards with Amazon shortcodes, renter-specific advice,
   price bands sourced, a Sources list. Add a "Bigger buys" angle where natural. Cross-link from 1–2 related guides.
4. If an Awin retailer has been approved (ops/awin-applications.xlsx), add its link (deep link generated in Awin –
   if that needs the browser and it's unavailable, skip and note it) alongside Amazon in the matching guides, with
   rel="sponsored nofollow noopener".
5. Pins: add entries to tools/pins.json (slug v2-…, layout photo2, unique photo, headline ≤7 words, sub line, label,
   guide URL with a #anchor that exists, board, title ≤100 chars, description starting "Ad – " ≤500 chars, alt).
   Render with tools/make_pins.py, view a contact sheet to check text fits and nothing overlaps.
6. `python3 build.py`, commit, push; wait ~70s, check the new pages and pin PNGs return 200, then run `python3 tools/indexnow.py <new and changed page URLs>`.
7. Schedule each pin: Tailwind create_post with mediaUrl https://therentednest.co.uk/pins/<slug>.png, title,
   description, url, boardId, altText, useNextOpenSlot:true. Record post IDs in tools/tailwind_queue.json.
8. Append a 3-line run log to ops/reports/content-log.md (date, guides added/changed, pins scheduled, credits left).
   No message to Dylan unless something failed or credits < 40.
Output: new pins queued (and any new guide live).
