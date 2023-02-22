import socket
s = socket.socket()
s.connect(("127.0.0.1",8888))
print(s.recv(2048).decode())
