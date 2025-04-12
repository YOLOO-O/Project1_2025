# reaction.py 
# Author: Liu Zibo
# ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Date: 2025-04-11
# Description: Part 2 - Controlling the light + Detecting button presses using gpiozero (fixed)

from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

def pressed(button):
    print(str(button.pin.number) + " won the game")

print("Quick Reaction Game - Phase: Detecting the buttons")

try:
    print("LED ON")
    led.on()

    delay_time = uniform(5, 10)
    print(f"Waiting for {delay_time:.2f} seconds... Get ready!")
    sleep(delay_time)

    print("LED OFF")
    led.off()

    print("Waiting for button press... (Press Ctrl+C to quit)")

    left_button.when_pressed = pressed
    right_button.when_pressed = pressed

    while True:
        sleep(0.1)

except KeyboardInterrupt:
    print("\nGame stopped by user.")

finally:
    print("Cleaning up GPIO resources...")
    led.close()
    left_button.close()
    right_button.close()
