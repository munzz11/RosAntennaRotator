import socket

buffer = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 7373))
print("Connected")

while True:
    data = s.recv(buffer)
    print(data)
