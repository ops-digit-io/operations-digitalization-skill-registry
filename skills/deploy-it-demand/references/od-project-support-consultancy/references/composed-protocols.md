---
type: Skill Reference
title: Composed protocols
description: Which real protocol in which composed skill answers each step of this lane's happy path, so a project is tracked against an actual document rather than a placeholder.
resource: ../procedure.md
status: stable
tags: [project-support-consultancy, lane]
---
# Composed protocols

This lane does not author its own artefact per project — it routes a project through four
protocols that now exist in the skills it composes into. Use the real file, not this lane's
own summary of it.

| Step | What it needs | Real protocol |
|---|---|---|
| 2 — Kick-off; scope and requirements | A requirement spec | `funnel-requirements`'s [`assets/requirement-template.md`](../../../../funnel-requirements/assets/requirement-template.md)) |
| 5 — Acceptance testing | A signed acceptance protocol | `deploy-acceptance`'s [`assets/acceptance-test-protocol.md`](../../../../../skills/deploy-acceptance/assets/acceptance-test-protocol.md) — six sections, §6 (handover readiness) is what step 6 reads next |
| 6 — Ensure use cases are integrated into daily processes | Adoption evidence, not a delivery date | `deploy-handover`'s [`references/evidence-of-adoption.md`](../../../../../skills/deploy-handover/references/evidence-of-adoption.md) (three tiers, strongest first) and its [`assets/handover-protocol.md`](../../../../../skills/deploy-handover/assets/handover-protocol.md) |
| 7 — Report progress and impact | A decision record if anything is gated | `dept-decision-rights`'s [`assets/decision-request.md`](../../../../../skills/dept-decision-rights/assets/decision-request.md) |

**Why this lane does not duplicate any of the four.** A protocol copied into a second
skill drifts from the original the first time either one is updated — exactly the failure
mode `mi-equipment`'s Route A/B merge was built to avoid. Point at the file,
not at a summary of it.

## What is still genuinely open, not answered by any of the four

- **Kick-off agenda template** (step 2's own agenda, separate from the requirement spec
  it produces) — no dedicated template found anywhere in the registry.
- **Application-consultancy session template** (step 4) — PS-04 "application consulting"
  was never built as its own skill (`docs/knowledge-base-alignment.md` still lists it "not built");
  this lane's own step 4 is as far as that work goes today.
- **Tool/licensing decision owner** — `dept-decision-rights`'s "Tool/system rollout" row
  names the IT-responsible role of the business side as the counterpart in the tandem; this lane's wait state
  uses the same counterpart.
- **The end-to-end flow owner** — tracked separately in `registry.yaml`'s `open_gaps`,
  unchanged by this pass.
