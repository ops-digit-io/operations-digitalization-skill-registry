---
type: Skill Reference
title: Ecr builder workflow
description: "The department's eCR builder workflow in five steps: ingest a folder plus the chat, refusal gate, grounded backbone, colour-coded honesty deck, maturity verdict."
resource: ../SKILL.md
status: draft
tags: [capital-request, ecr, workflow, department-package]
---
> Transcribed from the department package `ecr-builder.zip/SKILL.md` (the master).

# eCR builder

Turn whatever material exists for a capital request — a folder of quotes, a
savings spreadsheet, an e-mail thread, meeting notes, a rough business case — into
a clean, auditable eCR **Management Summary** deck in the neuwerk brand. The point
is not to make a pretty deck fast; it is to make an **honest** deck: one where a
reviewer can see exactly which numbers are real, which are our estimates, and what
still has to be answered before it can be signed.

Two commitments run through everything below, and they are the reason this skill
exists rather than "just make the slides":

> **Grounding rule — never invent information that you cannot derive from the
> material, a question back, or public web material. Mark low-confidence points.**

> **Refusal gate — refuse the creation if inputs on the business case are far too
> risky to assume, and propose de-risk questions before creating.**

Everything is rendered in **English** (project rule), even when the sources are in
German — translate for the deliverable, keep proper nouns (neuwerk, plant names,
programme names) as-is.

## Setup — where the files live

The render engine and the four reference files are packaged at
`OD-instance/30-skills/ecr-builder.zip`. If a `` or `assets/` folder is
not already beside this SKILL.md, extract the zip into a working directory first:

```bash
unzip -o "<OD-instance>/30-skills/ecr-builder.zip" -d ecr-builder-work
```

Then the paths below (`…`, `../scripts/build_ecr.py`) resolve relative to that
extracted folder. The neuwerk template ships inside the zip as
`assets/_nw_template.pptx`.

## The five-step workflow

1. **Ingest.** Gather every source: the folder the user points at (read each file),
   plus anything stated in the chat. Make a short inventory — one line per source,
   what it contributes. Do not start slides yet.

2. **Gate (grounding + refusal).** Before compiling, run the refusal check in
   `open-items-and-conflicts.md`. If the core value drivers can't be
   responsibly derived, stop and return de-risk questions instead of a deck.

3. **Compile the backbone.** Write a layered-markdown backbone (see
   `backbone-and-conditionals.md`) that maps the material onto the eCR
   sections and carries a **grounding tag on every figure**. This markdown *is* the
   intermediate deliverable that feeds the deck — save it next to the pptx.

4. **Challenge & tag.** Apply the challenge principles and the colour code in
   `grounding-and-color-coding.md`: mark our own assumptions, flag
   low-confidence points, and separate grounded facts from estimates.

5. **Render + close.** Fill the `CASE` data in `../scripts/build_ecr.py`, build the
   deck, and author the final **Open items & conflicts** slide from what you found.
   QA the render (`../scripts/render_qa.sh`) and deliver the pptx + the backbone md.

## What "grounding" means in practice

Every number on every slide is one of four things, and it must be marked as such —
this is the heart of the skill, expanded in `grounding-and-color-coding.md`:

- **grounded** — stated in the source material. Printed plainly, no chip.
- **assumption** — our own estimate, defensible but not in the sources. Marked with
  an amber **A** chip and a `[a]` tag in the backbone. We own it.
- **market/standard** — a standard value used *because none was given* (e.g. a duty
  rate, a WACC). Marked with a blue **M** chip / `[m]` tag, and added to open items.
- **low confidence / unknown** — a crucial input we could not derive and refuse to
  fake. Marked with a red **?** chip / `[?]` tag, never silently turned into a
  confident number, and carried to the Open-items slide as a top question.

Small immaterial gaps are fine to assume quietly. Big value-driving numbers that
rest on a guess are **never** printed as fact — they are flagged, ring-fenced as a
sensitivity, or (if too central) they trigger the refusal gate.

## The two things this skill adds beyond a normal deck

**A colour-coded honesty layer.** The reader can tell at a glance what is real. The
exec-summary slide carries the full legend once; tagged figures elsewhere carry the
chip. This is a direct sibling of the `bc-assessment` skill's grounding tags — if
that skill is present, keep the two consistent.

**A final "Open items & conflicts" slide** (modelled on the bc-assessment
provenance/conflict backup slide). Left column: the open questions that would
sharpen the case, each with why-it-matters and an owner. Right column: every place
the base material *disagreed with itself* (two different capex numbers, a baseline
that changed between drafts, a figure in one file not carried into another) and how
you resolved it. A verdict band states the maturity: *Ready to sign* / *Sign the
floor, validate the upside* / *Not ready*. `../scripts/build_ecr.py` renders this from
an `open_items` + `conflicts` + `verdict` block — see
`open-items-and-conflicts.md`.

## Reference files — read the one you need

- `backbone-and-conditionals.md` — the eCR section map (1 Exec summary …
  9 Timeline + Backup), the layered-markdown format to compile, and the governance
  conditional rules (when sensitivity is mandatory, GPA vs non-GPA/RPE, when the
  growth/value field and layout apply). **Read before compiling.**
- `grounding-and-color-coding.md` — the four grounding tags, the slide
  colour legend, and the challenge principles (what to interrogate in the material
  before you trust it). **Read before tagging.**
- `open-items-and-conflicts.md` — the refusal gate (with the de-risk
  question bank and the threshold for "too risky"), and the spec for the final
  slide. **Read at step 2 and step 5.**
- `build-engine.md` — how to fill the `CASE` data and run
  `../scripts/build_ecr.py`; the helper library, slide-type functions, and neuwerk
  brand rules (Navy/Sun budget, Poppins/Lora, semantic colours, footer indices).
  **Read before rendering.**

## Delivering

Save two things to the user's workspace: the compiled backbone markdown
(`eCR_<slug>_backbone.md`) and the rendered deck (`eCR_<slug>_neuwerk.pptx`).
Lead the reply with the deck link and, crucially, a one-line honesty summary — how
many figures are grounded vs assumed, and the single most important open question.
If you refused, deliver the de-risk questions instead and say plainly why.
