---
name: bc-portfolio
description: >-
  Reads the OD use-case portfolio and the savings ledger correctly: cuts use cases by plant, region, capability, cluster, status and asset, labels every euro as tracked or proven, names the denominator and capture date, and treats blank fields as unknown, not zero. Use for any portfolio question, regional or plant comparison, conversion-rate or standardization analysis, savings roll-up, or before a portfolio number goes into a deck, board paper or business case. Second job with its own trigger: ranks competing candidate use cases for one plant or region into a prioritization record. Read-only; changes no list. Not for building a case (bc-build).
license: MIT
metadata:
  id: bc-portfolio
  aliases: [od-portfolio-and-savings-analysis]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (24)"
  new_state_step: "Business case (value and cost), assessment, ranking"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: read-only
  status: stable
  requires: [dept-context]
  composes: [know-sharepoint-export, bc-build, catalog-standardization, metrics-scorecard, dept-decision-rights]
  okf:
    type: Agent Skill
    title: Portfolio and savings analysis
    tags: [analytical-support-service, practice, use-case-support-service]
---

# Portfolio and savings analysis

- Read `dept-context` first.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- This skill carries no counts. Every figure comes from a live read with its capture date.

## Which job

| The user asks | Job | Go to |
|---|---|---|
| A portfolio, regional, plant, standardization, conversion or savings question; a number going into a deck, board paper or business case | **Portfolio read** | Procedure (below) |
| Which of several competing candidate use cases to do first for a plant or region | **Prioritization** (Lane 2 step 24) | [`procedure.md`](references/od-use-case-prioritization/procedure.md), then record in [`prioritization-record.md`](references/od-use-case-prioritization/assets/prioritization-record.md) |

## How to read the portfolio

- Every figure comes from a live read of the use case list (`know-sharepoint-export`) with its capture date.
- The cuts to take, and what each field means:

| Delivery status | Means |
|---|---|
| `IDEA` | Recorded, not yet committed to a plan |
| `PLANNED` | Committed, not yet built |
| `IMPLEMENTED` | Built and handed to the plant |
| `PRODUCTIVE` | In daily use |
| `STOPPED` | Deliberately discontinued |

- The share of what has been asked for that has been built is `IMPLEMENTED` plus `PRODUCTIVE` over all use cases. Always state the denominator.
- **Workflow state** (Development, Implementation, Handover, each `DONE` or `ONGOING`): read it as a funnel and cross-check it against the delivery status before quoting either; they are maintained separately and can disagree.
- **Category**: standard use case cross process, standard per process, non-standard unique to one plant, AI use case (generative, ML or deep learning). Rank within a category.
- **Rollout phase** (`PHASE 1` onwards) is recorded only on some use cases. Phases are named rollout batches, not sequential queues; a blank phase is not "phase 0".
- **Output asset** (dashboard, report, app, analytics workflow, agent) and **utilization** (Daily, Weekly, Monthly, On-Demand, `NEVER`) are recorded only where someone filled them. Count the recorded ones as the denominator, never the whole portfolio.

## Regional shape

- Cut use cases, productive use cases and conversion (productive over all) per region, live.
- Never blend the regions into one conversion figure (`references/regional-handling.md`), because a blended rate hides that each region has a different problem.

## The savings ledger

- Read the ledger live: row count, tracked euros, proven euros and proven rows, the split by reliability (`CALCULATION`, `ESTIMATION`, not recorded), automated versus manual rows, and the number of use cases that carry a saving figure of any kind.
- Quote each with its capture date.
- Treat the total as a **floor on what has been captured**.
- See `bc-build` for how a row is built and what may be added to what.

## The three ways this data misleads

1. **Absence read as a zero.** Many use cases carry `UNKNOWN` priority or potential and many saving rows carry no reliability. "The top priorities" phrased so that the remainder is low reads absence as an answer.
2. **Tracked read as proven.** Never add the two.
3. **`IMPLEMENTED` read as in use.** It is not; that is what `PRODUCTIVE` and the utilization field are for.

- A fourth, about provenance: version history carries text the current record does not. Export versions, not just items (`know-sharepoint-export`).

## Checks against standing findings

- Count blank reliability on the live ledger before saying how complete it is.
- Check the live capability instance list before saying templates are the constraint; adoption of the proven instance is the usual constraint.
- Track the size of C12 "Other and plant-specific" over time; it is a data-quality signal, not only a topic.
- More context in `references/background.md`.

## Procedure - portfolio read

