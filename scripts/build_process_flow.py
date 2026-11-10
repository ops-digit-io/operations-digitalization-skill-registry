#!/usr/bin/env python3
"""Build docs/new-state/OD_NewState_ProcessFlow.html - the new-state lanes with the skills on every step.

Reads docs/new-state/process.yaml (steps, core `skills`, extension `proposed`, waits) and each skill's
SKILL.md (status: stable = built, draft = draft). Core skills are the department's skills; extension skills
are drawn as small outlined chips under the step they deepen. A step with no core skill is a human or plant
step. The page keeps the owner's original design.

    python3 scripts/build_process_flow.py            # write the page
    python3 scripts/build_process_flow.py --check    # fail if the page is stale
"""
from __future__ import annotations
import html, pathlib, sys
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import skillpaths as sp  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "new-state" / "OD_NewState_ProcessFlow.html"
PROC = ROOT / "docs" / "new-state" / "process.yaml"

CSS_EXTRA = """
  .chip.draft{background:var(--part-bg);color:var(--part);}
  .chip.ext{background:#fff;color:var(--b2);border:1px solid var(--b4);font-weight:500;font-size:8px;}
  .node.draft{border-top-color:var(--part);} .node.draft .state{color:var(--part);}
  .node.human{border-top-color:var(--b4);background:#f7f9fd;} .node.human .state{color:var(--b2);}
  .node.supplier{border-top-color:var(--melon-d);background:#fff6f3;} .node.supplier .state{color:var(--melon-d);}
  .exts{display:flex;flex-wrap:wrap;gap:0;margin-top:2px;padding-top:4px;border-top:1px dotted var(--g6);}
  .exts .lbl{font-size:7.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--g3);width:100%;margin-bottom:1px;}
  .sw.draft{background:var(--part);} .sw.human{background:var(--b4);} .sw.supplier{background:var(--melon-d);}
  .node .t{padding-right:40px;}
  .chipk{display:inline-block;font-size:8.5px;padding:1px 6px;border-radius:3px;}
"""
LANE = {"lane1": ("l1", "Lane 1", "Self-service"), "lane2": ("l2", "Lane 2", "OD-led"),
        "lane3": ("l3", "Lane 3", "OD / Ext / IT&middot;CS")}
BTAG = {"1a": ("1a", "connected"), "1b": ("1b", "not connected"), "2": ("", ""),
        "front": ("Front&#8209;end", "shared"), "3a": ("3a", "new system"), "3b": ("3b", "new connector")}
SUPPLIER = {"3b5": "Integration execution is supplier-dependent (App-Store-Ops feature request)"}


def status(sid: str) -> str:
    fm = yaml.safe_load((sp.skill_dir(sid) / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1])
    return "built" if str(fm["metadata"].get("status")) == "stable" else "draft"


def e(s: str) -> str:
    return html.escape(str(s))


def node(st: dict) -> str:
    core = st.get("skills") or []
    ext = st.get("proposed") or []
    states = [status(s) for s in core]
    if not core:
        cls, lab = "human", "Human"
    elif all(x == "built" for x in states):
        cls, lab = "built", "Built"
    else:
        cls, lab = "draft", "Draft"
    out = [f'<div class="node {cls}"><span class="state">{lab}</span>',
           f'<div class="t">{e(st["id"])} &middot; {e(st["title"])}</div>']
    if not core:
        out.append('<div class="who">human / plant step</div>')
    for s, x in zip(core, states):
        out.append(f'<span class="chip {x}">{e(s)}</span>')
    if st["id"] in SUPPLIER:
        out.append(f'<div class="who" style="color:var(--melon-d)">{e(SUPPLIER[st["id"]])}</div>')
    if ext:
        out.append('<div class="exts"><span class="lbl">extension</span>' +
                   "".join(f'<span class="chip ext">{e(s)}</span>' for s in ext) + "</div>")
    out.append("</div>")
    return "".join(out)


def track(steps: list) -> str:
    parts = []
    for i, st in enumerate(steps):
        parts.append(node(st))
        if i < len(steps) - 1:
            w = st.get("wait")
            parts.append(f'<div class="arr wait"><span class="wlab">{e(w)}</span></div>' if w else '<div class="arr"></div>')
    return '<div class="track">' + "".join(parts) + "</div>"


