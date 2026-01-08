from display import show_centered, show_result
import time

# Show READY immediately (before camera/model imports)
show_centered("READY")
time.sleep(1)

# Show SCAN
show_centered("SCAN")
time.sleep(1)

# Countdown
for i in ["3", "2", "1"]:
    show_centered(i)
    time.sleep(1)

# NOW import heavy stuff
from camera import capture_image
from model import predict

# Capture + inference
image = capture_image()
label, confidence = predict(image)
confidence_pct = int(confidence * 100)

# Show result
show_result(label, confidence_pct)

# Reset to READY after 5 sec
time.sleep(5)
show_centered("READY")

while True:
    time.sleep(10)