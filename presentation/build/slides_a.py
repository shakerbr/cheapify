"""Slides 1-7."""
import json

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
    w = 1.25
    logo, _ = pic_contain(sh, A("cheapify-logo.png"), (SLIDE_W - w) / 2, 1.80, w, w * 9 / 7)
    wm = text(sh, 0, 3.45, SLIDE_W, 0.95, "Cheapify", size=54, bold=True, font="Comfortaa",
              align="c", anchor="m")
    slogan = text(sh, 0, 4.38, SLIDE_W, 0.5, "The bright side of choosing.", size=22,
                  color=BLUE, font="Comfortaa", align="c", anchor="m")
    f1 = text(sh, 0, 5.18, SLIDE_W, 0.32, "Shakir Bashar · Founder", size=14, bold=True,
              align="c", anchor="m")
    f2 = text(sh, 0, 5.50, SLIDE_W, 0.3, "Youth Entrepreneurship Program · Final Pitch",
              size=12, color=INK60, align="c", anchor="m")
    an = Anim()
    an.add([[fx(logo, "zoom")], [fx(wm, "fade")], [fx(slogan, "fade"), fx(f1, "fade"),
                                                      fx(f2, "fade")]], auto=True)
    return an


# ------------------------------------------------------------------ 2 problem
def problem(sl, ctx):
    sh = sl.shapes
    an = Anim()
    M = meta()["ev-miswag-anker"]
    gl = group(sh)
    card(gl.shapes, 0.79, 2.70, 4.10, 3.70)
    rect(gl.shapes, 0.94, 2.85, 3.80, 2.95, fill=SURFACE, radius=0.08)
    pic, geom = pic_contain(gl.shapes, A("ev-miswag-anker.jpg"), 0.94, 2.85, 3.80, 2.95)
    text(gl.shapes, 0.94, 5.88, 3.80, 0.40, "Miswag app — same search, same screen (Oct 20, 2026)",
         size=11, color=INK60)
    rings = []
    for box in M["rings"]:
        g = group(sh)
        ring(g.shapes, geom, box)
        rings.append(g)

    # chart
    X0, X1, AY = 5.60, 12.30, 5.60
    px = lambda v: X0 + (v - 80000) / 130000 * (X1 - X0)
    ga = group(sh)
    text(ga.shapes, 5.40, 2.70, 5.0, 0.28, "Every price we found for this model (IQD)", size=13,
         bold=True, color=INK60)
    for lbl, col, lx in (("Instagram", INK, 10.05), ("Miswag", BLUE, 11.05), ("iBazzar", ORANGE, 11.85)):
        oval(ga.shapes, lx + 0.07, 2.86, 0.07, fill=col)
        text(ga.shapes, lx + 0.20, 2.72, 0.9, 0.28, lbl, size=11, anchor="m")
    line(ga.shapes, X0, AY, X1, AY, INK35, 1.0)
    for v in range(80000, 200001, 20000):
        line(ga.shapes, px(v), AY, px(v), AY + 0.07, INK35, 1.0)
        text(ga.shapes, px(v) - 0.4, AY + 0.11, 0.8, 0.22, f"{v // 1000}k", size=10, color=INK60,
             align="c")
    chan = {"IG": INK, "MS": BLUE, "IB": ORANGE}
    dots = []
    placed = []
    for v, ch in D.DOTS:
        lvl = 0
        while any(l == lvl and abs(px(v) - x) < 0.26 for x, l in placed):
            lvl += 1
        placed.append((px(v), lvl))
        g = group(sh)
        oval(g.shapes, px(v), AY - 0.20 - lvl * 0.28, 0.12, fill=chan[ch], line=WHITE, lw=0.75)
        dots.append(g)
    gb = group(sh)
    xa, xb, by = px(90000), px(200000), 4.05
    line(gb.shapes, xa, by, xb, by, RED, 2.0)
    line(gb.shapes, xa, by, xa, by + 0.14, RED, 2.0)
    line(gb.shapes, xb, by, xb, by + 0.14, RED, 2.0)
    pct = grp_text(sh, (xa + xb) / 2 - 1.5, 3.05, 3.0, 0.6, "+122%", size=40, bold=True,
                   color=RED, font="Comfortaa", align="c", anchor="m")
    sub = grp_text(sh, (xa + xb) / 2 - 2.5, 3.62, 5.0, 0.3, "≈ 110,000 IQD more for the same model",
                   size=14, bold=True, align="c", anchor="m")

    an.add([[fx(gl)]], auto=True)
    an.add([[fx(rings[0], "zoom")], [fx(rings[1], "zoom", 80)]])
    an.add([[fx(ga)]] + stagger(dots, "zoom"))
    an.add([[fx(gb), fx(pct, "zoom")], [fx(sub, "fade", 80)]])
    return an


