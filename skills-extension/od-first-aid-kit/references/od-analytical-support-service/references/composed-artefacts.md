---
type: Skill Reference
title: Composed artefacts
description: Which composed skill's real, built asset answers each happy-path step, now that those skills have gone deep — so this lane page routes to them instead of carrying its own unresolved placeholder for the same thing.
resource: ../procedure.md
status: stable
tags: [analytical-support-service, lane]
---
# Composed artefacts

This lane page is a router, not a builder — each step's real output lives in the skill it
hands off to. The ones below are built deep enough to name directly.

| Step | Composed skill | The real artefact |
|---|---|---|
| 2 · Check data availability | `od-data-availability-check` | `assets/data-availability-verdict.md` — the six-step verdict, run via `scripts/check_availability.py` |
| 4 · Build the asset | `od-analytics-asset-build` | `assets/asset-build-protocol.md` — asset type, ritual, data path and utilization expectation |
| 6 · Promote to standard use case | `od-use-case-standardization` | `assets/standardization-review.md` |

**What is still genuinely open, not just unlinked:** the Process First-Aid Kit's own
template, a target for analytics-asset output volume, and trackers for ad-hoc turnaround
and promotion rate. None of the three composed skills above answer these — they are
different metrics, not the same one under a different name. Checked, not assumed.
