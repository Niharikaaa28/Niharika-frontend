from display import show_result
from camera import capture_image
from model import predict
import time

# Step 1: Ready
show_result("READY")
time.sleep(2)

# Step 2: Scan
show_result("SCAN")
time.sleep(1)

# Step 3: Countdown
for i in ["3", "2", "1"]:
    show_result(i)
    time.sleep(1)

# Step 4: Capture + process
show_result("PROCESS")
time.sleep(0.5)

image = capture_image()
result = "Malignant"

# Step 5: Show result
show_result(result)

# Keep display alive
while True:
    time.sleep(10)