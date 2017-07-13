import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000
print("Start the client at {}".format(datetime.now()))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey~~~')
data = client.recv(max_size)
print("AT", datetime.now(), "some reply", data)
client.close()