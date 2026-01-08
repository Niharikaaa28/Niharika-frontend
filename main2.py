from display import show_centered, show_result, show_status
import time
import sys
import select

# Startup UI
show_status("STARTING", "Loading model...")
time.sleep(0.5)

# Import model (loads here)
from model import predict

show_status("STARTING", "Loading camera...")
time.sleep(0.5)

# Import camera (initializes here)
from camera import capture_image

# Ready state
show_centered("READY")

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

# First scan
scan_once()

print("Press 'r' + Enter to rescan")

# Terminal-controlled loop
while True:
    if select.select([sys.stdin], [], [], 0.1)[0]:
        cmd = sys.stdin.readline().strip()
        if cmd.lower() == "r":
            scan_once()