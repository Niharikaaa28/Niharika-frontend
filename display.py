from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, width=128, height=64)

font_big = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28
)
font_small = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14
)

def show_centered(text):
    """Single line, perfectly centered"""
    device.clear()
    with canvas(device) as draw:
        w, h = draw.textsize(text, font=font_big)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font_big, fill=255)

def show_result(label, confidence_pct):
    """Two-line result layout"""
    device.clear()
    with canvas(device) as draw:
        # Top line (label)
        w1, h1 = draw.textsize(label, font=font_big)
        x1 = (device.width - w1) // 2
        draw.text((x1, 8), label, font=font_big, fill=255)

        # Bottom line (confidence)
        conf_text = f"Conf: {confidence_pct}%"
        w2, h2 = draw.textsize(conf_text, font=font_small)
        x2 = (device.width - w2) // 2
        draw.text((x2, 44), conf_text, font=font_small, fill=255)