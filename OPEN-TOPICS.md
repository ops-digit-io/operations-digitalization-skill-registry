---
type: Design Record
title: Open topics
description: "All open topics of the skills in one file, moved out of the skills; the skills themselves carry no open-topic sections."
status: draft
owner: human:jakob.gabriel
tags: [open-topics, working-file]
generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }
---
# Open topics

All open topics of the skills in one place. The skills themselves carry none: no "open points", "still open" or "to confirm" section remains in `skills/`. Each entry below is moved verbatim from the section named under it; the skill it concerns is the heading.

The inline markers `⟨to confirm⟩` and `⟨to be collected⟩` inside the skill text and the open-items fields of the output templates in `assets/` are not listed here: they mark a value a user still has to supply in a concrete package, not an open topic of the skill.

Skills with open topics: 20. Sections moved: 41.

## bc-build

### What is still open

Source: `skills/bc-build/references/review-checklist.md`

The specific reasons a *particular* row gets challenged or bounced at the SPRINT review
itself — as opposed to why the ledger is thin in the first place — are not in this
record. If there is a recurring SPRINT objection (a category SPRINT routinely does not
accept, a methodology SPRINT routinely asks to redo), add it here directly; the above
explains the upstream cause, not the review gate's own criteria.

## bc-capital-request

### What is still open

Source: `skills/bc-capital-request/SKILL.md`

- ⟨System the eCR is filed in and who may file⟩: not in any source; the form content is the builder's backbone. OD lead with BA Operations / Finance.
- ⟨Whether the 2026-03-02 approval matrix (OESL stand-alone) still applies under neuwerk⟩. Finance.
- ⟨Approval lead time⟩: the skill-map queue is a placeholder. OD data.
- ⟨Cost rates (people, hardware, compute) the department should use⟩: the knowledge base cases use their own FTE rates; none is
  an OD standard. Finance.
- ⟨The investment planning template⟩ and ⟨the use-case business-case template⟩ (`00-core/15-resources.md`). DBVE / OD lead.
- ⟨Whether this skill and `bc-cost` merge⟩. OD lead.

### Pre-approval route for small spend: open points

Source: `skills/bc-capital-request/references/spend-route.md`

⟨whether the 25 kEUR central-approval limit is the Lane 1b "lightweight approval" limit⟩ · ⟨which route the 25 to 100 kEUR band takes⟩ · ⟨what "eCR" stands for: this skill reads it as electronic capital request, while the bundle's `10-Department/Decision rights.md` says engineering change request; confirm with Finance⟩.

## catalog-guardrails

### Open

Source: `skills/catalog-guardrails/references/technical-guardrails.md`

- ⟨Whether the newer Grafana major version used at one plant is the target platform or an exception⟩ - SPEC-01 / SPEC-04 open question; affects G12 for plugin panels.
- ⟨Whether the community chart plugin in use is on the approved list⟩ - SPEC-03 Q2; until then a plugin panel in a self-served screen is a warn.
- ⟨Who owns the central dashboard repository and the signal record⟩ - SPEC-04 Q3, SPEC-02 D-01.
- ⟨The dashboard language rule⟩ (titles with non-Latin characters exist) - SPEC-03 Q1.

## catalog-systems

### Open

Source: `skills/catalog-systems/references/tool-boundaries-mda-mes-mil-msb-qfpr.md`

- ⟨Which MDA/PDA version is the standard for a new plant⟩ - OD lead.
- ⟨Whether the image-library pilot has a funded path to productive⟩ - OD lead, IIAE.
- ⟨Where performance analysis sits between MES and the capability services⟩ - the process-chain note leaves this open.

### Open

Source: `skills/catalog-systems/references/tools-and-footprint.md`

- ⟨Which plants have no edge platform at all⟩ - a plant with no row in the tool overview is unknown, not a "No".
- ⟨Licence position of the aggregation server per PLC family⟩: the product needs a licence per family unless the extended
  suite is in place (`mi-equipment`, `softing-datafeed.md`); the knowledge base does not say which plants hold which.

### Open

Source: `skills/catalog-systems/references/validated-routes.md`

