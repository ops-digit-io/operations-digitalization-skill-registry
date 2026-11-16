---
name: catalog-template
description: >-
  Find which approved master template or standard a deliverable must start from, before anyone writes it: look it up in the department's resource register, name its owner, location and verification state, and say plainly when the master is still "to collect" or "to confirm" so nobody builds from an ad-hoc copy. Use when someone is about to write a use-case one-pager, business case, requirement specification, signal report, acceptance protocol, handover record, scorecard update or outreach deck, when two copies of "the template" circulate, when a colleague mails a template and nobody knows where the master lives, or when a skill asks which template to fill. Read-only: it points to the master and never approves it. Not for filling the deliverable (the skill that owns it).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: catalog-template
  aliases: [od-template-resolution]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Lane 1a (1a2), Spine"
  new_state_step: "Apply the standard template (self-service); Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only; points to the approved master
  status: draft
  requires: [dept-context]
  composes: [dept-decision-rights, funnel-requirements, bc-build, metrics-scorecard, deploy-handover]
  okf:
    type: Agent Skill
    title: Template resolution
    tags: [all, practice, new-state, draft]
---

# Template resolution

## Purpose

- Every deliverable starts from the approved master listed in the department resource register (`15-resources.md`), never from an ad-hoc copy, because an invented structure drifts from the approved one and cannot be checked.
- This skill is the lookup that makes the rule usable at the moment of need: it points; it never decides which master is approved.
- Read `dept-context` first.

## Terms used here

- **Deliverable**: what is being produced (one-pager, business case, requirement spec, signal report, acceptance protocol, handover record, scorecard update, outreach or strategy deck).
- **Master**: the approved template or standard for a deliverable, as the register names it. Say "master" for the approved one; a copy that differs is a **fork**.
- **Resolution record**: the one-page output of this skill.

## When to use it

- Before the first line of any deliverable.
- When a colleague sends "the template" as an attachment and you cannot say where the master lives.
- When two copies of a "template" circulate.
- When another OD skill names a deliverable and asks you to fill it (almost all of them do).
- Lane position: the Spine (all lanes), and Lane 1 step 2 where a plant applies a template to a catalogued use case.

## Inputs and output

- Input: one sentence naming the deliverable and its lane or use case; read access to the register and the master's location.
- Output: the filled [`assets/template-resolution-record.md`](assets/template-resolution-record.md), attached to the deliverable.
- The record authorises nothing: it is evidence that the master was looked up, not that the deliverable is approved.
- Output contract: [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Procedure

1. **Name the deliverable and its lane.** One sentence: what deliverable, for which lane or use case. If you cannot say, the work has not been scoped; hand back to `dept-intake` or `dept-decision-rights`.
2. **Look it up** in `references/master-register.md`: section A (register rows) first, then B (templates produced inside skills), then C (found in the knowledge base, not registered). Match on the column *Applies to (lane / use case)*.
3. **Read the state of the row**, not just its existence, because a row can exist and still have no usable master (see the decision table).
   - `⟨... to confirm or create⟩` in the location column: **no master exists**. Do not improvise.
   - `⟨... to collect⟩`: the master exists somewhere but is not yet in the register. Stop, ask the owner.
   - A location and a version date: usable. The register is reviewed quarterly, so a date older than one quarter at the time of use gets the flag "register row not re-verified".
4. **Open the master at the location given** (the SharePoint library or Power BI report named in the row), not a copy in an e-mail or a plant folder.
   - If you cannot open it, you do not have it: say so, do not recreate it.
5. **Check the master is the master.** Compare title and version date with the register row. A copy that differs is a fork; record it and tell the owner, do not merge it silently.
6. **Fill the record** and attach it to the deliverable.
   - Cite the register row in the deliverable's source line.
   - Before it leaves your hands, run the leak check in `references/process-chain-practice.md`: no placeholder text and no sample figure from the master remains.
7. **If the outcome is "stop" or "route"**, write the one sentence that says who can supply the master (the owner column) and carry on only with the parts of the work that do not depend on it.
   - Do not substitute a plausible structure; an empty section beats an invented one.

## Decision table

| Register state | Outcome | What you do |
|---|---|---|
| Location is a link and a version date is present | Use the master | Fill the record; cite the row |
| Location is a link, version date is old or missing | Use the master and flag its age | Fill the record; name the date; ask the owner (at the COP or directly) whether it still holds |
| Location says `to collect` | Master not collected: stop and route | Ask the named owner role; log it as an open item |
| Location says `to confirm or create` | No master: route to creation | Propose the gap to the owner role; produce a draft *clearly labelled as draft, not as the template* |
| Deliverable is not in the register at all | Not registered | Check sections B and C; if still absent, tell the register owner, who is the OD lead role |
| Two files claim to be the master | Conflict | Do not pick; show both with dates to the owner; `dept-decision-rights` for who resolves |

## Who is the owner

- The register names owners as roles or as the OD lead; this skill uses roles only.
- Where a row has a role (DBVE, IIAE, Engineering Standards, OESL IT Digital Platforms), that role is who you ask.
- Where the owner cell is itself a gap marker, ask the OD lead role. The register has no rule for this: ⟨fallback owner for unowned rows, to confirm with the OD lead⟩.

## Example

```text
Request: "Write the business case for the scrap-reduction use case at plant Alpha" (fictional)
1 Deliverable: business case, Lane 2.
2 Register: section A row "use-case one-pager and business case", owner role DBVE.
3 State: location cell says "to confirm or create" -> no master exists.
Outcome: route to creation. Ask DBVE; carry on only with value evidence collection.
Draft produced is labelled "draft, not the template"; bc-build protocol used as best available.
Source line: none yet (no master). Record attached, outcome "route to creation".
```

## Pitfalls

- A finished earlier deliverable copied as "the template": it is not a master, the register excludes one-off outputs, and old figures leak in.
- A gap row filled with a plausible structure: the gap is information; hiding it means nobody creates the master.
- A master opened from an e-mail attachment: it may be a fork, so the register row is not what you used.
- Sample figures or placeholder text left from the master: the deliverable then quotes numbers nobody measured. Run the leak check.
- A row treated as usable because it exists: read the state marker and the version date, not just the name.
- A master declared approved by the agent: approval is the owner's; report only what the register says.

## Human gate and AI-agent notes

- Authority is read-only; the agent points to the master and does not approve it.
- Approval of a master belongs to the owner role; the register owner is the OD lead role.
- Where a master is missing, the agent proposes the gap to the owner role and labels any draft as a draft.
- Allowed tools: Read, Grep, Glob; nothing is written outside the record.

## Do not

- Do not copy last month's deliverable and call it the template.
- Do not fill a gap row with a plausible template.
- Do not decide that a master is approved.
- Do not paste the master's content into a skill or a plant folder; point to the location.

## Definition of done

- A resolution record states, for one deliverable: the master chosen, its location, its owner, the register's verification date, and one of four outcomes.
- The outcomes are: **use the master**, **use the master and flag its age**, **the master is not collected yet: stop and route**, or **no master exists: route to creation**.
- The register row is cited in the deliverable and the leak check is done.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/master-register.md`](references/master-register.md) | Step 2 to 3: the lookup, owners, state markers, templates inside skills, the knowledge base file not in the register |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Step 6: which template type each process step uses, the seven-step pipeline, residue and placeholder-leak checks, handoff contract |
| [`assets/template-resolution-record.md`](assets/template-resolution-record.md) | Step 6: the one-page record that travels with the deliverable |
| [`references/background.md`](references/background.md) | You need context, the gap patterns to expect, or rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
