---
type: Skill Reference
title: Build engine
description: "How the eCR management summary deck is filled and rendered with build_ecr.py on the neuwerk template; slide-type functions, brand rules, QA checklist."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [capital-request, ecr, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ecr-builder.zip/reference/build-engine.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ecr-builder.zip/reference/build-engine.md` (the master).

# Build engine — filling CASE and rendering the deck

`../scripts/build_ecr.py` is a data-driven neuwerk-brand renderer. It ships runnable
with an illustrative example (Product Regionalization, Kranj) so you can see the
target before editing. To build a real eCR you edit **only** two regions:

1. the `CASE` dict (slug + footer chrome), and
2. the `build()` function's slide-assembly body (the actual content).

The helper library and slide-type functions above `CASE` are the stable engine.

## Run it

```bash
cd assets
python build_ecr.py          # writes eCR_<slug>_neuwerk.pptx
bash render_qa.sh eCR_<slug>_neuwerk.pptx 90   # -> per-slide JPEGs to eyeball
```

`_nw_template.pptx` (the neuwerk template) must sit next to the script; it is
included in the skill's `assets/`.

## Slide-type functions (compose the deck from these)

- `cover(title, subtitle, id_rows)` — dark title slide (layout 1) + white ID card.
- `content(title, sub=None)` — standard content slide (layout 2); returns the slide
  so you can add boxes/tables.
- `divider(title)` — section/backup divider (layout 4).
- `table(slide, x, y, colw, headers, rows, aligns, total_row=, accent=)` — clean
  grid; `total_row=True` bolds+shades the last row in `accent`.
- `rr_table(slide, headers, rows, accent)` — the rated Risk/Opportunity table; each
  row `[item, actions, level, case]`; the level cell auto-colours
  High=Melon / Medium=Peach / Low=Mint. Use `accent=PEACH` for risks, `GREEN` for
  opportunities.
- `kpi_row(slide, [(label,value,sub),...])` — the financial KPI cards.
- `box / lines / caption / chip / tag_legend` — primitives. `chip(slide,x,y,tag)`
  drops an A/M/? grounding marker; `tag_legend(slide,x,y)` prints the legend once.
- `open_items_conflicts(open_items, conflicts, verdict)` — the final slide (see
  `open-items-and-conflicts.md`). Author its three arguments from what you found.

## neuwerk brand rules (non-negotiable)

- **Canvas** 13.333 × 7.5 in (16:9). Content margin ~0.50 in.
- **Palette** — Navy `1B1E51` (primary text/dark panels), Sun `FFA500` (title rule +
  logo only, keep to ≤10–15% of the slide), Periwinkle `8793CA` (bands/neutral),
  and the semantic pairs: Melon `FBD9CC` / Peach `F8AF99` = risk / High / before /
  problem; Mint `CBE7DC` / Green `1EB68A` = opportunity / Low / after / solution.
  Grounding chips reuse Peach (A) / Periwinkle (M) / Melon-dark `F37558` (?).
- **Type** — Poppins everywhere; Lora *only* for the tagline "The neuwerk way".
  Titles sentence case, no terminal full stop.
- **Footers** — the layouts carry placeholder indices 10 (title tag), 12 (presenter),
  13 (year), 14 (tagline, set to Lora). `content()`/`cover()`/`divider()` fill these
  from `CASE`; don't hand-place footers.
- **Chrome consistency** — one presenter string, one year, one title tag across all
  slides. Mixed ContiTech/Continental branding or date formats is a defect.

## Mapping the backbone → CASE/slides

Work section by section from your `eCR_<slug>_backbone.md`:

- Layer-3 figures become the strings in `lines()`/`table()` calls; append a chip at
  the box's top-right for every `[a]`/`[m]`/`[?]` figure.
- The exec-summary rail gets the headline financials + one `tag_legend()`.
- Risks/opportunities go through `rr_table()`, never as free bullets.
- Sections that the conditional rules switch off (sensitivity below threshold,
  layout "if applicable") are stated-as-not-required or omitted — not faked.
- The last slide is always `open_items_conflicts(...)`.

## QA checklist before delivering

- Deck opens, slide count matches the sections you intended.
- Every non-grounded figure has a chip; the legend appears once.
- Risks/opportunities are the rated table; totals reconcile; no netting of value
  against cost.
- Sensitivity handled correctly for the amount/duration.
- Every acronym is in the Glossary.
- The Open items & conflicts slide is present, the verdict matches how grounded the
  case actually is, and no conflict/open item was invented.
