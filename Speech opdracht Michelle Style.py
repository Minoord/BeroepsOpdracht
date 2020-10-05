# Add your Python code here. E.g.
from microbit import *
import speech
import random

lengteWoordArray = 3
onderwerp = ["You", "Ricky", "Mickey"] 
werkwoord = ["love", "hates", "likes"]
rest = ["me", "Reading", "coffee"]

def sayTheWords1(word):
    print(word)
    speech.say(word, speed=100, pitch=50, throat=90, mouth=120)
    sleep(500)

def sayTheWords2():
    willekeurigGetal = random.randint(0, lengteWoordArray - 1)
    display.show(willekeurigGetal)
    sayTheWords1(onderwerp[willekeurigGetal])
    sayTheWords1(werkwoord[willekeurigGetal])
    sayTheWords1(rest[willekeurigGetal])
    
while True:
    if button_a.is_pressed():
        display.show(Image.DUCK)
        sayTheWords1("hallo i am a Duck, Quack")
    elif button_b.is_pressed():
        display.show(Image.HEART)
        sayTheWords1("I love you!")
    elif display.read_light_level() < 40: 
        sayTheWords2()
    else:
        display.show(Image.SAD) 