---
name: it-demand-package
description: >-
  Hand a cleared Lane 3 demand to IT or an outside developer as an OpenSpec change package plus OD handover annex. Not for requirements (od-requirements-breakdown) or tool choice (od-system-fit-check).
license: MIT
metadata:
  id: it-demand-package
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3a (3a.3, 3a.4); hand-off at the end of the Lane 3 front-end (step 3)"
  new_state_step: "3a.3 New codebase (external dev); 3a.4 Integrate a foreign app; front-end step 3 hand off once demand is clear"
  department_names: ["it-demand-package"]
  owner_role: OD lead for the Lane 3 front-end; IIAE for connector demands
  tags: [lane-3, handover, openspec, it-alignment, practice]
  authority_level: draft the package and run its checks; IT or the external developer accepts it; submission, approval and the ownership transfer are human
  status: draft
  requires: [od-context]
  composes: [od-requirements-breakdown, od-system-fit-check, od-benefit-calculation, od-investment-input, od-capital-request, od-decision-routing, od-cybersec-gate, od-acceptance-test, od-handover-and-adoption, deploy-appstore, od-data-availability-check, od-signal-standardization]
  okf:
    type: Agent Skill
    title: IT handover
    tags: [lane-3, handover, openspec, it-alignment, practice]
---
# IT handover

Read `od-context` first.

OD's value in Lane 3 sits in the span **requirements → decision gate → clear demand**; execution after
handover is IT's or the external developer's (department Lane 3 file). This skill is the last link of that
span: it turns a clear demand into an **OpenSpec change** that IT can review, build from and archive like
code, and attaches the OD handover annex with the inputs IT named on 2026-09-11. It replaces the
Project Support & Application Consultancy lane's "handover" and the earlier `it-demand-package`.

**Why OpenSpec.** IT asked for one consolidated set of artefacts from the requirements funnel and a place
to store and exchange them (action item 2, IT). OpenSpec is a public, plain-markdown format for
exactly that: a change folder with `proposal.md`, delta `specs/`, `design.md` and `tasks.md`, versioned
in Git and reviewed in a pull request, checked by `openspec validate`. A package IT can open with its own
tooling is a cleaner handover than a slide deck.

## Purpose

Turns a clear Lane 3 demand into an OpenSpec change package plus the OD handover annex, so IT or an external developer can take over the build. Use it after requirements, the tool-decision gate and the business case are done, and when someone asks what IT needs from OD.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the front-end results named in step 2 of the Procedure (requirement with growth boundaries, gate verdict and route, business case and investment estimate, approval route), plus every file or note the user adds: PDF, Excel, images, slides, mails, exports, links. All of it is collected in step 1, read, and registered.
- **Out:** `openspec/changes/<change-id>/` with the OpenSpec files and `handover.md`, and the check output (see Output below).

## The rule it serves

**Hand off only once the demand is clear.** An under-specified demand stays in the front-end; it is never
pushed to IT or an external developer (department Lane 3, error paths). "Clear" is tested, not felt: the
package passes `scripts/check_handover.py` with no errors and no open blocking field.

## Where the flow puts it

| Where | Step | Route |
|---|---|---|
| Lane 3 front-end, end of step 3 | Business case & capital request: hand off once demand is clear | After requirements engineering (1) and the tool-decision / IT-footprint gate (2) |
| Lane 3a | 3a.3 external build (guided buy); 3a.4 integrate a foreign app | IT, Cyber Security gated |
| Lane 3a | 3a.1 / 3a.2, when IT must run what OD or externals deploy | Ownership terms of the annex; deploy with `deploy-appstore` |
| Lane 2 → 3 | A new use case that needs software chains here through the front-end | — |

## The references

