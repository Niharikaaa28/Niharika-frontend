import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17  # GPIO17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_button_action():
    """
    Returns:
    - "short" for normal press
    - "long" for long press (>= 2 seconds)
    """

    # wait for press
    while GPIO.input(BUTTON_PIN):
        time.sleep(0.01)

    press_time = time.time()

    # wait for release
    while not GPIO.input(BUTTON_PIN):
        time.sleep(0.01)

    duration = time.time() - press_time

    time.sleep(0.05)  # debounce

    if duration >= 4.0:
        return "long"
    else:
        return "short"
    
def detect_long_press(hold_time=2.0):
    """
    Returns True if button is held LOW for hold_time seconds
    """
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        start = time.time()

        # wait while button is held
        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            if time.time() - start >= hold_time:
                return True
            time.sleep(0.05)

    return False