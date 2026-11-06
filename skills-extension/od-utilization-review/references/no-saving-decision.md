---
type: Skill Reference
title: No-saving decision
description: What to do with a scaled-out use case that has deployments but no saving - the contradiction between decks (to be evaluated vs no potential), the safer reading, the decision rule, and the savings-forecast gate at the close of a sprint.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# No-saving decision

## 1 The rule

A scaled-out top use case that is deployed without a reported saving is "to be evaluated until investigated" (one deck version
records it as "expected savings to be evaluated"; a later revision wrote "the use case probably has no potential" without evidence,
so treat that wording as unproven). "No potential" is a result of an investigation, not a status to write in advance. Only a human
(the OD lead with the plant owner) may decide "no potential"; an agent never writes it.

## 2 Three lists per use case

For each top use case state: where it saved, where it was deployed without saving, where it still has potential. Mark each line
tracked or proven (`od-portfolio-and-savings-analysis`). A use case that cannot show a before/after condition is not countable as a saving.

## 3 Decision rule (PROPOSAL)

Take the rows deployed without saving and walk them in order:

1. **Is a saving unreported?** The deployer may not report. Ask the plant; if yes, route to `od-impact-evaluation` and the ledger. Not a utilization gap.
2. **Is it used with an action?** If `USED-WITH-ACTION` but no saving: calculate it (`od-benefit-calculation`), then register it.
3. **Is it used without action, or not used but fixable** (no ritual, no action owner, no access, no training)? Re-scope and follow up; re-evaluate at the review date `<months>`.
4. **Not used and not fixable at this site** (no process need, wrong site type, cyber-security or platform barrier)? Propose retirement at the site or a site-specific "no potential here". Escalate to the OD lead.
5. **Same use case saved elsewhere?** Then the gap is adoption or site fit, not the asset. Compare sites with similar systems and effort but different savings: equal effort with zero savings points to people and method, not technology (`od-use-case-standardization`).

Use-case-wide "no potential" needs: investigation done at the sites listed, evidence cited, plant owner heard, decision by a human
(OD lead with the plant owner; the deciding role or forum named in the current approval policy, look up via `od-decision-routing`). Reasons seen for missed savings: no savings-calculation standard, weak requirements,
no follow-up or escalation, culture and perceived value, cyber security, unclear roles, production and OPEX not involved.

## 4 Sprint-close savings-forecast gate

At the end of a use-case sprint, every use case implemented in the sprint must have a savings forecast and a registered project, or an
explicit, owned reason. The decks show sprints that closed with neither, leaving the savings pipeline partly invisible. The gate itself is
a proposed addition (`PROPOSAL`; the owner places it): this review supplies the check, the sprint owner stops the close.
Agent: list the sprint's use cases, flag "implemented, no forecast / no project registered"; human: plant owner confirms adoption, sprint owner decides to close.

## Recording the decision

Use `assets/utilization-review-record.md`: verdict, decision (evaluate / re-scope / retire / escalate), evidence, owner, review date.
