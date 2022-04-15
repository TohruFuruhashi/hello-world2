import socket

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

data = client.recv(4096)
print(data.decode("UTF-8"))

client.close()
