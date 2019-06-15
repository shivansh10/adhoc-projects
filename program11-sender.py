#!/usr/local/bin/python2


import re
import  socket 
recv_ip="127.0.0.1"
recv_port=4444  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4 ,  uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

option='''
 press 1 to send message:
 press 2 to abort
'''
print(option)


choice= int(raw_input())

while 3>2:

    if choice ==1:
        input_str=raw_input("plz  enter your message :   ") 
        if len(input_str) > 150:
            print ("ERROR! Max 150 characters are allowed")
            print("\n")
            input_str=input("plz  enter your message :   ") 
        
        
    elif choice ==2:
        exit()
        
#  sending  data  to target
    s.sendto(input_str,(recv_ip,recv_port)) 
    #  recv data  from  recv  
    print(s.recvfrom(10))
