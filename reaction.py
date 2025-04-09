# reaction.py
# Author: Liu Zibo
# Description: Part 2 - Controlling the light in the Quick Reaction Game using RPi.GPIO

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


GPIO.setup(4, GPIO.OUT)

try:
    print("Quick Reaction Game - Phase: Controlling the light")
    
    print("LED ON")
    GPIO.output(4, GPIO.HIGH) 
    time.sleep(5) 

    print("LED OFF")
    GPIO.output(4, GPIO.LOW)

finally:
    GPIO.cleanup() 
