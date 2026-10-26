"""Slides 1-7 (v4 spec)."""
import json
import math

from pptx.enum.dml import MSO_LINE
from pptx.enum.shapes import MSO_SHAPE

import deck_data as D
from deckkit import *

ASSETS = None  # set by build_deck
SLIDE_W = 13.333


def A(name):
    return ASSETS / name


def meta():
    return json.loads((ASSETS / "ev-meta.json").read_text())


def grp_text(parent, *a, **k):
    g = group(parent)
    text(g.shapes, *a, **k)
    return g


# ------------------------------------------------------------------ 1 cover
def cover(sl, ctx):
    sh = sl.shapes
    t1 = text(sh, 0, 2.82, SLIDE_W, 0.80, "Youth Entrepreneurship Program", size=38, bold=True,
              font="Comfortaa", color=INK, align="c", anchor="m")
    t2 = text(sh, 0, 3.66, SLIDE_W, 0.44, "One product, ten prices.", size=18,
              color=BLUE, font="Comfortaa", align="c", anchor="m")
    rule = rect(sh, (SLIDE_W - 2.40) / 2, 4.38, 2.40, 0.05, fill=BLUE)
    f1 = text(sh, 0, 4.68, SLIDE_W, 0.38, "Shakir Bashar · Founder", size=18, bold=True,
              color=INK, align="c", anchor="m")
    f2 = text(sh, 0, 5.12, SLIDE_W, 0.32, "4 November 2026", size=13.5, color=INK60,
              align="c", anchor="m")
    an = Anim()
    an.add([[fx(t1, "fade"), fx(t2, "fade", 60)],
            [fx(rule, "zoom"), fx(f1, "fade", 60), fx(f2, "fade", 90)]], auto=True)
    return an


# ------------------------------------------------------------------ 2 problem
def problem(sl, ctx):
    sh = sl.shapes
    an = Anim()
    M = meta()["ev-miswag-anker"]

    # Large Miswag screenshot (~60% of slide width)
    gl = group(sh)
    card(gl.shapes, 0.79, 2.58, 7.10, 4.30)
    rect(gl.shapes, 0.95, 2.70, 6.78, 3.68, fill=SURFACE, radius=0.10)
    pic, geom = pic_contain(gl.shapes, A("ev-miswag-anker.jpg"), 1.03, 2.78, 6.62, 3.52)
    text(gl.shapes, 0.95, 6.44, 6.78, 0.34,
         "Same search. Same screen. Same model.",
         size=14, bold=True, color=INK, align="c", anchor="m")

    # Right-side context & progressive callouts
    ctx_box = group(sh)
    text(ctx_box.shapes, 8.20, 2.62, 4.34, 0.34, "Anker 25,000 mAh · 165 W",
         size=16, bold=True, color=INK, anchor="m")
    text(ctx_box.shapes, 8.20, 2.96, 4.34, 0.28, "Miswag search grid",
         size=12.5, color=INK60, anchor="m")

    rings = []
    for box in M["rings"]:
        g = group(sh)
        ring(g.shapes, geom, box, pad=8, color=RED, lw=2.5)
        rings.append(g)

    p1 = group(sh)
    card(p1.shapes, 8.20, 3.42, 4.34, 0.68, fill=SURFACE, line=NEUTRAL)
    text(p1.shapes, 8.40, 3.42, 1.80, 0.68, "Seller 1", size=13, color=INK60, anchor="m")
    text(p1.shapes, 10.10, 3.42, 2.24, 0.68, "100,000 IQD", size=20, bold=True,
         font="Comfortaa", color=INK, align="r", anchor="m")

    p2 = group(sh)
    card(p2.shapes, 8.20, 4.22, 4.34, 0.68, fill=SURFACE, line=RED)
    text(p2.shapes, 8.40, 4.22, 1.80, 0.68, "Seller 2", size=13, color=INK60, anchor="m")
    text(p2.shapes, 10.10, 4.22, 2.24, 0.68, "200,000 IQD", size=20, bold=True,
         font="Comfortaa", color=RED, align="r", anchor="m")

    # Bracket across the two prices on the screenshot + 2x callout on the right
    px, py, s = geom
    b0, b1 = M["rings"][0], M["rings"][1]
    pad_in = 8 * s
    x0_r = px + b0[2] * s + pad_in
    x1_l = px + b1[0] * s - pad_in
    y_mid = py + ((b0[1] + b0[3]) / 2) * s

    gb = group(sh)
    line(gb.shapes, x0_r, y_mid, x1_l, y_mid, RED, 2.5)
    mx_b = (x0_r + x1_l) / 2
    rect(gb.shapes, mx_b - 0.34, y_mid - 0.14, 0.68, 0.28, fill=RED, radius=0.14)
    text(gb.shapes, mx_b - 0.34, y_mid - 0.14, 0.68, 0.28, "2×",
         size=11, bold=True, color=WHITE, align="c", anchor="m")

    callout = group(sh)
    card(callout.shapes, 8.20, 5.10, 4.34, 1.78, fill=WHITE, line=RED, lw=2.0, shadow="elev2")
    text(callout.shapes, 8.35, 5.22, 4.04, 0.72, "2× the price", size=38, bold=True,
         font="Comfortaa", color=RED, align="c", anchor="m")
    text(callout.shapes, 8.35, 5.96, 4.04, 0.38, "same power bank", size=18, bold=True,
         color=INK, align="c", anchor="m")
    text(callout.shapes, 8.35, 6.36, 4.04, 0.32, "+100,000 IQD on the same screen",
         size=12.5, color=INK60, align="c", anchor="m")

    an.add([[fx(gl), fx(ctx_box)]])
    an.add([[fx(rings[1], "zoom"), fx(p1, "fade", 60)]])
    an.add([[fx(rings[0], "zoom"), fx(p2, "fade", 60)]])
    an.add([[fx(gb, "zoom"), fx(callout, "zoom", 60)]])
    return an


