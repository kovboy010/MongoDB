import socket
import cdb

#Открытие сокета приема
sockin = socket.socket()
sockin.bind(('', 1111))
sockin.listen()
print("socket_in created.")
connin, addrin = sockin.accept()
print("connected", addrin)

#Прием и запись данных в базу даннных
def write():
    while True:
        data1 = connin.recv(1024)
        check = data1.decode('utf-8')
        if check != '':
            data2 = check
            data = {"massage": data2}
            print("ПОЛУЧИЛИ В data: ", data2)
            resp = cdb.coll.insert_one(data)
            connin.send(data1.upper())
        if not data1:
            break
    connin.close()
    print("socket_in close")