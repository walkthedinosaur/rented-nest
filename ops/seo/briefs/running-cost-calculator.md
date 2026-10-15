# Brief: Drying & heating running-cost calculator (link magnet)
Written: 2026-10-15 (CEO) · For: content run Fri 16 Oct (PRIORITY 1 – due live by Mon 26 Oct) · Status: brief written
Suggested slug: /tools/drying-heating-cost-calculator.html (kind: page, add to footer + home "Tools" link) · Label: Keeping warm

## Target queries
"is it cheaper to use a heated airer or tumble dryer uk", "how much does a dehumidifier cost to run per hour uk",
"heated airer running cost calculator", "cost to run an oil filled radiator per hour". Volumes: not verified.

## What to build
One static page, plain HTML + a small inline <script> (no external libraries, no cookies, no storage):
- Inputs: appliance preset (heated airer winged / heated airer tower / drying pod / dehumidifier compressor /
  dehumidifier desiccant / tumble dryer vented / heat-pump tumble dryer / oil-filled radiator / fan heater / electric
  blanket / heated throw) – each preset fills a wattage the user can edit; hours per use; uses per week; electricity
  unit rate in p/kWh, prefilled with the CURRENT Ofgem price-cap average unit rate for electricity (look it up on
  ofgem.gov.uk on the day; state the period it applies to and link it). Tumble dryers: use kWh per cycle instead of watts.
- Outputs: cost per use, per week, per month, per winter (Oct–Mar, 26 weeks). Show the working (watts ÷ 1000 × hours × rate).
- Comparison table: run the user's weekly pattern across 3–4 presets side by side.
- Every preset wattage must come from a cited source (Which?, manufacturer spec pages, Energy Saving Trust). Where only a
  range exists, use the midpoint and say so. If you can't source a preset, leave it out. Never invent figures.
- Plain caveats: estimates only; real costs depend on tariff, thermostat cycling (radiators/dehumidifiers with humidistats
  draw less than rated power) and standing charges (excluded).
- Below the tool: 300–500 words answering "heated airer vs tumble dryer – which is cheaper?" using the tool's own maths,
  links to the airers, dehumidifiers, stay-warm and drying-clothes guides, Sources list. Affiliate links optional and light.
- Add the cap-rate update to ops/plan/growth-plan-2026q4.md: next cap (Jan–Mar 2027) is expected to be announced late Nov – update the default rate then.

## Why
A useful free tool is the most linkable thing we can make (forums, Reddit answers, money-saving blogs) and it feeds the
damp/heating guides. Also gives Pinterest a "how much does it cost" pin angle.
