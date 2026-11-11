---
type: Skill Reference
title: Library catalog
description: How to search the use-case library (proven reference solutions) by capability, what a good entry looks like, and the lean-method vocabulary - a how-to-get-it guide to the live list, with no entries, counts or plant names copied.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, library, elicited]
---

# Library catalog (how to search it)

The Phase 3 (Assess) step "check the library before specifying" points at `catalog-standardization`. The library is a set of
reference solutions, each a real dashboard or app built at one plant and available as a starting point for another. Read the
closest match before drafting a new definition from scratch: most of what a new use case needs has usually been built once.

**This file used to copy the entries. It no longer does** (a copied list is a snapshot of the estate that goes stale). Get the
live content here instead:

| Where | What you get |
|---|---|
| SharePoint list **UseCase Library** (write surface) | One row per reference solution: name, plant, capability link, description, method tag, CSP decision |
| Knowledge base `Graph/Library Use Cases/` (read surface, rebuilt from the list) | One note per entry, searchable by name and text |
| Knowledge base `Case Groups` notes | The same use cases grouped by template and process family, with a rollout map per plant |

## How to search

1. **Filter by capability first.** The capability groups are the cross-plant templates: Process Values, Analytics, Cycle Time,
   Downtime Reporting, Andon Board, Process Quality Data, Machine Alerts, OEE Calculation, Manual Quality Data (and
   the catch-all for entries with no capability link, labelled `Unlinked`). Check the `Unlinked` entries too when nothing in the
   matching group fits.
2. **Then scan descriptions for the signal and the decision**, not for the plant: what is measured, against which reference,
   over which window, and who reacts.
3. **Read the CSP decision field.** A library entry is a proven reference solution; only a recorded CSP `Yes` makes it standard
   enough to roll out (`dept-decision-rights`). Count the `Yes` entries live; do not assume.
4. **Take the closest one and record only the delta** (which lines, which machines, which thresholds).
5. **If nothing fits**, say so in the definition: "no library match" is itself a finding and goes into the Assess section.

## What a good entry description looks like (pattern to copy)

An entry that is easy to reuse states, in one or two sentences: what it monitors or calculates, against which setpoint or target,
over which time window (shift, 12 h, 24 h), the visual device (color-coded cells, Pareto, heatmap, status timeline), and the decision it
supports (which machine or parameter the supervisor should look at). Poor entries state only the area ("Production
Attainment") or a plan ("planned for all assembly lines"); upgrade them when you reuse them.

## Method tags (the department's own lean vocabulary)

Where a `[Method]` tag appears, it is the lean / continuous-improvement method the plant recorded behind the solution - real
vocabulary, not a classification imposed here:

- Gemba Management
- Visual Management
- Jidoka
- 5S
- Total Productive Maintenance
- Workplace Design
- "No method reference" (explicitly tagged as such)

Many entries carry no method tag; unrecorded is not method-free. Use a tag when a use case's method genuinely matches one, and
leave the field blank rather than force a tag onto a use case that fits none. Count tags live if you need the mix.
