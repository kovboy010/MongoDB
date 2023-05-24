import open_socket_in
import cdb

#Прием и запись данных в базу даннных
def write(data1):
    while True:
        data1 = open_socket_in.op_sock_in()
        check = data1.decode('utf-8')
        if check != '':
            data2 = check
        else:
            print("Данных по запросу не найдено!")
        data = {"massage": data2}
        print("ПОЛУЧИЛИ В data: ", data2)
        cdb.coll.insert_one(data)
        open_socket_in.op_sock_in().conn.send(data1.upper())
        if not data1:
            break
    open_socket_in.op_sock_in().connin.close()
    print("socket_in close")

#write()