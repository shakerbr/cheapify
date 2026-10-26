"""Slides 8-14 and appendix A1-A9 (v4 spec)."""
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

    # Left half: Our fee (5% / 3% / 1.5%)
    left_bg = group(sh)
    card(left_bg.shapes, 0.79, 2.58, 5.60, 4.30)
    text(left_bg.shapes, 1.10, 2.76, 5.00, 0.34, "Our fee", size=18, bold=True, color=INK,
         anchor="m")
    text(left_bg.shapes, 1.10, 3.10, 5.00, 0.26, "Lighter as prices rise", size=13, color=INK60,
         anchor="m")

    cols = []
    tiers = [
        (1.85, "5%", "first 10,000 IQD"),
        (1.18, "3%", "10,001 – 100,000"),
        (0.62, "1.5%", "above 100,000"),
    ]
    T_BASE = 5.76
    for i, (h, v, cap) in enumerate(tiers):
        x = 1.22 + i * 1.72
        g = group(sh)
        rect(g.shapes, x, T_BASE - h, 1.32, h, fill=BLUE, radius=0.06)
        text(g.shapes, x - 0.14, T_BASE - h - 0.42, 1.60, 0.38, v, size=24, bold=True,
             font="Comfortaa", color=BLUE, align="c", anchor="m")
        text(g.shapes, x - 0.18, T_BASE + 0.08, 1.68, 0.28, cap, size=11, bold=True,
             color=INK60, align="c", anchor="m")
        cols.append(g)

    cap_left = group(sh)
    rect(cap_left.shapes, 1.02, 6.20, 5.14, 0.48, fill=BLUE12, radius=0.10)
    text(cap_left.shapes, 1.02, 6.20, 5.14, 0.48,
         "Typical 25,000 IQD order → 950 IQD fee + 500 delivery margin.",
         size=11, bold=True, color=INK, align="c", anchor="m", wrap=False)

    # Right half: Per-order waterfall
    right_bg = group(sh)
    card(right_bg.shapes, 6.69, 2.58, 5.85, 4.30)
    text(right_bg.shapes, 7.00, 2.76, 5.20, 0.34, "Per order", size=18, bold=True, color=INK,
         anchor="m")
    text(right_bg.shapes, 7.00, 3.10, 5.20, 0.26, "From our 1,450 IQD share to net profit",
         size=13, color=INK60, anchor="m")

    BASE, SC = 6.18, 2.15 / 1450.0
    steps = [
        ("Our share", 1450, "1,450", INK),
        ("Messages", 90, "−90", RED),
        ("Logins", 25, "−25", RED),
        ("Returns", 20, "−20", RED),
        ("Re-delivery", 200, "−200", RED),
    ]
    cols_wf = []
    run = 1450
    prev_level = None
    for k, (cat, val, lbl, col) in enumerate(steps):
        x = 6.96 + k * 0.88
        g = group(sh)
        if k == 0:
            wtop, wbot = BASE - 1450 * SC, BASE
        else:
            wtop = BASE - run * SC
            wbot = BASE - (run - val) * SC
            if wbot - wtop < 0.07:
                wbot = wtop + 0.07
            run -= val
        if prev_level is not None:
            line(g.shapes, x - 0.26, prev_level, x, prev_level, INK35, 1.0)
        rect(g.shapes, x, wtop, 0.62, wbot - wtop, fill=col)
        text(g.shapes, x - 0.14, wtop - 0.30, 0.90, 0.26, lbl, size=11.5, bold=True,
             color=col if k else INK, align="c", anchor="m")
        text(g.shapes, x - 0.14, BASE + 0.08, 0.90, 0.26, cat, size=10.5, color=INK60,
             align="c", anchor="m")
        prev_level = wbot if k else wtop
        cols_wf.append(g)

    px_ = 6.96 + 5 * 0.88
    prof = group(sh)
    line(prof.shapes, px_ - 0.26, prev_level, px_, prev_level, INK35, 1.0)
    rect(prof.shapes, px_, BASE - 1115 * SC, 0.72, 1115 * SC, fill=BLUE)
    text(prof.shapes, px_ - 0.29, BASE - 1115 * SC - 0.44, 1.30, 0.38, "1,115 IQD", size=17,
         bold=True, font="Comfortaa", color=BLUE, align="c", anchor="m")
    text(prof.shapes, px_ - 0.14, BASE + 0.08, 1.00, 0.26, "Kept", size=11, bold=True,
         color=BLUE, align="c", anchor="m")

    if mode == "anim":
        an.add([[fx(left_bg)]] + stagger(cols, "zoom") + [[fx(cap_left, "fade", 60)]], auto=True)
        wf = [[fx(right_bg)] + [fx(c, "fade", i * 80, 240) for i, c in enumerate(cols_wf)]]
        an.add(wf)
        an.add([[fx(prof, "zoom")]])
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