- ⟨The list of purchasable kits per route, prices and lead times⟩ - OD lead, IIAE, procurement; not in the knowledge base notes read.
- ⟨Why some integrated machines carry no method⟩ and ⟨whether machines under `EVALUATION ONGOING` will land on edge or
  aggregation⟩ - IIAE.
- ⟨Whether the guide's `TODO` for Beckhoff and Omron on the edge is still current⟩ given that machines are recorded as
  integrated that way - IIAE.

## catalog-usecase

### Open points - what only the OD lead can supply

Source: `skills/catalog-usecase/SKILL.md`

- ⟨Where the catalog lives and in what form (list, library, portal)⟩ and ⟨who maintains it⟩. Partial answer from the knowledge base: the nearest thing today is the SharePoint list `UseCase-Library` (the CSP field lives there) read through the eleven template pages in `Graph/Use Case Views`; no plant-facing portal is recorded.
- ⟨Whether a recorded CSP `Yes` is the right threshold for self-service⟩, given how few entries may have one.
- ⟨Which entries with a `Yes` a plant can take as is today⟩: conditions 3 and 4 (standardized signals, plant owner and handover) are not recorded in the entries - IIAE and plant owner.
- ⟨How a plant reaches the catalog⟩ and ⟨who may add an entry⟩.
- ⟨The standardized-system list itself⟩: kits, prices, lead times, validated plants, and ⟨who maintains it⟩. Route evidence is in `references/validated-routes.md`; the kit side is open.
- ⟨Whether "standardized" means a validated route plus a purchasable kit⟩.
- ⟨The Cyber Security sign-off standard document⟩ - listed in the bundle as still to be collected.
- ⟨Further technical guardrails⟩: naming, refresh interval and unit rules are proposed in `references/technical-guardrails.md` (SPEC-03, draft); **access rights and performance** are not recorded (performance of the proposed single-read function on the real telemetry table is "not known and must be measured", SPEC-02 D-04).
- ⟨Which guardrails block go-live and which only warn⟩. A proposal exists in SPEC-03 section 6 (S-01 to S-03, S-06, S-07, S-10, S-15, S-17), applied in `references/technical-guardrails.md`. G1 to G7 are "block" until the OD lead says otherwise.
- ⟨The utilization target after go-live⟩ for a self-served use case: the field is recorded, not a target.
- ⟨Who OD names as the contact when a guardrail fails⟩: nearest recorded answer is by role (IIAE, DBVE, OD lead, Plant IT) in `references/failure-cases-and-routing.md`.

### Open

Source: `skills/catalog-usecase/references/legacy-application-position.md`

- ⟨Which plant runs which application⟩ is in the individual notes (a plant field), not in the aggregate - read the note when
  a specific plant is concerned.
- ⟨Whether "licence unknown" means not asked, or not held⟩ - plant IT, OD lead.

### Open

Source: `skills/catalog-usecase/references/library-and-csp-state.md`

- ⟨Whether library entries without a recorded decision are undecided, not applied, or lost in the export⟩ - OD lead.
- ⟨Why only library entries carry the CSP field⟩ and whether a dashboard family can be put through the gate - OD lead.
- ⟨The date and forum of each CSP decision⟩ - not in the notes read; the CSP call (see `dept-decision-rights`) would hold them.

### Open

Source: `skills/catalog-usecase/references/template-coverage.md`

- ⟨Which of the eleven templates the OD lead wants offered for self-service first⟩ - the live coverage shows where the data is
  thickest, not what OD has decided.
- ⟨Whether the `scalable` flag may serve as the entry gate for candidates⟩ - OD lead.

## comms-brief

### Open points

Source: `skills/comms-brief/references/department-formats.md`

- Whether the January 2026 initiative produced a result outside the deck. ⟨to confirm⟩
- Whether the Yokoten database, the CoP best-practice slot and the OPEX exchange call are still in use. ⟨to confirm⟩
- Which of these formats Internal Communications will accept as they are. ⟨to confirm, from the IC brief⟩

### Open points (to fill from the Internal Communications brief)

Source: `skills/comms-brief/references/ic-handover.md`

