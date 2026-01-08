import RPi.GPIO as GPIO
import time

CAPTURE_BTN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(CAPTURE_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_capture():
    while GPIO.input(CAPTURE_BTN):
        time.sleep(0.05)