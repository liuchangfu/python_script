import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ('127.0.0.1',1024)

s.bind(host)

s.listen(5)

while True:
    c,addr = s.accept()

    print('连接地址:%s' % str(addr))

    msg = '欢迎您！！'

    c.send(msg.encode('utf-8'))
    c.close()