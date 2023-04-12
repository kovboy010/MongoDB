import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Test']
coll = db['testing']
print(client.list_database_names())

# #Creating a collection
# coll = db['testing']
#
# data = [
#    {"_id": "101", "name": "Ram", "age": "26", "city": "Hyderabad"},
#    {"_id": "102", "name": "Rahim", "age": "27", "city": "Bangalore"},
#    {"_id": "103", "name": "Robert", "age": "28", "city": "Mumbai"}
# ]
# res = coll.insert_many(data)
# print(coll.inserted_ids)

#Retrieving all the records using the find() method
print("Records of the collection: ")
for doc1 in coll.find():
   print(doc1)



