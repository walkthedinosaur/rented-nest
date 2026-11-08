#!/usr/bin/env python3
"""Turn an Instagram carousel (static/social/<week>/<slug>/NN.png) into a 9:16 Reel: reel.mp4 (1080x1920, no audio –
Dylan adds a trending sound from Instagram's own library when posting, which keeps music licensed).
Each slide ~2.6 s (cover 3 s), slide centred on a blurred, darkened copy of itself, short crossfades.
Run: python3 tools/make_reel.py [slug ...]   (needs ffmpeg)"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "social"
FADE = 0.4

def reel(d: Path):
    slides = sorted(d.glob("[0-9][0-9].png"))
    if not slides:
        return False
    durs = [3.0] + [2.6] * (len(slides) - 2) + [3.0] if len(slides) > 1 else [3.0]
    inputs, filters = [], []
    for i, (s, t) in enumerate(zip(slides, durs)):
        inputs += ["-loop", "1", "-t", f"{t + FADE:.2f}", "-i", str(s)]
        filters.append(
            f"[{i}:v]split[a{i}][b{i}];"
            f"[a{i}]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5,eq=brightness=-0.12[bg{i}];"
            f"[b{i}]scale=1000:-1[fg{i}];"
            f"[bg{i}][fg{i}]overlay=(W-w)/2:(H-h)/2,format=yuv420p,setsar=1,fps=30[v{i}]")
    chain, prev, offset = [], "v0", 0.0
    for i in range(1, len(slides)):
        offset += durs[i - 1]
        chain.append(f"[{prev}][v{i}]xfade=transition=slideleft:duration={FADE}:offset={offset - FADE * (i - 1) - FADE:.2f}[x{i}]")
        prev = f"x{i}"
    fc = ";".join(filters + chain)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", fc, "-map", f"[{prev}]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-movflags", "+faststart", str(d / "reel.mp4")]
    subprocess.run(cmd, check=True)
    return True

def main():
    posts = json.loads((ROOT / "ops" / "instagram" / "posts.json").read_text())
    only = set(sys.argv[1:])
    for p in posts:
        if (only and p["slug"] not in only) or (not only and p.get("posted")):
            continue
        d = OUT / p["week"] / p["slug"]
        if d.exists() and reel(d):
            print("reel", p["slug"])

if __name__ == "__main__":
    main()
