---
type: Skill Reference
title: Benefit theory
description: The Benefits Dependency Network, adapted to the four phases - why a dashboard is not a benefit, what closes the Implemented-to-Productive gap, and how to classify a benefit before it reaches od-benefit-calculation.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, benefits, method]
---

# Benefit theory

> **Sourcing.** External methodology, not knowledge base-derived — cited inline. The Benefits
> Dependency Network is Cranfield School of Management's model for IT-enabled change
> (Peppard, Ward & Daniel, 2007, *"Managing the Realization of Business Benefits from IT
> Investments"*); the options discipline is PRINCE2's Business Case practice. Both are
> adapted here to this department's four phases, not reproduced in general form.

A use case can be fully built, connected and handed over, and still deliver nothing. This
registry already names that failure without naming its cause: handover trails development
and implementation by about thirty use cases, and `IMPLEMENTED` and `PRODUCTIVE` are
tracked as separate states precisely because something can be built and not used (see
`SKILL.md` § *The states it will be tracked in*). The Benefits Dependency Network names the
missing link: **the technical enabler and the business benefit are connected by a change in
what someone does — and that change is usually the part nobody wrote down.**

## The chain, mapped to the four phases

| Link | Question it answers | Produced in |
|---|---|---|
| **Investment objective** | Why does this matter to the plant or the department, beyond this one request? | Collect |
| **Business benefit** | What measurably improves, and for whom? | Analyse |
| **Business / process change** | What will someone do differently once this exists — and who confirms they actually do it? | Control |
| **Enabling change** | What has to be true in the systems and machines first? | Assess |
| **Technical enabler** | What gets built? | Control (output asset) |

Read it as a chain, not a checklist: a technical enabler with no named business/process
change is a change with nothing to make it happen, which is a benefit that will not land.
**A dashboard is not a benefit. The decision someone makes differently because the
dashboard exists is the benefit — name that decision, not the dashboard.**

The illustrative `Alarm Notification` use case (full record in `references/worked-examples.md` §1) has
this chain, even though nothing in a typical original record labels it as one:

| Link | What it actually was |
|---|---|
| Investment objective | Stop energy loss and silent quality loss in a thermal process |
| Business benefit | Fewer wasted heating cycles, fewer unrecoverable loads |
| Business / process change | Shop-floor personnel receive a Teams alert and decide, inside the stated window, whether to intervene — a decision nobody was making before, because nobody knew |
| Enabling change | Node-RED gateway reading PLC signals directly, no IT-network dependency |
| Technical enabler | The Analytics Workflow itself |

The middle link — who decides what, now, that they couldn't before — was never written
down as its own field. It's recoverable here because the target text happened to describe
it in passing. Make it a required field instead of hoping it survives in the prose.

## Classify the benefit before it reaches benefit-calculation

Two independent axes. A benefit can sit anywhere in the grid — cashable is not "the real
kind" and intangible is not "not a benefit":

| | **Cashable** (a budget line shrinks) | **Non-cashable** (capacity freed, not removed) |
|---|---|---|
| **Tangible** (countable) | Headcount reduced, scrap material saved | Hours freed for other work, cycle time reduced |
| **Intangible** (not countable) | — (rare; cashable benefits are usually countable) | Fewer missed escalations, faster decisions, less firefighting |

This feeds directly into `od-benefit-calculation`'s existing `savings / lead-time
reduction / cost avoidance` categories — classify here, calculate there. It also explains
why `potential` is `UNKNOWN` on many use cases without that being a recording failure: an
intangible, non-cashable benefit is real and still resists a number. `od-benefit-calculation`
already states the rule this classification exists to support: *"do not read a missing
figure as zero value."* Classify the benefit as intangible/non-cashable explicitly, rather
than leaving the field blank and indistinguishable from "never assessed."

## Options considered, before committing to a build

PRINCE2's business-case discipline, reduced to what this phase actually needs: name what
else was on the table before choosing a bespoke build.

- **Do nothing** — the cost of the status quo, stated plainly. If nobody can say what
  continues to go wrong, the use case is not yet justified.
- **The closest library entry** — see `references/library-catalog.md`. If it fits, this is
  not a new definition; it's an instance.
- **A smaller scope** — the same objective, fewer machines or one plant instead of a
  rollout wave.
- **The full bespoke build** — chosen because the first three were considered and rejected,
  not because it's the first thing anyone thought of.

Naming the rejected options costs one sentence each and is what makes "we need a custom
build" a decision instead of a default.
