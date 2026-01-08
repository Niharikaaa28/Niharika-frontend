# camera.py
import cv2
import time

print("Initializing camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Camera not detected")

def capture_image(debug=True):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image")

    if debug:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"debug_capture_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[DEBUG] Image saved as {filename}")

    return frame