---
name: od-template-resolution
description: >-
  Resolve which approved master template or standard a deliverable must start from, before
  anyone writes it - look the artefact up in the department's resource register, name its
  owner, location and verification state, and say plainly when the master is still "to collect"
  or "to confirm" so that nobody builds from an ad-hoc copy. Use when a plant or OD person is
  about to produce a use-case one-pager, business case, requirement specification, signal
  report, acceptance protocol, handover record, scorecard update or outreach deck, when two
  copies of a "template" circulate, or when a skill asks which template to fill.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-template-resolution
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Lane 1a (1a2), Spine"
  new_state_step: "Apply the standard template (self-service); Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only; points to the approved master
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-decision-routing, od-requirements-breakdown, od-benefit-calculation, od-scorecard-reporting, od-handover-and-adoption]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/15-resources.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/tasks.md
    - Department knowledge base, folder Master-Slide-Templates (one pptx file name only, not opened), read 2026-11-05
    - Skills od-benefit-calculation, od-requirements-breakdown, od-scorecard-reporting, od-handover-and-adoption, od-acceptance-test and od-signal-standardization, their assets folders listed 2026-11-05
  okf:
    type: Agent Skill
    title: Template resolution
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Template resolution

Read `od-context` first.

Plan item P-06 of the department's skill map: **every deliverable starts from the approved master
listed in the resource register, never from an ad-hoc copy.** The register (`15-resources.md`) says
its own reason: when an agent produces a deliverable "it must start from the approved template and
cite the canonical source, not invent one". This skill is the lookup that makes that rule usable at the
moment of need. It points; it never decides which template is approved.

## When to use it

- Before the first line of any artefact: use-case one-pager, business case, requirement spec,
  signal report, acceptance protocol, handover record, scorecard update, outreach or strategy deck.
- When a colleague sends "the template" as an attachment and you cannot say where the master lives.
- When another OD skill names an artefact and asks you to fill it (almost all of them do).
- Lane position: the Spine (all lanes), and Lane 1 step 2 where a plant applies a template to a catalogued
  use case.

## Definition of done

A resolution record ([`assets/template-resolution-record.md`](assets/template-resolution-record.md)) that states,
for one deliverable: the master chosen, its location, its owner, the register's verification date, and one of
four outcomes: **use the master**, **use the master and flag its age**, **the master is not collected yet:
stop and route**, or **no master exists: route to creation**.

## The references

| File | Use it for |
|---|---|
| [`references/master-register.md`](references/master-register.md) | The lookup: every template, standard and tool the resource register lists, with owner, state and the exact gap marker it carries, plus the templates that live inside skills and the knowledge base file not in the register |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Which template type each process step uses, the seven-step pipeline for a template-bound generated deliverable, residue and placeholder-leak checks, handoff contract, agent notes (types only, no locations) |
| [`assets/template-resolution-record.md`](assets/template-resolution-record.md) | The one-page output that travels with the deliverable |

## Procedure

1. **Name the deliverable and its lane.** One sentence: what artefact, for which lane or use case.
   If you cannot say, the work has not been scoped; hand back to `od-use-case-intake-triage` or
   `od-decision-routing`.
2. **Look it up** in [`master-register.md`](references/master-register.md), section A (register rows) first,
   then section B (templates produced inside skills), then section C (found in the knowledge base, not registered).
   Match on the register's own column *Applies to (lane / use case)*.
3. **Read the state of the row**, not just its existence. A row can exist and still have no usable master:
   - `⟨... to confirm or create⟩` in the location column: **no master exists**. Do not improvise.
   - `⟨... to collect⟩`: the master exists somewhere but is not yet in the register. Stop, ask the owner.
   - A location and a version date: usable. Note the date; the register itself is reviewed quarterly, so a
     date older than one quarter at the time of use gets the flag "register row not re-verified".
4. **Open the master at the location given** (the SharePoint library or Power BI report named in the row),
   not a copy in an e-mail or a plant folder. If you cannot open it, you do not have it: say so, do not recreate it.
5. **Check the master is the master.** Compare the title and the version date with the register row. A copy that
   differs from the master is a fork; record it and tell the owner, do not merge it silently.
6. **Fill the record** and attach it to the deliverable. Cite the register row in the deliverable's source line.
   Before it leaves your hands, check that no placeholder text and no sample figure from the master remains
   (the leak check in `references/process-chain-practice.md`).
7. **If the outcome is "stop" or "route"**, write the one sentence that says who can supply the master (the owner
   column) and carry on only with the parts of the work that do not depend on it. Do not substitute a plausible
   structure; an empty section beats an invented one.

## Decision table

| Register state | Outcome | What you do |
|---|---|---|
| Location is a link and a version date is present | Use the master | Fill the record; cite the row |
| Location is a link, version date is old or missing | Use the master and flag its age | Fill the record; name the date; ask the owner (at the COP or directly) whether it still holds |
| Location says `to collect` | Master not collected: stop and route | Ask the named owner role; log it as an open item |
| Location says `to confirm or create` | No master: route to creation | Propose the gap to the owner role; produce a draft *clearly labelled as draft, not as the template* |
| Artefact is not in the register at all | Not registered | Check sections B and C; if still absent, tell the register owner, who is the OD lead role |
| Two files claim to be the master | Conflict | Do not pick; show both with dates to the owner; `od-decision-routing` for who resolves |

## Who is the owner

The register names owners as roles or as the OD lead; this skill uses roles only. Where a row has a role
(DBVE, IIAE, Engineering Standards, OESL IT Digital Platforms) that role is who you ask. Where the owner cell is itself
a gap marker, the OD lead role is the fallback question, but the register has no rule saying so:
⟨fallback owner for unowned rows, to confirm with the OD lead⟩.

## Output

The filled [`assets/template-resolution-record.md`](assets/template-resolution-record.md). It authorises nothing:
the skill is read-only, and the record is evidence that the master was looked up, not that the deliverable is approved.

## Kinds of gap to expect

These are patterns, not a status report. Whether a gap is open today is read from the register on the day.

- The use-case one-pager and business-case template has been a gap row (`to confirm or create`, owner role DBVE).
  While it is a gap, `od-benefit-calculation` and `od-use-case-definition` carry their own protocols and those are the
  best available, not the approved master.
- Locations of Power BI reports, the data platform portal and the IIoT Edge / MSB portal are often `to confirm` or
  `to collect`. Owner: IIAE for the platforms, DBVE / OD lead for the reports.
- The Cyber Security sign-off standard is a standard that belongs to another team; while it is `to collect`,
  `od-cybersec-gate` (planned) has no approved master to start from.
- The knowledge base can hold a master-slide file that the register does not list ([section C](references/master-register.md)):
  whether it is approved, and for which deliverable, is `to confirm` with the OD lead role.
- Register freshness: check the register's own verification date against the quarterly review cadence. See
  `od-context-freshness` (planned).

## Do not

- Do not copy last month's deliverable and call it the template. A finished deliverable is not a master; the register
  expressly excludes one-off outputs.
- Do not fill a gap row with a plausible template. The gap is information.
- Do not decide that a master is approved. Approval is the owner's; you report what the register says.
- Do not paste the master's content into a skill or a plant folder; point to the location.
