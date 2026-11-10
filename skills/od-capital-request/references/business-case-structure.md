---
type: Skill Reference
title: Business case structure
description: What a business case holds in the department's own records (the work vault Business Cases folder) - fields, ranges, scores, cost split, validation plans, prerequisites and typical gaps - as a pattern for the capital request package. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Business case structure

Source: `Work-OpsDigit-Knowledge/Graph/Business Cases`, notes from the SharePoint list
"BusinessCasesAIatOperations". Re-read the folder before relying on this file: the set of cases changes.

**What these are, and are not.** They are business cases for an **AI-at-operations portfolio** (predictive
maintenance, vision QC, a catalog sprint, a manufacturing app store and so on), written at portfolio level with
ranges. They are not eCR submissions, not plant use-case business cases and not proven. The notes typically do not
mention an eCR as a dependency; the eCR dependencies in the department's records sit on saving rows
(`spend-route.md`). Use them as a pattern for structure, never as evidence for a value or a cost.

## The fields a case carries

| Field | What it holds |
|---|---|
| Description | What it is, in one paragraph; sometimes "why no standalone euro" |
| Evidence | External anchors and internal baselines, with source tags |
| Prerequisites | What must exist first; often names another case of the portfolio |
| Validation plan | Where, how long, what is run, pass criterion (check that one is stated) |
| Sensitivity notes | What moves the range; adoption haircuts; what breaks it |
| Cross references | Links to the catalog, other cases, external sources |
| Key risk | One falsifiable sentence the case fails on |
| Cost breakdown (resources plus costs) | People as FTE times rate, then compute, licences, external assist |
| MVP scope | Smallest thing that tests the key risk |
| Portfolio linkage | Which catalog use cases or fleet it touches |
| Value justification | Anchored arithmetic: quantity times baseline times rate times reduction |
| Score justification | Why the score is what it is, including "enabler, not standalone" |

Header fields: code, category, portfolio tier, cost low / high / mid, value low / high / mid (per year), confidence
score 1 to 5 with a note, strategic fit and synergy scores, a value-effort score. To see how complete the fields are
today, count the filled fields in the live folder (look up: the Business Cases notes).

## How to read the ranges and scores

- **Cost ranges** are written low-high with a mid. A few cases give none; check why before comparing.
- **Value ranges per year** are absent by design for foundation or enabler cases (catalog sprint, edge MLOps
  backbone, attribution layers, sensor-upgrade frames, ramp-up outcomes). Each says why in its text. An enabler is
  valued by what it unlocks, not by a standalone number.
- **Confidence scores** run on a 1 to 5 scale. The lowest belong to big bets and R&D-only bets; a big bet can be
  defended on the cost of not acting rather than on value-effort ratio, and the case says so.
- **Portfolio tiers** in use include quick win, enabler, platform, sprint, big bet, process, defer to a later year,
  and bundle. A tier is a recommendation about timing and funding, not an approval.

## Patterns worth copying into a request

1. **Cost split in two lines**: "Resources" (people as FTE times annual rate) and "Costs" (compute, licences,
   optional external assistance), each with a total. A predictive-maintenance style case lists roles as FTE
   fractions, compute per year and optional vendor benchmarking. The FTE rates are the case's own;
   ⟨department cost rates⟩ come from Finance.
2. **Value anchored in more than one way, one of them dropped honestly.** One case builds value from downtime
   avoidance (assets times hours times rate times avoidance share), preventive-maintenance deferral, and
   remaining-life extension; it takes the first as the case, calls the second small and leaves the third out because
   it is hard to attribute. Quote the arithmetic, not only the result.
3. **A range with a stated reason**: sensitivity notes say what the range depends on, what today is "asserted, not
   measured" and what baseline data to request. Copy this: say which inputs are asserted.
4. **An adoption haircut where people must act**: a case plans a haircut in year 1. Value that needs behaviour
   change is not booked at full.
5. **Enabler framing**: a case that is weak alone but multiplies others says so and warns not to count its value
   twice and not to fund it if its parents stay deferred. When a request depends on another request, say which and
   what happens if it is declined.
6. **Key risk as one falsifiable sentence** with the consequence ("if the false-positive rate is too high, teams
   ignore alerts, adoption collapses, no realized euro").
7. **MVP scope plus validation plan**: a small asset set in one pilot plant, a time box in weeks, named pass
   criteria. The request funds a test first when the key risk is unresolved (patterns in `od-prototype-poc`).
8. **Decision foundation first**: a catalog maturity sprint is "not a euro number"; it makes the other cases'
   numbers defensible and gates later funding at a coverage threshold. A request may be a prerequisite for decisions
   rather than a saving.

## What is typically missing or weak

- **Asserted baselines**: "today this is asserted, not measured" appears in a case's own sensitivity text; ranges
  rest on assumed asset counts and rates.
- **No outcome**: check whether any case records a pilot result, a decision, an approval or an eCR number. Typically
  they are proposals.
- **Mid-points do the work**: scores and portfolio ranks use the mid of a wide range. A request should show low and
  high and the reason, not only the mid.
- **Costs for enablers rely on assumed availability** (for example owner time per owner).

## Structure proposed for the capital request package

This maps the fields above onto what `od-benefit-calculation` and the routing add. It is a **proposal**, because no
eCR form is in the sources ([`../assets/capital-request-package.md`](../assets/capital-request-package.md) implements it).

| Package section | Fills from |
|---|---|
| 1 Ask and route | amount, phase funded, approver per `spend-route.md` |
| 2 Need and scope | use case record (`od-use-case-definition`), solution-evaluation verdict |
| 3 Evidence | validation record (`od-prototype-poc`), baselines with source and date |
| 4 Value | saving rows with firmness; tracked and proven separately (`od-benefit-calculation`) |
| 5 Cost | resources and costs split, one-time and recurring |
| 6 Options | request, staged, adopt-from-library, do nothing |
| 7 Risks and sensitivity | key risk sentence, range reasons, adoption haircut |
| 8 Dependencies and prerequisites | other requests, IT demand, Cyber Security, signals, `ECR` dependency |
| 9 Validation plan for the funded phase | scope, time, pass criterion, validator |
| 10 Approvals and outcome | filed by, approved by, date, decision - human fields, left blank by the agent |
