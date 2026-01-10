import cv2
import time

print("Initializing camera...")

cap = None

def init_camera():
    global cap

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Camera not detected")

    # 🔥 CAMERA WARM-UP
    print("Warming up camera...")
    start = time.time()
    while time.time() - start < 2.5:
        cap.read()

    # Drop extra frames to stabilize exposure
    for _ in range(10):
        cap.read()

    print("Camera ready.")

def capture_image(debug=True):
    if cap is None:
        raise RuntimeError("Camera not initialized")

    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Failed to capture image")
    
    if debug:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"debug_capture_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"[DEBUG] Image saved as {filename}")

    return frame