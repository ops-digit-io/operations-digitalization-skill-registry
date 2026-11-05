---
type: Skill Asset
title: Capital request package
description: The package od-capital-request produces for the human who files the eCR - ask and route, need, evidence, value with firmness, cost, options, risks, dependencies, validation plan and approval fields.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, template, protocol]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Capital request package - ⟨use case or system name⟩

Copy once per request. The structure is a proposal built from the department's business-case records
([`../references/business-case-structure.md`](../references/business-case-structure.md)); the actual eCR form is
not in the sources, so the human who files maps these sections onto it. **Drafted by an agent; submission and
approval are human.** Leave section 10 blank.

| | |
|---|---|
| **Use case / system** | ⟨name, plant(s), lane (2 or 3)⟩ |
| **From** | ⟨definition, solution-evaluation, validation records⟩ |
| **Drafted by / date** | ⟨role⟩ · ⟨date⟩ |
| **Status of this draft** | ⟨complete · gaps named⟩ |

## 1 · Ask and route

| | |
|---|---|
| **Amount** | ⟨EUR, one-time⟩ plus ⟨EUR per year, recurring⟩ |
| **What it buys / phase funded** | ⟨one line⟩ |
| **Decide by** | ⟨date and the reason⟩ |
| **Spend ladder** | ⟨per the current approval policy (look up: OD lead / Finance); quote it as the source words it, with its date⟩ |
| **Approver for this amount** | ⟨name the body; ⟨to confirm with the OD lead⟩ if the recorded thresholds overlap at this amount⟩ |
| **OD decision row** | ⟨Digitalization investment planning: OD lead with BA Operations, consultation, `recommend`⟩ |
| **Other gates touched** | ⟨IT demand · Cyber Security · CSP · plant adoption · none⟩ |

## 2 · Need and scope

⟨The problem in the plant's words, the use case in one paragraph, what is in and what is explicitly not in the
request (for example rollout, hardware, licences). Solution-evaluation verdict: ready to build / capability to
raise first / over-engineered / platform investment.⟩

## 3 · Evidence

| Item | Source and date |
|---|---|
| Validation record | ⟨`od-prototype-poc` record: status label mock-up, PoC or pilot; result vs. criterion⟩ |
| Baseline | ⟨measured or asserted? say which; source, date⟩ |
| Data verdict | ⟨`od-data-availability-check` verdict⟩ |
| Precedent | ⟨library entry or other plant, or none⟩ |

State the label honestly: a pilot or PoC is evidence, not proof.

## 4 · Value (from `od-benefit-calculation`; do not recalculate here)

| Row | Amount | Year | Category | Rationale | Methodology | Reliability | Proven? | Dependency |
|---|--:|---|---|---|---|---|---|---|
| ⟨1⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨formula or "none: estimation"⟩ | ⟨CALCULATION / ESTIMATION / not recorded⟩ | ⟨yes / no⟩ | ⟨ECR CREATION / ECR APPROVAL / other⟩ |

| | EUR |
|---|--:|
| **Tracked** (all rows) | ⟨⟩ |
| **Proven** (passed SPRINT) | ⟨⟩ |

The two lines are never added. Rows with no figure are ⟨to be collected⟩ from ⟨role⟩, not zero. Range with the
reason for low and high: ⟨⟩. Adoption haircut if people must act on the output: ⟨percent, source⟩.

## 5 · Cost

| Line | One-time | Per year | Basis and source | Status |
|---|--:|--:|---|---|
| People (FTE times rate) | ⟨⟩ | ⟨⟩ | ⟨rate source: Finance⟩ | ⟨firm · estimate · to be collected⟩ |
| Hardware | ⟨⟩ | ⟨⟩ | ⟨quote or catalog⟩ | |
| Licences / platform | ⟨⟩ | ⟨⟩ | | |
| External work | ⟨⟩ | ⟨⟩ | | |
| Compute / hosting | ⟨⟩ | ⟨⟩ | | |
| IT demand / platform effort | ⟨⟩ | ⟨⟩ | ⟨IT estimate⟩ | |
| Plant time (validator, training) | ⟨⟩ | ⟨⟩ | | |
| **Total** | ⟨⟩ | ⟨⟩ | | |

Costs the plant carries after handover and who carries them: ⟨⟩.

## 6 · Options

| Option | Cost | Value | Why chosen or not |
|---|---|---|---|
| The request | | | |
| Staged / smaller | | | |
| Adopt a proven library solution | | | |
| Do nothing | | | cost of not acting: ⟨⟩ |

## 7 · Risks and sensitivity

- **Key risk** (one falsifiable sentence, with its consequence): ⟨⟩
- **Inputs that are asserted, not measured**: ⟨⟩
- **What moves the range**: ⟨⟩

## 8 · Dependencies and prerequisites

| Dependency | Owner | State |
|---|---|---|
| Other requests or use cases this needs | ⟨⟩ | ⟨⟩ |
| Signals / machine integration | ⟨IIAE⟩ | ⟨⟩ |
| IT demand, Cyber Security | ⟨⟩ | ⟨⟩ |
| `ECR CREATION` / `ECR APPROVAL` recorded on the use case and on rows 4.⟨n⟩ | ⟨role⟩ | ⟨to be recorded by the human at filing⟩ |

## 9 · Validation plan for the funded phase

| | |
|---|---|
| **Scope and time box** | ⟨⟩ |
| **Pass criterion, baseline, validator (a plant role)** | ⟨⟩ |
| **On pass / on fail** | ⟨release next tranche · stop · re-scope⟩ |
| **Handover** | ⟨`od-handover-and-adoption`: plant owner, utilization expectation⟩ |

## 10 · Approvals and outcome (human fields; the agent leaves these blank)

| | |
|---|---|
| **Reviewed by (OD lead / Plant ME)** | |
| **Filed by / date / reference** | |
| **Approver / decision / date** | |
| **Conditions attached** | |
| **Dependency updated on use case and rows** | |
