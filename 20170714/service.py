import socket,os  #socket模块

server_add  = ('127.0.0.1',9999) #IP和端口构成表示地址
server = socket.socket() #生成一个新的socket对象
server.setsockopt(socket.SOL_SOCKET,socket.SOCK_STREAM,1)  #设置地址复用
server.bind(server_add) #绑定地址
server.listen(5) #监听, 最大监听数为5
while True:
    client,client_add = server.accept()  #接收TCP连接, 并返回新的套接字和地址
    print('Connected by',client_add)
    while True:
        data = client.recv(1024)  #从客户端接收数据
        print(data.decode('utf-8'))
        client.sendall(data)  #发送数据到客户端
server.close()
