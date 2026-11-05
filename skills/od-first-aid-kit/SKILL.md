---
name: od-first-aid-kit
description: >-
  Capture an ad-hoc plant process issue (a ramp-up problem, a trouble-shooting case, an unexplained process behaviour) in a structured first-aid request - problem made S.M.A.R.T., process and machine, what data exists, which of the two data scenarios applies, who benefits - and route it either to Analytical Support (a one-off insight) or to use case intake (a recurring need), or back as a data gap. Drafts the request; does not install devices or commit cost. Use when a plant raises a process issue and there is no use case yet, when someone asks for the Process First-Aid Kit, or when a one-off analytical request must be scoped before analysis starts.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-first-aid-kit
  tier: practice
  lane: use-case-support-service
  new_state_lane: Intake and Lane 2 (step 1)
  new_state_step: "Define and diagnose: first aid"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-use-case-definition, od-analytical-support-service, od-data-availability-check, od-requirements-breakdown, od-cybersec-gate, od-equipment-integration, od-decision-routing, od-system-fit-check]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/04-service-catalog.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/05-intake.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/14-glossary.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/analytical-support-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/analytical-support-service/tasks.md
    - Work vault (Work-OpsDigit-Knowledge), Slide Index and Split Slides of the Data Science Factory tool deck in 03-AMT_MI_Standard_Agenda_Use_Case_Workshop, slides 11 and 12 First AID Kit (dated 2024-07-14; repeated in decks of 2025-01-17 and 2025-05-07), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Slide Index - 25-Adhoc_Analysis (two Waltershausen ad-hoc analyses of 2024), read 2026-11-05
    - Skill od-analytical-support-service, SKILL.md and references/composed-artefacts.md (happy path, error paths, the open Process First-Aid Kit template)
    - Skill od-use-case-definition, assets/use-case-definition-questionnaire.md (a need that surfaces once is a first-aid request)
    - Skill od-use-case-support-service, references/lane-templates.md (the first-aid template gap)
  okf:
    type: Agent Skill
    title: Process First-Aid Kit
    tags: [use-case-support-service, practice, first-aid, ad-hoc]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process First-Aid Kit

Read `od-context` first. The service catalogue lists the Smart Factory Use Case Support Service
"(incl. Process First-Aid Kit)"; the glossary calls it a "rapid diagnostic offering within Use Case
Support Service", next to Ad-Hoc Analytics in the Analytical Support Service. The lane's recurring
tasks list "Process First-Aid Kit request — ad-hoc plant process issue" with the template marked
"to confirm", and two registry pages (`od-analytical-support-service`, `od-use-case-support-service`)
record that no dedicated template exists. This skill supplies the **working version of that
template** and the routing rule. It is a draft for the DBVE to adopt or replace.

## What the offering is, in OD's words

From the IIoT Edge platform deck (2024-07-14, repeated 2025): purpose is **process or product
ramp-up support** and **process or product trouble shooting**. What OD does: prepare process data
acquisition that fulfils the analytics requirements, **make problems S.M.A.R.T.**, generate
insights. Details, the two data scenarios, a priced example and two ad-hoc analyses that show the
shape of the work: [`references/first-aid-offering.md`](references/first-aid-offering.md).

## When it applies, and when it does not

| Situation | Use this skill? | Instead |
|---|---|---|
| A process issue now, no use case, plant wants insight | Yes | |
| The need keeps coming back every shift or week | Capture it, then route to intake | `od-use-case-intake-triage`, then `od-use-case-definition` |
| A request to change the look of an existing dashboard | No | `od-use-case-intake-triage` (refusal playbook) |
| Plant wants a machine connected for good | No, that is integration | Information Integration lane, `od-equipment-integration` |
| Request without an owner who can confirm facts at the plant | Not yet | Ask the Plant ME to name one |

## Procedure

1. **Receive and log the request** (channel: "ad-hoc analytics / Process First-Aid Kit requests",
   `05-intake.md`). Note date, plant, requester role. ⟨Central queue or mailbox — "to confirm" in
   `05-intake.md`⟩.
