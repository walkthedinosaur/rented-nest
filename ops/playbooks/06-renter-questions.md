# Playbook: Renter questions run (QUESTIONS)
Trigger: every Thursday ~10:15 UK.
Inputs: ops/playbooks/05-plan-register.md, ops/seo/target-queries.md, unwritten briefs in ops/seo/briefs/, latest
ops/reports/growth-*.md and community-*.md, content/guides/.
Output: 2 new renter-question pages live, owned register items done and ticked, one log entry.
Goal: grow the renter-question SEO cluster to 30–50 pages by mid-January 2027. Pins are secondary.
(Moved here from the scheduled-task prompt on 19 Oct 2026 so it can be fixed like every other playbook.)

## A. Read
1. Read 00-standing-context.md, ops/plan/growth-plan-2026q4.md and 03-content-production.md (house format, build,
   verify and IndexNow steps).
2. Read 05-plan-register.md and list every OPEN item owned by QUESTIONS that is due by next Thursday. These are this
   run's first pages (e.g. #5 winter damp data page, #11 deposit checklist).
3. Read target-queries.md, every unwritten brief, the latest growth review and the latest community-*.md file
   (real renter questions – the best signal of what people actually ask).

## B. Pick 2 pages
4. Register items first; then briefs marked PRIORITY (lowest number first); then other unwritten briefs; then [ ]
   items in target-queries.md from the Damp, Renters' Rights Act and Moving and deposits sections; then a question
   from the community file that has no page yet.
5. Skip anything the Tuesday/Friday run already published (check content/guides/ and the [x] marks). For an
   unbriefed query, do a quick SERP check and skip it if it would cannibalise an existing guide.

## C. Write
6. Research and verify: for the Renters' Rights Act or any legal topic, check every fact and commencement date on
   GOV.UK on the day.
7. Write each page: answer first, then steps; UK renter's point of view; sources listed and linked; no legal advice –
   point to Shelter / Citizens Advice / GOV.UK; a "Last reviewed" date on legal pages; England-only pages say so and
   link the Scotland/Wales/NI equivalents.
8. Affiliate links only where genuinely useful (then the "Ad" label applies; otherwise set `ads: none`).
9. Cross-link from 1–2 related guides. Mark the query [x] in target-queries.md. Tick any register item done.

## D. Publish
10. Build, commit, push, check 200s and run IndexNow exactly as in 03-content-production.md steps 15–17.
11. Pins: make at most 1 pin per new page and SAVE IT AS A DRAFT (create_post without useNextOpenSlot/sendAt) – the
    Tue/Fri content runs schedule drafts under the 1-a-day limit and 7-day spacing rule (growth plan, reset 30 Oct).
    Same pin rules and checks as 03 steps 13–14.

## E. Log
12. Append a 3-line entry to ops/reports/content-log.md (pages added + register items ticked, pins, credits left and
    any playbook fix), commit and push. Only message Dylan if something failed.

Quality rules: never invent stats, prices, quotes or sources; never claim testing; say "not verified" where unsure.
