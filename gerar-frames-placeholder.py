"""
Generates a PLACEHOLDER hero frame sequence: an ocean-view interior that
transforms from hazy / cold / neglected to clear / golden / immaculate.

This exists so the scroll mechanism is real and testable today.
Replace public/frames/ with the ffmpeg-extracted frames from the AI video
and update public/frames/manifest.json -> the site picks it up automatically.
"""
import json
import math
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 960, 540
N = 150
OUT = os.path.join(os.path.dirname(__file__), "public", "frames")
os.makedirs(OUT, exist_ok=True)

rng = np.random.default_rng(7)

# Fixed dust/particle field, so particles stay put across frames (locked camera)
P = 420
px = rng.uniform(0, W, P)
py = rng.uniform(0, H, P)
psz = rng.uniform(0.6, 2.4, P)
pph = rng.uniform(0, math.tau, P)

# Window geometry
WIN = (78, 62, 700, 452)  # left, top, right, bottom
MULLION_X = (WIN[0] + WIN[2]) // 2


def lerp(a, b, t):
    return a + (b - a) * t


def mix(c1, c2, t):
    return tuple(lerp(c1[i], c2[i], t) for i in range(3))


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / max(e1 - e0, 1e-6), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def build_sea(t, clarity_map):
    """Sky + sea seen through the window. clarity_map: (h,w) in [0,1]."""
    ww, wh = WIN[2] - WIN[0], WIN[3] - WIN[1]
    horizon = int(wh * 0.46)

    yy = np.arange(wh)[:, None].astype(np.float32)
    xx = np.arange(ww)[None, :].astype(np.float32)

    # --- sky ---
    sky_top_c = mix((116, 124, 132), (58, 96, 152), t)
    sky_top_w = mix((150, 148, 140), (74, 136, 196), t)
    sky_hz_c = mix((168, 172, 176), (150, 190, 226), t)
    sky_hz_w = mix((186, 180, 168), (198, 226, 244), t)

    warm = smoothstep(0.45, 1.0, t)
    sky_top = mix(sky_top_c, sky_top_w, warm)
    sky_hz = mix(sky_hz_c, sky_hz_w, warm)

    g = np.clip(yy / max(horizon, 1), 0, 1) ** 0.85
    sky = np.zeros((wh, ww, 3), np.float32)
    for i in range(3):
        sky[:, :, i] = lerp(sky_top[i], sky_hz[i], g[:, 0])[:, None]

    # sun: rises into view then settles toward the horizon, glow grows
    sun_t = smoothstep(0.30, 1.0, t)
    if sun_t > 0.01:
        sx = ww * 0.62
        sy = lerp(-horizon * 0.5, horizon * 0.72, sun_t)
        d = np.sqrt((xx - sx) ** 2 + ((yy - sy) * 1.15) ** 2)
        glow = np.exp(-(d / (68 + 62 * sun_t)) ** 2) * (0.18 + 0.30 * sun_t)
        core = np.exp(-(d / (13 + 9 * sun_t)) ** 2) * (0.42 * sun_t)
        add = np.clip(glow + core, 0, 1)[:, :, None]
        sun_c = np.array(mix((250, 250, 246), (246, 250, 254), sun_t), np.float32)
        sky = sky * (1 - add) + sun_c * add

    # --- sea ---
    sea_far_c = mix((122, 132, 140), (58, 146, 176), t)
    sea_near_c = mix((88, 96, 104), (18, 82, 124), t)
    sea = np.zeros((wh, ww, 3), np.float32)
    depth = np.clip((yy - horizon) / max(wh - horizon, 1), 0, 1)
    for i in range(3):
        sea[:, :, i] = lerp(sea_far_c[i], sea_near_c[i], depth[:, 0])[:, None]

    # wave banding — more defined as the water clarifies
    band = (np.sin(yy * 0.55 + np.sin(xx * 0.018) * 2.1) * 0.5 + 0.5) ** 2
    band = band * (5 + 16 * t)
    sea += band[:, :, None] * np.array([1.0, 1.02, 1.06], np.float32)

    # golden reflection path toward the horizon
    if sun_t > 0.01:
        sx = ww * 0.62
        spread = 14 + (yy - horizon) * 0.42
        path = np.exp(-((xx - sx) / np.maximum(spread, 1)) ** 2)
        flick = (np.sin(yy * 1.7 + np.cos(xx * 0.05) * 3.0) * 0.5 + 0.5) ** 1.6
        pv = np.clip(path * flick * sun_t * 0.62, 0, 1)[:, :, None]
        gold = np.array([228, 244, 250], np.float32)
        sea = sea * (1 - pv) + gold * pv

    out = np.where((yy >= horizon)[:, :, None], sea, sky)

    # --- salt haze, removed by the sweeping clean edge ---
    haze_amt = clarity_map  # 1 = still dirty, 0 = clean
    haze_col = np.array(mix((196, 198, 196), (206, 208, 204), warm), np.float32)
    a = (haze_amt * 0.62)[:, :, None]
    out = out * (1 - a) + haze_col * a

    # dirty glass loses contrast and saturation too
    des = (haze_amt * 0.55)[:, :, None]
    grey = out.mean(axis=2, keepdims=True)
    out = out * (1 - des) + grey * des

    return np.clip(out, 0, 255)


