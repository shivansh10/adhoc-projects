#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import datetime

x = datetime.datetime.now()
name = input("Enter your name :")


if (x.hour >= 0 and x.hour <= 5):
	print("Hello " + name +" Good Night ")

if (x.hour >= 6 and x.hour <= 12):
        print("Hello " + name +" Good Morning ")

if (x.hour >= 13 and x.hour <= 16):
        print("Hello " + name +" Good Afternoon ")

if (x.hour >= 17 and x.hour <= 20):
        print("Hello " + name +" Good Evening ")

if (x.hour >= 20 and x.hour <= 24):
        print("Hello " + name +" Good Night ")
