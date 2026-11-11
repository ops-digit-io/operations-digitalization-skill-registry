---
type: Skill Reference
title: Generation pipeline
description: The seven-stage pipeline for a template-bound generated deliverable with its human gate and visual-QA loop, and the recipes for signal selection, dashboard generation, click-dummy, guided analyser and deployment set.
resource: ../SKILL.md
status: draft
tags: [all, practice, ai]
---
# Generation pipeline

Pattern shared by every recipe: **fixed-structure inputs -> importable or reviewable output -> expert
validation on the running artefact -> missing-input table up front -> visual QA loop.** Step ids refer to
the process chain.

## 1 The pipeline for a template-bound deliverable (any step that produces a document or deck)

1. **Read the context by relevance** (`od-context`; stale sections stop the run, `od-context-freshness`).
2. **Read the template and its layouts** from the approved master (`od-template-resolution`).
3. **Human gate on what cannot be derived:** lane, depth, language, audience. The agent asks; it does not guess.
4. **Map fields to template elements, one source per element.** An element without a source stays empty.
5. **Apply the honesty rules:** open ("to confirm") items stay out of the artefact and go on a list.
6. **Build, render, inspect, fix - loop.** Look for overflow, invisible text, low contrast, clipped
   bullets. Repeat until the render is clean.
7. **Deliver editable,** with a validation (every element has a source) and a placeholder-leak check (no
   `<...>` left in the visible output).

Human stays on: the step-3 choices, review before the audience, closing the open items, confirming that
figures are still current.

## Signal selection (step 22; feeds 23 and 3b4)

Without AI the work is slow and error-prone: scan the tag list by hand, interview the domain expert at
the HMI, iterate proposal and correction over several sessions, map to identifiers that are hard-coded
into queries, and find during the test that a datapoint is not collecting.

With AI:

- **Inputs:** datapoint export (identifier and label only), requirements text, optionally an HMI
  screenshot and an equipment reference; equipment context (known signal paths, scaling conventions,
  thresholds) is carried in the skill or context pack.
- **Method:** match by label suffix scoped to the device, drop archived points, group the matches into
  query patterns (trend, latest, event-anchored, scaled).
- **Output order:** the **missing-signal table first** (`signal id | label | why needed`), then the
  matched proposal with the rule used per match ([`assets`](../assets/missing-signal-and-binding-table.md)).
- **Validation:** the domain expert reviews the proposal on a **running dashboard**, in one focused
  session, not as a spreadsheet.
- **Handoff:** missing signals go to the information-integration lane (`od-signal-standardization`,
  `od-data-availability-check`); they are not approximated. Units and scaling are written into the
  panel description.
- **Pitfalls:** no naming convention across plants, cryptic or foreign-language labels, scaling that only
  people know, no plausibility check ("garbage in, garbage out").
- A sensor value is not an event: derive events from boolean or discrete tags on purpose, and check
  where object identifiers (order, part, tool, recipe, serial) live before promising an analysis
  (`od-data-availability-check`).

## Dashboard generation (step 23, 1a2)

- **Inputs (fixed structure):** tag list with labels, requirements as text, optionally a reference
  dashboard as a configuration file. Time-series data is not needed.
- **Flow:** handover prompt -> dashboard configuration -> import and test -> iterate -> handover. The
  import and test is short; iteration is bounded; compare this with the manual route where offline
  signal analysis and iteration with the expert dominate.
- **Side outputs worth keeping:** the iterated tag list, the machine-specific process description and
  documented domain knowledge, the refined requirements.
- **Evidence to cite:** which tag matched which requirement; which panel uses which query pattern.
- **Gate:** the domain expert judges the result at the point of use; requirements are approved by the
  requester. A dashboard without an action owner is a build smell (`od-analytics-asset-build`): the
  utilisation moment is named before the build, and the handover carries the ritual of use
  (`od-handover-and-adoption`).
- Reuse the dashboard family (overview for supervisors, operations view for technicians, process-value
  view for diagnosis) rather than generating one-off layouts.

## 4 Other generation recipes

| Recipe | Step | Input | Output | Gate / rule |
|---|---|---|---|---|
| Click-dummy | 23 | refined requirements (atomic, testable, one vocabulary, assumptions parked as open issues) | clickable mock-up and a product video, not a wireframe picture | Plant users review it; it answers "do they understand and want it" only (`od-prototype-poc`) |
| Guided ML analyser (cycle time, downtime) | 23 | raw signals plus business context (machine, grouping such as part or recipe or tool, plausibility range) | signal proposals for start and stop, model, cycle time and ranked influencers | Human interaction is mandatory at tuning and deployment; abnormal values go to notification; a rule-based per-machine solution does not generalise, ML only where generalisation and influencers are the value |
| Deployment set | 3a4 | source and deployment files, or image and deployment files, plus the sourcing route | deployment, service, config map, namespace, probes, resources | Agent drafts from a template because the structure is fixed; Cyber Security sign-off and deployment into the shared platform stay human (`deploy-appstore`, `od-cybersec-gate`) |
| Flow documentation | 3b4 | flow configuration file | purpose, flow functionality, node functionality | Owner confirms; entry goes to the flow library |
| Tag-selection list | 3b4 | controller type, tag export | proposed tag list and integration option, citing the guide step | Cyber Security approval and procurement are gates |

Platform-migration reminder for any deployment set: runtime licences of some servers are bound to one
machine, so the licence key must be available before a migration; also confirm new DNS, certificates and
access carry-over.

## 5 Visual-QA loop in practice

Render -> inspect against a fixed checklist (overflow, invisible text, contrast, clipped text, leftover
placeholders, units on every number) -> fix -> render again. The loop ends on a clean render and the
placeholder-leak check, not on "looks fine". An agent that cannot render the artefact says so and does
not claim the check was done.

## 6 Pitfalls and how to spot them early

- Output without a binding or evidence table: nobody can check it; treat as draft.
- Open items quietly filled in the artefact: search the output for values with no source field.
- First delivery treated as final: requirements change; schedule an explicit iteration after first
  delivery.
- Approximated signal in place of a missing one: the missing-signal table is empty although the
  requirements mention signals not in the export.
- Generated artefact reported as proven value: see `od-prototype-poc` status labels.
