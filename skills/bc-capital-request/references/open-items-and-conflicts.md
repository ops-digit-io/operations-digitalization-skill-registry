---
type: Skill Reference
title: Open items and conflicts
description: "The refusal gate before compiling (when inputs are too thin, stop and return de-risk questions), the de-risk question bank, and the closing Open items and conflicts slide."
resource: ../SKILL.md
status: draft
tags: [capital-request, ecr, department-package]
---
> Transcribed from the department package `ecr-builder.zip/reference/open-items-and-conflicts.md` (the master).

# Refusal gate + the "Open items & conflicts" final slide

Two related things live here: the **gate** that decides whether a deck should be
built at all (step 2), and the **final slide** that records what remains open and
where sources disagreed (step 5). Both express the same discipline — be honest about
what isn't known.

## The refusal gate (step 2, before compiling)

Verbatim rule:

> **Refuse the creation if inputs on the business case are far too risky to assume,
> and propose de-risk questions before creating.**

### How to decide "too risky"

Look at the **core value drivers** — the handful of figures the decision actually
turns on. For a typical eCR these are: (1) the capex / request amount, (2) the
volume or activity base, (3) the unit saving or price delta, and (4) the baseline
being improved on. Tag each `[input]` / `[a]` / `[m]` / `[?]` as best the material
allows, then apply:

- **Build normally** if the value drivers are mostly grounded, or the assumptions
  are small and clearly ownable. Mark them and proceed.
- **Build the floor, flag the upside** if the *structure/logic* is grounded but the
  *magnitudes* are estimates. This is common and fine: build the deck, tag every
  euro, and set the verdict band to "Sign the floor, validate the upside". A single
  data round will firm it.
- **Refuse** if **two or more core value drivers are `[?]`** (crucial and
  underivable), or if the central decision (make-vs-buy, go-vs-no-go) rests entirely
  on a number nobody can source. A deck here would look authoritative while being
  fiction — exactly what the grounding rule forbids.

When you refuse: do **not** produce slides. Return a short, plain-language note that
says which drivers can't be responsibly assumed, and a **de-risk question bank** —
the specific questions (and who owns each) that would move each `[?]` to `[input]`.
Offer to build the moment the answers come back.

### De-risk question bank (adapt to the case)

- **Capex** — is there a supplier quote (or three) for the request amount, or is it
  a rough budget line? Who can confirm the installed cost?
- **Volume** — is the volume from a signed OEM call-off / order book, or an internal
  forecast? What is the year-1 committed volume vs break-even?
- **Saving basis** — what exactly is the current-state (baseline) cost, and is it
  measured or estimated? What drives the unit delta (freight, duty, labour, scrap)?
- **Rates** — which duty %, FX, WACC, depreciation life were used, and are they the
  official Controlling values?
- **Timing / thresholds** — realization months and total amount (do they cross the
  EUR 1M / 24-month sensitivity threshold)? SOP date committed?
- **Governance** — investment class (Expansion → growth field?), Right-of-Use (IIR?),
  make-or-buy done, EHS/quality/IT-footprint cleared?

## The "Open items & conflicts" slide (step 5, always the last body/backup slide)

Modelled on the `bc-assess` provenance/conflict backup slide. Rendered by
`open_items_conflicts(open_items, conflicts, verdict)` in `build_ecr.py`.

**Verdict band (top).** One line: the maturity label + a sentence. Labels:
`Ready to sign` (green) / `Sign the floor, validate the upside` (periwinkle) /
`Not ready` (red — and if you got here you probably should have refused).

**Left column — Open questions to sharpen.** The questions that would raise
confidence, each: the question, a *Why* line (why it matters / what it moves), an
*Owner*, and a chip for the residual tag (`a` / `m` / `?`). Order by value-at-stake.
These come straight from your `[a]`/`[m]`/`[?]` figures and any de-risk questions
that were answered "later".

**Right column — Conflicts in the base material.** One card per place the sources
disagreed with each other, on Melon. Each: the conflict, the *Sources* it spans, and
*Resolved:* — which version the deck adopted, why, and the residual tag in brackets.
Typical conflicts to hunt for:
- two different values for the same figure across two files (e.g. capex ⟨amount A⟩ vs ⟨amount B⟩);
- a baseline or formula that changed between an early draft and the final;
- a number in one document not carried into another;
- a leading/throwaway figure deliberately *not* enshrined;
- single-source figures (record the caveat).

If there were genuinely no conflicts, say so in one card rather than inventing them —
"no material conflicts across sources" is a legitimate, useful finding.

## Mirror it in the reply

The one-line honesty summary you lead the delivery with is the written twin of this
slide: e.g. *"14 of 19 figures grounded; capex and volume are assumptions to
confirm; top open question: verify the ⟨x⟩% duty rate with Trade Compliance."*
