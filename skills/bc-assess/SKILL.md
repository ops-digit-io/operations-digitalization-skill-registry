---
name: bc-assess
description: >-
  Scores a drafted business case against the OD house rubric (C1-C5 core integrity, D1-D9 structure, E1-E6 discipline) and returns pass, partial or gap per criterion with evidence, a conflict register, ranked open questions and a maturity-gate verdict (ready to sign, sign the floor, not ready). Use when someone asks "is this business case signable", "review or score the case before the capital request", "does it pass the maturity gate", or wants two cases compared on one rubric. Recommends only; the approvers decide. Not for building the value model (bc-build), costs (bc-cost) or the request itself (bc-capital-request).
license: MIT
metadata:
  id: bc-assess
  aliases: [bc-assessment]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (24), Lane 3 front-end (33)"
  new_state_step: "Business case (value and cost), assessment, ranking; Business case, prioritization, capital request"
  department_names: ["bc-assess", "bc-assess", "business-case-assessor"]
  owner_role: OD lead (separation of duties - not the person who built the case)
  tags: [department-core, lane-2, lane-3]
  authority_level: recommend - scores and gives a verdict; the approvers decide
  status: ready
  requires: [dept-context]
  composes: [bc-build, bc-cost, bc-capital-request]
  okf:
    type: Agent Skill
    title: Business case assessment
    tags: [department-core, lane-2, lane-3]
---
# Business case assessment

- Read `dept-context` first.
- The department's `bc-assess`: it scores a case, it does not build one.
- Governance stays separate from build, because a builder who scores their own case lets unsupported figures reach the approvers.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Scores a business case against the OD house rubric and gives a maturity-gate verdict.
- Use it when a case is drafted and before a capital request, when a reviewer asks whether a case is signable, or when two cases must be compared on the same rubric.

## Inputs and output

- **Inputs:** the value backbone `business-case.md` (`bc-build`, `business-case-backbone.md`), the investment estimate (`bc-cost`), the raw inputs of the case (transcripts, mockups, reference drafts, cross-checks), and if present the intake questionnaire [`assets/use-case-input-questionnaire.md`](assets/use-case-input-questionnaire.md) (sections A-L).
- **Output:** `bc-assessment-report.md` next to the case: scorecard (criterion, verdict, evidence, note), conflict register, maturity-gate verdict, ranked open questions. Optional: the one-pager deck (9 slides plus the provenance backup slide). All generated files in English.
- **Vocabulary:** criteria are scored pass, partial or gap. Only the gate verdict uses "Ready to sign", "Sign the floor, validate the upside" or "Not ready".

## The rubric ([`references/criteria-checklist.md`](references/criteria-checklist.md))

- Score every criterion **pass / partial / gap** with evidence (file and section).
- A gap on any C criterion blocks signing, because C1-C5 are what make a figure trustworthy at all.

| Group | Criteria |
|---|---|
| **C - core integrity** | C1 value-only separation (cost in the investment estimate, never netted) · C2 grounding tag on every figure · C3 expected and potential kept apart (`~ EXPECTED (min / potential)`) · C4 de-banking of big movers resting on an `[unknown]` · C5 auditable arithmetic (`value x driver`, hard floor derivable by hand) |
| **D - deck-renderable structure (D1-D9)** | D1 lever register (H hard, O optional IDs) · D2 contribution matrix min / expected / max with confidence · D3 sub-cases with effort to realize · D4 value vs. dependencies · D5 abstracted before / after · D6 SMART gated milestones M0-M4, dates after approval · D7 soft / strategic clusters kept qualitative · D8 ranked refinement questions with worked examples · D9 overall picture slide |
| **E - discipline** | E1 factual language · E2 tilde convention for estimated euros · E3 market value tagged `[market]` where input is missing · E4 baseline honesty (representative plant) · E5 per-plant value and rollout scope on separate axes · E6 neuwerk brand |

- OD x IT (2026-09-11) adds one check to C1: bankable vs. assumption-dependent stated apart, with investment envelope, minimum viable rollout, maximum scale-out and TCO.

## Procedure

1. **Assessor.** Confirm the case was built by someone else; if not, stop and ask the OD lead to name a different assessor.
2. **Read everything** - backbone, every input file, the questionnaire. Map which fact came from which file, because scoring from the summary alone misses figures that are not in the sources.
3. **Score** every criterion of the rubric with evidence. Start with C1-C5; a gap there already decides the verdict.
4. **Provenance and conflicts** ([`provenance-and-conflicts.md`](references/provenance-and-conflicts.md)): list every input, what the case drew from it, and every conflict between sources with how it was resolved and why.
5. **Verdict** (maturity gate), one of three:
   - **Ready to sign:** all C pass, expected floor grounded.
   - **Sign the floor, validate the upside:** C pass, a de-banked lever awaits its input.
   - **Not ready:** any C gap; name the missing input and its owner.
