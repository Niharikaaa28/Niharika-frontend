from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, width=128, height=64)

# Fonts
font_big = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28
)
font_medium = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22
)
font_small = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12
)

def _fit_font(draw, text, max_width):
    """Pick the largest font that fits the screen width"""
    for font in (font_big, font_medium):
        w, _ = draw.textsize(text, font=font)
        if w <= max_width - 4:
            return font
    return font_small  # last-resort fallback

def show_centered(text):
    device.clear()
    with canvas(device) as draw:
        font = _fit_font(draw, text, device.width)
        w, h = draw.textsize(text, font=font)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font, fill=255)

def show_result(label, confidence_pct):
    device.clear()
    with canvas(device) as draw:
        # Label (auto-fit)
        font_label = _fit_font(draw, label, device.width)
        w1, h1 = draw.textsize(label, font=font_label)
        x1 = (device.width - w1) // 2
        draw.text((x1, 6), label, font=font_label, fill=255)

        # Confidence (always small)
        conf_text = f"Conf: {confidence_pct}%"
        w2, h2 = draw.textsize(conf_text, font=font_small)
        x2 = (device.width - w2) // 2
        draw.text((x2, 44), conf_text, font=font_small, fill=255)

def show_status(main_text, status_text):
    device.clear()
    with canvas(device) as draw:
        # Status line (small)
        draw.text((0, 0), status_text, font=font_small, fill=255)

        # Main text (auto-fit)
        font = _fit_font(draw, main_text, device.width)
        w, h = draw.textsize(main_text, font=font)
        x = (device.width - w) // 2
        y = (device.height - h) // 2 + 8
        draw.text((x, y), main_text, font=font, fill=255)