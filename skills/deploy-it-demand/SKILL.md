---
name: deploy-it-demand
description: >-
  OD part of the IT demand, which follows OpenSpec (step 3a4): collect every input, add the OD annex, check and hand over. Not for writing the OpenSpec change (OpenSpec's skills) or requirements.
license: MIT
metadata:
  id: deploy-it-demand
  aliases: [it-demand-package]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-3
  new_state_lane: "Lane 3a, step 3a4 (routes 3a.3, 3a.4): sub-steps 3a4.1 and 3a4.3 of the OpenSpec process"
  new_state_step: "3a.3 New codebase (external dev); 3a.4 Integrate a foreign app; front-end step 3 hand off once demand is clear"
  department_names: ["deploy-it-demand"]
  owner_role: OD lead for the Lane 3 front-end; IIAE for connector demands
  tags: [lane-3, handover, openspec, it-alignment, practice]
  authority_level: draft the package and run its checks; IT or the external developer accepts it; submission, approval and the ownership transfer are human
  status: draft
  requires: [dept-context]
  composes: [funnel-requirements, invest-screen, bc-build, bc-cost, bc-capital-request, dept-decision-rights, deploy-cybersec, deploy-acceptance, deploy-handover, deploy-appstore, mi-data-availability, mi-signals]
  okf:
    type: Agent Skill
    title: IT handover
    tags: [lane-3, handover, openspec, it-alignment, practice]
---
# IT handover

Read `dept-context` first.

OD's value in Lane 3 sits in the span **requirements → decision gate → clear demand**; execution after
handover is IT's or the external developer's (department Lane 3 file). This skill is the last link of that
span: it turns a clear demand into an **OpenSpec change** that IT can review, build from and archive like
code, and attaches the OD handover annex with the inputs IT named on 2026-09-11. It replaces the
Project Support & Application Consultancy lane's "handover" and the earlier `deploy-it-demand`.

**Why OpenSpec.** IT asked for one consolidated set of artefacts from the requirements funnel and a place
to store and exchange them (action item 2, IT). OpenSpec is a public, plain-markdown format for
exactly that: a change folder with `proposal.md`, delta `specs/`, `design.md` and `tasks.md`, versioned
in Git and reviewed in a pull request, checked by `openspec validate`. A package IT can open with its own
tooling is a cleaner handover than a slide deck.

## Purpose

The IT demand follows the OpenSpec process, modelled as the sub-steps of step 3a4 *Package / build* in the process
flow (`docs/new-state/process.yaml`): explore, propose, validate and hand over (OD), then apply, verify and archive (IT).
OpenSpec's own skills do every OpenSpec stage. This skill carries only what OpenSpec has no place for: every input the
user brings, the OD annex IT asked for, OD's context and rules for the store, and the check before hand-over. It also
carries the OpenSpec copy the stages use ([`references/openspec/VENDORED.md`](references/openspec/VENDORED.md)).
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the front-end results (requirement with growth boundaries, gate verdict and route, business case and
  investment estimate, approval route), plus every file or note the user adds: PDF, Excel, images, slides, mails,
  exports, links.
- **Out:** the OD part of the change in the OD store: `attachments/` with the register, `handover.md` (the annex), OD's
  `config.yaml`, and the check output. The OpenSpec files are written by OpenSpec's skills in sub-step 3a4.2.

## The rule it serves

**Hand off only once the demand is clear.** An under-specified demand stays in the front-end; it is never
pushed to IT or an external developer (department Lane 3, error paths). "Clear" is tested, not felt: the
package passes `scripts/check_handover.py` with no errors and no open blocking field.

## Where the flow puts it: the OpenSpec process in step 3a4

Routes 3a.3 (external build) and 3a.4 (integrate a foreign app) run step 3a4 as six sub-steps. OD acts on the first
three, IT or the external developer on the last three. The OpenSpec skills are carried unchanged in this skill.

| Sub-step | Who | OpenSpec skill | This skill's part |
|---|---|---|---|
| 3a4.1 Explore + collect inputs | OD | [`openspec-explore`](references/openspec/skills/openspec-explore/SKILL.md) | Procedure steps 1 to 3: inputs, front-end check, store |
| 3a4.2 Propose the change | OD | [`openspec-propose`](references/openspec/skills/openspec-propose/SKILL.md), or [`openspec-new-change`](references/openspec/skills/openspec-new-change/SKILL.md) + [`openspec-continue-change`](references/openspec/skills/openspec-continue-change/SKILL.md), [`openspec-ff-change`](references/openspec/skills/openspec-ff-change/SKILL.md) | None: OpenSpec writes proposal, specs, design and tasks with OD's rules |
| 3a4.3 Validate + hand over | OD | [`openspec-update-change`](references/openspec/skills/openspec-update-change/SKILL.md) for fixes | Procedure steps 4 to 6: annex, check, hand-over |
| 3a4.4 Apply | IT / Ext | [`openspec-apply-change`](references/openspec/skills/openspec-apply-change/SKILL.md) | None |
| 3a4.5 Verify | IT / Ext | [`openspec-verify-change`](references/openspec/skills/openspec-verify-change/SKILL.md) | None |
| 3a4.6 Archive + sync specs | IT | [`openspec-archive-change`](references/openspec/skills/openspec-archive-change/SKILL.md), [`openspec-bulk-archive-change`](references/openspec/skills/openspec-bulk-archive-change/SKILL.md), [`openspec-sync-specs`](references/openspec/skills/openspec-sync-specs/SKILL.md) | None; ownership moves on formal acceptance (`deploy-handover`) |

[`openspec-onboard`](references/openspec/skills/openspec-onboard/SKILL.md) teaches the workflow once. Without the
OpenSpec CLI (Claude Cowork), run these skills as described in
[`references/openspec-without-cli.md`](references/openspec-without-cli.md).

## The references

| File | Use it for |
|---|---|
| [`references/openspec-format.md`](references/openspec-format.md) | The OpenSpec rules this package must meet, and which OD skill fills which artefact |
| [`references/openspec-without-cli.md`](references/openspec-without-cli.md) | Running OpenSpec's skills with no OpenSpec CLI (Claude Cowork): each CLI command they call and its replacement |
| [`scripts/openspec_offline.py`](scripts/openspec_offline.py) | `new change`, `instructions` and `status` without the CLI, from the OpenSpec copy in this skill |
| [`references/input-intake.md`](references/input-intake.md) | How to collect every input, including the user's own files (PDF, Excel, images, slides, mails), read each by type, register it and trace it |
| [`references/it-expected-inputs.md`](references/it-expected-inputs.md) | What IT asked OD for on 2026-09-11, item by item, with the open IT actions that will firm each one |
| [`references/openspec/VENDORED.md`](references/openspec/VENDORED.md) | OpenSpec 1.17.0 as its authors ship it: the agent skills (`openspec-propose`, `openspec-new-change`, `openspec-continue-change`, `openspec-apply-change`, ...), the spec-driven schema and templates, the docs including the store guide. Unchanged; this skill follows them |
| [`assets/openspec/config.yaml.tmpl`](assets/openspec/config.yaml.tmpl) | OD's project context and per-artifact rules for the OD store; OpenSpec hands them to its skills through `openspec instructions` |
| [`assets/openspec/change/handover.md.tmpl`](assets/openspec/change/handover.md.tmpl) | The OD annex, the one file OD adds to an OpenSpec change |
| `assets/example/` | An illustrative package (`*.example`; drop the suffix to use it) that passes this check and OpenSpec's own validator in strict mode; no figures |
| [`scripts/new_handover.py`](scripts/new_handover.py) | Add the OD annex and `attachments/` to a change OpenSpec created |
| [`scripts/check_handover.py`](scripts/check_handover.py) | Run the OpenSpec CLI in strict mode on a package, then check the annex's blocking fields |
| [`references/it-demand-package/procedure.md`](references/it-demand-package/procedure.md) | Absorbed: the IT demand management package for the evaluation board (formerly `deploy-it-demand`) |
| [`references/od-project-support-consultancy/procedure.md`](references/od-project-support-consultancy/procedure.md) | Absorbed: the retired Project Support & Application Consultancy lane, kept for its composed protocols |

## Procedure

The OD part, by sub-step. Hand off only once the demand is clear.

**3a4.1 Explore + collect inputs**
1. **Collect every input first** ([`references/input-intake.md`](references/input-intake.md)). Show the user the twelve
   expected inputs as a checklist and ask for each gap; invite any further material in any form (PDF, Excel or CSV,
   Word or slides, images and screenshots, mails, exports, links) until the user says there is nothing else. Read every
   file by its type and ask who may see it. Use [`openspec-explore`](references/openspec/skills/openspec-explore/SKILL.md)
   when the demand itself is still unclear.
2. **Check the front-end is complete.** Requirement with growth boundaries (`funnel-requirements`), gate verdict and
   route (`invest-screen`, verdict Go or PoC-first), business case and investment estimate (`bc-build`, `bc-cost`),
   approval route (`bc-capital-request`, `dept-decision-rights`). If a part is missing, name it and stop.
3. **Open the OD store.** A folder (Git repository) with `openspec/`; OD's context and rules sit in its
   `openspec/config.yaml` ([`assets/openspec/config.yaml.tmpl`](assets/openspec/config.yaml.tmpl)). Start the change
   with `python3 scripts/openspec_offline.py new <store> <change-id>` (or `openspec new change` where the CLI exists),
   then `python3 scripts/new_handover.py <store>/openspec/changes/<change-id> --with-config`, which adds `handover.md`
   and `attachments/` and writes OD's config where the store has only OpenSpec's default. Copy the user's files into
   `attachments/` and register each in section 14 of `handover.md`.

**3a4.2 Propose the change** is OpenSpec's: follow its skill (table above). Feed it the inputs and the front-end results;
which OD result feeds which artifact is in [`openspec-format.md`](references/openspec-format.md). Do not write the
OpenSpec files by hand.

**3a4.3 Validate + hand over**
4. **Fill the annex** (`handover.md`): every input IT asked for
   ([`references/it-expected-inputs.md`](references/it-expected-inputs.md)), the business case summary, the approval
   status, the ownership terms and the register of every input (section 14). Unknown stays ⟨…⟩ with who supplies it.
5. **Run the check**: `python3 scripts/check_handover.py <store>/openspec/changes/<change-id>`. It applies OpenSpec
   1.17.0's validation rules offline (and `openspec validate --strict` where the CLI is installed), then checks the
   annex, the attachments and the no-template rule. Fix through
   [`openspec-update-change`](references/openspec/skills/openspec-update-change/SKILL.md) until it reports READY.
6. **Hand over.** A human commits and pushes the change in the OD store and opens a pull request there; IT reads it
   from the store. For 3a.4 the absorbed IT demand package goes to the demand board as well. Record the demand as
   handed over, not accepted.

**3a4.4 to 3a4.6** are IT's, with OpenSpec's skills. Ownership moves only on formal acceptance (`deploy-handover`);
until then OD owns the demand. Do not pass a delivery date to the plant before a team has committed the work.

## Output

The OD part of `<od-store>/openspec/changes/<change-id>/`: `handover.md` and `attachments/` with the register, OD's
`config.yaml` in the store, and the check output. The OpenSpec files beside them are written by OpenSpec's skills.

## Definition of done

The check reports no errors; every blocking annex field is filled or the package is not sent; every file the user provided is
in `attachments/` and registered, read in full or carried as an open item; the route,
the approval status and the Cyber Security inputs are stated; a human has sent it; the demand record shows
"handed over, awaiting acceptance" with the receiving team named.

## Open - what only the OD lead and IT can supply

- ⟨The OD store: its id and repository URL⟩ - decided: OD drafts in its own OpenSpec store; the OD lead sets it
  up once (a Git repository with `openspec/`; no CLI needed) and names it here.
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
| `scripts/openspec_offline.py` | OpenSpec's `new change`, `instructions` and `status` without the CLI | `new <store> <change-id>` · `instructions <change> <artifact>` · `status <change>` |
| `scripts/check_handover.py` | OpenSpec's validation rules offline (plus `openspec validate --strict` where the CLI exists), then the annex, attachments and blocking fields | `<path-to-openspec/changes/<change-id>> [--json] [--require-cli]` |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## Example

Fictional example; the change id and the output are made up for illustration.

```text
$ python3 scripts/openspec_offline.py new ./od-store add-downtime-reason-capture   # then follow openspec-propose
$ python3 scripts/new_handover.py ./od-store/openspec/changes/add-downtime-reason-capture --with-config
$ python3 scripts/check_handover.py ./od-store/openspec/changes/add-downtime-reason-capture
NOTE    checked offline against OpenSpec 1.17.0's rules (no OpenSpec CLI here; none needed)
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
