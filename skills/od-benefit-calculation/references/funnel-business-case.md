---
type: Skill Reference
title: Funnel business case
description: "The department's business-case stage of the product funnel (bc-build): value model from the features and prototype, savings model, auditable deck."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, funnel, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `product-funnel-skills.zip/skills/business-case/SKILL.md` (the master).

# Business Case

Turn a validated prototype into a defensible value story and a deck someone can
present.

Final stage of the chain: `requirements-funnel` → `feature-funnel` →
`click-dummy` → **`business-case`**.

## Core Principle

**Separate what is measured from what is assumed, visibly, on the slide.**

A business case collapses the moment someone in the room cannot tell which
numbers came from the system and which came from the author's optimism. Keep the
two in different columns, label them, and let anyone recompute the arithmetic in
their head. A model that survives challenge is worth more than a model with a
bigger number.

<HARD-RULE>
Never invent a financial input. Hourly rates, margins, scrap costs, volumes and
headcount are the user's to supply — asking costs one message, and a fabricated
rate discovered in the room discredits every other number on the slide. If the
user does not have a figure, use a clearly-labelled placeholder and list it under
inputs still needed. Never quietly substitute an industry average.
</HARD-RULE>

## Stage 1 — Gather the Inputs

Read `feature-book.md` and `prototype-notes.md`. If the requirements artifact
carries a `baseline` block, that is the as-is cost and the comparison is
already grounded — use it.

**If there is no baseline, get one now.** A value claim needs a before. Ask what
the process costs today: how often it runs, how long it takes, how often it is
redone, and who is blocked meanwhile. Estimates are acceptable if labelled.

Then ask for the money, in one batch rather than one at a time. Which apply
depends on the domain:

| Input | Needed for |
|-------|-----------|
| Loaded hourly rate (person or machine) | Converting hours saved into money |
| Annual volume or run frequency | Scaling per-run savings to a year |
| Contribution margin per unit | Valuing throughput gains — only if capacity is sold out |
| Scrap or defect cost per unit | Valuing quality improvements |
| Headcount touching the process | Sizing adoption effort and change risk |
| Build and rollout effort | Payback period |

**Throughput is worth nothing unless the extra output can be sold.** Ask
directly whether the line or team is capacity-constrained. If it is not, count
the saving in hours released, not in units produced — and say so on the slide.
Nothing discredits a case faster than a capacity manager recognising phantom
revenue.

## Stage 2 — Build the Model

One row per **lever** — a distinct mechanism by which value appears. Three or
four levers is right; more reads as padding and invites line-item argument
rather than a decision.

Each row carries four columns, in this order:

| Column | Contains |
|--------|----------|
| **Lever** | The mechanism, in the business's words |
| **Measured by** | What the solution itself observes — the evidence |
| **Scenario assumption** | The user's judgement call, with a range |
| **Annual value** | The arithmetic, shown, not just the result |

The second and third columns are the whole point. The left is what the system
knows; the right is what the user is choosing to believe. Anyone can then attack
the assumption without attacking the measurement, which is exactly the argument
you want to have.

**Give assumptions ranges, not points.** "Close ⟨x⟩% of the gap (range ⟨low⟩–⟨high⟩%)"
invites a conversation; "saves ⟨x⟩%" invites disbelief. Compute the headline at
the middle of the range and note what the low end yields — a case that still
works at its pessimistic end is far more persuasive than one that only works at
its optimistic one.

**Show the arithmetic inline.** `⟨runs⟩ runs × ⟨h⟩ h × ⟨share⟩ = ⟨hours⟩ h/yr ×
€⟨rate⟩/h`. If a reader cannot follow it across the page, it is not auditable, and
unauditable numbers get discounted to zero by anyone senior.

**Payback:** build and rollout effort ÷ (annual value ÷ 52) = weeks. State the
effort as a number, not a feeling.

Label the whole thing what it is: **scenario arithmetic, not a forecast.** This
is not modesty — it is what lets a sceptical reader engage with the model
instead of dismissing it.

## Stage 3 — Build the Deck

### Ask for a template, and take only the design from it

A template supplies the **visual shell**: masters, layouts, theme colours and
fonts, the logo, and the footer treatment. A deck in the organisation's own
design is read as the organisation's work rather than an outsider's proposal,
which is most of why it is worth using one.

<IMPORTANT>
Take the design, not the content. A template deck's own slide text is whatever
that deck was about — it is a sample, not a specification. Do not carry its
section headings, its column captions, or its slide count into this deck, and do
not reshape the business case to fit the sample's arc. Content comes from the
model built in Stage 2; the template decides what it looks like.
</IMPORTANT>

Mechanics for harvesting a template without inheriting its content, and how to
map content onto its layouts: `deck-structure.md`. Follow the `pptx`
skill for the unpack, edit, repack and validate cycle.

### Let the case decide the slides

Build the deck the argument needs. A default arc that works, to adapt rather
than follow:

1. **Title** — what it is, and the value in one sentence
2. **The problem** — what it costs today, from the baseline
3. **The solution** — the prototype, as a screenshot
4. **What it is worth** — the lever table, inputs needed, payback
5. **What it takes** — effort, rollout, what scaling costs

Add, merge or drop slides as the case requires. A strong case with two levers
does not need a slide per lever; a case that has to win over four departments
may well need a slide naming what each of them decides today without evidence.

The one slide that always earns its place is the lever table. Everything else is
setup for it.

Screenshot the prototype rather than describing it — the whole reason it exists
is that people believe what they can see. Capture the state that best shows the
comparison the case rests on, not the default view.

## Stage 4 — State the Limits

On the slide or in the notes, not buried:

- Which figures the user supplied and which the solution measured
- Which inputs are still missing, and what they would change
- What the value depends on — adoption, data quality, a decision not yet taken
- What is explicitly **not** claimed

A case that names its own weak points is treated as honest and gets challenged
on its merits. One that hides them gets challenged on its credibility, and loses
even when the numbers were right.

## Red Flags

| Thought | Reality |
|---------|---------|
| "I'll use a typical industry hourly rate" | Then every number below it is fiction. Ask. |
| "Bigger number, better case" | A number nobody can recompute gets discounted to zero. Auditable beats large. |
| "Throughput up ⟨x⟩% = ⟨x⟩% more revenue" | Only if the extra output sells. Ask whether capacity is the constraint. |
| "One value figure is cleaner than a range" | A point estimate invites disbelief; a range invites a conversation. |
| "Six levers show more value than three" | Six levers read as padding and move the discussion to line items. |
| "I'll show the totals, not the arithmetic" | Then it cannot be checked, so it will not be trusted. |
| "The prototype's limitations weaken the pitch" | Naming them is what makes the rest credible. |
| "The template deck had six slides, so mine has six" | A template is a design, not an outline. Its slide text is whatever that deck was about. |
| "I'll reuse the template's section headings" | Then the deck argues that deck's case, not yours. Take masters, layouts, theme and logo only. |
| "Soft benefits are still benefits" | Put them in a separate, unpriced list. Mixing them into the arithmetic taints the hard numbers. |

## Chaining

- Runs **after**: `click-dummy`
- Reads: `feature-book.md`, `prototype-notes.md`, and the `baseline` block from
  `requirements-funnel-output.md` if as-is mode was used
- Uses: the `pptx` skill for deck production
- Produces: `business-case.md` (the model, auditable) and the presentation