# ------------------------------------------------------------------ 10 growth
def growth(sl, ctx):
    sh = sl.shapes
    an = Anim()
    C = (6.67, 4.38)
    R = 1.20
    ringg = group(sh)
    oval(ringg.shapes, C[0], C[1], R, line=BLUE, lw=2.5)
    pic_contain(ringg.shapes, A("cheapify-logo.png"), C[0] - 0.28, C[1] - 0.36, 0.56, 0.72)

    node_def = [
        ((C[0], C[1] - R), "Lower prices"),
        ((C[0] + R, C[1]), "More shoppers"),
        ((C[0], C[1] + R), "More orders"),
        ((C[0] - R, C[1]), "More stores"),
    ]
    nodes = []
    for (nx, ny), lbl in node_def:
        g = group(sh)
        card(g.shapes, nx - 0.82, ny - 0.23, 1.64, 0.46)
        text(g.shapes, nx - 0.82, ny - 0.23, 1.64, 0.46, lbl, size=12, bold=True, align="c",
             anchor="m")
        nodes.append(g)

    chevs = []
    for ang in (45, -45, -135, 135):
        th = math.radians(ang)
        px, py = C[0] + R * math.cos(th), C[1] - R * math.sin(th)
        rot = math.degrees(math.atan2(math.cos(th), math.sin(th)))
        g = group(sh)
        ch = rect(g.shapes, px - 0.10, py - 0.13, 0.20, 0.26, fill=BLUE, shape=MSO_SHAPE.CHEVRON)
        ch.rotation = rot
        chevs.append(g)

    def column(x0, title, rows):
        h = grp_text(sh, x0, 2.58, 3.30, 0.34, title, size=16, bold=True, color=BLUE, anchor="m")
        gs = []
        for i, (ic, lbl) in enumerate(rows):
            y = 3.04 + i * 0.70
            g = group(sh)
            oval(g.shapes, x0 + 0.24, y + 0.24, 0.24, fill=BLUE12)
            icon_c(g.shapes, ic, BLUE, x0 + 0.24, y + 0.24, 0.26)
            text(g.shapes, x0 + 0.60, y, 2.75, 0.48, lbl, size=12.5, bold=True, anchor="m")
            gs.append(g)
        return h, gs

    hl, rl = column(0.79, "Stores", [
        ("handshake", "Signed in person · 20 stores"),
        ("gift", "0% in month 1"),
        ("rocket", "Free ads"),
        ("link", "Their followers · 1.5k–50k each"),
    ])
    hr, rr = column(9.25, "Shoppers", [
        ("megaphone", "Targeted ads · $2,200"),
        ("clapperboard", "Short videos"),
        ("graduation-cap", "Campus deals · 3 universities"),
        ("users", "Referrals · 52 on the waitlist"),
    ])
    al = group(sh)
    rect(al.shapes, 4.18, 4.27, 0.38, 0.20, fill=BLUE, shape=MSO_SHAPE.RIGHT_ARROW)
    ar = group(sh)
    rect(ar.shapes, 8.77, 4.27, 0.38, 0.20, fill=BLUE, shape=MSO_SHAPE.LEFT_ARROW)

    # Bottom expansion roadmap strip (moved from slide 6)
    strip = group(sh)
    rect(strip.shapes, 0.79, 6.22, 11.75, 0.58, fill=SURFACE, line=NEUTRAL, lw=1.0, radius=0.12)
    pts = [
        (1.15, "Duhok · Semel · Zakho", 3.10),
        (5.25, "Erbil · Mosul · Sulaymaniyah", 3.40),
        (9.75, "All of Iraq", 2.30),
    ]
    for px, lbl, tw in pts:
        oval(strip.shapes, px, 6.51, 0.09, fill=BLUE)
        text(strip.shapes, px + 0.20, 6.22, tw, 0.58, lbl, size=12.5, bold=True, color=INK,
             anchor="m")
    rect(strip.shapes, 4.45, 6.42, 0.36, 0.18, fill=BLUE, shape=MSO_SHAPE.RIGHT_ARROW)
    rect(strip.shapes, 8.95, 6.42, 0.36, 0.18, fill=BLUE, shape=MSO_SHAPE.RIGHT_ARROW)

    an.add([[fx(ringg)]], auto=True)
    an.add([[fx(hl)]] + stagger(rl, "fade") + [[fx(al)]])
    an.add([[fx(hr), fx(ar)]] + stagger(rr, "fade"))
    an.add(stagger([nodes[3], nodes[0], nodes[1], nodes[2]], "zoom") +
           [[fx(c, "fade", 80 * i, 240) for i, c in enumerate(chevs)]])
    an.add([[fx(strip, "fade")]])
    return an


