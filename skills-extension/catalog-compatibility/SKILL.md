---
name: catalog-compatibility
description: >-
  Checks that a signal standard, data model, flow, dashboard or library entry built at one plant stays consumable at every plant's instance of the same capability. Builds the plant grid (controller vendor, field network, ingress variant, tool versions, tag language, instance state), tests the standard against each difference, and gives a verdict per plant: consumable, consumable with a mapping, not consumable or unknown. Use when a signal standard or data-model change is about to be recommended, a use case from one plant is proposed for another, something hard-codes a plant-specific name, or someone asks "will this hold at the other plants". Recommends only. Not for defining the signals (mi-signals).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: catalog-compatibility
  aliases: [od-cross-plant-compatibility]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-3
  new_state_lane: "Extension, deepens Lane 3b (3b4)"
  new_state_step: "Connector design and data pipeline (edge to data platform)"
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  requires: [dept-context]
  composes: [mi-signals, catalog-standardization, mi-equipment, mi-data-availability, invest-screen, dept-decision-rights, catalog-usecase]
  okf:
    type: Agent Skill
    title: Cross-plant compatibility check
    tags: [information-integration-service, practice, new-state, draft]
---

# Cross-plant compatibility check

- Read `dept-context` first.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- **Standard under test**: the one thing being checked: a signal set, a data model, a flow, a dashboard or a library entry. This file always calls it "the standard".
- Rule tested: the standard "must stay consumable by every plant's instance of the capability" (decision rights, authority `recommend`).
- `mi-signals` defines the standard for one machine and `catalog-standardization` runs the CSP gate; this skill asks whether the standard still works at the plants that are not the first plant.

## Inputs and output

- **Inputs**: the standard under test (from the `mi-signals` report or the `catalog-standardization` review), the capability it belongs to, the first plant it was built at.
- **Output**: [`assets/compatibility-check.md`](assets/compatibility-check.md): the plant grid with one verdict per plant, the findings and the recommendation.

## References

| File | Open when |
|---|---|
| [`references/plant-differences.md`](references/plant-differences.md) | Building the plant grid: the dimensions on which plants differ and how to read each live (no figures) |
| [`references/compatibility-tests.md`](references/compatibility-tests.md) | Running the tests: what a pass and a fail look like per dimension, which skill supplies the evidence |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The standard concerns a continuous or brownfield process, or one machine type is unknown: fit of the base data model, handoff contract |
| [`assets/compatibility-check.md`](assets/compatibility-check.md) | Writing the grid, findings and recommendation |
| [`references/outputs.md`](references/outputs.md) | Checking each output's recipient and completion rule |
| [`references/background.md`](references/background.md) | Why a check is needed, plan item and open questions; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |

## Procedure

1. **Fix the subject.** Name the capability, the standard under test and the first plant it was built at.
   - Take the standard itself from the `mi-signals` report or the `catalog-standardization` review; do not restate it.
2. **List the plants in scope.** Default: every plant that instantiates the capability, from the Capability Epics notes.
   - If the standard is proposed for a subset, say which and why; the rule is written for every plant.
3. **Build the plant grid** using `plant-differences.md`: for each plant fill controller vendor, field network, ingress variant, tool versions available, plant language of tags, and the state of its instance.
   - Refresh any figure from the live lists (Machine List, Tool Overview) if you rely on it for a verdict; the reference holds no figures.
4. **Run the tests** in `compatibility-tests.md` for each dimension in which at least one plant differs from the first plant. Use `mi-data-availability` to learn what the platform really receives per plant instance.
5. **Give a verdict per plant** from four values:
   - *Consumable*: works unchanged.
   - *Consumable with mapping*: works if the plant's local name, unit or state model is mapped to the standard; the mapping is written down and owned, the standard itself is untouched, and the local name stays an alias (`mi-signals`, multilingual tags).
   - *Not consumable*: the standard would need a plant-specific branch. This is a finding against the standard.
   - *Unknown*: no evidence either way. This is never rounded to "consumable".
