---
type: Skill Reference
title: Public methods
description: The public sources and methods behind process-derivation - what each one says (quoted from the page or document opened on 2026-11-16), what it is used for in the procedure, its source tier, and what could not be verified. Open it when you must justify or replace a method.
resource: ../SKILL.md
status: draft
tags: [process-derivation, sources, methods]
---
# Public methods

Every method below was **opened and read on 2026-11-16** (retrieval date for all entries). Quotes are verbatim and short; a quote is what the source says, not our finding. Tiers follow the registry's source tiers: 1 standards, specifications, peer-reviewed papers and government texts; 2 textbooks; 3 industry-association material; 4 vendor pages. Where only a page about a source could be read (not the source), the entry says so.

## The finding in one paragraph

**No public source opened for this work prescribes a method for exactly this trigger** (a validated prototype, a recorded request and a recorded demand, turned into a process that lives in the organisation). Public material covers the parts: the BPM lifecycle [PD1], redesign heuristics [PD2], process notations [PD3] [PD4] [PD5] [PD6], process classification [PD7], standardized work [PD9], change adoption [PD10] [PD11], change control [PD12] and monitoring [PD13]. **The composition in this skill is our own inference from those parts**, labelled as such in the procedure. It is not a published method and has not been validated by the department.

## Entries

| Key | Source | Used for | Tier |
|---|---|---|---|
| PD1 | Dumas, La Rosa, Mendling, Reijers. *Fundamentals of Business Process Management*, second edition. Springer. Author site <https://fundamentals-of-bpm.org/>. Only the author site was read; the Springer page redirects to a login. | The phase order of the procedure (identify, discover, analyse, redesign, implement, monitor) | 2 |
| PD2 | Reijers, H.A., Liman Mansar, S. (2005). Best practices in business process redesign: an overview and qualitative evaluation of successful redesign heuristics. *Omega* 33(4), 283-306. Abstract read at <https://econpapers.repec.org/RePEc:eee:jomega:v:33:y:2005:i:4:p:283-306>; the full text and the list of heuristics were **not** read. | The redesign checklist and the four impact dimensions | 1 |
| PD3 | OMG. *Business Process Model and Notation (BPMN)*, version 2.0.2, formal/13-12-09, January 2014. <https://www.omg.org/spec/BPMN/2.0.2/> | The notation of the to-be model | 1 |
| PD4 | ISO/IEC 19510:2013, *Information technology - Object Management Group Business Process Model and Notation*. IEC webstore page <https://webstore.iec.ch/publication/10695> | BPMN as an international standard | 1 |
| PD5 | OMG. *Case Management Model and Notation (CMMN)*, version 1.1, December 2016. <https://www.omg.org/spec/CMMN/> | Optional: knowledge-intensive work that cannot be a fixed sequence | 1 |
| PD6 | OMG. *Decision Model and Notation (DMN)*. Formal version 1.6 (1.7 is shown as beta). <https://www.omg.org/spec/DMN/> | Optional: decision rules that sit inside a process | 1 |
| PD7 | APQC. *Understanding the Elements of APQC's Process Classification Framework*, (c) 2018 APQC. PDF from apqc.org (the HTML pages of apqc.org refuse automated access). | Placing the process in the landscape | 3 |
| PD8 | VDI/VDE 3682 Blatt 1, *Formalisierte Prozessbeschreibungen; Konzept und grafische Darstellung*. VDI catalogue page. Only the catalogue page was read. | Optional: technical (plant) process descriptions | 1 (page only) |
| PD9 | Lean Enterprise Institute. Lexicon, *Standardized Work*. <https://www.lean.org/lexicon-terms/standardized-work/> | Standard work for repetitive operator tasks | 3 |
| PD10 | Prosci. *The Prosci ADKAR Model*. <https://www.prosci.com/methodology/adkar> | Adoption plan per role group | 4 |
| PD11 | Kotter International. *The 8 Steps for Leading Change*. <https://www.kotterinc.com/methodology/8-steps/> | Programme-level sponsorship and anchoring | 4 |
| PD12 | U.S. OSHA. 29 CFR 1910.119, paragraph (l) *Management of change*. <https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119> | A checklist pattern for change control | 1 |
| PD13 | IEEE Task Force on Process Mining. *Process Mining Manifesto*, in BPM 2011 Workshops, Part I, LNBIP 99, Springer, pp. 169-194, 2012. Read from the PDF on <https://www.tf-pm.org/resources/manifesto>. | Designing the monitoring so the live process can be checked | 1 |

## What each source says, and how the skill uses it

**PD1 (lifecycle).** Quote: "This second edition includes extended and completely revised chapters on process identification, process discovery, qualitative process analysis, process redesign, process automation and process monitoring." (author site, About). *Use:* the procedure follows this phase order. *Limit:* the author site lists the chapters; the authors' own description of the lifecycle and the edition year were not on the page read.

