import socket 

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
print("socket created")
port = 8888

#Bind the port to computer
s.bind(('',port))
print("socket binded to port : ",port)

#Max number of clients that can connect
s.listen(5)
print('socket is listening')

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send('Message from server'.encode())



