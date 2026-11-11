---
type: Skill Reference
title: Promotion criteria
description: The six tests an ad-hoc asset must be put through before it is proposed as a standard use case, the evidence that answers each, the promote / keep / retire rule and the catalog conditions.
resource: ../procedure.md
status: draft
tags: [analytical-support-service, practice]
---
# Promotion criteria

Sources: the analytical lane's playbook, tasks, agent brief and metrics; `catalog-usecase` (four conditions);
`catalog-standardization`; `deploy-handover`; `ops-analytics-asset`. The tests are this
skill's arrangement of those sources. The OD lead has not confirmed them as a rule; **no numeric threshold
is given in the sources** and none is invented here.

## The six tests

| # | Test | Question | Evidence that answers it | Source of the rule |
|---|---|---|---|---|
| 1 | **Recurrence** | Did the same need come back, from the same or another plant? | Request log with dates, plants, requesters, what differed; the asset's reuse | Playbook step 6; trigger "recurring value in an ad-hoc asset". Threshold `⟨to confirm⟩` |
| 2 | **Value** | Is the asset used, and does it move a decision or a loss? | Utilization record (daily / weekly / ... / `NEVER`) from the Scorecard; saving rows with reliability and proven flag; the named ritual it serves | Metrics: utilization rate; `bc-build`; `deploy-handover` question 1 |
| 3 | **Reproducibility** | Can a second plant take it without the builder? | Data path written to machine and signal; data-fitness verdict; standardized signals; validation checklist passed; plant-specific parts separable | `mi-data-availability`, `mi-signals`, `ops-analytics-asset` (validate before calling it built) |
| 4 | **Placement** | Is there already a library entry, and where would a new one sit? | Library search result; capability template, process group, cluster tag assigned by the classifier; deltas against the cluster baseline | `catalog-standardization`, procedure steps 1 to 4 |
| 5 | **Handover** | Does the plant own it and use it in real shifts? | Named plant owner; the three-question test answered without the builder; handover state | `deploy-handover` |
| 6 | **Catalog conditions** | Which of the four conditions for "catalogued" hold? | See below | `catalog-usecase` |

### Test 6 in detail (`catalog-usecase`, "What counts as catalogued")

| Condition | Status in the sources |
|---|---|
| 1. A CSP decision `Yes` is recorded | A rule from the decision rights: "whether a solution is standard enough to roll out" is the CSP decision, per library entry |
| 2. It maps to one of the capability templates | A **proposal** of `catalog-usecase`, awaiting the OD lead |
| 3. Its signals are standardized | A **proposal** of `catalog-usecase`, awaiting the OD lead |
| 4. It has a plant owner and a handover record that passed the three-question test | From the sources |

A candidate without a recorded CSP `Yes` is not catalogued; `catalog-usecase` routes it to Lane 2 (OD-led).
So the promotion package **prepares** the CSP decision (methods and actions written down, evidence it works
at its first plant); it does not take it.

## Decision rule

| Result | When | Next |
|---|---|---|
| **Promote (recommend)** | Tests 1 to 5 answered with evidence, a library check shows no covering entry, a named responsible human accepts it | `funnel-use-case` (Phase 1, Collect, with the package as the logged demand); `catalog-standardization` for CSP preparation; `bc-portfolio` if candidates compete |
| **Reuse** | Test 4 finds a library entry that covers the need | Point the requester at the entry; no new use case |
| **Keep as ad-hoc** | Recurrence or value is not shown yet | Record a review date; keep tracking utilization |
| **Retire** | Low utilization after review with the requester | Retire the asset ("review with requester or retire", playbook error path) |
| **Stop and fix** | Reproducibility fails (data gap, unstandardized signals) | Data gap: route to the Information Integration lane and mark it (playbook); do not approximate missing data |

Escalation for low utilization or unclear value: OD lead via COP (analytical lane agent brief).

## What a promotion package must not smuggle in

- A **savings figure** without a nameable source. In the portfolio most use cases carry no recorded saving, and many
  delivered cases carry none (Case Groups overview; count live): an asset with no saving is the normal case, and
  "to be collected" is the honest entry.
- A **declared standard**. Declaring a use case standard commits it to `catalog-standardization`
  ("the hinge the whole function turns on"); do not use the word for an ad-hoc asset.
- A **library duplicate**. A library entry marked CSP `No` with the note that "the other common solution is
  a much better solution" exists in the data (a library entry recorded with CSP `No`
  and a note that a better common solution exists). Promoting a weaker duplicate adds to the catalogue that "has not scaled".

## Which asset types get promoted

Output assets recorded across the portfolio are dashboards, reports, apps, analytics workflows and agents (count the mix
live). Most candidates will be dashboards; `ops-analytics-asset`
and `ops-dashboard-engine` hold the standard layouts the promoted version should follow.
An "app disguised as a dashboard" (the user types something back) is a different asset type and a
different promotion: check the type first (`ops-analytics-asset`, asset type and tier).
