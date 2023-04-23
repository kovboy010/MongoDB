import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 1112))
print("connected with srever.")
while True:
    inp = input()
    print(inp)
    if inp == 'exit':
        break
        sock.close()
    sock.send(inp.encode('utf-8'))
    #data = ''
    data = sock.recv(1024)
    deserialezed = pickle.loads(data)
    for i in range(len(deserialezed)):
        print(deserialezed[i])