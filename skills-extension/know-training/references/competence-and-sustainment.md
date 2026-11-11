---
type: Skill Reference
title: Competence and sustainment
description: How competence is evidenced and confirmed by the plant, the single-point-of-failure rule, a proposed hand-down from key user to key user, and what keeps the competence alive after the trainer leaves.
resource: ../SKILL.md
status: draft
tags: [project-support-consultancy, practice]
---
# Competence and sustainment

## 1. Competence is a thing a person does, not a session they attended

The call decks record training as counts of formats, sessions and participants. Attendance says nothing about competence, and a deck planned to "improve
recorded training sessions", so even attendance was weakly recorded. This skill therefore writes each
competence as an observable statement and asks for evidence.

**Evidence ranking.** The rollout uses the evidence tiers that `deploy-handover` already defines, strongest
first, so the two skills read the same way:

1. **System record** - a dashboard view count, a query log, an edit history, a saved flow or protocol with the
   trainee as the author.
2. **The named plant owner's dated statement** - "I saw the trainee do X on date, in a real shift."
3. **A third party's observation** - a visit, a Gemba walk, a colleague.

Not evidence: that the session took place, that the material was sent, that nobody complained. Record the tier that
was available; never upgrade it.

## 2. The plant confirms, the assistant drafts

The skill map sets the authority: *draft the training package and competence checklist; the plant confirms
competence.* In practice:

| Step | Who |
|---|---|
| Draft the package and the checklist | The assistant, reviewed by the IIAE |
| Deliver the sessions | The trainer role (⟨who⟩) |
| Mark a competence confirmed, with evidence | The **plant owner** of the solution, by role, with a date |
| Record the checklist as input to the handover | The DBVE or IIAE, from the confirmed checklist |

The assistant leaves the confirmation fields empty and never infers one.

## 3. The single-point-of-failure rule

The risk register lists "Limited internal IT knowledge (data platform, MDA/PDA)" with the early indicator
"dependence on few individuals", the countermeasure "training; knowledge sharing via COP" and the escalation
trigger "single point of failure identified". Applied to a plant:

- Every **critical** competence (the ones marked critical on the checklist) must be confirmed for **at least two**
  people, or the gap is reported as a single point of failure. "Two" is the minimum that removes a single point of
  failure; it is not a recorded department target. ⟨Target number of key users per plant⟩ is open.
- A person who leaves the role takes the competence with them, so the checklist carries a **date** and a
  **re-confirm** trigger (section 5).
- The same logic applies one level up: the Information Integration lane has 3 IIAE roles with open positions in
  Asia and Americas (`capabilities.md`), so the plant cannot depend on the IIAE for routine questions.

## 4. A proposed hand-down model (proposal, not a department standard)

The sources show OD running workshops and trainings itself. They do not say whether a trained plant key user may
train colleagues or other plants, and this is the core of decentralization. A proposal for the OD lead to confirm:

| Stage | Who teaches | Who confirms | Condition |
|---|---|---|---|
| 1. First key users | OD (IIAE or DBVE) at the plant, with the real solution | The plant owner | The module's hands-on form is done on the real screen or machine |
| 2. Further staff at the same plant | A confirmed key user | The plant owner | The key user has the same competence confirmed and the trainer role is named on the package |
| 3. Another plant | A confirmed key user, with OD present on the first run | The receiving plant owner | ⟨Allowed or not⟩ - OD lead decision; COP is the forum where it is shared |

If the OD lead rules that stage 3 is not allowed, the package remains valid for stages 1 and 2.

## 5. Keeping it alive

| Mechanism | What it does | Source |
|---|---|---|
| Utilization rate on the Digitalization Scorecard | Carries the Reinforcement element after the trainer is gone | `deploy-handover`, `metrics-scorecard` |
| Re-confirm trigger | A competence is re-confirmed when the person changes role, when the solution changes version, or when the data path changes | proposal; ⟨interval⟩ is open |
| COP as the sharing forum | Technical issues and connector or data-model updates are brought to the COP; the risk register names COP as the knowledge-sharing channel | `06-operating-rhythm.md`, `09-risks.md` |
| Recorded sessions | A session record (date, module, trainer role, attendee roles, evidence) so attendance is no longer the only trace | a call-deck plan; ⟨system where it is kept⟩ is open |

## 6. When competence is not confirmed

1. Do not mark the solution as adopted. Hold the handover at the Knowledge or Ability element.
2. Check what the trainee could not do: a content gap (repeat the module at the real screen), a Desire gap (nobody
   asked for it - the ADKAR barrier point, `deploy-handover`), or an infrastructure gap (the plant cannot yet
   do it, for example because the network is not ready).
3. Report a single point of failure or an unconfirmed critical competence to the OD lead through COP.