# ------------------------------------------------------------------ 11 finance
def finance(sl, ctx):
    sh = sl.shapes
    an = Anim()

    # Three small tiles above the chart
    tiles_def = [
        (0.79, "Costs $435 / month", "from month 6: $527"),
        (4.79, "Break-even 585 orders / mo", "≈ 390 regular shoppers"),
        (8.79, "Payback month 8", "fast case: month 6"),
    ]
    tiles = []
    for tx, t_main, t_sub in tiles_def:
        g = group(sh)
        card(g.shapes, tx, 2.54, 3.75, 0.66, fill=BLUE12, line=BLUE, lw=1.0, radius=0.12)
        text(g.shapes, tx + 0.14, 2.56, 3.47, 0.34, t_main, size=14, bold=True, color=INK,
             align="c", anchor="m")
        text(g.shapes, tx + 0.14, 2.90, 3.47, 0.26, t_sub, size=10.5, color=INK60,
             align="c", anchor="m")
        tiles.append(g)

    PX0, PX1 = 1.50, 12.30
    X = lambda i: PX0 + i * (PX1 - PX0) / 12
    Y = lambda v: 3.45 + (3500 - v) * (6.72 - 3.45) / 6500

    axes = group(sh)
    for v, lab in ((3000, "+$3k"), (2000, "+$2k"), (1000, "+$1k"), (0, "$0"), (-1000, "−$1k"),
                   (-2000, "−$2k"), (-3000, "−$3k")):
        if v != 0:
            line(axes.shapes, PX0, Y(v), PX1, Y(v), NEUTRAL, 0.5)
        text(axes.shapes, 0.85, Y(v) - 0.11, 0.55, 0.22, lab, size=10, color=INK60, align="r",
             anchor="m")
    line(axes.shapes, PX0, Y(0), PX1, Y(0), INK, 1.0)
    x_labels = ("Start", "M-1", "Launch", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9",
                "M10")
    for idx, lab in enumerate(x_labels):
        text(axes.shapes, X(idx) - 0.36, 6.75, 0.72, 0.22, lab, size=9.5, color=INK60, align="c",
             anchor="m")

    legend = group(sh)
    text(legend.shapes, PX0, 3.38, 3.10, 0.24, "Cumulative net cash position (USD)",
         size=10.5, bold=True, color=INK60, anchor="m")
    lx = 4.55
    for lbl, col, lw, dash, w_lbl in (
        ("Planned (base)", BLUE, 3.0, None, 1.18),
        ("Fast (2× pace)", INK, 2.2, None, 1.15),
        ("Slow (half pace)", INK35, 1.5, MSO_LINE.DASH, 1.25),
    ):
        line(legend.shapes, lx, 3.50, lx + 0.28, 3.50, col, lw, dash)
        text(legend.shapes, lx + 0.34, 3.38, w_lbl, 0.24, lbl, size=10, bold=(col == BLUE),
             color=INK if col != INK35 else INK60, anchor="m", wrap=False)
        lx += w_lbl + 0.44

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

    def label(idx, series, txt, color, box, anchor_pt):
        g = group(sh)
        bx, by, bw = box
        line(g.shapes, X(idx), Y(series[idx]), anchor_pt[0], anchor_pt[1], color, 1.0)
        rect(g.shapes, bx, by, bw, 0.26, fill=color, radius=0.13)
        text(g.shapes, bx, by, bw, 0.26, txt, size=10.5, bold=True, color=WHITE, align="c",
             anchor="m")
        return g

    pl, fa, sp = D.CHART_PLANNING, D.CHART_FAST, D.CHART_SLOW
    plan_segs = segs(pl, BLUE, 3.0)
    plan_dots = [dot(i, pl, BLUE) for i in (5, 6, 10)]
    plan_pills = [
        label(5, pl, "Lowest −$2,180 · month 3", BLUE, (3.40, 6.40, 2.05), (5.45, 6.48)),
        label(6, pl, "Monthly break-even · month 4", BLUE, (7.55, 6.22, 2.25), (7.55, 6.32)),
        label(10, pl, "All losses recovered · month 8", BLUE, (8.95, 4.24, 2.32), (10.11, 4.50)),
    ]
    fast_segs = segs(fa, INK, 2.2)
    fast_dots = [dot(i, fa, INK) for i in (5, 8)]
    fast_pills = [
        label(5, fa, "Fast break-even · month 3", INK, (4.10, 5.38, 2.02), (5.35, 5.64)),
        label(8, fa, "Fast payback · month 6", INK, (6.20, 3.86, 1.85), (8.05, 3.99)),
    ]
    arrow = group(sh)
    rect(arrow.shapes, X(9) - 0.09, Y(fa[9]) - 0.28, 0.18, 0.20, fill=INK,
         shape=MSO_SHAPE.ISOSCELES_TRIANGLE)
    text(arrow.shapes, X(9) + 0.14, Y(fa[9]) - 0.28, 1.2, 0.22, "keeps rising", size=10,
         color=INK, bold=True, anchor="m")

    slow = group(sh)
    fb = slow.shapes.build_freeform(E(X(0)), E(Y(sp[0])), scale=1.0)
    fb.add_line_segments([(E(X(i)), E(Y(sp[i]))) for i in range(1, 13)], close=False)
    ff = fb.convert_to_shape()
    ff.fill.background()
    ff.line.color.rgb = rgb(INK35)
    ff.line.width = Pt(1.5)
    ff.line.dash_style = MSO_LINE.DASH
    no_effect(ff)
    slow_lbl = group(sh)
    oval(slow_lbl.shapes, X(9), Y(sp[9]), 0.070, fill=INK60, line=WHITE, lw=1.0)
    line(slow_lbl.shapes, X(9), Y(sp[9]), 10.45, 5.98, INK35, 1.0)
    rect(slow_lbl.shapes, 9.45, 5.66, 2.75, 0.32, fill=SURFACE, line=NEUTRAL, lw=1.0, radius=0.14)
    text(slow_lbl.shapes, 9.45, 5.66, 2.75, 0.32, "Slow case: profitable from month 7",
         size=10, bold=True, color=INK60, align="c", anchor="m", wrap=False)

    an.add(stagger(tiles, "fade"), auto=True)
    an.add([[fx(axes), fx(legend)]] + stagger(plan_segs, "appear", 40) +
           stagger(plan_dots, "zoom", 40, 220) + stagger(plan_pills, "fade"))
    an.add(stagger(fast_segs, "appear", 40) + stagger(fast_dots, "zoom", 40, 220) +
           [[fx(arrow)]] + stagger(fast_pills, "fade"))
    an.add([[fx(slow), fx(slow_lbl)]])
    return an