# ------------------------------------------------------------------ 3 evidence
def evidence(sl, ctx):
    sh = sl.shapes
    an = Anim()
    M = meta()
    specs = [
        ("ev-ibazzar-xiaomi", "Same product, listed twice", "iBazzar app · 60,000 vs 70,000 IQD"),
        ("ev-instagram-noprice", "No price: 'call to order'",
         "Instagram · a buyer asks: “How much is it?”"),
        ("ev-vacuum-fakedeal", "A fake “deal”",
         "Same Newal vacuum: 95,000 on Instagram · “−35%” at 133,250 on Miswag"),
    ]
    cards, rings = [], []
    for i, (key, title, sub) in enumerate(specs):
        x, y = [0.79, 4.89, 8.99][i], 2.70
        g = group(sh)
        card(g.shapes, x, y, 3.55, 3.30)
        rect(g.shapes, x + 0.15, y + 0.15, 3.25, 2.20, fill=SURFACE, radius=0.08)
        pic, geom = pic_contain(g.shapes, A(key + ".jpg"), x + 0.15, y + 0.15, 3.25, 2.20)
        text(g.shapes, x + 0.15, y + 2.45, 3.25, 0.36, title, size=14, bold=True, anchor="m")
        text(g.shapes, x + 0.15, y + 2.82, 3.25, 0.40, sub, size=10.5, color=INK60, anchor="t")
        cards.append(g)
        rg = group(sh)
        for box in M[key]["rings"]:
            ring(rg.shapes, geom, box)
        rings.append(rg)
    s97 = grp_text(sh, 0.79, 6.15, 1.45, 0.7, "97%", size=34, bold=True, color=BLUE,
                   font="Comfortaa", anchor="m")
    t97 = grp_text(sh, 2.30, 6.18, 4.10, 0.7,
                   "of 179 surveyed shoppers notice big price gaps on the same item", size=14,
                   anchor="m")
    s55 = grp_text(sh, 6.90, 6.15, 1.45, 0.7, "55%", size=34, bold=True, color=BLUE,
                   font="Comfortaa", anchor="m")
    t55 = grp_text(sh, 8.40, 6.18, 4.10, 0.7,
                   "of merchants pick answering “price?” messages as a top headache — the most common answer",
                   size=14, anchor="m")
    for c, rg in zip(cards, rings):
        an.add([[fx(c)], [fx(rg, "zoom", 80)]])
    an.add([[fx(s97, "zoom"), fx(t97)], [fx(s55, "zoom", 80), fx(t55, delay=80)]])
    return an