| File | Use it for |
|---|---|
| [`references/openspec-format.md`](references/openspec-format.md) | The OpenSpec rules this package must meet, and which OD skill fills which artefact |
| [`references/input-intake.md`](references/input-intake.md) | How to collect every input, including the user's own files (PDF, Excel, images, slides, mails), read each by type, register it and trace it |
| [`references/it-expected-inputs.md`](references/it-expected-inputs.md) | What IT asked OD for on 2026-09-11, item by item, with the open IT actions that will firm each one |
| [`references/openspec/VENDORED.md`](references/openspec/VENDORED.md) | OpenSpec 1.17.0 as its authors ship it: the agent skills (`openspec-propose`, `openspec-new-change`, `openspec-continue-change`, `openspec-apply-change`, ...), the spec-driven schema and templates, the docs including the store guide. Unchanged; this skill follows them |
| [`assets/openspec/config.yaml.tmpl`](assets/openspec/config.yaml.tmpl) | OD's project context and per-artifact rules for the OD store; OpenSpec hands them to its skills through `openspec instructions` |
| [`assets/openspec/change/handover.md.tmpl`](assets/openspec/change/handover.md.tmpl) | The OD annex, the one file OD adds to an OpenSpec change |
| `assets/example/` | An illustrative package (`*.example`; drop the suffix to use it) that passes this check and OpenSpec's own validator in strict mode; no figures |
| [`scripts/new_handover.py`](scripts/new_handover.py) | Add the OD annex and `attachments/` to a change OpenSpec created |
| [`scripts/check_handover.py`](scripts/check_handover.py) | Run the OpenSpec CLI in strict mode on a package, then check the annex's blocking fields |
| [`references/it-demand-package/procedure.md`](references/it-demand-package/procedure.md) | Absorbed: the IT demand management package for the evaluation board (formerly `it-demand-package`) |
| [`references/od-project-support-consultancy/procedure.md`](references/od-project-support-consultancy/procedure.md) | Absorbed: the retired Project Support & Application Consultancy lane, kept for its composed protocols |

## Procedure

1. **Collect every input first** ([`references/input-intake.md`](references/input-intake.md)). Show the user the twelve
   expected inputs as a checklist (known, partly known, missing) and ask for each gap. Invite any further material,
   in any form: PDF, Excel or CSV, Word or slides, images and screenshots, mails, exports, links. Repeat "anything
   else?" until the answer is no. Read every file completely, by its type; ask who may see it. Copy each file to
   `attachments/` in the change folder and register it in section 14 of `handover.md`. Nothing provided is dropped and
   nothing is filled in that no input supports.
2. **Check the front-end is complete.** Requirement with growth boundaries (`od-requirements-breakdown`),
   gate verdict and route (`od-system-fit-check`, verdict Go or PoC-first), business case and investment
   estimate (`od-benefit-calculation`, `od-investment-input`), approval route (`od-capital-request`,
   `od-decision-routing`). If a part is missing, name it and stop.
3. **Work in the OD store.** OD drafts every change in its own OpenSpec store (a Git repository) and hands it over
   from there ([`store guide`](references/openspec/docs/stores-beta/user-guide.md)). Once per machine a human clones
   it and runs `openspec store register <path>`; the very first time, `openspec store setup <od-store> --path <path>
   --remote <repository URL>`. The store's `openspec/config.yaml` carries OD's context and rules
   ([`assets/openspec/config.yaml.tmpl`](assets/openspec/config.yaml.tmpl)); OpenSpec passes them to its skills for
   every artifact. All OpenSpec commands below take `--store <od-store>`.
4. **Create the change with OpenSpec's own skills, never by hand.** Follow
   [`openspec-propose`](references/openspec/skills/openspec-propose/SKILL.md) to create the change and all its
   artifacts in one pass, or [`openspec-new-change`](references/openspec/skills/openspec-new-change/SKILL.md) and then
   [`openspec-continue-change`](references/openspec/skills/openspec-continue-change/SKILL.md) for one reviewed
   artifact at a time; [`openspec-explore`](references/openspec/skills/openspec-explore/SKILL.md) first when the
   demand is still unclear. Give them the inputs from step 1 and the front-end results; which OD result feeds which
   artifact is in [`openspec-format.md`](references/openspec-format.md). The change id is kebab-case and names the
   change (`add-downtime-reason-capture`), not the project. Later edits go through
   [`openspec-update-change`](references/openspec/skills/openspec-update-change/SKILL.md).
5. **Add the OD part**: `python3 scripts/new_handover.py <store>/openspec/changes/<change-id> --with-config`. It adds
   `handover.md` (the OD annex, not part of OpenSpec) and `attachments/`, and writes OD's `config.yaml` where the store
   has only OpenSpec's default. Copy the user's files into `attachments/` and fill the annex: every input IT asked for
   ([`references/it-expected-inputs.md`](references/it-expected-inputs.md)), the business case summary, the approval
   status, the ownership terms and the register of every input (section 14). Unknown stays ⟨…⟩ with who supplies it.