6. **Decide what the standard does about a "not consumable".** Options, in order of preference:
   - change the standard so it holds (a COP matter);
   - add a mapping rule to the standard;
   - narrow the stated scope of the standard and say which plants it does not cover.
   - Never add a plant-specific branch inside the standard, because it stops being a standard.
7. **Completion check** (repeat until all hold):
   - [ ] Every plant in scope has exactly one of the four verdicts.
   - [ ] Every "unknown" names the evidence that would resolve it.
   - [ ] Every mapping is written down with an owner.
   - [ ] Figures relied on were refreshed from the live lists.
8. **Write the recommendation** in `assets/compatibility-check.md` and route it with `dept-decision-rights`.
   - The decision is IIAE's by consultation; for a tool or system rollout the IIAE decides in tandem with the IT-responsible role of the business side (`08-decision-rights.md`).
   - A change to a data model or connector goes to the COP (monthly, technical).
9. **If the standard feeds the catalog**, hand the verdict grid to `catalog-usecase` so a plant picking the entry sees which plants it was checked at and which not.

## Decision table: what to do with the result

| Result | Action |
|---|---|
| All plants consumable | Recommend the standard; attach the grid |
| Some consumable with mapping | Recommend the standard plus the mapping rules; owner for each mapping is the plant's IT role, `⟨named owners to confirm⟩` |
| Any not consumable | Do not recommend as "standard for all plants"; return to step 6 |
| More than a few unknown | Recommend only for the checked plants; list the unknown plants and the evidence that would resolve each |
| First-plant-only evidence | Say so: a standard proven at one plant is a proposal, not a standard (compare the CSP gate in `catalog-standardization`) |

## Example

```text
Standard under test: machine-state signal set for "press capability" (fictional), built at Plant A
| Plant | Controller | Ingress    | Tag language | Verdict                  | Note                                  |
| A     | Siemens    | IIoT Edge  | English      | Consumable               | first plant                           |
| B     | Siemens    | OPC UA agg.| German       | Consumable with mapping  | local state names mapped, owner: Plant B IT |
| C     | Rockwell   | evaluation | unknown      | Unknown                  | no machine records; need platform check (mi-data-availability) |
Recommendation: recommend for A and B with the mapping rule; scope narrowed, C not covered yet
```

## Human gate and AI-agent notes

- **An agent may**: build the grid, run the tests, write verdicts and the recommendation.
- **Stays with roles**: IIAE decides by consultation; the COP handles a data-model or connector change; plant IT roles own mappings.
- The agent recommends; it does not decide the data-model change.

## What is still open

- **Per-plant tag language** is recorded nowhere as a field; infer from the signal list with `mi-signals`.
- **Plants with no machine records** (zero machines in the plant notes) cannot be graded; their verdict is *unknown*.
- **Tool rollout records** in the plant notes list only tools recorded per plant; a missing line is not proof of "not available". Confirm with the IIAE role.
- **Whether a mapping is accepted by consumers** (dashboards, reports on the data platform) is not recorded; the test needs a named consumer per capability. `⟨consumer inventory per capability, to collect from DBVE and IIAE⟩`.
- **Lead time of the COP route** is not stated (escalation window `⟨to confirm⟩` in the operating rhythm).

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Treating "the data lands on the platform" as "the standard holds" | Two plants can land different names for the same concept |
| Rounding unknown up to consumable | A missing record is not evidence of fit |
| Editing the standard to fit one plant | The standard then forks; map the plant instead |
| Assuming the base data model fits a continuous process | It was found suitable for discrete, time-series-centric machines |
| Reading a missing tool-rollout line as "not available" | Only recorded tools are listed |
| Calling a standard cross-plant on the evidence of its builder plant | One plant's proof is a proposal |

## Do not

- Do not hard-code a plant, line or machine name into a standard, flow or dashboard that is meant for all.
- Do not treat "the data lands on the platform" as "the standard holds".
- Do not edit the standard to fit one plant; map the plant to the standard.
- Do not call a standard cross-plant on the evidence of the plant that built it.
- Do not decide the data-model change yourself: you recommend; the decision route is in `dept-decision-rights`.

## Definition of done

- Every plant in scope has one of the four verdicts, the recommendation follows the decision table, and it is routed with `dept-decision-rights`.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).
