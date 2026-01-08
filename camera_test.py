import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not detected")
    exit()

ret, frame = cap.read()

if not ret:
    print("❌ Failed to capture image")
else:
    cv2.imwrite("camera_test.jpg", frame)
    print("✅ Image captured and saved as camera_test.jpg")

cap.release()