---
type: Skill Reference
title: Clusters
description: The cluster tags' (C01-C12) standard definition, KPI set and requirements checklist each — the default baseline an undocumented use case is built to instead of being re-invented locally.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, standardization]
---
# The clusters — definition, KPIs, requirements checklist

A plant use case with no local notes is built to the checklist below, not from a blank
page; only the plant-specific deltas (which machines, which line, which local constraint)
get written down on top of it. Seven clusters (C01, C02, C03, C04, C06, C08, C11) cite a
source independently verified against its DOI, Crossref record or standard preview in the
Department knowledge base's reference library; the remaining five (C05, C07, C09, C10, C12) carry a
citation to the same standard or literature carried over from the department's own
standardization knowledge base, not independently re-verified this round — treat those as
a correct pointer to check, not as a verified quote.

## C01 · Real-time line and OEE / performance monitoring

**Definition.** Overall Equipment Effectiveness = Availability × Performance × Quality —
the share of scheduled time that is genuinely productive, introduced by Nakajima as the
central metric of Total Productive Maintenance.
**KPIs.** Availability %, Performance/speed rate %, Quality/first-pass yield %, OEE %,
TEEP (OEE × loading rate for 24/7 potential).
**Checklist.**
- Run/stop states, actual-vs-ideal cycle time and good/defective counts collected
  automatically or semi-automatically.
- A fixed, documented ideal cycle time per product, agreed once and never silently
  re-tuned — a quietly re-tuned cycle time is the single most common way this cluster's
  trend stops meaning anything.
- A documented micro-stop recording threshold per line (industry convention: 1-5 minutes).
- The dashboard shows availability, performance and quality **separately**, never only the
  blended percentage — the split is what tells an operator which loss to attack.
- Never used to rank machines, shifts or plants against each other. It is a loss-diagnosis
  tool per asset, not a league table.
**Sources.** ISO 22400-2:2014 (verified: defines manufacturing-operations KPIs with
formula, time behaviour and unit per indicator; the individual KPI formulas themselves are
not independently verified here — do not quote one from this entry). Muchiri & Pintelon
(2008), *Performance measurement using OEE: literature review and practical application
discussion*, International Journal of Production Research 46(13), DOI
10.1080/00207540601142645 (verified). VDI 3423:2011-08 and Nakajima, *TPM Development
Program* (1988) — carried over, not independently re-verified.

## C02 · Digital Andon, Gemba and escalation

