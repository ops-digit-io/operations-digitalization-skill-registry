---
type: Skill Reference
title: Spend route
description: How to find the spend gate and approver for an OD investment, the ambiguity in the recorded thresholds to resolve with the OD lead, where the eCR sits in Lane 2 and Lane 3, and what a saving waiting on it looks like in the ledger. Guidance only, no amounts.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Spend route

The sources are silent on the eCR form. Amounts and thresholds are deliberately not repeated here: they are company
policy and change. Look them up each time (look up: `10-Department/Decision rights.md`, `od-decision-routing`, the
OD lead, Finance) and quote them with their source and date.

## What the sources say (qualitatively)

| Statement | Source |
|---|---|
| Investment goes through the **eCR** (electronic capital request) route, with two approval thresholds "that are not alternatives but a ladder": a CTO limit and a Board limit | Bundle `10-Department/Decision rights.md`; repeated in `od-decision-routing` |
| Digitalization investment planning: role OD lead, together with BA Operations, mode Consultation (hear, then decide alone), approval **yes**, reversible **no**, budget threshold marked to confirm, authority level `recommend` | `00-core/08-decision-rights.md` |
| Deputisation: investment commitments wait for the OD lead; no urgency substitutes | `00-core/08-decision-rights.md`, `od-decision-routing` |
| "Skills may prepare the input (II-07), never the approval" | `OD_Skill_Map.md`, rules section |
| An agent never commits investment or allocates resources | `od-decision-routing`, "What an agent may never do" |
| The thresholds also appear in a separate department set-up plan (Digital Unit time plan) as an open item owned by Finance | Bundle `90-Sources/du-overview/.../260818_DU_Setup_Timeplan.md` |

## The overlap

As recorded, the CTO limit and the Board limit overlap in a band: the wording does not say which body decides there.
Two readings are possible and the sources support neither over the other:

1. Below the lower threshold the CTO decides, in the band both are involved, above the upper threshold only the
   Board.
2. The thresholds are for different spend types or for different organisations (the second source is the Digital
   Unit plan, not the OD route).

Rule for this skill: **write the amount, quote the ladder as the source words it, and mark the route as
⟨to confirm with the OD lead⟩ if the amount falls in the overlapping band.** Also open: ⟨the route for small
spend⟩. The Lane 1b step "cost template and lightweight approval" in the flow (rated Partial) suggests a lighter
route for small spend, but no source gives its limit.

Practical note for a key user: a single use case at one plant is usually far smaller than the portfolio-level
amounts in the vault business cases, which are proposals, not eCR amounts. Do not infer the route from them.

## Where the eCR sits in the lanes

| Lane step | What the flow says | Wait recorded |
|---|---|---|
| Lane 2, step 4 | Business case and prioritize: value model, cost side, portfolio ranking | portfolio decision |
| Lane 2, step 5 | Capital request (if invest needed): package value and cost for approval | MPEE / BA Operations approval |
| Lane 3, step 2 | Tool-decision / IT-footprint gate: make, buy, integrate or connect | - |
| Lane 3, step 3 | Business case and capital request: value and cost, capital request if needed; hand off once demand is clear | IT commitment and MPEE approval |

Waiting times are placeholders in the skill-map table; no measurement exists.

## What a saving waiting on the gate looks like

`od-benefit-calculation` records dependencies on saving rows. `ECR APPROVAL` and `ECR CREATION` are two of its
values. To see how many rows currently wait on them, filter the live savings ledger on the dependency field and
re-count; quote the count with its source and date, and never mix counts from different registers. Use the two
values in sequence:

- Drafting or not yet filed: dependency `ECR CREATION`, owner = the role who files.
- Filed and waiting: dependency `ECR APPROVAL`, owner = the approver named by the route.
- Approved: remove the dependency, keep the approval date in the row's rationale.

Different vault registers (the skill's ledger summary, the Savings Basis Register export) can disagree on row counts
because they are exports of different dates; this is a trap, not an error to fix.

## eCR traces in other vault records

- A plant saving row can list "eCR presentation" as its calculation input and comment: the eCR was backed by a
  presentation, and the saving's basis was kept there, not in the ledger. Pattern to avoid: a methodology that
  lives only in a deck (`Savings Basis Register`).
- A process-epic blocker can list "eCR for additional hardware" as a blocking point: hardware that a use case
  needs can itself require an eCR (`Blocker Register`).
- A business case may plan to read past eCR data as input for a risk model and to test whether it is machine
  readable (`Graph/Business Cases`). So eCR records may exist in a form worth reading; ⟨where eCRs are stored⟩ is
  unknown.

## Other gates the same spend may hit

| Gate | Skill | When |
|---|---|---|
| IT demand management and the demand evaluation board | `it-demand-package` | the request needs a platform OD does not own |
| Cyber Security / OT sign-off | `od-cybersec-gate`, `od-equipment-integration` | external connection or new connector |
| CSP decision | `od-use-case-standardization` | the solution is meant to roll out across plants |
| Plant adoption | `od-handover-and-adoption` | daily use is the plant's decision |
| SPRINT review | `od-benefit-calculation` | only SPRINT makes a saving proven |