# ------------------------------------------------------------------ 4 solution
def solution(sl, ctx, mode="anim"):
    """mode: anim | static."""
    sh = sl.shapes
    an = Anim()
    chaos = []
    if mode == "anim":
        for x, y, src, price, dm in D.CHAOS:
            g = group(sh)
            card(g.shapes, x, y, 2.15, 0.95)
            text(g.shapes, x + 0.15, y + 0.10, 1.9, 0.2, src, size=10, color=INK60)
            text(g.shapes, x + 0.15, y + 0.30, 1.9, 0.22, "Anker 25K 165W", size=11)
            text(g.shapes, x + 0.15, y + 0.52, 1.9, 0.32, price, size=14 if dm else 16,
                 bold=True, color=RED if dm else INK, anchor="m")
            chaos.append(g)
    master = group(sh)
    card(master.shapes, 1.90, 2.75, 7.50, 4.15, shadow="elev2")
    pic_contain(master.shapes, A("product-anker.png"), 2.15, 3.00, 1.30, 0.95)
    text(master.shapes, 3.65, 3.00, 5.6, 0.4, "Anker Power Bank 25,000 mAh · 165 W", size=17,
         bold=True, anchor="m")
    text(master.shapes, 3.65, 3.42, 5.6, 0.3, "One page · every verified seller", size=12,
         color=INK60, anchor="m")
    cols = [("Seller", 2.15, 1.9, "l"), ("Item", 4.20, 1.15, "r"), ("Delivery", 5.45, 1.05, "r"),
            ("Doorstep total", 6.60, 1.45, "r"), ("Arrives", 8.20, 1.05, "l")]
    for t, x, w, al in cols:
        text(master.shapes, x, 4.02, w, 0.25, t, size=10.5, bold=True, color=INK60, align=al,
             anchor="m")
    tint = group(sh)
    rect(tint.shapes, 2.05, 4.32, 7.20, 0.52, fill=GREEN8, radius=0.08)
    rows = []
    for i, r in enumerate(D.SELLERS):
        y = 4.32 + i * 0.54
        g = group(sh)
        line(g.shapes, 2.15, y + 0.52, 9.15, y + 0.52, NEUTRAL, 0.75)
        for j, (t, (_, x, w, al)) in enumerate(zip(r, cols)):
            text(g.shapes, x, y, w, 0.52, t, size=13, bold=(j == 3), align=al, anchor="m")
        rows.append(g)
    pill = group(sh)
    rect(pill.shapes, 8.95, 4.36, 1.35, 0.40, fill=GREEN, radius=0.20)
    icon(pill.shapes, "sparkle", WHITE, 9.07, 4.46, 0.20)
    text(pill.shapes, 9.31, 4.36, 0.95, 0.40, "BEST VALUE", size=10, bold=True, color=WHITE,
         anchor="m")
    legend = []
    for i, t in enumerate(D.RANKING):
        y = 4.30 + i * 0.60
        g = group(sh)
        oval(g.shapes, 10.78, y + 0.18, 0.18, fill=BLUE)
        text(g.shapes, 10.60, y, 0.36, 0.36, str(i + 1), size=12, bold=True, color=WHITE,
             align="c", anchor="m")
        text(g.shapes, 11.05, y, 1.5, 0.40, t, size=12, bold=True, anchor="m")
        legend.append(g)
    tag = grp_text(sh, 10.60, 6.15, 1.94, 0.5, "Ranking can't be bought.", size=12.5, bold=True,
                   color=BLUE, anchor="t")

    if mode == "anim":
        an.add(stagger(chaos, "fade"), auto=True)
        an.add([[fx(c, "fadeout") for c in chaos] + [fx(master, "zoom", 200)]])
        an.add(stagger(rows, "fade"))
        an.add([[fx(tint), fx(pill, "zoom")]] + stagger(legend, "fade") + [[fx(tag, "fade", 80)]])
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
def _pill(parent, x, y, tag, w=0.80):
    est = tag == "estimate"
    rect(parent, x, y, w, 0.22, fill=WHITE if est else NEUTRAL, line=ORANGE if est else None,
         lw=1.25, radius=0.11)
    text(parent, x, y, w, 0.22, tag, size=9, bold=est, color=INK, align="c", anchor="m")


def _tangents(parent, c1, r1, c2, r2, cy):
    import math
    D = c2 - c1
    sn = (r1 - r2) / D
    cs = math.sqrt(1 - sn * sn)
    for sgn in (-1, 1):
        line(parent, c1 + r1 * sn, cy + sgn * r1 * cs, c2 + r2 * sn, cy + sgn * r2 * cs, INK35,
             1.25, MSO_LINE.DASH)