# ------------------------------------------------------------------ 12 funding
def funding(sl, ctx):
    sh = sl.shapes
    an = Anim()

    # Main visual (left): Horizontal timeline M0 -> M6 with 5 blocks dropping in
    tl_frame = group(sh)
    card(tl_frame.shapes, 0.79, 2.56, 8.15, 3.56)
    text(tl_frame.shapes, 1.05, 2.70, 2.50, 0.36, "$5,480 total ask", size=17, bold=True,
         font="Comfortaa", color=BLUE, anchor="m")
    text(tl_frame.shapes, 3.55, 2.70, 5.10, 0.36, "When each dollar is spent (M0 → M6)",
         size=12, bold=True, color=INK60, align="r", anchor="m")

    GX0, GX1 = 3.85, 8.65
    mx = lambda m: GX0 + (m / 6.0) * (GX1 - GX0)
    for m in range(7):
        x = mx(m)
        line(tl_frame.shapes, x, 3.12, x, 5.95, NEUTRAL, 0.75)
        text(tl_frame.shapes, x - 0.25, 5.88, 0.50, 0.20, f"M{m}", size=9.5, bold=True,
             color=INK60, align="c", anchor="m")

    colors = dict(INK=INK, BLUE=BLUE, INK60=INK60, BLUE50=BLUE50, ORANGE=ORANGE)
    blocks = []
    for i, (title, detail, usd, m0, m1, ck) in enumerate(D.FUNDING_BLOCKS):
        y = 3.18 + i * 0.52
        g = group(sh)
        text(g.shapes, 1.02, y + 0.01, 1.95, 0.22, title, size=12.5, bold=True, color=INK,
             anchor="t", wrap=False)
        text(g.shapes, 1.02, y + 0.24, 1.95, 0.20, detail, size=9.5, color=INK60,
             anchor="t", wrap=False)
        text(g.shapes, 2.95, y + 0.04, 0.78, 0.34, f"${usd:,}", size=13, bold=True,
             font="Comfortaa", color=INK, align="r", anchor="m")
        bx = mx(m0)
        bw = max(0.55, mx(m1) - mx(m0))
        rect(g.shapes, bx, y + 0.06, bw, 0.32, fill=colors[ck], radius=0.08)
        tcol = INK if ck == "BLUE50" else WHITE
        text(g.shapes, bx, y + 0.06, bw, 0.32, f"${usd:,}", size=10.5, bold=True,
             color=tcol, align="c", anchor="m")
        blocks.append(g)

    # Visual 2 (right): Less? Still a plan.
    tiers_card = group(sh)
    card(tiers_card.shapes, 9.15, 2.56, 3.39, 3.56, fill=SURFACE, line=NEUTRAL)
    text(tiers_card.shapes, 9.40, 2.74, 2.89, 0.34, "Less? Still a plan.", size=16, bold=True,
         color=INK, anchor="m")
    for i, (amt, headline, desc) in enumerate(D.FUNDING_TIERS):
        ty = 3.24 + i * 1.36
        rect(tiers_card.shapes, 9.35, ty, 2.99, 1.20, fill=WHITE, line=BLUE, lw=1.25, radius=0.12)
        text(tiers_card.shapes, 9.52, ty + 0.10, 2.65, 0.34, amt, size=18, bold=True,
             font="Comfortaa", color=BLUE, anchor="m")
        text(tiers_card.shapes, 9.52, ty + 0.44, 2.65, 0.26, headline, size=12, bold=True,
             color=INK, anchor="m")
        text(tiers_card.shapes, 9.52, ty + 0.72, 2.65, 0.40, desc, size=10, color=INK60,
             anchor="t")

    # Bottom bar
    callout = group(sh)
    rect(callout.shapes, 0.79, 6.26, 11.75, 0.62, fill=BLUE12, line=BLUE, lw=1.0, radius=0.12)
    icon(callout.shapes, "code", BLUE, 1.05, 6.42, 0.30)
    text(callout.shapes, 1.48, 6.26, 10.80, 0.62,
         "No salaries. No developers. I build the platform myself.",
         size=15, bold=True, color=INK, anchor="m")

    an.add([[fx(tl_frame)]], auto=True)
    for b in blocks:
        an.add([[fx(b, "zoom")]])
    an.add([[fx(tiers_card, "fade")]])
    an.add([[fx(callout, "zoom")]])
    return an


