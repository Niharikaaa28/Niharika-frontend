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

def show_text(top_text, bottom_text=""):
    device.clear()
    with canvas(device) as draw:
        # Top (big)
        w, h = draw.textsize(top_text, font=font_big)
        x = (device.width - w) // 2
        draw.text((x, 0), top_text, font=font_big, fill=255)

        # Bottom (small)
        if bottom_text:
            w2, h2 = draw.textsize(bottom_text, font=font_small)
            x2 = (device.width - w2) // 2
            draw.text((x2, 40), bottom_text, font=font_small, fill=255)