---
name: bc-capital-request
description: >-
  Packages a use case's value rows and cost estimate into a draft capital request (eCR) and management summary deck for human approvers: ask in one line, approval route by amount, options including do-nothing, risks, sensitivity, open items and a maturity verdict. Use when a Lane 2 use case has passed its business case and needs investment, a Lane 3 system needs funding, a saving waits on ECR CREATION or ECR APPROVAL, or someone asks "how do I get this funded". Drafts only; a human submits, approvers decide. Not for calculating value (bc-build), costs (bc-cost) or scoring the case (bc-assess).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: bc-capital-request
  aliases: [od-capital-request, eCR]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (25), Lane 3 front-end (33)"
  new_state_step: "Capital request if investment is needed; Business case, prioritization, capital request"
  department_names: ["bc-capital-request", "ecr-builder", "capital-request-builder", "eCR"]
  owner_role: human:jakob.gabriel
  tags: [use-case-support-service, practice, new-state, ready]
  authority_level: draft the request; submission and approval are human
  status: ready
  requires: [dept-context]
  composes: [bc-build, dept-decision-rights, funnel-prototype, bc-portfolio, funnel-evaluation, invest-screen, bc-cost, deploy-cybersec, deploy-handover]
  okf:
    type: Agent Skill
    title: Capital request
    tags: [use-case-support-service, practice, new-state, ready]
---

# Capital request

- Read `dept-context` first.
- The department's `bc-capital-request` (its package `ecr-builder`) is the last link of the business-case chain: value from `bc-build`, cost from `bc-cost`, assessment verdict from `bc-assess`, then this package for the approval route.
- It does not recalculate value, set thresholds or approve.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Packages a use case's value and cost into a draft capital request (eCR) so the human approvers can decide.
- Use it when a Lane 2 use case has passed its business case and needs investment, when a Lane 3 system or connector needs funding, or when a saving waits on `ECR CREATION` or `ECR APPROVAL`.

## Inputs and output

- **Inputs**: the use case record, the saving rows from `bc-build`, the cost side from `bc-cost`, the validation record from `funnel-prototype`, the solution-evaluation verdict, and the Plant ME agreement on priority.
- **Output**: the package [`assets/capital-request-package.md`](assets/capital-request-package.md) and the management summary deck from the builder, closed with the open items and one maturity verdict. A human reviews and submits.
- **Where it sits**: Lane 2 step 25 and Lane 3 front-end step 33 (see `references/background.md`).

## Procedure

1. **Confirm a request is needed.** Is there money to commit (hardware, licences, external work, headcount)? If the work is within the plant roadmap and spends nothing new, no capital request: record that and stop.
2. **Collect the inputs.** The use case record, the saving rows (`bc-build`), the investment estimate (`bc-cost`), the validation record (`funnel-prototype`), the solution-evaluation verdict, the Plant ME agreement on priority.
3. **Refusal / de-risk gate** ([`open-items-and-conflicts.md`](references/open-items-and-conflicts.md)).
   - If the value backbone, the investment estimate or the assessment verdict is missing or too thin to carry the amount, stop and return the de-risk questions from its question bank, not a package.
4. **Route first** (`dept-decision-rights`): read the amount against the tiers of the approval matrix ([`ecr-approval-matrix.md`](references/ecr-approval-matrix.md)), classify the case (IT invest, expansion, R&D, real estate) and list the approvers by role.
   - If the recorded ladder is ambiguous for the amount, do not pick a side silently ([`references/spend-route.md`](references/spend-route.md)); the OD lead confirms the route.
   - Also name the other gates the spend touches: IT demand (OpenSpec IT demand, external), Cyber Security (`deploy-cybersec`, `mi-equipment`).
5. **State the ask** in one line: amount, what it buys, what phase it funds, by when it must be decided.
6. **Pull the value in, do not rebuild it.** Take each saving row with amount, year, category, rationale, methodology, reliability and dependency.
   - Show **tracked and proven separately, never summed** (`bc-build`).
   - Where a row has no methodology it is an estimation: label it so.
7. **Pull the cost side in from `bc-cost`.** Use its investment estimate (one-time and recurring: people, hardware, licences, external, compute, IT demand); do not define cost lines again here.
   - Every figure has a source and a date, or is ⟨to be collected⟩ with the role who supplies it.
   - The checklist of what a cost side holds is in [`references/business-case-structure.md`](references/business-case-structure.md).
8. **Give options and the do-nothing case**, and for each decision its risk of not doing. At least: the request, a smaller or staged version, and not acting.
   - Include the library alternative (adopt a proven solution) if one exists.
9. **State risks, sensitivity and dependencies.** The one assumption the case fails on, a range not a point where the value is asserted, an adoption haircut if people must act on the output, prerequisites that must exist.
10. **Define what the money buys and how it will be judged:** a validation plan or stage gate for the funded phase with a pass criterion, a validator and a date (pattern in `funnel-prototype`).
11. **Record the gate as a dependency** on the use case and on each affected saving row (`ECR CREATION` while drafting, `ECR APPROVAL` once filed), with the owner (`bc-build` dependency list).
12. **Render** the management summary with the builder ([`build-engine.md`](references/build-engine.md)): every figure carries its grounding chip, the last slide is Open items and conflicts, and the reply mirrors it in one line.
13. **Check before handing over** (repeat until all hold):
    - [ ] The ask is one line with amount, purchase, phase and decision date.
    - [ ] Route and approvers are written next to the amount.
    - [ ] Tracked and proven are separate; every figure has its chip.
    - [ ] Options include a smaller version and do-nothing; one verdict is stated.
14. **Hand the package to the human** to review and submit. Stop there. After the decision, record the outcome in the package and update the dependency.

