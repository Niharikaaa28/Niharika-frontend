from camera import capture_image
from model import predict
from display import show_result
from buttons import wait_for_capture

show_result("READY")

while True:
    wait_for_capture()
    show_result("SCAN")
    image = capture_image()
    result = predict(image)
    show_result(result)