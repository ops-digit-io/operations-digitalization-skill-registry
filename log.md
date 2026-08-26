# Log

History of this bundle. Reserved under OKF §9: headings are ISO 8601 dates, and this file is
not a concept.

## 2026-08-26

- Added `docs/skill-state-map.md` and `scripts/build_skill_map.py`: a generated Mermaid map of
  all 24 skills in delivery order, coloured by build state, with inbound `composes` counts and
  the three recommended next. Build state is read from the filesystem so the map cannot drift.

- Described the OPC UA direct connector properly and added availability to every connector
  table. `references/connectors.md` covers all 26 with what each reaches, over which protocol,
  which PLCs, its container image, and whether it can be used — seven cannot. The B&R and
  Bachmann connectors are `Idea · NOT AVAILABLE` while 73 machines across those families are
  integrated over OPC UA, so `check_availability.py` now routes them to `DTQ-OPCUA-Connector`
  instead of raising a connector gap, and no longer offers the `DO NOT USE`
  `SFT-SIMATIC S7-Connector` to Siemens machines.
- Built out `od-data-availability-check`: four references, the verdict asset, and
  `check_availability.py`, which walks the six steps against the Machine List, the Connector
  Overview and the 825-flow Node-RED corpus and names which step a request dies at. Step 5 is
  reported unproven on every run because no source in the bundle records fitness for use.
- Recorded five new open gaps found while building it, among them 16 plants with no flow
  evidence, 191 machines integrated by an unrecorded method, and 23 machine rows whose
  `plc_vendor` is not a vendor.

## 2026-08-25

- Adopted the Open Knowledge Format across the registry. Every concept carries OKF
  frontmatter; a `SKILL.md` carries its OKF fields under `metadata.okf`, because the Agent
  Skills spec allows only six top-level keys and anything else fails packaging and upload.
  Contract in [docs/okf-conventions.md](docs/okf-conventions.md), guard in
  `scripts/verify_okf.py`, generated indexes from `scripts/build_okf_index.py`.
- Removed `argument-hint` from `build-grafana-ops-dashboard/SKILL.md`, which would have
  failed upload with a hard error; it now lives under `metadata`.
- Replaced `last_verified` with `sources_read` on all 24 skills. The old name asserted a
  verification nobody performed and carried no actor, so no OKF trust tier could be derived
  from it. Every concept is `unverified`, which is accurate.
- Fixed defects found by review: hand-rolled argument parsing in four scripts silently
  dropped `--lane=` and `--capability=` and reported success; `tokens()` never split
  camelCase, so `HeadTemperature` was reported as German; ambiguous terms across Spanish,
  Portuguese and Serbian resolved to whichever loaded first; three call sites read the label
  column differently; the money check missed the `EUR 340,000 2026` form its own template
  uses; a `"signal" not in row` filter dropped real rows such as `SignalQuality`; unnamed
  Node-RED groups leaked an empty entry into a finding; and `arraySplt` was gated on the
  wrong field.
- Synced `authority_level` between `registry.yaml` and each `SKILL.md` — the registry granted
  `execute-autonomously` in one case where the skill capped at recommend — and made
  `validate_registry.py` fail on any disagreement or on a placeholder inside metadata.
- Added the epic and user stories output to `od-requirements-breakdown`.
- Added multilingual tag handling to `od-signal-standardization`.
