# reaction_202283890023.py
# Author: Qin Siyuan
# ID: 20109672(SETU)/202283890023(NUIST)
# Date: 2025/4/11
# Description: Part2 - Controlling the light + Adding element of surprise in the Quick Reaction Game using RPi.GPIO
 
from gpiozero import LED, Button  
from time import sleep, time  
from random import uniform  

# Get player names  
left_name = input("Enter left player's name: ")  
right_name = input("Enter right player's name: ")  

# Initialize LED and two buttons  
led = LED(4)  
# According to the requirements, left button is connected to GPIO14 and right button to GPIO15  
left_button = Button(14)  
right_button = Button(15)  

# Initialize scores  
left_score = 0  
right_score = 0  

# Define the button press callback function to calculate reaction time and update scores  
def button_pressed(button):  
    global win, reaction_time, left_score, right_score, start_time  
    # Ensure that only the first press in each round is recorded  
    if win is None:  
        reaction_time = time() - start_time  
        if button.pin.number == left_button.pin.number:  
            win = left_name  
            left_score += 1  
        else:  
            win = right_name  
            right_score += 1  

print("Quick Reaction Game - Final Version")  
print("--------------------------------------")  

# The game enters a loop, repeating each round  
while True:  
    print("\nNew round starts!")  
    # LED on: players' waiting phase  
    print("LED ON")  
    led.on()  
    
    # Random wait between 5 and 10 seconds  
    wait_time = uniform(5, 10)  
    print(f"Waiting for {wait_time:.2f} seconds... Get ready!")  
    sleep(wait_time)  
    
    # LED off: start recording reaction time  
    print("LED OFF")  
    led.off()  
    start_time = time()  
    
    # Reset previous round's winner and reaction time  
    win = None  
    reaction_time = None  

    # Bind the button press callback function to both buttons  
    left_button.when_pressed = button_pressed  
    right_button.when_pressed = button_pressed  

    # Wait until one button is pressed (winner is determined)  
    while win is None:  
        sleep(0.01)  

    # Output the result of the current round and reaction time  
    print(f"{win} pressed the button in {reaction_time:.3f} seconds and won this round!")  
    print(f"Current score: {left_name}: {left_score} points, {right_name}: {right_score} points")  
    
    # Unbind button callbacks to avoid repeated detection  
    left_button.when_pressed = None  
    right_button.when_pressed = None  

    # Provide a short interval before the next round starts  
    print("Next round will start in 3 seconds...")  
    sleep(3)