1. State which surface you are reading and when it was captured. The knowledge graph is a rebuilt read surface; the SharePoint lists are the write surface.
2. Cut by plant / region / capability / cluster / status / asset; never by one dimension alone when a claim about scale is being made.
3. For every empty field, decide and **state** whether it is unknown or genuinely nil.
4. Label every euro figure tracked or proven, per `references/rollup-method.md`.
5. Name the denominator on every rate, and never blend the three regions into one (`references/regional-handling.md`).
6. Rank only within a category (`references/prioritization.md`) and keep the unscoreable bucket visible rather than folding it into the bottom of a ranked list.
7. **Pre-publication check** (repeat until all hold):
   - [ ] Capture date and surface stated.
   - [ ] Denominator on every rate.
   - [ ] Every euro labelled tracked or proven; none summed across.
   - [ ] Every blank stated as unknown or nil.
   - [ ] Regions shown separately.
8. Fill [`assets/portfolio-review-protocol.md`](assets/portfolio-review-protocol.md) as the review happens; it is the record a reader who was not in the room can act on.

## Procedure - prioritization

- Run [`references/od-use-case-prioritization/procedure.md`](references/od-use-case-prioritization/procedure.md) when several candidate use cases compete for a plant or region and need a recommended order (Lane 2 step 24).
- It keeps its own references and assets under that folder and the authority it had (recommend).

## Example

```text
Portfolio read (fictional numbers, invented for illustration)
Surface: use case list export, captured 2026-xx-xx (date stated)
Region A: 40 use cases, 6 PRODUCTIVE -> conversion 6/40 (denominator: all use cases in region A)
Region B: 25 use cases, 10 PRODUCTIVE -> 10/25   (never blended with region A)
Savings: tracked 120 | proven 20   (labelled, never summed); 15 of 25 rows have blank reliability
Priority: 12 use cases UNKNOWN -> unscoreable bucket, not "low"
```

## Human gate and AI-agent notes

- **An agent may**: read the lists, cut and label figures, fill the protocol, draft a ranking.
- **Stays with roles**: the DBVE owns the ledger; the OD lead signs a prioritization; finance confirms proven savings. This skill changes no list.

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Quoting a count without its capture date | The lists move; the reader cannot tell how old it is |
| A rate without its denominator | The same numerator can mean very different shares |
| Treating a blank as zero | A blank usually means never assessed |
| Writing "no potential" for a scaled use case without savings | It was probably not assessed; mark it for further investigation |
| Ranking across categories | The categories are different problems |
| Reading only the current snapshot | Rationale was tidied back to `-`; versions hold the narrative |

## Do not

- Do not treat rollout or deployment count as value, and do not write "no potential" for a scaled use case without savings; mark it for further investigation.
- Do not rank without saying which order of criteria was used and which planning state it is.
- Do not roll up savings across reliability classes into one headline.
- Do not compare regional counts without their conversion rates.
- Do not present a portfolio figure without the date it was read.

## Definition of done

- The protocol is filled with surface and capture date, denominators, tracked and proven labels and blanks stated as unknown or nil.
- A prioritization record, if requested, names the criteria order and planning state and keeps the unscoreable bucket visible.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/rollup-method.md`](references/rollup-method.md) | Summing anything: which boundaries a sum may never cross (tracked/proven, reliability class) |
| [`references/regional-handling.md`](references/regional-handling.md) | Comparing Europe, Americas and Asia, or reporting a conversion figure |
| [`references/prioritization.md`](references/prioritization.md) | Ranking use cases in a review: weighted scoring, value-effort, the unscoreable bucket |
| [`references/strategic-initiatives-and-savings.md`](references/strategic-initiatives-and-savings.md) | Reading strategic business cases next to plant savings: addressable vs realistic, no double counting |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Order of ranking criteria, planning states, where-saved matrix, kill and hold hygiene |
| [`references/od-use-case-prioritization/assets/prioritization-record.md`](references/od-use-case-prioritization/assets/prioritization-record.md) | Producing the prioritization record: candidates, criteria and weights, scores with evidence, sign-off |
| [`references/od-use-case-prioritization/references/ranking-criteria.md`](references/od-use-case-prioritization/references/ranking-criteria.md) | Building a ranking from the department's own criteria, each with source and limit |
| [`references/od-use-case-prioritization/references/evidence-baselines.md`](references/od-use-case-prioritization/references/evidence-baselines.md) | Reading case groups, rollout maps and savings basis for a candidate before asking anyone |
| [`references/od-use-case-prioritization/references/business-case-archetypes.md`](references/od-use-case-prioritization/references/business-case-archetypes.md) | Classifying strategic business cases (foundation, enabling layer, value layer, big bet, defer) |
| [`references/od-use-case-prioritization/references/process-chain-practice.md`](references/od-use-case-prioritization/references/process-chain-practice.md) | Running ranking at step 24: planning states, ordering rule, foundation-first logic, value tiers |
| [`references/outputs.md`](references/outputs.md) | Checking each output's recipient and completion rule |
| [`references/background.md`](references/background.md) | Standing findings and context; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
