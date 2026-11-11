---
type: Skill Asset
title: First aid request
description: The structured problem-capture form for a Process First-Aid Kit request, with the S.M.A.R.T. restatement, data scenario, routing decision and hand-over - a working version of the template the lane documents leave open.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice, template]
---
# Process First-Aid request — ⟨plant⟩ — ⟨date⟩

Working version; the official template is open (`SKILL.md`). Fill it with the requester, in order.
Write `⟨not recorded⟩` when a field has no answer. Roles only, no names, no hostnames or addresses.
Authority: draft. Nothing here commits cost, installation or a connection.

## 1 · Request

| Field | Entry |
|---|---|
| Received on / through which channel | ⟨⟩ |
| Plant / area / line / machine | ⟨⟩ |
| Requester (role) / plant owner of the answer (role) | ⟨⟩ / ⟨⟩ |
| Type | ⟨ramp-up support · trouble shooting · other⟩ |
| Urgency and why (what happens if nothing is done) | ⟨⟩ |

## 2 · The symptom in plain words

| Question | Answer |
|---|---|
| What is going wrong, as someone on the shop floor would say it? | ⟨⟩ |
| Since when, how often, on which shifts or products? | ⟨⟩ |
| Is it one event or recurring? | ⟨once · recurring: how often⟩ |
| What has already been tried? | ⟨⟩ |
| What is measured today, by which system or by hand? | ⟨⟩ |
| What decision will the answer inform, and who takes it? | ⟨⟩ |

## 3 · Made S.M.A.R.T. (working expansion, see `SKILL.md`)

| Element | Restatement |
|---|---|
| Specific: which process, machine, product, defect | ⟨⟩ |
| Measurable: which quantity shows the symptom, with unit | ⟨⟩ |
| Achievable: can a dataset answer it, with what data | ⟨⟩ |
| Relevant: why it matters (quality, output, safety, cost), as the requester states it | ⟨⟩ |
| Time-bound: period to analyse, and when the answer is needed | ⟨⟩ |

**Question in one sentence that the data can answer:** ⟨⟩

## 4 · Data and scenario

| Field | Entry |
|---|---|
| Signals or records needed | ⟨⟩ |
| Available on the data platform? (`mi-data-availability`) | ⟨yes · partly · no⟩ |
| Coverage gaps found (signals, classes, periods, lines) | ⟨⟩ |
| Scenario | ⟨A: edge platform and compliant network available · B: not available, device at the machine and manual transfer · unknown, who checks⟩ |
| PLC type, if scenario B | ⟨⟩ |
| Cyber Security status for any connection | ⟨not needed · needed, not requested · requested ⟨date⟩ · approved⟩ |
| Cost indication, if asked | ⟨"any indication in a tool deck is not a quote; OD lead decides"⟩ |

## 5 · Route

| Test | Result |
|---|---|
| One-off or recurring? | ⟨⟩ |
| Does the answer need data that is not available? | ⟨⟩ |
| Does it need a system outside the lean standardized footprint? | ⟨⟩ |
| Is more than one line, shift or plant asking? | ⟨⟩ |

**Route chosen** (one): ⟨Analytical Support (`funnel-first-aid`) · Information Integration lane as data gap · Intake (`dept-intake`) · refused with reason · returned to requester with missing items⟩

**Reason, in one or two sentences:** ⟨⟩

## 6 · Hand-over

| Item | Entry |
|---|---|
| To (role) | ⟨⟩ |
| Attached | ⟨this form · data availability result · photos or sketches of the setup⟩ |
| Next step and date | ⟨⟩ |
| Requester informed on | ⟨date⟩ |
| Promotion watch | ⟨if the insight is reused, who checks for recurring value and when⟩ |

## 7 · Open points

⟨what could not be answered, and who can supply it⟩
