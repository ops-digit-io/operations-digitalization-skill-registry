---
name: od-risk-watch
description: >-
  Read the department's early indicators against the six-row risk register each month and say
  which escalation triggers are hit - for every risk, find the monitorable value, read it from
  its source with a date, compare it with the trigger, and classify the risk as triggered, on
  watch, clear or unreadable (no source), then draft the risk reading for the OD lead. Use when
  the monthly risk review is due, before an ODEC or COP round, after a blocked rollout or a
  Cyber Security finding, or when someone asks whether any risk has crossed its escalation trigger.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-risk-watch
  tier: practice
  lane: all
  new_state_lane: Spine
  new_state_step: Risk watch
  owner_role: human:jakob.gabriel
  authority_level: read-only on sources; draft the risk reading
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-scorecard-reporting, od-portfolio-and-savings-analysis, od-decision-routing, od-retro, od-cybersec-gate, od-system-fit-check]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/09-risks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/12-portfolio.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/07-metrics.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/13-swot.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/capabilities.md
    - Work vault (Work-OpsDigit-Knowledge), Graph/Registers/Blocker Register (export of 2026-08-21), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Legacy Applications (268 notes, cyber-security status field) and Graph/Plants tool-rollout lines, aggregated 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), ODEC Facts, Department KPIs and Roadmap Status, strategy recap slide, read 2026-11-05
  okf:
    type: Agent Skill
    title: Risk watch
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Risk watch

Read `od-context` first.

Plan item O-07 of the department's skill map. The risk register (`09-risks.md`, review cadence **monthly**) is built
so that an agent can watch it: "an early indicator is a monitorable value - a register an agent can watch, not a table
opened once a year". It deliberately has **no probability x damage matrix** ("false precision; the early indicator does
more"). This skill therefore never scores risks; it reads indicators and tests triggers.

## What it produces

A dated **risk reading**: for each of the six registered risks, the indicator value with its source and read date, the
escalation trigger, and a status. Then the triggers hit, with the forum they go to. The draft goes to the OD lead role,
who owns five of the six risks (the sixth, value not materializing, is owned by the DBVE role).

## The references

| File | Use it for |
|---|---|
| [`references/risk-indicators.md`](references/risk-indicators.md) | The six risks, one by one: where the indicator is read, how to read the indicator live (source, field, filter), the trigger test, the kinds of gap that make an indicator unreadable |
| [`assets/risk-reading.md`](assets/risk-reading.md) | The monthly reading to fill |

## Statuses

| Status | Meaning |
|---|---|
| **Triggered** | The register's escalation trigger is met by a value read from a source, dated |
| **On watch** | The indicator shows movement toward the trigger, or the trigger has an open parameter and the value is close by any reasonable reading; say why |
| **Clear** | The indicator is read from a source and the trigger is not met |
| **Unreadable** | No source for the indicator, or the trigger parameter is `⟨n⟩` (undefined). This is a finding, not a pass |

"Unreadable" is not "clear". Some indicators typically have no named source or an undefined parameter (see the
reference); reporting them as clear would be the exact failure the honesty rules forbid.

## Procedure

1. **Open the register** (`09-risks.md`) and note its `last-verified` date. If the register itself is older than the
   month, say so in the reading's header; the register is the thing being watched.
2. **For each risk, read the indicator** at the source named in
   [`risk-indicators.md`](references/risk-indicators.md). Refetch live figures (Power BI, lists); treat any vault aggregate only
   as a labelled, dated snapshot and never as the reading.
3. **Test the trigger** exactly as written in the register. Where it contains a parameter in brackets (`open role > ⟨n⟩
   months`), the trigger cannot be tested: status *Unreadable*, with the parameter named for the OD lead to set.
4. **Classify** per the statuses above. Write the evidence in one sentence.
5. **List triggers hit** and route each: the risk owner is given in the register; the forum is ODEC for strategy, priority
   and rollout matters, COP for technical ones (`06-operating-rhythm.md`); use `od-decision-routing` for any decision
   outside OD. Cyber Security items go through the gate in `od-cybersec-gate` (planned).
6. **Name the countermeasure in the register** next to each triggered or on-watch risk. The register already lists it;
   do not invent others. A new countermeasure is a proposal for the OD lead and is marked as one.
7. **Hand to the retro.** The reading is an input of `od-retro`. A trigger hit two months running is a candidate for the
   retro's one adjustment.
8. **Check the register for staleness:** a risk whose indicator has been *Unreadable* three months in a row means the
   register row needs a source or a rewrite; propose that.

## Decision table: what a triggered risk goes to

| Risk (register wording) | Trigger | Where it goes |
|---|---|---|
| Missing operations concept for core systems | Rollout blocked at a strategic plant | ODEC (rollout and priority); tool rollout decision is the OD lead's (`08-decision-rights.md`) |
| Key-person / staffing gaps | Open role > `⟨n⟩` months | ODEC; the staffing plan is global ("Global staffing plan") |
| Limited internal IT knowledge | Single point of failure identified | COP (knowledge sharing via COP is the stated countermeasure) |
| External tooling dependence | Decision delayed past plan | ODEC; the owner is `⟨to confirm⟩` in the register |
| Cyber Security / OT exposure | Security gap on connected asset | COP for the technical aspect; Cyber Security sign-off gate; never act on an external machine connection without sign-off |
| Value not materializing | Impact < target for the quarter | ODEC; DBVE owns; gauge value delivery before scale-out (a metric not captured today) |

## What is still open

- **Parameters:** `open role > ⟨n⟩ months` has no n unless the OD lead has set one; "impact < target" needs a defined target for use-case impact.
- **Sources with no system named:** support tickets, open-role list, "dependence on few individuals".
- **Owner of the external-tooling risk** is `⟨to confirm⟩` in the register.
- **Escalation window** of ODEC and COP is `⟨to confirm⟩`.
- **Who may declare a trigger "triggered"**: the register names risk owners, not a declarer. The skill drafts; the OD lead role confirms.

## Do not

- Do not assign probabilities, impact scores or colours that the register excludes by design.
- Do not report an unreadable indicator as clear.
- Do not take a vault aggregate as a live reading; label the snapshot date.
- Do not add risks to the register; propose them to the OD lead.
- Do not escalate by e-mail or by name; use the round and the role.
