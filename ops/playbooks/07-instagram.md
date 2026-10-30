# 07 – Instagram posts (part of the Friday content run)

Account: @therentednestonline (https://www.instagram.com/therentednestonline/), created by Dylan 30 Oct 2026.
Agents CANNOT post to Instagram (no connector; publishing on Dylan's behalf needs his yes each time). So agents MAKE the
posts and Dylan schedules them (Meta Business Suite or Instagram's own scheduler) – about 10 minutes a week.
Bio link: https://therentednest.co.uk/links?utm_source=instagram (page /links lists featured + 12 newest guides; the
featured list is content/links.html – keep it to the 4 most timely guides).

## Volume (new account – same lesson as Pinterest, 30 Oct)
- 3 carousel posts a week, no more, until the Growth review shows Instagram visits growing (GoatCounter campaign
  utm_source=instagram). Never post the same guide twice in 14 days.

## Schedule and reminders (set 30 Oct 2026)
- Dylan posts Mon, Wed and Fri. Each post in posts.json has "day" (YYYY-MM-DD, the Mon/Wed/Fri it goes out).
  /social/ lists the next post first, labelled "Post on <day>"; set "posted": true once a post is up (check the
  public profile https://www.instagram.com/therentednestonline/ – posts newer than the last run).
- Scheduled task "The Rented Nest – Instagram reminder" (Mon/Wed/Fri 11:47) pushes Dylan a one-line reminder with
  that day's post. If no post exists for the day it tells him so – then the next content run must fill the gap first.
- Visual style: theme "pop" (bright colour panel per slide) for everyday posts, "halloween" or another seasonal
  palette for events. Every tip gets a photo that actually shows it; leave it out rather than use a mismatch.
- Seasonal/timely posts (Halloween, Bonfire Night, Black Friday, Christmas, January sales) beat evergreen ones in
  their week – check the calendar when picking guides.

## Steps (Friday content run, after the pins)
1. Pick 3 guides for next week (Mon, Wed, Fri – one each): one gift/seasonal (Nov–Dec), one renter problem (damp, cold, deposit, rules), one
   home/decor idea. Skip any guide used on Instagram in the last 14 days (check ops/instagram/posts.json).
2. For each, add an entry to ops/instagram/posts.json: week = next Monday's date, day = its Mon/Wed/Fri date, slug, theme, cover photo already in
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

## Following (30 Oct 2026)
- Followed (all checked as real, active accounts): @stephkaluza, @emmajanepalin, @charlottejacklin, @londonrentersunion,
  @georgiewebart, @apartmenttherapy, @ikeauk, @ourcuratedabode, @dunelmuk, @habitatuk. The account follows 44 in total
  (Dylan also followed some himself).
- Limit: new account – at most 10 new follows a day, spaced out, and no mass unfollowing. Agents follow only
  when Dylan asks. Not found / wrong account: @shelter (Australian gym), @generationrent, @citizensadvice, @dunelm,
  @livingetc (Australian shop) – don't follow these.
- Growth comes from comments: a helpful, non-salesy comment on @stephkaluza / @emmajanepalin posts beats more follows.
- Comments: agents may DRAFT comments (1–2 sentences, helpful, on-topic, no links, no selling, no claims of personal
  experience the brand doesn't have) but post only after Dylan says yes to each one – posting is public. Max ~5 a day.
  30 Oct: posted 1 approved comment on @emmajanepalin's secondhand-shopping reel (p/DfAkb1FIICQ).
