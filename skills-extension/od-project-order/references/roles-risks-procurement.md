---
type: Skill Reference
title: Roles risks procurement
description: Requesting side versus contracting side in a project order, how opportunities and risks are classified and treated, the limited-risk funding pattern for an unfamiliar field, and the procurement milestone chain for a bought solution.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Roles, risks and procurement chain

## Two sides

| Side | Who | Does |
|---|---|---|
| **Requesting** | Steering committee, including the sponsor | Sponsor authorises the order and mediates; the committee nominates the project manager, approves the plan, provides resources, decides on changes and is the escalation authority |
| **Contracting** | Project team, including the project manager | The project manager owns the status light and the budget (within the sign-off rules), reports and escalates; the team delivers the work packages |

The project manager sets the traffic light within the agreed KPIs; the steering committee decides on changes
to scope, timing or budget. The approved order lists real names; an agent draft lists roles and
`<name>` placeholders. Approval is documented (signature, e-signature or e-mail).

Before a system goes to productive use it also needs a business owner, an IT owner, a service concept,
roles and responsibilities, requirements, a change-management process and a risk-management process
(see `od-system-fit-check`). Name them in the organisation chapter or list them as open.

## Opportunities and risks

1. Keep opportunities and risks as two separate lists.
2. Rate each by probability times impact on scope, timing, financials and quality: high, medium or low.
3. A **high** risk requires a treatment; the treatment effort goes into plan and budget.
4. Per risk: countermeasure, owner, due date.
5. Prompting questions. Risks: what could slow the project, overrun the budget, prevent delivery. Opportunities:
   what could speed it up, save money, boost results. Always: are the team members available, are they trained.
6. The steering committee's boundary conditions go next to the risk list.
7. Hand risks with owner and due date to `od-risk-watch`.

## Limited-risk funding pattern (unfamiliar field)

When a field is new and little understood, fund only the first step (for example the governing tool or
framework), time-box it (about a year), assess the benefit, then decide continuation at minimum cost
("minimising the cost of failure"). A decision paper for such a step lists each needed decision, the
option proposed and the risk of not deciding (for example a security-audit scope, or whether to run a
supplier comparison). Take the decision itself to `od-decision-routing`.

## Procurement milestone chain (bought solution)

Order of milestones; each is a date in the plan and a line the project manager reports on.

1. NDA closed.
2. First-round quotation.
3. Supplier Q&A and selection.
4. Quotation updated from the Q&A.
5. Second-round quotation (where the approval policy asks for a second quotation).
6. Capital request (eCR) launched and approved. The package is `od-capital-request`; the approval is human.
7. Sourcing complete. Before ordering, offer = eCR = contract (check).
8. Go-live within a fixed window after the purchase order (`<window>` set per project).

For machine connection, the equipment request is the first milestone of each integration wave
(`od-equipment-integration`). The offer is obtained first (a second quotation where the policy asks), then the eCR is raised; offer, eCR
and contract must agree before the order is placed.

## Pitfalls

- Capital requests not supported by the plants, and eCR set-up as a weak point: the work then "does not
  materialize". Make the plant's part of the eCR a named milestone with an owner.
- Open question to the steering committee that blocks everything (can budget go to external suppliers; can
  supplier selection for future contracts start). Put it on the kick-off list early, with the cost of not deciding.
- A high risk listed without treatment; a treatment that is not in the budget.
- An order that names no owner on either side.
