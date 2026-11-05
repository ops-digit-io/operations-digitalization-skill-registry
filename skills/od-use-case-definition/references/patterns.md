---
type: Skill Reference
title: Patterns
description: The abstract rules this procedure runs on, each illustrated once against a real use case.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, patterns]
derived_from:
  - personal vault, Graph/Use Cases/*.md and Graph/Library Use Cases/*.md, read 2026-09-17
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Patterns

## Match effort to category

A `standard` use case inherits its objective from the capability template — write only the
plant-specific delta (which lines, which machines). A `non-standard, unique to one plant`
use case has no template behind it, so Analyse and Assess have to carry the whole
specification, or nobody downstream can build it.

An OEE-calculation instance (illustrative: a template instantiated at nearly every plant)
needs one line: *"OEE Dashboard - for <line A> and <line B>."* It still ships and runs daily.
A custom alarm notification (illustrative: custom Node-RED alarming logic, no template) needs the
full chain: a diagnosed problem, named machines, exact thresholds. Same depth of
"definition," opposite amount of writing, both correct — because the template did or didn't
already carry the objective.

Declaring `standard` to skip the writing, rather than because the template genuinely fits,
is the thing `SKILL.md`'s guardrails exist to catch.

## A decision is not a scope

Priority, potential and savings get filled on the benefit-calculation cadence — a schedule
of their own, independent of whether Phase 2 (Analyse) ever produced a stated objective. A
filled priority tells you a number was calculated; it tells you nothing about whether the
problem was ever diagnosed. Check the objective directly before trusting the priority as
informed.

## The legacy-system check is tacit knowledge, not a lookup

"Assess the (legacy) MF IT systems it touches" has no system of record to search — it is a
question you ask the plant and the DBVE each time, answered from memory. Do not go looking
for it in a use-case record and conclude "none" when it isn't there; conclude "not asked
yet."

## A blocked use case is a finding, not a failure

An analytics use case (illustrative: a process step as the likely root cause of leaking parts) was correctly
diagnosed and then correctly stopped at Assess, because the machine it needed was
never even scheduled for integration. That's not a data-availability gap
`od-data-availability-check` can close, and it isn't a requirement-breakdown problem — it's
a prior decision (no integration plan for that equipment) that has to be revisited above
this skill's authority. Recording *which* phase a use case stalled in, and why, is the
point; an unexplained `IDEA` sitting untouched is the actual failure mode, not the stall
itself.

## A capability being instantiated is not evidence a use case exists

A plant carrying a capability epic (the record that says "this plant has an OEE
Calculation instance") is not evidence anything was built — many capability-epic records
group no use case at all; the capability was declared, not delivered. Checking that the
plant "has the capability" answers a different question than checking whether a working
reference exists to take instead of specifying from scratch. Check
`references/library-catalog.md` directly; do not infer a usable precedent from the
capability coordinate alone.

## A fleet use case is not a scaled-up single-machine one

A use case naming one or two machines is usually a single-line or single-cell diagnostic. A
use case naming ten or more is usually a fleet-level Andon or OEE capability — a different
shape of problem, not the same one repeated. Check which the category and the Collect-phase
ritual actually imply before scoping it as either.