# ------------------------------------------------------------------ 3 evidence
def evidence(sl, ctx):
    sh = sl.shapes
    an = Anim()
    M = meta()
    specs = [
        ("ev-ibazzar-xiaomi", "Same item, listed twice", "60,000 vs 70,000 IQD"),
        ("ev-instagram-noprice", "No price — just 'DM us'", "Buyer asks: “How much?”"),
        ("ev-vacuum-fakedeal", "A fake 35% discount", "95,000 IG vs 133,250 “deal”"),
    ]
    cards, rings = [], []
    for i, (key, title, sub) in enumerate(specs):
        x, y = [0.79, 4.815, 8.84][i], 2.56
        g = group(sh)
        card(g.shapes, x, y, 3.70, 3.42)
        rect(g.shapes, x + 0.15, y + 0.14, 3.40, 2.42, fill=SURFACE, radius=0.10)
        pic, geom = pic_contain(g.shapes, A(key + ".jpg"), x + 0.23, y + 0.22, 3.24, 2.26)
        text(g.shapes, x + 0.15, y + 2.64, 3.40, 0.36, title, size=15, bold=True,
             align="c", anchor="m")
        text(g.shapes, x + 0.15, y + 3.00, 3.40, 0.30, sub, size=11.5, color=INK60,
             align="c", anchor="m")
        cards.append(g)
        rg = group(sh)
        for box in M[key]["rings"]:
            ring(rg.shapes, geom, box)
        rings.append(rg)

    bar = group(sh)
    rect(bar.shapes, 0.79, 6.14, 11.75, 0.74, fill=BLUE12, line=BLUE, lw=1.25, radius=0.14)
    text(bar.shapes, 1.10, 6.14, 1.55, 0.74, "97%", size=32, bold=True, color=BLUE,
         font="Comfortaa", align="c", anchor="m")
    text(bar.shapes, 2.75, 6.14, 9.50, 0.74,
         "of 179 shoppers we surveyed see this.", size=18, bold=True, color=INK, anchor="m")

    for c, rg in zip(cards, rings):
        an.add([[fx(c)], [fx(rg, "zoom", 80)]])
    an.add([[fx(bar, "zoom")]])
    return an


