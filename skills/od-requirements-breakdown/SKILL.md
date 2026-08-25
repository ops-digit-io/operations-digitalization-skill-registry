---
name: od-requirements-breakdown
description: >-
  Turn an accepted demand into a requirement another lane can act on, for any of the four OD
  service lines. Elicits the problem behind the stated request, sets it against the
  capability's standard baseline, names the signals it needs and whether they exist, writes
  testable acceptance criteria, assesses the legacy MF IT systems it touches, and produces
  the handover packet that crosses a lane boundary. Use after intake accepts a demand and
  before anything is built — when scoping a use case for integration, specifying a machine or
  its signals, baselining a project, or scoping an analytical request.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-requirements-breakdown
  tier: practice
  lane: all
  scope: od
  origin: derived
  owner_role: Digital-Business-Value-Engineer (DBVE) or IIoT Interface & Automation Engineer (IIAE), per lane
  authority_level: draft the requirement; accept or refuse per intake; approvals are human
  status: stable
  last_verified: 2026-08-25
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-use-case-definition, od-data-availability-check, od-signal-standardization, od-use-case-standardization, od-benefit-calculation, od-machine-integration-guidance, od-acceptance-test, od-handover-and-adoption]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md (UC-03, P-04)
    - ops-knowledge-graph/.../20-lanes/*/playbook.md (step 3 in each lane)
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv (650 use cases; field population, target_text and blockers grammar; 268 legacy applications)
    - ops-knowledge-graph/_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase.md
    - ops-knowledge-graph/.../00-core/{05-intake,15-resources}.md
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

| Heading already in use | Use cases carrying it |
|---|--:|
| `Use Case Target Overview` | 99 |
| `Major Issue` / `Key Problem` | 44 |
| `Tags of Interest` | 29 |
| `Acceptance criteria` | 13 |
| `Traces to` | 13 |
| `Major` / `Minor Blocking Points` | 162 |

The estate knows what a requirement looks like. **It writes one about one use case in eight.**
The job is to make that the default.

## The references

| File | Use it for |
|---|---|
| [`references/requirement-template.md`](references/requirement-template.md) | The ten core sections and the four lane variants, with what each is for and how it fails |
| [`references/elicitation.md`](references/elicitation.md) | The question rounds that get the problem out, and the five judgement calls that make this hard |
| [`references/legacy-system-assessment.md`](references/legacy-system-assessment.md) | The other half of the output — checking 268 legacy applications and the lean-footprint fit |
| [`assets/requirement-template.md`](assets/requirement-template.md) | The blank to copy |
| [`scripts/check_requirement.py`](scripts/check_requirement.py) | Completeness check before handover |

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
[`legacy-system-assessment.md`](references/legacy-system-assessment.md).

**7 · Classify the blockers.** Two of the six classes — *method undefined* and *parameter
selection open* — are **the requirement's own work**, not something to escalate.

**8 · Value it honestly.** A figure carries `CALCULATION`, `ESTIMATION`, or *not yet
assessed* → `od-benefit-calculation`.

**9 · Check it.**

```bash
python3 scripts/check_requirement.py MyRequirement.md --lane use-case
```

Exit **2** on blockers, **1** on warnings, **0** ready. It catches a problem statement that
names a technology, prose acceptance criteria, a figure without a reliability label, an
unverified signal list, a target with no consuming moment, and a missing lane section.

**10 · Hand over.** The lane variant is what the receiving side consumes.

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
3. **Standard or genuinely specific?** Two thirds of the portfolio is declared standard at
   intake, and that declaration is the hinge the whole function turns on.
4. **Is the missing thing a signal or a decision?** *"Selection of process parameter to be
   connected"* is a real recorded blocker — and it is the requirement's job, not engineering's.
5. **Is it worth doing at all?** Fail it here, cheaply, rather than at the business case.

## Refusal is a finished outcome

No roadmap link and no nameable business case · needs a system outside the lean footprint ·
owned by a sibling function · a one-off with no recurring value · already exists elsewhere.

**Refuse with a named route and a written reason.** A refusal is a better outcome than a thin
requirement: the thin one consumes an integration slot and then stalls. Some of the 229 `IDEA`
use cases are refusals nobody wrote down.

## Definition of done

Sections 1–6 and 10 complete, the lane variant present, every signal carrying an existence
verdict, acceptance criteria testable with one adoption criterion, blockers classified with
owners, the legacy assessment done, the value labelled, and `check_requirement.py` reporting
zero blockers. Then the receiving lane accepts it — or says what is missing.

## Do not

- **Do not write the solution.** This says what must be true, not which nodes to wire.
- **Do not assume a signal exists.** Verify it; the corpus is full of blockers that are
  assumptions found out late.
- **Do not invent a figure** to make the case look decided. *Not yet assessed* is honest.
- **Do not skip the library check.** Rebuilding what another plant has is the failure the
  whole standardization effort exists to prevent.
- **Do not hand over without the lane variant.** It is the only part the receiver acts on.
