---
type: Design Record
title: New-state conformance
description: "Every skill the new-state flow names, checked against its own text: where the skill does what the flow says, where it does less, and where the flow says something the skill does not."
status: draft
owner: human:jakob.gabriel
tags: [process-flow, lanes, conformance]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# New-state conformance

The [new-state flow](new-state-flow.md) names, for each step, the registry skill that serves it and rates that skill
Built, Partial or Gap. This page checks the 25 existing skills against the flow: for every step it looks in the skill's
`SKILL.md` and its references for the capability the flow expects.

**Method and limits.** Keyword search for the expected capability, then reading the hits. A zero count is evidence, not
proof: the skill may say it in other words. The verdicts are an AI assessment and not reviewed by a human. The five skills the
flow lists as missing now exist as drafts (see the [README](../README.md)); they are not rated here.

**Verdicts.** *Match*: the skill does what the flow expects. *Partial*: it does part of it. *Mismatch*: the skill contradicts the
flow, or the flow claims something the skill does not contain.

## Result

18 match, 5 are partial, 2 are mismatches, 3 skills are not placed on the flow. Two of the mismatches are statements in the flow
files that the registry does not support, so the flow needs correcting as much as the skills do.

## Mismatches

| Skill | Flow says | The skill |
|---|---|---|
| `od-use-case-intake-triage` | Built. Intake classifies a demand into Lane 1, 2 or 3 | Its description admits a request "into one of the four service lines" and routes by DBVE / IIAE owner. It does not mention Lane 1, 2 or 3, a known-use-case path, a catalog or self-service. It is built for the old model |
| `od-analytics-asset-build` (prototype, Lane 2 step 3) | Partial, "click-dummy only" | No click-dummy, prototype, proof-of-concept or mock-up wording in the skill or its references. Prototype / PoC is closer to a gap than to a partial |

## Partial

| Skill and step | Flow says | The skill |
|---|---|---|
| `od-analytics-asset-build`, `build-grafana-ops-dashboard` (Lane 1, apply the template, "self-service mode") | Built | They build assets from templates, but **no skill in the registry mentions self-service** or a plant applying a template itself. The mode the flow assumes is written nowhere |
| `od-acceptance-test` (Lane 3 6b, "acceptance + CS sign-off") | Built, "acceptance / CS-gate is Built" | Acceptance protocol and human-only sign-off are there. **Cyber Security is not mentioned.** The gate is written in `od-equipment-integration` (9 mentions) and `od-decision-routing` (4) |
| `od-system-fit-check` (Intake / Lane 3 tool-decision gate) | Built | Screens the lean-footprint fit with three verdicts: fits, redesign, escalate. The make / buy / integrate / connect split into 3a and 3b is not in it, and the check could not confirm it in `od-decision-routing` either |
| `od-benefit-calculation` (Lane 2 step 4, Lane 3 step 3) | Built, "value + cost" | The savings and benefit side is deep (23 mentions). The cost side appears once |

## Match

| Flow step | Skill | Note |
|---|---|---|
| Lane 1b, cost template and lightweight approval | `od-decision-routing` | Routes spend with thresholds; the cost template is an artifact, not a skill. The flow rates it Partial and the skill agrees |
| Lane 1b, order and connect; Lane 3b connector | `od-equipment-integration` | Procurement, connectors, standards. Also holds the Cyber Security gate |
| Lane 2, define and diagnose | `od-use-case-definition` | Process diagnostics, definition lane end to end |
| Lane 2 and Lane 3, requirements | `od-requirements-breakdown` | Says requirement, epic and story; the word "feature" in the flow's wording is not used |
| Lane 2, data check | `od-data-availability-check` | Verdict naming the step the request dies at |
| Lane 2, solution evaluation | `od-use-case-solution-evaluation` | Complexity drivers and the 16 capability areas |
| Lane 2, portfolio and ranking | `od-portfolio-and-savings-analysis` | |
| Lane 2, capital request | `od-decision-routing` | Routes the eCR, no packaging; the flow rates it Partial and the skill agrees |
| Lane 2 step 6, Lane 3a rollout | `od-handover-and-adoption` | Handover and adoption yes; **no graduation into a catalog** (zero mentions), which is what the flow rates as Partial |
| Lane 2 step 6, graduate | `od-use-case-standardization` | Catalogue, reference library, CSP gate. Run by OD, not by plants, as the flow says |
| Lane 3b, signals and pipeline | `od-signal-standardization`, `od-node-red-flows` | |
| Lane 3b, connect the machine | `od-node-red-flows` | |
| Spine | `od-context`, `od-scorecard-reporting`, `od-sharepoint-list-export` | `od-context` still frames the department as "four service lines" |

## Not placed on the flow

- `od-analytical-support-service`: the flow itself calls it the orchestrator of the Analytics lane the new state dissolves and leaves
  the decision open (re-home into Lane 1 or Lane 2, or retire).
- `od-information-integration-service` and `od-project-support-consultancy`: the flow says nothing about them. They are the orchestrators
  of the two other old lanes; whether they stay is undecided.

## What to do about it

1. Decide where Cyber Security lives in the flow: move the chip to `od-equipment-integration` and `od-decision-routing`, or add the
   gate to `od-acceptance-test`. Until then the flow's claim is not supported.
2. Correct the flow's prototype claim, or decide that prototype / PoC is a missing skill.
3. When the three-lane model is adopted, change `od-use-case-intake-triage` and the framing in `od-context` from four service lines to
   the three lanes. They are also the places the old lane model is written down.
4. Write the self-service mode somewhere: in `od-analytics-asset-build`, or through the new `od-catalog`.
5. Decide whether `od-benefit-calculation` should carry a cost side, or accept the flow's rating as too generous.
6. Re-home or retire the three lane orchestrators. Then regenerate [`process-overview.html`](process-overview.html), which still draws four lanes.