**Definition.** Andon is a Toyota Production System / Jidoka signalling system letting any
worker flag a problem and, traditionally, stop the line until it is resolved. Gemba ("the
actual place") is the lean principle that the most valuable improvement ideas come from
observing the real shop floor.
**KPIs.** Andon-pull rate, time-to-acknowledge (tier-1 response), time-to-resolve (full
escalation cycle), % of escalations closed with a documented root cause, line-stop minutes
attributable to andon events.
**Checklist.**
- Triggerable by hand (a button, not necessarily a pull-cord) **and** automatically from
  machine signals.
- Two-step logic by design: the first signal requests help without stopping the line; the
  second stops it only if nobody came. Do not default every signal to a hard stop.
- Defined escalation tiers (operator/team lead → supervisor → engineering/management),
  each with a time-boxed response.
- Every event **logged**, not only displayed — the log is what makes the improvement
  analysis possible afterward; a display-only Andon has nothing to analyse once the shift
  ends.
- One cross-plant standard — this is the cluster with the strongest case for it, because
  what it replaces is a different whiteboard at every site.
**Sources.** Ma, Wang, Zhao (2017), *SLAE-CPS: smart lean automation engine enabled by
cyber-physical systems technologies*, Sensors 17(7), DOI 10.3390/s17071500 (verified).
Lean Enterprise Institute Lean Lexicon, "Andon", "Gemba", "Jidoka" (verified, practitioner
tier). Liker, *The Toyota Way* (2004); Imai, *Gemba Kaizen* (1997) — carried over, not
independently re-verified.

## C03 · SPC and in-process quality

**Definition.** Statistical Process Control, pioneered by Shewhart, distinguishes common-
cause (inherent) variation from special-cause (assignable) variation using control charts
— catching a quality problem before a batch of bad product is produced, not just
inspecting it afterward.
**KPIs.** Process capability indices (Cp, Cpk), out-of-control-limit event rate, control-
chart rule violations, scrap/rework rate, first-pass yield.
**Checklist.**
- Specification limits and statistically-derived (never guessed) control limits defined
  per characteristic before go-live. Conflating specification limits with control limits
  is the most common way an SPC chart ends up meaning nothing.
- The right chart type for the data (I-MR, X-bar/R, p-chart…); a continuous process prone
  to autocorrelation (extrusion, vulcanization) may need a model-based residual chart
  instead of a plain Shewhart chart.
- A defined reaction plan attached to every out-of-control signal, with root-cause tooling
  (Ishikawa/Pareto) behind it. A chart nobody is required to act on is a chart, not SPC.
- The process stabilized *before* SPC goes live, not the other way round.
**Sources.** NIST/SEMATECH e-Handbook of Statistical Methods §6.3.1, "What are Control
Charts?" (verified). Psarommatis, May, Dreyfus, Kiritsis (2020), *Zero defect
manufacturing: state-of-the-art review*, International Journal of Production Research
58(1), DOI 10.1080/00207543.2019.1605228 (verified). Shewhart, *Economic Control of
Quality of Manufactured Product* (1931); AIAG *SPC Reference Manual* (2005) — carried
over, not independently re-verified.

## C04 · Manual data digitization

**Definition.** Replacing a paper form or shared spreadsheet with structured digital
capture — the lowest-technology cluster in the portfolio, the first step of any MES
deployment, and often the highest-return because what it removes is time spent every
shift.
**KPIs.** % of records captured digitally at source, data-entry time per record, data-
entry error rate, time-to-availability of a record for downstream use.
**Checklist.**
- Structured input (form, tablet, scanner) at the point of work — never a spreadsheet
  filled in after the shift ends.
- Mandatory fields matched to what a downstream SPC/OEE/traceability use case actually
  needs: define the consumer before building the form.
- A named migration path to automatic/sensor-based capture where feasible. Manual capture
  is a valid ISA-95 Level-3 starting point, not the target end state.
- Version-controlled master data (product/recipe/spec) behind the form.
- Digitizing is not the goal — the entry becoming usable downstream is. A digital form
  nothing reads is the paper form with extra steps.
**Sources.** ILO, *Introduction to Work Study* (4th rev. ed., 1992), ch. 19-20 (verified:
work-measurement and work-sampling definitions, elements, standard-time formula). REFA
Lexikon, "Verteilzeitstudie" (verified: basic time / allowance time / execution time
breakdown). MESA International's 11 MES functions; ISA-95 Level 3 scope — carried over,
not independently re-verified.

## C05 · Downtime reporting and machine alerts

**Definition.** Automated capture of machine run/stop/fault states with structured
downtime-reason coding, feeding both OEE's availability component and real-time alerting
to the right role — the direct digital replacement for a manual downtime log.
**KPIs.** MTBF, MTTR, unplanned-downtime %, alert-to-acknowledgement time, % of downtime
auto-classified vs. manually coded.
**Checklist.**
- A standard, plant-wide downtime-reason taxonomy, never a free-text field — without one,
  every plant's stop reasons are unique and nothing rolls up across the estate.
- Alerts routed automatically to a defined recipient tier, tying directly into C02's
  escalation model.
- Every event written to a historian, not only displayed — an alert with no defined
  recipient and no defined acknowledgement becomes noise within a fortnight, and after
  that it is worse than nothing, because people have learned to ignore it.
- Interlinked-equipment logic distinguishes "starved" (no input) and "blocked" (no output)
  from a genuine machine fault, so the wrong asset is not blamed.
**Sources.** ISO 22400-2's downtime/loss categories; the "interlinked equipment" guidance
in the OEE literature and MESA International's MES functions — carried over from the
department's standardization knowledge base, not independently re-verified this round.

## C06 · Predictive maintenance

**Definition.** Maintenance triggered by the measured condition of equipment (vibration,
temperature, acoustic emission, oil analysis, current signature) rather than a fixed time
or usage interval, intervening only when genuinely warranted.
**KPIs.** Unplanned-downtime reduction %, maintenance-cost reduction %, false-positive
alert rate, lead time between predicted and actual failure, spare-parts inventory
reduction.
**Checklist.**
- Sensing technology matched to the failure mode: vibration for high-speed rotating
  equipment, infrared for the widest general applicability, oil analysis for long-term
  high-maturity programs, motor current signature analysis where vibration sensors are
  impractical.
- Results feed a CMMS so a detected condition becomes a work order automatically — a
  standalone dashboard with no CMMS link is low-value by design, not a smaller version of
  the real thing.
- Start with the highest-criticality, highest-failure-cost assets, not the easiest to
  instrument.
- False-positive rate tracked explicitly — it is the main reason a predictive-maintenance
  program loses operator trust.
- A prediction has to reach a maintenance plan to be worth anything; a model that is right
  and changes nobody's schedule has produced no value.
- This cluster is gated on machine integration more directly than any other — it needs
  condition data over time, so check `mi-equipment` before promising a
  timeline.
**Sources.** ISO 17359:2018, condition monitoring and diagnostics of machines (verified,
general guidelines only — no claim is made beyond that scope). Pech, Vrchota, Bednář
(2021), *Predictive maintenance and intelligent sensors in smart factory: review*, Sensors
21(4), DOI 10.3390/s21041470 (verified). Jardine, Lin, Banjevic (2006), *A review on
machinery diagnostics and prognostics implementing condition-based maintenance*,
Mechanical Systems and Signal Processing 20(7), DOI 10.1016/j.ymssp.2005.09.012 (verified
by title only — do not attribute a specific finding or figure to it).

## C07 · Recipe and traceability

**Definition.** Two disciplines recorded together because they fail together: managing
and verifying machine recipes so the right process window is always loaded, and
traceability — an unbroken, auditable chain linking a produced unit back to its process
parameters, materials and quality results.
**KPIs.** Recipe-verification error rate (wrong recipe loaded), traceability query
response time, % of production covered by end-to-end traceability, time-to-root-cause on
a complaint.
**Checklist.**
- Recipes stored and version-controlled centrally, with electronic verification against
  the job order before a machine starts — not reliant on operator memory or a paper
  traveler.
- A unique, scannable identifier per lot or unit carried through the whole production flow
  — the traceability key, at minimum one-up-one-down.
- Queryable in both directions: forward (where this batch went) and backward (what made
  this unit, for a complaint).
- Traceability is a customer-quality and audit-evidence asset, not an internal
  convenience — its retention period and access model are documented, not implicit.
- A recipe change nobody logged is a traceability gap nobody can see; the two halves are
  reviewed together, never one without the other.
**Sources.** ISO 22005, traceability system design principles; MES "management of product
definitions" and "production track and trace" functions — carried over, not independently
re-verified this round.

## C08 · Energy management

**Definition.** Capturing and acting on energy consumption at machine or line level to
identify waste — idle consumption, an oversized machine running underloaded, an avoidable
shutdown gap.
**KPIs.** kWh per unit produced, idle/standby consumption %, energy cost per line/shift,
avoided-consumption value from shutdown-discipline initiatives.
**Checklist.**
- Metered at the level the initiative needs to act on — line or cell, not only building
  level. A plant-level meter reading identifies no action, because consumption has to be
  attributed to something before anyone can act on it.
- A baseline normal-consumption pattern per shift/product recorded **before** flagging an
  anomaly — a saving claim is only as good as the before it is measured against.
- Energy data tied to the same OEE/downtime timeline (C01/C05) so idle-but-powered time is
  visible and actionable.
- Treated as a joint digital-plus-behavioral program (shutdown discipline), not a
  dashboard alone.
**Sources.** ISO 50001:2018, energy management systems (verified: requirements for
establishing, implementing and improving an energy management system; does not prescribe
specific performance criteria). Sullivan, Pugh, Melendez, Hunt (2010), *Operations &
Maintenance Best Practices*, PNNL-19634, DOI 10.2172/1034595 (verified: reports 5-20%
energy-bill savings from O&M programs without major capital investment, for federal
facilities — a reported estimate, not a measured result of this estate; do not quote a
predictive-maintenance-specific figure from this source).

## C09 · Analytics and cross-cutting reporting

**Definition.** Use cases that sit on top of the other data domains rather than owning
one — cross-machine or cross-line dashboards, ad-hoc analysis and management reporting.
**KPIs.** None standard beyond adoption — the question this cluster answers varies too
much for one KPI set; each report defines its own, tied to the decision it supports.
**Checklist.**
- Consumes data from the domain-owning capability (C01/C03/C05/C07/C08, etc.); never
  duplicates its collection.
- The audience and the decision the report supports are named *before* it is built — a
  dashboard with no attached decision is a dead end on arrival, not a useful general-
  purpose asset.
- A small number of standard, reusable report templates beats one bespoke analysis per
  plant.
- Most things proposed for this cluster are better as an addition to an existing
  dashboard — apply that filter at intake before accepting a genuinely new one.
**Sources.** MES "production performance analysis" function; general BI/analytics
practice — carried over from the department's standardization knowledge base, not
independently re-verified this round.

## C10 · Generative and agentic AI

**Definition.** Generative AI (drafting, summarization, code/PLC generation), agentic
workflows (multi-step autonomous task execution) and machine-learning/deep-learning use
cases — the newest cluster; check on the live list how many of its use cases are
productive before claiming maturity.
**KPIs.** None standard yet at this maturity — governance gates (below) substitute for a
KPI set until a use case reaches pilot.
**Checklist.**
- A named, human-gated decision point on every agentic or generative use case: agents
  draft, humans decide. Never let an agent autonomously close a quality, cost or safety
  decision.
- Start read-only / draft-only (sensing and suggesting); expand to write/action scope
  only once a human-in-the-loop track record exists.
- An explicit data-access grant from IT before any agent gets a live system connection.
- The data a model needs has to exist and be reachable first — most of what is proposed
  here is gated on the same machine integration and data digitization as the rest of the
  portfolio, not on the model itself.
- Classic SPC control charts apply to a deployed model too, not only to a physical
  process — model drift is a monitoring problem, not a one-time validation.
**Sources.** General MES "modern trends" literature (AI/ML in MES, low-code platforms)
and SPC-for-model-monitoring practice — carried over, not independently re-verified this
round. The human-gated-decision rule is this registry's own governance principle (see
`dept-context`), not a cited external source.