# ------------------------------------------------------------------ 13 next
def next_steps(sl, ctx):
    sh = sl.shapes
    an = Anim()
    ln = group(sh)
    line(ln.shapes, 1.35, 3.35, 11.98, 3.35, NEUTRAL, 3.0)
    xs = [1.89, 4.28, 6.67, 9.06, 11.45]
    items = []
    for i, ((when, ic_name, title, sub), x) in enumerate(zip(D.TIMELINE, xs)):
        n = group(sh)
        oval(n.shapes, x, 3.35, 0.38, fill=BLUE)
        icon_c(n.shapes, ic_name, WHITE, x, 3.35, 0.38)
        w = group(sh)
        rect(w.shapes, x - 0.52, 2.58, 1.04, 0.28, fill=BLUE12, radius=0.14)
        text(w.shapes, x - 0.52, 2.58, 1.04, 0.28, when, size=11.5, bold=True, color=BLUE,
             align="c", anchor="m")
        cd = group(sh)
        card(cd.shapes, x - 1.10, 3.92, 2.20, 2.22)
        text(cd.shapes, x - 0.96, 4.08, 1.92, 0.82, title, size=15, bold=True, color=INK,
             align="c", anchor="m")
        line(cd.shapes, x - 0.65, 4.98, x + 0.65, 4.98, NEUTRAL, 1.0)
        text(cd.shapes, x - 0.96, 5.10, 1.92, 0.88, sub, size=12, color=INK60, align="c",
             anchor="m")
        items.append((n, w, cd))

    kpi = group(sh)
    rect(kpi.shapes, 0.79, 6.32, 11.75, 0.56, fill=SURFACE, line=NEUTRAL, lw=1.0, radius=0.12)
    icon(kpi.shapes, "chart-column", BLUE, 1.05, 6.47, 0.26)
    text(kpi.shapes, 1.42, 6.32, 10.90, 0.56,
         "We report monthly: orders · sales · active stores · repeat orders · delivery time.",
         size=13, bold=True, color=INK, anchor="m")

    an.add([[fx(ln)]], auto=True)
    for n, w, cd in items:
        an.add([[fx(n, "zoom"), fx(w, "fade"), fx(cd, "fade")]])
    an.groups[-1][1].append([fx(kpi, delay=90)])
    return an


