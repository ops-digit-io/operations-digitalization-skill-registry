---
type: Skill Asset
title: Cybersec signoff package
description: The request package for a Cyber Security / OT sign-off of a machine connection or an app deployment, with a wait-state log and an answer record - fill once per case.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Cyber Security sign-off package - ⟨plant⟩ · ⟨machine or app⟩

Draft by the assistant. Submission and the sign-off are human. Fill from the sources named in
[`../references/package-contents.md`](../references/package-contents.md). Leave `⟨…⟩` where unknown. **No
credentials, addresses, certificates or tokens in this document.**

| | |
|---|---|
| **Case type** | ⟨A machine connection · B app deployment⟩ |
| **Lane step** | ⟨1b order and connect · 3a deploy · 3b acceptance and live⟩ |
| **Plant / sponsor role** | ⟨plant · Plant ME / Plant IT role⟩ |
| **Responsible OD role** | ⟨IIAE · OD lead⟩ |
| **Drafted on / by** | ⟨date⟩ · ⟨assistant, reviewed by role⟩ |
| **Treated as external?** | ⟨yes · no · asked, answer pending⟩ - basis: ⟨…⟩ |

## 1 · What is being connected or deployed

⟨Machine: name, EQ id, vendor, PLC model. App: name, owner, version, sourcing route.⟩

## 2 · Data path and direction

⟨machine → connector → edge or server → platform → offload. What is read; what, if anything, is written
back to the controller. For an app: data read and written, against the systems of record.⟩

## 3 · Network position and access

⟨Where it sits; how it reaches the platform; network separation status. Which role holds endpoint credentials
and certificates (not the values).⟩

## 4 · Known security points

| Point | Status | Source |
|---|---|---|
| ⟨firmware patch needed · security-compliant communication available · flat network · none known⟩ | ⟨⟩ | ⟨barrier-classes.md · machine record⟩ |

## 5 · Cover and dependencies

| Item | Entry |
|---|---|
| Wave-level sign-off in force | ⟨reference and listed scope · none⟩ |
| Investment approved | ⟨yes, ref · no⟩ |
| Decision request | ⟨link to the filled decision request⟩ |
| Acceptance protocol drafted | ⟨link⟩ |

## 6 · Questions for Cyber Security

| # | Question | Role that must answer |
|---|---|---|
| 1 | ⟨e.g. does this case fall under an existing sign-off?⟩ | ⟨⟩ |

## 7 · Wait-state log

| Date | Event (submitted · reminder · escalated · answered) | By (role) | Next check |
|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

Escalation rule: a technical item unresolved beyond one COP cycle goes to the OD lead (escalation role per `od-decision-routing`); a security gap on a connected
asset goes to the OD lead and Cyber Security at once.

## 8 · Answer record (filled only when given)

| Field | Entry |
|---|---|
| Answered by (role) | ⟨⟩ |
| Date | ⟨⟩ |
| Scope - machines or app version | ⟨⟩ |
| Outcome | ⟨granted · granted with conditions · refused⟩ |
| Conditions | ⟨⟩ |
| Validity | ⟨⟩ |
| Evidence reference | ⟨where the written answer is kept⟩ |

## 9 · Definition of done

- [ ] Every item above is sourced or a visible `⟨…⟩`
- [ ] No secret appears in this document
- [ ] Decision request filed; sign-off recorded as a dependency on the case
- [ ] Nothing is connected or deployed before section 8 shows an outcome
- [ ] Granted answer attached to the acceptance protocol evidence
