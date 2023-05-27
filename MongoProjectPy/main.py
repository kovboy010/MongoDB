import open_socket
import cdb

#Прием и запись данных в базу даннных
while True:
   data1 = open_socket.conn.recv(1024)
   check = data1.decode('utf-8')
   if check != '':
      data2 = check
      data = {"massage": data2}
      print("ПОЛУЧИЛИ В data: ", data2)
      resp = cdb.coll.insert_one(data)
      open_socket.conn.send(data1.upper())
   if not data1:
      break
open_socket.conn.close()
print("socket_in close")

#Извлчение данных из базы данных
# for CDB.first in CDB.find({"massage": {"girl"}}):
#    print(CDB.first)


# while True:
#    d = input()
#    if d == 'exit':
#       break
#    print(f'echo: {d}')

for fin in cdb.coll.find({"massage": "121"}):
  print(fin)