# ------------------------------------------------------------------ 14 thanks
def thanks(sl, ctx):
    sh = sl.shapes
    w = 1.15
    logo, _ = pic_contain(sh, A("cheapify-logo.png"), (SLIDE_W - w) / 2, 1.95, w, w * 9 / 7)
    t1 = text(sh, 0, 3.55, SLIDE_W, 0.80, "Thank you", size=48, bold=True, font="Comfortaa",
              align="c", anchor="m")
    t2 = text(sh, 0, 4.42, SLIDE_W, 0.42, "The bright side of choosing.", size=20, color=BLUE,
              font="Comfortaa", align="c", anchor="m")
    t5 = text(sh, 0, 5.12, SLIDE_W, 0.34, "getcheapify.com", size=17, bold=True, color=BLUE,
              align="c", anchor="m")
    t6 = text(sh, 0, 5.50, SLIDE_W, 0.30, "Shakir Bashar · Founder", size=13.5, color=INK60,
              align="c", anchor="m")
    an = Anim()
    an.add([[fx(logo, "zoom")], [fx(t1, "fade", 60), fx(t2, "fade", 90)],
            [fx(t5, "fade", 60), fx(t6, "fade", 60)]], auto=True)
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
    fill = tcPr.find(qn("a:solidFill"))
    if fill is not None:
        tcPr.remove(fill)
        tcPr.append(fill)