def clarity(t):
    """(h,w) map. 1 = hazy, 0 = clean. A vertical edge sweeps left -> right."""
    ww, wh = WIN[2] - WIN[0], WIN[3] - WIN[1]
    xx = np.arange(ww)[None, :].astype(np.float32)
    # sweep happens between t=.32 and t=.66 — frame 4 of the storyboard
    s = smoothstep(0.32, 0.66, t)
    edge = -60 + s * (ww + 120)
    m = smoothstep(edge - 26, edge + 26, xx)
    m = np.repeat(m, wh, axis=0)
    # after the sweep, a last bit of residual haze fades out completely
    resid = (1.0 - smoothstep(0.66, 0.80, t)) * 0.18
    return np.clip(m + resid * (1 - m), 0, 1)


def frame(i):
    t = i / (N - 1)
    warm = smoothstep(0.45, 1.0, t)

    # --- interior shell ---
    wall = mix((40, 43, 48), (26, 48, 78), warm)
    wall_lo = mix((22, 24, 27), (12, 26, 46), warm)
    img = Image.new("RGB", (W, H), tuple(int(v) for v in wall))
    d = ImageDraw.Draw(img)
    for y in range(H):
        k = (y / H) ** 1.3
        d.line([(0, y), (W, y)], fill=tuple(int(v) for v in mix(wall, wall_lo, k)))

    # --- window ---
    sea = build_sea(t, clarity(t))
    img.paste(Image.fromarray(sea.astype(np.uint8)), (WIN[0], WIN[1]))

    # frame + mullion
    fr = mix((26, 28, 32), (16, 34, 58), warm)
    d.rectangle(WIN, outline=tuple(int(v) for v in fr), width=7)
    d.line([(MULLION_X, WIN[1]), (MULLION_X, WIN[3])],
           fill=tuple(int(v) for v in fr), width=5)

    # --- floor + light spill ---
    fy = int(H * 0.80)
    floor_c = mix((28, 30, 33), (20, 40, 64), warm)
    d.rectangle([0, fy, W, H], fill=tuple(int(v) for v in floor_c))

    spill = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(spill)
    reach = lerp(0.10, 0.72, smoothstep(0.10, 0.95, t))
    inten = int(lerp(26, 122, smoothstep(0.05, 1.0, t)))
    sd.polygon(
        [(WIN[0], fy), (WIN[2], fy),
         (WIN[2] + W * reach * 0.5, H), (WIN[0] - W * reach * 0.18, H)],
        fill=inten,
    )
    spill = spill.filter(ImageFilter.GaussianBlur(26))
    spill_c = Image.new("RGB", (W, H), tuple(int(v) for v in mix((150, 158, 168), (208, 230, 246), warm)))
    img = Image.composite(spill_c, img, spill.point(lambda v: int(v * 0.85)))

    # polished floor sheen — grows as surfaces get clean
    sheen = Image.new("L", (W, H), 0)
    shd = ImageDraw.Draw(sheen)
    gl = smoothstep(0.40, 1.0, t)
    if gl > 0.01:
        shd.polygon(
            [(WIN[0] + 30, fy), (WIN[2] - 30, fy), (WIN[2] + 60, H), (WIN[0] - 60, H)],
            fill=int(120 * gl),
        )
        sheen = sheen.filter(ImageFilter.GaussianBlur(30))
        img = Image.composite(
            Image.new("RGB", (W, H), tuple(int(v) for v in mix((170, 180, 190), (198, 224, 242), warm))),
            img, sheen,
        )

    # --- clutter that clears away (kept abstract: soft dark masses) ---
    cl = 1.0 - smoothstep(0.08, 0.42, t)
    if cl > 0.02:
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        blobs = [(742, 372, 906, 452), (700, 468, 830, 512), (560, 486, 668, 524)]
        for b in blobs:
            od.ellipse(b, fill=(18, 18, 20, int(220 * cl)))
        ov = ov.filter(ImageFilter.GaussianBlur(9))
        img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

    # --- suspended particles: many at the start, gone at the end ---
    pa = 1.0 - smoothstep(0.20, 0.72, t)
    if pa > 0.02:
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        drift = t * 26
        for k in range(P):
            x = px[k] + math.sin(pph[k] + t * 3.1) * 5
            y = (py[k] + drift + math.cos(pph[k] + t * 2.2) * 4) % H
            if not (WIN[0] < x < WIN[2] and WIN[1] < y < WIN[3]):
                continue
            r = psz[k]
            a = int(150 * pa * (0.4 + 0.6 * (math.sin(pph[k] + t * 5) * 0.5 + 0.5)))
            od.ellipse([x - r, y - r, x + r, y + r], fill=(255, 250, 236, a))
        img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

    # --- global grade: cold + flat  ->  warm + contrasty ---
    a = np.asarray(img, np.float32)
    con = lerp(0.86, 1.16, smoothstep(0.15, 1.0, t))
    a = (a - 128) * con + 128
    tint = np.array([
        lerp(0.98, 0.985, warm),
        lerp(0.99, 0.995, warm),
        lerp(1.05, 1.035, warm),
    ], np.float32)
    a *= tint
    sat = lerp(0.82, 1.06, smoothstep(0.15, 1.0, t))
    g = a.mean(axis=2, keepdims=True)
    a = g + (a - g) * sat
    a = np.clip(a, 0, 255)

    # vignette
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    dx = (xx - W / 2) / (W / 2)
    dy = (yy - H / 2) / (H / 2)
    v = 1.0 - 0.30 * np.clip(dx * dx + dy * dy, 0, 1.6)
    a *= v[:, :, None]

    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


for i in range(N):
    frame(i).save(os.path.join(OUT, "frame_%04d.jpg" % (i + 1)), quality=82, optimize=True)

with open(os.path.join(OUT, "manifest.json"), "w") as f:
    json.dump({"total": N, "pattern": "frames/frame_%04d.jpg", "placeholder": True}, f)

print("wrote %d frames" % N)
