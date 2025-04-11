# reaction_202283890023.py
# Author: Qin Siyuan
# ID: 20109672(SETU)/202283890023(NUIST)
# Date: 2025/4/11
# Description: Part2 - Controlling the light + Adding element of surprise in the Quick Reaction Game using RPi.GPIO
 
from gpiozero import LED, Button  
from time import sleep  
from random import uniform  

left_name = input("Please enter left player's name:")
right_name = input("Please enter right player's name:")
  
led = LED(4)  
right_button = Button(14)   
left_button = Button(15)    

print("Quick Reaction Game - Phase: Controlling the light + Surprise!")  

print("LED ON")  
led.on()  
   
delay_time = uniform(5, 10)  
print(f"Waiting for {delay_time:.2f} seconds...")  
sleep(delay_time)  

print("LED OFF")  
led.off()  

  
def pressed(button):
    if button.pin.number == 14:  
       print(left_name + ' won the game')  
    else:
       print(right_name + ' won the game')
    exit()

right_button.when_pressed = pressed  
left_button.when_pressed = pressed  
  
while True:  
    sleep(1)  
