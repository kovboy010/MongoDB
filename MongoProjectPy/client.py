import socket

sock = socket.socket()
sock.connect(('localhost', 1111))
print("connected with srever.")
while True:
    inp = input()
    print(inp)
    if inp == 'exit':
        break
        sock.close()
    sock.send(inp.encode('utf-8'))
    data = sock.recv(1024)


print (data)