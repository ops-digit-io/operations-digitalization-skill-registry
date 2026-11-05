---
type: Skill Reference
title: Spend route
description: The spend gate for OD investment as the sources state it, the unresolved overlap in the thresholds, where the eCR sits in Lane 2 and Lane 3, and what a saving waiting on it looks like in the ledger.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Spend route

All statements below are from the sources named, read 2026-11-05. The sources are silent on the eCR form.

## What the sources say

| Statement | Source |
|---|---|
| Investment goes through the **eCR** (engineering change request) route, with two thresholds "that are not alternatives but a ladder": the CTO approves up to EUR 150k, the Board approves above EUR 75k | Bundle `10-Department/Decision rights.md`; repeated in `od-decision-routing` |
| Digitalization investment planning: role OD lead, together with BA Operations, mode Consultation (hear, then decide alone), approval **yes**, reversible **no**, threshold ⟨budget threshold - to confirm⟩, authority level `recommend` | `00-core/08-decision-rights.md` (last verified 2026-08-10) |
| Deputisation: investment commitments wait for the OD lead; no urgency substitutes | `00-core/08-decision-rights.md`, `od-decision-routing` |
| "Skills may prepare the input (II-07), never the approval" | `OD_Skill_Map.md`, rules section |
| An agent never commits investment or allocates resources | `od-decision-routing`, "What an agent may never do" |
| The same two thresholds appear in a separate department set-up plan (Digital Unit time plan, 2026-08-18) as an open item: "Pilot approval-threshold (EUR 75k board / EUR 150k CTO)", owner Finance, status pending; and "EUR 75k board-approval threshold; CTO can sign up to EUR 150k" in its funding governance text | Bundle `90-Sources/du-overview/.../260818_DU_Setup_Timeplan.md` |

## The overlap

"CTO up to EUR 150k" and "Board above EUR 75k" overlap between EUR 75k and EUR 150k. The sources do not say
which applies in that band. Two readings are possible and the sources support neither over the other:

1. Up to EUR 75k the CTO decides, from EUR 75k to EUR 150k both are involved, above EUR 150k only the Board.
2. The thresholds are for different spend types or for different organisations (the second source is the Digital
   Unit plan, not the OD route).

Rule for this skill: **write the amount, quote the ladder as the source words it, and mark the route as
⟨to confirm with the OD lead⟩ if the amount is above EUR 75k.** Also open: ⟨the route below EUR 75k⟩. The
Lane 1b step "cost template and lightweight approval" in the flow (rated Partial) suggests a lighter route for
small spend, but no source gives its limit.

## Illustration with the vault's business cases (not a routing decision)

Of 27 AI business cases that state a cost range, the range of 20 starts at or above EUR 150k, 6 straddle EUR 150k
(for example the Catalog Maturity Sprint, EUR 0.1M to 0.2M) and 1 ends at or below it
(`Graph/Business Cases`, read 2026-11-05; costs are portfolio-level proposals, not eCR amounts). The point for
a key user: most investments of the size the department discusses sit at or above the CTO limit, so the Board
route is the usual case, and a single use case at one plant is usually far smaller.

## Where the eCR sits in the lanes

| Lane step | What the flow says | Wait recorded |
|---|---|---|
| Lane 2, step 4 | Business case and prioritize: value model, cost side, portfolio ranking | portfolio decision |
| Lane 2, step 5 | Capital request (if invest needed): package value and cost for approval | MPEE / BA Operations approval |
| Lane 3, step 2 | Tool-decision / IT-footprint gate: make, buy, integrate or connect | - |
| Lane 3, step 3 | Business case and capital request: value and cost, capital request if needed; hand off once demand is clear | IT commitment and MPEE approval |

Waiting times are placeholders in the skill-map table; no measurement exists.

## What a saving waiting on the gate looks like

`od-benefit-calculation` records dependencies on saving rows: 60 of 553 rows record one; `ECR APPROVAL` 14 rows and
`ECR CREATION` 6 rows (20 together); `ECR APPROVAL` is the second most common value after `NO DEPENDENCY` (18), and `ECR CREATION` is tied for fifth. Source:
`Savings and value tracking.md` (as quoted in the skill, dated 2026-10-22). Use these two values in sequence:

- Drafting or not yet filed: dependency `ECR CREATION`, owner = the role who files.
- Filed and waiting: dependency `ECR APPROVAL`, owner = the approver named by the route.
- Approved: remove the dependency, keep the approval date in the row's rationale.

Counts in other vault registers differ from the skill's (the Savings Basis Register export of 2026-08-21 shows 580
rows); do not mix the figures, quote each with its source and date.

## eCR traces in other vault records

- A plant saving row (Mako, 2023, estimation, closed) lists "eCR presentation" as its calculation input and comment:
  so the eCR was backed by a presentation, and the saving's basis was kept there, not in the ledger. Pattern to
  avoid: a methodology that lives only in a deck (`Savings Basis Register`).
- A process-epic blocker at a metal furnace lists "eCR for additional hardware (equipment for camera)" as a blocking
  point: hardware that a use case needs can itself require an eCR (`Blocker Register`, modified 2023-07-26).
- Production Risk Scoring plans to read past eCR data as input for a risk model, and to test whether it is machine
  readable (`Graph/Business Cases`). So eCR records may exist in a form worth reading; ⟨where eCRs are stored⟩ is unknown.

## Other gates the same spend may hit

| Gate | Skill | When |
|---|---|---|
| IT demand management and the demand evaluation board | `it-demand-package` (planned) | the request needs a platform OD does not own |
| Cyber Security / OT sign-off | `od-cybersec-gate` (planned), `od-equipment-integration` | external connection or new connector |
| CSP decision | `od-use-case-standardization` | the solution is meant to roll out across plants |
| Plant adoption | `od-handover-and-adoption` | daily use is the plant's decision |
| SPRINT review | `od-benefit-calculation` | only SPRINT makes a saving proven |
