#!/usr/bin/env python3
"""Check that a batch of new pins in tools/pins.json is visually varied (added 3 Nov 2026).

Usage: python3 tools/check_pin_variety.py [slug ...]
  With slugs: checks those pins as one batch. Without: checks the last 7 entries in pins.json.
Exit code 1 if any rule fails – fix pins.json and re-render before pushing.

Rules (Dylan, 3 Nov 2026: "the pins all look the same – vary colours and design styles"):
  1. New pins use a v3 layout (overlay, split, poster, checklist, frame, numbered, arch, duo, script).
     photo2/photo/a/b/c are retired for new pins.
  2. Neighbouring pins (in pins.json order, including the pin just before the batch) never share
     a layout, a palette or a font.
  3. In any batch: no layout used more than twice, no palette more than twice; a batch of 4+ pins
     uses at least 4 layouts and 4 palettes.
  4. The last 7 v3 pins in the file together use at least 5 layouts and 5 palettes.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V3 = {"overlay", "split", "poster", "checklist", "frame", "numbered", "arch", "duo", "script"}
NEEDS = {"checklist": "points", "numbered": "num", "duo": "photo_b"}


def main():
    pins = json.loads((ROOT / "tools" / "pins.json").read_text())
    idx = {p["slug"]: i for i, p in enumerate(pins)}
    slugs = sys.argv[1:]
    if slugs:
        missing = [s for s in slugs if s not in idx]
        if missing:
            sys.exit(f"Not in pins.json: {missing}")
        batch_idx = sorted(idx[s] for s in slugs)
    else:
        batch_idx = list(range(max(0, len(pins) - 7), len(pins)))
    errors = []
    batch = [pins[i] for i in batch_idx]

    for p in batch:
        if p.get("layout") not in V3:
            errors.append(f"{p['slug']}: layout '{p.get('layout')}' is retired – use one of {sorted(V3)}")
            continue
        for f in ("palette", "font"):
            if not p.get(f):
                errors.append(f"{p['slug']}: missing {f}")
        need = NEEDS.get(p["layout"])
        if need and not p.get(need):
            errors.append(f"{p['slug']}: layout {p['layout']} needs '{need}'")

    for i in batch_idx:
        if i == 0:
            continue
        a, b = pins[i - 1], pins[i]
        for f in ("layout", "palette", "font"):
            if a.get(f) and a.get(f) == b.get(f) and b.get("layout") in V3:
                errors.append(f"{b['slug']}: same {f} ('{b[f]}') as the pin before it ({a['slug']})")

    lay = Counter(p.get("layout") for p in batch)
    pal = Counter(p.get("palette") for p in batch)
    for name, c in (("layout", lay), ("palette", pal)):
        for k, n in c.items():
            if k and n > 2:
                errors.append(f"batch uses {name} '{k}' {n} times (max 2)")
    if len(batch) >= 4:
        if len(lay) < 4:
            errors.append(f"batch of {len(batch)} uses only {len(lay)} layouts (need 4+)")
        if len(pal) < 4:
            errors.append(f"batch of {len(batch)} uses only {len(pal)} palettes (need 4+)")

    recent = [p for p in pins if p.get("layout") in V3][-7:]
    if len(recent) == 7:
        rl = len({p["layout"] for p in recent})
        rp = len({p.get("palette") for p in recent})
        if rl < 5 or rp < 5:
            errors.append(f"last 7 v3 pins use {rl} layouts / {rp} palettes (need 5+ of each)")

    print("Batch:", ", ".join(f"{p['slug']}={p.get('layout')}/{p.get('palette')}/{p.get('font')}" for p in batch))
    if errors:
        print("VARIETY CHECK FAILED:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("Variety check passed.")


if __name__ == "__main__":
    main()
