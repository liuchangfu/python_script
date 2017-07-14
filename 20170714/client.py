import socket

server_addr = ('127.0.0.1',9999) #IP和端口构成表示地址
client = socket.socket() #IP和端口构成表示地址
client.connect(server_addr) #要连接的服务器地址
while True:
    data = input('Plese input some string>>>')
    if not data:
        continue
    client.sendall(data.encode('utf-8'))   #发送数据到服务器
    data = client.recv(1024)
    print(data.decode('utf-8'))
client.close()