---
name: od-it-handover
description: >-
  Hand a clear demand over to IT or an external developer as an OpenSpec change package they can
  work with directly - proposal, delta specs with SHALL requirements and WHEN/THEN scenarios, design,
  tasks - plus an OD handover annex with every artefact IT asked for in the OD x IT alignment
  (requirements, source-code ownership, deployment assumptions, Cyber Security inputs, access rights,
  data models, data and interface catalog entries), the business case with bankable value, investment
  envelope, rollout scenarios and TCO, the approval status, and the ownership terms (build-and-run,
  formal acceptance, handover checklist). The last step of the Lane 3 front-end and the route for 3a.3
  external build and 3a.4 foreign-app integration; also packages an IT demand for the evaluation board
  (formerly it-demand-package). Use when a Lane 3 demand has passed requirements, the tool-decision
  gate and the business case, when IT or an external developer must take over a build, or when someone
  asks what IT needs from OD.
license: MIT
metadata:
  id: od-it-handover
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3 front-end (34), Lane 3a (3a4)"
  new_state_step: "Handover once the demand is clear; Build or integrate (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 foreign app)"
  owner_role: OD lead (Thomas Zipf) for the Lane 3 front-end; IIAE for connector demands
  authority_level: draft the package and run its checks; IT or the external developer accepts it; submission, approval and the ownership transfer are human
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-requirements-breakdown, od-system-fit-check, od-benefit-calculation, od-investment-input, od-capital-request, od-decision-routing, od-cybersec-gate, od-acceptance-test, od-handover-and-adoption, deploy-appstore, od-data-availability-check, od-signal-standardization]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt and INDEX.md (OD x IT alignment: artefacts IT expects, catalogs, Cyber Security pre-evaluation, ownership and handover, guardrails, sourcing, business cases, legacy, Gemba lessons), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/lane-3-new-system-or-connector.md (front-end step 5 handover once the demand is clear; it-demand-package named as gap; error path: do not push an under-specified demand), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/README.md (Project Support & Application Consultancy transformed into the Lane 3 front-end), read 2026-11-10"
    - "OpenSpec (github.com/Fission-AI/OpenSpec, public): schemas/spec-driven/schema.yaml and templates, src/core/validation/constants.ts, docs/team-workflow.md, read 2026-11-10"
    - "Absorbed skills it-demand-package and od-project-support-consultancy (see references/), 2026-11-10"
  okf:
    type: Agent Skill
    title: IT handover
    tags: [lane-3, handover, openspec, it-alignment, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# IT handover

Read `od-context` first.

OD's value in Lane 3 sits in the span **requirements → decision gate → clear demand**; execution after
handover is IT's or the external developer's (department Lane 3 file). This skill is the last link of that
span: it turns a clear demand into an **OpenSpec change** that IT can review, build from and archive like
code, and attaches the OD handover annex with the inputs IT named on 2026-09-11. It replaces the
Project Support & Application Consultancy lane's "handover" and the earlier `it-demand-package`.

**Why OpenSpec.** IT asked for one consolidated set of artefacts from the requirements funnel and a place
to store and exchange them (action item 2, Ignacio). OpenSpec is a public, plain-markdown format for
exactly that: a change folder with `proposal.md`, delta `specs/`, `design.md` and `tasks.md`, versioned
in Git and reviewed in a pull request, checked by `openspec validate`. A package IT can open with its own
tooling is a cleaner handover than a slide deck.

## The rule it serves

**Hand off only once the demand is clear.** An under-specified demand stays in the front-end; it is never
pushed to IT or an external developer (department Lane 3, error paths). "Clear" is tested, not felt: the
package passes `scripts/check_handover.py` with no errors and no open blocking field.

## Where the flow puts it

| Where | Step | Route |
|---|---|---|
| Lane 3 front-end, step 34 | Handover once the demand is clear | After requirements (31), tool-decision gate (32), business case and capital request (33) |
| Lane 3a | 3a.3 external build (guided buy); 3a.4 integrate a foreign app | IT, Cyber Security gated |
| Lane 3a | 3a.1 / 3a.2, when IT must run what OD or externals deploy | Ownership terms of the annex; deploy with `deploy-appstore` |
| Lane 2 → 3 | A new use case that needs software chains here through the front-end | — |

## The references

| File | Use it for |
|---|---|
| [`references/openspec-format.md`](references/openspec-format.md) | The OpenSpec rules this package must meet, and which OD skill fills which artefact |
| [`references/it-expected-inputs.md`](references/it-expected-inputs.md) | What IT asked OD for on 2026-09-11, item by item, with the open IT actions that will firm each one |
| [`assets/openspec/`](assets/openspec/) | The templates: `config.yaml` (project context for IT's repository) and `change/` (proposal, spec, design, tasks, `.openspec.yaml`, `handover.md`) |
| `assets/example/` | An illustrative package (`*.example`; drop the suffix to use it) that passes this check and OpenSpec's own validator in strict mode; no figures |
| `scripts/new_handover.py` | Scaffold a change folder from the templates |
| `scripts/check_handover.py` | Check a package against OpenSpec's validation rules and the annex's blocking fields |
| [`references/it-demand-package/procedure.md`](references/it-demand-package/procedure.md) | Absorbed: the IT demand management package for the evaluation board (formerly `it-demand-package`) |
| [`references/od-project-support-consultancy/procedure.md`](references/od-project-support-consultancy/procedure.md) | Absorbed: the retired Project Support & Application Consultancy lane, kept for its composed protocols |

## Procedure

1. **Check the front-end is complete.** Requirement with growth boundaries (`od-requirements-breakdown`),
   gate verdict and route (`od-system-fit-check`, verdict Go or PoC-first), business case and investment
   estimate (`od-benefit-calculation`, `od-investment-input`), approval route (`od-capital-request`,
   `od-decision-routing`). If a part is missing, name it and stop.
2. **Scaffold** the change: `python3 scripts/new_handover.py <out-dir> <change-id>`. The change id is
   kebab-case and names the change (`add-downtime-reason-capture`), not the project.
3. **Fill `proposal.md`.** *Why* from the problem and the bankable value (50 to 1000 characters).
   *What Changes* from the requirement's scope. *Capabilities*: one per durable behaviour the epic
   describes, named for the behaviour (`downtime-reason-capture`), not the work. *Impact*: plants,
   systems, interfaces, data.
4. **Write one delta spec per capability** under `specs/<capability>/spec.md`: `## Purpose` (50+
   characters), then `## ADDED Requirements`; each `### Requirement:` states one behaviour with SHALL or
   MUST in its body (500 characters at most) and has at least one `#### Scenario:` with **WHEN** and
   **THEN**. User stories and acceptance criteria become scenarios (`od-acceptance-test`); data the
   system must read or publish becomes requirements on the data contract (`od-signal-standardization`,
   `od-data-availability-check`). No framework names, no class names: those go in `design.md`.
5. **Fill `design.md`**: the route (3a.1-3a.4 or 3b) and why, target platform (CMO with the standard
   manifests where the app is a container), interfaces (approved OT interfaces, reuse of central data
   stores), the data platform, Cyber Security constraints, the legacy application it replaces or touches,
   **non-goals = the growth boundaries**, risks.
6. **Fill `tasks.md`**: numbered checkbox groups. Always include logging and observability, the standard
   manifests, the acceptance test, the Cyber Security sign-off and the handover checklist.
7. **Fill `handover.md`** (the OD annex, not part of OpenSpec): every input IT asked for
   ([`references/it-expected-inputs.md`](references/it-expected-inputs.md)), the business case summary,
   the approval status, the ownership terms. Unknown stays ⟨…⟩ with who supplies it.
8. **Fill the project context** (`assets/openspec/config.yaml`) once per IT repository, if IT does not
   have one yet: stack, deployment, interfaces, guardrails, language rules.
9. **Run the check**: `python3 scripts/check_handover.py <out-dir>/openspec/changes/<change-id>`. It mirrors
   OpenSpec's validator in strict mode and adds the annex and the no-template rule; a package must report
   READY. Where the OpenSpec CLI is installed, `openspec validate <change-id> --strict` is the same check
   on IT's side (the example passed both, 2026-11-10).
10. **Hand over.** A human sends the package (pull request into IT's repository, or the demand board for
    3a.4 with the absorbed IT demand package). Record the demand as handed over, not accepted.
11. **Ownership moves only on formal acceptance** (`od-handover-and-adoption`). Until IT or the developer
    accepts, OD remains the owner of the demand. Do not pass a delivery date to the plant until a team has
    committed the work in sprint or PI planning.

## Output

`openspec/changes/<change-id>/` with `.openspec.yaml`, `proposal.md`, `specs/<capability>/spec.md`,
`design.md`, `tasks.md` and `handover.md`, plus `openspec/config.yaml` when the receiving repository needs
one; the check output attached.

## Definition of done

The check reports no errors; every blocking annex field is filled or the package is not sent; the route,
the approval status and the Cyber Security inputs are stated; a human has sent it; the demand record shows
"handed over, awaiting acceptance" with the receiving team named.

## Open - what only the OD lead and IT can supply

- ⟨The receiving repository or store for OpenSpec changes on the IT side⟩ - the meeting asked IT to define
  where each artefact is stored and exchanged (Ignacio).
- ⟨Published technology guardrails, sourcing criteria, ownership gates, platform-level Cyber Security
  model, data and interface catalog structure⟩ - open IT action items; the annex marks each.
- ⟨Whether IT adopts OpenSpec itself⟩ - proposed here; if IT keeps its own demand form, the absorbed IT
  demand package carries the same content.

## Do not

- Do not send a package that fails the check, or one with a blocking field ⟨open⟩.
- Do not put implementation choices into specs; requirements describe observable behaviour.
- Do not invent a figure, a date, a threshold, an owner or an IT field; mark it ⟨…⟩ and name who supplies it.
- Do not promise a delivery date; only a committed sprint or PI does that.
- Do not treat "sent" as "accepted"; ownership moves only on formal acceptance.
- Do not hand over a demand whose growth boundaries are not written down.
