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
Rule for this skill: **write the amount, quote the ladder as the source words it, and when the amount falls in the
overlapping band apply the stricter (higher) route; Controlling may downgrade it.** Look the amounts up in the current
approval policy; none are written here. The route for small spend is
recorded in 2026 material, quoted in the next section; it is **recorded, not confirmed** by the OD lead. The Lane 1b step
"cost template and lightweight approval" in the flow (rated Partial) is the OD-side step that prepares such an item.

Practical note for a key user: a single use case at one plant is usually far smaller than the portfolio-level
amounts in the knowledge base business cases, which are proposals, not eCR amounts. Do not infer the route from them.

## The pre-approval route for small spend (recorded 2026, owner to confirm)

Four 2026 sources record a route that runs **before** the eCR. Amounts are quoted as the sources give them, with source and date; they are company policy and may change, so look them up again before using them (the OD lead or Finance confirms).

| Statement | Source |
|---|---|
| Locations enter all planned investment items for 2026 in a SharePoint list with status `IDEA`; a quarterly prioritisation and review meeting (location and central) follows; plants start the pre-approval workflow after it; the eCR is created after pre-approval; a location can request pre-approval on demand (rolling forecast); no approval workflow starts before the review meeting | Knowledge base `Document Texts/Department Documents/20260302_Investment Planning Process_Introduction 1.md`, slides 5-6 (source deck dated 2026-03-02) |
| Three amount bands are shown: below 25 kEUR, 25 to 100 kEUR, above 100 kEUR. The text next to them reads "Automated Pre-Approval Workflow to proceed with details (start D4/D5 Project & eCR)" and, for the top band, "PRE-eCR", then project management per the PM standard, the eCR, and end of production or closure. The diagram's arrows are not in the text, so **which band takes which route is an inference** (the automated workflow for the two lower bands, the pre-eCR for the top band) | same file, slide 7 |
| A review-meeting action reads "Central Approval >> put to 25k EUR >> NOT 50k EUR" (the context of the change is not recorded) | Knowledge base `Work-2015_2026/2026/2026-02-24 - Review Meeting 1.md` |
| The central flow starts only if the local approval is "done" and "approved"; the request for execution now triggers only the local approval flow | Knowledge base `Work-2015_2026/2026/2026-03-27 Changes on Invest Approval.md` |

The eCR approval matrix itself (tiers below 50 kEUR, from 50 kEUR and from 150 kEUR) is in `ecr-approval-matrix.md`. How the pre-approval bands (25 and 100) relate to those tiers (50 and 150) is **not stated** in the sources.

**Open points.** ⟨whether the 25 kEUR central-approval limit is the Lane 1b "lightweight approval" limit⟩ · ⟨which route the 25 to 100 kEUR band takes⟩ · ⟨what "eCR" stands for: this skill reads it as electronic capital request, while the bundle's `10-Department/Decision rights.md` says engineering change request; confirm with Finance⟩.

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

Different knowledge base registers (the skill's ledger summary, the Savings Basis Register export) can disagree on row counts
because they are exports of different dates; this is a trap, not an error to fix.

## eCR traces in other knowledge base records

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
