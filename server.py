import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(30) # Accepts up to 30 connections.

while True:
    sc, address = s.accept()
    print(address)
    l = sc.recv(1024).decode().rstrip()
    ip=l.split(";;")
    ip.remove('')
    print(ip)
    #i=1
    #i=i+1

    for tup in ip:
        fname,msg=tup.split(";")
        with open(fname,'a+',encoding='utf-8') as fw:
            fw.write(msg)
    