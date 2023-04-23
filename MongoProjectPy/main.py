import pymongo
import socket
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['project']
coll = db['first']

sock = socket.socket()
sock.bind(('', 1111))
sock.listen(1)
conn, addr = sock.accept()
print("connected", addr)

while True:
   data1 = conn.recv(64)
   check1 = data1.decode('utf-8')
   if check1 != '':
      data2 = check1
   data = {"massage": data2}
   print("ПОЛУЧИЛИ В data: ", data)
   if data2 != check1:
      res = coll.insert_one(data)
   if not data1:
      break
   conn.send(data1.upper())
conn.close()
print("socket close")

#print(client.list_database_names())

#Dropping a collection
#coll.drop()
#print("List of collections after dropping:")

# #List of collections
# print("List of collections:")
# collections = db.list_collection_names()
# for coll in collections:
#    print(coll)

#Creating a collection
#coll = db['first']


# for i in range(5):
#    id_data = i
#    name = "Dima"
#    age = i+18
#    city = "N" + "ixN"*i
#
#    data = [
#       {"name": name, "age": age, "city": city}
#    ]
#data = [{"massage": data2}]

#res = coll.insert_many(data)
   #print(coll.inserted_ids)

# while True:
#    d = input()
#    if d == 'exit':
#       break
#    print(f'echo: {d}')

#Retrieving all the records using the find() method
#print("Records of the collection: ")
#for first in coll.find():
  # print(first)



