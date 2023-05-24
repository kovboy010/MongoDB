import socket
import pickle

#Подлючение клиента получения
def cl_out():
    sock = socket.socket()
    sock.connect(('localhost', 1111))
    print("connected with srever.")
    while True:
        inp = input()
        #print(inp)
        if inp == 'exit':
            break
            sock.close()
        sock.send(inp.encode('utf-8'))
        #data = ''
        data = sock.recv(1024)
        deserialezed = pickle.loads(data)
        print(deserialezed)
        # for i in range(len(deserialezed)):
        #     print(deserialezed[i])