def build() -> str:
    p = yaml.safe_load(PROC.read_text(encoding="utf-8"))
    css = (ROOT / "scripts" / "process_flow.css").read_text(encoding="utf-8") + CSS_EXTRA
    core = [s for s in sp.all_ids() if sp.library_of(s) == "core"]
    n_built = sum(1 for s in core if status(s) == "built")
    body = []
    i = p["intake"]["steps"][0]
    body.append('<div class="lane" style="background:#f2f5fb;"><div class="spine" style="background:var(--b1);">'
                '<div class="ln">Intake</div><div class="nm">Classify</div><div class="ow">one lane per demand</div></div>'
                f'<div class="body" style="background:#f2f5fb;">{track([i])}'
                '<div class="fallnote">Known &amp; catalogued &rarr; <b>Lane&nbsp;1</b> &nbsp;&middot;&nbsp; new recurring need &rarr; '
                '<b>Lane&nbsp;2</b> &nbsp;&middot;&nbsp; new system or connector &rarr; <b>Lane&nbsp;3</b> &nbsp;&middot;&nbsp; '
                'no roadmap link or nameable business case &rarr; <b>refuse</b></div></div></div>')
    notes = {"lane1": 'Fall-through: not truly catalogued &rarr; <b>Lane&nbsp;2</b> &nbsp;&middot;&nbsp; no standard system fits &rarr; <b>Lane&nbsp;3</b>',
             "lane2": 'Chains out: needs new software &rarr; <b>Lane&nbsp;3&middot;3a</b> &nbsp;&middot;&nbsp; needs new connection &rarr; <b>Lane&nbsp;3&middot;3b</b> &nbsp;&middot;&nbsp; proven &amp; repeatable &rarr; <b>catalog &rarr; Lane&nbsp;1</b>',
             "lane3": 'Hand over only once the demand is clear &nbsp;&middot;&nbsp; Cyber Security runs in parallel and blocks go-live &nbsp;&middot;&nbsp; delivery after handover is IT / external'}
    for lane in p["lanes"]:
        cls, ln, ow = LANE[lane["id"]]
        rows = []
        for br in lane["branches"]:
            tag, sub = BTAG[br["id"]]
            t = track(br["steps"])
            rows.append(f'<div class="brow"><div class="btag">{tag}<span>{sub}</span></div>{t}</div>' if tag else t)
            if br["id"] == "front":
                rows.append('<div class="opts"><div class="opt"><span class="h">3a.1 reuse app</span>deploy existing codebase</div>'
                            '<div class="opt"><span class="h">3a.2 self dev</span>build then deploy</div>'
                            '<div class="opt"><span class="h">3a.3 external dev</span>guided buy, IT guidelines</div>'
                            '<div class="opt"><span class="h">3a.4 integrate</span>foreign app via IT&middot;CS</div>'
                            '<div class="opt"><span class="h">3b connector</span>new machine connection</div></div>')
        body.append(f'<div class="lane {cls}"><div class="spine"><div class="ln">{ln}</div><div class="nm">{e(lane["title"])}</div>'
                    f'<div class="ow">{ow}</div></div><div class="body">{"".join(rows)}<div class="fallnote">{notes[lane["id"]]}</div></div></div>')
    spine = p["spine"]
    body.append('<div class="lane" style="background:#f7f8fc;"><div class="spine" style="background:var(--g2);"><div class="ln">Spine</div>'
                '<div class="nm">Every step</div></div><div class="body" style="background:#f7f8fc;">'
                + node({"id": "spine", "title": "Context layer", "skills": spine["skills"], "proposed": spine.get("proposed")})
                + "</div></div>")
    drafts = [s for s in core if status(s) == "draft"]
    cards = "".join(f'<div class="gcard thin"><div class="gn">{e(s)}</div><div class="gl">core &middot; draft</div></div>' for s in drafts)
    cards += ('<div class="gcard"><div class="gn">Integration execution</div><div class="gl">Lane 3b &middot; supplier gap</div>'
              '<div class="gd">Not an OD skill; waits on the App-Store-Ops supplier decision.</div></div>')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OD New-State Service Lanes — Process Flow</title>
<style>{css}</style>
</head>
<body>
<div class="page">
  <header>
    <div class="logo"><div class="mark">neu<b>werk</b></div><div class="tag">The neuwerk way</div></div>
    <div class="eyebrow">Operations Digitalization &middot; MPEE</div>
    <h1>New-State Service Lanes <span class="thin">— process flow with the department skills</span></h1>
  </header>
  <div class="legend">
    <div class="grp"><b>Core skill:</b>
      <span class="st"><span class="sw built"></span>Built</span>
      <span class="st"><span class="sw draft"></span>Draft</span>
      <span class="st"><span class="sw human"></span>Human / plant step</span>
      <span class="st"><span class="sw supplier"></span>Supplier gap</span>
    </div>
    <div class="grp"><b>Extension:</b> <span class="chip ext">outlined chip</span> deepens the step</div>
    <div class="grp"><span style="color:var(--melon-d);font-weight:700;font-size:13px;">&#8594;</span> external wait</div>
  </div>
  <div class="flow">{"".join(body)}</div>
  <div class="gaps"><h2>Still open: {len(drafts)} of {len(core)} core skills are drafts</h2><div class="gaprow">{cards}</div></div>
  <div class="foot">
    <div class="src">Generated by <b>scripts/build_process_flow.py</b> from <b>docs/new-state/process.yaml</b> and each skill's <code>SKILL.md</code>
    status (stable = built, draft = draft). Core = the department's skills ({len(core)}, {n_built} built); lanes from the department's
    new-state lane files (Thomas, 2026-09) and the OD x IT alignment of 2026-09-11.</div>
    <div class="way">The neuwerk way</div>
  </div>
</div>
</body>
</html>
"""


def main(argv: list[str]) -> int:
    page = build()
    if "--check" in argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != page:
            print("OD_NewState_ProcessFlow.html is stale: run scripts/build_process_flow.py", file=sys.stderr)
            return 1
        print("process flow up to date")
        return 0
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
