import socket
import cdb
import pickle

#Открытие сокета выдачи
sockout = socket.socket()
sockout.bind(('', 1112))
sockout.listen()
print("socket_out created.")
connout, addrout = sockout.accept()
print("connected", addrout)

#Поиск и выдача данных и базы даннных
def read ():
    while True:
        #connout.send("Vvedite zapros: ".encode('utf-8'))
        data_1 = connout.recv(1024)
        check_2 = data_1.decode('utf-8')
        if check_2 != '':
            print(check_2)
            mass = []
            for zapr in cdb.coll.find({"massage": str(check_2)}):
                mass.append(zapr)
            #print(mass)

            serialized = pickle.dumps(mass)
            print(connout.send(serialized))
        if not data_1:
            break
    connout.close()
    b = "socket_out close"
    print(b)