## C11 · Digital twin and simulation — reserved cluster

**Definition.** A computational model of a physical asset, line or process that stays
continuously synchronized with real data from its physical counterpart — distinguishing a
true digital twin from a static simulation model.
**KPIs.** Not applicable while the cluster has no entry — reserved for its first use case.
**Checklist, for when it does.**
- Decide up front whether a **digital shadow** (one-way: physical → digital only) or a
  true **digital twin** (bidirectional, can send control commands back) is required —
  this materially changes the licensing and security scope.
- Reuse the same telemetry backbone as C01/C06 rather than standing up a separate data
  pipe.
- If the cluster is empty on the live list, check whether that is because no use case has
  matched digital-twin or simulation keywords, or because of a data gap, before treating
  the emptiness as a genuine white space.
**Sources.** ISO 23247-1:2021, digital twin framework for manufacturing (verified:
overview, terms and definitions, framework requirements). Tao, Zhang, Liu, Nee (2019),
*Digital twin in industry: state-of-the-art*, IEEE Transactions on Industrial Informatics
15(4), DOI 10.1109/TII.2018.2873186 (verified).

## C12 · Other and plant-specific — not a standard pattern by design

**Definition.** The bucket for use cases genuinely specific to one plant or process, and
for items too sparse in text to classify confidently. Typically the largest cluster in the
portfolio, which makes its size a data-quality measure more than a topical one — it
shrinks as plant notes get written and the classifier is re-run.
**KPIs.** None — a plant-specific item does not get a standard KPI set by definition.
Track only the cluster's own size over time as the data-quality indicator it is.
**Before committing bespoke work to a C12 item:**
1. Re-check its process group — many C12 items are process-specific instances of an
   otherwise standard capability that simply lacks the link in the source data.
2. Check whether a sibling use case at another plant, same process, has already solved
   the same problem — see the library catalogue in `funnel-use-case`.
3. Only start genuinely new design work once both checks come back empty.
**Sources.** None — there is no standard to cite for a bucket defined as not-yet-standard.
