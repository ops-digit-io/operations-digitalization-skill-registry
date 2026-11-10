---
type: Skill Reference
title: Deck structure
description: "Slide order and content rules of the funnel business-case deck."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, deck, department-package]
derived_from:
  - "Department knowledge base, OD Department Knowledge/OD-instance/30-skills/product-funnel-skills.zip/skills/business-case/references/deck-structure.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `product-funnel-skills.zip/skills/business-case/references/deck-structure.md` (the master).

# Deck Production

How to take a template's design without inheriting its content, and how to build
slides that carry the case.

## What a template gives you

| Take | Ignore |
|------|--------|
| `ppt/slideMasters/` and `ppt/slideLayouts/` | The sample deck's slide text |
| `ppt/theme/` — palette, fonts | Its section headings and column captions |
| `ppt/media/` — logo, background art | Its slide count and running order |
| Footer treatment, title placement, margins | Its subject matter and framing |

The distinction matters because a template is usually a *finished deck about
something else*. Its structure reflects that topic. Reuse the structure and you
end up arguing that deck's case with your numbers pasted in — which reads as
generic, and loses the specificity that makes a business case persuasive.

## Harvesting the shell

Two workable routes. Prefer the first.

### Route A — reuse slides as layout shells

Keep the template's slides, strip their content, refill. Reliable, because every
placeholder, font size, and logo position is already correct.

```bash
python3 -c "import sys,zipfile; zipfile.ZipFile(sys.argv[1]).extractall('unpacked')" template.pptx
python /mnt/skills/public/pptx/scripts/thumbnail.py template.pptx tpl-thumbs
```

Look at the grid and pick which visual layout suits each piece of your content —
a title treatment, a multi-column body, a full-bleed image frame, a table slide,
a closing slide. Then:

- Duplicate the slides you need more of with `../scripts/add_slide.py`
- Delete the ones you do not, via `<p:sldIdLst>` in `ppt/presentation.xml`, then
  `../scripts/clean.py`
- **Do all structural work before editing any content** — `add_slide.py` copies
  verbatim, so duplicating after editing clones the edited text
- Replace every text run. One `<a:p>` per list item, copy the sibling `<a:pPr>`
  to keep spacing

Then repack and validate:

```bash
(cd unpacked && rm -f ../out.pptx && zip -Xr ../out.pptx .)
python /mnt/skills/public/pptx/scripts/office/validate.py out.pptx --original template.pptx
```

Pass `--original` — a template often carries its own schema quirks, and without
the baseline they read as your errors.

### Route B — build fresh against the theme

Only when the template's layouts genuinely do not fit the content. Read the
theme's colours and fonts out of `ppt/theme/theme1.xml`, extract the logo from
`ppt/media/`, and build with `pptxgenjs` using those values. You are
reconstructing the design by hand, so it will be close rather than exact — take
this route knowingly, not by default.

## Checking you took design and not content

```bash
markitdown out.pptx | grep -iE "\bx{3,}\b|lorem|ipsum|\bTODO|\[insert"
```

Then read the dump end to end. Any sentence still describing the template's
original subject is a leak. So is any section heading you did not choose for
this case.

## Slides that carry a business case

Whatever the arc, these two do the work.

### The lever table

The slide everything else sets up. One row per lever, four columns: the
mechanism, what the solution measures itself, the user's assumption with a
range, and the arithmetic shown inline.

Above it, one line stating the split — that the left columns are measured and
the right are the reader's call. That sentence is what gets the room engaging
with the model instead of judging it.

Below it: inputs still needed, payback, and a plain statement that this is
scenario arithmetic rather than a forecast.

Watch the width. Four columns of arithmetic overflow easily, and a value slide
with text spilling past its box loses the room before the argument starts. If it
does not fit, cut a lever rather than shrinking the font past legibility.

### The prototype screenshot

Near full-bleed, one line of caption at most. Never a mockup drawn for the deck —
the point is that this already exists and was clicked through.

## Required QA

Run all three from the `pptx` skill. The visual pass is not optional here: a
business case is read closely by people looking for reasons to doubt it, and a
layout defect gives them one for free.

1. `markitdown out.pptx` — content, order, leftover placeholders
2. `validate.py out.pptx --original template.pptx` — file integrity
3. Render to images and look at every slide — overflow first, then overlap,
   contrast, and template decoration left stranded after text replacement
