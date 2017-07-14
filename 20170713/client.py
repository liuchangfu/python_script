__author__ = 'qingjin'
from socket import *

HOST='127.0.0.1'
POST=21567
BUFSIZE=1024
ADDR=(HOST,POST)
tcpClientSocket=socket(AF_INET,SOCK_STREAM)
tcpClientSocket.connect(ADDR)

while True:
    try:
        data=input('>')
        if data.lower()=='q':
            break
        tcpClientSocket.send(data.encode())
        data=tcpClientSocket.recv(BUFSIZE).decode()
        if len(data) == 0:
            continue
        print(data)
    except socket.error:
        tcpClientSocket.connect(ADDR)
tcpClientSocket.close()