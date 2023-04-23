import socket

sock = socket.socket()
sock.connect(('localhost', 1111))
sock.send('TEST'.encode('utf-8'))

data = sock.recv(64)
sock.close()

print (data)