6. **Run the check**: `python3 scripts/check_handover.py <store>/openspec/changes/<change-id>`. It runs the real
   OpenSpec CLI (`openspec validate <change-id> --strict`, release 1.17.0) and fails without it, then checks the annex,
   the attachments and the no-template rule; a package must report READY. CI proves the worked example, the OD part
   and the OpenSpec copy against that release (`scripts/check_openspec_conformance.py`,
   `scripts/sync_openspec_vendor.py --check`).
7. **Hand over.** A human commits and pushes the change in the OD store and opens a pull request there for review. IT
   reads it with `openspec show <change-id> --store <od-store>`, or lists the store under `references:` in its own
   repository's `openspec/config.yaml`. For 3a.4 the absorbed IT demand package goes to the demand board as well.
   Record the demand as handed over, not accepted.
8. **IT builds with OpenSpec's skills, not OD.** IT implements with
   [`openspec-apply-change`](references/openspec/skills/openspec-apply-change/SKILL.md), checks the result with
   [`openspec-verify-change`](references/openspec/skills/openspec-verify-change/SKILL.md) and closes with
   [`openspec-archive-change`](references/openspec/skills/openspec-archive-change/SKILL.md) or
   [`openspec-sync-specs`](references/openspec/skills/openspec-sync-specs/SKILL.md). OD does not run these.
9. **Ownership moves only on formal acceptance** (`od-handover-and-adoption`). Until IT or the developer
   accepts, OD remains the owner of the demand. Do not pass a delivery date to the plant until a team has
   committed the work in sprint or PI planning.

## OpenSpec skills in this handover

| OpenSpec skill | Who | When |
|---|---|---|
| [`openspec-onboard`](references/openspec/skills/openspec-onboard/SKILL.md) | OD, once | Learning the OpenSpec workflow |
| [`openspec-explore`](references/openspec/skills/openspec-explore/SKILL.md) | OD | Clarifying a demand before the change exists |
| [`openspec-propose`](references/openspec/skills/openspec-propose/SKILL.md) | OD | Creating the change and all artifacts in one pass (step 4) |
| [`openspec-new-change`](references/openspec/skills/openspec-new-change/SKILL.md), [`openspec-continue-change`](references/openspec/skills/openspec-continue-change/SKILL.md), [`openspec-ff-change`](references/openspec/skills/openspec-ff-change/SKILL.md) | OD | Creating the change artifact by artifact, or fast-forwarding the rest (step 4) |
| [`openspec-update-change`](references/openspec/skills/openspec-update-change/SKILL.md) | OD | Changing artifacts after review or new inputs |
| [`openspec-apply-change`](references/openspec/skills/openspec-apply-change/SKILL.md) | IT | Implementing the tasks (step 8) |
| [`openspec-verify-change`](references/openspec/skills/openspec-verify-change/SKILL.md) | IT | Checking the implementation against the change before archive |
| [`openspec-archive-change`](references/openspec/skills/openspec-archive-change/SKILL.md), [`openspec-bulk-archive-change`](references/openspec/skills/openspec-bulk-archive-change/SKILL.md), [`openspec-sync-specs`](references/openspec/skills/openspec-sync-specs/SKILL.md) | IT | Folding the finished change into the main specs |

## Output

`<od-store>/openspec/changes/<change-id>/` as OpenSpec's skills write it (`.openspec.yaml`, `proposal.md`,
`specs/<capability>/spec.md`, `design.md`, `tasks.md`), plus OD's `handover.md` and the user's files under
`attachments/` (each registered in section 14 of `handover.md`); OD's `config.yaml` in the store; the check output
attached.

## Definition of done

The check reports no errors; every blocking annex field is filled or the package is not sent; every file the user provided is
in `attachments/` and registered, read in full or carried as an open item; the route,
the approval status and the Cyber Security inputs are stated; a human has sent it; the demand record shows
"handed over, awaiting acceptance" with the receiving team named.

## Open - what only the OD lead and IT can supply

