# main2.py (TEMP, no buttons)

from display import show_text
from camera import capture_image
from model import predict
import time

# READY
show_text("READY")
time.sleep(2)

# SCAN
show_text("SCAN")
time.sleep(1)

# Countdown
for i in ["3", "2", "1"]:
    show_text(i)
    time.sleep(1)

# Processing animation
for _ in range(2):
    show_text("PROCESS", "Please wait")
    time.sleep(0.5)
    show_text("PROCESS.", "Please wait")
    time.sleep(0.5)
    show_text("PROCESS..", "Please wait")
    time.sleep(0.5)
    show_text("PROCESS...", "Please wait")
    time.sleep(0.5)

# Capture + inference
image = capture_image()
label, confidence = predict(image)

confidence_pct = int(confidence * 100)

# Show result
show_text(label, f"Conf: {confidence_pct}%")

# Keep display alive
while True:
    time.sleep(10)