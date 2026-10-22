"""Slides 8-14 and appendix."""
import math

from lxml import etree
from pptx.enum.dml import MSO_LINE
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.util import Pt

import deck_data as D
from deckkit import *
from slides_a import A, SLIDE_W, grp_text


# ------------------------------------------------------------------ 8 model
def model(sl, ctx, mode="anim"):
    sh = sl.shapes
    an = Anim()
    top = group(sh)
    text(top.shapes, 0.79, 2.70, 8.5, 0.32,
         [[("Shopper pays 28,000 IQD at the door", dict(size=16, bold=True)),
           ("   (25,000 item + 3,000 Duhok delivery)", dict(size=12, color=INK60))]],
         anchor="m")
    base = group(sh)
    rect(base.shapes, 0.79, 3.15, 11.75, 0.85, fill=NEUTRAL)
    text(base.shapes, 0.79, 3.15, 11.75, 0.85, "28,000 IQD", size=16, bold=True, align="c",
         anchor="m")
    if mode == "bar":
        return None
    wM, wC, wH = 10.093, 1.049, 0.608
    xM, xC, xH = 0.79, 0.79 + wM, 0.79 + wM + wC
    segM, segC, segH = group(sh), group(sh), group(sh)
    rect(segM.shapes, xM, 3.15, wM, 0.85, fill=BLUE)
    rect(segC.shapes, xC, 3.15, wC, 0.85, fill=INK60)
    rect(segH.shapes, xH, 3.15, wH, 0.85, fill=INK)
    lM = group(sh)
    text(lM.shapes, 0.79, 4.10, 8.0, 0.34,
         [[("Merchant 24,050 IQD — keeps ", dict(size=14, bold=True)),
           ("96%", dict(size=14, bold=True, color=BLUE)),
           (" of the item price", dict(size=14, bold=True))]], anchor="m")
    lC = group(sh)
    cx = xC + wC / 2
    line(lC.shapes, cx, 4.02, cx, 4.28, INK60, 1.0)
    text(lC.shapes, 8.9, 4.12, cx - 0.08 - 8.9, 0.30, "Courier 2,500", size=13, bold=True,
         align="r", anchor="m")
    lH = group(sh)
    hx = xH + wH / 2
    line(lH.shapes, hx, 4.02, hx, 4.62, INK, 1.0)
    text(lH.shapes, 10.4, 4.50, hx - 0.08 - 10.4, 0.30, "Cheapify 1,450", size=13, bold=True,
         align="r", anchor="m")
    callout = grp_text(sh, 8.5, 2.70, 4.04, 0.40, "950 fee + 500 delivery margin", size=12,
                       color=INK60, align="r", anchor="m")

    fee_title = group(sh)
    text(fee_title.shapes, 0.79, 4.95, 1.55, 1.0, "Our fee gets lighter as prices rise", size=15,
         bold=True)
    cols = []
    for i, (h, v, cap) in enumerate([(1.35, "5%", "first 10,000 IQD"),
                                      (0.81, "3%", "10,001 – 100,000"),
                                      (0.41, "1.5%", "above 100,000")]):
        x = 2.55 + i * 1.40
        g = group(sh)
        rect(g.shapes, x, 6.55 - h, 1.2, h, fill=BLUE)
        text(g.shapes, x - 0.2, 6.55 - h - 0.40, 1.6, 0.36, v, size=20, bold=True,
             font="Comfortaa", align="c", anchor="m")
        text(g.shapes, x - 0.2, 6.60, 1.6, 0.25, cap, size=11, color=INK60, align="c")
        cols.append(g)
    big = grp_text(sh, 6.90, 4.95, 5.64, 0.85, "≈ 1,100 IQD", size=44, bold=True,
                   font="Comfortaa", anchor="m")
    bigsub = grp_text(sh, 6.90, 5.85, 5.4, 0.6,
                      "kept per delivered order after messaging, failed-delivery and return costs",
                      size=13, color=INK60)
    if mode == "anim":
        an.add([[fx(top), fx(base)]], auto=True)
        an.add([[fx(segM), fx(lM)]])
        an.add([[fx(segC), fx(lC)]])
        an.add([[fx(segH), fx(lH), fx(callout)]])
        an.add([[fx(fee_title)]] + stagger(cols, "zoom", 150) + [[fx(big, "zoom", 200), fx(bigsub, "fade", 200)]])
    return an