**PD2 (redesign heuristics).** Quotes: "This paper gives an overview of heuristic rules that can support practitioners"; "The emphasis is on the mechanics of the process, rather than on behavioral or change management aspects."; "To evaluate the impact of each best practice along the dimensions of cost, flexibility, time and quality, a conceptual framework is presented"; "They can be used as a "check list" for process redesign under the umbrella of diverse management approaches" (abstract). *Use:* step 4 runs the heuristics as a checklist and judges each change on cost, flexibility, time and quality. *Limit:* the paper itself says it does not cover behavioural or change-management aspects, which is why steps 6 and 7 add standard work and adoption methods.

**PD3 and PD4 (BPMN).** Quotes: "It is intended to be used directly by the stakeholders who design, manage and realize business processes" and "BPMN has an easy-to-use flowchart-like notation that is independent of any particular implementation environment." (OMG page); "ISO/IEC 19510:2013 is identical to OMG BPMN 2.0.1." (IEC webstore). *Use:* the to-be model is BPMN. *Limit:* the IEC page names version 2.0.1, the OMG page lists 2.0.2 and does not mention the ISO standard; the relation of 2.0.2 to ISO/IEC 19510 is not stated on either page.

**PD5 and PD6 (CMMN, DMN).** Quotes: "This specification defines a common meta-model and notation for modeling and graphically expressing a Case" (CMMN page); "DMN provides two tools for modeling decision-making: a graphical notation and an expression language." (DMN page). *Use:* only when the process has an unpredictable course (CMMN) or a decision that is better a table than a gateway chain (DMN). Neither is required.

**PD7 (process classification).** Quotes: "It includes 13 Level 1 Categories."; a Level 3 process is defined as "a single process"; "this does not imply that process elements occur in a certain order"; each element "has a unique five-digit reference number" so organisations "can rename processes according to organizational norms, but keep the reference numbers" (APQC document). *Use:* step 8 places the process in the landscape at the right level and keeps a stable reference number. *Limit:* tier 3; APQC offers a cross-industry and industry-specific versions, the choice is the department's.

**PD8 (VDI/VDE 3682).** The catalogue page says the guideline "in der ein einfaches Konzept zur grafischen Beschreibung technischer Prozesse vorgestellt wird, wird überarbeitet" (is being revised). *Use:* mentioned as an option for plant (technical) process descriptions. *Limit:* only the catalogue page was read; whether it is paid and which edition is current were not verified.

**PD9 (standardized work).** Quotes: "Establishing precise procedures for each operator's work in a production process, based on three elements:" takt time, "The precise work sequence in which an operator performs tasks within takt time." and "The standard inventory, including units in machines, required to keep the process operating smoothly."; "Standardized work, once established and displayed at workstations, is the object of continuous improvement through kaizen." *Use:* step 6, for repetitive operator work only.

**PD10 and PD11 (adoption).** Quotes: "ADKAR is a model for individual change." and "The ADKAR elements are sequential but not linear" and "identify where progress is blocked and focus support on the earliest unmet element." (Prosci; the elements are Awareness, Desire, Knowledge, Ability, Reinforcement). Kotter names eight steps, ending in "Institute Change", and calls itself "the proven approach to producing lasting change" (vendor claim, not verified). *Use:* step 7 uses ADKAR per role group and Kotter's steps as a programme-level check. *Limit:* tier 4, vendor pages; nothing about their effectiveness is claimed here.

**PD12 (change control pattern).** Quotes: "The employer shall establish and implement written procedures to manage changes (except for "replacements in kind")"; the procedures address before any change "The technical basis for the proposed change;", "Impact of change on safety and health;", "Modifications to operating procedures;", "Necessary time period for the change; and," "Authorization requirements for the proposed change."; affected employees "shall be informed of, and trained in, the change prior to start-up". *Use:* step 7 uses these five points as a checklist for a process that touches plant operation. *Limit:* the regulation applies to processes covered by paragraph (a) (highly hazardous chemicals); the registry does not claim it applies to any plant process. Local legal requirements are for the plant's safety role to name.

**PD13 (process mining).** Quotes: the Manifesto's goal is "to increase the maturity of process mining as a new tool to improve the (re)design, control, and support of operational business processes." Its six guiding principles are: GP1 Event Data Should Be Treated as First-Class Citizens; GP2 Log Extraction Should Be Driven by Questions; GP3 Concurrency, Choice and Other Basic Control-Flow Constructs Should be Supported; GP4 Events Should Be Related to Model Elements; GP5 Models Should Be Treated as Purposeful Abstractions of Reality; GP6 Process Mining Should Be a Continuous Process. Challenge C4 is "Dealing with Concept Drift". *Use:* step 9 designs the event data now, so the live process can be compared with the to-be model later (GP1, GP4) and reviewed continuously (GP6).

## Candidates not used (could not be verified)

Opened without success on 2026-11-16 (access refused or a login required), therefore **not cited and not relied on**: ISO 9001:2015 (iso.org), ASQ pages on SIPOC and DMAIC (asq.org), the Springer pages of PD1 and PD13. They may be good sources; open them in a browser and add them here with their wording before using them. ITIL change enablement and the ABPMN BPM CBOK were not searched.
