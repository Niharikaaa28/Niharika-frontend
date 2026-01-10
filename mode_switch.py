import os
import time
from display import show_centered

def switch_to_web_mode():
    show_centered("SWITCHING")
    time.sleep(1)
    show_centered("WEB MODE")
    time.sleep(1)

    os.system("sudo systemctl stop skin-main.service")
    os.system("sudo systemctl start skin-web.service")

def switch_to_device_mode():
    show_centered("SWITCHING")
    time.sleep(1)
    show_centered("DEVICE MODE")
    time.sleep(1)

    os.system("sudo systemctl stop skin-web.service")
    os.system("sudo systemctl start skin-main.service")