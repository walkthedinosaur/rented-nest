# Playbook: CEO weekly report
Trigger: every Monday ~08:00 UK.
Inputs: last 7 days of Tailwind, Pinterest, Cloudflare, Awin, Search Console, Gmail business emails; ops/ files.

Steps
1. Read ops/playbooks/00-standing-context.md and the latest ops/reports/*.md (last week's report, incl. the Growth
   Marketer review from Sunday, ops/reports/growth-YYYY-MM-DD.md).
2. Pinterest: Tailwind get_account_usage (credits left), get_schedule next 7 days (how many open slots), list_posts
   status sent for last 7 days (count), get_account_analytics / get_pin_analytics if available (impressions, saves,
   outbound clicks). Check list_posts status failed/missed.
3. Website: Cloudflare Web Analytics (built-in browser, dash.cloudflare.com → Web analytics, last 7 days): visits,
   page views, top pages, referrers (Pinterest/Google). If the browser is unreachable, say so.
4. Affiliates: Awin (built-in browser, ui.awin.com/awin/affiliate/3120264) – programme statuses (Joined/Pending/
   Rejected) and any clicks/commission; update ops/awin-applications.xlsx Status + Date decided. Amazon: from
   forwarded Associates emails only (no login) – note the 3-sale deadline (~early April 2027) and any warnings.
5. Email sweep per ops/email-monitoring.md (read-only).
6a. Plan register: run the "CEO weekly check" in ops/playbooks/05-plan-register.md – list late items with
   reasons, add rows for any new commitments, and check new Awin approvals have links (item 18).
6. Compare actuals with the base case in ops/revenue-forecast-24m.xlsx (impressions, visits, clicks, commission).
7. Write ops/reports/ceo-YYYY-MM-DD.md, commit and push.
8. Send Dylan ONE short message (push notification if available), max ~12 lines:
   headline numbers vs forecast; what changed; approvals; risks/warnings; decisions needed (spend only); next week's
   plan. If nothing needs him, say "No action needed."
Output: the report file + one message. Review gates: end Dec 2026 and end Jan 2027 – if tracking at/below base case,
add a recommendation on whether to keep paying for Tailwind (Dylan decides).
