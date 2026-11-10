---
type: Skill Reference
title: Requirements funnel
description: "The department's requirements funnel (funnel-requirements): from a vague idea to framed problems and candidate requirements, with a human gate and a handoff file."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [requirements, funnel, department-package]
derived_from:
  - "Department knowledge base, OD Department Knowledge/OD-instance/30-skills/product-funnel-skills.zip/skills/requirements-funnel/SKILL.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `product-funnel-skills.zip/skills/requirements-funnel/SKILL.md` (the master).

# Requirements Funnel

Turn an idea into a defensible set of candidate features through dialogue.

This skill owns the **front half** of the pipeline. It ends by producing a
handoff artifact that the `feature-funnel` skill consumes for scoring and
release tiering. Do not score, rank, or assign versions here — that is the
next skill's job, and doing it early anchors the user on a number before the
requirement is understood.

<HARD-GATE>
Do NOT write code, scaffold a project, design a schema, or produce an
architecture until the funnel has completed Stage 4 and the user has approved
the candidate feature set. If the user asks for implementation mid-funnel, say
which stage you are at, offer to finish or to skip deliberately, and let them
choose. Never skip silently.
</HARD-GATE>

## Core Principle

**Prioritize problems, not solutions.** A user asking for a feature has already
performed an unexamined design step. Your job is to recover the problem behind
it, because a different feature often solves it better and cheaper. When the
user names a feature, ask what breaks without it.

## The Single-Stakeholder Adaptation

Classical requirements methods assume many stakeholders to interview and
customers to survey. This funnel usually runs with exactly one person — the
user — talking to Claude. That changes two things:

- **You are the elicitation instrument.** There are no interview transcripts to
  synthesize. Your questions are the only source of requirements, so question
  quality *is* requirement quality.
- **Importance and satisfaction are expert estimates, not survey data.** The
  user is a domain expert standing in for the eventual users. Record their
  estimates as estimates. Flag anything resting on a guess about a user group
  the user has not actually spoken to — that flag becomes a `confidence`
  penalty downstream.

## Stage 0 — Pick the Entry

Ask which of these the user has, and say which you are running:

| They have | Mode | Start at |
|-----------|------|----------|
| An idea for something new | **Greenfield** | Stage 1 |
| A process that already happens today | **As-is** | Stage 0.5, then Stage 1 |

Default to asking. Most business software replaces a process rather than
inventing one, and users often describe a solution when they have a process —
"I want a layout tool" usually means "laying out cells today is painful". If
they describe how something is done today, unprompted, that is as-is mode.

## Stage 0.5 — Map the As-Is (as-is mode only)

Skip entirely in greenfield mode.

### Map the current process

Walk the steps end to end. For each: **who does it, what they use, how long it
takes, and what they hand to the next step.** Number them — you will refer back.

Then, per step, capture what it costs today:

- **Frequency** — how often the step runs
- **Duration** — how long it takes, including the waiting
- **Rework rate** — how often it gets redone, and why
- **Who is blocked** while it happens

<IMPORTANT>
These numbers are the **baseline**, and they are the single most valuable thing
this stage produces. Without them the eventual business case has nothing to
compare against, and its value claims collapse into assertion. Capture them here
even when they feel tedious, and mark each as measured or estimated — that
distinction carries all the way to the final deck.
</IMPORTANT>

Estimates are fine. "About two days, mostly waiting for the drawing" is a usable
baseline; "it takes a while" is not. Push once for a number, accept an
order of magnitude, and mark it estimated.

### Find where the time actually goes

Against the mapped steps, look for:

| Pattern | Question |
|---------|----------|
| **Waiting** | Which steps sit idle waiting for a person, an approval, or a file? |
| **Rework** | What gets done twice because it was wrong or unclear the first time? |
| **Re-entry** | Where is the same data typed into a second system? |
| **Handoffs** | Where does work change hands, and what gets lost there? |
| **Overproduction** | What is produced that nobody downstream uses? |
| **Expertise bottleneck** | Which steps only one person can do? |

The biggest number usually sits in waiting or rework, not in the step everyone
complains about. Say which step dominates and check the user agrees before
building on it.

### Propose a to-be process

