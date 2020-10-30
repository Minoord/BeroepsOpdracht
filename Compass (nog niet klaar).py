# Add your Python code here. E.g.
from microbit import *

while True:
     if button_a.was_pressed():
        bearing = compass.heading()
        if bearing < 45 or bearing > 315:
            display.show('N')
        else:
          bearing < 45 or bearing > 135:
            display.show('O')
        else:
          bearing < 135 or bearing > 225:
            display.show('Z')
        else:
            bearing < 225 or bearing > 315:
             display.show('W')
        


