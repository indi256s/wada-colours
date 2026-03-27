#!/usr/bin/env python3
"""Sanzo Wada palette search, filter, and export tool.

Usage:
    python palette_tool.py search <query>           Search colours by name
    python palette_tool.py palette <id> [--format]  Get palette by ID (1-348)
    python palette_tool.py mood <mood> [--format]   Get palettes for a mood
    python palette_tool.py size <n>                 Get palettes by colour count (2/3/4)
    python palette_tool.py with <colour_name>       Get palettes containing a colour
    python palette_tool.py random <n> [--size S]    Get N random palettes
    python palette_tool.py swatch <n>               List colours in swatch group (0-5)
    python palette_tool.py contrast <hex1> <hex2>   Check WCAG contrast ratio

Formats: hex (default), css, tailwind, echarts, json
"""

import json
import sys
import os
import random
import math
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_PATH = SCRIPT_DIR.parent / "references" / "colors.json"

MOODS = {
    "warm": [2, 3, 8, 26, 33, 102, 121, 132, 243, 296],
    "cool": [11, 29, 34, 76, 93, 139, 167, 218, 321, 330],
    "bold": [1, 22, 39, 46, 62, 154, 164, 240, 257, 313],
    "pastel": [45, 55, 72, 169, 176, 180, 195, 292, 317],
    "floral": [43, 90, 128, 134, 162, 220, 282],
    "nature": [5, 19, 73, 146, 278, 318, 341, 348],
    "tropical": [17, 21, 78, 138, 163, 300, 305],
    "dramatic": [28, 84, 95, 155, 182, 216, 307, 331],
    "ui": [7, 15, 25, 44, 99, 114, 119, 202, 259],
    "earthy": [2, 3, 8, 26, 33, 102, 121, 132, 243, 296],
}


def load_colors():
    with open(DATA_PATH) as f:
        return json.load(f)


def build_palettes(colors):
    palettes = {}
    for c in colors:
        for combo_id in c["combinations"]:
            if combo_id not in palettes:
                palettes[combo_id] = []
            palettes[combo_id].append({
                "name": c["name"],
                "hex": c["hex"],
                "rgb": c["rgb"],
                "swatch": c["swatch"],
            })
    return palettes


def relative_luminance(r, g, b):
    """WCAG 2.0 relative luminance."""
    def linearize(v):
        v = v / 255.0
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(b)


