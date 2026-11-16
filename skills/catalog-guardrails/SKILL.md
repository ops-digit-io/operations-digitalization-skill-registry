---
name: catalog-guardrails
description: >-
  Runs the go-live self-check and technology guardrails (G1-G7a, plus candidate G8-G19) on a catalogued use case that a plant applied itself, and writes the go-live check record with a result, evidence and date per guardrail. Use when a plant says "can we go live with this screen", wants to declare a dashboard productive, applied a template without OD, or someone proposes a new guardrail (steps 1a3 and 1b4). Reports only; the plant decides PRODUCTIVE and a failed guardrail means no go-live. Not for the data check (mi-data-availability), matching the use case (catalog-usecase) or the OD handover (deploy-handover).
license: MIT
metadata:
  id: catalog-guardrails
  tier: practice
  lane: lane-1
  new_state_lane: "Lane 1a (1a3), Lane 1b (1b4)"
  new_state_step: "Guardrails, go live, confirm adoption"
  department_names: ["catalog-guardrails"]
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant runs the check
  tags: [department-core, lane-1]
  authority_level: draft the go-live check and report it; the plant decides PRODUCTIVE; a block-level failure stops go-live
  status: ready
  requires: [dept-context]
  okf:
    type: Agent Skill
    title: Catalog guardrails
    tags: [department-core, lane-1]
---
# Catalog guardrails

- Read `dept-context` first.
- The department's `catalog-guardrails`: the boundaries inside which a plant runs a catalogued use case itself, and the go-live self-check (steps 1a3 and 1b4).
- Self-service stays inside pre-approved guardrails; anything outside them is not self-service.
- Terms: the **go-live check** is the whole run; a **guardrail** is one numbered rule in it; a **go-live check record** is its written result.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Run the go-live self-check for a catalogued use case that a plant applied itself, and keep self-service inside the guardrails.
- Use it at steps 1a3 and 1b4, when a plant wants to go live, or when a new guardrail is proposed.

## Inputs and output

- Inputs: the Part A match record (and, on branch 1b, the system match record), the data-availability verdict, the handover record, and evidence for each guardrail (a verdict, a source, a name).
- Output: the go-live check record ([`assets/go-live-check-record.md`](assets/go-live-check-record.md)) with a result per guardrail, evidence, date and who answered.

## The guardrails

| # | Guardrail | Why it exists | A failure means |
|---|---|---|---|
| G1 | The signals the template reads exist and are fresh (`mi-data-availability` verdict) | A screen on missing or stale signals shows nothing or old values silently | Stop. Back to the data check; Lane 2 or Lane 3 if the data cannot be had |
| G2 | **Platform boundary:** a plant's manufacturing dashboards run on that plant's local Grafana; the global layer (Databricks, Azure Storage Account) is not wired into it, and no cross-plant view is built on a local instance | Wiring the layers together breaks the platform boundary recorded in `registry.yaml` (open gaps) | Stop. Undo the wiring, or ask OD for a cross-plant view |
| G3 | The solution stays inside the lean footprint, no system outside it (`invest-screen`) | A system outside the footprint has not been screened | Stop. Escalate as an exception through `dept-decision-rights` |
| G4 | **No invented figures:** no savings or impact number unless a source and a capture date are named | An unsourced number gets quoted as a fact (`dept-context` honesty rules) | Remove the number, or mark it as to be collected |
| G5 | A **named plant owner** exists, and the plant, not OD, decides daily use | Without an owner nobody acts on the screen | Stop. Name the owner first |
| G6 | The **three-question handover test** is answerable by the receiving side from the handover record alone, and the record names **who uses the screen, in which meeting, and which action follows** (`deploy-handover`) | A screen with no user, meeting and action is not adopted | Not done. Close the gap before go-live |
| G7 | An **external connection** has a Cyber Security sign-off. Human-only | An unsigned connection exposes the plant network | Hold at the wait state. Do not go live |
| G7a | **No change to the data model or signal standard:** the plant uses the catalogued model as it is (Lane 1 "may not change data models") | A changed model stops being consumable by other plants | Stop. Lane 2 or Lane 3 via `mi-signals`, decided through `dept-decision-rights` |

