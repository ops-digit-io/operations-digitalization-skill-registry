---
type: Skill Asset
title: IT demand package
description: The one-document package for IT demand management or an external developer, with OD's parts pre-wired to the skills that produce them and every IT-side field marked as missing. Copy one per demand.
resource: ../procedure.md
status: draft
tags: [all, practice]
---
# IT demand package

Draft. A human submits it. The evaluation board decides. This package does neither.

```text
0  HEADER
   Demand in one paragraph (what the plant needs done, not the tool):
   Route:  3a.3 external development / 3a.4 integrate a foreign app
   Plant sponsor (role):               Plant owner (role):           OD owner (role):
   Version / date:                     Submitted by a human on ⟨date⟩ - not yet

1  WHY IT (the rule that sends it here)
   Which platform OD does not own is touched:           Source: Decision rights, demand route
   Spend gate (eCR) needed in parallel?  yes / no       Threshold step: ____ (dept-decision-rights)
   Tool or system rollout decision involved?  yes / no  (OD lead decides, in tandem with the IT-responsible role of the business side)

2  REQUIREMENT                       (funnel-requirements)
   Requirement link (ten sections) / epic and stories link:

3  FIT-CHECK VERDICT                 (invest-screen)
   Verdict:      inside lean footprint / outside -> tool-rollout decision / substitute available ____
   Four assessment questions answered (existing app? supported? licence? footprint?):  yes / which not

4  BUSINESS CASE                     (bc-build)
   Every figure: value ____ source ____ capture date ____ ; none without; "to be collected" otherwise

5  APPROVAL ROUTE                    (dept-decision-rights)
   Decision / owner / mode / threshold / authority level:          Gate recorded as a dependency on the record:

6  ACCEPTANCE CRITERIA               (deploy-acceptance, drafted)
   Protocol link:   defined before the build: yes / no

7  CYBER SECURITY - OPEN POINTS      (deploy-cybersec)
   Network status: Standalone / IT / OT/IT / OT      Writes to a machine?  yes / no (yes -> segmentation review)
   External connection?  yes / no                    Sign-off: requested ____ / granted ____  (human-only)
   Points still open:

8  FOREIGN APP DESCRIPTION  (3a.4 only; fill with the legacy list's own columns, see references/external-build-and-foreign-app-inputs.md)
   Name / version / supplier:                 Category / functional mapping:
   Production criticality:                    Licence required:  ____ (unknown stays unknown)
   Support concept / availability / supplier status:           Cyber-security status:
   Interfaced machines:                       Divisional standard or local application?
   Reads: ____  Writes: ____  Direction: ____  Where it runs / who runs it: ____
   Data object owned, and any second source for it: ____

9  EXTERNAL BUILD INPUTS  (3a.3 only)
   Source owned by the department?  yes / no (one of the three onboarding scenarios)
   Spec format IT accepts / environment access / security terms:   ⟨to be supplied⟩ (IT demand management, Cyber Security)

10 IT-SIDE FIELDS                      ⟨IT demand form fields - to be supplied⟩ ; board criteria ⟨⟩ ; rhythm ⟨⟩ ; contact (role) ⟨⟩

11 THE KIND OF ASK (so the board can place it): licences or budget / platform integration / capacity / delivery predictability

12 OPEN ITEMS WITH OWNERS
   | item | who can close it (role) | needed by |
```

## Reading the package (checks before handing over)

| Check | If it fails |
|---|---|
| Parts 2 to 4 exist | stop and name the missing part; the front-end is incomplete |
| Part 4 has no figure without source and date | remove the figure, mark "to be collected" |
| Part 8 has no field filled from a guess | mark it ⟨missing⟩ with the person who can close it (requester, plant IT, supplier) |
| Part 7 does not state a sign-off as granted | only the Cyber Security sign-off itself can be marked granted, by its owner |
| Route is 3a.3 or 3a.4 | for 3a.1 and 3a.2 this package is not needed |
| Demand stays inside platforms OD owns | do not use this package |

After the board's decision: `deploy-appstore` (gate) and `deploy-handover` (rollout).
