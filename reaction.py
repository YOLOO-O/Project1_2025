# reaction.py
# Author: Liu Zibo
# ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Date: 2025-04-11
# Description: Quick Reaction Game - Final Version

from gpiozero import LED, Button
from time import sleep, time
from random import uniform

left_name = input("Enter left player's name: ")
right_name = input("Enter right player's name: ")

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_score = 0
right_score = 0
winner = None
reaction_time = 0
start_time = 0

def pressed(button):
    global winner, left_score, right_score, reaction_time
    if winner is None:
        reaction_time = time() - start_time
        if button.pin.number == 14:
            winner = left_name
            left_score += 1
        else:
            winner = right_name
            right_score += 1

print("\nQuick Reaction Game - Final Version with Scores and Timer")
print("------------------------------------------------------------")

try:
    while True:
        print("\nNew round starting...")
        print("LED ON (get ready)")
        led.on()
        wait_time = uniform(5, 10)
        sleep(wait_time)

        print("LED OFF! Press the button!")
        led.off()
        start_time = time()

        winner = None
        reaction_time = 0

        left_button.when_pressed = pressed
        right_button.when_pressed = pressed

        while winner is None:
            sleep(0.01)

        print(f"{winner} won this round!")
        print(f"Reaction time: {reaction_time:.3f} seconds")
        print(f"Scoreboard: {left_name} - {left_score} | {right_name} - {right_score}")
        print("Next round in 3 seconds...\n")
        sleep(3)

except KeyboardInterrupt:
    print("\nGame ended by user.")

finally:
    print("Cleaning up GPIO resources...")
    led.close()
    left_button.close()
    right_button.close()

