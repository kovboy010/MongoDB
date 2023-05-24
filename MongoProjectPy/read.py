import open_socket_out
import cdb
import pickle

#Поиск и выдача данных и базы даннных
def read ():
    while True:
        #connout.send("Vvedite zapros: ".encode('utf-8'))
        data_1 = open_socket_out.connout.recv(1024)
        check_2 = data_1.decode('utf-8')
        if check_2 != '':
            print(check_2)
            mass = []
            for zapr in cdb.coll.find({"massage": str(check_2)}):
                print(zapr)
                mass.append(zapr)
            if mass != []:
                #print(mass)
                serialized = pickle.dumps(mass)
                open_socket_out.connout.send(serialized)
            else:
                send = "Data not Found"
                open_socket_out.connout.send(pickle.dumps(send))
        if not data_1:
            break
    open_socket_out.connout.close()
    print("socket_out close")