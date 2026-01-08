from model import predict_from_file
from display import show_result
import time

# Run inference on test image
label, confidence = predict_from_file("test_images/malignant.jpg")
confidence_pct = int(confidence * 100)

# Show on OLED
show_result(label, confidence_pct)

# Keep display visible
while True:
    time.sleep(10)