| # | Question | Answer |
|---|---|---|
| 1 | Which IC contact or intake channel receives a story (a role, not a name)? | ⟨to confirm⟩ |
| 2 | Which channels exist for the four audiences (plants and key users, BA Operations leadership, all employees, OPEX and PPI/ME)? | ⟨to confirm⟩ |
| 3 | Lead time from brief to publication? | ⟨to confirm⟩ |
| 4 | Does IC have its own template or review route that replaces `comms-brief.md`? | ⟨to confirm⟩ |
| 5 | Which brand and tone rules apply, and is the neuwerk template to be used? | ⟨to confirm⟩ |
| 6 | Is there an approval by IC leadership or a second language needed? | ⟨to confirm⟩ |
| 7 | What reach or response data does IC give back after publication? | ⟨to confirm⟩ |

## comms-followup

### Open points

Source: `skills/comms-followup/references/feedback-routing.md`

- How long a story stays current before it needs a review. ⟨to confirm⟩
- Whether Internal Communications can correct or withdraw a published item, and how fast. ⟨to confirm, from the IC brief⟩

## comms-showcase

### Open points

Source: `skills/comms-showcase/references/readiness-gate.md`

- Whether OD needs the OD lead's sign-off for every story or only for those with a figure. ⟨to confirm⟩
- Which Internal Communications review applies on top of this gate. ⟨to confirm, from the IC brief⟩

## deploy-appstore

### Open - what only the OD lead can supply

Source: `skills/deploy-appstore/SKILL.md`

- ⟨The target platform⟩ and ⟨the deployment procedure⟩, including who holds deploy rights.
- ⟨The Cyber Security requirements for an app⟩ and ⟨the lead time⟩.
- ⟨The release cadence⟩ - the bundle says "per release" without a rhythm; neither the AI deck nor the initiative note gives one.
- ⟨The pilot's scope, plants and exit criteria⟩ - the department deck marks the GitOps deployment as a pilot and says no more.

### Open

Source: `skills/deploy-appstore/references/app-manifest-and-release-gate.md`

- ⟨Containerization, image and registry rules, resource limits⟩ - OD lead, IT platform.
- ⟨Who holds deploy rights on the app store and on the plant runtime⟩.
- ⟨Cyber Security requirements for an app⟩ and ⟨lead time⟩ - owner of the Cyber Security standard (listed in the bundle as still to be collected).

### Open

Source: `skills/deploy-appstore/references/platform-and-pilot-status.md`

- ⟨Release cadence of the app store⟩ - the systems-of-record note says "per release" without a rhythm; the deck gives none.
- ⟨Scope and plants of the GitOps pilot⟩ and ⟨exit criteria of the pilot⟩ - OD lead.
- ⟨Whether the validation plan's adoption criterion has been tested⟩ - OD lead.

## deploy-handover

### What is still open

Source: `skills/deploy-handover/references/od-impact-evaluation/procedure.md`

- ⟨n weeks live before evaluation⟩ — plan UC-06 leaves it open. Supplier: OD lead.
- ⟨Impact evaluation template⟩ — `tasks.md` of the lane says "template — to confirm"; the record in
  `assets/` is the working version, built from OD's own utilization template and the Canvas success
  criteria. Supplier of the official one: DBVE.
- ⟨SPRINT acceptance criteria⟩ — no source read says what SPRINT routinely rejects (also open in
  `bc-build`). Supplier: whoever attends the SPRINT review.
- ⟨Utilization target⟩ — "to confirm" in the lane metrics. Supplier: OD lead.
- ⟨Plant-side owner for confirmation⟩ — the department has no plant-side lane owner yet (OD skill
  map, open gaps). Supplier: OD lead.

## deploy-it-demand

### Open - what only the OD lead and IT can supply

Source: `skills/deploy-it-demand/SKILL.md`

- ⟨The OD store: its id and repository URL⟩ - decided: OD drafts in its own OpenSpec store; the OD lead sets it
  up once (a Git repository with `openspec/`; no CLI needed) and names it here.
- ⟨How IT takes a change from the OD store: `references:` in its repositories, or a copy into its own store⟩ -
  the meeting asked IT to define where each artefact is stored and exchanged (IT).
- ⟨Published technology guardrails, sourcing criteria, ownership gates, platform-level Cyber Security
  model, data and interface catalog structure⟩ - open IT action items; the annex marks each.
- ⟨Whether IT adopts OpenSpec itself⟩ - proposed here; if IT keeps its own demand form, the absorbed IT
  demand package carries the same content.

