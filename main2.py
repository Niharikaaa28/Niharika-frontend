from display import show_centered, show_result
import time

# Show READY immediately
show_centered("READY")
time.sleep(1)

# Show SCAN
show_centered("SCAN")
time.sleep(1)

# Countdown
for i in ["3", "2", "1"]:
    show_centered(i)
    time.sleep(1)

# VERY IMPORTANT: show PROCESS and yield CPU
show_centered("PROCESS")
time.sleep(0.3)   # allows OLED to refresh

# Now import heavy modules
from camera import capture_image
from model import predict

# Heavy work happens AFTER PROCESS is visible
image = capture_image()
label, confidence = predict(image)
confidence_pct = int(confidence * 100)

# Show result
show_result(label, confidence_pct)

# Keep result visible
time.sleep(5)

# Return to READY and IDLE
show_centered("READY")

# Idle loop (wait for future button press)
while True:
    time.sleep(1)