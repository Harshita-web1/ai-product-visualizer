"""Locally generated placeholder imagery and inline icons.

No network requests: thumbnails are drawn with Pillow so the interface can be
previewed offline.
"""

import base64
from io import BytesIO

from PIL import Image, ImageDraw


def _hex_to_rgb(value: str):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def placeholder_image(tint: str = "#7C5CFF", size: int = 480) -> Image.Image:
    """A muted square stand-in for a product photo."""
    base = Image.new("RGB", (size, size), (17, 22, 29))
    draw = ImageDraw.Draw(base, "RGBA")
    r, g, b = _hex_to_rgb(tint)

    # soft corner glow
    for i in range(14, 0, -1):
        alpha = int(6 + i * 1.4)
        pad = size * (0.04 * i)
        draw.ellipse(
            [-pad, -pad, size * 0.78 + pad, size * 0.78 + pad],
            fill=(r, g, b, alpha),
        )

    # centred object block
    m = size * 0.28
    draw.rounded_rectangle(
        [m, m, size - m, size - m],
        radius=int(size * 0.07),
        fill=(r, g, b, 46),
        outline=(r, g, b, 120),
        width=2,
    )
    draw.line([m, size * 0.62, size - m, size * 0.62], fill=(r, g, b, 80), width=2)
    return base


def image_data_uri(img: Image.Image, fmt: str = "PNG") -> str:
    buf = BytesIO()
    img.save(buf, format=fmt)
    return f"data:image/{fmt.lower()};base64," + base64.b64encode(buf.getvalue()).decode()


# --- inline icons (stroke inherits from CSS) --------------------------------

ICON_SCAN = (
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M3 8V5a2 2 0 0 1 2-2h3M16 3h3a2 2 0 0 1 2 2v3'
    'M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3"/><circle cx="12" cy="12" r="3"/></svg>'
)

ICON_TEXT = (
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h10"/></svg>'
)

ICON_CHAT = (
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-8 8H7l-4 3v-5.5A8 8 0 0 1 '
    '11 4h2a8 8 0 0 1 8 8z"/></svg>'
)

ICON_LAYERS = (
    '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" '
    'stroke-linejoin="round"><path d="M12 3 3 8l9 5 9-5-9-5zM3 16l9 5 9-5M3 12l9 5 9-5"/></svg>'
)
