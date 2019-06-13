#!/usr/local/bin/python2


import socket


recv_ip="127.0.0.1"
recv_port=4444 # 0  - 1024 - - you can check netstat -nulp

#creating udp socket
#ip type v4 , udp

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending data to target

while 4>3:
    msg=raw_input
s.sendto("hello",(recv_ip,recv_port))

#recv data from recievre
print(s.recvfrom(10))