## Maturity verdict

- Close every package with the open items and conflicts and one verdict: **Ready to sign**, **Sign the floor** (approve the grounded part only) or **Not ready**.
- Recommendation only.

## Human gate and AI-agent notes

- **An agent may**: check whether a request is needed, read the amount against the approval matrix, collect the inputs, draft the package and the deck, list open items, and propose the maturity verdict.
- **Stays with roles**: the OD lead confirms the route when the ladder is ambiguous; the approvers named in the approval matrix (by role, tier and case type) decide; Finance confirms rates and whether the matrix still applies; a human submits.
- The agent never submits, signs or approves.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/build_ecr.py` | Render the eCR management summary as a neuwerk-branded pptx. Needs `python-pptx` and the neuwerk template `_nw_template.pptx` (from the `ecr-builder` package, not stored here) | `--template PATH`, `--case case.json` (overrides slug, title_tag, presenter, year, tagline), `--out PATH`; `--help`; exit 1 on missing template, bad JSON or missing `python-pptx` |
| `scripts/render_qa.sh` | Render a pptx to one jpeg per slide so the result can be looked at. Needs `soffice` and `pdftoppm` on PATH | `deck.pptx [dpi]` (dpi defaults to 100); exit 1 if a tool is missing |

- The slide content inside `build_ecr.py` is the illustrative worked example; edit it for the case before showing the deck.
- An agent runs a script with its code or shell tool and reads the exit code and output.

## Example

```text
Input : ask = 100 (fictional units) for a pilot phase; value rows = 2 (tracked, none proven);
        cost = one-time hardware 40, recurring licence 10 per year; verdict = Sign the floor
Output: route = tier by amount and case type, approvers listed by role
        value: tracked 80 | proven 0   (shown separately, never summed)
        dependency on both rows: ECR CREATION -> ECR APPROVAL once filed
        last slide: Open items and conflicts; verdict: Sign the floor
```

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Printing NPV or IRR without a measured baseline | The result looks precise but rests on a guess; fund the baseline first |
| Offer, eCR and contract disagree on version or scope | Approvers sign one thing and purchasing orders another |
| Splitting one investment into several requests | It can dodge a threshold; this is a proposed rule, not stated in the sources |
| Treating a saving that waits on this approval as booked | It is not real until the gate is passed |
| Taking an approval tier from memory | The ladder can be ambiguous or out of date; read the matrix and ask the OD lead |
| Turning a missing value into zero or a range into its mid-point | It hides the uncertainty the approvers need to see |

## Do not

- Do not call the request ready before offer, eCR and contract agree on version and a named role drives purchasing (`references/process-chain-practice.md`), because approvers would sign a spend that purchasing cannot execute.
- Do not net value against cost, and do not print NPV or IRR when no measured baseline exists; fund the baseline first.
- Do not submit, sign, approve or state that approval will be given. Those are human (`dept-decision-rights`: an agent never commits investment or allocates resources).
- Do not put a threshold, a form field or an approval time in the package that no source gives.
- Do not add tracked and proven euros together, or present a saving that is waiting on this approval as booked.
- Do not turn a missing value into zero, or a range into its mid-point without saying so.
- Do not invent cost lines or rates; mark them ⟨to be collected⟩.
- Do not duplicate `bc-build` or `bc-cost`: reference their rows and estimate, do not re-derive them.
- Do not split one investment into several requests to land under a threshold.

## Definition of done

- The package in [`assets/capital-request-package.md`](assets/capital-request-package.md) is complete or its gaps are named with a role who closes them; the route and approver are written next to the amount; tracked and proven euros are separate.
- The dependency is recorded on the saving rows; a human has been handed the package.
- Nothing has been submitted or approved by the agent.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/ecr-management-summary.md`](references/ecr-management-summary.md) | You need the eCR section map, enums, governance conditionals and the builder's house rules |
| [`references/ecr-builder-workflow.md`](references/ecr-builder-workflow.md) | Running the builder: ingest, refusal gate, grounded backbone, honesty deck, verdict, rendering |
| [`references/backbone-and-conditionals.md`](references/backbone-and-conditionals.md) | Compiling the backbone and deciding which conditional sections apply |
| [`references/grounding-and-color-coding.md`](references/grounding-and-color-coding.md) | Choosing a grounding chip and colour for a figure on the deck |
| [`references/open-items-and-conflicts.md`](references/open-items-and-conflicts.md) | Applying the refusal gate or writing the closing slide and the de-risk questions |
| [`references/build-engine.md`](references/build-engine.md) | Running `build_ecr.py` and `render_qa.sh` and checking the rendered slides |
| [`references/ecr-approval-matrix.md`](references/ecr-approval-matrix.md) | Finding the approver chain by amount tier and case type (IT invest, expansion, R&D, real estate) |
| [`references/spend-route.md`](references/spend-route.md) | The ladder is ambiguous for the amount, or you need to know what a booked saving waits on |
| [`references/business-case-structure.md`](references/business-case-structure.md) | Checking what a business case and its cost side should hold and what is typically missing |
| [`assets/capital-request-package.md`](assets/capital-request-package.md) | Producing the package the human submits |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Writing the management summary, decisions with risk of not doing, sensitivity, the offer-eCR-contract check |
| [`references/outputs.md`](references/outputs.md) | Checking each output's recipient and completion rule |
| [`references/background.md`](references/background.md) | Where the skill sits in the lanes, source notes and open points; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`scripts/build_ecr.py`](scripts/build_ecr.py) | Run it as the Procedure says; `--help` lists the arguments |
| [`scripts/render_qa.sh`](scripts/render_qa.sh) | Run it as the Procedure says; `--help` lists the arguments |
