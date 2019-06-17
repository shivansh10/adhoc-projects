#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import datetime
import pyttsx3

sound_driver = pyttsx3.init()
x = datetime.datetime.now()
name = input("Enter your name :")
sound_driver.say("Hello"+ name)
sound_driver.runAndWait()


if (x.hour >= 0 and x.hour <= 5):
        print("Hello " + name +" Good Night")
        sound_driver.say("Good Night")
        sound_driver.runAndWait()
       

if (x.hour >= 6 and x.hour <= 12):
        print("Hello " + name +" Good Morning")
        sound_driver.say("Good Morning")
        sound_driver.runAndWait()
        

if (x.hour >= 13 and x.hour <= 16):
        print("Hello " + name +" Good Afternoon")
        sound_driver.say("Good Afternoon")
        sound_driver.runAndWait()
        

if (x.hour >= 17 and x.hour <= 20):
        print("Hello " + name +" Good Evening")
        sound_driver.say("Good Evening")
        sound_driver.runAndWait()
       

if (x.hour >= 20 and x.hour <= 24):
        print("Hello " + name +" Good Night")
        sound_driver.say("Good Night")
        sound_driver.runAndWait()
        