def market(sl, ctx):
    sh = sl.shapes
    an = Anim()
    CY = 4.20
    # circles: (cx, d, fill, text color, head, number, num size, under lines, tag)
    def circle(cx, d, fill, tcol, head, num, nsz, hsz, sub):
        g = group(sh)
        oval(g.shapes, cx, CY, d / 2, fill=fill)
        text(g.shapes, cx - d / 2 + 0.1, CY - 0.62, d - 0.2, 0.26, head, size=hsz, bold=True,
             color=tcol, align="c", anchor="m")
        text(g.shapes, cx - d / 2 + 0.1, CY - 0.30, d - 0.2, 0.60, num, size=nsz, bold=True,
             font="Comfortaa", color=tcol, align="c", anchor="m")
        text(g.shapes, cx - d / 2 + 0.1, CY + 0.32, d - 0.2, 0.24, sub, size=12 if hsz > 12 else 11,
             color=tcol if fill == BLUE else INK60, align="c", anchor="m")
        return g

    c1 = circle(2.30, 2.60, NEUTRAL, INK, "Iraq", "46.1M", 30, 13, "people")
    c2 = circle(5.70, 2.00, BLUE12, INK, "Duhok governorate", "1.60M", 26, 11, "people")
    c3 = circle(8.65, 1.70, BLUE, WHITE, "Launch area", "1.06M", 24, 11, "people")

    def under(cx, lines, tag):
        g = group(sh)
        text(g.shapes, cx - 1.5, 5.60, 3.0, 0.24, lines, size=11, color=INK60, align="c",
             anchor="m")
        if tag:
            _pill(g.shapes, cx - 0.40, 5.90, tag)
        return g

    u1 = under(2.30, "39.6M online · $1.32B a year", "published")
    u2 = under(5.70, "≈ 1.34M online · ≈ $46M a year", "estimate")
    u3 = group(sh)
    text(u3.shapes, 8.65 - 1.5, 5.60, 3.0, 0.24, "Duhok · Semel · Zakho", size=11, bold=True,
         color=INK, align="c", anchor="m")
    t1 = group(sh)
    _tangents(t1.shapes, 2.30, 1.30, 5.70, 1.00, CY)
    t2 = group(sh)
    _tangents(t2.shapes, 5.70, 1.00, 8.65, 0.85, CY)

    def stat(y, ic, num, lbl):
        g = group(sh)
        icon(g.shapes, ic, BLUE, 9.90, y + 0.06, 0.40)
        text(g.shapes, 10.45, y - 0.04, 2.0, 0.38, num, size=20, bold=True, font="Comfortaa",
             anchor="m")
        text(g.shapes, 10.45, y + 0.35, 0.95, 0.22, lbl, size=11, color=INK60, anchor="m")
        _pill(g.shapes, 11.62, y + 0.35, "estimate")
        return g

    s1 = stat(3.05, "wifi", "≈ 0.89M", "online")
    s2 = stat(3.85, "shopping-cart", "≈ $30M", "a year online")
    pie = group(sh)
    oval(pie.shapes, 10.475, 5.225, 0.475, fill=NEUTRAL)
    pie_slice(pie.shapes, 10.475, 5.225, 0.475, 270, 276, BLUE)
    text(pie.shapes, 11.15, 4.88, 1.39, 0.34, "0.4%", size=18, bold=True, font="Comfortaa",
         color=BLUE, anchor="m")
    text(pie.shapes, 11.15, 5.24, 1.39, 0.5, "is all we need to break even", size=11,
         color=INK60)
    strip = group(sh)
    pts = [(1.60, "Launch: Duhok · Semel · Zakho", 2.9), (5.55, "Next: Erbil · Mosul · Sulaymaniyah", 3.5),
           (10.30, "Then: all of Iraq", 2.0)]
    for px, lbl, tw in pts:
        oval(strip.shapes, px, 6.60, 0.08, fill=BLUE)
        text(strip.shapes, px + 0.18, 6.48, tw, 0.25, lbl, size=12, anchor="m")
    line(strip.shapes, 4.60, 6.60, 5.45, 6.60, INK35, 1.5)
    line(strip.shapes, 9.10, 6.60, 10.20, 6.60, INK35, 1.5)
    an.add([[fx(c1, "zoom"), fx(u1, "zoom")]], auto=True)
    an.add([[fx(t1), fx(c2, "zoom"), fx(u2, "zoom")]])
    an.add([[fx(t2), fx(c3, "zoom"), fx(u3, "zoom")]] + stagger([s1, s2], "fade") +
           [[fx(pie, "zoom", 80)]])
    an.add([[fx(strip)]])
    return an


