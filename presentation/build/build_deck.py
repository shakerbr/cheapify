#!/usr/bin/env python3
"""Rebuild the Cheapify GIZ pitch deck.

    python build/build_deck.py            # animated PPTX + static PDF + speaker script
    python build/build_deck.py --static   # only the static (no animation) PPTX
    python build/build_deck.py --qa-states  # also render intermediate-state slides

Run with the venv that has python-pptx 1.0.2 (see presentation/README notes in the script header
of the build log): /tmp/cheapify-deck-venv/bin/python
"""
import argparse
import copy
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pptx import Presentation  # noqa: E402
from pptx.opc.constants import RELATIONSHIP_TYPE as RT  # noqa: E402
from pptx.oxml.ns import qn  # noqa: E402

import assets  # noqa: E402
import deck_data as D  # noqa: E402
import slides_a  # noqa: E402
import slides_b  # noqa: E402
from deckkit import content_frame, finalize_slide, footnote  # noqa: E402

ROOT = HERE.parents[1]
PRES = ROOT / "presentation"
TEMPLATE = ROOT / "archive/program-giz-cheapify/Presentation-stuff/Modified template.pptx"
OUT_PPTX = PRES / "Cheapify-GIZ-Pitch.pptx"
OUT_PDF = PRES / "Cheapify-GIZ-Pitch.pdf"
OUT_SCRIPT = PRES / "speaker-script.md"
WPM = 140

MAIN = ["cover", "problem", "evidence", "solution", "value", "market", "product", "model",
        "competitors", "growth", "finance", "funding", "next", "thanks"]
APPX = ["A1", "A2", "A3", "A4", "A5", "A6", "A7"]


class Ctx:
    def __init__(self, static):
        self.static = static


def snapshot_header(slide):
    out = []
    for pic in slide.shapes._spTree.findall(qn("p:pic")):
        rid = pic.find(".//" + qn("a:blip")).get(qn("r:embed"))
        out.append((copy.deepcopy(pic), slide.part.related_part(rid)))
    return out


def add_header(slide, header):
    for pic, part in header:
        new = copy.deepcopy(pic)
        rid = slide.part.relate_to(part, RT.IMAGE)
        new.find(".//" + qn("a:blip")).set(qn("r:embed"), rid)
        slide.shapes._spTree.append(new)


def set_notes(slide, seconds, body):
    tf = slide.notes_slide.notes_text_frame
    tf.text = f"Time: ~{seconds}s\n{body}"


def build(static=False, qa_states=False, out=OUT_PPTX):
    meta = assets.build_all()
    slides_a.ASSETS = assets.OUT
    prs = Presentation(str(TEMPLATE))
    s_cover, s_content, s_thanks = list(prs.slides)
    layout = s_content.slide_layout
    header = snapshot_header(s_content)
    ctx = Ctx(static)
    order = {}
    anims = {}

    def content(key, reuse=None, label=None, headline=None, foot=None):
        if key in D.SLIDES:
            d = D.SLIDES[key]
            label, headline, foot = d["label"], d["headline"], d.get("footnote")
        sl = reuse if reuse is not None else prs.slides.add_slide(layout)
        if reuse is None:
            add_header(sl, header)
        content_frame(sl, label, headline)
        if foot:
            footnote(sl, foot)
        return sl

    # main deck
    order["cover"] = s_cover
    anims["cover"] = slides_a.cover(s_cover, ctx)
    order["problem"] = content("problem", reuse=s_content)
    anims["problem"] = slides_a.problem(order["problem"], ctx)
    for key, fn in (("evidence", slides_a.evidence), ("solution", None), ("value", slides_a.value),
                    ("market", slides_a.market), ("product", None), ("model", None),
                    ("competitors", slides_b.competitors), ("growth", slides_b.growth),
                    ("finance", slides_b.finance), ("funding", slides_b.funding),
                    ("next", slides_b.next_steps)):
        sl = content(key)
        order[key] = sl
        if key == "solution":
            anims[key] = slides_a.solution(sl, ctx, "static" if static else "anim")
        elif key == "product":
            anims[key] = slides_a.product(sl, ctx, "static" if static else "anim")
        elif key == "model":
            anims[key] = slides_b.model(sl, ctx, "static" if static else "anim")
        else:
            anims[key] = fn(sl, ctx)
    order["thanks"] = s_thanks
    anims["thanks"] = slides_b.thanks(s_thanks, ctx)

    # appendix
    for k in APPX:
        sl = content(k, label="Appendix", headline=D.APPENDIX[k]["headline"])
        order[k] = sl
        anims[k] = slides_b.appendix(sl, k, ctx)

    # QA-only intermediate states
    extra = []
    if qa_states:
        sl = content("qa4", label="QA state", headline="Solution — chaos state")
        slides_a.solution(sl, ctx, "chaos")
        extra.append(sl)
        for k in range(5):
            sl = content(f"qa7_{k}", label="QA state", headline=f"Product — screen {k + 1}")
            slides_a.product(sl, ctx, "state", k)
            extra.append(sl)
        sl = content("qa8", label="QA state", headline="Business model — bar only")
        slides_b.model(sl, ctx, "bar")
        extra.append(sl)

    # notes, transitions, animations
    for key in MAIN:
        set_notes(order[key], D.SLIDES[key]["seconds"], D.SLIDES[key]["notes"])
    for k in APPX:
        order[k].notes_slide.notes_text_frame.text = D.APPENDIX_NOTE
    for key, sl in order.items():
        finalize_slide(sl, None if static else anims.get(key))
    for sl in extra:
        finalize_slide(sl, None)

    # slide order
    seq = [order[k] for k in MAIN + APPX] + extra
    lst = prs.slides._sldIdLst
    by_part = {}
    for sldId in list(lst):
        by_part[prs.part.related_part(sldId.rId)] = sldId
    for sldId in list(lst):
        lst.remove(sldId)
    for sl in seq:
        lst.append(by_part[sl.part])
    prs.save(str(out))
    return out


