#!/usr/bin/env python3
"""Turn the PNGs from capture_shots.mjs into the WebP files the site serves.

    python3 tools/shots_to_webp.py

Reads tools/shots/<theme>/<name>.png and writes
assets/img/shot-<name>-<theme>.webp. Quality 82 keeps interface text crisp at
a fifth of the PNG size; the pages are laid out for 1600x1000, and these are
captured at 2x for the retina case.

Needs Pillow: pip install pillow
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "tools", "shots")
DEST = os.path.join(ROOT, "assets", "img")

if not os.path.isdir(SHOTS):
    sys.exit(f"{SHOTS} is missing — run tools/capture_shots.mjs first.")

total = 0
for theme in sorted(os.listdir(SHOTS)):
    folder = os.path.join(SHOTS, theme)
    if not os.path.isdir(folder):
        continue
    for png in sorted(os.listdir(folder)):
        if not png.endswith(".png"):
            continue
        name = png[: -len(".png")]
        out = os.path.join(DEST, f"shot-{name}-{theme}.webp")
        Image.open(os.path.join(folder, png)).convert("RGB").save(
            out, "WEBP", quality=82, method=6
        )
        size = os.path.getsize(out)
        total += size
        print(f"  shot-{name}-{theme}.webp  {size // 1024} KB")

print(f"\n{total / 1048576:.1f} MB in {DEST}")
