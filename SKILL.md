---
name: wada-colours
description: >
  Sanzo Wada colour palette system — 159 named colours and 348 curated palettes from the 1930s
  "Dictionary of Colour Combinations". Use this skill whenever picking colours for ANY design task:
  UI themes, component styling, data visualization palettes, brand colours, ECharts themes, Tailwind
  config, CSS custom properties, dark/light mode schemes, dashboard colour systems, or accent colours.
  Also use when the user says "pick colours", "colour palette", "design system colours", "theme colours",
  "Wada", "Sanzo", "muted palette", "earthy palette", "vintage colours", or anything about choosing
  harmonious colour combinations. This is the go-to colour source for all design work in this project.
---

# Wada Colour Palettes

You have access to 159 historically curated colours and 348 hand-picked combinations from Sanzo Wada's
1933 "Dictionary of Colour Combinations". These are NOT algorithmically generated — each palette was
composed by a colour theorist with decades of experience. The muted, sophisticated aesthetic makes them
ideal for professional interfaces, data visualization, and editorial design.

## Data

The complete colour dataset is bundled at `references/colors.json` — 159 colour objects with name, hex,
rgb, cmyk, lab, swatch group (0-5), and combination IDs (1-348).

A helper script at `scripts/palette_tool.py` can search, filter, and reconstruct palettes. Use it
instead of manually parsing the JSON.

## Quick Reference: Palette Tool

```bash
# Search colours by name
python scripts/palette_tool.py search "blue"

# Get a specific palette by ID (1-348)
python scripts/palette_tool.py palette 42

# Get all palettes for a mood/aesthetic
python scripts/palette_tool.py mood warm      # warm, cool, bold, pastel, earthy, nature, dramatic, ui

# Get palettes by size
python scripts/palette_tool.py size 2         # 2-colour, 3-colour, or 4-colour

# Get palettes containing a specific colour
python scripts/palette_tool.py with "Cerulian Blue"

# Output as CSS custom properties
python scripts/palette_tool.py palette 42 --format css

# Output as Tailwind config
python scripts/palette_tool.py palette 42 --format tailwind

# Output as ECharts theme colours
python scripts/palette_tool.py palette 42 --format echarts

# Get N random palettes of a given size
python scripts/palette_tool.py random 3 --size 4
```

## Palette Structure

| Size | Count | ID Range | Best For |
|------|-------|----------|----------|
| 2-colour | 120 | #1–#120 | Accent pairs, hover states, duotone |
| 3-colour | 120 | #121–#240 | Primary/secondary/accent, charts with 3 series |
| 4-colour | 108 | #241–#348 | Full UI themes, dashboard palettes, rich charts |

## Swatch Groups (Chapters)

| Swatch | Hue Range | Count | Character |
|--------|-----------|-------|-----------|
| 0 | Pinks → Reds → Earth tones | 38 | Warm, dramatic, romantic |
| 1 | Yellows → Ochres → Olives | 49 | Natural, earthy, autumnal |
| 2 | Greens → Teals | 23 | Fresh, organic, calming |
| 3 | Blues → Blue-greens | 23 | Cool, professional, serene |
| 4 | Purples → Violets | 20 | Rich, luxurious, creative |
| 5 | Neutrals (White→Black) | 6 | Foundational, supporting |

## Curated Mood Collections

These are pre-selected palette IDs grouped by aesthetic. When the user asks for a "mood" or "vibe",
start here and then refine by running the palette tool.

### Warm & Earthy
IDs: 2, 3, 8, 26, 33, 102, 121, 132, 243, 296
Ochres, siennas, cinnamons — restaurant brands, craft products, autumn themes.

### Cool & Muted
IDs: 11, 29, 34, 76, 93, 139, 167, 218, 321, 330
Slate blues, sage greens, lavenders — SaaS dashboards, corporate, healthcare.

### Bold & Vivid
IDs: 1, 22, 39, 46, 62, 154, 164, 240, 257, 313
Saturated primaries, strong contrast — hero sections, calls to action, campaigns.

### Pastel & Soft
IDs: 45, 55, 72, 169, 176, 180, 195, 292, 317
Pale pinks, buffs, light greens — onboarding, empty states, gentle UI.

### Floral & Romantic
IDs: 43, 90, 128, 134, 162, 220, 282
Roses, violets, mauves — wedding, beauty, editorial.

### Forest & Nature
IDs: 5, 19, 73, 146, 278, 318, 341, 348
Deep greens, olive, moss — sustainability, outdoor brands, organic.

### Tropical & Bright
IDs: 17, 21, 78, 138, 163, 300, 305
Teal, coral, golden yellow — playful apps, summer themes, food.

### Deep & Dramatic
IDs: 28, 84, 95, 155, 182, 216, 307, 331
Dark indigos, burgundy, violet — luxury, night mode, premium.

### Dashboard / UI-Friendly
IDs: 7, 15, 25, 44, 99, 114, 119, 202, 259
Balanced contrast, readable on white/dark — metrics dashboards, data tables, charts.

## Applying Palettes

### CSS Custom Properties
```css
:root {
  --color-primary: #0093a5;    /* Cerulian Blue */
  --color-secondary: #d96629;  /* English Red */
  --color-accent: #ffefae;     /* Pale Lemon Yellow */
  --color-surface: #f5ecc2;    /* Sulpher Yellow */
}
```

### Tailwind CSS v4
```css
@theme {
  --color-wada-cerulian: #0093a5;
  --color-wada-english-red: #d96629;
  --color-wada-lemon: #ffefae;
  --color-wada-sulpher: #f5ecc2;
}
```

### ECharts Theme
```js
const wadaTheme = {
  color: ['#0093a5', '#d96629', '#ffefae', '#b73f74'],
  backgroundColor: '#ffffff',
  textStyle: { color: '#34454c' },  // Slate Color
};
```

### Design System Token Pattern
For a full theme, pick a 4-colour palette and extend with neutrals:
1. **Primary** — the dominant colour (buttons, links, headers)
2. **Secondary** — supporting colour (cards, borders, secondary actions)
3. **Accent** — highlight colour (badges, notifications, active states)
4. **Surface** — background tint (subtle backgrounds, hover states)
5. **Neutrals** — always pair with Wada neutrals: White (#ffffff), Neutral Gray (#b6bfc1), Warm Gray (#a1a39a), Slate Color (#34454c), Black (#111314)

## Tips

- **3-4 colour palettes** are the sweet spot for full design systems — enough variety without chaos
- **2-colour palettes** are perfect for accent pairs, duotone effects, and chart highlighting
- **Combine palettes** — use a 2-colour palette for primary/accent, then pull neutrals from swatch 5
- **CMYK accuracy** — the hex values come from professional ICC profile conversion (U.S. Web Coated SWOP v2 → sRGB), so they're faithful to the original printed swatches
- **Contrast** — always verify WCAG contrast ratios when using for text. Wada's palettes were designed for print, not screens, so some combinations need a darker/lighter variant for accessibility
- **Most versatile colours**: Black (23 combos), Raw Sienna (19), Pale Lemon Yellow (19), Sulpher Yellow (18) — these work in the widest range of contexts