Draft the future-state process at **MVP scale, not utopia**. Same step
numbering so the delta is legible. For each changed step say what happens
instead, and what the change is worth against the baseline.

Then state the delta explicitly: steps removed, steps automated, steps merged,
time saved per run, rework avoided. Present it and get agreement before
continuing — a to-be the user does not believe produces requirements for a
product nobody wants.

### Derive requirements from the delta

Now the important move: **the problems are the deltas, not the steps.** A step
that is unchanged between as-is and to-be generates no requirement, however
important the step is. Only what has to change becomes a problem statement, in
the same form Stage 2 uses.

Carry the baseline numbers forward into the handoff artifact. Stage 4 writes
them into a `baseline` block, and the `business-case` skill reads them at the
end of the chain.

## Four Stages

Announce the stage you are entering. Do not run them in one breath — each
stage ends with a check-in.

### Stage 1 — Frame

Establish the boundary before generating anything.

Ask, in one batch (not one at a time):

1. **Who is the primary actor?** The person whose job gets easier. If more than
   one, rank them; a funnel with two co-primary actors produces a bloated MVP.
2. **What is the outcome?** Finish the sentence: "This succeeds if _____ can
   now _____ in _____ instead of _____." Force the before/after.
3. **What is the trigger, and how often does it fire?** What happens right
   before someone opens this tool, and how many times a year. Get an order of
   magnitude even if it is a guess — weekly and twice-a-year are different
   products. Frequency sets how much setup and data entry a user will tolerate
   per use, and it is the Reach input if the next stage scores with RICE.
4. **What is explicitly out of scope?** Get at least two exclusions. If the
   user cannot name any, the scope is not yet real.
5. **What are the hard constraints?** Time, budget, tech, regulatory, existing
   systems it must sit alongside.

In as-is mode, most of this is already answered by Stage 0.5 — the actor is
whoever runs the process, the outcome is the delta you agreed. Confirm rather
than re-ask, and only chase what the process map did not settle.

Reflect the frame back in five lines and get a yes before continuing.

### Stage 2 — Elicit

Widen before narrowing. Work the input space systematically rather than taking
whatever the user volunteers first.

Walk these five lenses, and say which one you are on:

| Lens | Question to ask |
|------|-----------------|
| **Inputs** | What does the user hand the system? Format, volume, quality, who produces it |
| **Decisions** | What judgement is the system making on their behalf? This is where the real value hides |
| **Outputs** | What artifact leaves the system? Who consumes it and what do they do next |
| **Exceptions** | What is the messy case, the rush job, the incomplete input |
| **Environment** | Who else touches this, what does it integrate with, where does it run |

For each lens capture the *problem*, not the requested feature. Write findings
as: `As <actor>, when <situation>, I need <capability>, so that <outcome>.`

If the user supplied a feature list up front, run it backwards through this
table: for each stated feature, log the problem it implies, then continue the
lenses to find problems they did not cover. Stated features become evidence,
not requirements.

### Stage 3 — Decompose

Turn problems into candidate features. This is a fan-out step: expect 2–4
candidates per problem, including at least one deliberately cheap option.

For each problem, generate:

- **The obvious solution** — what the user probably had in mind
- **The cheap solution** — the 80% version, often manual or semi-automated
- **The strong solution** — what you would build with no constraints

The cheap option matters most. It is usually the MVP candidate, and without it
the funnel produces a feature set where everything is expensive and nothing can
be cut.

**Cap the set at around 15 candidates.** Past that, scoring degrades: the tail
gets scored quickly and carelessly, which is worse than not scoring it, because
a careless number looks identical to a considered one in the table. If you are
over, merge near-duplicates and drop `strong` variants for problems where the
cheap option clearly wins — record them in the next stage's Won't list rather
than carrying them through scoring.

Split anything that bundles multiple capabilities. A candidate that reads "and"
in its description is two candidates. Downstream scoring is meaningless on
bundles, because a high-value half drags a low-value half into the MVP.

### Stage 4 — Converge

Before handing off:

- **Deduplicate.** Merge candidates that differ only in wording.
- **Mark dependencies.** `B requires A` — this constrains tiering later, since
  a high-scoring feature whose prerequisite scores low must still wait.
- **Surface assumptions.** For each candidate, what must be true for it to
  deliver value? Mark each assumption `validated` or `unvalidated`.
