---
type: Skill Reference
title: Dependencies
description: Which focus-area levels require which others first, the source table's own reliability caveat, and the recommended backbone chain for sequencing a gap.
resource: ../SKILL.md
status: stable
tags: [use-case-evaluation, maturity-model]
---
# Realization dependencies

A target level can only be planned once its prerequisites exist. `scripts/evaluate_fit.py`
reads the same table from `model_data.json` to flag a gap as "ready now" or "blocked on
`<code>`" — this file is its source and its honesty caveat.

## The source table is a starting point, not a mechanical sequencer

The published dependency table uses an inconsistent level-numbering scheme across its own
rows; reading every prerequisite one level higher than printed (the "best-fit" reading used
throughout this skill) is the version that actually reproduces the paper's own published
development-path examples — but even under that reading, several real sequencing decisions
in the source material are not explained by the table at all. The tool that produced them
evidently used further, unpublished dependencies (plausible ones: real-time collection needs
standardized protocols or a partly-continuous information model; predictive analytics needs
real-time data; hybrid control needs predictive analytics or combined storage/processing).

**Consequence:** treat the table below as where to start a sequence, not as an authority to
plan a roadmap against mechanically. Validate it against this registry's own architecture —
`mi-equipment` and `mi-signals` are the skills that know what is
actually true for this estate's connectors and data model — before committing to an order.

## Full table (best-fit reading)

| Target | Requires |
|---|---|
| `C1-2` (anonymously known) | none |
| `C1-3` (individually known) | none |
| `C1-4` (managed as an entity) | `C2-2` (passive), `C12-2` (outsourced) |
| `C2-2` (passive) | `C1-2` (anonymously known), `C9-2` (cable-based) |
| `C2-3` (active) | `C1-3` (individually known) |
| `C2-4` (compliant to the service system) | `C1-4` (managed as an entity), `C10-4` (undefined 4th level) |
| `C3-2` (data handling) | `C1-4` (managed as an entity), `C2-2` (passive), `C9-2` (cable-based), `C13-2` (outsourced) |
| `C3-3` (information recognition) | `C2-3` (active), `C13-3` (combined), `C14-2` (descriptive) |
| `C3-4` (decision ability) | `C2-4` (compliant to the service system), `C12-4` (embedded), `C14-5` (prescriptive) |
| `C4-2` (localizable) | `C1-3` (individually known), `C2-2` (passive) |
| `C5-2` (partly mobile) | `C2-2` (passive), `C4-2` (localizable), `C9-3` (wireless), `C12-3` (combined) |
| `C6-2` / `C6-3` (partly / fully automated) | none |
| `C6-4` (modularly automated) | `C2-4` (compliant to the service system), `C5-2` (partly mobile), `C10-3` (standardized), `C15-2` (centralized) |
| `C7-2` (analogous) / `C7-5` (AR/VR) | none |
| `C7-3` (digital, stationary) | `C8-2` (technical), `C16-2` (partly continuous) |
| `C7-4` (digital, mobile) | `C9-3` (wireless) |
| `C8-2` / `C8-3` (technical / natural) | none |
| `C9-2` / `C9-3` (cable-based / wireless) | none |
| `C10-2` / `C10-3` (proprietary / standardized) | none |
| `C10-4` (undefined 4th level) | `C16-2` (partly continuous) |
| `C11-2` (historical) | `C2-2` (passive), `C15-1` (no control system) |
| `C11-3` (real-time) | none |
| `C12-2` (outsourced) | `C2-2` (passive) |
| `C12-3` (combined) | `C3-2` (data handling) |
| `C12-4` (embedded) | `C2-3` (active), `C3-3` (information recognition) |
| `C13-2` (outsourced) | none |
| `C13-3` (combined) | `C3-2` (data handling) |
| `C13-4` (embedded) | `C3-4` (decision ability) |
| `C14-2` (descriptive) | `C16-2` (partly continuous) |
| `C14-3` (diagnostic) | `C11-3` (real-time) |
| `C14-4` / `C14-5` (predictive / prescriptive) | none |
| `C15-2` (centralized) | `C12-3` (combined), `C13-3` (combined), `C14-5` (prescriptive), `C16-2` (partly continuous) |
| `C15-3` (hybrid) | none |
| `C16-2` (partly continuous) | none |

Levels the source table lists with no prerequisite at all (`none`) are not automatically
free — they simply have no *published* dependency. F11 real-time, F14 predictive/
prescriptive and F15 hybrid are the three documented cases where the source material itself
admits the published table undersells the real prerequisite chain (see above).

## Recommended backbone, for sequencing a gap this table does not fully explain

1. **Connectivity and segmentation** — F9: every relevant asset networked, in a segmented
   OT network.
2. **Identity** — F1 level 3: unique IDs, one registry.
3. **Open protocols** — F10 level 3; F2 level 3 (event-driven).
4. **Semantic model** — F16 level 2 per domain: a defined hierarchy and payload
   conventions.
5. **Real-time state and history** — F11 level 3 for decision-relevant signals; F12/F13
   "combined" with a managed edge.
6. **Analytics ladder** — F14 descriptive -> diagnostic -> predictive, per use case.
7. **Assist before decide** — F3 level 3 broadly, level 4 per decision with a safety case;
   F15 hybrid.
8. **Point of use** — F7 digital stationary/mobile, F8 harmonized HMI.

Steps 1-4 are foundational and worth building ahead of any single use case; 5-7 are where a
use case's own business case should carry the cost, because that is the layer where the
payoff is specific to what the use case does.
