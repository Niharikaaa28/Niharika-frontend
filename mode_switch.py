import os
import time
from display import show_centered
from luma.core.render import canvas
from display import device, font_small

def switch_to_web_mode():
    with canvas(device) as draw:
        text = "Switching..."
        w, h = draw.textsize(text, font=font_small)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font_small, fill=255)
    time.sleep(0.8)

    # STOP device mode first
    os.system("sudo systemctl stop skin-main.service")
    time.sleep(1)  # allow full stop

    # START web mode
    os.system("sudo systemctl start skin-web.service")

    # 🔥 EXIT IMMEDIATELY
    os._exit(0)

def switch_to_device_mode():
    with canvas(device) as draw:
        text = "Switching..."
        w, h = draw.textsize(text, font=font_small)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font_small, fill=255)
    time.sleep(1)
    with canvas(device) as draw:
        text = "DEVICE MODE"
        w, h = draw.textsize(text, font=font_small)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font_small, fill=255)
    time.sleep(1)

    os.system("sudo systemctl stop skin-web.service")

    # Give Flask + AP time to die
    time.sleep(2)

    # Start device mode
    os.system("sudo systemctl start skin-main.service")

    # KILL THIS PROCESS COMPLETELY
    os._exit(0)