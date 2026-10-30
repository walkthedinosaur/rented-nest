# Playbook: CEO weekly report
Trigger: every Monday ~08:00 UK.
Inputs: last 7 days of Tailwind, Pinterest, Cloudflare, Awin, Search Console, Gmail business emails; ops/ files.
Output: ops/reports/ceo-YYYY-MM-DD.md + one short message to Dylan.

Focus metric (added 19 Oct 2026): **qualifying Amazon sales toward the 3-sale deadline (~early April 2027)**. Missing
it closes the Amazon Associates account, which every guide depends on. It leads both the report and the message.
Second line: outbound clicks to retailers (Amazon + Awin), the leading indicator of sales.

## A. Read
1. Read ops/playbooks/00-standing-context.md, ops/plan/growth-plan-2026q4.md, last week's ceo-*.md and the Growth
   review from Sunday (ops/reports/growth-YYYY-MM-DD.md).

## B. Gather (one source per step)
2. Pinterest: Tailwind get_account_usage (credits left), get_schedule next 7 days (open slots), list_posts status
   sent for the last 7 days (count), list_posts status failed/missed, get_account_analytics / get_pin_analytics if
   available (impressions, saves, outbound clicks).
3. Website: GoatCounter (public, no login, works from the cloud even when Dylan's computer is offline): https://therentednest.goatcounter.com/?period-start=YYYY-MM-DD&period-end=YYYY-MM-DD – read it with WebFetch or curl. Counts start 28 Oct 2026; Cloudflare (built-in browser, often signed out) is only a fallback for earlier dates.
   Last 7 days: visits, top pages, referrers (Pinterest/Google).
4. Awin (built-in browser, ui.awin.com/awin/affiliate/3120264): programme statuses (Joined/Pending/Rejected) and
   any clicks/commission; update ops/awin-applications.xlsx Status + Date decided.
5. Amazon: from forwarded Associates emails only (no login) – qualifying sales so far, days left to the deadline,
   any warnings.
6. Email sweep per ops/email-monitoring.md (read-only).

## C. Judge
7. Compare actuals with the base case in ops/revenue-forecast-24m.xlsx (impressions, visits, clicks, commission).
8. Plan register: run the "CEO weekly check" in 05-plan-register.md – list late items with reasons, add rows for any
   new commitments, check new Awin approvals have links (item 18). Note any playbook changes made this week
   (git log ops/playbooks/) in one line. If the last two growth reviews both say "Trends: not checked", list it as a
   risk with the reason.
9. If Amazon sales are behind the path to 3 by the deadline (none by end Dec is "behind"), add one specific
   recommendation for next week's growth review (e.g. shift pins to the guides with the most Amazon clicks).

## D. Report
10. Write ops/reports/ceo-YYYY-MM-DD.md (focus metric first), commit and push.
11. Send Dylan ONE short message (push notification if available), max ~12 lines: focus metric; headline numbers vs
    forecast; what changed; approvals; risks/warnings; Dylan's open register items; decisions needed (spend only);
    next week's plan. If nothing needs him, say "No action needed."

Review gates: end Dec 2026 and end Jan 2027 – if tracking at/below base case, add a recommendation on whether to keep
paying for Tailwind (Dylan decides).

## Instagram (added 30 Oct 2026)
- In the report: @therentednestonline followers and posts this week (public profile, built-in browser: https://www.instagram.com/therentednestonline/ – if unreachable, say "not checked"), and visits from Instagram in GoatCounter (referrer instagram.com / l.instagram.com or campaign utm_source=instagram).
- Remind Dylan in the message that this week's posts are at therentednest.co.uk/social/ (Mon/Wed/Fri; the Instagram reminder task pings him on the day).