def contrast_ratio(hex1, hex2):
    def parse_hex(h):
        h = h.lstrip("#")
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    l1 = relative_luminance(*parse_hex(hex1))
    l2 = relative_luminance(*parse_hex(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def format_palette(palette, fmt="hex", palette_id=None):
    if fmt == "json":
        return json.dumps(palette, indent=2)

    header = f"Palette #{palette_id}" if palette_id else "Palette"
    lines = [header, "=" * len(header)]

    for c in palette:
        lines.append(f"  {c['hex']}  {c['name']}")

    if fmt == "css":
        lines.append("")
        lines.append("/* CSS Custom Properties */")
        lines.append(":root {")
        roles = ["primary", "secondary", "accent", "surface"]
        for i, c in enumerate(palette):
            role = roles[i] if i < len(roles) else f"color-{i+1}"
            slug = c["name"].lower().replace(" ", "-").replace("|", "").replace("  ", "-")
            lines.append(f"  --color-{role}: {c['hex']};  /* {c['name']} */")
        lines.append("}")

    elif fmt == "tailwind":
        lines.append("")
        lines.append("/* Tailwind CSS v4 @theme */")
        lines.append("@theme {")
        for c in palette:
            slug = c["name"].lower().replace(" ", "-").replace("|", "").replace("  ", "-").strip("-")
            lines.append(f"  --color-wada-{slug}: {c['hex']};")
        lines.append("}")

    elif fmt == "echarts":
        hexes = [c["hex"] for c in palette]
        lines.append("")
        lines.append("// ECharts theme color array")
        lines.append(f"color: {json.dumps(hexes)}")

    return "\n".join(lines)


def cmd_search(args, colors):
    query = " ".join(args).lower()
    results = [c for c in colors if query in c["name"].lower()]
    if not results:
        print(f"No colours matching '{query}'")
        return
    for c in results:
        combos = ", ".join(str(x) for x in c["combinations"][:8])
        more = f" +{len(c['combinations'])-8} more" if len(c["combinations"]) > 8 else ""
        print(f"  {c['hex']}  {c['name']:30s}  swatch:{c['swatch']}  palettes:[{combos}{more}]")


def cmd_palette(args, colors, palettes):
    fmt = "hex"
    if "--format" in args:
        idx = args.index("--format")
        fmt = args[idx + 1]
        args = args[:idx] + args[idx+2:]

    for a in args:
        if a.startswith("--format="):
            fmt = a.split("=", 1)[1]
            args.remove(a)
            break

    # Also check shorthand flags
    for f in ["css", "tailwind", "echarts", "json"]:
        if f"--{f}" in args:
            fmt = f
            args.remove(f"--{f}")

    palette_id = int(args[0])
    if palette_id not in palettes:
        print(f"Palette #{palette_id} not found (valid: 1-348)")
        return
    print(format_palette(palettes[palette_id], fmt, palette_id))


def cmd_mood(args, colors, palettes):
    fmt = "hex"
    for f in ["css", "tailwind", "echarts", "json"]:
        if f"--{f}" in args:
            fmt = f
            args.remove(f"--{f}")
    if "--format" in args:
        idx = args.index("--format")
        fmt = args[idx + 1]
        args = args[:idx] + args[idx+2:]

    mood = args[0].lower()
    if mood not in MOODS:
        print(f"Unknown mood '{mood}'. Available: {', '.join(sorted(MOODS.keys()))}")
        return
    ids = MOODS[mood]
    print(f"Mood: {mood} ({len(ids)} palettes)")
    print()
    for pid in ids:
        if pid in palettes:
            print(format_palette(palettes[pid], fmt, pid))
            print()


def cmd_size(args, palettes):
    n = int(args[0])
    matching = {pid: pal for pid, pal in palettes.items() if len(pal) == n}
    print(f"{len(matching)} palettes with {n} colours:")
    print()
    for pid in sorted(matching.keys()):
        hexes = " ".join(c["hex"] for c in matching[pid])
        names = ", ".join(c["name"] for c in matching[pid])
        print(f"  #{pid:3d}  {hexes}  ({names})")


def cmd_with(args, colors, palettes):
    name = " ".join(args).lower()
    matches = [c for c in colors if name in c["name"].lower()]
    if not matches:
        print(f"No colour matching '{name}'")
        return
    color = matches[0]
    print(f"Palettes containing {color['name']} ({color['hex']}):")
    print()
    for combo_id in color["combinations"]:
        if combo_id in palettes:
            others = [c for c in palettes[combo_id] if c["name"] != color["name"]]
            other_str = ", ".join(f"{c['hex']} {c['name']}" for c in others)
            print(f"  #{combo_id:3d}  + {other_str}")


def cmd_random(args, palettes):
    n = int(args[0]) if args else 3
    size = None
    if "--size" in args:
        idx = args.index("--size")
        size = int(args[idx + 1])

    candidates = palettes
    if size:
        candidates = {pid: pal for pid, pal in palettes.items() if len(pal) == size}

    if not candidates:
        print("No palettes match criteria")
        return

    chosen = random.sample(list(candidates.keys()), min(n, len(candidates)))
    for pid in chosen:
        print(format_palette(candidates[pid], "hex", pid))
        print()


def cmd_swatch(args, colors):
    n = int(args[0])
    group = [c for c in colors if c["swatch"] == n]
    swatch_names = {
        0: "Pinks / Reds / Earth tones",
        1: "Yellows / Ochres / Olives",
        2: "Greens / Teals",
        3: "Blues / Blue-greens",
        4: "Purples / Violets",
        5: "Neutrals",
    }
    print(f"Swatch {n}: {swatch_names.get(n, 'Unknown')} ({len(group)} colours)")
    print()
    for c in group:
        print(f"  {c['hex']}  {c['name']}")


def cmd_contrast(args):
    hex1, hex2 = args[0], args[1]
    ratio = contrast_ratio(hex1, hex2)
    aa_normal = "PASS" if ratio >= 4.5 else "FAIL"
    aa_large = "PASS" if ratio >= 3.0 else "FAIL"
    aaa_normal = "PASS" if ratio >= 7.0 else "FAIL"
    print(f"Contrast ratio: {ratio:.2f}:1")
    print(f"  WCAG AA  (normal text): {aa_normal}")
    print(f"  WCAG AA  (large text):  {aa_large}")
    print(f"  WCAG AAA (normal text): {aaa_normal}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]
    colors = load_colors()
    palettes = build_palettes(colors)

    if cmd == "search":
        cmd_search(args, colors)
    elif cmd == "palette":
        cmd_palette(args, colors, palettes)
    elif cmd == "mood":
        cmd_mood(args, colors, palettes)
    elif cmd == "size":
        cmd_size(args, palettes)
    elif cmd == "with":
        cmd_with(args, colors, palettes)
    elif cmd == "random":
        cmd_random(args, palettes)
    elif cmd == "swatch":
        cmd_swatch(args, colors)
    elif cmd == "contrast":
        cmd_contrast(args)
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
