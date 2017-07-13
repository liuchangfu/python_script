import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ('127.0.0.1',1024)

s.connect(host)

msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))