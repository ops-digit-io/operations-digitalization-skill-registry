# The Node-RED estate

53 instances, 825 flows, as auto-documented by `node-red-auto-docs`. Read 2026-08-25.

## Naming

```
ct-oesl-<plant-code>-nodered-<prod|test>[N]
```

The doc generator discovers repositories with the regex
`^ct-oesl-.*-nodered-(prod|test).*` in the `ct-oesl` GitHub organization, clones each, and
reads its `flows.json` (or `flow.json`). An instance not matching that pattern is invisible
to the documentation — which is a reason to follow it, not a naming preference.

The trailing `2` / `-2` variants (`…-prod2`, `…-test-2`) are second instances at the same
site, not versions.

## Flows per instance

| Instance | Flows | | Instance | Flows |
|---|--:|---|---|--:|
| ct-oesl-som-nodered-test | 97 | | ct-oesl-cshz-nodered-prod2 | 12 |
| ct-oesl-mak-nodered-prod | 57 | | ct-oesl-tsaz-nodered-test | 11 |
| ct-oesl-som-nodered-prod | 54 | | ct-oesl-car-nodered-prod | 10 |
| ct-oesl-tsaz-nodered-prod | 47 | | ct-oesl-qda-nodered-test | 7 |
| ct-oesl-wth4-nodered-prod | 42 | | ct-oesl-mpee-nodered-test-jg | 6 |
| ct-oesl-del-nodered-prod2 | 41 | | ct-oesl-cal-nodered-prod | 6 |
| ct-oesl-pogz-nodered-prod | 39 | | ct-oesl-spr-nodered-test | 5 |
| ct-oesl-wth4-nodered-test | 38 | | ct-oesl-wth3-nodered-prod | 4 |
| ct-oesl-sub-nodered-test | 35 | | ct-oesl-krb-nodered-test | 4 |
| ct-oesl-wth2-nodered-prod | 32 | | ct-oesl-wth1-nodered-test | 3 |
| ct-oesl-wth2-nodered-test | 31 | | ct-oesl-som-nodered-test2 | 3 |
| ct-oesl-sub-nodered-prod | 31 | | ct-oesl-del-nodered-test2 | 3 |
| ct-oesl-vac-nodered-prod | 29 | | ct-oesl-cal-nodered-test | 3 |
| ct-oesl-krb-nodered-prod | 29 | | ct-oesl-wth2-nodered-prod2 | 2 |
| ct-oesl-mak-nodered-test | 23 | | ct-oesl-vac-nodered-test | 2 |
| ct-oesl-spr-nodered-prod | 18 | | ct-oesl-dol-nodered-prod / prod2 / test | 2 each |
| ct-oesl-qda-nodered-prod | 18 | | ct-oesl-car-nodered-test | 2 |
| ct-oesl-mty-nodered-test2 | 18 | | ct-oesl-wth4-nodered-test-2 | 1 |
| ct-oesl-qda-nodered-prod-2 | 17 | | ct-oesl-qda-nodered-test-2 | 1 |
| ct-oesl-wth1-nodered-prod | 14 | | ct-oesl-nomz-nodered-prod / test | 1 each |
| ct-oesl-som-nodered-prod2 | 13 | | ct-oesl-mty-nodered-prod / prod2 / test | 1 each |
| | | | ct-oesl-del-nodered-prod / test | 1 each |
| | | | ct-oesl-cshz-nodered-prod / test | 1 each |
| | | | ct-oesl-ccn-nodered-prod / test | 1 each |

## Plant codes

Three are confirmed by the `CT/…` topics inside the flows themselves:

| Code | Plant | Confirmed by |
|---|---|---|
| `qda` | Qingdao | `CT/OESL/AS/CHN/QDA/…` |
| `spr` | Sun Prairie | `CT/OESL/NA/USA/SPR/…` |
| `cshz` | Changshu | `CT/MFS/AS/CHN/CSHZ/…` |

The remaining codes — `cal`, `car`, `ccn`, `del`, `dol`, `krb`, `mak`, `mty`, `nomz`,
`pogz`, `som`, `sub`, `tsaz`, `vac`, `wth1`–`wth4` — are OESL site codes and are **not**
resolved to plant names here, because nothing in the bundle states the mapping. ⟨Site-code
table — to confirm with the IIAE.⟩ Do not infer one from a name that merely looks similar;
the Machine List's plant names are the authority and joining on a guess would produce a
wrong per-plant figure.

`mpee` is not a plant: `ct-oesl-mpee-nodered-test-jg` is a department test instance.

`wth1`–`wth4` are four instances at one site, which is why the site appears four times.

## What the shape says

**Test carries as much as prod, sometimes more.** `som` runs 97 flows on test against 54 on
prod; `wth4` 38 against 42; `sub` 35 against 31. Test instances here are working
environments, not scratch — which is why "build on test" is a workable rule rather than a
formality, and also why a test instance can hold a literal secret that matters.

**Flow count is not maturity.** A site with one flow may have a single well-built
integration; a site with 97 may have accumulated variants. Read the flows, not the count.

**No flow in the corpus is marked disabled** — 0 of 825. Either disabled flows are deleted
rather than parked, or the exported per-flow JSON drops the tab's `disabled` state. The
generator does track it, so treat a zero here as *not evidenced* rather than *none*.

## The documentation pipeline

`generate_docs.py` produces, per flow: a Markdown page (title, repository, flow id,
disabled state, description, an embedded interactive flow renderer, a node-details table
and a groups table) plus the flow's own JSON beside it, and rebuilds `mkdocs.yml` nav and
an index dashboard. It needs `GH_ORG`, `GH_REPO_PATTERN`, `GITHUB_PAT`, and optionally
`GH_API` for GitHub Enterprise.

Everything on the generated page comes from the flow itself: the tab `label` and `info`,
each node's `name` and `info`, and each group's `name`. There is no separate documentation
source and no place to add prose afterwards — **the flow is the documentation**.