# ------------------------------------------------------------------ 7 customers
def customers(sl, ctx):
    sh = sl.shapes
    an = Anim()
    head = group(sh)
    text(head.shapes, 0.79, 2.65, 1.5, 0.34, "Shoppers", size=16, bold=True, anchor="m")
    text(head.shapes, 2.05, 2.65, 2.0, 0.34, "target groups", size=10, color=INK60, anchor="m")
    avs, fades = [], []
    for cx, ic, age, nm in ((1.70, "briefcase", "23–38", "Professionals"),
                            (3.75, "house", "26–48", "Families"),
                            (5.80, "graduation-cap", "18–24", "Students")):
        a = group(sh)
        oval(a.shapes, cx, 3.85, 0.65, fill=BLUE12)
        icon_c(a.shapes, ic, BLUE, cx, 3.85, 0.60)
        avs.append(a)
        f = group(sh)
        rect(f.shapes, cx - 0.40, 4.62, 0.80, 0.26, fill=BLUE, radius=0.13)
        text(f.shapes, cx - 0.40, 4.62, 0.80, 0.26, age, size=11, bold=True, color=WHITE,
             align="c", anchor="m")
        text(f.shapes, cx - 0.95, 4.94, 1.90, 0.28, nm, size=13, bold=True, align="c", anchor="m")
        fades.append(f)
    g88 = group(sh)
    gauge(g88.shapes, 2.30, 6.05, 1.25, 0.88)
    text(g88.shapes, 1.70, 5.80, 1.2, 0.50, "88%", size=20, bold=True, font="Comfortaa",
         align="c", anchor="m")
    text(g88.shapes, 3.15, 5.82, 3.0, 0.28, "would use it", size=13, bold=True, anchor="m")
    text(g88.shapes, 3.15, 6.12, 3.0, 0.22, "179 surveyed shoppers", size=10, color=INK60)

    mh = group(sh)
    text(mh.shapes, 7.60, 2.65, 2.5, 0.34, "Merchants", size=16, bold=True, anchor="m")
    phone = group(sh)
    PX, PY, PW, PH = 7.60, 3.10, 1.85, 3.55
    rect(phone.shapes, PX, PY, PW, PH, fill=INK, radius=0.22)
    rect(phone.shapes, PX + 0.07, PY + 0.07, PW - 0.14, PH - 0.14, fill=WHITE, radius=0.17)
    oval(phone.shapes, PX + 0.35, PY + 0.45, 0.21, fill=BLUE12)
    icon_c(phone.shapes, "store", BLUE, PX + 0.35, PY + 0.45, 0.24)
    text(phone.shapes, PX + 0.64, PY + 0.28, 1.1, 0.20, "Your shop", size=9.5, bold=True,
         anchor="m")
    text(phone.shapes, PX + 0.64, PY + 0.48, 1.1, 0.18, "12.4k followers", size=8, color=INK60,
         anchor="m")
    px = PX + 0.13
    for lbl, w in (("Instagram", 0.56), ("Facebook", 0.58), ("TikTok", 0.40)):
        rect(phone.shapes, px, PY + 0.84, w, 0.20, fill=BLUE12, radius=0.10)
        text(phone.shapes, px, PY + 0.84, w, 0.20, lbl, size=8, bold=True, color=INK, align="c",
             anchor="m")
        px += w + 0.02
    for r_ in range(3):
        for c_ in range(2):
            rect(phone.shapes, PX + 0.15 + c_ * 0.80, PY + 1.20 + r_ * 0.74, 0.74, 0.64,
                 fill=NEUTRAL, radius=0.08)
    facts = []
    for y, ic, t in ((3.20, "users", "1.5k–50k followers"), (3.75, "package", "20–150 products")):
        g = group(sh)
        icon(g.shapes, ic, BLUE, 9.80, y, 0.36)
        text(g.shapes, 10.26, y - 0.02, 2.3, 0.40, t, size=13, bold=True, anchor="m")
        facts.append(g)
    gs = []
    for cx, pct, lbl in ((10.35, 0.85, "sell on IG / FB"), (11.85, 0.75, "want to try")):
        g = group(sh)
        gauge(g.shapes, cx, 5.35, 1.05, pct, thick=0.12)
        text(g.shapes, cx - 0.45, 5.15, 0.90, 0.40, f"{int(pct * 100)}%", size=16, bold=True,
             font="Comfortaa", align="c", anchor="m")
        text(g.shapes, cx - 0.75, 5.95, 1.50, 0.24, lbl, size=11, align="c", anchor="m")
        gs.append(g)
    lab20 = grp_text(sh, 9.80, 6.50, 2.74, 0.22, "20 surveyed merchants", size=10, color=INK60,
                     align="c")
    an.add([[fx(head)] + [fx(a, "zoom", i * 80, 250) for i, a in enumerate(avs)] ] +
           [[fx(f, "fade", i * 80, 250) for i, f in enumerate(fades)]] + [[fx(g88, "zoom")]],
           auto=True)
    an.add([[fx(mh), fx(phone)]] + stagger(facts, "fade") + stagger(gs, "zoom") + [[fx(lab20)]])
    return an


