---
name: od-requirements-breakdown
description: >-
  Turn an accepted demand into a requirement another lane can act on, for any of the four OD
  service lines. Elicits the problem behind the stated request, sets it against the
  capability's standard baseline, names the signals it needs and whether they exist, writes
  testable acceptance criteria, assesses the legacy MF IT systems it touches, and produces
  both the handover packet that crosses a lane boundary and a standardized epic with its
  user stories and a background description of what it is used for. Use after intake accepts a
  demand and before anything is built — when scoping a use case for integration, specifying a machine or
  its signals, baselining a project, or scoping an analytical request.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob Bash(python3 scripts/check_epic.py:*) Bash(python3 scripts/check_requirement.py:*)
metadata:
  id: od-requirements-breakdown
  tier: practice
  lane: all
  scope: od
  origin: derived
  owner_role: Digital-Business-Value-Engineer (DBVE) or IIoT Interface & Automation Engineer (IIAE), per lane
  authority_level: draft the requirement; accept or refuse per intake; approvals are human
  status: stable
  sources_read: 2026-08-25
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-system-fit-check, od-use-case-definition, od-data-availability-check, od-signal-standardization, od-use-case-standardization, od-benefit-calculation, od-equipment-integration, od-acceptance-test, od-handover-and-adoption]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md (UC-03, P-04)
    - ops-knowledge-graph/.../20-lanes/*/playbook.md (step 3 in each lane)
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv (use case field population, target_text and blockers grammar; legacy applications)
    - ops-knowledge-graph/_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase.md
    - ops-knowledge-graph/.../00-core/{05-intake,15-resources}.md
  okf:
    type: Agent Skill
    title: Requirements breakdown
    tags: [all, od, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Requirements breakdown

Read `od-context` first. Run **after** `od-use-case-intake-triage` has accepted the demand.

This is the artefact that crosses a lane boundary. The department's own skill map calls it
*"the handover artefact between lane 1 and lane 2, the step most dependent on tacit
judgement, and the one currently held by a departing individual."* That is what this skill
is for: making the judgement explicit enough to be run by somebody else.

## The template is already yours

**This does not introduce a new form.** The best-documented use cases in the portfolio
already use these headings, inside their `target_text` and `blockers` fields:

| Heading already in use | How common it is |
|---|---|
| `Use Case Target Overview` | The most widely used of these headings |
| `Major Issue` / `Key Problem` | Used by a minority |
| `Tags of Interest` | Used by a minority |
| `Acceptance criteria` | Rare |
| `Traces to` | Rare |
| `Major` / `Minor Blocking Points` | Used in many records |

The estate knows what a requirement looks like. **It writes one about only a small fraction of
its use cases.** The job is to make that the default. (To measure it, count the headings in the
live `target_text` and `blockers` fields and quote the export date.)

## The references

| File | Use it for |
|---|---|
| [`references/requirement-template.md`](references/requirement-template.md) | The ten core sections and the four lane variants, with what each is for and how it fails |
| [`references/elicitation.md`](references/elicitation.md) | The question rounds that get the problem out, and the five judgement calls that make this hard |
| [`references/legacy-system-assessment.md`](references/legacy-system-assessment.md) | The other half of the output — checking the legacy applications and the lean-footprint fit |
| [`references/epic-and-user-stories.md`](references/epic-and-user-stories.md) | The second output — the background description, which epic axis to use, how to cut stories, and what makes acceptance testable |
| [`assets/requirement-template.md`](assets/requirement-template.md) | The blank requirement to copy |
| [`assets/epic-and-stories.md`](assets/epic-and-stories.md) | The blank epic to copy |
| [`assets/epic-and-stories.example.md`](assets/epic-and-stories.example.md) | A worked epic that passes every check — read this before the blank |
| [`scripts/check_requirement.py`](scripts/check_requirement.py) | Completeness check before handover |
| [`scripts/check_epic.py`](scripts/check_epic.py) | Check the epic and its stories before they enter a backlog |

## The procedure

**1 · Elicit the problem, not the solution.** Five rounds in
[`elicitation.md`](references/elicitation.md), ordered to get the fields people otherwise
never fill. *If the stated problem names a technology, it is a solution — ask again.*

**2 · Check the library before specifying.** If another plant has built this, the requirement
is an **adoption**, not a build → `od-use-case-standardization`. Adoption is what the
department is short of, not templates.

**3 · Set the standard baseline.** Take the cluster's KPI set and requirements checklist as
the default, and record only this plant's deltas. Check whether a public data model already
defines the signals — `od-signal-standardization`.

**4 · Name the signals, and verify them.** Canonical names, direction in/out, and an
existence verdict per signal from `od-data-availability-check` — **verified, not assumed**.
An `out` signal must be registered on the edge platform before anything publishes to it.

**5 · Write testable acceptance criteria**, including one that requires use in a real shift
by a named plant role. That is the department's own handover rule.

**6 · Assess the legacy systems and the footprint** →
[`legacy-system-assessment.md`](references/legacy-system-assessment.md). If the spec implies
more than the lightweight tools cover (cross-process scheduling, full order genealogy, a
heavier read on image/recipe/energy data than their own boundary) → `od-system-fit-check`,
before the spec is written any further around the heavier assumption.

**7 · Classify the blockers.** Two of the six classes — *method undefined* and *parameter
selection open* — are **the requirement's own work**, not something to escalate.

**8 · Value it honestly.** A figure carries `CALCULATION`, `ESTIMATION`, or *not yet
assessed* → `od-benefit-calculation`.

**9 · Cut it into an epic and its stories** →
[`epic-and-user-stories.md`](references/epic-and-user-stories.md). One epic, **at least two**
stories, and a background description saying what it is used for. Cut by moment and role, or
by which signals exist today — **never by technical layer**.

**10 · Check both.**

```bash
python3 scripts/check_requirement.py MyRequirement.md --lane use-case
python3 scripts/check_epic.py MyEpic.md
```

Exit **2** on blockers, **1** on warnings, **0** ready. Between them they catch a problem
statement that names a technology, prose acceptance criteria, a figure without a reliability
label, an unverified signal list, a missing lane section, a placeholder role, a "so that" made
only of generic benefit words, an epic with one story, and a story with no use-in-a-real-shift
criterion.

**11 · Hand over.** The lane variant is what the receiving side consumes; the epic is what
enters the backlog.

## The second output: one epic, many stories, and a background

The requirement says what must be true. The **epic** says how the work is cut up so somebody
can start on Monday. Every requirement produces exactly one, and it always carries:

| Part | Rule |
|---|---|
| **Background — what this is used for** | Prose. What happens today with the role and the hour named, the moment the output gets used, the decision it changes, why now, and what it is *not* for. This is the part that survives the person who asked leaving |
| **Epic statement** | As ⟨named role⟩, we want ⟨capability⟩, so that ⟨outcome particular to this plant⟩ |
| **Both epic axes** | The capability epic *and* the process epic — the source data shows many leaves carrying only one of the two, so a query on either axis misses part of the portfolio |
| **At least two user stories** | Each with its own background, signals carrying an existence verdict, Given/When/Then acceptance including one use-in-a-real-shift criterion, blockers, and dependencies |
| **Epic acceptance** | What is only true across the whole epic — or "all stories accepted", if that is honestly the case |

### This structure already exists, and it is hollow

The use case list encodes the hierarchy in its own fields — process epics, capability
epics and leaf stories. What is typically in the leaves:

| Of the leaf stories | Pattern |
|---|---|
| Carry an **"I want"** tag | Few do — the rest render as *"I want (not tagged)"* |
| Mention **acceptance criteria** | Almost none |
| Carry a **"so that"** that differs from the generated one | None |

Every generated story ends with the same sentence: *"…so that the process gains transparency, faster reaction
and less manual effort."* True of every use case ever written, which is what makes it useless.

**So the job is not to introduce the structure. It is to stop filling it with a sentence that
fits anything.** If your "so that" would read equally well on another plant's epic, it is the
generated one with new words — and `check_epic.py` will say so.

## The four lane variants

Same core, one added section each:

| Lane | Adds | Because its definition of done is |
|---|---|---|
| **Use Case Support** | **Handover packet to Information Integration** — machines, signals, expected data path, output points to register, the acceptance the integration must satisfy | "…handed to integration **with a business case**" |
| **Information Integration** | **Equipment requirement** — PLC identity, protocol, ingress variant, connector, **PLC program available?**, tag export, companion specification, Cyber Security sign-off | "Machine integrated, signals standardized, data landing on the data platform" |
| **Project Support** | **Project scope baseline** — stage/gate, investment and eCR route, milestones with acceptance points, resources, dependencies, **training and competence**, flow owner | "Managed to acceptance test; application consulted and accepted" |
| **Analytical Support** | **Request scope** — the question, the decision it supports, the data-availability verdict, turnaround, and **one-off or recurring** | "Process diagnostics / analytical insight delivered" |

**Nothing crosses a lane boundary without its variant.** An integration request with no signal
list and no acceptance criterion is a conversation, not a work item — and it will consume an
integration slot before anyone notices.

## Where each lane's requirement comes from

| Lane | Playbook step this serves |
|---|---|
| Use Case Support | Step 3 — *break down the customer/process requirement; assess (legacy) MF IT systems* |
| Information Integration | Step 1 — *equipment assessment*, feeding the PRS (Doc ID 215534) where a machine is purchased or modified |
| Project Support | Step 2 — *kick-off; scope and requirements* |
| Analytical Support | Step 1 — *request received and scoped* |

## The judgement this skill is trying to transfer

Five calls, in full in [`elicitation.md`](references/elicitation.md):

1. **One use case or three?** Different people, different moments → different use cases.
2. **Is the stated problem the real one?** Ask what they would do differently with the answer.
3. **Standard or genuinely specific?** Most of the portfolio is declared standard at
   intake, and that declaration is the hinge the whole function turns on.
4. **Is the missing thing a signal or a decision?** *"Selection of process parameter to be
   connected"* is a real recorded blocker — and it is the requirement's job, not engineering's.
5. **Is it worth doing at all?** Fail it here, cheaply, rather than at the business case.

## Refusal is a finished outcome

No roadmap link and no nameable business case · needs a system outside the lean footprint ·
owned by a sibling function · a one-off with no recurring value · already exists elsewhere.

**Refuse with a named route and a written reason.** A refusal is a better outcome than a thin
requirement: the thin one consumes an integration slot and then stalls. Some `IDEA`
use cases are refusals nobody wrote down.

## Definition of done

Sections 1–6 and 10 complete, the lane variant present, every signal carrying an existence
verdict, acceptance criteria testable with one adoption criterion, blockers classified with
owners, the legacy assessment done, the value labelled, and `check_requirement.py` reporting
zero blockers.

Plus the epic: a background covering all five prompts, both epic axes recorded, at least two
stories each with its own background and a use-in-a-real-shift criterion, and `check_epic.py`
reporting zero blockers. Then the receiving lane accepts it — or says what is missing.

## Do not

- **Do not write the solution.** This says what must be true, not which nodes to wire.
- **Do not assume a signal exists.** Verify it; the corpus is full of blockers that are
  assumptions found out late.
- **Do not invent a figure** to make the case look decided. *Not yet assessed* is honest.
- **Do not skip the library check.** Rebuilding what another plant has is the failure the
  whole standardization effort exists to prevent.
- **Do not hand over without the lane variant.** It is the only part the receiver acts on.
- **Do not write "so that the process gains transparency."** That clause is already generated on
  every story in the estate and has never once told anybody anything.
- **Do not cut stories by technical layer.** *Connect the PLC · build the flow · build the
  dashboard* are tasks: none is usable alone, so none can be accepted.
- **Do not call one story an epic.** If it will not split, it is a story — say so and move on.
