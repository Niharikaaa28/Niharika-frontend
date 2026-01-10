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
    
def restart_watchdog(hold_time=2.0):
    """
    ALWAYS running watchdog.
    Restarts service if button held for hold_time seconds.
    """
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            start = time.time()
            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                if time.time() - start >= hold_time:
                    return True
                time.sleep(0.05)
        time.sleep(0.1)

def detect_triple_click(timeout=1.8):
    """
    Returns True if button is clicked 3 times within timeout
    """
    clicks = 0
    start = time.time()

    while time.time() - start < timeout:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            clicks += 1

            # wait for release
            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.01)

            time.sleep(0.2)  # debounce gap

        if clicks >= 3:
            return True

    return False

def get_button_intent(window=1.8):
    """
    Returns one of:
    - "scan"
    - "web"
    - "restart"
    - "long"
    """
    clicks = 0
    press_start = None
    start = time.time()

    while time.time() - start < window:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            press_start = time.time()

            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.01)

            duration = time.time() - press_start

            # Very long press → restart immediately
            if duration >= 2.0:
                return "restart"

            # Long press
            if duration >= 5.0:
                return "long"

            # Otherwise it's a click
            clicks += 1
            time.sleep(0.25)  # debounce

        time.sleep(0.01)

    if clicks >= 3:
        return "web"
    elif clicks == 1:
        return "scan"

    return None