# ------------------------------------------------------------------ 7 product
def _screen_group(sh, k):
    g = group(sh)
    s = g.shapes
    SX, SY, SW, SH = 1.43, 2.70, 2.04, 4.14
    rect(s, SX, SY, SW, SH, fill=WHITE, radius=0.22)
    x = SX + 0.14
    w = SW - 0.28
    if k == 0:  # search
        pic_contain(s, A("cheapify-logo.png"), x, SY + 0.22, 0.22, 0.30)
        text(s, x + 0.30, SY + 0.22, 1.2, 0.30, "Cheapify", size=11, bold=True, font="Comfortaa",
             color=INK, anchor="m")
        rect(s, x, SY + 0.68, w, 0.36, fill=SURFACE, line=NEUTRAL, lw=0.75, radius=0.18)
        icon(s, "search", INK60, x + 0.10, SY + 0.78, 0.16)
        text(s, x + 0.34, SY + 0.68, w - 0.4, 0.36, "anker power bank", size=9, anchor="m")
        rows = [("Anker 25K · 165 W", "from 95,000 IQD · 4 sellers"),
                ("Anker 10K · 30 W", "from 35,000 IQD"),
                ("Xiaomi 10K · 165 W", "from 60,000 IQD")]
        for i, (n, sub) in enumerate(rows):
            y = SY + 1.25 + i * 0.90
            rect(s, x, y, 0.50, 0.50, fill=NEUTRAL, radius=0.08)
            text(s, x + 0.58, y + 0.02, w - 0.56, 0.22, n, size=8.5, bold=True, anchor="t")
            text(s, x + 0.58, y + 0.25, w - 0.58, 0.36, sub, size=8, color=INK60, anchor="t")
    elif k == 1:  # compare
        pic_contain(s, A("product-anker.png"), x, SY + 0.25, 0.50, 0.80)
        text(s, x + 0.60, SY + 0.40, 1.30, 0.3, "Anker 25K · 165 W", size=9.5, bold=True)
        text(s, x + 0.60, SY + 0.68, 1.2, 0.3, "4 sellers", size=9, color=INK60)
        data = [("Store A · Duhok", "95,000 IQD"), ("Store D · Erbil", "96,000 IQD"),
                ("Store B · Duhok", "102,000 IQD")]
        for i, (n, t) in enumerate(data):
            y = SY + 1.55 + i * 0.78
            rect(s, x - 0.02, y, w + 0.04, 0.64, fill=GREEN8 if i == 0 else WHITE,
                 line=GREEN if i == 0 else NEUTRAL, lw=1.0 if i == 0 else 0.75, radius=0.08)
            text(s, x + 0.08, y + 0.06, 1.5, 0.20, n, size=9, bold=True)
            text(s, x + 0.08, y + 0.25, 1.0, 0.20, t, size=10, bold=True)
            text(s, x + 0.08, y + 0.45, 1.5, 0.16, "Doorstep total", size=8, color=INK60)
        rect(s, x + w - 0.86, SY + 1.55 + 0.34, 0.80, 0.22, fill=GREEN, radius=0.11)
        text(s, x + w - 0.86, SY + 1.55 + 0.34, 0.80, 0.22, "BEST VALUE", size=8, bold=True,
             color=WHITE, align="c", anchor="m")
    elif k == 2:  # checkout
        text(s, x, SY + 0.25, w, 0.3, "Checkout", size=12, bold=True)
        text(s, x, SY + 0.60, w, 0.25, "Anker 25K · 165 W", size=9, color=INK60)
        for i, (a, b) in enumerate([("Item", "92,000"), ("Delivery (Duhok)", "3,000")]):
            y = SY + 1.05 + i * 0.34
            text(s, x, y, 1.1, 0.26, a, size=10, anchor="m")
            text(s, x + w - 0.8, y, 0.8, 0.26, b, size=10, align="r", anchor="m")
        line(s, x, SY + 1.80, x + w, SY + 1.80, NEUTRAL, 1.0)
        text(s, x, SY + 1.90, w, 0.22, "Doorstep total", size=10, bold=True, anchor="m")
        text(s, x, SY + 2.14, w, 0.34, "95,000 IQD", size=14, bold=True, anchor="m")
        rect(s, x, SY + 2.58, w, 0.42, fill=WHITE, line=BLUE, lw=1.0, radius=0.08)
        oval(s, x + 0.22, SY + 2.79, 0.09, line=BLUE, lw=1.25)
        oval(s, x + 0.22, SY + 2.79, 0.045, fill=BLUE)
        text(s, x + 0.42, SY + 2.58, w - 0.5, 0.42, "Cash on delivery", size=10, bold=True,
             anchor="m")
        rect(s, x, SY + 3.08, w, 0.42, fill=WHITE, line=NEUTRAL, lw=1.0, radius=0.08)
        oval(s, x + 0.22, SY + 3.29, 0.09, line=INK35, lw=1.25)
        text(s, x + 0.42, SY + 3.08, w - 0.5, 0.42, "Card / e-wallet", size=10, anchor="m")
        rect(s, x, SY + 3.62, w, 0.42, fill=BLUE, radius=0.12)
        text(s, x, SY + 3.62, w, 0.42, "Order now", size=12, bold=True, color=WHITE, align="c",
             anchor="m")
    elif k == 3:  # merchant
        text(s, x, SY + 0.25, w, 0.3, "Your store · Orders", size=11, bold=True)
        line(s, x, SY + 0.62, x + w, SY + 0.62, NEUTRAL, 1.0)
        rect(s, x, SY + 0.80, w, 2.05, fill=WHITE, line=NEUTRAL, lw=0.75, radius=0.10)
        text(s, x + 0.12, SY + 0.90, w - 0.2, 0.25, "New order", size=10, bold=True, color=BLUE)
        text(s, x + 0.12, SY + 1.18, w - 0.2, 0.25, "Anker 25K · Black · ×1", size=9)
        text(s, x + 0.12, SY + 1.46, w - 0.2, 0.40, "95,000 IQD · cash on delivery", size=9,
             bold=True)
        icon(s, "map-pin", INK60, x + 0.12, SY + 1.92, 0.16)
        text(s, x + 0.34, SY + 1.90, w - 0.4, 0.22, "Duhok — Malta", size=9, color=INK60,
             anchor="m")
        rect(s, x + 0.12, SY + 2.30, 0.66, 0.34, fill=BLUE, radius=0.08)
        text(s, x + 0.12, SY + 2.30, 0.66, 0.34, "Accept", size=9, bold=True, color=WHITE,
             align="c", anchor="m")
        rect(s, x + 0.86, SY + 2.30, 0.78, 0.34, fill=WHITE, line=BLUE, lw=1.0, radius=0.08)
        text(s, x + 0.86, SY + 2.30, 0.78, 0.34, "Print waybill", size=8, bold=True, color=BLUE,
             align="c", anchor="m")
        icon(s, "truck", BLUE, x + 0.02, SY + 3.15, 0.26)
        text(s, x + 0.36, SY + 3.12, w - 0.4, 0.32, "Courier pickup today", size=10, bold=True,
             anchor="m")
    else:  # payout
        text(s, x, SY + 0.25, w, 0.3, "Payout sent", size=12, bold=True)
        text(s, x, SY + 0.58, w, 0.22, "Order #1042 · delivered", size=9, color=INK60)
        text(s, x, SY + 0.80, w, 0.22, "Return window closed (48 h)", size=9, color=INK60)
        rect(s, x, SY + 1.20, w, 1.75, fill=WHITE, line=NEUTRAL, lw=0.75, radius=0.10)
        for i, (a, b) in enumerate([("Item", "92,000"), ("Cheapify fee", "−2,960")]):
            y = SY + 1.33 + i * 0.34
            text(s, x + 0.12, y, 1.0, 0.28, a, size=9.5, anchor="m")
            text(s, x + w - 1.0 - 0.12, y, 1.0, 0.28, b, size=9.5, align="r", anchor="m")
        line(s, x + 0.12, SY + 2.08, x + w - 0.12, SY + 2.08, NEUTRAL, 1.0)
        text(s, x + 0.12, SY + 2.18, w - 0.2, 0.22, "Paid to you", size=9.5, color=INK60)
        text(s, x + 0.12, SY + 2.42, w - 0.2, 0.40, "89,040 IQD", size=14, bold=True, color=BLUE,
             anchor="m")
    return g


