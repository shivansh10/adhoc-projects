#!//Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import datetime

name=input("enter your name:")
age=int(input("enter your age :"))

x = datetime.datetime.now()

x=x.year
year=int(x-age+95)

print("Hello "+name+" your age after 95 years will be:",year)