- The plant always answers G1 to G7 and G7a.
- **G8 to G19** (screen-level) and **P1 to P7** (process level) are **candidates**, not a confirmed set; the OD lead has not confirmed them. See [`references/technical-guardrails.md`](references/technical-guardrails.md).
- The plant answers the candidates when it has built or copied the screen itself.

## Procedure - go-live check

1. Take the Part A match record and, on branch 1b, the system match record.
2. The **plant** answers G1 to G7 and G7a, each with evidence (a verdict, a source, a name). A guardrail with no evidence is "not checked", not "passed".
3. If the plant built or copied the screen itself, open [`references/technical-guardrails.md`](references/technical-guardrails.md) and answer G8 and up as well.
4. Do one deep dive against the paper process before declaring the screen live (`catalog-usecase`, `references/process-chain-practice.md`, Part C).
5. Write the **go-live check record**: per guardrail the result (passed / failed / not checked), evidence, date, who answered; at the top the use case, plant, plant owner, and the final line "go-live decision: the plant's".
   - Write the utilization expectation into the record before go-live.
6. Any failed guardrail means **no go-live**; route back as the table says (data to `mi-data-availability`, footprint to `invest-screen`, handover to `deploy-handover`, security to `deploy-cybersec`; say which).
7. **Re-run after a fix:** when a failed guardrail is fixed, check it again and update the record. Repeat until every guardrail passes or is marked not applicable.
8. All passed - report it. **The plant decides to go live** (`PRODUCTIVE`); this skill never does.
9. After go-live, adoption is checked as `deploy-handover` describes.

## Human gate and AI-agent notes

- An agent may draft the go-live check record, collect evidence, and report which guardrails passed, failed or were not checked.
- The plant owner role decides `PRODUCTIVE`.
- The Cyber Security role signs off any external connection (G7).
- The OD lead role confirms the candidate guardrails G8 to G19 and P1 to P7 and any new guardrail.
- An agent never marks a failed guardrail as passed.

## Example

```text
Input : use case "line-state board" (fictional), plant "Plant X", plant owner role named, data verdict fresh
Check : G1 passed (verdict dated), G2 passed, G3 passed, G4 failed (a savings number without source),
        G5 passed, G6 passed, G7 not checked (no external connection), G7a passed
Output: go-live check record; result "no go-live" - remove the number or mark it to be collected;
        re-run G4 after the fix; final line "go-live decision: the plant's"
```

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Answering "yes" without evidence | It counts as "not checked"; a bare yes cannot be audited |
| Letting a failed block-level guardrail pass as a warning | Go-live then happens on a known defect |
| Presenting the candidate guardrails as an approved set | The OD lead has not confirmed them |
| Copying a screen by its title | Same-name dashboards differ per plant; check the template page and library entry |
| Using "not opened" as evidence of non-use | The exports carry no view counts |

## Do not

- Do not present the seeded guardrails as a finished, approved set.
- Do not let a failed guardrail pass as a warning when it is marked block.
- Do not set `PRODUCTIVE`; the plant decides.

## Definition of done

- The go-live check record is complete: every guardrail has a result, evidence, date and answering role.
- The utilization expectation is written into it.
- Any failure is routed back and re-checked after the fix.
- The plant owner role has the report for its go-live decision.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/technical-guardrails.md`](references/technical-guardrails.md) | The plant built or copied the screen itself: candidate guardrails G8 to G18, the same-name trap, and the IT technology guardrails |
| [`assets/go-live-check-record.md`](assets/go-live-check-record.md) | Writing the record the plant fills at go-live |
| [`references/outputs.md`](references/outputs.md) | Checking each output's recipient and completion rule |
| [`references/background.md`](references/background.md) | Why the guardrails exist, which are unconfirmed, and open questions; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
