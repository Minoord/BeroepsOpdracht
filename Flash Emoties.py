# Add your Python code here. E.g.
from microbit import *


while True:
   
    if button_a.is_pressed():
        for x in range(4):
            display.show(Image.HAPPY)
            sleep(200)
            display.clear()
            sleep(200)
    if button_b.is_pressed():
        for x in range(4):
            display.show(Image.SILLY)
            sleep(200)
            display.clear()
            sleep(200)
    if accelerometer.was_gesture('shake'):
        for x in range(4):
            display.show(Image.ANGRY)
            sleep(200)
            display.clear()
            sleep(200)
    
    
  
