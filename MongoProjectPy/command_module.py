import open_socket_in
import cdb
import pickle
from pymongo import MongoClient
import socket

fwr = 0
fre = 0
def handle_command(command):
    global fwr
    global fre
    # command = open_socket_in.recieve_handler(mess).data
    if command == ('wr'):
        fwr = 1
        # write(command)
    elif command == ('re'):
        fre = 1
        # read(command)
    elif command == ('dis'):
        disconnect()
    elif (command != 'wr') or (command != 're') or (command != 'dis'):
        if fwr == 1:
            fwr = 0
            write(command)
        elif fre == 1:
            fre = 0
            read(command)
        else:
            print("Command not found")


def write(data_mess):
    # data_mess = open_socket_in.recieve_handler(mess)
    data = {"massage": data_mess}
    print("ПОЛУЧИЛИ В data: ", data_mess)
    # cdb.start_base().coll.insert_one(data)
    #db = MongoClient('localhost', 27017)['project']['second']
    cdb.start_base().insert_one(data)
    # open_socket_in.op_sock_in().connin.close()
    # print("socket_in close")

def read(inp):
    mass = []
    # f = cdb.start_base().find({"massage:": str(inp)})
    # mass.append(f)
    print("input", inp)
    for f in cdb.start_base().find({"massage": inp}):
        mass.append(f)
    print ("Получили из базы данных: ", mass)
    if mass == []:
        print("я здесь 2")
        return(print("Данных не найдено!"))
    if mass != []:
        print("я здесь 3")
        return open_socket_in.send(pickle.dumps(mass))


def disconnect():
    open_socket_in.op_sock_in().conn.close()




