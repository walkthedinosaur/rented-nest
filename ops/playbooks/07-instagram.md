# 07 – Instagram posts (part of the Friday content run)

Account: @therentednestonline (https://www.instagram.com/therentednestonline/), created by Dylan 30 Oct 2026.
Agents CANNOT post to Instagram (no connector; publishing on Dylan's behalf needs his yes each time). So agents MAKE the
posts and Dylan schedules them (Meta Business Suite or Instagram's own scheduler) – about 10 minutes a week.
Bio link: https://therentednest.co.uk/links?utm_source=instagram (page /links lists featured + 12 newest guides; the
featured list is content/links.html – keep it to the 4 most timely guides).

## Volume (new account – same lesson as Pinterest, 30 Oct)
- 3 carousel posts a week, no more, until the Growth review shows Instagram visits growing (GoatCounter campaign
  utm_source=instagram). Never post the same guide twice in 14 days.

## Steps (Friday content run, after the pins)
1. Pick 3 guides for next week: one gift/seasonal (Nov–Dec), one renter problem (damp, cold, deposit, rules), one
   home/decor idea. Skip any guide used on Instagram in the last 14 days (check ops/instagram/posts.json).
2. For each, add an entry to ops/instagram/posts.json: week = next Monday's date, slug, theme, cover photo already in
   static/photos (Unsplash free licence, already credited), label, headline ≤12 words, sub line, 4–6 tips taken ONLY
   from the guide's own content (no new claims, no prices), guide URL, caption. Give each tip a "photo" from
   static/photos that actually shows that item or idea (prefer the guide's own section photos; check the alt text) –
   if nothing fits, leave the photo out and the slide renders text-only. Never use a photo that implies we tested it.
3. Caption: hook line, 1–2 lines of value, a question to invite comments, "link in bio", then "#ad – our website guide
   contains affiliate links." if the guide has affiliate links, then 10–15 relevant hashtags (UK renter/home terms).
   No product prices, no testing claims, no invented stats.
4. `python3 tools/make_ig.py <slugs>` – renders slides into static/social/<week>/<slug>/ and rebuilds
   static/social/index.html (noindex, robots-disallowed). View slide 1 and one tip slide; fix text that overflows.
5. Build, commit, push with the site. Check https://therentednest.co.uk/social/ returns 200 and shows the new posts.
6. Log "IG: <slugs> for week of <date>" in the content-log entry. The Monday CEO message reminds Dylan the week's
   posts are ready at therentednest.co.uk/social/.