# ------------------------------------------------------------------ 4 solution
def solution(sl, ctx, mode="anim", frame_shapes=None):
    """mode: anim | static. Click 0 = Cheapify brand reveal; Click 1 = headline + chaos; Click 2 = master page; Click 3 = Best Value."""
    sh = sl.shapes
    an = Anim()

    reveal = []
    chaos = []
    if mode == "anim":
        w = 1.30
        logo_g = group(sh)
        pic_contain(logo_g.shapes, A("cheapify-logo.png"), (SLIDE_W - w) / 2, 2.05, w, w * 9 / 7)
        wm = grp_text(sh, 0, 3.85, SLIDE_W, 0.90, "Cheapify", size=54, bold=True,
                      font="Comfortaa", color=INK, align="c", anchor="m")
        slogan = grp_text(sh, 0, 4.78, SLIDE_W, 0.48, "The bright side of choosing.", size=22,
                          color=BLUE, font="Comfortaa", align="c", anchor="m")
        reveal = [logo_g, wm, slogan]

        for x, y, src, price, dm in D.CHAOS:
            g = group(sh)
            card(g.shapes, x, y, 2.15, 0.95)
            text(g.shapes, x + 0.15, y + 0.10, 1.9, 0.2, src, size=10, color=INK60)
            text(g.shapes, x + 0.15, y + 0.30, 1.9, 0.22, "Anker 25K 165W", size=11)
            text(g.shapes, x + 0.15, y + 0.52, 1.9, 0.32, price, size=14 if dm else 16,
                 bold=True, color=RED if dm else INK, anchor="m")
            chaos.append(g)

    master = group(sh)
    card(master.shapes, 0.79, 2.68, 8.35, 4.18, shadow="elev2")
    pic_contain(master.shapes, A("product-anker.png"), 1.05, 2.92, 1.30, 0.95)
    text(master.shapes, 2.55, 2.92, 6.3, 0.40, "Anker Power Bank 25,000 mAh · 165 W", size=17,
         bold=True, anchor="m")
    text(master.shapes, 2.55, 3.34, 6.3, 0.30, "One page · every verified seller", size=12,
         color=INK60, anchor="m")
    cols = [("Seller", 1.05, 1.85, "l"), ("Item", 3.00, 1.10, "r"), ("Delivery", 4.20, 1.05, "r"),
            ("Doorstep total", 5.35, 1.45, "r"), ("Arrives", 7.00, 0.95, "l")]
    for t, x, w, al in cols:
        text(master.shapes, x, 3.96, w, 0.25, t, size=10.5, bold=True, color=INK60, align=al,
             anchor="m")

    tint = group(sh)
    rect(tint.shapes, 0.95, 4.28, 8.03, 0.54, fill=GREEN8, radius=0.08)

    rows = []
    for i, r in enumerate(D.SELLERS):
        y = 4.28 + i * 0.56
        g = group(sh)
        line(g.shapes, 1.05, y + 0.54, 8.85, y + 0.54, NEUTRAL, 0.75)
        for j, (t, (_, x, w, al)) in enumerate(zip(r, cols)):
            text(g.shapes, x, y, w, 0.54, t, size=13, bold=(j == 3), align=al, anchor="m")
        rows.append(g)

    pill = group(sh)
    rect(pill.shapes, 7.72, 4.35, 1.22, 0.40, fill=GREEN, radius=0.20)
    icon(pill.shapes, "sparkle", WHITE, 7.82, 4.45, 0.20)
    text(pill.shapes, 8.05, 4.35, 0.85, 0.40, "BEST VALUE", size=9.5, bold=True, color=WHITE,
         anchor="m")

    rail = group(sh)
    card(rail.shapes, 9.40, 2.68, 3.14, 4.18, fill=SURFACE, line=NEUTRAL)
    text(rail.shapes, 9.65, 2.90, 2.64, 0.34, "Best Value rules", size=15, bold=True,
         color=INK, anchor="m")
    legend = []
    for i, (ic_name, t) in enumerate(D.RANKING):
        y = 3.48 + i * 0.78
        g = group(sh)
        oval(g.shapes, 9.85, y + 0.25, 0.25, fill=BLUE12)
        icon_c(g.shapes, ic_name, BLUE, 9.85, y + 0.25, 0.26)
        text(g.shapes, 10.20, y, 2.24, 0.50, f"{i + 1}. {t}", size=12, bold=True, anchor="m",
             wrap=False)
        legend.append(g)

    tag = group(sh)
    rect(tag.shapes, 9.65, 5.98, 2.64, 0.62, fill=BLUE12, radius=0.12)
    text(tag.shapes, 9.65, 5.98, 2.64, 0.62, "Ranking can't be bought.", size=13.5, bold=True,
         color=BLUE, align="c", anchor="m")

    if mode == "anim":
        an.add([[fx(reveal[0], "zoom")], [fx(reveal[1], "fade"), fx(reveal[2], "fade", 60)]],
               auto=True)
        head_fxs = [fx(s, "fade", 160) for s in (frame_shapes or ())]
        an.add([[fx(r, "fadeout") for r in reveal] + head_fxs])
        an.add(stagger(chaos, "fade"))
        an.add([[fx(c, "fadeout") for c in chaos] + [fx(master, "zoom", 180)]] + stagger(rows, "fade"))
        an.add([[fx(tint), fx(pill, "zoom"), fx(rail, "fade")]] + stagger(legend, "fade") +
               [[fx(tag, "zoom", 60)]])
    return an