6. **Report** `bc-assessment-report.md`: scorecard, conflict register, verdict, ranked open questions (normalized influence 0-100, grouped into blocks one conversation can close). Pattern: [`worked-example-gemba.md`](references/worked-example-gemba.md).
7. **Pre-verdict check** (repeat until all hold):
   - [ ] Every criterion C1-C5, D1-D9, E1-E6 has a verdict.
   - [ ] Every verdict has evidence with file and section.
   - [ ] Every gap names the missing input and its owner.
   - [ ] Every input file appears in the conflict register.
   - [ ] The verdict line follows from the C scores.
8. **Deck (optional)** with `scripts/build_bc_short.py` - slide sequence in [`deck-spec.md`](references/deck-spec.md), run and QA loop in [`build-engine.md`](references/build-engine.md). Needs `python-pptx` and the neuwerk template (see Available Scripts).
9. Hand a signable case to `bc-capital-request` if money is needed; send an unsigned case back to `bc-build` with the findings.

## Human gate and AI-agent notes

- **Agent may:** read the case and its inputs, score the rubric with evidence, list conflicts, draft the report and the optional deck.
- **Roles decide:** the OD lead names the assessor (never the builder of the case); the approvers decide on the capital request. The verdict is a recommendation only.
- If an input file is missing or invalid, mark the criterion gap and name the input; do not guess.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/build_bc_short.py` | Build the optional one-pager deck. Needs `python-pptx` (`pip install python-pptx`) and the neuwerk template `_nw_template.pptx` (department packages `bc-assessment.zip` or `neuwerkbrand.zip`; not stored here) | `--template PATH` (default: beside the script), `--out PATH`; `--help` lists them; exit 1 if the template or `python-pptx` is missing |

- The script carries the Gemba App worked-example text with placeholders. Replace the slide text with the case's own figures from the backbone before showing the deck.
- An agent runs a script with its code or shell tool and reads the exit code and output.

## Example

```text
Case: "Line-side digital shift log" (fictional)
| Criterion | Verdict | Evidence | Note |
| C2 grounding tag on every figure | gap | business-case.md, "Levers" | two figures untagged |
| C1 value-only separation | pass | business-case.md, "Scope" | |
| C4 de-banking applied | partial | business-case.md, "O1" | range shown, but summed into headline |
Verdict: Not ready (C2 gap). Missing input: the source of the two figures; owner: case builder.
```

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Passing a figure that has no grounding tag | A bare number looks like a fact and reaches the approvers as one |
| Scoring from the headline or summary instead of the inputs | Conflicts between sources and untagged figures sit in the inputs |
| Accepting a headline that sums hard and optional levers | The bankable floor is overstated; C3 is violated |
| Passing a big lever resting on an `[unknown]` because the range is plausible | C4 requires a sensitivity range, labelled not banked |
| Fixing the case while assessing it | The builder then cannot see what was wrong; return it to `bc-build` |
| Letting the builder assess their own case | Separation of duties is lost |
| Reading the deck as the case | The deck renders the backbone; score the backbone |

## Do not

- Do not fix the case while assessing it; return it to `bc-build` with the findings.
- Do not pass a figure without a grounding tag, or a headline that sums hard and optional levers.
- Do not let the builder assess their own case.

## Definition of done

- `bc-assessment-report.md` holds the scorecard with evidence, the conflict register, the verdict and the ranked open questions; the assessor is not the builder; a signable case goes to `bc-capital-request`, an unsigned one back to `bc-build`.
- The pre-verdict check passed.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/criteria-checklist.md`](references/criteria-checklist.md) | Scoring any criterion: the full definition and what counts as pass or gap |
| [`references/grounding-discipline.md`](references/grounding-discipline.md) | Deciding whether a figure earns `[input]`, `[assumption]`, `[market]` or `[unknown]` (C2, E3) |
| [`references/lever-model.md`](references/lever-model.md) | Checking lever IDs, formulas, the min / expected / max matrix and de-banking (C3-C5, D1-D2) |
| [`references/provenance-and-conflicts.md`](references/provenance-and-conflicts.md) | Writing the conflict register (step 4) |
| [`references/worked-example-gemba.md`](references/worked-example-gemba.md) | Writing the report, to copy the pattern of a complete run |
| [`references/deck-spec.md`](references/deck-spec.md) | The user wants the optional deck: slide-by-slide content rules |
| [`references/build-engine.md`](references/build-engine.md) | Running the deck script, its QA loop and the brand palette |
| [`references/outputs.md`](references/outputs.md) | Checking what each output must contain and who receives it |
| [`references/background.md`](references/background.md) | Context, rationale, hand-off and notes; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`scripts/build_bc_short.py`](scripts/build_bc_short.py) | Run it as the Procedure says; `--help` lists the arguments |
