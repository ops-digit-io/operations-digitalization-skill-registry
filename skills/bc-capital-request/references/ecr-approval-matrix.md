---
type: Skill Reference
title: Ecr approval matrix
description: "Who approves an eCR, step by step, in the recorded approval matrix (OESL stand-alone, 2026-03-02): local management, functional reviews, central management, by amount tier and by case type. Roles only; the amounts stay in the source."
resource: ../SKILL.md
status: draft
tags: [capital-request, ecr, approval, decision-rights]
---
# eCR approval matrix

The recorded approval chain for an electronic capital request. It has **three amount tiers**: below the lower
threshold, from the lower threshold, from the upper threshold. The amounts are company figures and are not repeated
here: read them in the source document named above. The matrix is dated 2026-03-02 and was made for OESL
stand-alone; confirm with the OD lead and Finance that it still applies under neuwerk before quoting it in a package.

`x` = approver in that tier, `-` = not involved in that tier. Names are not recorded here; the source holds them.

| Step | Area | Function | When | Lower tier | Middle tier | Upper tier |
|---|---|---|---|---|---|---|
| 1 | Management approval, local | Plant Controlling | always | x | x | x |
| 2 | | Plant Manager | always | x | x | x |
| 3 | | Financial Manager | always | x | x | x |
| 4 | Functional review, finance | Investment Controlling | always | x | x | x |
| 5 | Functional review, central functions | ESH | always | x | x | x |
| 6 | | Tax | if tax relevance | x | x | x |
| 6 | | Legal | if legal relevance | x | x | x |
| 6 | | IT Controller | if IT invest | x | x | x |
| 6 | | Head of Manufacturing & Engineering | always | x | x | x |
| 7 | | Head Operations Controlling | if not expansion, R&D, real estate or IT | - | x | x |
| 7 | | Head of Business Controlling | if expansion | - | x | x |
| 8 | Management approval, central | Real Estate (CREM) | if real estate | x | x | x |
| 8 | | Head of R&D | if R&D | x | x | x |
| 8 | | CIO | if IT invest | - | x | x |
| 8 | | Head of Business | if expansion | - | x | x |
| 8 | | COO | if not expansion, R&D, IT or real estate | - | - | x |
| 9 | | CFO | always | - | - | x |
| 10 | | CEO | always | - | - | x |
| read | | Head of Purchasing, Financial Reporting | read access | (x) | (x) | (x) |

## How to use it in a package

1. Read the amount against the tiers in the source; write the tier, not the amount, in the route line.
2. Classify the case: IT invest, expansion, R&D, real estate, or none of these. The class switches steps 6 to 8.
3. List the approvers for that tier and class, by role, in the package (`assets/capital-request-package.md`).
4. An OD digitalization investment with software or hosting is usually an **IT invest**: IT Controller (step 6)
   always, CIO (step 8) from the middle tier. Flag it, and open the IT demand in parallel (`deploy-it-demand`).
5. The decision-rights row "digitalization investment planning" (OD lead with BA Operations, consultation,
   approval yes) sits **before** this chain: the OD lead recommends, the chain approves (`dept-decision-rights`).