def table(sl, x, y, w, header, rows, col_w, row_h=0.38, size=12, align=None, highlight=None,
          wrap=True):
    shp = sl.shapes.add_table(len(rows) + 1, len(header), E(x), E(y), E(w),
                              E(row_h * (len(rows) + 1)))
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
        is_hl = (r > 0 and highlight is not None and (r - 1) == highlight)
        for c in range(len(header)):
            cell = tbl.cell(r, c)
            txt = header[c] if r == 0 else rows[r - 1][c]
            cell.margin_left = cell.margin_right = E(0.12)
            cell.margin_top = cell.margin_bottom = E(0.04)
            cell.vertical_anchor = ANCHOR["m"]
            tf = cell.text_frame
            tf.word_wrap = wrap
            p = tf.paragraphs[0]
            p.alignment = ALIGN[(align[c] if align else "l")]
            run = p.add_run()
            run.text = txt
            f = run.font
            f.size = Pt(size)
            f.bold = (r == 0) or is_hl
            f.color.rgb = rgb(WHITE if r == 0 else (BLUE if (is_hl and c == len(header) - 1) else INK))
            rPr = run._r.get_or_add_rPr()
            rPr.set("lang", "en-US")
            for tag in ("a:latin", "a:cs"):
                etree.SubElement(rPr, qn(tag), typeface="Inter")
            cell.fill.solid()
            if r == 0:
                cell.fill.fore_color.rgb = rgb(INK)
            elif is_hl:
                cell.fill.fore_color.rgb = rgb(BLUE12)
            else:
                cell.fill.fore_color.rgb = rgb(WHITE if r % 2 == 1 else SURFACE)
            _cell_border(cell)
    return shp


def _takeaway_bar(sh, txt):
    g = group(sh)
    rect(g.shapes, 0.79, 6.40, 11.75, 0.50, fill=BLUE12, line=BLUE, lw=1.0, radius=0.10)
    text(g.shapes, 1.00, 6.40, 11.33, 0.50, txt, size=12.5, bold=True, color=BLUE, anchor="m")
    return g


