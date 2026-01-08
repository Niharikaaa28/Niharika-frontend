from display import show_centered, show_result, show_status
import time
import sys
import select

# ---------- STARTUP ----------
show_status("STARTING", "Loading model...")
from model import predict

show_status("STARTING", "Loading camera...")
from camera import capture_image

# ---------- FUNCTIONS ----------
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
    # wait for terminal input
    if select.select([sys.stdin], [], [], 0.1)[0]:
        cmd = sys.stdin.readline().strip().lower()

        if cmd == "r":
            scan_once()
            time.sleep(5)        # show result long enough
            show_centered("READY")
            print("READY again. Press 'r' to rescan.")