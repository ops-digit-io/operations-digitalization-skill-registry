---
type: Skill Reference
title: Evidence and human decisions
description: What an AI agent must cite at each process step, how it labels drafts, and the list of decisions and signatures that stay with a named human role.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, ai]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Evidence and human decisions

## 1 Citation rules

1. Every figure, name, status or classification carries a source (list row, library entry, document,
   tool-status line) and the **read date**. No source, no statement.
2. Missing input is written `<...>` and listed; it is never replaced by a plausible value.
3. An output with open items or missing citations is labelled **draft**; only a human removes the label.
4. Label what kind of claim it is: tracked versus proven (`od-context`), input versus assumption versus
   unknown (business-case figures), prototype versus pilot versus proven (`od-prototype-poc`).
5. Say which rule or check was used for a classification (for example the label-suffix rule for a signal
   match, the bucket rule for a triage label).
6. If a check could not be run (no render, no data access), say that; never imply it was done.

## 2 Per step: what to cite, where the human gate sits

| Step | Agent may | Must cite | Human gate |
|---|---|---|---|
| spine | check sections against review dates | section, owner, review date | OD lead confirms updates |
| i1 | classify the request (object, event, time; advice or change; Just-do, Go-forward, Lead-change) | the fact used (machine connected, prototype exists) | triage owner; Lead-change label |
| 21 | rewrite the request, pre-fill canvas and one-pager | use-case list row, library entry, tool-status source and date | plant process owner confirms the problem and the moment of use |
| 22 | propose signals, write the missing-signal table | label, path, rule used | domain expert on the running dashboard; verdict of `od-data-availability-check` |
| 23 | generate dashboard, click-dummy, analyser proposals | tag-to-requirement and panel-to-query binding | domain expert at the point of use; requester approves requirements |
| 24 | draft calculation rows, flag missing baselines | baseline, factor, ledger row | plant controlling accepts baseline and factor; ranking sign-off |
| 25 | assemble scenario tables, completeness check | benefit rows, quote, frame-contract id | scope and scenario decision; submission and approval |
| 26 | monitor utilisation, draft savings evaluation | usage source, forecast and project register | plant owner confirms adoption; savings status confirmed |
| 31, 32 | check tool against fit criteria | criteria source, tool status and date | fit verdict, tool decision |
| 3a4-3a6 | draft deployment set, checklists | template, sourcing route, repo folder | Cyber Security sign-off; deployment into the shared platform |
| 3b4-3b6 | draft tag list, flow documentation, cyber-security package | guide step, controller data, document list | Cyber Security approval; procurement; connection |

## 3 What stays a human decision

- Accepting a requirement, problem statement or utilisation moment.
- The domain-expert verdict on a generated or proposed signal set and dashboard.
- Choices the context cannot derive (lane, depth, language, audience).
- Priority, ranking, go / no-go, kill or cancel, and the Lead-change label.
- Assumptions, baselines and factors of a benefit; whether a savings status is confirmed; "no potential".
- Scope and scenario of a decision; anything that commits budget; submission of a request.
- Any machine connection, PLC write or parameter change; Cyber Security sign-off (no expedited path).
- Deployment into a shared platform; promotion to the catalog (`od-use-case-promotion`).
- Choice of facilitation format and the order of a workshop.
- Escalation wording to a forum.

## 4 Hand-over format

Use the step card ([`../assets/ai-step-card.md`](../assets/ai-step-card.md)): output, evidence table,
open items, missing-input table, the human who gates, the decision still needed. The receiving skill
reads the card instead of re-asking.
