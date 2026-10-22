"""Asset pipeline: evidence crops/blurs, logo, recolored Lucide icons."""
import io
import json
import re
from pathlib import Path

import cairosvg
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
EVID = ROOT / "entrepreneurship" / "assets" / "evidence"
OUT = ROOT / "presentation" / "assets"
ICON_SVG = OUT / "icons" / "svg"
ICON_OUT = OUT / "icons"
BLUR_RADIUS = 14
DARK_BG = (26, 27, 30)


def _blur(im, boxes):
    for x0, y0, x1, y1 in boxes:
        region = im.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(BLUR_RADIUS))
        im.paste(region, (x0, y0))
    return im


def _crop_blur(src, crop, blurs):
    im = Image.open(EVID / src).convert("RGB")
    im = _blur(im, blurs)
    return im.crop(crop)


def _rel(box, origin, off=(0, 0)):
    return [box[0] - origin[0] + off[0], box[1] - origin[1] + off[1],
            box[2] - origin[0] + off[0], box[3] - origin[1] + off[1]]


def build_evidence():
    meta = {}

    crop = (0, 1258, 1080, 2122)
    im = _crop_blur("Anker-Power-Bank/Screenshot_20261020_225824_Miswag.jpg", crop,
                    [(36, 2060, 308, 2125), (561, 2060, 756, 2125)])
    im.save(OUT / "ev-miswag-anker.jpg", quality=92)
    meta["ev-miswag-anker"] = {
        "size": im.size,
        "rings": [_rel((38, 1910, 232, 1956), crop), _rel((560, 1910, 757, 1956), crop)],
    }

    crop = (0, 288, 1080, 1818)
    im = _crop_blur("xiaomi-power-bank/Screenshot_20260920_130923.jpg", crop, [])
    im.save(OUT / "ev-ibazzar-xiaomi.jpg", quality=92)
    meta["ev-ibazzar-xiaomi"] = {
        "size": im.size,
        "rings": [_rel((567, 924, 775, 970), crop), _rel((48, 1700, 261, 1747), crop)],
    }

    src = "no-price-dm-for-price/Screenshot_20261021_122639_Instagram.jpg"
    ad = (57, 108, 1008, 920)
    com = (36, 2000, 1028, 2118)
    full = Image.open(EVID / src).convert("RGB")
    full = _blur(full, [(77, 134, 206, 257), (435, 868, 642, 922),
                        (40, 2022, 140, 2118), (168, 2018, 415, 2056)])
    ad_im = full.crop(ad)
    com_im = full.crop(com)
    gap = 24
    W = max(ad_im.width, com_im.width)
    comp = Image.new("RGB", (W, ad_im.height + gap + com_im.height), DARK_BG)
    ad_off = ((W - ad_im.width) // 2, 0)
    com_off = ((W - com_im.width) // 2, ad_im.height + gap)
    comp.paste(ad_im, ad_off)
    comp.paste(com_im, com_off)
    comp.save(OUT / "ev-instagram-noprice.jpg", quality=92)
    meta["ev-instagram-noprice"] = {
        "size": comp.size,
        "rings": [_rel((158, 2062, 318, 2110), com, com_off)],
    }

    crop = (0, 1131, 1080, 1774)
    im = _crop_blur("Anker-Power-Bank/Screenshot_20261020_225624.jpg", crop, [])
    im.save(OUT / "ev-ibazzar-foundcheaper.jpg", quality=92)
    meta["ev-ibazzar-foundcheaper"] = {
        "size": im.size,
        "rings": [_rel((34, 1488, 505, 1534), crop)],
    }

    crop = (236, 308, 772, 1052)
    im = Image.open(EVID / "Anker-Power-Bank/Screenshot_20261020_225624.jpg").convert("RGB").crop(crop)
    im.save(OUT / "product-anker.png")

    (OUT / "ev-meta.json").write_text(json.dumps(meta, indent=1))
    return meta


def build_logo():
    cairosvg.svg2png(url=str(ROOT / "assets" / "cheapify-logo.svg"),
                     write_to=str(OUT / "cheapify-logo.png"), output_width=1400)


def icon_path(name, color):
    """Lucide icon recolored to hex `color` (no #), 256 px PNG; cached."""
    color = color.lstrip("#").upper()
    out = ICON_OUT / f"{name}_{color}.png"
    if not out.exists():
        svg = (ICON_SVG / f"{name}.svg").read_text()
        svg = svg.replace("currentColor", f"#{color}")
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out),
                         output_width=256, output_height=256)
    return out


def build_all():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = build_evidence()
    build_logo()
    return meta


if __name__ == "__main__":
    build_all()