2. **Fill the first-aid request**
   ([`assets/first-aid-request.md`](assets/first-aid-request.md)) with the requester, in this order:
   the symptom in plain words; where and since when; the process and machine; what is already
   measured; what has been tried; what decision the answer will inform; who at the plant owns the
   answer. If the requester cannot state a question, run the S.M.A.R.T. step of the form before
   anything else.
3. **Make it S.M.A.R.T.** Restate the problem so that it has a measurable symptom, a defined scope,
   a question the data can answer, a reason it matters and a time frame. The deck does not expand
   the acronym; the usual expansion (specific, measurable, achievable, relevant, time-bound) is the
   working assumption here. Use the examples in the offering reference to see the difference
   between "diameter oscillates" and a question a dataset can answer.
4. **Check the data** with `od-data-availability-check`: is the signal readable, at what
   resolution, for what period? Classify into the two scenarios of the offering (A: edge platform
   and compliant network available; B: no way to connect the machine to an available edge
   installation). Scenario B means a device on the machine and manual transfer of data; any
   connection to a machine needs `od-cybersec-gate` first and is not committed by this skill.
5. **Decide the route** with the table below, and write the reason on the form.
6. **State the cost question honestly.** The deck gives an indication of "3k EUR additional invest
   up to 20k EUR depending on preconditions" (2024-07-14). That is a range from a tool deck, not
   a quote. Do not offer it to a plant as a price. Cost goes to the OD lead
   (`od-decision-routing`; investment is not a draft decision).
7. **Hand over with the form.** The form travels with the request so the next skill does not
   re-ask. Close the loop with the requester (what was routed where and why).

## Routing decision

| Finding | Route | Why / source |
|---|---|---|
| One-off question, data readable, insight is the answer | `od-analytical-support-service` (step 1 scoping, then `od-data-availability-check`) | "Insight, not an industrialized solution"; refusing to industrialize is valid |
| One-off question, data not readable on the data platform | Information Integration lane, mark a **data gap**; do not approximate missing data | Analytical Support error path |
| Same need raised by several shifts, lines or plants, or recurring | `od-use-case-intake-triage` then `od-use-case-definition` | Questionnaire: a need that surfaces once is first aid; recurring is a use case |
| Insight delivered and used repeatedly, with recurring value | Promotion to a standard use case via `od-use-case-standardization` (planned `od-use-case-promotion`) | Analytical Support step 6 |
| Needs a system outside the lean standardized footprint | Refuse and say why | `05-intake.md` |
| Needs new connectivity or a Cyber Security decision | `od-cybersec-gate`, Information Integration lane | Wait state in the lane playbook |
| Plant cannot name a question or an owner | Back to requester with the missing items | |

⟨Whether the roadmap-link and business-case refusal rule of `05-intake.md` also applies to a
first-aid request — the source states it for requests in general; first aid is not mentioned
there. Supplier: OD lead.⟩

## Definition of done

The request form is complete or lists exactly what is missing; the problem is restated S.M.A.R.T.;
data availability and scenario are recorded; the route is chosen with a written reason; the
requester has been told; no cost or connection has been promised.

## What is still open

- ⟨Official first-aid template⟩ — not in any source. Supplier: DBVE.
- ⟨Lead time and capacity for first-aid requests⟩ — all lane lead times are "to confirm". Supplier:
  OD lead.
- ⟨Who pays⟩ — the priced example in the deck does not say which budget carried it. Supplier: OD lead.
- ⟨Turnaround and promotion-rate trackers⟩ — named as missing in `od-analytical-support-service`.
- ⟨Closing rule⟩ — when a first-aid case counts as done (insight delivered, or insight understood).
  The lane's definition of done for analytical support is "process diagnostics / analytical insight
  delivered".

## Do not

- Do not turn a one-off issue into a use case just because it is interesting.
- Do not quote the price range as an offer.
- Do not connect, install or reconfigure anything; propose it, route it, and respect the Cyber
  Security gate.
- Do not invent missing data or fill gaps by interpolation (Analytical Support error path).
- Do not name people in the form; use roles. No hostnames, addresses or credentials.
