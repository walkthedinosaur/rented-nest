"""Insert an Amazon UK search link after each matching idea heading in the guides.
Links use the {{amazon:search terms|label}} shortcode, which build.py expands."""
import re
from pathlib import Path

LINKS = {
 "A good-quality toolkit in a small case": "compact home tool kit",
 "A set of matching storage baskets": "storage baskets set",
 "A plug-in rechargeable torch": "plug in rechargeable torch",
 "A heated throw": "heated throw",
 "A draught excluder for the front door": "door draught excluder",
 "Thermal-lined curtains": "thermal blackout curtains",
 "A self-watering windowsill planter": "self watering windowsill planter",
 "A plant stand": "indoor plant stand",
 "Nesting mixing bowls or measuring cups": "nesting mixing bowls",
 "An in-drawer knife organiser": "in drawer knife organiser",
 "A personalised chopping board": "personalised chopping board",
 "A laptop stand that folds flat": "foldable laptop stand",
 "A desk lamp with a warm light setting": "desk lamp warm light dimmable",
 "1. Over-door hooks and racks": "over door hooks",
 "2. Over-door shoe or pantry organisers": "over door hanging organiser",
 "3. Removable adhesive hooks": "removable adhesive hooks",
 "4. Picture ledges that lean": "picture ledge shelf",
 "5. Ladder shelves": "ladder shelf",
 "6. Tension-pole shelving": "tension pole shelf",
 "7. Slim rolling trolleys": "slim rolling storage trolley",
 "8. Freestanding clothes rails": "clothes rail with shelf",
 "9. Bed risers and under-bed boxes": "bed risers",
 "10. Shelf risers inside cupboards": "cupboard shelf riser",
 "11. Under-shelf baskets": "under shelf basket",
 "12. Tension rods inside cupboards": "tension rod",
 "13. Storage ottomans and benches": "storage ottoman",
 "14. Cube units on their side": "cube storage unit",
 "15. Nesting side tables": "nesting side tables",
 "Layer lamps instead of relying on the ceiling light": "floor lamp",
 "Lean a large mirror": "full length floor mirror",
 "Cover the sofa": "stretch sofa cover",
 "Put a rug over the carpet": "rug for carpet non slip",
 "Use a bookcase as a room divider": "open cube bookcase room divider",
}
for f in Path("content/guides").glob("*.html"):
    t = f.read_text()
    for head, q in LINKS.items():
        pat = re.compile(r"(<h3>" + re.escape(head) + r"</h3><p>.*?</p>)(?!<p class=\"shop\">)")
        t = pat.sub(lambda m: m.group(1) + '<p class="shop">{{amazon:' + q + '|Shop on Amazon UK}}</p>', t, count=1)
    f.write_text(t)
