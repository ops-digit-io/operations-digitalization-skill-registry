---
type: Skill Reference
title: Build engine
description: "How the deck is rendered from the backbone with build_bc_short.py on the neuwerk template; QA before delivery."
resource: ../SKILL.md
status: draft
tags: [business-case, assessment, department-package]
---
> Transcribed from the department package `bc-assessment.zip/reference/build-engine.md` (the master).

# Build engine — how to render the deck

The reference renderer is `../scripts/build_bc_short.py` (python-pptx on the real Neuwerk template,
"Route A"). It is the canonical implementation of the 9-slide + backup sequence for the Gemba
case; adapt its content blocks for other cases, keeping the helpers, palette, and geometry.

## Setup

Keep `assets/_nw_template.pptx` beside the script. The script reads `SRC` (template) and writes
`OUT` (the deck), stripping the template's own slides first, then adding cover (layout 1) +
content slides (layout 2).

Adjust the two paths at the top for the environment:
```python
SRC = '.../_nw_template.pptx'
OUT = '.../bc-<case>-onepager-neuwerk.pptx'
```

## Palette (brand-exact — do not invent hex)

```
NAVY 1B1E52  DEEP 273892  BLUE 4E66AE  PERI 8793CA        # navy + blue ramp (graded cards)
GREEN 1EB78B  PEACH F9B09A  TEAL 48C3CB  PINK EEC1DB       # Mint / Melon / Azure / Levander bases
MELONL F6CFC6  MELOND F37558                                # Melon light (caution tint) / dark (brand-red)
GRY CCCCCC  SUN FFA500                                      # Grey06 / Sun (budget only: title rule + logo)
FONT 'Poppins'  SERIF 'Lora'
```

Semantic use: **Mint = solution/banked**, **Melon = problem/not-banked**, **Melon-dark F37558 =
brand-red for wide-uncertainty flags**, **Blue ramp = neutral/graded**, **Azure = cross-plant**.

## Helpers (reuse; don't re-implement)

- `rich(p, text, size, color, bold, italic, font)` — splits on `**` for inline bold.
- `ph_fill(slide, idx, rows)` — fill a placeholder with sized paragraphs.
- `box(slide, l, t, w, h, fillc, ml, mt, shape, adj)` — rounded-rect card (no shadow, no outline).
- `lines(shape, rows, anchor, align)` — rows = `(text, size, color, bold, italic, space_after)`.
- `caption(slide, l, t, w, h, text, size, italic, align, color, bold)` — a text box.
- `cols(n, total, gut)` — returns `(col_width, [left_x...])` for an n-column grid.
- `content(title_text, sub)` — adds a layout-2 content slide: title 24pt at `(0.77, 0.69,
  9.80, 0.69)`, **deletes body placeholder idx 11** (else Lorem-ipsum leaks), fills footers
  10/12/13/14, optional sub-caption at y=1.38. Use this for every content slide.
- `panel(...)`, `chip(...)` — a titled body card / a small pill.

Footers via the `FT` dict: `tag='BC Assessment'`, `who='OD - Operations Digitalization'`,
`yr='2026'`, `tl='The neuwerk way'`.

## Geometry

Canvas 13.333×7.5 in. Content safe band x 0.50→12.83, y 1.36→6.60. Title 24pt at
`(0.77, 0.69)`. Footer baseline y≈6.81. The orange title rule and the logo are the **only** Sun
elements — never add a second orange element.

## QA render loop

Each bash call is independent (no cwd/env carryover). Render into a fresh tmp dir and copy JPEGs
out in the same call, then Read them via the Windows outputs path.

```bash
cd /sessions/<sess>/mnt/outputs && python3 build_bc_short.py && \
d=/tmp/q_$(date +%s) && mkdir -p $d && \
soffice --headless --convert-to pdf --outdir $d bc-<case>-onepager-neuwerk.pptx && \
pdftocairo -jpeg -r 110 $d/bc-<case>-onepager-neuwerk.pdf $d/bc && \
cp $d/bc-*.jpg /sessions/<sess>/mnt/outputs/
```

Then Read each `C:\...\outputs\bc-NN.jpg` (the Windows path — the /sessions path errors as
"root- or drive-relative"). Check: no overflow/cut-off; Sun budget ≤10–15%; no white text on
light tints (white is safe only on Navy, Blue tint 1–2, and dark secondary tints); tilde +
factual-language conventions honored on every slide; every slide has a visual.

## Adapting for a new case

Change the content tuples (headline band, panels, register `regs`/`uncts`, sub-case `rows`,
milestones `mile`, refinement `refblock`s) to the case's levers and figures from the backbone.
Keep the sequence, helpers, palette, and geometry. Append the provenance/conflict slide last
(see `provenance-and-conflicts.md`).
