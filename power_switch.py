import RPi.GPIO as GPIO
import time
import os
from display import device   # 🔥 IMPORTANT

POWER_PIN = 27  # GPIO27

GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def monitor_power_switch():
    while True:
        if GPIO.input(POWER_PIN):   # switch OFF
            time.sleep(0.3)         # debounce
            if GPIO.input(POWER_PIN):
                try:
                    device.clear()  # 🔥 clear OLED before shutdown
                except:
                    pass
                os.system("sudo shutdown now")
        time.sleep(0.1)