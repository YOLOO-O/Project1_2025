from gpiozero import LED, Button
from time import sleep
from random import uniform

left_name = input("Enter left player's name: ")
right_name = input("Enter right player's name: ")

led = LED(4)
left_button = Button(14)
right_button = Button(15)

game_over = False

def pressed(button):
    global game_over
    if button.pin.number == 14:
        print(left_name + " won the game!")
    else:
        print(right_name + " won the game!")
    game_over = True

print("Quick Reaction Game - Phase: Detecting the buttons + Player names")

try:
    print("LED ON")
    led.on()

    delay_time = uniform(5, 10)
    print(f"Waiting for {delay_time:.2f} seconds... Get ready!")
    sleep(delay_time)

    print("LED OFF")
    led.off()

    print("Waiting for button press...")

    left_button.when_pressed = pressed
    right_button.when_pressed = pressed

    while not game_over:
        sleep(0.1)

except KeyboardInterrupt:
    print("\nGame stopped by user.")

finally:
    print("Cleaning up GPIO resources...")
    led.close()
    left_button.close()
    right_button.close()