- **Name the riskiest assumption** across the whole set. The MVP's real job is
  usually to test this, and the next skill needs it called out.
- **Accept partial answers.** If the user skips questions, declines a lens, or
  says "just assume", record what is missing as an explicit gap and continue.
  Mark the affected problems `evidence: assumed` so the confidence penalty
  flows downstream automatically. Never stall the funnel waiting for complete
  information, and never quietly fill a gap with your own guess presented as
  theirs.
- **Check coverage.** Every problem from Stage 2 has at least one candidate;
  every candidate traces to a problem. Orphan candidates are scope creep —
  drop them or find their problem.

Present the set and get approval.

<HARD-GATE>
Then **write `requirements-funnel-output.md` before invoking `feature-funnel`**,
and confirm it exists. Do not carry the candidate set forward as chat text —
not as a table, not as a summary, not "since we just discussed it".

This is the gate that makes the chain a chain. Without the file, the next stage
depends on conversation history: it cannot run in a fresh session, the schema is
never exercised, and nothing downstream can be traced back to a stated problem.
Skipping it silently is the single most likely failure of this skill, precisely
because the conversation feels like sufficient context at the moment you skip it.
</HARD-GATE>

## Handoff Artifact

Write `requirements-funnel-output.md` with a YAML block the next skill reads.
Full field reference in `handoff-schema.md`.

In as-is mode the artifact also carries a `baseline` block. It is what makes the
final business case auditable rather than asserted — see the `business-case`
skill.

```yaml
baseline:                        # as-is mode only
  mode: as-is
  process: "Relayout of an assembly cell"
  runs_per_year: 20              # mark estimated vs measured
  steps:
    - n: 3
      name: "Draw options in CAD and compare by hand"
      owner: "ME engineer"
      duration_h: 16
      basis: estimated
      pain: "only one option gets drawn; comparison is by eye"
  totals:
    hours_per_run: 74
    rework_rate: "1 in 4 relayouts revised after install"
frame:
  actor: "Manufacturing engineer laying out a new assembly cell"
  outcome: "produce a costed cell layout in an afternoon instead of two weeks"
  out_of_scope: ["ERP integration", "shopfloor scheduling"]
  constraints: ["must accept existing CAD exports", "single user, offline"]
riskiest_assumption: "engineers will trust a generated layout enough to build from it"
problems:
  - id: P1
    statement: "As a manufacturing engineer, when I place machines by hand, I need to compare layout options quickly, so that I stop defaulting to the first workable one"
    evidence: stated
candidates:
  - id: F1
    problem: P1
    name: "Manual layout canvas with live travel-distance readout"
    variant: cheap
    depends_on: []
    assumptions:
      - text: "travel distance is the metric engineers actually optimise"
        status: unvalidated
```

## Red Flags

| Thought | Reality |
|---------|---------|
| "They described a process, so I'll design the software for it" | A process map is the as-is. Software for the as-is automates the waste. Propose a to-be first, then derive requirements from the delta. |
| "The baseline numbers are tedious, I'll get them later" | Later is after the prototype, when nobody can remember what the old way cost. The business case then has nothing to compare against. |
| "They gave me a feature list, so requirements are done" | A feature list is a set of answers with the questions missing. Run it backwards through Stage 2. |
| "I'll ask questions as I build" | Questions asked after building are rationalisations of what you already built. |
| "The scope is obvious to me" | Then Stage 1 costs you four minutes. If it is genuinely obvious the user will confirm fast. |
| "This candidate is clearly the MVP" | You do not know that yet — you have not weighted anything. Say it as a hypothesis, let scoring test it. |
| "One big feature covers three problems" | Bundles cannot be scored or cut. Split it. |
| "They said the users want X" | Did they ask the users? If not, mark it unvalidated and let confidence drop. |

## Chaining

- Runs **before**: `feature-funnel` (scoring and release tiering)
- Feeds: `business-case` at the end of the chain, via the `baseline` block
- Pairs with: a domain skill, if one exists for the user's field — load it
  during Stage 3 so candidate generation uses real domain vocabulary
- Related upstream: if the user has not decided *whether* to build at all, that
  is a strategy question, not a requirements one
