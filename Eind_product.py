# Add your Python code here. E.g.
from microbit import *


while True:
   
    if button_a.is_pressed():
        for x in range(4):
            display.show(Image.HEART)
            sleep(500)
            display.show(Image.HEART_SMALL)
            sleep(500)
    if button_b.is_pressed():
        for x in range(4):
            display.show(Image.DUCK)
            sleep(500)
            display.show(Image(
                "99000:"
                "99000:"
                "99990:"
                "99900:"
                "00000"))
            sleep(500)
            display.show(Image(
                "90000:"
                "90000:"
                "99900:"
                "99000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "99000:"
                "90000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "90000:"
                "00000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00000:"
                "00009:"
                "00000:"
                "00000:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00009:"
                "00099:"
                "00009:"
                "00009:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00099:"
                "00999:"
                "00099:"
                "00099:"
                "00000"))
            sleep(500)
            display.show(Image(
                "00990:"
                "09990:"
                "00999:"
                "00999:"
                "00000"))
            sleep(500)
            display.clear()
            sleep(200)
    if accelerometer.was_gesture('shake'):
        for x in range(4):
            display.show(Image.ANGRY)
            sleep(200)
            display.clear()
            sleep(200)
    
    
  
