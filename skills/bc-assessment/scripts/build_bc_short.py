#!/usr/bin/env python3
"""Concise value-focused BC deck for the Gemba App. English only. Value side only.
Phase-B re-architecture: purpose-per-slide sequence.
 cover; 1 overall picture (C-level); 2 sub-buckets + effort; 3 contribution register
 (all lines incl. uncounted, HIGH/MED/LOW potential); 4 value vs effort (dependencies);
 5 abstracted BPMN (marked differences); 6 SMART milestones + time-to-value;
 7 soft impact clusters; 8 refinement questions led by worked examples."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

SRC = '/sessions/awesome-vigilant-hopper/mnt/outputs/_nw_template.pptx'
OUT = '/sessions/awesome-vigilant-hopper/mnt/outputs/bc-gemba-onepager-neuwerk.pptx'

# Neuwerk brand-exact palette. Blue ramp = the sanctioned graded-card device.
NAVY, DEEP, BLUE, PERI = '1B1E52', '273892', '4E66AE', '8793CA'
# Secondary bases (brand-exact): Mint / Melon / Azure / Levander
GREEN, PEACH, TEAL, PINK, W = '1EB78B', 'F9B09A', '48C3CB', 'EEC1DB', 'FFFFFF'
MELONL = 'F6CFC6'   # Melon light - problem/caution tint
MELOND = 'F37558'   # Melon dark - the brand's red/warning ink (wide-range flag)
GRY = 'CCCCCC'      # Grey 06 - LOW potential chip
SUN = 'FFA500'      # Sun: budget <=10-15%; on a slide ONLY the template title rule + logo
FONT, SERIF = 'Poppins', 'Lora'
GUT = 0.26
FT = dict(tag='BC Assessment', who='OD - Operations Digitalization', yr='2026', tl='The neuwerk way')

prs = Presentation(SRC)
for sld in list(prs.slides._sldIdLst):
    prs.part.drop_rel(sld.rId); prs.slides._sldIdLst.remove(sld)


def rich(p, text, size, color, bold=False, italic=False, font=FONT):
    for i, seg in enumerate(text.split('**')):
        if not seg:
            continue
        r = p.add_run(); r.text = seg
        r.font.size = Pt(size); r.font.bold = bold or (i % 2 == 1)
        r.font.italic = italic; r.font.name = font
        r.font.color.rgb = RGBColor.from_string(color)


def ph_fill(slide, idx, rows):
    ph = slide.placeholders[idx]; ph.text_frame.word_wrap = True
    first = True
    for row in rows:
        text, size = row[0], row[1]
        bold = row[2] if len(row) > 2 else False
        ital = row[3] if len(row) > 3 else False
        p = ph.text_frame.paragraphs[0] if first else ph.text_frame.add_paragraph()
        first = False
        p.space_before = Pt(0); p.space_after = Pt(6)
        r = p.add_run(); r.text = text
        r.font.size = Pt(size); r.font.bold = bold; r.font.italic = ital
    return ph


def box(slide, l, t, w, h, fillc, ml=0.13, mt=0.11, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.06):
    sh = slide.shapes.add_shape(shape, Inches(l), Inches(t), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = RGBColor.from_string(fillc)
    sh.line.fill.background(); sh.shadow.inherit = False
    try:
        sh.adjustments[0] = adj
    except Exception:
        pass
    tf = sh.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(ml)
    tf.margin_top = tf.margin_bottom = Inches(mt)
    return sh


def lines(shape, rows, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
    tf = shape.text_frame; tf.vertical_anchor = anchor
    first = True
    for text, size, color, bold, italic, sa in rows:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align; p.space_before = Pt(0); p.space_after = Pt(sa)
        rich(p, text, size, color, bold, italic)
    return shape


def caption(slide, l, t, w, h, text, size=10, italic=True, align=PP_ALIGN.LEFT, color=NAVY, bold=False):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tb.text_frame.word_wrap = True
    p = tb.text_frame.paragraphs[0]; p.alignment = align
    rich(p, text, size, color, bold, italic)
    return tb


def cols(n, total=12.33, gut=GUT):
    w = (total - (n - 1) * gut) / n
    return w, [0.50 + i * (w + gut) for i in range(n)]


def content(title_text, sub=None):
    s = prs.slides.add_slide(prs.slide_layouts[2])
    t = ph_fill(s, 0, [(title_text, 24)])
    t.left, t.top, t.width, t.height = (Inches(0.77), Inches(0.69), Inches(9.80), Inches(0.69))
    b = s.placeholders[11]._element; b.getparent().remove(b)
    ph_fill(s, 10, [(FT['tag'], 11)]); ph_fill(s, 12, [(FT['who'], 11)])
    ph_fill(s, 13, [(FT['yr'], 11)]); ph_fill(s, 14, [(FT['tl'], 11)])
    if sub:
        caption(s, 0.50, 1.38, 12.33, 0.34, sub, 11)
    return s


def panel(slide, l, t, w, h, fillc, head, head_c, body_rows, body_c, hsize=12.5):
    sh = box(slide, l, t, w, h, fillc, ml=0.18, mt=0.15)
    rows = [(head, hsize, head_c, True, False, 7)]
    for br in body_rows:
        rows.append((br, 10, body_c, False, False, 5))
    lines(sh, rows)
    return sh


def chip(slide, l, t, w, text, fillc, tc, h=0.30, size=8.5):
    sh = box(slide, l, t, w, h, fillc, ml=0.04, mt=0.02, adj=0.5)
    lines(sh, [(text, size, tc, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    return sh


# ================================================= COVER
s = prs.slides.add_slide(prs.slide_layouts[1])
t = ph_fill(s, 0, [('Gemba App - the business case on a page', 32, True),
                   ('Value first, assumptions derived from the case, before/after in one view.', 15)])
t.left, t.top, t.width, t.height = (Inches(0.77), Inches(2.02), Inches(9.81), Inches(2.40))
ph_fill(s, 10, [(FT['tag'], 11)]); ph_fill(s, 11, [(FT['who'], 11)])
ph_fill(s, 12, [(FT['yr'], 11)]); ph_fill(s, 14, [(FT['tl'], 11)])
ph_fill(s, 13, [('Working / engineering review', 11)])

# ================================================= 1 OVERALL PICTURE (C-LEVEL)
s = content('The business case on one page',
            'First implementation = one plant; drivers are averages for the initial area. Every figure carries a grounding tag.')
band = box(s, 0.50, 1.82, 12.33, 1.48, NAVY, ml=0.24, mt=0.14)
lines(band, [('EXPECTED ~EUR 25k / plant / yr   (min ~EUR 22k floor  /  potential ~EUR 83k)', 21, W, True, False, 3),
             ('Expected = grounded hard admin saving. Potential adds reaction upside - NOT banked, one input still missing.', 12.5, PEACH, True, False, 4),
             ('Verdict: sign on the expected floor now - effect certain, size to confirm. Reaction upside is not banked until one input is measured. Value only; cost in the investment file.', 10, PERI, False, False, 0)])
CW, XS = cols(3)
panel(s, XS[0], 3.44, CW, 2.53, PERI, 'Key assumptions (area averages)', NAVY,
      ['6 lines, 3 shifts, 220 days / yr  [market]',
       'Loaded labour EUR 40 / h  [market]',
       '~12 min/line/shift admin; ~78% removed  [assumption]',
       'EUR 250 / machine-h  [market];  idle h/machine  [unknown]'], NAVY)
panel(s, XS[1], 3.44, CW, 2.53, GREEN, 'Savings - the actual case / plant / yr', NAVY,
      ['**EXPECTED   ~EUR 25k**',
       '**Min   ~EUR 22k**  - hard floor, banked',
       '**Max   ~EUR 83k**  - if reaction validated',
       'Hard admin saving: effect [input], size [assumption].'], NAVY)
panel(s, XS[2], 3.44, CW, 2.53, PEACH, 'Further & soft potential (unevaluated)', NAVY,
      ['Reaction: little extra IF waits are already short;',
       'up to ~EUR 56k / plant IF reaction lag is large',
       'Rollout across floor plants ~EUR 0.7-0.9m / yr',
       'Soft: quality/scrap, availability, handover, audit, safety'], NAVY)
caption(s, 0.50, 6.12, 12.33, 0.5,
        'Grounding tags:  [input] from interview/mockup  ·  [assumption] our estimate  ·  [market] standard value where none was given  ·  [unknown] the crucial missing input.',
        9.5)

# ================================================= 2 SUB-BUCKETS + EFFORT
s = content('The case breaks into sub-business cases',
            'Each sub-case has its own value, status and effort to realize. This is the structure the rest of the deck follows.')
# header row
HX = [0.50, 4.35, 6.95, 9.30]
HW = [3.85, 2.60, 2.35, 3.53]
for x, w, h in zip(HX, HW, ['Sub-business case', 'Value / plant / yr', 'Status', 'Effort & key dependency to realize']):
    caption(s, x, 1.92, w, 0.30, h, 9.5, italic=False, color=PERI, bold=True)
rows = [
    ('F', GREEN, 'F  Admin floor', 'Manual KPI entry + board removed', '~EUR 22-27k', NAVY, '', 'Banked', GREEN, NAVY,
     'LOW', GREEN, NAVY, 'Go-live: retire the board. One system decision.'),
    ('R', PEACH, 'R  Reaction', 'Faster reaction to stoppages', '~EUR 5-56k', MELOND, 'wide range: near-zero to substantial', 'Not banked', PEACH, NAVY,
     'MEDIUM', PERI, NAVY, 'Behaviour change: Andon watched + acted on daily.'),
    ('S', TEAL, 'S  Rollout / cross-plant', 'Same process, other plants', '~EUR 0.7-0.9m', NAVY, '', 'Potential', TEAL, NAVY,
     'HIGH', DEEP, W, 'Many sites; transferability + local baselines.'),
    ('X', PERI, 'Soft / strategic', 'Quality, safety, audit, learning', 'not quantified', NAVY, '', 'Optional', PERI, NAVY,
     'VARIES', GRY, NAVY, 'Depends which clusters the plant confirms.'),
]
ry = 2.30
RH = 0.86
for lid, lc, name, desc, val, vcolor, vnote, stat, statc, stattc, eff, effc, efftc, dep in rows:
    # ID tab
    box(s, 0.50, ry + 0.06, 0.44, RH - 0.18, lc, ml=0, mt=0, adj=0.18)
    bd = s.shapes[-1]
    lines(bd, [(lid, 12, NAVY if lid != 'S' else NAVY, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    cell = box(s, 1.04, ry, 3.20, RH, W, ml=0.10, mt=0.06)
    cell.line.color.rgb = RGBColor.from_string(GRY); cell.line.width = Pt(0.5)
    lines(cell, [(name.split('  ', 1)[-1] if '  ' in name else name, 11, NAVY, True, False, 3),
                 (desc, 9, NAVY, False, False, 0)])
    if vnote:
        caption(s, 4.35, ry + 0.04, 2.55, 0.4, val, 11.5, italic=False, color=vcolor, bold=True)
        caption(s, 4.35, ry + 0.44, 2.55, 0.34, vnote, 8, italic=True, color=NAVY, bold=False)
    else:
        caption(s, 4.35, ry + 0.16, 2.55, 0.5, val, 11.5, italic=False, color=vcolor, bold=True)
    chip(s, 6.95, ry + 0.24, 2.05, stat, statc, stattc, size=9)
    chip(s, 9.30, ry + 0.06, 1.00, eff, effc, efftc, size=8.5)
    caption(s, 10.42, ry + 0.02, 2.41, 0.9, dep, 8.5, italic=False, color=NAVY)
    ry += RH + 0.10
caption(s, 0.50, ry + 0.02, 12.33, 0.5,
        'Effort is a qualitative judgement (dependencies to realize, not build hours) - firmed on the investment file. Sign F now; plan R and S dependencies before banking them.',
        9.5)

# ================================================= 3 CONTRIBUTION REGISTER (all lines)
s = content('Contribution register - every line, counted or not',
            'Bar spans min -> max, bold tick = expected. Counted lines carry euros; uncounted lines carry a potential estimate (HIGH / MED / LOW).')
CID, CNM, CBAR, CRNG, CCONF, CPOT = 0.50, 1.28, 5.55, 8.75, 10.05, 11.55
CIDW, CNMW, CRNGW, CCONFW, CPOTW = 0.60, 4.15, 1.28, 1.40, 1.28
HDRY = 1.90
ROWH = 0.44
BARL = 5.55
BARMAX = 2.95
VMAX = 56.0


def rcell(l, w, y, h, text, size, color, bold=False, align=PP_ALIGN.LEFT, italic=False):
    tb = s.shapes.add_textbox(Inches(l), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = Inches(0.04); tf.margin_right = Inches(0.04)
    tf.margin_top = Inches(0.02); tf.margin_bottom = Inches(0.02)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = align
    rich(p, text, size, color, bold, italic)
    return tb


for l, w, hdr, al in [(CID, CIDW, 'ID', PP_ALIGN.LEFT), (CNM, CNMW, 'Lever / line item', PP_ALIGN.LEFT),
                      (CBAR, BARMAX, 'min | exp | max', PP_ALIGN.LEFT), (CRNG, CRNGW, 'EUR k / yr', PP_ALIGN.LEFT),
                      (CCONF, CCONFW, 'Confidence', PP_ALIGN.LEFT), (CPOT, CPOTW, 'Potential', PP_ALIGN.CENTER)]:
    rcell(l, w, HDRY, 0.30, hdr, 9, PERI, True, al)

# (id, name, min, exp, max, conf, barcolor, counted, potlabel, potfill, pottc)
regs = [
    ('H1', 'Hourly KPI entry -> one-tap / MES capture', 13, 15, 16, 'Medium', GREEN, True, 'banked', GREEN, NAVY),
    ('H2', 'Shift-end board -> Excel transcription', 7, 8, 9, 'Medium', GREEN, True, 'banked', GREEN, NAVY),
    ('H3', 'Issue write-up -> auto-recorded once', 2, 2, 2, 'Medium', GREEN, True, 'banked', GREEN, NAVY),
]
y = HDRY + 0.36
for lid, name, c, b, o, conf, barc, counted, potlab, potfill, pottc in regs:
    box(s, CID, y + 0.03, 0.56, ROWH - 0.12, barc, ml=0, mt=0, adj=0.22)
    lines(s.shapes[-1], [(lid, 10, NAVY, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    rcell(CNM, CNMW, y, ROWH, name, 9.5, NAVY)
    xmin = BARL + BARMAX * c / VMAX
    xexp = BARL + BARMAX * b / VMAX
    xmax = BARL + BARMAX * o / VMAX
    ymid = y + ROWH / 2
    box(s, xmin, ymid - 0.04, max(0.04, xmax - xmin), 0.08, barc, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
    box(s, xexp - 0.025, ymid - 0.12, 0.05, 0.24, NAVY, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
    rcell(CRNG, CRNGW, y, ROWH, '%d|%d|%d' % (c, b, o), 9, NAVY)
    rcell(CCONF, CCONFW, y, ROWH, conf, 9, NAVY)
    chip(s, CPOT, y + 0.07, CPOTW, potlab, potfill, pottc, size=8)
    y += ROWH

# hard subtotal
box(s, CID, y + 0.02, 12.33, 0.02, PERI, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
y += 0.06
rcell(CNM, CNMW, y, ROWH, 'Hard subtotal - the bankable ROI floor', 9.5, NAVY, True)
rcell(CRNG, CRNGW, y, ROWH, '22|25|27', 9, NAVY, True)
rcell(CCONF, CCONFW, y, ROWH, 'Medium', 9, NAVY, True)
chip(s, CPOT, y + 0.07, CPOTW, 'BANKED', GREEN, NAVY, size=8)
y += ROWH + 0.06

# not-banked / uncounted lines
uncts = [
    ('O1', 'Reaction-time idle hours recovered', 5, 37, 56, 'Low', PEACH, 'HIGH', DEEP, W),
    ('O2', 'Availability - fewer repeat stoppages', None, None, None, 'Unmeasured', PERI, 'MED', PERI, NAVY),
    ('O3', 'Quality / scrap during degraded runs', None, None, None, 'Unmeasured', PERI, 'MED', PERI, NAVY),
    ('O4', 'Management reporting / KPI consolidation', None, None, None, 'Unmeasured', PERI, 'HIGH', DEEP, W),
]
for lid, name, c, b, o, conf, barc, potlab, potfill, pottc in uncts:
    box(s, CID, y + 0.03, 0.56, ROWH - 0.12, barc, ml=0, mt=0, adj=0.22)
    lines(s.shapes[-1], [(lid, 10, NAVY, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    rcell(CNM, CNMW, y, ROWH, name, 9.5, NAVY)
    ymid = y + ROWH / 2
    if c is not None:
        xmin = BARL + BARMAX * c / VMAX
        xexp = BARL + BARMAX * b / VMAX
        xmax = BARL + BARMAX * o / VMAX
        box(s, xmin, ymid - 0.04, max(0.04, xmax - xmin), 0.08, barc, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
        box(s, xexp - 0.025, ymid - 0.12, 0.05, 0.24, DEEP, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
        rcell(CRNG, CRNGW, y, ROWH, '(%d|%d|%d)' % (c, b, o), 9, NAVY, italic=True)
    else:
        box(s, BARL, ymid - 0.01, BARMAX, 0.02, GRY, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
        rcell(CRNG, CRNGW, y, ROWH, 'not sized', 9, NAVY, italic=True)
    rcell(CCONF, CCONFW, y, ROWH, conf, 9, DEEP if conf == 'Low' else NAVY, conf == 'Low')
    chip(s, CPOT, y + 0.07, CPOTW, potlab, potfill, pottc, size=8)
    y += ROWH

# arithmetic callout folded in (kills the separate numbers slide)
cb = box(s, 0.50, y + 0.08, 12.33, 0.56, NAVY, ml=0.18, mt=0.06)
lines(cb, [('Hard floor derivation:  9.4 min saved  x  6 lines  x  3 shifts  x  220 days  =  618 h/yr  x  EUR 40/h  =  ~EUR 25k.   O1 range = machines x avoidable idle h/machine x EUR 250/machine-h.', 9.5, W, True, False, 0)],
      anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
caption(s, 0.50, y + 0.70, 12.33, 0.4,
        'Counted = summed into the floor. O1 is a ring-fenced sensitivity (never summed). O2-O4 are unsized potential - a HIGH chip flags the biggest next case (management reporting).',
        9)

# ================================================= 4 VALUE vs EFFORT (dependencies)
s = content('Value vs. dependencies to realize',
            'Y = likeliness the value lands (achievement). X = how many dependencies must line up. This is confidence-in-achievement, not confidence in the euro figure (that is the register).')
QX0, QX1 = 2.05, 11.60
QY0, QY1 = 2.55, 5.35
qmx = (QX0 + QX1) / 2
qmy = (QY0 + QY1) / 2
box(s, QX0, QY0, qmx - QX0, qmy - QY0, PERI, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
box(s, QX0, qmy - 0.01, QX1 - QX0, 0.02, NAVY, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
box(s, qmx - 0.01, QY0, 0.02, QY1 - QY0, NAVY, ml=0, mt=0, shape=MSO_SHAPE.RECTANGLE, adj=0)
caption(s, QX0 + 0.08, QY0 + 0.03, qmx - QX0 - 0.16, 0.3, 'DO FIRST - few dependencies', 9.5, italic=False, color=NAVY, bold=True)
caption(s, qmx + 0.10, QY0 + 0.03, QX1 - qmx - 0.16, 0.3, 'BIG BETS - line up the dependencies', 9.5, italic=False, color=DEEP, bold=True)
caption(s, QX0 + 0.08, QY1 - 0.30, qmx - QX0 - 0.16, 0.3, 'easy extras', 9, italic=True, color=NAVY)
caption(s, qmx + 0.10, QY1 - 0.30, QX1 - qmx - 0.16, 0.3, 'defer - low value, many dependencies', 9, italic=True, color=NAVY)
caption(s, QX0, QY1 + 0.06, QX1 - QX0, 0.3,
        'few dependencies to realize      ->      many dependencies to realize',
        9, italic=True, align=PP_ALIGN.CENTER, color=NAVY)
caption(s, 0.30, QY0 - 0.04, 1.72, 0.3, 'value likely lands', 8.5, italic=True, color=NAVY)
caption(s, 0.30, QY1 - 0.26, 1.72, 0.3, 'value uncertain', 8.5, italic=True, color=NAVY)


def qbub(impact, complexity, d, color, label, lx, ly, tc=NAVY):
    cx = QX0 + complexity * (QX1 - QX0)
    cy = QY1 - impact * (QY1 - QY0)
    box(s, cx - d / 2, cy - d / 2, d, d, color, ml=0.0, mt=0.0, shape=MSO_SHAPE.OVAL)
    caption(s, cx + lx, cy + ly, 3.1, 0.5, label, 9, italic=False, color=tc, bold=True)


qbub(0.80, 0.10, 0.44, GREEN, 'F  Admin floor', -0.62, 0.20)
qbub(0.55, 0.50, 0.46, PEACH, 'R  Reaction routine', 0.30, -0.10, DEEP)
qbub(0.78, 0.85, 0.52, TEAL, 'S  Cross-plant reuse', -0.05, 0.28, DEEP)
qbub(0.30, 0.22, 0.42, PERI, 'Soft / org potential', 0.26, -0.08)
# START-HERE detail: spell out why F is a self-contained, few-dependency step
det = box(s, 3.60, 2.86, 3.10, 1.08, W, ml=0.12, mt=0.08)
det.line.color.rgb = RGBColor.from_string(GREEN); det.line.width = Pt(1.0)
lines(det, [('Start here - why F is self-contained:', 9, DEEP, True, False, 3),
            ('- one decision: retire the paper board', 8.5, NAVY, False, False, 2),
            ('- one integration: the MES data link', 8.5, NAVY, False, False, 2),
            ('- no behaviour change; one area, one process', 8.5, NAVY, False, False, 0)])
caption(s, 0.50, 5.92, 12.33, 0.6,
        'Start with F - the narrowest, most self-contained step: it depends only on itself, so it lands almost certainly. R then adds a daily behaviour change; S adds many plants plus transferability. Value rises with dependencies - and so does the risk of it landing.',
        10)

# ================================================= 5 ABSTRACTED BPMN (marked differences)
s = content('Process, abstracted - only where it changes',
            'Three steps, two lanes. Numbered badges mark the differences the app makes; euros are detailed in the register.')
STEPS = ['1  Capture', '2  Detect & react', '3  Record & escalate']
LX = [0.60, 4.68, 8.76]
LWID = 3.72
# step headers
for i, st in enumerate(STEPS):
    caption(s, LX[i], 1.80, LWID, 0.3, st, 11, italic=False, color=NAVY, bold=True)
# lane labels
caption(s, 0.50, 2.28, 12.33, 0.3, 'TODAY - paper / whiteboard baseline', 11.5, italic=False, color=PEACH, bold=True)
today = ['Operator writes KPI on the board by hand',
         'Supervisor sweep every 1-2 h finds the problem',
         'Transcribe to Excel; escalate at the L2 meeting']
for i, tx in enumerate(today):
    b = box(s, LX[i], 2.58, LWID, 1.02, PEACH, ml=0.14, mt=0.10)
    lines(b, [(tx, 10, NAVY, False, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    if i < 2:
        box(s, LX[i] + LWID + 0.02, 2.58 + 0.51 - 0.10, 0.32, 0.20, NAVY, shape=MSO_SHAPE.RIGHT_ARROW, adj=0.5)
caption(s, 0.50, 4.02, 12.33, 0.3, 'WITH THE GEMBA APP', 11.5, italic=False, color=GREEN, bold=True)
app = ['One-tap / MES auto-capture at source',
       'Instant Andon push - act in minutes',
       'Auto-recorded once; recurrence + cross-plant']
delta = ['no manual entry  ->  H1+H2', 'latency  h -> min  ->  O1', 'auto record  ->  H3']
for i, tx in enumerate(app):
    b = box(s, LX[i], 4.32, LWID, 1.02, GREEN, ml=0.14, mt=0.10)
    lines(b, [(tx, 10, NAVY, False, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    if i < 2:
        box(s, LX[i] + LWID + 0.02, 4.32 + 0.51 - 0.10, 0.32, 0.20, NAVY, shape=MSO_SHAPE.RIGHT_ARROW, adj=0.5)
    # numbered change badge bridging the two lanes
    bd = box(s, LX[i] + LWID / 2 - 0.19, 3.68, 0.38, 0.38, NAVY, shape=MSO_SHAPE.OVAL, ml=0, mt=0)
    lines(bd, [(str(i + 1), 12, W, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    caption(s, LX[i], 5.40, LWID, 0.3, delta[i], 9, italic=False, align=PP_ALIGN.CENTER, color=NAVY, bold=True)
caption(s, 0.50, 5.88, 12.33, 0.6,
        'The process is unchanged except at the three numbered points - that is exactly where the value is created. Everything else stays the same.',
        10)

# ================================================= 6 SMART MILESTONES + TIME-TO-VALUE
s = content('Milestones - how fast we farm the value',
            'SMART milestones after approval; each is specific and measurable. Durations are placeholders to set at planning.')
caption(s, 0.50, 1.82, 12.33, 0.3,
        'Time-to-first-value: hard euros come online at M1, ~⟨set⟩ weeks after approval; the larger reaction value follows at M2.',
        10, italic=True, color=NAVY)
mw = (12.33 - 4 * 0.22) / 5
mx = [0.50 + i * (mw + 0.22) for i in range(5)]
mile = [
    (PERI, NAVY, 'M0  Baseline & integrate', 'MES link + escalation rules set; baseline measured.', 'T + ⟨..⟩ wks', PERI, NAVY, 'Enabling - no value', False),
    (GREEN, NAVY, 'M1  Go-live, board retired', '100% hourly entries digital; paper board removed.', 'T + ⟨..⟩ wks', NAVY, GREEN, 'HARD value ON ~EUR 22-27k', True),
    (PEACH, NAVY, 'M2  Reaction routine embedded', 'Andon acted on < ⟨..⟩ min; cause codes on most events.', 'T + ⟨..⟩ wks', NAVY, GREEN, 'REACTION value ON ~EUR 37k', True),
    (BLUE, W, 'M3  Proven on dashboard', 'Before->after confirmed on the OPEX dashboard.', 'T + ⟨..⟩ wks', PERI, NAVY, 'Value confirmed', False),
    (TEAL, NAVY, 'M4  Scaled to ⟨N⟩ sites', 'Repeat M1-M3 per site across the footprint.', 'T + ⟨..⟩', PERI, NAVY, 'Program ceiling', False),
]
CY, CH = 2.42, 2.02
for i, (cf, tc, title, meas, dur, tf, ttc, ttext, unlocked) in enumerate(mile):
    sh = box(s, mx[i], CY, mw, CH, cf, ml=0.13, mt=0.13)
    lines(sh, [(title, 10.5, tc, True, False, 5),
               (meas, 9, tc, False, False, 6),
               (dur, 9, tc, True, True, 0)])
    if i < 4:
        box(s, mx[i] + mw + 0.01, CY + CH / 2 - 0.10, 0.20, 0.20, NAVY, shape=MSO_SHAPE.RIGHT_ARROW, adj=0.5)
    tg = box(s, mx[i], CY + CH + 0.12, mw, 0.78, tf, ml=0.10, mt=0.08)
    lines(tg, [(ttext, 9, ttc, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    if unlocked:
        bd = box(s, mx[i] - 0.05, CY - 0.20, 0.40, 0.40, GREEN, shape=MSO_SHAPE.OVAL, ml=0, mt=0)
        lines(bd, [('EUR', 8.5, NAVY, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
caption(s, 0.50, 5.62, 12.33, 0.7,
        'The hard lever comes online first at go-live (lowest dependency); the larger reaction lever follows once the routine is embedded. A paper board kept in parallel means M1 never completes and the saving stays zero.',
        10)

# ================================================= 7 SOFT IMPACT CLUSTERS
s = content('Soft & strategic stakes not in the equation',
            'These are not in the headline number. They raise the stake of doing this - mainly soft savings and option value.')
CW, XS = cols(2)
sh = box(s, XS[0], 1.98, CW, 3.55, PEACH, ml=0.22, mt=0.18)
lines(sh, [('People & operating discipline', 12.5, NAVY, True, False, 9),
           ('Onboarding / language - multilingual, voice entry', 10.5, NAVY, False, False, 7),
           ('Shift-handover losses closed by a shared record', 10.5, NAVY, False, False, 7),
           ('Safety - faster hazard capture and closure', 10.5, NAVY, False, False, 7),
           ('Less firefighting - standard work holds under stress', 10.5, NAVY, False, False, 0)])
sh = box(s, XS[1], 1.98, CW, 3.55, PERI, ml=0.22, mt=0.18)
lines(sh, [('Organisation & option value', 12.5, NAVY, True, False, 9),
           ('Cross-plant learning - scales with the rollout', 10.5, NAVY, False, False, 7),
           ('Audit / compliance readiness - digital record', 10.5, NAVY, False, False, 7),
           ('Data foundation - clean shopfloor data for AI', 10.5, NAVY, False, False, 7),
           ('Platform / option value for further use cases', 10.5, NAVY, False, False, 0)])
caption(s, 0.50, 5.74, 12.33, 0.7,
        'Kept qualitative on purpose - big but undependable value is not forced into a number. Operational levers that can be sized (availability, scrap, reporting) live in the register as O2-O4. Reviewer: which of these are real here?',
        10)

# ================================================= 8 REFINEMENT - LED BY WORKED EXAMPLES
s = content('Refinement - the inputs that move the case',
            'Each block leads with a worked example (easy to correct), then the proxy questions. Answer a block, close a sub-case.')
CW, XS = cols(2)


def refblock(l, t, w, h, fill, header, example, qs):
    sh = box(s, l, t, w, h, fill, ml=0.18, mt=0.13)
    rows = [(header, 11, NAVY, True, False, 5),
            ('Example: ' + example, 9, NAVY, False, True, 6)]
    for q in qs:
        rows.append(('-  ' + q, 9.5, NAVY, False, False, 3))
    lines(sh, rows)
    return sh


refblock(XS[0], 1.92, CW, 2.02, PEACH, 'R - Reaction    moves the case most',
         '~25 idle h/machine/yr recovered -> +~EUR 37k; only ~3 h -> +~EUR 5k.',
         ['Q5. Hours/yr a machine waits for a reaction? (crucial)',
          'Q6. Time to help today - minutes, or an hour+?',
          'Q4. Cost of one idle machine-hour? (EUR 100 / 250 / 500)'])
refblock(XS[0], 4.08, CW, 1.78, GREEN, 'F - Admin floor    already banked',
         'each +1 min of admin per line/shift -> +~EUR 2k/yr.',
         ['Q1. Minutes/hour on the board + shift-end Excel?',
          'Q2. After the app: writing left, or fully replaced?'])
refblock(XS[1], 1.92, CW, 1.78, TEAL, 'S - Rollout    the big multiplier',
         'each added paper plant -> +~EUR 22-27k/yr on the floor.',
         ['Q3. Machines / lines in the first area?',
          'Q10 / Q11. Which plant starts; how many still on paper?'])
refblock(XS[1], 3.92, CW, 1.94, PERI, 'G - Go-live gate    make-or-break',
         'board kept in parallel -> no admin saving -> EUR 0.',
         ['Q7. Board off at go-live, or run in parallel?',
          'Q9. Who watches the live screen and can act?'])
caption(s, 0.50, 6.02, 12.33, 0.5,
        'Ranked by how much each moves the total: R moves the case most, then the S multiplier, then F. G is the gate that switches the floor on. Cost/effort is firmed on the investment file.',
        9.5)

# ================================================= 9 PROVENANCE & CONFLICTS (appendix)
s = content('Provenance & conflicts across the inputs',
            'Left: which input files fed the BC and what each contributed. Right: where sources disagreed, and how each was resolved into the case.')
# ---- Left column: input inventory
LX0, LW = 0.50, 4.15
caption(s, LX0, 1.86, LW, 0.28, 'Input files -> what the BC drew from each', 10, italic=False, color=PERI, bold=True)
# (filename, contributed, tag, tagcolor)
srcs = [
    ('gemba-alignment-transcript.md', 'Current-state process, media breaks, sweep cadence, operating model', '[input] structure', BLUE),
    ('gemba-management.html (mockup)', 'Target-state capabilities; pins each lever to a process step', '[input] structure', BLUE),
    ('...business-case-REFERENCE.md', 'Earlier lever set + formulas (superseded - see conflicts)', '[assumption]', PEACH),
    ('interview-cross-check.md', 'Gap flags: no quantities, baseline open, single-source bias', 'caveat', MELONL),
    ('business-case.md (backbone)', 'Final levers H1-H3 / O1-O4, headline, grounding tags', 'source of truth', GREEN),
]
ly = 2.18
LH = 0.80
for name, contrib, tag, tc in srcs:
    b = box(s, LX0, ly, LW, LH, W, ml=0.12, mt=0.07)
    b.line.color.rgb = RGBColor.from_string(GRY); b.line.width = Pt(0.5)
    lines(b, [(name, 9.5, NAVY, True, False, 2),
              (contrib, 8, NAVY, False, False, 3),
              (tag, 8, tc if tc != MELONL else MELOND, True, False, 0)])
    ly += LH + 0.09
# ---- Right column: conflict register
RX, RW = 4.90, 7.93
caption(s, RX, 1.86, RW, 0.28, 'Thesis / assumption conflicts -> how each flowed into the BC', 10, italic=False, color=PERI, bold=True)
# (conflict, resolution, residual)
confs = [
    ('Hard-lever count: REFERENCE H1-H4 vs final H1-H3',
     'H4 Gemba-walk doc de-scoped from the banked floor to soft clusters (slide 7).', 'not banked'),
    ('Reaction O1 formula changed (latency x events  vs  machines x idle-h)',
     'Adopted the machine-based, sourceable form; crucial idle-h stays [unknown] -> O1 de-banked as ~EUR 5-56k.', 'de-banked'),
    ('"4 min" per entry - floated earlier, in no source',
     'Deliberately not enshrined; admin time derived from the 1-2 h sweep cadence.', 'assumption'),
    ('Baseline asked in interview (13:31) but left unanswered',
     'Analyst-set to a representative paper/whiteboard plant; carried as the top open question.', 'assumption'),
    ('Interview holds zero quantities; single source + leading Qs',
     'Every euro tagged [assumption]/[market]; structure is [input]. Case signed on logic, sized after one data round.', 'maturity gate'),
    ('Management reporting: described in sources but uncounted',
     'Kept [input]-grounded but out of the floor (O4, HIGH chip) - the candidate 2nd hard lever.', 'uncounted'),
]
ry2 = 2.18
CH2 = 0.66
for conf, res, resid in confs:
    b = box(s, RX, ry2, RW, CH2, MELONL, ml=0.14, mt=0.06)
    lines(b, [(conf + '   [' + resid + ']', 8.5, MELOND, True, False, 2),
              (res, 8, NAVY, False, False, 0)])
    ry2 += CH2 + 0.055
caption(s, LX0, 6.52, 12.33, 0.5,
        'The structure is [input] from the interview + mockup; every magnitude is [assumption] or [market] pending one quantitative round. Conflicts were resolved toward the more sourceable, lower-risk option and quarantined where an input is still missing.',
        9)

prs.save(OUT)
print('written', OUT, 'slides:', len(prs.slides._sldIdLst))