# ------------------------------------------------------------------ 9 competitors
def competitors(sl, ctx):
    sh = sl.shapes
    an = Anim()
    cx = [5.30, 6.90, 8.50, 10.10, 11.70]
    rows_y = [3.45, 4.20, 4.95, 5.70]
    base = group(sh)
    for (lbl, _), y in zip(D.COMP_ROWS, rows_y):
        text(base.shapes, 0.79, y, 3.5, 0.75, lbl, size=15, bold=True, anchor="m")
    for i in range(4):
        text(base.shapes, cx[i] - 0.8, 2.80, 1.6, 0.55, D.COMP_COLS[i], size=13, bold=True,
             align="c", anchor="m")
    for y in rows_y[:-1]:
        line(base.shapes, 0.79, y + 0.75, 10.70, y + 0.75, NEUTRAL, 0.75)
    line(base.shapes, 0.79, rows_y[0] - 0.03, 10.70, rows_y[0] - 0.03, NEUTRAL, 0.75)
    line(base.shapes, 0.79, rows_y[-1] + 0.75, 10.70, rows_y[-1] + 0.75, NEUTRAL, 0.75)

    mk = {"yes": ("circle-check", INK60), "partly": ("contrast", INK60), "no": ("circle-x", RED)}
    comp_cols = []
    for ci in range(4):
        g = group(sh)
        for ri, (_, vals) in enumerate(D.COMP_ROWS):
            name, col = mk[vals[ci]]
            icon_c(g.shapes, name, col, cx[ci], rows_y[ri] + 0.375, 0.36)
        comp_cols.append(g)
    # cheapify column
    ch = group(sh)
    rect(ch.shapes, 10.90, 2.70, 1.60, 3.80, fill=BLUE12, line=BLUE, lw=1.5, radius=0.14)
    pic_contain(ch.shapes, A("cheapify-logo.png"), 10.98, 2.88, 0.22, 0.30)
    text(ch.shapes, 11.24, 2.80, 1.2, 0.55, "Cheapify", size=13, bold=True, color=BLUE,
         anchor="m")
    marks = []
    for ri, (_, vals) in enumerate(D.COMP_ROWS):
        name, col = mk[vals[4]]
        col = GREEN if vals[4] == "yes" else col
        g = group(sh)
        icon_c(g.shapes, name, col, cx[4], rows_y[ri] + 0.375, 0.36)
        marks.append(g)
    leg = group(sh)
    x = 0.79
    for name, col, lbl in (("circle-check", INK60, "yes"), ("contrast", INK60, "partly"),
                           ("circle-x", RED, "no")):
        icon(leg.shapes, name, col, x, 6.60, 0.22)
        text(leg.shapes, x + 0.30, 6.58, 0.8, 0.26, lbl, size=11, color=INK60, anchor="m")
        x += 1.25
    an.add([[fx(base), fx(leg)]], auto=True)
    an.add([[fx(comp_cols[0])]] + [[fx(c, delay=200)] for c in comp_cols[1:]])
    an.add([[fx(ch, "zoom")]] + stagger(marks, "zoom", 120))
    return an


