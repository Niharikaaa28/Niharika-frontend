# display.py
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, width=128, height=64)

font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    28
)

def show_result(text):
    device.clear()
    with canvas(device) as draw:
        w, h = draw.textsize(text, font=font)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font, fill=255)