# ------------------------------------------------------------------ 5 value
def value(sl, ctx):
    sh = sl.shapes
    an = Anim()
    div = group(sh)
    line(div.shapes, 6.665, 2.80, 6.665, 6.85, NEUTRAL, 1.0)
    heads = []
    cols = [
        (0.95, "shopping-bag", "For shoppers", [
            ("eye", "Every price, side by side", "No more checking ten pages"),
            ("message-circle-off", "Order in 30 seconds", "No “price?” DMs, no waiting"),
            ("banknote", "Cash on delivery or card", "Doorstep total shown upfront")]),
        (7.05, "store", "For merchants", [
            ("package-check", "Orders, not interrogations", "Ready orders with address and variant"),
            ("layout-dashboard", "Free dashboard", "Stock, orders and payouts in one place"),
            ("percent", "Fair, low fee", "About 3.8% on a typical 25,000 IQD order")]),
    ]
    row_groups = []
    for x0, hic, htitle, rows in cols:
        g = group(sh)
        oval(g.shapes, x0 + 0.275, 2.78 + 0.275, 0.275, fill=BLUE12)
        icon_c(g.shapes, hic, BLUE, x0 + 0.275, 2.78 + 0.275, 0.30)
        text(g.shapes, x0 + 0.75, 2.78, 4.5, 0.55, htitle, size=20, bold=True, anchor="m")
        heads.append(g)
        rg = []
        for i, (ic, ph, sub) in enumerate(rows):
            y = 3.70 + i * 1.0
            r = group(sh)
            oval(r.shapes, x0 + 0.275, y + 0.275, 0.275, fill=BLUE12)
            icon_c(r.shapes, ic, BLUE, x0 + 0.275, y + 0.275, 0.30)
            text(r.shapes, x0 + 0.75, y - 0.02, 4.9, 0.34, ph, size=18, bold=True, anchor="m")
            text(r.shapes, x0 + 0.75, y + 0.34, 4.9, 0.28, sub, size=13, color=INK60, anchor="t")
            rg.append(r)
        row_groups.append(rg)
    an.add([[fx(heads[0]), fx(heads[1]), fx(div)]], auto=True)
    an.add(stagger(row_groups[0], "fade"))
    an.add(stagger(row_groups[1], "fade"))
    return an