# ------------------------------------------------------------------ 10 growth
def growth(sl, ctx):
    sh = sl.shapes
    an = Anim()
    C = (3.90, 4.75)
    R = 1.55
    ringg = group(sh)
    oval(ringg.shapes, C[0], C[1], R, line=BLUE, lw=2.0)
    pic_contain(ringg.shapes, A("cheapify-logo.png"), C[0] - 0.275, C[1] - 0.354, 0.55, 0.707)
    nodes_def = [((3.90, 3.20), "store", "A store joins", 135),
                 ((6.00, 4.75), "link", "Adds its Cheapify link to its bio", 45),
                 ((3.90, 6.30), "users", "Its followers order on Cheapify", -45),
                 ((1.80, 4.75), "trending-up", "More orders bring more stores", -135)]
    nodes, tris = [], []
    for (nx, ny), ic, t, ang in nodes_def:
        g = group(sh)
        card(g.shapes, nx - 1.0, ny - 0.475, 2.0, 0.95)
        icon(g.shapes, ic, BLUE, nx - 0.88, ny - 0.16, 0.32)
        text(g.shapes, nx - 0.45, ny - 0.40, 1.38, 0.80, t, size=13, bold=True, anchor="m")
        nodes.append(g)
        th = math.radians(ang)
        px, py = C[0] + R * math.cos(th), C[1] - R * math.sin(th)
        dx, dy = math.sin(th), math.cos(th)
        rot = math.degrees(math.atan2(dx, -dy))
        tg = group(sh)
        tri = rect(tg.shapes, px - 0.10, py - 0.10, 0.20, 0.20, fill=BLUE,
                   shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
        tri.rotation = rot
        tris.append(tg)
    cap = grp_text(sh, 2.40, 6.82, 3.0, 0.24, "≈ zero cost to acquire these shoppers", size=11,
                   color=INK60, align="c", anchor="m")
    phases = []
    for i, (a, b, c) in enumerate([("Phase 1 · Months 1–6", "Duhok", "20 founding stores · 3,000+ orders"),
                                    ("Phase 2 · Months 7–15", "Erbil · Mosul · Sulaymaniyah", "75 stores"),
                                    ("Phase 3 · Month 16+", "All of Iraq", "300+ stores")]):
        y = 2.80 + i * 1.15
        g = group(sh)
        card(g.shapes, 8.00, y, 4.54, 1.00)
        text(g.shapes, 8.20, y + 0.10, 4.1, 0.22, a, size=11, color=BLUE, anchor="m")
        text(g.shapes, 8.20, y + 0.32, 4.1, 0.32, b, size=16, bold=True, anchor="m")
        text(g.shapes, 8.20, y + 0.66, 4.1, 0.24, c, size=12, color=INK60, anchor="m")
        phases.append(g)
    chip = group(sh)
    rect(chip.shapes, 8.00, 6.30, 4.54, 0.45, fill=BLUE12, radius=0.22)
    text(chip.shapes, 8.10, 6.30, 4.34, 0.45, "Founding stores: 0% commission in month 1 + free ads",
         size=11, bold=True, align="c", anchor="m")
    an.add([[fx(ringg)]], auto=True)
    an.add([[fx(nodes[0]), fx(tris[0])]])
    an.add([[fx(nodes[1]), fx(tris[1])]])
    an.add([[fx(nodes[2]), fx(tris[2]), fx(cap)]])
    an.add([[fx(nodes[3]), fx(tris[3])]])
    an.add(stagger(phases, "fade", 150) + [[fx(chip)]])
    return an


# ------------------------------------------------------------------ 11 finance
def finance(sl, ctx):
    sh = sl.shapes
    an = Anim()
    kpis = []
    for i, (big, tail, sub) in enumerate([("~585", " orders / month", "break-even · about 1 order per store per day"),
                                           ("~1,115 IQD", "", "kept per delivered order"),
                                           ("Month 4", "", "monthly break-even (planning case)")]):
        y = 2.75 + i * 1.35
        g = group(sh)
        card(g.shapes, 0.79, y, 3.30, 1.22)
        runs = [(big, dict(size=24, bold=True, font="Comfortaa"))]
        if tail:
            runs.append((tail, dict(size=14, bold=True, font="Comfortaa")))
        text(g.shapes, 1.00, y + 0.14, 3.0, 0.50, [runs], anchor="m")
        text(g.shapes, 1.00, y + 0.70, 3.0, 0.40, sub, size=12, color=INK60)
        kpis.append(g)

    PX0, PX1 = 4.90, 12.30
    X = lambda i: PX0 + i * (PX1 - PX0) / 12
    Y = lambda v: 3.05 + (2500 - v) * (6.55 - 3.05) / 5500
    axes = group(sh)
    for v, lab in ((2000, "+$2k"), (1000, "+$1k"), (0, "$0"), (-1000, "−$1k"), (-2000, "−$2k"),
                   (-3000, "−$3k")):
        if v != 0:
            line(axes.shapes, PX0, Y(v), PX1, Y(v), NEUTRAL, 0.5)
        text(axes.shapes, 4.20, Y(v) - 0.11, 0.6, 0.22, lab, size=10, color=INK60, align="r",
             anchor="m")
    line(axes.shapes, PX0, Y(0), PX1, Y(0), INK, 1.0)
    text(axes.shapes, PX0 + 0.05, Y(0) - 0.26, 1.5, 0.22, "break-even line", size=10, color=INK60,
         align="l", anchor="m")
    for idx, lab in ((0, "Start"), (2, "Launch"), (4, "M2"), (6, "M4"), (8, "M6"), (10, "M8"),
                     (12, "M10")):
        text(axes.shapes, X(idx) - 0.4, 6.62, 0.8, 0.22, lab, size=10, color=INK60, align="c",
             anchor="m")
    pl = D.CHART_PLANNING
    segs = []
    for i in range(12):
        g = group(sh)
        c = line(g.shapes, X(i), Y(pl[i]), X(i + 1), Y(pl[i + 1]), BLUE, 3.0)
        ln = c.line._get_or_add_ln()
        ln.set("cap", "rnd")
        segs.append(g)
    sl_pts = D.CHART_SLOW
    slow = group(sh)
    fb = slow.shapes.build_freeform(E(X(0)), E(Y(sl_pts[0])), scale=1.0)
    fb.add_line_segments([(E(X(i)), E(Y(sl_pts[i]))) for i in range(1, 13)], close=False)
    ff = fb.convert_to_shape()
    ff.fill.background()
    ff.line.color.rgb = rgb(INK35)
    ff.line.width = Pt(2.0)
    ff.line.dash_style = MSO_LINE.DASH
    no_effect(ff)

    def marker(idx, vals, color, label, lx, ly, lw, align, leader_to=None, color_txt=INK, lh=0.24):
        g = group(sh)
        cx, cy = X(idx), Y(vals[idx])
        if leader_to is not None:
            line(g.shapes, cx, cy, cx, leader_to, color, 1.0)
        oval(g.shapes, cx, cy, 0.08, fill=color, line=WHITE, lw=1.0)
        text(g.shapes, lx, ly, lw, lh, label, size=11, bold=True, color=color_txt, align=align,
             anchor="m")
        return g

    m3 = marker(5, pl, RED, "Lowest point −$2,180 (month 3)", 5.20, 4.15, 2.76, "r", 4.42, RED)
    m4 = marker(6, pl, BLUE, "Monthly break-even (month 4)", 8.70, 4.15, 2.30, "l", 4.42, BLUE)
    m8 = marker(10, pl, INK, "All losses recovered (month 8)", 7.9, 3.55, 3.13, "r", 3.82, INK)
    ms = group(sh)
    cx, cy = X(8), Y(sl_pts[8])
    oval(ms.shapes, cx, cy, 0.08, fill=INK35, line=WHITE, lw=1.0)
    line(ms.shapes, cx + 0.06, cy - 0.06, cx + 0.16, cy - 0.30, INK35, 1.0)
    text(ms.shapes, cx + 0.18, 5.62, 2.2, 0.40,
         ["Worst case −$2,750", "(half-speed growth)"], size=11, bold=True, color=INK60, anchor="m")

    an.add([[fx(kpis[0])]] + [[fx(k, delay=150)] for k in kpis[1:]], auto=True)
    an.add([[fx(axes)]] + [[fx(s, "appear", 70)] for s in segs[:5]] + [[fx(m3, "zoom")]])
    an.add([[fx(segs[5], "appear")], [fx(m4, "zoom")]])
    an.add([[fx(s, "appear", 70)] for s in segs[6:]] + [[fx(m8, "zoom")]])
    an.add([[fx(slow), fx(ms, "zoom")]])
    return an


# ------------------------------------------------------------------ 12 funding
def _arc(parent, cx, cy, ro, ri, a0, a1, fill, line_col=None):
    sp = parent.add_shape(MSO_SHAPE.BLOCK_ARC, E(cx - ro), E(cy - ro), E(2 * ro), E(2 * ro))
    av = sp._element.spPr.find(qn("a:prstGeom")).find(qn("a:avLst"))
    for ch in list(av):
        av.remove(ch)
    thick = (ro - ri) / (2 * ro)
    for name, val in (("adj1", int((a0 % 360) * 60000)), ("adj2", int((a1 % 360) * 60000)),
                      ("adj3", int(thick * 100000))):
        etree.SubElement(av, qn("a:gd"), name=name, fmla=f"val {val}")
    sp.fill.solid()
    sp.fill.fore_color.rgb = rgb(fill)
    if line_col:
        sp.line.color.rgb = rgb(line_col)
        sp.line.width = Pt(0.75)
    else:
        sp.line.fill.background()
    no_effect(sp)
    return sp


def funding(sl, ctx):
    sh = sl.shapes
    an = Anim()
    cx, cy, ro, ri = 2.70, 4.75, 1.75, 1.05
    center = group(sh)
    text(center.shapes, cx - 1.0, cy - 0.38, 2.0, 0.5, "$7,500", size=32, bold=True,
         font="Comfortaa", align="c", anchor="m")
    text(center.shapes, cx - 1.0, cy + 0.14, 2.0, 0.28, "≈ 11.25M IQD", size=12, color=INK60,
         align="c", anchor="m")
    colors = dict(INK=INK, BLUE=BLUE, INK60=INK60, BLUE50=BLUE50, NEUTRAL=NEUTRAL, ORANGE=ORANGE)
    ang = 270.0
    steps = []
    for i, (label, usd, deg, ck) in enumerate(D.DONUT):
        g = group(sh)
        _arc(g.shapes, cx, cy, ro, ri, ang, ang + deg, colors[ck], INK35 if ck == "NEUTRAL" else None)
        ang += deg
        y = 3.05 + i * 0.48
        lg = group(sh)
        rect(lg.shapes, 4.80, y + 0.04, 0.22, 0.22, fill=colors[ck], line=INK35 if ck == "NEUTRAL" else None,
             lw=0.75, radius=0.04)
        text(lg.shapes, 5.12, y, 2.45, 0.30, label, size=12, anchor="m")
        text(lg.shapes, 7.55, y, 0.65, 0.30, f"${usd:,}", size=13, bold=True, align="r", anchor="m")
        steps.append([fx(g, delay=150), fx(lg, delay=150)])
    callout = group(sh)
    rect(callout.shapes, 8.60, 5.98, 3.94, 0.94, fill=BLUE12, radius=0.12)
    icon(callout.shapes, "code", BLUE, 8.76, 6.10, 0.28)
    text(callout.shapes, 9.14, 6.04, 3.30, 0.46, "Built in-house: $0 to developers · $0 salaries",
         size=13, bold=True, anchor="m")
    text(callout.shapes, 9.14, 6.52, 3.30, 0.34,
         "Founder in-kind contribution ≈ $9,500 (equipment + build time)", size=10.5,
         color=INK60, anchor="t")
    tt = grp_text(sh, 8.60, 2.80, 3.94, 0.30, "Every rank funds a complete plan", size=15,
                  bold=True, anchor="m")
    tiers = []
    for i, (a, b) in enumerate([("1st · $7,500", "Full plan: launch + growth marketing"),
                                 ("2nd · $4,500", "Launch, registration and pilot; slower growth"),
                                 ("3rd · $2,500", "Covers the launch gap; growth stays organic")]):
        y = 3.25 + i * 0.90
        g = group(sh)
        card(g.shapes, 8.60, y, 3.94, 0.80)
        text(g.shapes, 8.80, y + 0.08, 3.6, 0.28, a, size=15, bold=True, color=BLUE, anchor="m")
        text(g.shapes, 8.80, y + 0.40, 3.6, 0.34, b, size=12, color=INK60, anchor="t")
        tiers.append(g)
    an.add([[fx(center, "zoom")]], auto=True)
    for e in steps[0]:
        e.delay = 0
    an.add(steps)
    an.add([[fx(callout)]])
    an.add([[fx(tt)]] + stagger(tiers, "fade", 150))
    return an


# ------------------------------------------------------------------ 13 next
def next_steps(sl, ctx):
    sh = sl.shapes
    an = Anim()
    ln = group(sh)
    c = line(ln.shapes, 1.20, 4.40, 12.10, 4.40, NEUTRAL, 3.0)
    xs = [1.60, 4.15, 6.70, 9.25, 11.80]
    items = []
    for i, ((when, title, sub), x) in enumerate(zip(D.TIMELINE, xs)):
        n = group(sh)
        oval(n.shapes, x, 4.40, 0.21, fill=BLUE)
        text(n.shapes, x - 0.21, 4.19, 0.42, 0.42, str(i + 1), size=13, bold=True, color=WHITE,
             align="c", anchor="m")
        w = group(sh)
        text(w.shapes, x - 1.15, 3.70, 2.30, 0.30, when, size=13, bold=True, color=BLUE,
             align="c", anchor="m")
        cd = group(sh)
        card(cd.shapes, x - 1.15, 4.75, 2.30, 1.55)
        text(cd.shapes, x - 1.00, 4.88, 2.0, 0.70, title.replace(": ", ":\n").split("\n"),
             size=14, bold=True)
        text(cd.shapes, x - 1.00, 5.62, 2.0, 0.60, sub, size=11.5, color=INK60)
        items.append((n, w, cd))
    kpi = group(sh)
    icon(kpi.shapes, "chart-column", BLUE, 0.79, 6.60, 0.26)
    text(kpi.shapes, 1.15, 6.55, 11.4, 0.35,
         "We report monthly: delivered orders · sales volume · active stores · repeat orders · delivery time",
         size=12, color=INK60, anchor="m")
    an.add([[fx(ln)]], auto=True)
    for i, (n, w, cd) in enumerate(items):
        step = [fx(n, "zoom"), fx(w), fx(cd)]
        an.add([step])
    # KPI strip fades after node 5 within the last click group
    an.groups[-1][1].append([fx(kpi, delay=200)])
    return an


# ------------------------------------------------------------------ 14 thanks
def thanks(sl, ctx):
    sh = sl.shapes
    w = 1.05
    logo, _ = pic_contain(sh, A("cheapify-logo.png"), (SLIDE_W - w) / 2, 1.70, w, w * 9 / 7)
    t1 = text(sh, 0, 3.10, SLIDE_W, 0.8, "Thank you", size=46, bold=True, font="Comfortaa",
              align="c", anchor="m")
    t2 = text(sh, 0, 3.95, SLIDE_W, 0.42, "The bright side of choosing.", size=20, color=BLUE,
              font="Comfortaa", align="c", anchor="m")
    t3 = text(sh, 0, 4.42, SLIDE_W, 0.42, "ڕوویێ گەش یێ هەلبژارتنێ", size=20,
              font="IBM Plex Sans Arabic", align="c", anchor="m", rtl=True)
    t4 = text(sh, 0, 4.88, SLIDE_W, 0.42, "الجانب المشرق للاختيار", size=20,
              font="IBM Plex Sans Arabic", align="c", anchor="m", rtl=True)
    t5 = text(sh, 0, 5.42, SLIDE_W, 0.30, "getcheapify.com", size=16, bold=True, color=BLUE,
              align="c", anchor="m")
    t6 = text(sh, 0, 5.75, SLIDE_W, 0.28, "Shakir Bashar · Founder", size=13, color=INK60,
              align="c", anchor="m")
    an = Anim()
    an.add([[fx(logo, "zoom")], [fx(t, delay=0) for t in (t1, t2, t3, t4, t5, t6)]], auto=True)
    return an


# ------------------------------------------------------------------ appendix
def _cell_border(cell, color=NEUTRAL, w=9525):
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        for old in tcPr.findall(qn(tag)):
            tcPr.remove(old)
    for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
        ln = etree.SubElement(tcPr, qn(tag), w=str(w), cap="flat", cmpd="sng", algn="ctr")
        sf = etree.SubElement(ln, qn("a:solidFill"))
        etree.SubElement(sf, qn("a:srgbClr"), val=color)
        etree.SubElement(ln, qn("a:prstDash"), val="solid")
    # borders must precede fill in tcPr
    fill = tcPr.find(qn("a:solidFill"))
    if fill is not None:
        tcPr.remove(fill)
        tcPr.append(fill)


def table(sl, x, y, w, header, rows, col_w, row_h=0.34, size=12, align=None, bold_last=False):
    shp = sl.shapes.add_table(len(rows) + 1, len(header), E(x), E(y), E(w), E(row_h * (len(rows) + 1)))
    tbl = shp.table
    tblPr = tbl._tbl.tblPr
    for a in ("firstRow", "bandRow"):
        tblPr.set(a, "0")
    sid = tblPr.find(qn("a:tableStyleId"))
    if sid is not None:
        tblPr.remove(sid)
    tot = sum(col_w)
    for i, cw in enumerate(col_w):
        tbl.columns[i].width = E(w * cw / tot)
    for r in range(len(rows) + 1):
        tbl.rows[r].height = E(row_h)
        for c in range(len(header)):
            cell = tbl.cell(r, c)
            txt = header[c] if r == 0 else rows[r - 1][c]
            cell.margin_left = cell.margin_right = E(0.10)
            cell.margin_top = cell.margin_bottom = E(0.03)
            cell.vertical_anchor = ANCHOR["m"]
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = ALIGN[(align[c] if align else "l")]
            run = p.add_run()
            run.text = txt
            f = run.font
            f.size = Pt(size)
            f.bold = (r == 0) or (bold_last and r == len(rows))
            f.color.rgb = rgb(INK)
            rPr = run._r.get_or_add_rPr()
            rPr.set("lang", "en-US")
            for tag in ("a:latin", "a:cs"):
                etree.SubElement(rPr, qn(tag), typeface="Inter")
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(NEUTRAL if r == 0 else WHITE)
            _cell_border(cell)
    return shp


def appendix(sl, key, ctx):
    d = D.APPENDIX[key]
    sh = sl.shapes
    an = Anim()
    target = None
    if key == "A1":
        text(sh, 0.79, 2.65, 11.75, 0.60, d["line"], size=12, color=INK60)
        target = table(sl, 0.79, 3.40, 11.75, d["header"], d["rows"], [1, 1, 1], row_h=0.36,
                       align=["l", "r", "r"])
    elif key == "A2":
        t1 = table(sl, 0.79, 2.65, 11.75, d["header"], d["rows"], [4, 1], row_h=0.29,
                   align=["l", "r"], bold_last=True)
        text(sh, 0.79, 5.04, 11.75, 0.26, d["caption"], size=12, bold=True)
        table(sl, 0.79, 5.36, 11.75, d["header2"], d["rows2"], [3, 1.4, 1.8], row_h=0.29,
              align=["l", "r", "r"])
        target = t1
    elif key == "A3":
        target = table(sl, 0.79, 2.80, 11.75, d["header"], d["rows"], [1.6, 1.4, 1.5, 1.4, 1.4],
                       row_h=0.50, align=["l", "r", "r", "r", "r"])
        text(sh, 0.79, 5.00, 11.75, 0.30, d["note"], size=12, color=INK60)
    elif key == "A4":
        g = group(sh)
        for x, title, items in ((0.79, d["shoppers_title"], d["shoppers"]),
                                (6.85, d["merchants_title"], d["merchants"])):
            text(g.shapes, x, 2.75, 5.7, 0.34, title, size=16, bold=True, color=BLUE)
            text(g.shapes, x, 3.20, 5.7, 3.4, items, size=13, spacing=1.1)
        text(g.shapes, 0.79, 6.55, 11.75, 0.40, d["bottom"], size=11, color=INK60)
        target = g
        for tb in g.shapes:
            if tb.has_text_frame and len(tb.text_frame.paragraphs) > 1:
                for p in tb.text_frame.paragraphs:
                    p.space_after = Pt(9)
    elif key == "A5":
        target = table(sl, 0.79, 2.75, 11.75, d["header"], d["rows"], [2.4, 1.7, 1.7, 1.2, 2.6],
                       row_h=0.50)
        text(sh, 0.79, 6.45, 11.75, 0.30, d["note"], size=12, color=INK60)
    elif key == "A6":
        target = table(sl, 0.79, 2.75, 11.75, d["header"], d["rows"], [2.6, 6.2], row_h=0.70)
    elif key == "A7":
        g = group(sh)
        n = len(d["steps"])
        xs = [1.76 + i * 1.96 for i in range(n)]
        line(g.shapes, xs[0], 3.30, xs[-1], 3.30, NEUTRAL, 3.0)
        for i, (s, x) in enumerate(zip(d["steps"], xs)):
            oval(g.shapes, x, 3.30, 0.26, fill=BLUE)
            text(g.shapes, x - 0.26, 3.04, 0.52, 0.52, str(i + 1), size=14, bold=True, color=WHITE,
                 align="c", anchor="m")
            text(g.shapes, x - 0.9, 3.75, 1.8, 0.70, s, size=13, bold=True, align="c")
        for i, ln in enumerate(d["lines"]):
            text(g.shapes, 0.79, 5.00 + i * 0.42, 11.75, 0.30, ln, size=12, color=INK60)
        target = g
    an.add([[fx(target)]], auto=True)
    return an
