---
type: Skill Reference
title: Process chain practice
description: How the IT demand package is assembled at chain step 3a4 - the demand-management question list, the request flow, small change versus project routing, the supplier-built app and selection practice, commercial consistency check, decision phrasing, handoffs and agent notes.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - the demand package in the chain

Derived from the Operations Digitalization slide decks (demand-management, capital-request, project-order and supplier-exchange decks),
abstracted into process guidance. No figures. IT's own demand form is still not in the decks; `<...>` marks it. `PROPOSAL` =
synthesis not stated in a deck.

## Where it sits in the chain

3a4 package or build the app (routes 3a.3 and 3a.4), after 31 requirements, 32 tool decision and 33 business case. Downstream: IT
demand management and its board (human), then `deploy-appstore` (3a5).

## 1 Method in practice

### The demand-management question list

The deck lists these questions with unanswered ("tbd") cells; use them as the checklist and mark each answered or open:

1. Who can raise requests? 2. Who manages the backlog? 3. Who evaluates? 4. Who decides yes or no? 5. Who estimates effort? 6. Who
decides to start development? 7. Who develops? 8. Who does final testing? 9. Who decides and triggers implementation? 10. Which
configuration items are affected? 11. Who is responsible for implementation? And per step: which tool documents and tracks it.

### The flow in the deck

Request by the key user -> backlog kept by the product owner -> evaluation -> work order by the service centre -> development system
-> test system -> user acceptance -> transport to production -> post-implementation review with the requester -> change coordination
(tasks, approvals, risks, affected configuration items).

### Small change or project?

A small change (a few days of effort, budget available, standard interface) is requested by the local key user in the ticket tool and
approved in the change process. Anything larger, needing central budget or a non-standard interface, becomes a project and goes to
the governance board with the product owner. A package belongs here only in the second case.

### Intake form that arrives already complete (Quick Charter questions)

Business problem; existing solution to modify or new; business functions needed; obstacles (typically uneven deployments of the source
system across plants, inconsistent API availability); deadline and why; requesting organisation and proposed sponsor; risk if not
solved; business benefit; investment capacity.

### Demand-request one-pager fields

What it is; business value; who benefits (roles); one-time cost; running cost over the planning horizon; business representative; IT
representative; budget source (IT or business); budget owner; timeline of benefit realisation; footnote that figures are estimates.
Name both a business and an IT representative. Never leave the budget empty, even for internal effort: give an educated guess and
label it. The headline is potential, not banked value.

### Decisions phrased as pairs

*Decision* - *Proposal* (including limiting conditions such as a time limit or a reduced audit) - *Risk of not doing* (the realistic
alternative, for example that the thing happens anyway through uncontrolled channels). When no competitive comparison was run, say so
and plan it along the work; get a quote before the cost risk is accepted.

### Supplier-built app: what the package must prepare

- Requirements handed to purchasing are the product backlog; the offer is the input to the purchase order, which precedes
  development. The requirement specification document is the contract anchor.
- Milestones: requirements, purchase order, environment, installation, configuration, function and integration tests, dashboards,
  key-user training, security approval, go-live and handover, lessons learned. Short sprints with a weekly supplier meeting and internal
  testing between sprints; strong location support is needed.
- Round two with each shortlisted supplier uses the same agenda: demo, feature-solution session on one or two requirement stories,
  advantages and disadvantages for the pilot and for scale-out, Q and A on a question sheet. Detail in
  `od-system-fit-check` (practice file).
- Ask for source ownership in the contract (see `deploy-appstore` scenarios).

### Commercial consistency check (add before the package is called ready)

Obtain the offer first (a second quotation where the policy asks), then raise the capital request; before ordering, offer = capital request = contract must agree (check). They must be the same version; a named role drives purchasing; a frame contract is used where one
exists. Lessons: an eCR launched before a contract separation was stopped; offer versions then disagreed with the eCR and with the
contracted version; a first purchase order could not be approved because of a contract carry-over; nobody owned purchasing.
Connectivity-related requests repeatedly arrived incomplete and deviated from the standard rollout templates and frame contracts; use
the cost calculator for the connectivity scenario before the project starts.

## 2 Decision rules

| Situation | Rule |
|---|---|
| Initiative lists no lead, team or sponsor | Do not enter routing; name the missing role |
| Demand stays inside platforms OD owns | No package |
| Front-end part missing (requirement, fit verdict, business case) | Name it and stop |
| New little-understood field | Fund the first step only, time-boxed, assess, then decide continuation (limit the cost of failure) |
| Foreign app whose supplier status is unclear | Mark `<missing>` with the person who can close it; no guess |
| Larger-than-small change or non-standard interface | Project; governance board with the product owner |
| Approval route for the application | OD and IT approve any plant software solution so data, interface and knowledge domains fit |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `od-requirements-breakdown` | Epic and stories, acceptance criteria |
| Receive | `od-system-fit-check` | Verdict and boundary quoted, operations-concept status |
| Receive | `od-benefit-calculation` / `od-capital-request` | Tagged figures, firmness, alternatives |
| Receive | `od-system-fit-check` | Route 3a.3 or 3a.4, source ownership, run owner |
| Hand on | IT demand management (human) | The package, open items with owners, "submitted by a human on `<date>` - not yet" |
| Hand on | `deploy-appstore` | Decision, scenario, owners |
| Hand on | `od-cybersec-gate` | Components, data path, open points |

## 4 Pitfalls and lessons

- Plants' capital requests were not always supported locally, so work "did not materialize"; push for local management approval and
  list the approving manager as a field.
- Reorganisation can orphan Cyber Security ownership or the central funding path: list as open items.
- Budget class of the pilot differs between copies of the same summary: confirm with controlling before submission.
- An AI-built prototype follows the path generated solution, IT takeover, Cyber Security approval; do not skip the takeover.

## 5 Questions to ask and definition of done

Who is the business representative and who the IT representative? Who owns the budget? Which question of the list above is still
open? Is the offer the same version as the capital request and the contract? Who drives purchasing?

Done = parts in the table filled, every gap `<missing>` with an owner, consistency check run, route stated, submission left to a human.

## 6 AI agent operating notes

- **Can do**: walk the question list and mark unanswered ones, assemble the package from the front-end outputs, run the consistency
  check, draft the decision pairs, prefill the one-pager fields from the demand text.
- **Inputs required**: requirement, fit verdict, tagged business case, offer and contract references, plant sponsor.
- **Evidence to cite**: each package part's source skill output and date; quote and frame-contract id where used.
- **Human gates**: submission to IT demand management, the board's decision, budget commitment, the product owner's yes or no.
- **Handover**: the package plus an open-items list with owner roles.
