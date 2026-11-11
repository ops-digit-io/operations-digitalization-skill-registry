---
type: Skill Reference
title: Lane templates
description: Which already-built skill's asset answers each happy-path step's template, so this lane routes to the real artefact instead of leaving a placeholder next to a skill that already has the answer.
resource: ../SKILL.md
status: stable
tags: [lane, use-case-support-service]
---
# Lane templates — route to the real artefact

A lane overview names its steps; it should not re-describe an artefact a composed skill
already owns. This is the routing table, resolved once the composed skills went deep.

| Step | What it needs | Built where |
|---|---|---|
| 3 — system assessment | A requirement spec, signals named and verified, legacy-system check | `od-requirements-breakdown`'s `assets/requirement-template.md` + `references/legacy-system-assessment.md` |
| 3 — system-fit check | Does the spec quietly need MES/EMS or a heavier read on a lightweight tool | `od-system-fit-check`'s `assets/system-fit-check.md` |
| 4 — benefit calculation | Saving rows with reliability labels | `od-benefit-calculation`'s saving-row fields (amount, year, category, methodology, reliability) |
| Before 5 — library check | Does another plant already have this | `od-use-case-standardization`'s `assets/standardization-review.md` |
| 7 — impact evaluation | Is this actually adopted, not just delivered | `od-handover-and-adoption`'s three-question test, ADKAR barrier-point diagnostic, and `assets/handover-protocol.md` |

**Why this file exists rather than a template of its own:** every one of these steps already
has a deep, maintained artefact one hop away. Duplicating it here would drift the moment the
owning skill changes. This lane's job is routing, not re-authoring.

## What is still genuinely missing

**Process First-Aid Kit request template.** Checked `od-requirements-breakdown` (covers
scoped requirements, not an ad-hoc rapid-diagnostic intake form), `od-analytical-support-
service` (names the same Process First-Aid Kit as its own trigger, with the identical open
placeholder — not independently resolved there either). No dedicated template exists
anywhere in the registry. This is a real gap, not a routing miss.