- ⟨The OD store: its id and repository URL⟩ - decided: OD drafts in its own OpenSpec store; the OD lead sets it
  up once (`openspec store setup`) and names it here.
- ⟨How IT takes a change from the OD store: `references:` in its repositories, or a copy into its own store⟩ -
  the meeting asked IT to define where each artefact is stored and exchanged (IT).
- ⟨Published technology guardrails, sourcing criteria, ownership gates, platform-level Cyber Security
  model, data and interface catalog structure⟩ - open IT action items; the annex marks each.
- ⟨Whether IT adopts OpenSpec itself⟩ - proposed here; if IT keeps its own demand form, the absorbed IT
  demand package carries the same content.

## Human gate and AI-agent notes

- **Agent may:** ask for and read every input and attachment, register it, create the change with OpenSpec's skills in the OD store, draft the annex from the front-end results, run `scripts/check_handover.py`, list open fields and who supplies them.
- **Roles decide:** the OD lead for the Lane 3 front-end sends the package; IT or the external developer accepts it; Cyber Security signs off; the approvers of the capital request approve the money. The agent never sends a package and never marks an acceptance as given.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/new_handover.py` | Add the OD annex and `attachments/` to a change OpenSpec created; never overwrites | `<path-to-openspec/changes/<change-id>> [--with-config]` |
| `scripts/check_handover.py` | Run `openspec validate --strict` on the change, then check the annex, attachments and blocking fields | `<path-to-openspec/changes/<change-id>> [--json]` |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## Example

Fictional example; the change id and the output are made up for illustration.

```text
$ openspec new change add-downtime-reason-capture --store od-handover   # then openspec-propose fills it
$ python3 scripts/new_handover.py ~/openspec/od-handover/openspec/changes/add-downtime-reason-capture --with-config
$ python3 scripts/check_handover.py ~/openspec/od-handover/openspec/changes/add-downtime-reason-capture
ERROR handover.md: blocking section "Cyber Security inputs" still has a placeholder
NOT READY (1 error)   -> exit 1; fix, re-run until it reports READY
```

If the check fails, fix the named file and run it again; the package is sent only when it reports READY.

## Do not

- Do not send a package that fails the check, or one with a blocking field ⟨open⟩.
- Do not write or reformat OpenSpec files by hand or from other templates; OpenSpec's skills and CLI write them.
- Do not edit the copy under `references/openspec/`; refresh it from the pinned release.
- Do not put implementation choices into specs; requirements describe observable behaviour.
- Do not invent a figure, a date, a threshold, an owner or an IT field; mark it ⟨…⟩ and name who supplies it.
- Do not promise a delivery date; only a committed sprint or PI does that.
- Do not treat "sent" as "accepted"; ownership moves only on formal acceptance.
- Do not hand over a demand whose growth boundaries are not written down.

## Templates and the worked example

| File | Kind |
|---|---|
| [`assets/example/openspec/changes/add-downtime-reason-capture/.openspec.yaml.example`](assets/example/openspec/changes/add-downtime-reason-capture/.openspec.yaml.example) | Worked example (file of the example change) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/attachments/downtime-export-sample.csv.example`](assets/example/openspec/changes/add-downtime-reason-capture/attachments/downtime-export-sample.csv.example) | Worked example (a registered attachment) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/design.md.example`](assets/example/openspec/changes/add-downtime-reason-capture/design.md.example) | Worked example (file of the example change) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/handover.md.example`](assets/example/openspec/changes/add-downtime-reason-capture/handover.md.example) | Worked example (file of the example change) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/proposal.md.example`](assets/example/openspec/changes/add-downtime-reason-capture/proposal.md.example) | Worked example (file of the example change) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/specs/downtime-reason-capture/spec.md.example`](assets/example/openspec/changes/add-downtime-reason-capture/specs/downtime-reason-capture/spec.md.example) | Worked example (file of the example change) |
| [`assets/example/openspec/changes/add-downtime-reason-capture/tasks.md.example`](assets/example/openspec/changes/add-downtime-reason-capture/tasks.md.example) | Worked example (file of the example change) |
| [`assets/openspec/change/handover.md.tmpl`](assets/openspec/change/handover.md.tmpl) | Template |
| [`assets/openspec/config.yaml.tmpl`](assets/openspec/config.yaml.tmpl) | Template |
