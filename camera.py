import cv2

print("Initializing camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Camera not detected")

def capture_image():
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image")
    return frame