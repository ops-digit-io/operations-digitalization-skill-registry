---
name: od-signal-standardization
description: >-
  Turn a connected machine's raw signals into standardized, use-case-ready data in the
  MDL — apply the process-related signal standard, build the transformation pipeline,
  keep the data model harmonized and compatible with ContiTech, and record the result in
  the readiness matrix. Use after a machine is connected to the IIoT Edge, when a data
  model needs harmonizing across plants, when a use case gets data it cannot compare with
  another plant's, or when a pipeline into the MDL is being specified or changed.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-signal-standardization
  tier: practice
  lane: information-integration-service
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: configure pipelines; recommend on standards (Consultation with ContiTech central)
  status: stable
  last_verified: 2026-08-10
  requires: [od-context]
  composes: [od-acceptance-test, od-data-availability-check]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,skills}.md
    - ops-knowledge-graph/.../10-modules/smart-factory-use-case/systems-of-record.md
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
---

# Signal standardization and pipelines

Read `od-context` first.

Connecting a machine gets you a signal. Standardizing it is what makes that signal
comparable to the same signal at the other thirty-two plants — which is the only reason a
cross-plant capability template means anything.

## The data path

| Data object | Source | Access path | Write right | Freshness |
|---|---|---|---|---|
| Machine / equipment signals | IIoT Edge Platform (plant Kubernetes runtime) | Edge → data pipelines | Data acquisition layer | near real-time |
| Standardized / transformed data | OESL Manufacturing Data Lake (MDL) | MDL API | Pipelines (ETL) | per pipeline |
| Use-case data exchange | Manufacturing Service Bus (MSB) | MSB | ⟨to confirm⟩ | event-driven |
| Machine/production data | MES (2 plants, in progress) / MDA/PDA (16 deployed) | ⟨interface — to confirm⟩ | ERP-dependent (MES) | ⟨to confirm⟩ |

Deployment reality to plan against (Route 25): MDA/PDA ≈16 and MDL ≈14 significantly
deployed; IIoT Edge significantly deployed; MES 2 in progress with rollout on hold and
ERP-dependent; **MSB limited**; MIL high demand and not deployed; EMS deployed but rollout
stopped pending operational criteria.

## Procedure

1. **Identify the process-related signals** the use case actually needs — cycle time,
   downtime reason, process value, recipe value, quality datum. Standardize what is
   needed, not everything the PLC emits.
2. **Apply the signal standard.** Signal standardization is aligned with M+E and machine
   standards, and must maintain **interface compatibility to ContiTech**.
3. **Build the transformation pipeline** into the MDL. The pipeline is the write right —
   nothing else writes standardized data.
4. **Verify against a second plant.** If the same capability at another plant cannot
   consume the result the same way, the signal is not standardized, it is merely
   transformed.
5. **Record the readiness change** in the Scorecard's System Integration and Availability
   matrix — RAG per readiness dimension × location.
6. Hand to `od-acceptance-test`; the receiving lanes then run
   `od-data-availability-check` against the MDL.

## Decision rights on the standard itself

Changing a data model or a signal standard is **Consultation** — IIAE hears ContiTech
central, then decides — at `recommend` authority, reversible, with the standing
constraint that ContiTech interface compatibility is maintained. Machine standards for
digital connection sit one level up: OD lead, in Consultation with Manufacturing
Engineering, aligned with M+E standards.

An agent may draft and propose a standard change. It may **not** enact one.

## Known weaknesses this skill runs into

- **Operations concepts are missing or immature for MDL, MSB and MDA/PDA.** Rollouts
  stall and support load rises. A pipeline built onto a system with no operations concept
  is a support ticket waiting to happen — record it as a risk, do not absorb it silently.
- **Internal IT knowledge of MDL and MDA/PDA is limited**, creating single points of
  failure. Share through COP rather than accumulating it in one head.

## Definition of done

Signals standardized to the agreed standard, transformation pipeline writing into the
MDL, a second plant's instance of the same capability able to consume the result, and the
readiness matrix updated with evidence.

## Do not

- Do not fix a standardization gap downstream in the dashboard. A per-plant transformation
  buried in a Grafana query is how comparability is lost.
- Do not mark a readiness dimension green because the pipeline runs; green means
  *available* to a use case.
- Do not introduce a new tool to solve a pipeline problem — the strategy is a deliberately
  **small operational footprint**, and broad tool proliferation is an explicit non-bet.
