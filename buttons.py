import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17  # GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_button_action():
    """
    Returns:
    - "short"  -> normal press
    - "restart"   -> long press (2–4 seconds)
    - "long"-> very long press (>= 4 seconds)
    """

    # wait for button press
    while GPIO.input(BUTTON_PIN):
        time.sleep(0.01)

    press_time = time.time()

    # wait for release
    while not GPIO.input(BUTTON_PIN):
        time.sleep(0.01)

    duration = time.time() - press_time
    time.sleep(0.05)  # debounce

    if duration >= 5.0:
        return "long"
    elif duration >= 1.5:
        return "restart"
    else:
        return "short"