# ------------------------------------------------------------------ 6 market
def _pill(parent, x, y, tag, w=0.84):
    est = tag == "estimate"
    rect(parent, x, y, w, 0.22, fill=WHITE if est else NEUTRAL, line=ORANGE if est else None,
         lw=1.25, radius=0.11)
    text(parent, x, y, w, 0.22, tag, size=9, bold=est, color=INK, align="c", anchor="m")


def _tangents(parent, c1, r1, c2, r2, cy):
    dist = c2 - c1
    sn = (r1 - r2) / dist
    cs = math.sqrt(1 - sn * sn)
    for sgn in (-1, 1):
        line(parent, c1 + r1 * sn, cy + sgn * r1 * cs, c2 + r2 * sn, cy + sgn * r2 * cs, INK35,
             1.25, MSO_LINE.DASH)


def market(sl, ctx):
    sh = sl.shapes
    an = Anim()
    CY = 4.35

    def circle(cx, d, fill, tcol, head, num, nsz, hsz, sub):
        g = group(sh)
        oval(g.shapes, cx, CY, d / 2, fill=fill)
        text(g.shapes, cx - d / 2 + 0.1, CY - 0.66, d - 0.2, 0.28, head, size=hsz, bold=True,
             color=tcol, align="c", anchor="m")
        text(g.shapes, cx - d / 2 + 0.1, CY - 0.32, d - 0.2, 0.64, num, size=nsz, bold=True,
             font="Comfortaa", color=tcol, align="c", anchor="m")
        text(g.shapes, cx - d / 2 + 0.1, CY + 0.34, d - 0.2, 0.26, sub,
             size=12 if hsz > 12 else 11,
             color=tcol if fill == BLUE else INK60, align="c", anchor="m")
        return g

    c1 = circle(2.35, 2.85, NEUTRAL, INK, "Iraq", "46.1M", 32, 13.5, "people")
    c2 = circle(5.80, 2.20, BLUE12, INK, "Duhok governorate", "1.60M", 28, 11.5, "people")
    c3 = circle(8.65, 1.85, BLUE, WHITE, "Launch area", "1.06M", 25, 11.5, "people")

    def under(cx, lines):
        g = group(sh)
        text(g.shapes, cx - 1.5, 5.95, 3.0, 0.26, lines, size=11.5, color=INK60, align="c",
             anchor="m")
        return g

    u1 = under(2.35, "39.6M online · $1.32B a year")
    u2 = under(5.80, "≈ 1.34M online · ≈ $46M a year")
    u3 = group(sh)
    text(u3.shapes, 8.65 - 1.5, 5.95, 3.0, 0.26, "Duhok · Semel · Zakho", size=12, bold=True,
         color=INK, align="c", anchor="m")

    t1 = group(sh)
    _tangents(t1.shapes, 2.35, 1.425, 5.80, 1.10, CY)
    t2 = group(sh)
    _tangents(t2.shapes, 5.80, 1.10, 8.65, 0.925, CY)

    def stat(y, ic, num, lbl):
        g = group(sh)
        icon(g.shapes, ic, BLUE, 9.85, y + 0.06, 0.40)
        text(g.shapes, 10.40, y - 0.04, 2.1, 0.38, num, size=21, bold=True, font="Comfortaa",
             anchor="m")
        text(g.shapes, 10.40, y + 0.35, 2.1, 0.22, lbl, size=11, color=INK60, anchor="m")
        return g

    s1 = stat(2.70, "wifi", "≈ 0.89M", "online")
    s2 = stat(3.55, "shopping-cart", "≈ $30M", "a year online")

    be = group(sh)
    card(be.shapes, 9.85, 4.45, 2.69, 2.20, fill=BLUE12, line=BLUE, lw=1.5)
    text(be.shapes, 10.00, 4.58, 2.39, 0.56, "~390", size=34, bold=True, font="Comfortaa",
         color=BLUE, align="c", anchor="m")
    text(be.shapes, 10.00, 5.16, 2.39, 0.48, ["regular shoppers", "to break even"], size=13.5,
         bold=True, color=INK, align="c", anchor="m")
    text(be.shapes, 10.00, 5.76, 2.39, 0.72,
         ["≈ 585 orders a month", "0.4% of launch-area online shopping"], size=10.5, color=INK60,
         align="c", anchor="m")

    an.add([[fx(c1, "zoom"), fx(u1, "zoom")]], auto=True)
    an.add([[fx(t1), fx(c2, "zoom"), fx(u2, "zoom")]])
    an.add([[fx(t2), fx(c3, "zoom"), fx(u3, "zoom")]] + stagger([s1, s2], "fade"))
    an.add([[fx(be, "zoom")]])
    return an


