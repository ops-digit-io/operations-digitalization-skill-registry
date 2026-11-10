#!/usr/bin/env python3
"""eCR (electronic Capital Request) Management Summary builder — neuwerk brand.

This is the render engine for the `ecr-builder` skill. It is DATA-DRIVEN: all
case content lives in the `CASE` dict at the bottom of the file. To build a real
eCR you:

  1. Compile the layered-markdown backbone from the source material (see the
     skill's reference/backbone-and-conditionals.md).
  2. Fill the `CASE` dict below with the backbone's values, carrying a grounding
     tag on every figure ('' | 'a' | 'm' | '?'  → grounded | assumption | market
     | unknown/low-confidence). See reference/grounding-and-color-coding.md.
  3. Author the final `open_items_conflicts` block from the open questions +
     source conflicts you found while compiling.
  4. Run:  python build_ecr.py   → writes eCR_<slug>_neuwerk.pptx

Only edit the CASE dict and the slide-assembly section at the very bottom. The
helper library and the slide-type functions above it are the stable engine and
should not need changing. All output is English (project rule).

Template path is resolved relative to this file: assets/_nw_template.pptx.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '_nw_template.pptx')

# ---- neuwerk palette -------------------------------------------------------
NAVY, DEEP, BLUE, PERI = '1B1E51', '273892', '4E66AE', '8793CA'
GREEN, PEACH, TEAL, PINK, W = '1EB68A', 'F8AF99', '48C2CA', 'EDC0DA', 'FFFFFF'
MINT, MELON = 'CBE7DC', 'FBD9CC'
MELOND, SUN = 'F37558', 'FFA500'
G6, G5, G3, GBG = 'E6E6E6', 'CCCCCC', '999999', 'F2F3F7'
FONT, SERIF = 'Poppins', 'Lora'
GUT = 0.26

# ---- grounding-tag colour map ---------------------------------------------
# '' grounded (no chip) | 'a' assumption | 'm' market/standard | '?' unknown/low-conf
TAG = {
    'a': ('A', PEACH, NAVY, 'assumption — our estimate, not in the source'),
    'm': ('M', PERI, W, 'market/standard value used because none was given'),
    '?': ('?', MELOND, W, 'low confidence / crucial input missing — see open items'),
}

L, R, C = PP_ALIGN.LEFT, PP_ALIGN.RIGHT, PP_ALIGN.CENTER
MID, TOP = MSO_ANCHOR.MIDDLE, MSO_ANCHOR.TOP

prs = Presentation(SRC)
for sld in list(prs.slides._sldIdLst):
    prs.part.drop_rel(sld.rId)
    prs.slides._sldIdLst.remove(sld)


# ============================================================ HELPER LIBRARY
def rich(p, text, size, color, bold=False, italic=False, font=FONT):
    for i, seg in enumerate(text.split('**')):
        if not seg:
            continue
        r = p.add_run(); r.text = seg
        r.font.size = Pt(size)
        r.font.bold = bold or (i % 2 == 1)
        r.font.italic = italic
        r.font.name = font
        r.font.color.rgb = RGBColor.from_string(color)


def ph_fill(slide, idx, rows):
    ph = slide.placeholders[idx]
    ph.text_frame.word_wrap = True
    first = True
    for row in rows:
        text, size = row[0], row[1]
        bold = row[2] if len(row) > 2 else False
        ital = row[3] if len(row) > 3 else False
        p = ph.text_frame.paragraphs[0] if first else ph.text_frame.add_paragraph()
        first = False
        p.space_before = Pt(0); p.space_after = Pt(4)
        r = p.add_run(); r.text = text
        r.font.size = Pt(size); r.font.bold = bold; r.font.italic = ital
        r.font.name = FONT
    return ph


def box(slide, l, t, w, h, fillc, ml=0.13, mt=0.11, line=None, radius=0.04):
    sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                Inches(l), Inches(t), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fillc)
    if line:
        sh.line.color.rgb = RGBColor.from_string(line); sh.line.width = Pt(1)
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    try:
        sh.adjustments[0] = radius
    except Exception:
        pass
    tf = sh.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(ml)
    tf.margin_top = tf.margin_bottom = Inches(mt)
    return sh


def lines(shape, rows, anchor=TOP, align=L):
    tf = shape.text_frame; tf.vertical_anchor = anchor
    first = True
    for text, size, color, bold, italic, sa in rows:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.space_before = Pt(0); p.space_after = Pt(sa)
        rich(p, text, size, color, bold, italic)
    return shape


def caption(slide, l, t, w, h, text, size=10, italic=True,
            align=L, color=NAVY, bold=False):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tb.text_frame.word_wrap = True
    p = tb.text_frame.paragraphs[0]; p.alignment = align
    rich(p, text, size, color, bold, italic)
    return tb


def chip(slide, x, y, tagkey, d=0.24):
    """Small grounding-tag marker. tagkey in {'a','m','?'}. '' → no chip."""
    if not tagkey or tagkey not in TAG:
        return
    letter, fill, fg, _ = TAG[tagkey]
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(y),
                                Inches(d), Inches(d))
    sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fill)
    sh.line.color.rgb = RGBColor.from_string(W); sh.line.width = Pt(1)
    sh.shadow.inherit = False
    tf = sh.text_frame; tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Inches(0)
    p = tf.paragraphs[0]; p.alignment = C
    rich(p, letter, 9, fg, True)


def tag_legend(slide, x, y, keys=('a', 'm', '?')):
    """Horizontal legend strip explaining the grounding chips present on a slide."""
    xx = x
    lb = caption(slide, xx, y, 0.9, 0.24, 'Grounding:', 8.5, False, L, G3, True)
    xx += 0.95
    for k in keys:
        letter, fill, fg, desc = TAG[k]
        chip(slide, xx, y, k, d=0.2)
        caption(slide, xx + 0.24, y - 0.01, 3.3, 0.24, desc, 8, False, L, G3)
        xx += 3.55


def cols(n, total=12.33, gut=GUT):
    w = (total - (n - 1) * gut) / n
    return w, [0.50 + i * (w + gut) for i in range(n)]


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


# ---- slide-type builders ---------------------------------------------------
def cover(title, subtitle, id_rows):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    t = ph_fill(s, 0, [(title, 44, True), (subtitle, 18)])
    t.left, t.top, t.width, t.height = (Inches(0.77), Inches(1.85),
                                        Inches(11.4), Inches(2.0))
    idb = box(s, 0.77, 4.15, 7.1, 1.75, W, ml=0.24, mt=0.18)
    lines(idb, id_rows)
    ph_fill(s, 10, [(CASE['title_tag'], 10)])
    ph_fill(s, 11, [(CASE['presenter'], 10)])
    ph_fill(s, 12, [(CASE['year'], 10)])
    fp = ph_fill(s, 14, [(CASE['tagline'], 10)])
    for p in fp.text_frame.paragraphs:
        for r in p.runs:
            r.font.name = SERIF
    return s


def content(title_text, sub=None):
    s = prs.slides.add_slide(prs.slide_layouts[2])
    t = ph_fill(s, 0, [(title_text, 24)])
    t.left, t.top, t.width, t.height = (Inches(0.77), Inches(0.69),
                                        Inches(11.6), Inches(0.69))
    b = s.placeholders[11]._element
    b.getparent().remove(b)
    ph_fill(s, 10, [(CASE['title_tag'], 10)])
    ph_fill(s, 12, [(CASE['presenter'], 10)])
    ph_fill(s, 13, [(CASE['year'], 10)])
    fp = ph_fill(s, 14, [(CASE['tagline'], 10)])
    for p in fp.text_frame.paragraphs:
        for r in p.runs:
            r.font.name = SERIF
    if sub:
        caption(s, 0.50, 1.36, 12.33, 0.30, sub, 10.5)
    return s


def divider(title):
    s = prs.slides.add_slide(prs.slide_layouts[4])
    ph_fill(s, 0, [(title, 40, True)])
    ph_fill(s, 10, [(CASE['title_tag'], 10)])
    ph_fill(s, 12, [(CASE['presenter'], 10)])
    ph_fill(s, 13, [(CASE['year'], 10)])
    fp = ph_fill(s, 14, [(CASE['tagline'], 10)])
    for p in fp.text_frame.paragraphs:
        for r in p.runs:
            r.font.name = SERIF
    return s


def table(slide, x, y, colw, headers, rows, aligns, hfill=NAVY, hcolor=W,
          fs=9.5, hfs=9.5, rh=0.36, hh=0.42, total_row=False, accent=None):
    xs = [x]
    for w in colw[:-1]:
        xs.append(xs[-1] + w)
    for j, h in enumerate(headers):
        hb = box(slide, xs[j], y, colw[j], hh, hfill, ml=0.1, mt=0.03, radius=0.03)
        lines(hb, [(h, hfs, hcolor, True, False, 0)], anchor=MID, align=aligns[j])
    yy = y + hh + 0.05
    n = len(rows)
    for ri, row in enumerate(rows):
        is_tot = total_row and ri == n - 1
        fill = (accent or PERI) if is_tot else (W if ri % 2 == 0 else GBG)
        for j, cell in enumerate(row):
            cb = box(slide, xs[j], yy, colw[j], rh, fill, ml=0.1, mt=0.02,
                     line=(None if is_tot else G6), radius=0.02)
            col = W if (is_tot and accent == NAVY) else NAVY
            lines(cb, [(cell, fs, col, is_tot, False, 0)], anchor=MID, align=aligns[j])
        yy += rh + 0.04
    return yy


def rr_table(slide, headers, rows, accent, y0=2.02):
    """Rated Risk / Opportunity table. Each row: [item, action, level, case].
    'level' cell is colour-coded High/Medium/Low."""
    colw = [4.9, 4.4, 1.15, 1.88]
    xs = [0.50]
    for w in colw[:-1]:
        xs.append(xs[-1] + w)
    for j, h in enumerate(headers):
        hb = box(slide, xs[j], y0, colw[j], 0.5, accent, ml=0.12, mt=0.06)
        lines(hb, [(h, 10, NAVY, True, False, 0)], anchor=MID,
              align=(C if j == 2 else L))
    yy = y0 + 0.56
    lvlcol = {'High': MELON, 'Medium': PEACH, 'Low': MINT}
    for row in rows:
        rh = 1.28
        for j, cell in enumerate(row):
            fillc = W
            if j == 2:
                fillc = lvlcol.get(cell, W)
            cb = box(slide, xs[j], yy, colw[j], rh, fillc, ml=0.12, mt=0.09,
                     line=(None if j == 2 else G6))
            al = C if j == 2 else L
            lines(cb, [(cell, 9.5, NAVY, (j == 2), False, 0)], anchor=MID, align=al)
        yy += rh + 0.1


def kpi_row(slide, kpis, y=1.86, dark=True):
    """kpis = list of (label, value, sub). Renders equal cards."""
    cw, xs = cols(len(kpis))
    for i, (lab, val, sub) in enumerate(kpis):
        fill = NAVY if dark else W
        c = box(slide, xs[i], y, cw, 1.62, fill, ml=0.16, mt=0.16,
                line=(None if dark else G5))
        labc = PERI if dark else DEEP
        valc = W if dark else NAVY
        lines(c, [(lab, 11, labc, True, False, 6), (val, 20, valc, True, False, 5),
                  (sub, 9, (PERI if dark else G3), False, True, 0)],
              anchor=MID, align=C)


# ============================================================ OPEN ITEMS & CONFLICTS
def open_items_conflicts(open_items, conflicts, verdict):
    """Final backup slide, modeled on the bc-assessment provenance/conflict slide.

    open_items  : list of (question, why_it_matters, owner, tagkey)
                  — the open questions that would sharpen the case.
    conflicts   : list of (conflict, sources, resolution, residual_tag_text)
                  — disagreements / gaps found in the base material.
    verdict     : (label, sentence) — the maturity-gate line for this deck.
    """
    s = content('Open items & conflicts',
                'What would sharpen this case, and where the base material disagreed')
    # verdict band across the top
    vlabel, vtext = verdict
    vcol = {'Ready to sign': GREEN, 'Sign the floor, validate the upside': PERI,
            'Not ready': MELOND}.get(vlabel, PERI)
    vb = box(s, 0.50, 1.70, 12.33, 0.62, vcol, ml=0.18, mt=0.08)
    tcol = W if vcol in (GREEN, MELOND) else NAVY
    lines(vb, [('%s — %s' % (vlabel, vtext), 10.5, tcol, True, False, 0)],
          anchor=MID, align=L)

    # LEFT: open questions to sharpen
    lx, lw = 0.50, 6.03
    hdr = box(s, lx, 2.48, lw, 0.44, NAVY, ml=0.16, mt=0.06)
    lines(hdr, [('Open questions to sharpen', 11, W, True, False, 0)],
          anchor=MID, align=L)
    yy = 3.00
    for q, why, owner, tk in open_items:
        h = 0.98
        cb = box(s, lx, yy, lw, h, W, ml=0.16, mt=0.09, line=G5)
        lines(cb, [(q, 9.5, NAVY, True, False, 3),
                   ('Why: ' + why, 8.5, G3, False, False, 2),
                   ('Owner: ' + owner, 8.5, DEEP, False, True, 0)], anchor=TOP)
        chip(s, lx + lw - 0.34, yy + 0.10, tk, d=0.22)
        yy += h + 0.12

    # RIGHT: conflicts in base material
    rx, rw = 6.80, 6.03
    hdr2 = box(s, rx, 2.48, rw, 0.44, MELOND, ml=0.16, mt=0.06)
    lines(hdr2, [('Conflicts in the base material', 11, W, True, False, 0)],
          anchor=MID, align=L)
    yy = 3.00
    for conflict, sources, resolution, residual in conflicts:
        h = 0.98
        cb = box(s, rx, yy, rw, h, MELON, ml=0.16, mt=0.09)
        lines(cb, [(conflict, 9.5, NAVY, True, False, 3),
                   ('Sources: ' + sources, 8.5, G3, False, True, 2),
                   ('Resolved: ' + resolution + '  [' + residual + ']',
                    8.5, NAVY, False, False, 0)], anchor=TOP)
        yy += h + 0.12
    caption(s, 0.50, 6.60, 12.0, 0.3,
            'Chips: **A** assumption   -   **M** market/standard   -   **?** low confidence / crucial input missing',
            8.5, False, L, G3)
    notes(s, 'Auto-generated final slide. Left = open questions that would raise '
             'confidence; right = disagreements/gaps found across the source files '
             'and how each was resolved into the deck. If too many core value '
             'drivers are unknown, the deck should not have been built — refuse '
             'and return the de-risk questions first (see the skill refusal gate).')
    return s


# ============================================================================
# ============================  CASE CONTENT  ================================
# Replace everything below with the compiled backbone for the real eCR.
# Every euro/number that is NOT stated in the source carries a chip tag.
# The values here are an ILLUSTRATIVE worked example (Product Regionalization,
# Kranj) so the engine is runnable/self-testing out of the box.
# ============================================================================
CASE = {
    'slug': 'Example_Regionalization',
    'title_tag': 'eCR - Example (illustrative)',
    'presenter': 'neuwerk',
    'year': '2025',
    'tagline': 'The neuwerk way',
}


def build():
    # ---- 1 COVER
    cover('Management Summary',
          'Product Regionalization - AC Pressure Lines  (illustrative example)',
          [('Capital Request', 10, G3, False, False, 3),
           ('Regionalization of AC pressure-line production to Kranj', 12.5, NAVY, True, False, 8),
           ('Location    Kranj, Slovenia', 10.5, NAVY, False, False, 2),
           ('Company    neuwerk', 10.5, NAVY, False, False, 0)])

    # ---- 2 CONTENT
    s2 = content('Content')
    toc = [('1', 'Executive summary', None),
           ('2', 'Project description', '2a current   -   2b planned situation'),
           ('3', 'Investment data - GPA / non-GPA', None),
           ('4', 'Additional details / assumptions', '4a volume   -   4b savings   -   4c price / cost'),
           ('5', 'Key figures of the financial analysis', '5a sensitivity calculation'),
           ('6', 'Risks & opportunities', None),
           ('7', 'Alternative solutions', None),
           ('8', 'Plant / production layout', None),
           ('9', 'Project timeline', None)]
    y = 1.70
    for num, title, sub in toc:
        nb = box(s2, 0.50, y, 0.62, 0.44, NAVY, ml=0, mt=0)
        lines(nb, [(num, 13, W, True, False, 0)], anchor=MID, align=C)
        rows = [(title, 12.5, NAVY, True, False, 0)]
        if sub:
            rows.append((sub, 9.5, G3, False, False, 0))
        tb = box(s2, 1.24, y, 11.6, 0.44, W, ml=0.12, mt=0.02)
        tb.line.fill.background()
        lines(tb, rows, anchor=MID)
        y += 0.485
    bb = box(s2, 0.50, y + 0.04, 12.33, 0.52, PERI, ml=0.18, mt=0.06)
    lines(bb, [('Backup', 12, NAVY, True, False, 0),
               ('P&L and cash-flow   -   CT Engineering Checklist   -   Open items & conflicts   -   Glossary',
                9.5, NAVY, False, False, 0)], anchor=MID)

    # ---- 3 EXEC SUMMARY (headline financials on the rail; legend shown once)
    s3 = content('1) Executive summary')
    CW = 7.35
    wwh = [
        ('What?', 'Invest EUR 398k [a] to establish regional production of 18 AC pressure-line part numbers at Kranj, currently imported from Aguascalientes.'),
        ('Why?', 'Removes ocean freight, 4.5% import duty and USD exposure; cuts lead time 8->2 weeks; lowers landed cost by ~EUR 0.44M/yr at full ramp [a].'),
        ('How?', 'One spiral-crimping line + assembly & leak-test cell in Hall 2; qualified via PPAP; SOP June 2026, full ramp 2028.'),
    ]
    for i, (head, body) in enumerate(wwh):
        yy = 1.62 + i * 1.55
        c = box(s3, 0.50, yy, CW, 1.42, W, ml=0.2, mt=0.13, line=G5)
        lines(c, [(head, 13, NAVY, True, False, 4), (body, 10, NAVY, False, False, 0)])
    rx, rw = 8.12, 4.71
    rail = box(s3, rx, 1.62, rw, 4.66, NAVY, ml=0.24, mt=0.16)
    lines(rail, [
        ('REQUEST TYPE', 9, PERI, True, False, 1),
        ('Capital Request - Cost Reduction', 10.5, W, False, False, 8),
        ('REQUEST AMOUNT', 9, PERI, True, False, 1),
        ('GPA 332k   non-GPA 66k', 10.5, W, False, False, 1),
        ('Total  EUR 398 k', 13, GREEN, True, False, 9),
        ('FINANCIAL KEY FIGURES', 9, PERI, True, False, 1),
        ('NPV (WACC 9%)   ~EUR 1.004 M', 10.5, W, False, False, 2),
        ('IRR   108.2 %', 10.5, W, False, False, 2),
        ('Payback   11 months', 10.5, W, False, False, 9),
        ('SCOPE', 9, PERI, True, False, 1),
        ('18 PNs - SOP Jun 2026', 10.5, W, False, False, 0)])
    chip(s3, rx + rw - 0.36, 2.55, 'a')       # amount is assumption in this example
    chip(s3, rx + rw - 0.36, 3.95, 'a')       # financials assumption
    tag_legend(s3, 0.50, 6.55)

    # ---- 4 / 5 PROJECT DESCRIPTION (2a current, 2b planned)
    s4 = content('2a) Project description - Current situation')
    lines(box(s4, 0.50, 1.66, 6.03, 4.94, GBG, ml=0.22, mt=0.18), [
        ('Today: intercontinental supply', 12.5, NAVY, True, False, 8),
        ('All 18 AC pressure-line PNs for the European OEM program are produced at Aguascalientes (Mexico) and shipped to Central Europe.', 10.5, NAVY, False, False, 8),
        ('- Ocean freight + 4.5% import duty per unit', 10.5, NAVY, False, False, 3),
        ('- 8-week replenishment lead time', 10.5, NAVY, False, False, 3),
        ('- USD billing -> EUR/USD exposure', 10.5, NAVY, False, False, 3),
        ('- Landed piece cost EUR 4.85 (2025)', 10.5, NAVY, False, False, 0)], anchor=TOP)
    r = box(s4, 6.80, 1.66, 6.03, 4.94, NAVY, ml=0.24, mt=0.2)
    lines(r, [('Pain today', 10, PERI, True, False, 8),
              ('EUR 4.85', 30, W, True, False, 0), ('landed cost / piece', 10, W, False, True, 14),
              ('8 weeks', 26, W, True, False, 0), ('replenishment lead time', 10, W, False, True, 14),
              ('4.5 %', 26, W, True, False, 0), ('import duty on every unit', 10, W, False, True, 0)], anchor=TOP)

    s5 = content('2b) Project description - Planned situation')
    lines(box(s5, 0.50, 1.66, 6.03, 4.94, MINT, ml=0.22, mt=0.18), [
        ('Target: regional production at Kranj', 12.5, NAVY, True, False, 8),
        ('One spiral-crimping line + assembly & leak-test cell installed in Hall 2, Cell 7 - no building modification.', 10.5, NAVY, False, False, 8),
        ('- Freight and import duty eliminated', 10.5, NAVY, False, False, 3),
        ('- Lead time cut 8 -> 2 weeks', 10.5, NAVY, False, False, 3),
        ('- EUR billing -> no FX exposure', 10.5, NAVY, False, False, 3),
        ('- Landed piece cost EUR 4.12 at full ramp [a]', 10.5, NAVY, False, False, 0)], anchor=TOP)
    r = box(s5, 6.80, 1.66, 6.03, 4.94, GREEN, ml=0.24, mt=0.2)
    lines(r, [('After regionalization', 10, W, True, False, 8),
              ('EUR 4.12', 30, W, True, False, 0), ('landed cost / piece (-15%)', 10, W, False, True, 14),
              ('2 weeks', 26, W, True, False, 0), ('replenishment lead time', 10, W, False, True, 14),
              ('EUR 0.44 M', 24, W, True, False, 0), ('net saving per year (full ramp)', 10, W, False, True, 0)], anchor=TOP)
    chip(s5, 6.80 + 6.03 - 0.40, 1.72, 'a')

    # ---- 6 INVESTMENT DATA
    s6 = content('3) Investment data', 'Capex split GPA / non-GPA-RPE - EUR thousand')
    table(s6, 0.50, 1.98, [6.9, 2.7, 2.73],
          ['Investment item', 'Category', 'kEUR'],
          [['Spiral-crimping machine', 'GPA', '145'],
           ['Assembly & leak-test cell', 'GPA', '118'],
           ['End-forming / swage unit', 'GPA', '69'],
           ['Product-specific tooling', 'non-GPA', '44'],
           ['Installation & qualification', 'non-GPA', '22'],
           ['Total capital request', '', '398']],
          [L, C, R], total_row=True, accent=NAVY, rh=0.44, fs=10.5, hfs=10.5)
    sub = box(s6, 0.50, 5.85, 12.33, 0.72, GBG, ml=0.22, mt=0.12)
    lines(sub, [('GPA 332k (83%)   -   non-GPA/RPE 66k (17%)   -   no building or utility modification required',
                 10.5, NAVY, True, False, 0)], anchor=MID)

    # ---- 7 / 8 / 9 ADDITIONAL DETAILS
    s7 = content('4a) Additional details - Volume, capacity & utilization', 'Annual volume, thousand pieces')
    table(s7, 0.50, 1.98, [4.13, 1.64, 1.64, 1.64, 1.64, 1.64],
          ['', '2026', '2027', '2028', '2029', '2030'],
          [['Program volume (k pcs)', '145', '320', '480', '480', '480'],
           ['Line capacity (k pcs)', '520', '520', '520', '520', '520'],
           ['Utilization', '28%', '62%', '92%', '92%', '92%']],
          [L, R, R, R, R, R], rh=0.44, fs=10.5, hfs=10.5)
    note = box(s7, 0.50, 4.05, 12.33, 2.55, GBG, ml=0.24, mt=0.2)
    lines(note, [('Assumptions', 12, NAVY, True, False, 8),
                 ('- Volume ramp follows the OEM call-off forecast confirmed by Sales.', 10.5, NAVY, False, False, 5),
                 ('- Full ramp 2028 at 480k pcs/yr; line sized for 520k on 2-shift, 5-day. [a]', 10.5, NAVY, False, False, 5),
                 ('- Break-even ~110k pcs/yr, below the 145k committed year 1. [a]', 10.5, NAVY, False, False, 0)], anchor=TOP)
    chip(s7, 12.55, 4.15, 'a')

    s8 = content('4b) Additional details - Savings', 'Annual savings at full ramp (2028), EUR thousand')
    table(s8, 0.50, 1.98, [7.9, 2.2, 2.23],
          ['Savings driver', 'Basis', 'kEUR / yr'],
          [['Ocean freight avoidance', 'no intercontinental shipping', '176'],
           ['Import duty avoidance (4.5%)', 'EU-produced, no duty', '104'],
           ['FX exposure reduction', 'EUR billing vs USD', '58'],
           ['Inventory & obsolescence', '8 -> 2 week lead time', '68'],
           ['Piece-cost reduction', 'regional process', '34'],
           ['Total annual savings', '', '440']],
          [L, L, R], total_row=True, accent=GREEN, rh=0.42, fs=10.5, hfs=10.5)

    s9 = content('4c) Additional details - Price / cost development', 'Landed piece cost, EUR per piece')
    table(s9, 0.50, 1.98, [4.13, 1.64, 1.64, 1.64, 1.64, 1.64],
          ['', '2026', '2027', '2028', '2029', '2030'],
          [['Imported (landed)', '4.85', '4.90', '4.95', '5.00', '5.05'],
           ['Regionalized (Kranj)', '4.35', '4.20', '4.12', '4.10', '4.08'],
           ['Saving per piece', '0.50', '0.70', '0.83', '0.90', '0.97']],
          [L, R, R, R, R, R], rh=0.44, fs=10.5, hfs=10.5)

    # ---- 10 / 11 KEY FIGURES + SENSITIVITY
    s10 = content('5) Key figures of the financial analysis')
    kpi_row(s10, [('NPV', '~EUR 1.004 M', 'WACC 9%'), ('IRR', '108.2 %', 'vs 9% hurdle'),
                  ('Payback', '11 months', 'after SOP'), ('RoS impact', '+2.3 pp', 'program level')])
    table(s10, 0.50, 3.78, [4.13, 1.64, 1.64, 1.64, 1.64, 1.64],
          ['Cash flow (kEUR)', '2026', '2027', '2028', '2029', '2030'],
          [['Net savings', '210', '448', '462', '470', '478'],
           ['Capex', '-398', '-', '-', '-', '-'],
           ['Free cash flow', '-188', '448', '462', '470', '478'],
           ['Cumulative FCF', '-188', '260', '722', '1 192', '1 670']],
          [L, R, R, R, R, R], rh=0.4, fs=10, hfs=10)
    caption(s10, 0.50, 6.35, 12.33, 0.3, 'Cumulative cash flow turns positive during 2027; figures from the financial model.', 9)

    s11 = content('5a) Sensitivity calculation')
    band = box(s11, 0.50, 1.72, 12.33, 0.62, PERI, ml=0.18, mt=0.08)
    lines(band, [('Mandatory only for projects > EUR 1M or realization > 24 months', 11, NAVY, True, False, 0)],
          anchor=MID, align=C)
    det = box(s11, 0.50, 2.60, 12.33, 1.5, MINT, ml=0.24, mt=0.18)
    lines(det, [('Not required for this request', 12.5, NAVY, True, False, 6),
                ('Request EUR 398k (< EUR 1M) and realization 9 months (< 24 months) - both below thresholds. A formal sensitivity analysis is not required by eCR governance.', 10.5, NAVY, False, False, 0)], anchor=TOP)
    det2 = box(s11, 0.50, 4.30, 12.33, 2.3, GBG, ml=0.24, mt=0.18)
    lines(det2, [('Robustness check performed anyway', 12, NAVY, True, False, 8),
                 ('- Break-even ~110k pcs/yr vs 145k committed -> survives a 24% volume shortfall.', 10.5, NAVY, False, False, 5),
                 ('- Payback stays under 18 months even if savings are 25% lower.', 10.5, NAVY, False, False, 5),
                 ('- NPV positive down to a WACC of ~30%, far above the 9% hurdle.', 10.5, NAVY, False, False, 0)], anchor=TOP)

    # ---- 12 / 13 RISKS & OPPORTUNITIES (rated tables)
    s12 = content('6) Risks')
    rr_table(s12, ['Risk', 'Actions to mitigate', 'Level', 'Sensitivity case'], [
        ['Equipment delivery slips beyond the 16-week lead time, putting SOP at risk',
         'Place PO within 2 weeks of approval; weekly supplier milestone tracking; penalty clause',
         'Medium', 'SOP +6 weeks defers ~EUR 55k'],
        ['OEM take-rate below forecast erodes the ramp and payback',
         'Line flexible for adjacent PNs; break-even 110k well below the 145k committed',
         'Low', 'Payback still < 18 months at -25% volume'],
        ['PPAP / customer qualification delay before run-at-rate',
         'Early SQE involvement; run-at-rate slot pre-booked; parallel first-article inspection',
         'Medium', 'Each month defers ~EUR 37k'],
    ], PEACH)

    s13 = content('6) Opportunities')
    rr_table(s13, ['Opportunity', 'Actions necessary to realize', 'Level', 'Upside case'], [
        ['Freight & duty savings scale as more PNs are regionalized',
         'Screen remaining imported AC-line PNs for a follow-on eCR in 2026',
         'High', '+EUR 0.2-0.3 M/yr potential'],
        ['Reuse the regional line for 3 adjacent AC-line PNs',
         'Qualify additional PNs on the spare 8% capacity; minimal tooling add',
         'Medium', '+EUR 0.12 M/yr'],
        ['Shorter lead time lowers safety stock across the program',
         'Rebalance replenishment policy with SCM once regional supply is stable',
         'Medium', 'One-off inventory release ~EUR 0.09 M'],
    ], GREEN)

    # ---- 14 ALTERNATIVES
    s14 = content('7) Alternative solutions', 'Three options evaluated; option A selected')
    opts = [
        ('A', 'Spiral-crimping line (selected)', GREEN,
         ['Capex EUR 332k GPA', 'Flexible across all 18 PNs + adjacents',
          'Lowest maintenance & opex', 'Chosen - best cost/flexibility balance']),
        ('B', 'Double-swage head retrofit', GBG,
         ['Capex EUR 398k GPA (+66k)', 'Higher maintenance (+EUR 33k/yr)',
          'Less flexible for mixed PNs', 'Rejected - higher cost, lower flexibility']),
        ('C', 'Continue import from Aguascalientes', GBG,
         ['No capex', '+EUR 0.44M/yr landed cost',
          'Tariff & FX risk, 8-week lead time', 'Rejected - status quo, no savings']),
    ]
    cw3, xs3 = cols(3)
    for i, (tag, title, fillc, bullets) in enumerate(opts):
        dark = fillc == GREEN
        c = box(s14, xs3[i], 1.86, cw3, 4.7, fillc, ml=0.2, mt=0.18,
                line=(None if dark else G5))
        tcol = W if dark else NAVY
        rows = [('Option ' + tag, 11, (W if dark else PERI), True, False, 3),
                (title, 12.5, tcol, True, False, 10)]
        for b in bullets:
            rows.append(('- ' + b, 10, tcol, False, False, 6))
        lines(c, rows, anchor=TOP)

    # ---- 15 LAYOUT
    s15 = content('8) Plant / production layout', 'if applicable')
    lines(box(s15, 0.50, 1.66, 6.03, 4.94, GBG, ml=0.24, mt=0.2), [
        ('Integration into Kranj Hall 2', 12.5, NAVY, True, False, 8),
        ('- New line in Hall 2, Cell 7, adjacent to existing hose assembly', 10.5, NAVY, False, False, 5),
        ('- Footprint 84 m2; fits current free area', 10.5, NAVY, False, False, 5),
        ('- No building, HVAC or compressed-air modification', 10.5, NAVY, False, False, 5),
        ('- Material flow: goods-in -> crimp -> assembly & leak test -> pack', 10.5, NAVY, False, False, 0)], anchor=TOP)
    ph = box(s15, 6.80, 1.66, 6.03, 4.94, W, ml=0.2, mt=0.16, line=G5)
    lines(ph, [('[ Hall 2 / Cell 7 layout drawing ]', 11, G3, False, True, 0)], anchor=MID, align=C)

    # ---- 16 TIMELINE
    s16 = content('9) Project timeline', 'Key milestones - eCR approval to SOP')
    mstones = [('Oct 2025', 'eCR approval'), ('Nov 2025', 'PO placed'),
               ('Mar 2026', 'Installation'), ('May 2026', 'PPAP & run-at-rate'), ('Jun 2026', 'SOP')]
    n = len(mstones); x0, x1 = 1.05, 12.1; step = (x1 - x0) / (n - 1)
    line = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x0), Inches(3.62), Inches(x1 - x0), Inches(0.035))
    line.fill.solid(); line.fill.fore_color.rgb = RGBColor.from_string(PERI)
    line.line.fill.background(); line.shadow.inherit = False
    for i, (dt, desc) in enumerate(mstones):
        cx = x0 + i * step
        dot = s16.shapes.add_shape(MSO_SHAPE.OVAL, Inches(cx - 0.14), Inches(3.48), Inches(0.28), Inches(0.28))
        dot.fill.solid(); dot.fill.fore_color.rgb = RGBColor.from_string(NAVY if i < n - 1 else GREEN)
        dot.line.color.rgb = RGBColor.from_string(W); dot.line.width = Pt(1.5); dot.shadow.inherit = False
        by = 2.30 if i % 2 == 0 else 3.95
        mb = box(s16, cx - 1.02, by, 2.04, 1.2, W, ml=0.12, mt=0.1, line=G5)
        lines(mb, [(dt, 10.5, (GREEN if i == n - 1 else NAVY), True, False, 3),
                   (desc, 9.5, NAVY, False, False, 0)], anchor=MID, align=C)

    # ---- 17 BACKUP DIVIDER
    divider('Backup')

    # ---- 18 P&L / CASH FLOW
    s18 = content('P&L and cash-flow statement', 'From the financial model - EUR thousand, WACC 9%')
    table(s18, 0.50, 1.98, [4.13, 1.64, 1.64, 1.64, 1.64, 1.64],
          ['', '2026', '2027', '2028', '2029', '2030'],
          [['Gross savings', '210', '448', '462', '470', '478'],
           ['Depreciation', '-80', '-80', '-80', '-80', '-80'],
           ['EBIT impact', '130', '368', '382', '390', '398'],
           ['Capex', '-398', '-', '-', '-', '-'],
           ['Free cash flow', '-188', '448', '462', '470', '478'],
           ['Cumulative FCF', '-188', '260', '722', '1 192', '1 670']],
          [L, R, R, R, R, R], rh=0.42, fs=10, hfs=10)
    caption(s18, 0.50, 5.95, 12.33, 0.4, 'Straight-line depreciation over 5 years; cumulative FCF turns positive during 2027.', 9)

    # ---- 19 CT ENGINEERING CHECKLIST
    s19 = content('CT Engineering Checklist', 'Governance gate - all items cleared before submission')
    items = [('Feasibility study completed', 'Done'), ('Make-or-buy analysis', 'Done'),
             ('Three supplier quotations obtained', 'Done'), ('Capacity & bottleneck analysis', 'Done'),
             ('EHS / safety assessment', 'Done'), ('Quality & PPAP plan agreed with OEM', 'Done'),
             ('IT / software footprint reviewed (OD)', 'Done'), ('Sustainability / energy impact', 'Done')]
    cw2, xs2 = cols(2)
    for i, (label, status) in enumerate(items):
        col = i // 4; row = i % 4; yy = 1.98 + row * 1.12
        c = box(s19, xs2[col], yy, cw2, 0.98, W, ml=0.18, mt=0.12, line=G5)
        dot = s19.shapes.add_shape(MSO_SHAPE.OVAL, Inches(xs2[col] + cw2 - 0.52),
                                   Inches(yy + 0.34), Inches(0.3), Inches(0.3))
        dot.fill.solid(); dot.fill.fore_color.rgb = RGBColor.from_string(GREEN)
        dot.line.fill.background(); dot.shadow.inherit = False
        lines(c, [(label, 11, NAVY, True, False, 4), (status, 10, GREEN, True, False, 0)], anchor=MID)

    # ---- 20 OPEN ITEMS & CONFLICTS  (the requested final slide)
    open_items_conflicts(
        open_items=[
            ('Confirm the 4.5% import-duty rate and USD/EUR rate used in the savings model',
             'Freight+duty are 64% of the EUR 440k savings; a rate change moves the whole case',
             'Controlling / Trade Compliance', 'a'),
            ('Validate the OEM volume ramp (145 -> 480k pcs) against the signed call-off',
             'Payback and NPV scale directly with volume; year-1 145k is the break-even buffer',
             'Sales / Program Mgmt', 'a'),
            ('Confirm installed capex EUR 398k against the latest three supplier quotes',
             'The request amount itself is an estimate here, not a quoted figure',
             'Plant Engineering', '?'),
        ],
        conflicts=[
            ('Landed-cost baseline differs between the freight sheet (EUR 4.85) and the SCM deck (EUR 4.72)',
             'freight-model.xlsx vs SCM-review.pptx',
             'Adopted 4.85 (freight sheet, more recent); 13c gap noted', 'assumption'),
            ('Two capex figures circulated: EUR 398k (eng.) and EUR 362k (early budget)',
             'engineering-quote-draft, FY25-budget-line',
             'Used 398k pending final quotes; budget line was pre-scoping', 'unknown'),
        ],
        verdict=('Sign the floor, validate the upside',
                 'structure and logic are grounded; the euro magnitudes are estimates to firm in one data round before submission'),
    )

    # ---- 21 GLOSSARY
    s21 = content('Glossary', 'Acronyms used in this eCR')
    gloss = [('eCR', 'electronic Capital Request'), ('GPA', 'Globally Pooled Assets (central capex)'),
             ('non-GPA / RPE', 'Regional Plant Equipment (local capex)'), ('NPV', 'Net Present Value'),
             ('IRR', 'Internal Rate of Return'), ('RoS', 'Return on Sales'),
             ('WACC', 'Weighted Average Cost of Capital'), ('SOP', 'Start of Production'),
             ('PPAP', 'Production Part Approval Process'), ('PCIS', 'Project/Product Cost Info System ref'),
             ('PN', 'Part Number'), ('OEM', 'Original Equipment Manufacturer')]
    cw2, xs2 = cols(2); per = (len(gloss) + 1) // 2
    for i, (term, defn) in enumerate(gloss):
        col = i // per; row = i % per; yy = 1.90 + row * 0.78
        tb = box(s21, xs2[col], yy, 1.7, 0.66, NAVY, ml=0.1, mt=0.06)
        lines(tb, [(term, 10.5, W, True, False, 0)], anchor=MID, align=C)
        db = box(s21, xs2[col] + 1.8, yy, cw2 - 1.8, 0.66, W, ml=0.12, mt=0.06, line=G6)
        lines(db, [(defn, 9.5, NAVY, False, False, 0)], anchor=MID)


if __name__ == '__main__':
    build()
    out = 'eCR_%s_neuwerk.pptx' % CASE['slug']
    prs.save(out)
    print('written', out, 'slides:', len(prs.slides._sldIdLst))
