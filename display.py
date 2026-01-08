from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
import time
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

def _choose_font(text):
    """Choose font based on text length"""
    if len(text) <= 6:
        return font_big
    else:
        return font_medium

def show_centered(text):
    """Single line, auto-scaled and centered"""
    device.clear()
    font = _choose_font(text)

    with canvas(device) as draw:
        w, h = draw.textsize(text, font=font)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font, fill=255)

def show_result(label, confidence_pct):
    """Two-line result layout"""
    device.clear()

    with canvas(device) as draw:
        # Label (auto font)
        font_label = _choose_font(label)
        w1, h1 = draw.textsize(label, font=font_label)
        x1 = (device.width - w1) // 2
        draw.text((x1, 6), label, font=font_label, fill=255)

        # Confidence
        conf_text = f"Conf: {confidence_pct}%"
        w2, h2 = draw.textsize(conf_text, font=font_small)
        x2 = (device.width - w2) // 2
        draw.text((x2, 44), conf_text, font=font_small, fill=255)

def show_status(main_text, status_text):
    """Status line on top + centered main text"""
    device.clear()
    font = _choose_font(main_text)

    with canvas(device) as draw:
        # Status (small, top)
        draw.text((0, 0), status_text, font=font_small, fill=255)

        # Main text (centered lower)
        w, h = draw.textsize(main_text, font=font)
        x = (device.width - w) // 2
        y = (device.height - h) // 2 + 8
        draw.text((x, y), main_text, font=font, fill=255)
        
def show_web_mode(duration=3):
    """
    Inverted WEB MODE screen
    """
    device.clear()
    device.contrast(255)

    with canvas(device) as draw:
        # Full white background (inversion)
        draw.rectangle((0, 0, device.width, device.height), fill=255)

        # Black text
        title = "WEB"
        subtitle = "MODE"

        w1, h1 = draw.textsize(title, font=font_big)
        w2, h2 = draw.textsize(subtitle, font=font_medium)

        x1 = (device.width - w1) // 2
        x2 = (device.width - w2) // 2

        draw.text((x1, 10), title, font=font_big, fill=0)
        draw.text((x2, 38), subtitle, font=font_medium, fill=0)

    time.sleep(duration)
    device.clear()