# ------------------------------------------------------------------ 7 customers
def customers(sl, ctx):
    sh = sl.shapes
    an = Anim()

    # Left card — Shoppers (x=0.79..6.44, y=2.58..6.80)
    lcard = group(sh)
    card(lcard.shapes, 0.79, 2.58, 5.65, 4.22)
    oval(lcard.shapes, 1.24, 2.94, 0.22, fill=BLUE12)
    icon_c(lcard.shapes, "shopping-bag", BLUE, 1.24, 2.94, 0.24)
    text(lcard.shapes, 1.56, 2.76, 2.20, 0.36, "Shoppers", size=17, bold=True, anchor="m")
    rect(lcard.shapes, 4.92, 2.82, 1.28, 0.24, fill=SURFACE, line=NEUTRAL, lw=0.75, radius=0.12)
    text(lcard.shapes, 4.92, 2.82, 1.28, 0.24, "targeting plan", size=9.5, bold=True, color=INK60,
         align="c", anchor="m")
    line(lcard.shapes, 1.03, 5.56, 6.20, 5.56, NEUTRAL, 1.0)

    segs = (
        (3.30, "briefcase", "Time-poor professionals", "Chargers, perfume, gadgets", "23–38"),
        (4.02, "shopping-basket", "Household budget buyers", "Kitchen, home, personal care", "26–48"),
        (4.74, "graduation-cap", "Students & deal hunters", "Cables, earbuds, gaming", "18–24"),
    )
    srows = []
    for ry, ic, nm, buys, age in segs:
        r = group(sh)
        rect(r.shapes, 1.03, ry, 5.17, 0.62, fill=SURFACE, line=NEUTRAL, lw=0.75, radius=0.10)
        oval(r.shapes, 1.40, ry + 0.31, 0.22, fill=BLUE12)
        icon_c(r.shapes, ic, BLUE, 1.40, ry + 0.31, 0.24)
        text(r.shapes, 1.74, ry + 0.06, 3.30, 0.26, nm, size=13, bold=True, color=INK, anchor="m",
             wrap=False)
        text(r.shapes, 1.74, ry + 0.32, 3.30, 0.22, buys, size=11, color=INK60, anchor="m",
             wrap=False)
        rect(r.shapes, 5.22, ry + 0.18, 0.80, 0.26, fill=BLUE, radius=0.13)
        text(r.shapes, 5.22, ry + 0.18, 0.80, 0.26, age, size=10.5, bold=True, color=WHITE,
             align="c", anchor="m")
        srows.append(r)

    g97 = group(sh)
    gauge(g97.shapes, 1.56, 6.18, 0.92, 0.97, thick=0.11)
    text(g97.shapes, 1.10, 5.96, 0.92, 0.44, "97%", size=14.5, bold=True, font="Comfortaa",
         align="c", anchor="m")
    text(g97.shapes, 2.22, 5.88, 3.90, 0.30, "notice big price gaps on the same item",
         size=13.5, bold=True, color=INK, anchor="m", wrap=False)
    text(g97.shapes, 2.22, 6.20, 3.90, 0.24, "179 surveyed shoppers", size=11, color=INK60,
         anchor="m")

    # Right card — Merchants (x=6.89..12.54, y=2.58..6.80)
    rcard = group(sh)
    card(rcard.shapes, 6.89, 2.58, 5.65, 4.22)
    oval(rcard.shapes, 7.34, 2.94, 0.22, fill=BLUE12)
    icon_c(rcard.shapes, "store", BLUE, 7.34, 2.94, 0.24)
    text(rcard.shapes, 7.66, 2.76, 2.20, 0.36, "Merchants", size=17, bold=True, anchor="m")
    rect(rcard.shapes, 10.66, 2.82, 1.64, 0.24, fill=BLUE12, radius=0.12)
    text(rcard.shapes, 10.66, 2.82, 1.64, 0.24, "Duhok social shops", size=9.5, bold=True,
         color=BLUE, align="c", anchor="m")
    line(rcard.shapes, 7.13, 5.56, 12.30, 5.56, NEUTRAL, 1.0)

    m_items = (
        (3.30, "megaphone", "Social-commerce sellers", "Sell via DMs with digital photos ready",
         "IG · FB · TikTok", BLUE12, BLUE),
        (4.02, "users", "1,500 – 50,000 followers", "Active local audience per page",
         "20–150 products", BLUE12, BLUE),
        (4.74, "handshake", "20 founding stores at launch", "Signed in person · 0% fee in month 1",
         "~8 leads ready", BLUE12, BLUE),
    )
    mrows = []
    for ry, ic, nm, sub, tag, tfill, tcol in m_items:
        r = group(sh)
        rect(r.shapes, 7.13, ry, 5.17, 0.62, fill=SURFACE, line=NEUTRAL, lw=0.75, radius=0.10)
        oval(r.shapes, 7.50, ry + 0.31, 0.22, fill=BLUE12)
        icon_c(r.shapes, ic, BLUE, 7.50, ry + 0.31, 0.24)
        text(r.shapes, 7.84, ry + 0.06, 2.75, 0.26, nm, size=13, bold=True, color=INK, anchor="m",
             wrap=False)
        text(r.shapes, 7.84, ry + 0.32, 2.75, 0.22, sub, size=11, color=INK60, anchor="m",
             wrap=False)
        rect(r.shapes, 10.62, ry + 0.18, 1.52, 0.26, fill=tfill, radius=0.13)
        text(r.shapes, 10.62, ry + 0.18, 1.52, 0.26, tag, size=10, bold=True, color=tcol,
             align="c", anchor="m")
        mrows.append(r)

    gs = []
    for cx, tx, pct, lbl, sub in (
        (7.64, 8.24, 0.85, "sell on IG / FB", "20 surveyed shops"),
        (10.36, 10.96, 0.75, "want to try", "Cheapify at launch"),
    ):
        g = group(sh)
        gauge(g.shapes, cx, 6.18, 0.92, pct, thick=0.11)
        text(g.shapes, cx - 0.46, 5.96, 0.92, 0.44, f"{int(pct * 100)}%", size=14.5, bold=True,
             font="Comfortaa", align="c", anchor="m")
        text(g.shapes, tx, 5.88, 1.48, 0.30, lbl, size=13, bold=True, color=INK, anchor="m",
             wrap=False)
        text(g.shapes, tx, 6.20, 1.48, 0.24, sub, size=10.5, color=INK60, anchor="m", wrap=False)
        gs.append(g)

    an.add([[fx(lcard)]] + stagger(srows, "fade") + [[fx(g97, "zoom")]], auto=True)
    an.add([[fx(rcard)]] + stagger(mrows, "fade") + stagger(gs, "zoom"))
    return an