### Open IT action items that will firm the inputs

Source: `skills/deploy-it-demand/references/it-expected-inputs.md`

| Action | Owner (as recorded) | Firms input |
|---|---|---|
| Structure and contents of the data and interface catalogs | IT | 7, 8 |
| Consolidate the artefacts IT expects from the funnel and where each is stored or exchanged | IT | all; the receiving location for OpenSpec changes |
| Cyber Security pre-evaluation approach, aligned with Cyber Security | OD lead, IT | 4 |
| Platform-level Cyber Security approval model | IT | 4 |
| Ownership and handover gates | IT, OD lead | 11 |
| Technology guardrails (stacks, Kubernetes / CMO, interfaces, OT) | IT, OD | 3 |
| Recurring application self-assessment | IT, OD lead | 11 |
| CMO roadmap and target blueprint | IT | 3 |
| Minimum and maximum deployment scenarios per use case | OD lead, IT | 9 |
| Build / buy / guided delivery sourcing criteria with TCO | IT, OD lead | 10 |
| Requirements and technology baseline for the legacy applications | unassigned | 13 |

### Open - what only the OD lead can supply

Source: `skills/deploy-it-demand/references/it-demand-package/procedure.md`

- ⟨IT's demand form⟩ and ⟨the evaluation board's criteria and rhythm⟩ - searched in the bundle, the knowledge base's AI decks and the initiatives on 2026-11-05; the sources carry the route and OD's asks, not the form.
- ⟨Who the contact in IT demand management is⟩ and ⟨the usual lead time⟩ beyond the flow's "weeks".
- ⟨What an external developer must receive⟩ (spec format, environment access, security terms).

### Open

Source: `skills/deploy-it-demand/references/it-demand-package/references/external-build-and-foreign-app-inputs.md`

- ⟨IT's form fields, criteria, rhythm, lead time, contact⟩ - see `it-touchpoints.md`.
- ⟨The format of the specification IT accepts for an external build⟩.
- ⟨Whether a foreign app that is already in the legacy list needs a new demand or a change request on the existing entry⟩ - OD lead, IT.

### Open

Source: `skills/deploy-it-demand/references/it-demand-package/references/it-touchpoints.md`

- ⟨IT's demand form fields⟩, ⟨the evaluation board's criteria and rhythm⟩ and ⟨the usual lead time⟩ - not in any source read. The deck, the bundle and the knowledge base carry the *route*, not the form. Owner: OD lead, with the IT demand management contact.
- ⟨The IT contact in demand management⟩ - no source names a role or a mailbox for it.

### What is still genuinely open, not answered by any of the four

Source: `skills/deploy-it-demand/references/od-project-support-consultancy/references/composed-protocols.md`

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

## dept-context

### 6. The open-gaps list as a work queue

Source: `skills/dept-context/references/swot-and-dependency-seams.md`

The README closes with a numbered list of gaps: named owners behind role labels, targets and thresholds, a metric with no defined
source, adoption feedback, system interface detail, data-platform detail, decision counterparts, naming after an organisation
rename. Treat that list as the **queue of questions an agent may put to the OD lead**, ranked by how many skills carry a `<...>`
for the same gap. When a gap is closed, the closing note goes to the source note first, then into the skills that carry the
placeholder (`dept-context-freshness` finds them).

### Pitfalls and open points (open-point bullets)

Source: `skills/dept-context/SKILL.md`

- **Open points (to confirm):** Databricks access paths, workspace and container naming, catalog layout; MPEE expansion; named owners per lane (role labels only today); lane target lead times; budget figure; MES / MDA-PDA interface detail, write rights and freshness. Resolved gaps: `references/swot-and-dependency-seams.md`.

## funnel-prototype

### What is still open

Source: `skills/funnel-prototype/SKILL.md`

- ⟨Whether OD has a standard prototype time box, budget or sign-off rule⟩: not in any source. OD lead.
- ⟨Where finished mock-ups are stored and who can open them⟩: not stated. OD lead.
- ⟨Whether the Gemba App pilot reached a result⟩: the knowledge base holds the brief and the initiative request, not an
  outcome ([`references/gemba-app-pilot.md`](skills/funnel-prototype/references/gemba-app-pilot.md)). Gemba App initiative owner.
