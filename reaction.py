# reaction.py
# Author: Liu Zibo
# ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Date: 2025-04-11
# Description: Part 2 - Controlling the light + Adding element of surprise in the Quick Reaction Game using RPi.GPIO

import RPi.GPIO as GPIO
import time
from random import uniform

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)

try:
    print("Quick Reaction Game - Phase: Controlling the light + Surprise!")

    print("LED ON")
    GPIO.output(4, GPIO.HIGH)
    
    delay_time = uniform(5, 10)
    print(f"Waiting for {delay_time:.2f} seconds...")
    time.sleep(delay_time)

    print("LED OFF")
    GPIO.output(4, GPIO.LOW)

finally:
    GPIO.cleanup()

