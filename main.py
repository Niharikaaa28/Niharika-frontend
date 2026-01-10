import os
from display import show_centered, show_result, show_status
import time
import sys
from buttons import wait_for_button_action
import select
import threading
from power_switch import monitor_power_switch
import time
from buttons import detect_double_press
time.sleep(5)  # 🔥 allow USB + kernel to settle
# ---------- STARTUP ----------
show_status("STARTING", "Loading model...")
from model import predict

show_status("STARTING", "Loading camera...")
from camera import init_camera, capture_image
init_camera()

threading.Thread(target=monitor_power_switch, daemon=True).start()

# ---------- FUNCTIONS ----------
def scan_t():
    """Easter egg: shows 'code by tanish' then matrix animation"""
    from luma.core.render import canvas
    from display import device, font_small
    import random
    
    # Show "code by tanish" in small font
    device.clear()
    with canvas(device) as draw:
        text = "code by tanish"
        w, h = draw.textsize(text, font=font_small)
        x = (device.width - w) // 2
        y = (device.height - h) // 2
        draw.text((x, y), text, font=font_small, fill=255)
    
    time.sleep(2)
    
    # Matrix-style animation with 1's and 0's
    for _ in range(8):  # 15 frames
        device.clear()
        with canvas(device) as draw:
            for i in range(0, device.width, 8):
                for j in range(0, device.height, 10):
                    if random.random() > 0.3:
                        digit = random.choice(['1', '0'])
                        draw.text((i, j), digit, font=font_small, fill=255)
        time.sleep(0.1)
    
    device.clear()

def scan_once():
    show_centered("SCAN")
    time.sleep(1)

    for i in ["3", "2", "1"]:
        show_centered(i)
        time.sleep(1)

    show_centered("PROCESS")
    time.sleep(0.3)

    image = capture_image()
    label, confidence = predict(image)
    confidence_pct = int(confidence * 100)

    show_result(label, confidence_pct)

# ---------- IDLE STATE ----------
show_centered("READY")
print("Device READY. Press 'r' + Enter to scan.")

# ---------- MAIN LOOP ----------
while True:
    action = wait_for_button_action()
    if detect_double_press():
        show_centered("RESTARTING")
        time.sleep(1)
        os.system("sudo systemctl restart skin-main.service")
        exit()

    if action == "short":
        scan_once()
        time.sleep(5)
        show_centered("READY")

    elif action == "long":
        scan_t()
        show_centered("READY")