"""Asset pipeline: evidence crops/blurs, logo, recolored Lucide icons."""
import io
import json
import re
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
EVID = ROOT / "entrepreneurship" / "assets" / "evidence"
OUT = ROOT / "presentation" / "assets"
ICON_SVG = OUT / "icons" / "svg"
ICON_OUT = OUT / "icons"
BLUR_RADIUS = 14
DARK_BG = (26, 27, 30)
SURFACE_BG = (244, 246, 249)


def _round_corners(im, radius=48, bg=SURFACE_BG):
    """Apply smooth 4x-supersampled rounded corners onto `bg` (no added border)."""
    w, h = im.size
    scale = 4
    mask = Image.new("L", (w * scale, h * scale), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, w * scale - 1, h * scale - 1), radius=radius * scale, fill=255
    )
    mask = mask.resize((w, h), Image.LANCZOS)
    out = Image.new("RGB", (w, h), bg)
    out.paste(im, (0, 0), mask)
    return out


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
    im = _round_corners(im, radius=44)
    im.save(OUT / "ev-miswag-anker.jpg", quality=94)
    meta["ev-miswag-anker"] = {
        "size": im.size,
        "rings": [_rel((38, 1910, 232, 1956), crop), _rel((560, 1910, 757, 1956), crop)],
    }

    crop = (0, 288, 1080, 1818)
    im = _crop_blur("xiaomi-power-bank/Screenshot_20260920_130923.jpg", crop, [])
    im = _round_corners(im, radius=64)
    im.save(OUT / "ev-ibazzar-xiaomi.jpg", quality=94)
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
    ad_im = _round_corners(full.crop(ad), radius=28, bg=DARK_BG)
    com_im = full.crop(com)
    top_pad, gap, bot_pad = 18, 20, 10
    W = max(ad_im.width, com_im.width)
    comp = Image.new("RGB", (W, top_pad + ad_im.height + gap + com_im.height + bot_pad), DARK_BG)
    ad_off = ((W - ad_im.width) // 2, top_pad)
    com_off = ((W - com_im.width) // 2, top_pad + ad_im.height + gap)
    comp.paste(ad_im, ad_off)
    comp.paste(com_im, com_off)
    comp = _round_corners(comp, radius=48)
    comp.save(OUT / "ev-instagram-noprice.jpg", quality=94)
    meta["ev-instagram-noprice"] = {
        "size": comp.size,
        "rings": [_rel((158, 2062, 318, 2110), com, com_off)],
    }

    crop = (0, 1131, 1080, 1774)
    im = _crop_blur("Anker-Power-Bank/Screenshot_20261020_225624.jpg", crop, [])
    im = _round_corners(im, radius=44)
    im.save(OUT / "ev-ibazzar-foundcheaper.jpg", quality=94)
    meta["ev-ibazzar-foundcheaper"] = {
        "size": im.size,
        "rings": [_rel((34, 1488, 505, 1534), crop)],
    }

    crop = (236, 308, 772, 1052)
    im = Image.open(EVID / "Anker-Power-Bank/Screenshot_20261020_225624.jpg").convert("RGB").crop(crop)
    im = _round_corners(im, radius=32, bg=(255, 255, 255))
    im.save(OUT / "product-anker.png")


    ig = "vaccum-cleaner-vac3510/Screenshot_20261021_120338_Instagram.jpg"
    ms = "vaccum-cleaner-vac3510/Screenshot_20261021_120334_Miswag.jpg"
    ad = (0, 428, 1080, 1506)
    pr = (0, 260, 1080, 1896)
    left = Image.open(EVID / ig).convert("RGB").crop(ad)
    right = Image.open(EVID / ms).convert("RGB").crop(pr)
    H = left.height
    rw = round(right.width * H / right.height)
    right = right.resize((rw, H), Image.LANCZOS)
    left = _round_corners(left, radius=56)
    right = _round_corners(right, radius=56)
    gap = 40
    comp = Image.new("RGB", (left.width + gap + rw, H), SURFACE_BG)
    comp.paste(left, (0, 0))
    comp.paste(right, (left.width + gap, 0))
    comp.save(OUT / "ev-vacuum-fakedeal.jpg", quality=94)
    k = H / right.height * (right.height / (pr[3] - pr[1]))
    k = H / (pr[3] - pr[1])
    ox = left.width + gap
    meta["ev-vacuum-fakedeal"] = {
        "size": comp.size,
        "rings": [[776, 686 - ad[1], 976, 866 - ad[1]],
                  [round(ox + 24 * k), round((1706 - pr[1]) * k), round(ox + 1056 * k), round((1872 - pr[1]) * k)]],
    }

    (OUT / "ev-meta.json").write_text(json.dumps(meta, indent=1))
    return meta


def build_logo():
    cairosvg.svg2png(url=str(ROOT / "assets" / "cheapify-logo.svg"),
                     write_to=str(OUT / "cheapify-logo.png"), output_width=1400)


def footer_icon_paths(name):
    """Return (svg_path, png_path) for a footer SVG icon (`footer-facebook`, etc.), rendering 512px PNG."""
    svg_path = ICON_SVG / f"{name}.svg"
    png_path = ICON_OUT / f"{name}.png"
    if not png_path.exists() or svg_path.stat().st_mtime > png_path.stat().st_mtime:
        ICON_OUT.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path),
                         output_width=512, output_height=512)
    return svg_path, png_path


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
