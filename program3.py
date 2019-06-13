#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

k=5
count=0
i=0
j=2


for i in adhoc:
	if i > k :
		count = count + 1
		print(i)

for i in adhoc:
	if i <= j:
		count = count + 1
		print(i)



