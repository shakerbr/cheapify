"""Drawing helpers + animation XML engine (python-pptx / lxml)."""
import copy
from lxml import etree
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt
from PIL import Image

from assets import icon_path

EMU = 914400

INK = "101820"
INK60 = "5A6672"
INK35 = "A9B1B9"
BLUE = "298FC2"
BLUE12 = "E5F2F8"
BLUE50 = "94C7E0"
GREEN = "228848"
GREEN8 = "EDF5F0"
RED = "D22730"
ORANGE = "FFA300"
NEUTRAL = "DDE5ED"
SURFACE = "F4F6F8"
WHITE = "FFFFFF"

ALIGN = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}
ANCHOR = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"


def E(v):
    return Emu(int(round(v * EMU)))


def rgb(hexstr):
    return RGBColor.from_string(hexstr)


# ---------------------------------------------------------------- shadows
SHADOWS = {
    "elev1": (8, 2, 9000),
    "elev2": (24, 8, 8000),
}


def no_effect(shape):
    spPr = shape._element.spPr
    for old in spPr.findall(qn("a:effectLst")):
        spPr.remove(old)
    etree.SubElement(spPr, qn("a:effectLst"))
    _drop_style(shape)


def _drop_style(shape):
    st = shape._element.find(qn("p:style"))
    if st is not None:
        shape._element.remove(st)


def add_shadow(shape, kind="elev1"):
    blur, dist, alpha = SHADOWS[kind]
    spPr = shape._element.spPr
    eff = etree.SubElement(spPr, qn("a:effectLst"))
    _drop_style(shape)
    sh = etree.SubElement(eff, qn("a:outerShdw"), blurRad=str(blur * 12700),
                          dist=str(dist * 12700), dir="5400000", algn="t", rotWithShape="0")
    clr = etree.SubElement(sh, qn("a:srgbClr"), val=INK)
    etree.SubElement(clr, qn("a:alpha"), val=str(alpha))


# ---------------------------------------------------------------- shapes
def rect(parent, x, y, w, h, fill=None, line=None, lw=1.0, radius=None, shadow=None,
         shape=None, name=None, dash=None):
    if shape is None:
        shape = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    sp = parent.add_shape(shape, E(x), E(y), E(w), E(h))
    if radius and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sp.adjustments[0] = min(0.5, radius / min(w, h))
    if fill:
        sp.fill.solid()
        sp.fill.fore_color.rgb = rgb(fill)
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line)
        sp.line.width = Pt(lw)
        if dash:
            sp.line.dash_style = dash
    else:
        sp.line.fill.background()
    if shadow:
        add_shadow(sp, shadow)
    else:
        no_effect(sp)
    if name:
        sp.name = name
    return sp


def oval(parent, cx, cy, r, fill=None, line=None, lw=1.0, name=None):
    return rect(parent, cx - r, cy - r, 2 * r, 2 * r, fill=fill, line=line, lw=lw,
                shape=MSO_SHAPE.OVAL, name=name)


def card(parent, x, y, w, h, shadow="elev1", fill=WHITE, line=NEUTRAL, radius=0.14):
    return rect(parent, x, y, w, h, fill=fill, line=line, lw=1.0, radius=radius, shadow=shadow)


