import cv2

cap = cv2.VideoCapture(0)

def capture_image():
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image from camera")
    return frame