import socket

#Открытие сокета выдачи
def op_sock_out():
    sockout = socket.socket()
    sockout.bind(('', 1112))
    sockout.listen()
    print("socket_out created.")
    connout, addrout = sockout.accept()
    print("connected", addrout)