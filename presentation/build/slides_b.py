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
         [[("Shopper pays 28,000 IQD", dict(size=16, bold=True)),
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
    BASE, SC = 6.55, 1.70 / 1450.0
    wf_head = group(sh)
    text(wf_head.shapes, 6.90, 4.28, 3.2, 0.26, "Per order, after costs", size=13, bold=True,
         anchor="m")
    steps = [("Our share", 1450, None, INK), ("Messages", 90, "−90", RED),
             ("Logins", 25, "−25", RED), ("Returns", 20, "−20", RED),
             ("Re-delivery", 200, "−200", RED)]
    cols_wf = []
    run = 1450
    prev_level = None
    for k, (cat, val, lab, col) in enumerate(steps):
        x = 7.05 + k * 0.92
        g = group(sh)
        if k == 0:
            top, bot = BASE - 1450 * SC, BASE
            lbl = "1,450"
        else:
            top = BASE - run * SC
            bot = BASE - (run - val) * SC
            if bot - top < 0.06:
                bot = top + 0.06
            lbl = lab
            run -= val
        if prev_level is not None:
            line(g.shapes, x - 0.30, prev_level, x, prev_level, INK35, 1.0)
        rect(g.shapes, x, top, 0.62, bot - top, fill=col)
        text(g.shapes, x - 0.15, top - 0.28, 0.92, 0.24, lbl, size=11, bold=True, align="c",
             anchor="m")
        text(g.shapes, x - 0.15, 6.60, 0.92, 0.20, cat, size=10, color=INK60, align="c")
        prev_level = bot if k else top
        cols_wf.append(g)
    px_ = 7.05 + 5 * 0.92
    prof = group(sh)
    line(prof.shapes, px_ - 0.30, prev_level, px_, prev_level, INK35, 1.0)
    rect(prof.shapes, px_, BASE - 1115 * SC, 0.62, 1115 * SC, fill=BLUE)
    text(prof.shapes, px_ - 0.45, BASE - 1115 * SC - 0.42, 1.52, 0.38, "1,115 IQD", size=20,
         bold=True, font="Comfortaa", color=BLUE, align="c", anchor="m")
    text(prof.shapes, px_ - 0.15, 6.60, 0.92, 0.20, "Profit", size=10, color=INK60, align="c")
    if mode == "anim":
        an.add([[fx(top), fx(base)]], auto=True)
        an.add([[fx(segM), fx(lM)]])
        an.add([[fx(segC), fx(lC)]])
        an.add([[fx(segH), fx(lH), fx(callout)]])
        an.add([[fx(fee_title)]] + stagger(cols, "zoom"))
        wf = [[fx(wf_head)] + [fx(c, "fade", i * 80, 250) for i, c in enumerate(cols_wf)]]
        an.add(wf + [[fx(prof, "zoom", 80)]])
    return an


# ------------------------------------------------------------------ 9 competitors
def competitors(sl, ctx):
    sh = sl.shapes
    an = Anim()
    cx = [5.30, 6.90, 8.50, 10.10, 11.70]
    rows_y = [3.70, 4.42, 5.14, 5.86]
    RH = 0.72
    base = group(sh)
    for (lbl, _), y in zip(D.COMP_ROWS, rows_y):
        text(base.shapes, 0.79, y, 3.5, RH, lbl, size=15, bold=True, anchor="m")
    for i in range(4):
        text(base.shapes, cx[i] - 0.8, 2.82, 1.6, 0.55, D.COMP_COLS[i], size=13, bold=True,
             align="c", anchor="m")
    for y in rows_y[:-1]:
        line(base.shapes, 0.79, y + RH, 10.70, y + RH, NEUTRAL, 0.75)
    line(base.shapes, 0.79, rows_y[0] - 0.03, 10.70, rows_y[0] - 0.03, NEUTRAL, 0.75)
    line(base.shapes, 0.79, rows_y[-1] + RH, 10.70, rows_y[-1] + RH, NEUTRAL, 0.75)

    mk = {"yes": ("circle-check", INK60), "partly": ("contrast", INK60), "no": ("circle-x", RED)}
    comp_cols = []
    for ci in range(4):
        g = group(sh)
        for ri, (_, vals) in enumerate(D.COMP_ROWS):
            name, col = mk[vals[ci]]
            icon_c(g.shapes, name, col, cx[ci], rows_y[ri] + RH / 2, 0.36)
        comp_cols.append(g)
    ch = group(sh)
    rect(ch.shapes, 10.90, 2.67, 1.60, 3.99, fill=BLUE12, line=BLUE, lw=1.5, radius=0.14)
    pic_contain(ch.shapes, A("cheapify-logo.png"), cx[4] - 0.21, 2.84, 0.42, 0.54)
    text(ch.shapes, 10.95, 3.40, 1.5, 0.26, "Cheapify", size=13, bold=True, font="Comfortaa",
         color=BLUE, align="c", anchor="m")
    marks = []
    for ri, (_, vals) in enumerate(D.COMP_ROWS):
        name, col = mk[vals[4]]
        col = GREEN if vals[4] == "yes" else col
        g = group(sh)
        icon_c(g.shapes, name, col, cx[4], rows_y[ri] + RH / 2, 0.36)
        marks.append(g)
    leg = group(sh)
    x = 0.79
    for name, col, lbl in (("circle-check", INK60, "yes"), ("contrast", INK60, "partly"),
                           ("circle-x", RED, "no")):
        icon(leg.shapes, name, col, x, 6.74, 0.22)
        text(leg.shapes, x + 0.30, 6.72, 0.8, 0.26, lbl, size=11, color=INK60, anchor="m")
        x += 1.25
    an.add([[fx(base), fx(leg)]], auto=True)
    an.add(stagger(comp_cols, "fade"))
    an.add([[fx(ch, "zoom")]] + stagger(marks, "zoom"))
    return an


# ------------------------------------------------------------------ 11 growth
def growth(sl, ctx):
    sh = sl.shapes
    an = Anim()
    left = [("handshake", "I sign the first 20 stores in person",
             "Bazaar visits, Instagram outreach, a 45-second demo video"),
            ("gift", "A founding offer they can't ignore",
             "0% commission in month 1 + their products in our paid ads"),
            ("link", "Their followers come too",
             "Store link in bio and in replies to “price?” comments")]
    right = [("megaphone", "Targeted ads across Duhok",
              "Facebook, Instagram, TikTok — real products, real prices"),
             ("clapperboard", "Short videos", "“The old way vs the Cheapify way”"),
             ("graduation-cap", "Campus & workplace deals", "UoD, AUK, Nawroz and office hubs"),
             ("users", "Waitlist & referrals",
              "~52 contacts ready · credits only after a delivered order")]

    def column(x0, title, rows, w):
        h = grp_text(sh, x0, 2.72, 4.0, 0.34, title, size=16, bold=True, color=BLUE, anchor="m")
        gs = []
        for i, (ic, a, b) in enumerate(rows):
            y = 3.16 + i * 0.82
            g = group(sh)
            oval(g.shapes, x0 + 0.25, y + 0.30, 0.25, fill=BLUE12)
            icon_c(g.shapes, ic, BLUE, x0 + 0.25, y + 0.30, 0.28)
            text(g.shapes, x0 + 0.70, y + 0.02, w - 0.7, 0.30, a, size=15, bold=True, anchor="m")
            text(g.shapes, x0 + 0.70, y + 0.34, w - 0.7, 0.26, b, size=12, color=INK60, anchor="m")
            gs.append(g)
        return h, gs

    hl, rl = column(0.79, "Stores", left, 5.61)
    hr, rr = column(6.93, "Shoppers", right, 5.61)

    # loop strip
    labels = ["More stores", "Lower prices", "More shoppers", "More orders"]
    wid = [1.20, 1.25, 1.45, 1.25]
    gap = 0.62
    total = sum(wid) + gap * 3
    x = (SLIDE_W - total) / 2
    pieces = []
    xs = []
    for k, (lb, w) in enumerate(zip(labels, wid)):
        g = group(sh)
        text(g.shapes, x, 6.34, w, 0.28, lb, size=13, bold=True, align="c", anchor="m")
        pieces.append(g)
        xs.append((x, w))
        x += w
        if k < 3:
            a = group(sh)
            ar = rect(a.shapes, x + 0.14, 6.40, 0.34, 0.16, fill=BLUE, shape=MSO_SHAPE.RIGHT_ARROW)
            pieces.append(a)
            x += gap
    ret = group(sh)
    x1 = xs[0][0] + xs[0][1] / 2
    x2 = xs[3][0] + xs[3][1] / 2
    line(ret.shapes, x2, 6.66, x2, 6.84, BLUE, 1.5)
    line(ret.shapes, x2, 6.84, x1, 6.84, BLUE, 1.5)
    line(ret.shapes, x1, 6.84, x1, 6.72, BLUE, 1.5)
    tri = rect(ret.shapes, x1 - 0.07, 6.65, 0.14, 0.10, fill=BLUE,
               shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
    pieces.append(ret)
    an.add([[fx(hl), fx(hr)]], auto=True)
    an.add(stagger(rl, "fade"))
    an.add(stagger(rr, "fade"))
    an.add(stagger(pieces, "fade", 60, 150))
    return an


# ------------------------------------------------------------------ 12 finance
def finance(sl, ctx):
    sh = sl.shapes
    an = Anim()
    tiles = []
    for i, (big, tail, sub) in enumerate([("~585", " orders / month", "break-even · about 20 a day"),
                                           ("1,115 IQD", "", "profit per delivered order")]):
        y = 2.70 + i * 1.02
        g = group(sh)
        card(g.shapes, 0.79, y, 3.86, 0.92)
        runs = [(big, dict(size=24, bold=True, font="Comfortaa"))]
        if tail:
            runs.append((tail, dict(size=14, bold=True, font="Comfortaa")))
        text(g.shapes, 1.00, y + 0.08, 3.5, 0.44, [runs], anchor="m")
        text(g.shapes, 1.00, y + 0.54, 3.5, 0.30, sub, size=12, color=INK60)
        tiles.append(g)

    # milestone table as three adjacent native tables (label | Fast | Planned)
    ty = 4.82
    t_label = table(sl, 0.79, ty, 1.36, ["", "", "", ""][:1], [["Lowest cash point"], ["Monthly break-even"],
                    ["All losses recovered"]], [1], row_h=0.50, size=11.5)
    t_fast = table(sl, 2.15, ty, 1.25, ["Fast"], [["−$1,800 (month 2)"], ["Month 3"], ["Month 6"]],
                   [1], row_h=0.50, size=11.5, align=["r"])
    t_plan = table(sl, 3.40, ty, 1.25, ["Planned"], [["−$2,180 (month 3)"], ["Month 4"], ["Month 8"]],
                   [1], row_h=0.50, size=11.5, align=["r"])
    for t in (t_label, t_fast, t_plan):
        t.table.rows[0].height = E(0.34)

    PX0, PX1 = 5.60, 12.30
    X = lambda i: PX0 + i * (PX1 - PX0) / 12
    Y = lambda v: 3.05 + (3500 - v) * (6.55 - 3.05) / 6500
    axes = group(sh)
    for v, lab in ((3000, "+$3k"), (2000, "+$2k"), (1000, "+$1k"), (0, "$0"), (-1000, "−$1k"),
                   (-2000, "−$2k"), (-3000, "−$3k")):
        if v != 0:
            line(axes.shapes, PX0, Y(v), PX1, Y(v), NEUTRAL, 0.5)
        text(axes.shapes, 4.90, Y(v) - 0.11, 0.6, 0.22, lab, size=10, color=INK60, align="r",
             anchor="m")
    line(axes.shapes, PX0, Y(0), PX1, Y(0), INK, 1.0)
    for idx, lab in ((0, "Start"), (2, "Launch"), (4, "M2"), (6, "M4"), (8, "M6"), (10, "M8"),
                     (12, "M10")):
        text(axes.shapes, X(idx) - 0.4, 6.62, 0.8, 0.22, lab, size=10, color=INK60, align="c",
             anchor="m")
    legend = group(sh)
    lx = 9.55
    for lbl, col, lw, dash in (("Fast", BLUE, 3.0, None), ("Planned", INK, 2.5, None),
                               ("Slow", INK35, 1.5, MSO_LINE.DASH)):
        line(legend.shapes, lx, 2.76, lx + 0.32, 2.76, col, lw, dash)
        text(legend.shapes, lx + 0.40, 2.64, 0.8, 0.24, lbl, size=11, anchor="m")
        lx += 1.0 if lbl != "Planned" else 1.25

    def segs(series, color, lw):
        out = []
        for i in range(len(series) - 1):
            g = group(sh)
            c = line(g.shapes, X(i), Y(series[i]), X(i + 1), Y(series[i + 1]), color, lw)
            c.line._get_or_add_ln().set("cap", "rnd")
            out.append(g)
        return out

    def dot(idx, series, color):
        g = group(sh)
        oval(g.shapes, X(idx), Y(series[idx]), 0.075, fill=color, line=WHITE, lw=1.0)
        return g

    pl = D.CHART_PLANNING
    fa = D.CHART_FAST
    plan_segs = segs(pl, INK, 2.5)
    plan_dots = [dot(i, pl, INK) for i in (5, 6, 10)]
    fast_segs = segs(fa, BLUE, 3.0)
    fast_dots = [dot(i, fa, BLUE) for i in (4, 5, 8)]
    arrow = group(sh)
    tri = rect(arrow.shapes, X(9) - 0.09, Y(fa[9]) - 0.30, 0.18, 0.22, fill=BLUE,
               shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
    text(arrow.shapes, X(9) + 0.14, Y(fa[9]) - 0.30, 1.2, 0.22, "keeps rising", size=10.5,
         color=BLUE, bold=True, anchor="m")
    sp = D.CHART_SLOW
    slow = group(sh)
    fb = slow.shapes.build_freeform(E(X(0)), E(Y(sp[0])), scale=1.0)
    fb.add_line_segments([(E(X(i)), E(Y(sp[i]))) for i in range(1, 13)], close=False)
    ff = fb.convert_to_shape()
    ff.fill.background()
    ff.line.color.rgb = rgb(INK35)
    ff.line.width = Pt(1.5)
    ff.line.dash_style = MSO_LINE.DASH
    no_effect(ff)
    slow_lbl = grp_text(sh, X(12) - 2.05, 5.48, 2.05, 0.46,
                        ["Slow case: profitable", "every month from month 7"], size=10.5,
                        color=INK60, align="r", anchor="b")

    an.add(stagger(tiles + [t_label], "fade"), auto=True)
    an.add([[fx(axes), fx(legend), fx(t_plan)]] + stagger(plan_segs, "appear", 25) +
           stagger(plan_dots, "zoom", 25, 150))
    an.add(stagger(fast_segs, "appear", 25) + stagger(fast_dots, "zoom", 25, 150) +
           [[fx(arrow, "fade"), fx(t_fast)]])
    an.add([[fx(slow), fx(slow_lbl)]])
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
        steps.append([g, lg])
    tt = grp_text(sh, 8.60, 2.80, 3.94, 0.30, "Each amount has a job", size=15, bold=True,
                  anchor="m")
    steps_def = [("$7,500 — Grow fast", "+ growth marketing and founding-store kits → aims for the fast case", 0.22),
                 ("$4,500 — Launch properly", "+ hand-run pilot, company registration (unlocks the courier contract and card payments), larger reserve", 0.14),
                 ("$2,500 — Reach break-even safely", "Covers the cash gap until monthly break-even", 0.06)]
    cards = []
    for i, (a, b, w) in enumerate(steps_def):
        y = 3.20 + i * 1.03
        g = group(sh)
        card(g.shapes, 8.60, y, 3.94, 0.95)
        rect(g.shapes, 8.60, y + 0.14, w, 0.67, fill=BLUE)
        text(g.shapes, 8.88, y + 0.07, 3.60, 0.28, a, size=15, bold=True, color=BLUE, anchor="m")
        text(g.shapes, 8.88, y + 0.37, 3.60, 0.54, b, size=11, color=INK60, anchor="t")
        cards.append(g)
    callout = group(sh)
    rect(callout.shapes, 8.60, 6.36, 3.94, 0.62, fill=BLUE12, radius=0.12)
    icon(callout.shapes, "code", BLUE, 8.76, 6.53, 0.28)
    text(callout.shapes, 9.14, 6.38, 3.32, 0.58,
         "No salaries. No developers. I build the platform myself.", size=13, bold=True, anchor="m")
    an.add([[fx(center, "zoom")]], auto=True)
    an.add(pair_stagger(steps))
    an.add([[fx(tt), fx(cards[2])]])
    an.add([[fx(cards[1])]])
    an.add([[fx(cards[0])]])
    an.add([[fx(callout)]])
    return an


# ------------------------------------------------------------------ 13 next
def next_steps(sl, ctx):
    sh = sl.shapes
    an = Anim()
    ln = group(sh)
    c = line(ln.shapes, 1.20, 4.40, 12.10, 4.40, NEUTRAL, 3.0)
    xs = [1.95, 4.35, 6.75, 9.15, 11.40]
    items = []
    for i, ((when, title, sub), x) in enumerate(zip(D.TIMELINE, xs)):
        n = group(sh)
        oval(n.shapes, x, 4.40, 0.21, fill=BLUE)
        text(n.shapes, x - 0.21, 4.19, 0.42, 0.42, str(i + 1), size=13, bold=True, color=WHITE,
             align="c", anchor="m")
        w = group(sh)
        text(w.shapes, x - 1.10, 3.70, 2.20, 0.30, when, size=13, bold=True, color=BLUE,
             align="c", anchor="m")
        cd = group(sh)
        card(cd.shapes, x - 1.10, 4.75, 2.20, 1.55)
        text(cd.shapes, x - 1.00, 4.88, 2.04, 0.70, title.replace(": ", ":\n").split("\n"),
             size=14, bold=True)
        text(cd.shapes, x - 1.00, 5.62, 2.04, 0.60, sub, size=11.5, color=INK60)
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
    an.groups[-1][1].append([fx(kpi, delay=80)])
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
    an.add([[fx(logo, "zoom")], [fx(t) for t in (t1, t2, t3, t4, t5, t6)]], auto=True)
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
    elif key == "A8":
        target = table(sl, 0.79, 2.75, 11.75, d["header"], d["rows"], [2.3, 1.6, 3.6, 1.9], row_h=0.46)
        text(sh, 0.79, 6.10, 11.75, 0.50, d["note"], size=12, color=INK60)
    elif key == "A7":
        g = group(sh)
        n = len(d["steps"])
        xs = [1.60 + i * 1.69 for i in range(n)]
        line(g.shapes, xs[0], 3.30, xs[-1], 3.30, NEUTRAL, 3.0)
        for i, (s, x) in enumerate(zip(d["steps"], xs)):
            oval(g.shapes, x, 3.30, 0.26, fill=BLUE)
            text(g.shapes, x - 0.26, 3.04, 0.52, 0.52, str(i + 1), size=14, bold=True, color=WHITE,
                 align="c", anchor="m")
            text(g.shapes, x - 0.78, 3.75, 1.56, 0.80, s, size=13, bold=True, align="c")
        for i, ln in enumerate(d["lines"]):
            text(g.shapes, 0.79, 4.95 + i * 0.40, 11.75, 0.30, ln, size=12, color=INK60)
        target = g
    an.add([[fx(target)]], auto=True)
    return an
