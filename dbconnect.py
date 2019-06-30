#!/usr/bin/pyhton3

import mysql.connector as mysql
# RDS INFO
u='root'
p=''
db='adhoc'
h='mysqldbserver.cfk7oiewt5cv.ap-south-1.rds.amazonaws.com'


#now connecting
connect=mysql.connect(user=u,password=p,database=db,host=h)

#now geneerating a sql lang cursor

cur=connect.cursor()     #provides every sql command on python

#now we can write sql query

cur.execute("show tables;") 

#print result
print(cur.fetchall())    

#closing connection
connect.close()
