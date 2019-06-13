#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

f=open('ok.txt','r+') #this will create a file first 
f.seek(0)  #move cursor position
print(f.read())
