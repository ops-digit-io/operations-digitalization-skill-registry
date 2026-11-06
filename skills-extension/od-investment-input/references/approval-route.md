---
type: Skill Reference
title: Approval route
description: Who decides an investment input, how to find the current spend ladder and its ambiguity, the open budget threshold, and the gates and dependencies to record. Guidance only, no amounts.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, decision-rights]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Approval route

Source of the rows: `08-decision-rights.md` and `od-decision-routing`. Check on the live decision-rights page that
the rows are still verified and not past their review date. This skill reads them; it does not decide.

## The decisions around one investment

| Decision | Role | Together with | Mode | Approval | Reversible | Threshold | Level |
|---|---|---|---|---|---|---|---|
| Digitalization investment planning | OD lead | BA Operations | Consultation | yes | no | `⟨budget threshold, to confirm⟩` | recommend |
| Equipment integration go-ahead | IIAE | Plant ME / Plant IT | Tandem | yes | partially | per investment plan; Cyber Security sign-off for external connection | execute-with-approval |
| Tool / system rollout (MES, MSB, IIoT Edge, data platform) | OD lead | IT-responsible role of the business side | Tandem | yes | no | strategic-plant scope | execute-with-approval |

The pack feeds the first row. The second row uses the approved plan ("per investment plan"). The third row
is a different decision, taken when the pack contains a tool and not only machines.

## The spend ladder

`od-decision-routing`: spend is routed through eCR (electronic capital request) with two approval limits, a CTO
limit and a Board limit, described as "a ladder, not alternatives". The amounts are company policy and are not
repeated here: per the current approval policy (look up: `od-decision-routing`, the OD lead, controlling). Quote
them with source and date.

Read literally, the two limits overlap in a band. Where an amount falls in that band, the stricter (higher) route
applies; Controlling may downgrade it. Look the amounts up in the current approval policy and write the amount and its
scope (per item, per plant or per programme) in the pack.

Whether the ladder is the same thing as the "budget threshold" of the digitalization investment planning
row is also not stated. They may be two thresholds (who within OD plans, who approves the eCR). Keep both
open.

## Lane 1b: the lightweight approval

The new-state flow describes branch 1b as "predictable spend via cost template" and "standardized,
pre-priced spend, template, not a full business case", with a "small budget approval"; `od-decision-routing`
routes the approval, and the "cost template itself is an artifact, not a skill" (VSM skill map, step 2 of
branch 1b). Not given: the amount below which spend counts as small, and who approves. Mark both open and
do not borrow the ladder above for them.

## Gates the pack must name

| Gate | Applies when | Skill |
|---|---|---|
| Spend (eCR) | any capital spend | `od-decision-routing`, `od-capital-request` |
| Cyber Security / OT sign-off | any external connection; "no expedited path" | `od-cybersec-gate` |
| IT demand | the item touches a platform OD does not own | `it-demand-package` |
| Tool / system rollout | the pack adds or extends a tool | `od-decision-routing` (tool rollout row), `od-system-fit-check` |
| Plant adoption | the benefit depends on daily use | `od-handover-and-adoption` |
| SPRINT | the benefit is to be called proven | `od-benefit-calculation` |

## What the pack may and may not say

May: figures with sources, tracked benefit, a recommendation to the OD lead, open items.
May not (`od-decision-routing`, "what an agent may never do"): commit investment or allocate resources,
make licensing commitments, approve an external connection without Cyber Security / OT sign-off.

## Deputisation

In the OD lead's absence the next-higher management role decides prioritization and rollout within the agreed
roadmap; investment commitments stay with the competent approval body. No level of urgency substitutes.
