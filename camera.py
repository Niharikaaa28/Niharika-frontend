import cv2

cap = None

def init_camera():
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Camera not detected")

def capture_image():
    init_camera()
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image")
    return frame