def appendix(sl, key, ctx):
    d = D.APPENDIX[key]
    sh = sl.shapes
    an = Anim()
    target = None

    if key == "A1":
        text(sh, 0.79, 2.55, 11.75, 0.34, d["line"], size=12, color=INK60, anchor="m")
        target = table(sl, 0.79, 2.98, 11.75, d["header"], d["rows"], [1.3, 1, 1, 1],
                       row_h=0.36, size=12, align=["l", "r", "r", "r"], highlight=d["highlight"])
        _takeaway_bar(sh, d["takeaway"])
    elif key == "A2":
        t1 = table(sl, 0.79, 2.55, 5.45, d["header"], d["rows"], [3.6, 1.1],
                   row_h=0.58, size=11.5, align=["l", "r"], highlight=d["highlight"])
        table(sl, 6.49, 2.55, 6.05, d["header2"], d["rows2"], [2.6, 1.0, 1.1, 1.2],
              row_h=0.58, size=11, align=["l", "r", "r", "r"], highlight=d["highlight2"])
        _takeaway_bar(sh, d["takeaway"])
        target = t1
    elif key == "A3":
        t1 = table(sl, 0.79, 2.55, 11.75, d["header"], d["rows"], [1.8, 1.3, 1.4, 1.3, 1.4],
                   row_h=0.40, size=11.5, align=["l", "r", "r", "r", "r"], highlight=d["highlight"])
        table(sl, 0.79, 4.30, 11.75, d["header2"], d["rows2"], [3.4, 1.1, 1.0, 1.6],
              row_h=0.38, size=11, align=["l", "r", "r", "l"], highlight=d["highlight2"])
        _takeaway_bar(sh, d["takeaway"])
        target = t1
    elif key == "A4":
        g = group(sh)
        for x, title, items in ((0.79, d["shoppers_title"], d["shoppers"]),
                                (6.82, d["merchants_title"], d["merchants"])):
            card(g.shapes, x, 2.58, 5.72, 3.66)
            text(g.shapes, x + 0.24, 2.74, 5.24, 0.36, title, size=16, bold=True, color=BLUE,
                 anchor="m")
            for idx, (stat_lbl, desc) in enumerate(items):
                ry = 3.22 + idx * 0.72
                rect(g.shapes, x + 0.24, ry, 1.18, 0.44, fill=BLUE12, radius=0.08)
                text(g.shapes, x + 0.24, ry, 1.18, 0.44, stat_lbl, size=12, bold=True, color=BLUE,
                     align="c", anchor="m")
                text(g.shapes, x + 1.54, ry, 3.94, 0.54, desc, size=11.5, color=INK, anchor="m")
        _takeaway_bar(sh, d["takeaway"])
        target = g
    elif key == "A5":
        target = table(sl, 0.79, 2.58, 11.75, d["header"], d["rows"], [2.5, 1.5, 1.6, 1.0, 2.4],
                       row_h=0.50, size=11.5, align=["l", "r", "r", "r", "l"],
                       highlight=d["highlight"])
        _takeaway_bar(sh, d["takeaway"])
    elif key == "A6":
        target = table(sl, 0.79, 2.58, 11.75, d["header"], d["rows"], [2.6, 6.2],
                       row_h=0.60, size=11.5, highlight=d["highlight"])
        _takeaway_bar(sh, d["takeaway"])
    elif key == "A7":
        g = group(sh)
        steps = d["steps"]
        n = len(steps)
        xs = [1.58 + i * 1.83 for i in range(n)]
        line(g.shapes, xs[0], 3.15, xs[-1], 3.15, NEUTRAL, 3.0)
        for i, ((ic_name, title, desc), x) in enumerate(zip(steps, xs)):
            oval(g.shapes, x, 3.15, 0.32, fill=BLUE)
            icon_c(g.shapes, ic_name, WHITE, x, 3.15, 0.32)
            card(g.shapes, x - 0.84, 3.62, 1.68, 1.25)
            text(g.shapes, x - 0.76, 3.70, 1.52, 0.34, title, size=12, bold=True, color=INK,
                 align="c", anchor="m")
            text(g.shapes, x - 0.76, 4.06, 1.52, 0.72, desc, size=10, color=INK60,
                 align="c", anchor="m")
        for i, (ctitle, cdesc) in enumerate(d["cards"]):
            cx = 0.79 + i * 6.00
            card(g.shapes, cx, 5.04, 5.75, 1.18, fill=SURFACE, line=NEUTRAL)
            text(g.shapes, cx + 0.22, 5.16, 5.31, 0.32, ctitle, size=13, bold=True, color=BLUE,
                 anchor="m")
            text(g.shapes, cx + 0.22, 5.50, 5.31, 0.58, cdesc, size=11, color=INK, anchor="m")
        _takeaway_bar(sh, d["takeaway"])
        target = g
    elif key == "A8":
        target = table(sl, 0.79, 2.58, 11.75, d["header"], d["rows"], [2.3, 1.5, 3.6, 1.8],
                       row_h=0.50, size=11.5, align=["l", "r", "l", "l"], highlight=d["highlight"])
        _takeaway_bar(sh, d["takeaway"])
    elif key == "A9":
        target = table(sl, 0.79, 2.52, 11.75, d["header"], d["rows"],
                       [0.35, 2.15, 0.70, 0.95, 0.75, 4.90],
                       row_h=0.36, size=10.5, align=["c", "l", "r", "r", "c", "l"],
                       highlight=d["highlight"], wrap=False)
        # Monthly release strip (M0..M6)
        rel = group(sh)
        for i, (m_lbl, amt, what) in enumerate(d["schedule"]):
            rx = 0.79 + i * 1.69
            card(rel.shapes, rx, 5.52, 1.62, 0.74, fill=SURFACE, line=NEUTRAL, radius=0.08)
            text(rel.shapes, rx + 0.08, 5.56, 0.50, 0.24, m_lbl, size=10.5, bold=True,
                 color=BLUE, anchor="m")
            text(rel.shapes, rx + 0.58, 5.56, 0.96, 0.24, amt, size=11, bold=True,
                 font="Comfortaa", color=INK, align="r", anchor="m")
            text(rel.shapes, rx + 0.08, 5.82, 1.46, 0.38, what, size=9, color=INK60, anchor="m")
        _takeaway_bar(sh, d["takeaway"])

    an.add([[fx(target)]], auto=True)
    return an