def line(parent, x1, y1, x2, y2, color=INK35, lw=1.0, dash=None):
    c = parent.add_connector(MSO_CONNECTOR.STRAIGHT, E(x1), E(y1), E(x2), E(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(lw)
    if dash:
        c.line.dash_style = dash
    no_effect(c)
    return c


def group(parent):
    return parent.add_group_shape()


def _set_font(rPr, face, rtl=False):
    for tag in ("a:latin", "a:ea", "a:cs", "a:sym"):
        for old in rPr.findall(qn(tag)):
            rPr.remove(old)
    for tag in ("a:latin", "a:cs"):
        etree.SubElement(rPr, qn(tag), typeface=face)


def text(parent, x, y, w, h, paras, size=12, color=INK, bold=False, font="Inter",
         align="l", anchor="t", rtl=False, wrap=True, spacing=None, name=None):
    """paras: str | [para]; para: str | [run]; run: str | (str, {overrides})."""
    tb = parent.add_textbox(E(x), E(y), E(w), E(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = ANCHOR[anchor]
    bodyPr = tf._txBody.find(qn("a:bodyPr"))
    for ch in list(bodyPr):
        bodyPr.remove(ch)
    etree.SubElement(bodyPr, qn("a:noAutofit"))
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = ALIGN[align]
        if spacing:
            p.line_spacing = spacing
        if rtl:
            p._p.get_or_add_pPr().set("rtl", "1")
        runs = [para] if isinstance(para, (str, tuple)) else para
        for run in runs:
            if isinstance(run, str):
                t, o = run, {}
            else:
                t, o = run
            r = p.add_run()
            r.text = t
            f = r.font
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.color.rgb = rgb(o.get("color", color))
            rPr = r._r.get_or_add_rPr()
            fnt = o.get("font", font)
            rPr.set("lang", "ar-IQ" if rtl else "en-US")
            _set_font(rPr, fnt, rtl)
    return tb


def pic_contain(parent, path, x, y, w, h, align="c"):
    im = Image.open(path)
    iw, ih = im.size
    s = min(w / iw, h / ih)
    pw, ph = iw * s, ih * s
    px = x + (w - pw) / 2
    py = y + (h - ph) / 2
    pic = parent.add_picture(str(path), E(px), E(py), E(pw), E(ph))
    return pic, (px, py, s)


def pic_box(parent, path, x, y, w, h):
    return parent.add_picture(str(path), E(x), E(y), E(w), E(h))


def icon(parent, name, color, x, y, s):
    return parent.add_picture(str(icon_path(name, color)), E(x), E(y), E(s), E(s))


def icon_c(parent, name, color, cx, cy, s):
    return icon(parent, name, color, cx - s / 2, cy - s / 2, s)


def ring(parent, pic_geom, src_box, pad=6, color=RED, lw=2.25):
    px, py, s = pic_geom
    x0, y0, x1, y1 = src_box
    return rect(parent, px + (x0 - pad) * s, py + (y0 - pad) * s,
                (x1 - x0 + 2 * pad) * s, (y1 - y0 + 2 * pad) * s,
                line=color, lw=lw, radius=0.06)


# ---------------------------------------------------------------- template bits
def clone_header(src_slide, dst_slide):
    """Copy the two header-logo pictures (same image parts) from src to dst."""
    for pic in src_slide.shapes._spTree.findall(qn("p:pic")):
        new = copy.deepcopy(pic)
        blip = new.find(".//" + qn("a:blip"))
        rid = blip.get(qn("r:embed"))
        img_part = src_slide.part.related_part(rid)
        new_rid = dst_slide.part.relate_to(img_part, RT.IMAGE)
        blip.set(qn("r:embed"), new_rid)
        dst_slide.shapes._spTree.append(new)


def content_frame(slide, label, headline):
    rect(slide.shapes, 0.79, 1.66, 0.30, 0.05, fill=BLUE)
    text(slide.shapes, 1.24, 1.56, 6.0, 0.28, label, size=13, color=INK60, anchor="m")
    text(slide.shapes, 0.79, 1.86, 11.75, 0.62, headline, size=30, color=INK, bold=True,
         font="Comfortaa", anchor="m")


def footnote(slide, txt):
    text(slide.shapes, 0.79, 7.06, 11.75, 0.26, txt, size=9, color=INK60, anchor="m")


# ---------------------------------------------------------------- animation engine
class Fx:
    def __init__(self, shape, kind="fade", delay=0, dur=None):
        self.shape = shape
        self.kind = kind
        self.delay = delay
        self.dur = dur if dur is not None else {"fade": 450, "zoom": 400, "appear": 1,
                                                  "fadeout": 450}[kind]


def fx(shape, kind="fade", delay=0, dur=None):
    return Fx(shape, kind, delay, dur)


def stagger(shapes, kind="fade", delay=150, first_delay=None):
    out = []
    for i, s in enumerate(shapes):
        d = delay if (i or first_delay is None) else first_delay
        out.append([fx(s, kind, d)])
    return out


def together(*effects):
    return [list(effects)]


class Anim:
    """Collects click groups; group = list of steps; step = list[Fx]."""

    def __init__(self):
        self.groups = []

    def add(self, steps, auto=False):
        if steps and isinstance(steps[0], Fx):
            steps = [steps]
        self.groups.append((auto, [s for s in steps if s]))

    def build(self, slide):
        if not self.groups:
            return
        nid = [2]

        def nxt():
            nid[0] += 1
            return nid[0]

        used = {}
        bld = []
        P = "{%s}" % NS_P
        timing = etree.Element(P + "timing")
        tnLst = etree.SubElement(timing, P + "tnLst")
        par0 = etree.SubElement(tnLst, P + "par")
        root = etree.SubElement(par0, P + "cTn", id="1", dur="indefinite", restart="never",
                                nodeType="tmRoot")
        rc = etree.SubElement(root, P + "childTnLst")
        seq = etree.SubElement(rc, P + "seq", concurrent="1", nextAc="seek")
        main = etree.SubElement(seq, P + "cTn", id="2", dur="indefinite", nodeType="mainSeq")
        mc = etree.SubElement(main, P + "childTnLst")
        prev = etree.SubElement(seq, P + "prevCondLst")
        c = etree.SubElement(prev, P + "cond", evt="onPrev", delay="0")
        etree.SubElement(etree.SubElement(c, P + "tgtEl"), P + "sldTgt")
        nxtl = etree.SubElement(seq, P + "nextCondLst")
        c = etree.SubElement(nxtl, P + "cond", evt="onNext", delay="0")
        etree.SubElement(etree.SubElement(c, P + "tgtEl"), P + "sldTgt")

        for auto, steps in self.groups:
            gpar = etree.SubElement(mc, P + "par")
            gct = etree.SubElement(gpar, P + "cTn", id=str(nxt()), fill="hold")
            st = etree.SubElement(gct, P + "stCondLst")
            etree.SubElement(st, P + "cond", delay="indefinite")
            if auto:
                etree.SubElement(st, P + "cond", evt="onBegin", delay="0").append(
                    etree.Element(P + "tn", val="2"))
            gcl = etree.SubElement(gct, P + "childTnLst")
            start = 0
            for si, step in enumerate(steps):
                spar = etree.SubElement(gcl, P + "par")
                sct = etree.SubElement(spar, P + "cTn", id=str(nxt()), fill="hold")
                sst = etree.SubElement(sct, P + "stCondLst")
                etree.SubElement(sst, P + "cond", delay=str(start))
                scl = etree.SubElement(sct, P + "childTnLst")
                for ei, e in enumerate(step):
                    if ei == 0:
                        node = "clickEffect" if (si == 0 and not auto) else "afterEffect"
                    else:
                        node = "withEffect"
                    spid = e.shape.shape_id
                    grp = used.get(spid, 0)
                    used[spid] = grp + 1
                    if e.shape._element.tag == qn("p:sp"):
                        bld.append((spid, grp))
                    self._effect(scl, e, node, grp, nxt)
                start += max(x.delay + x.dur for x in step)

        if bld:
            bl = etree.SubElement(timing, P + "bldLst")
            for spid, grp in bld:
                etree.SubElement(bl, P + "bldP", spid=str(spid), grpId=str(grp), animBg="1")

        cSld_parent = slide._element
        for old in cSld_parent.findall(qn("p:timing")):
            cSld_parent.remove(old)
        cSld_parent.append(timing)

    @staticmethod
    def _effect(parent, e, node, grp, nxt):
        P = "{%s}" % NS_P
        exit_ = e.kind == "fadeout"
        preset = {"fade": ("10", "0"), "zoom": ("53", "16"), "appear": ("1", "0"),
                  "fadeout": ("10", "0")}[e.kind]
        par = etree.SubElement(parent, P + "par")
        ct = etree.SubElement(par, P + "cTn", id=str(nxt()), presetID=preset[0],
                              presetClass="exit" if exit_ else "entr",
                              presetSubtype=preset[1], fill="hold", grpId=str(grp),
                              nodeType=node)
        st = etree.SubElement(ct, P + "stCondLst")
        etree.SubElement(st, P + "cond", delay=str(e.delay))
        cl = etree.SubElement(ct, P + "childTnLst")
        spid = str(e.shape.shape_id)

        def tgt(bhvr):
            etree.SubElement(etree.SubElement(bhvr, P + "tgtEl"), P + "spTgt", spid=spid)

        def set_vis(val, delay="0"):
            s = etree.SubElement(cl, P + "set")
            b = etree.SubElement(s, P + "cBhvr")
            c2 = etree.SubElement(b, P + "cTn", id=str(nxt()), dur="1", fill="hold")
            etree.SubElement(etree.SubElement(c2, P + "stCondLst"), P + "cond", delay=delay)
            tgt(b)
            an = etree.SubElement(b, P + "attrNameLst")
            etree.SubElement(an, P + "attrName").text = "style.visibility"
            to = etree.SubElement(s, P + "to")
            etree.SubElement(to, P + "strVal", val=val)

        def fade(trans):
            a = etree.SubElement(cl, P + "animEffect", transition=trans, filter="fade")
            b = etree.SubElement(a, P + "cBhvr")
            etree.SubElement(b, P + "cTn", id=str(nxt()), dur=str(e.dur))
            tgt(b)

        if e.kind == "appear":
            set_vis("visible")
        elif e.kind == "fade":
            set_vis("visible")
            fade("in")
        elif e.kind == "zoom":
            set_vis("visible")
            for attr in ("ppt_w", "ppt_h"):
                a = etree.SubElement(cl, P + "anim", calcmode="lin", valueType="num")
                b = etree.SubElement(a, P + "cBhvr")
                etree.SubElement(b, P + "cTn", id=str(nxt()), dur=str(e.dur), fill="hold")
                tgt(b)
                an = etree.SubElement(b, P + "attrNameLst")
                etree.SubElement(an, P + "attrName").text = attr
                tl = etree.SubElement(a, P + "tavLst")
                t0 = etree.SubElement(tl, P + "tav", tm="0")
                etree.SubElement(etree.SubElement(t0, P + "val"), P + "fltVal", val="0")
                t1 = etree.SubElement(tl, P + "tav", tm="100000")
                etree.SubElement(etree.SubElement(t1, P + "val"), P + "strVal", val="#" + attr)
            fade("in")
        elif e.kind == "fadeout":
            fade("out")
            set_vis("hidden", delay=str(e.dur - 1))


def finalize_slide(slide, anim=None, transition=True):
    root = slide._element
    for old in root.findall(qn("p:transition")):
        root.remove(old)
    if transition:
        P = "{%s}" % NS_P
        tr = etree.Element(P + "transition", spd="fast")
        etree.SubElement(tr, P + "fade")
        clr = root.find(qn("p:clrMapOvr"))
        clr.addnext(tr)
    if anim is not None:
        anim.build(slide)