def convert_pdf(pptx_path, outdir):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(outdir),
                    str(pptx_path)], check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, timeout=600)
    return Path(outdir) / (Path(pptx_path).stem + ".pdf")


def words(txt):
    return len(re.sub(r"\[click\]", " ", txt).split())


def write_script():
    rows = []
    tot_t = tot_w = 0
    for i, key in enumerate(MAIN, 1):
        d = D.SLIDES[key]
        sect = d.get("label") or {"cover": "Cover", "thanks": "Thank you"}[key]
        w = words(d["notes"])
        est = round(w / WPM * 60)
        rows.append((i, sect, d["seconds"], w, est))
        tot_t += d["seconds"]
        tot_w += w
    lines = ["# Cheapify — Final Pitch Speaker Script", "",
             "Hard limit: under 6 minutes. `[click]` marks an animation click; the first animation "
             "of each slide plays automatically when the slide appears.", "",
             "## Timing", "",
             "| Slide | Section | Target (s) | Words | Est. at 140 wpm (s) |",
             "| :--- | :--- | :--- | :--- | :--- |"]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
    lines.append(f"| | **Total** | **{tot_t}** | **{tot_w}** | **{round(tot_w / WPM * 60)}** |")
    lines += ["", f"Target total: {tot_t // 60} min {tot_t % 60} s. Estimated at 140 words per "
                  f"minute: {round(tot_w / WPM * 60)} s.", "", "## Script", ""]
    for i, key in enumerate(MAIN, 1):
        d = D.SLIDES[key]
        sect = d.get("label") or {"cover": "Cover", "thanks": "Thank you"}[key]
        lines += [f"### Slide {i} — {sect}", "", f"*Time: ~{d['seconds']}s*", "", d["notes"], ""]
    OUT_SCRIPT.write_text("\n".join(lines).rstrip() + "\n")
    return rows, tot_t, tot_w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--static", action="store_true", help="build only the static PPTX")
    ap.add_argument("--qa-states", action="store_true")
    ap.add_argument("--qa-dir", default="/tmp/cheapify-deck-qa")
    a = ap.parse_args()
    qa = Path(a.qa_dir)
    qa.mkdir(parents=True, exist_ok=True)
    if a.static:
        out = qa / ("Cheapify-GIZ-Pitch-qastates.pptx" if a.qa_states else "Cheapify-GIZ-Pitch-static.pptx")
        build(static=True, qa_states=a.qa_states, out=out)
        print(out)
        return
    build(static=False, out=OUT_PPTX)
    st = qa / "Cheapify-GIZ-Pitch-static.pptx"
    build(static=True, qa_states=a.qa_states, out=st)
    pdf = convert_pdf(st, qa)
    shutil.copy(pdf, OUT_PDF)
    rows, tt, tw = write_script()
    print(OUT_PPTX, OUT_PDF, OUT_SCRIPT, f"target={tt}s words={tw}")


if __name__ == "__main__":
    main()