- ⟨Touch time and queue time of this step⟩: placeholders in the skill-map table. OD data.
- Whether the click-dummy stack in the Gemba App export (React with Tailwind) fits the department's small
  footprint rule, or the Mendix low-code route named in the initiative deck, is undecided. OD lead with IT.

## funnel-requirements

### Pitfalls and open points (open-point bullets)

Source: `skills/funnel-requirements/SKILL.md`

- **Open points:** none recorded.

## funnel-use-case

### Open points

Source: `skills/funnel-use-case/SKILL.md`

- ⟨Lane lead time to confirm⟩.
- ⟨Process First-Aid Kit request template: none found anywhere in the registry (real gap, `references/lane-templates.md`)⟩.
- ⟨MSB access scope (read / write) to confirm⟩.
- ⟨A dedicated OD use-case one-pager / business-case template beyond the SharePoint agenda: checked, not found; the questionnaire and protocol fill that gap⟩.

### What is still genuinely missing

Source: `skills/funnel-use-case/references/lane-templates.md`

**Process First-Aid Kit request template.** Checked `funnel-requirements` (covers
scoped requirements, not an ad-hoc rapid-diagnostic intake form), `od-analytical-support-
service` (names the same Process First-Aid Kit as its own trigger, with the identical open
placeholder — not independently resolved there either). No dedicated template exists
anywhere in the registry. This is a real gap, not a routing miss.

## invest-screen

### Still open

Source: `skills/invest-screen/references/od-application-consulting/procedure.md`

- `⟨What the "Manufacturing Software Suite" comprises⟩`. The glossary does not define it; the lane's
  skills table says "configure ⟨scope to confirm⟩"; the IIoT Edge operations concept in the department knowledge base
  speaks of a "CT Manufacturing Suite" without listing its parts. Until the OD lead confirms, treat a
  question about the suite as a question about the named tool. Supplier: OD lead.
- `⟨Application consultancy session template⟩` and a lead time for the lane (both `⟨to confirm⟩` in the
  lane documents).
- `⟨Counterpart of the OD lead for tool and system rollout decisions⟩`.
- `⟨Where 3a.1 to 3a.4 are decided⟩` between OD, IT and the external parties: the flow names the steps and
  skills, not the deciders.
- `⟨Owner of external tooling and licensing decisions⟩` (open in the risk register and the lane wait
  states).
- `⟨Current status of EMS and MES (the tool overview and the systems-of-record note can differ)⟩`:
  see the discrepancy list in `footprint-and-data-path`.

### Open

Source: `skills/invest-screen/references/od-application-consulting/references/build-path-options.md`

- `⟨Who decides among 3a.1 to 3a.4⟩` and the criteria; the flow shows them as options after the gate.
- The platform on which apps are deployed ("Container Orchestration Platform" in the VSM skill map) is the edge runtime of the IIoT Edge platform (Concept 3).
- `⟨Lead times⟩` for IT demand, Cyber Security and external development: the flow marks them as weeks
  and leaves the figures open.

### 6 Contradictions left open

Source: `skills/invest-screen/references/process-chain-practice.md`

