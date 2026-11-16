---
name: dept-risk
description: >-
  Answers "has any department risk crossed its escalation trigger this month?". Reads the early
  indicators against the six-row risk register: finds the monitorable value per risk, reads it from its
  source with a date, compares it with the trigger, classifies each risk as triggered, on watch, clear or
  unreadable (no source), and drafts the risk reading for the OD lead. It never scores risks. Use when the
  monthly risk review is due, before a COP round, after a blocked rollout or a Cyber Security finding, or
  when someone asks whether a risk needs escalation. Not for the monthly improvement decision
  (dept-retro) or for judging one use case or project risk (deploy-project-order).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-risk
  aliases: [od-risk-watch]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only on sources; draft the risk reading
  status: draft
  requires: [dept-context]
  composes: [metrics-scorecard, bc-portfolio, dept-decision-rights, dept-retro, deploy-cybersec, invest-screen]
  okf:
    type: Agent Skill
    title: Risk watch
    tags: [all, practice, new-state, draft]
---

# Risk watch

- Read `dept-context` first.
- The risk register (`09-risks.md`) is reviewed monthly and built so that an agent can watch it: an early indicator is a monitorable value.
- It has **no probability x damage matrix** (false precision; the early indicator does more), so this skill never scores risks: it reads indicators and tests triggers.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## What it produces

- A dated **risk reading**: for each of the six registered risks, the indicator value with its source and read date, the escalation trigger, and a status.
- Then the triggers hit, with the forum they go to.
- The draft goes to the OD lead role, who owns five of the six risks (the sixth, value not materializing, is owned by the DBVE role).

## The references

| File | Open when |
|---|---|
| [`references/risk-indicators.md`](references/risk-indicators.md) | Step 2: you read an indicator and need its source, field, filter, trigger test and the gaps that make it unreadable |
| [`assets/risk-reading.md`](assets/risk-reading.md) | Step 1: you start the monthly reading to fill |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Steps 5-7: you need supporting indicators from the chain, the blocker brief, cadence formats or the scoring conflict to avoid |
| [`references/background.md`](references/background.md) | You need the provenance, the open points or the required-output table; never an instruction |

## Statuses

| Status | Meaning |
|---|---|
| **Triggered** | The register's escalation trigger is met by a value read from a source, dated |
| **On watch** | The indicator shows movement toward the trigger, or the trigger has an open parameter and the value is close by any reasonable reading; say why |
| **Clear** | The indicator is read from a source and the trigger is not met |
| **Unreadable** | No source for the indicator, or the trigger parameter is `⟨n⟩` (undefined). This is a finding, not a pass |

- "Unreadable" is not "clear". Some indicators typically have no named source or an undefined parameter (see `references/risk-indicators.md`).
- Reporting them as clear would be the exact failure the honesty rules forbid.

## Procedure

1. **Open the register** (`09-risks.md`) and note its `last-verified` date. If the register itself is older than the month, say so in the reading's header; the register is the thing being watched.
2. **For each risk, read the indicator** at the source named in `references/risk-indicators.md`. Refetch live figures (Power BI, lists); treat any knowledge base aggregate only as a labelled, dated snapshot and never as the reading.
3. **Test the trigger** exactly as written in the register. Where it contains a parameter in brackets (`open role > ⟨n⟩ months`), the trigger cannot be tested: status *Unreadable*, with the parameter named for the OD lead to set.
4. **Classify** per the statuses above. Write the evidence in one sentence.
5. **List triggers hit** and route each: the risk owner is given in the register;
   - the forum is the OD lead or the deciding role named in the current approval policy (look up) for strategy, priority and rollout matters, COP for technical ones (`06-operating-rhythm.md`); use `dept-decision-rights` for any decision outside OD.
   - Cyber Security items go through the gate in `deploy-cybersec` (planned).
6. **Name the countermeasure in the register** next to each triggered or on-watch risk. The register already lists it; do not invent others. A new countermeasure is a proposal for the OD lead and is marked as one.
7. **Hand to the retro.** The reading is an input of `dept-retro`. A trigger hit two months running is a candidate for the retro's one adjustment.
8. **Check the register for staleness:** a risk whose indicator has been *Unreadable* three months in a row means the register row needs a source or a rewrite; propose that.
9. **Check completeness before the draft goes to the OD lead.** All six risks carry value, source, read date, trigger and status.
   - Every status has one sentence of evidence; every unreadable row names what is missing and which role could supply it.
   - Fix the gaps and check again.

## Decision table: what a triggered risk goes to

| Risk (register wording) | Trigger | Where it goes |
|---|---|---|
| Missing operations concept for core systems | Rollout blocked at a strategic plant | OD lead / deciding role per the current approval policy (rollout and priority); tool rollout decision is the OD lead's (`08-decision-rights.md`) |
| Key-person / staffing gaps | Open role > `⟨n⟩` months | OD lead / deciding role per the current approval policy; the staffing plan is global ("Global staffing plan") |
| Limited internal IT knowledge | Single point of failure identified | COP (knowledge sharing via COP is the stated countermeasure) |
| External tooling dependence | Decision delayed past plan | OD lead / deciding role per the current approval policy; the owner is `⟨to confirm⟩` in the register |
| Cyber Security / OT exposure | Security gap on connected asset | COP for the technical aspect; Cyber Security sign-off gate; never act on an external machine connection without sign-off |
| Value not materializing | Impact < target for the quarter | OD lead / deciding role per the current approval policy; DBVE owns; gauge value delivery before scale-out (a metric not captured today) |

## Example (fictional)

```text
Risk reading 2026-03 (fictional). Register last-verified 2026-02-10 (older than the month: stated).
Risk                        | Value read            | Source, date      | Trigger                 | Status
Missing operations concept  | 1 rollout blocked     | rollout list 03-02| blocked at strategic pl.| triggered
Key-person / staffing       | 1 open role, age 5 mo | HR view 03-02     | open role > <n> months  | unreadable (n undefined)
Limited internal IT know-how| no single point named | COP notes 03-05   | single point of failure | clear
External tooling dependence| decision 2 weeks late | decision log 03-03| delayed past plan       | on watch (approaching)
Cyber Security / OT         | 0 open findings       | CS tracker 03-04  | gap on connected asset  | clear
Value not materializing     | no target defined     | -                 | impact < target         | unreadable (no target)
Triggers hit: row 1 -> deciding role per approval policy. Unreadable twice -> proposal to the OD lead.
```

## Pitfalls

- **Importing probability or impact scoring** from project plans into the register. The register excludes it by design (`references/process-chain-practice.md`).
- **Assigning colours or scores** the register does not have; the status is one of four words.
- **Reporting an unreadable indicator as clear.** Silence is a finding, because a risk nobody can read is not a risk that is absent.
- **Taking a knowledge base aggregate as a live reading.** Label the snapshot date, because aggregates lag the lists.
- **Adding risks to the register.** Propose them to the OD lead.
- **Escalating by e-mail or by name.** Use the round and the role.

## Human gate and AI-agent notes

- The register names risk owners, not who may declare a trigger "triggered": the skill drafts; the OD lead role confirms.
- The agent is read-only on sources and never changes the register, a countermeasure or a status the OD lead has confirmed.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need the provenance, the open points or the required-output table; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