def product(sl, ctx, mode="anim"):
    """mode: anim | static (S2 only, no overlays)."""
    sh = sl.shapes
    an = Anim()
    frame = group(sh)
    rect(frame.shapes, 1.35, 2.62, 2.20, 4.30, fill=INK, radius=0.30)
    rect(frame.shapes, 1.43, 2.70, 2.04, 4.14, fill=WHITE, radius=0.22)
    rect(frame.shapes, 2.15, 2.75, 0.60, 0.07, fill=INK, radius=0.035)

    bgs, rows, dots = [], [], []
    ys = [2.75 + i * 0.84 for i in range(5)]
    if mode != "static":
        for i, y in enumerate(ys):
            bg = group(sh)
            rect(bg.shapes, 4.50, y, 8.04, 0.76, fill=BLUE12, radius=0.12)
            bgs.append(bg)
    for i, (t, sub) in enumerate(D.STEPS):
        y = ys[i]
        r = group(sh)
        oval(r.shapes, 4.84, y + 0.38, 0.24, fill=NEUTRAL)
        text(r.shapes, 4.60, y + 0.14, 0.48, 0.48, str(i + 1), size=14, bold=True, color=INK60,
             align="c", anchor="m")
        text(r.shapes, 5.55, y + 0.04, 7.0, 0.34, t, size=18, bold=True, anchor="m")
        text(r.shapes, 5.55, y + 0.40, 7.0, 0.28, sub, size=13, color=INK60, anchor="t")
        rows.append(r)
    if mode != "static":
        for i, y in enumerate(ys):
            d = group(sh)
            oval(d.shapes, 4.84, y + 0.38, 0.24, fill=BLUE)
            text(d.shapes, 4.60, y + 0.14, 0.48, 0.48, str(i + 1), size=14, bold=True,
                 color=WHITE, align="c", anchor="m")
            dots.append(d)
    if mode == "static":
        _screen_group(sh, 1)
        return None
    screens = [_screen_group(sh, k) for k in range(5)]
    an.add([[fx(frame), fx(screens[0])] + [fx(r) for r in rows] + [fx(bgs[0]), fx(dots[0])]],
           auto=True)
    for k in range(1, 5):
        an.add([[fx(screens[k]), fx(screens[k - 1], "fadeout"), fx(bgs[k]), fx(dots[k]),
                 fx(bgs[k - 1], "fadeout"), fx(dots[k - 1], "fadeout")]])
    return an