- Performance analysis (OEE) is assigned both to the edge or analytics side and to the MES side ("may overlap with MES
  functionalities"). Choose the lighter solution and name the overlap explicitly; do not build in parallel what the execution
  system (MES) already does.
- Energy monitoring: cloud tool with data logger against edge platform plus service bus; no deck says which is preferred for a
  new plant. `<to confirm>` with the OD lead.
- Recommendation wording differs for the same tool in the sources ("not necessary", "not recommended as of now", stop or
  continue). State the tool recommendation on one scale: recommended / recommended if <condition> / not recommended / not
  available. Each status carries its date and source; quote the source wording next to it.

### Discrepancies to confirm before quoting a status

Source: `skills/invest-screen/references/od-application-consulting/references/footprint-and-data-path.md`

| Item | One source says | Another says | Action |
|---|---|---|---|
| MES | `systems-of-record`: pilot plants in progress, rollout on hold | Tool note MES 1.0: a rollout record at one plant | Ask the OD lead which is current |
| EMS | Strategy: rollout paused until operational criteria are resolved | The tool catalogue in `invest-screen` and tool notes: rolled out at many plants | Do not pick the convenient version; ask |
| QFPR | `invest-screen` expands it as "Quality Feedback App" | The tool note records a work note expanding it as "Quality Feedback Part Routing" | Use "QFPR" until confirmed |
| MDA/PDA versions | `systems-of-record`: MDA/PDA as one deployed tool | Tool notes: versions 1.0, 2.0 and 3.0 with separate plant lists | Ask which version a plant runs before designing against it |

## mi-data-availability

### What stays open

Source: `skills/mi-data-availability/references/data-needs-by-capability.md`

⟨Which signals each template needs as a minimum (names, units, sampling). The cluster notes
state standards, not signal lists; the signal catalogue belongs to
`mi-signals`. Who could supply it: DBVE with the IIAE.⟩

## mi-equipment

### Still open

Source: `skills/mi-equipment/references/od-barrier-triage/procedure.md`

- `⟨Whether "roadmap" means the plant roadmap or the lane's integration roadmap⟩`: the playbook says
  "escalate to roadmap" without naming the owner. Supplier: IIAE.
- `⟨The barrier log's form and location⟩`: the playbook says "landscape module"; the module read
  (`landscape.md`) has a facility table with a "known barriers" column, not a per-machine log.
- `⟨Lead times⟩` for connector development and for OT and IT cyber-security approvals: called "high",
  no number in the sources.
- `⟨Counterpart for tool rollout decisions⟩` (open in `08-decision-rights.md`).
- `⟨Whether a vendor-less machine row⟩` is a data gap or an unknown machine: Plant ME.
- The class list is this skill's grouping of the recorded fallbacks and blocker texts; the OD lead has
  not confirmed it.

### Still open

Source: `skills/mi-equipment/references/od-machine-integration-plan/procedure.md`

- `<Budget classes>`: class names follow the systems needed; their limits are `<look up in the current approval policy>`.
- `<Capacity per phase>`: meetings per phase are known only qualitatively.
- `<Barrier log location and form>`; `<who convenes the rapid decision board>`.
- Back-out plan content per platform component: the sources hold diagrams only, `<...>`.

### Pitfalls and open points (open-point bullets)

Source: `skills/mi-equipment/SKILL.md`

- **Open points**: ⟨To attach: the two OESL guideline documents (Softing DataFeed Siemens S7; Beckhoff PLC integration) - pointed at, not contained.⟩ ⟨Unverified: whether any OESL plant still runs a NetLink configuration; the German manual's contradiction over the default unsigned-type mode.⟩ `DTQ-MODBUS-Connector` is `Idea` yet `USE` - confirm with the IIAE. Current name of *CT Base* and approved edge sizes - confirm with the IIAE.

## mi-signals

### Open questions worth answering once

Source: `skills/mi-signals/references/public-data-models.md`

⟨Which machines in the estate already expose an OPC UA companion specification — this is not
recorded anywhere and would change the integration route for every one of them.⟩

⟨Whether the requirement spec used at machine purchase (PRS, Doc ID 215534) already asks for
a companion specification. If not, that is a one-line change with a large downstream effect.⟩

⟨Whether the estate's data model — recorded as *CT Base* — was derived from any of these, or
independently. That decides whether adoption is a migration or a reconciliation.⟩

### Pitfalls and open points (open-point bullets)

Source: `skills/mi-signals/SKILL.md`

- **Open points**: ⟨Unit and scale: the estate has no written convention - confirm with the IIAE. `CycleTime` is seconds by convention; `MetersPerMinute` carries its unit in the name, which contradicts the naming rule.⟩

## ops-analytics-asset

### Open

Source: `skills/ops-analytics-asset/references/dashboard-estate-baseline.md`

- ⟨What `Quackito` is and whether it replaces `Telemetry` - data team (SPEC-02 Q4).⟩
- ⟨Definition of `is_delta` - data team (SPEC-02 Q2).⟩
- ⟨Whether the newest Grafana generation is the target platform or an exception - OD lead (SPEC-01 Q1).⟩
- ⟨Who owns the central dashboard repository and the signal record - OD lead (SPEC-04 Q3).⟩
- ⟨Column types, keys, indexes and retention of `telemetry` - needs a schema dump; the DTQ
  "Database Tables and Fields" dashboard can produce one (SPEC-02 Q1).⟩
