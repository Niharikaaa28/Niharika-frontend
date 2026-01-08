from display import show_centered, show_result
from camera import capture_image
from model import predict
import time

# READY
show_centered("READY")
time.sleep(2)

# SCAN
show_centered("SCAN")
time.sleep(1)

# Countdown
for i in ["3", "2", "1"]:
    show_centered(i)
    time.sleep(1)

# Capture + inference
image = capture_image()
label, confidence = predict(image)

confidence_pct = int(confidence * 100)

# Show final result (2 lines)
show_result(label, confidence_pct)

# Keep display alive
while True:
    time.sleep(10)