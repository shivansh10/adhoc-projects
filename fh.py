#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
'''
f=open("okay.txt","w")
f.write("hello")
f.write("\n")
f.write("world")
f.close()
'''


f=open("okay.txt","r")
data=f.read()
f.seek(0)
print(data)
f.close()
