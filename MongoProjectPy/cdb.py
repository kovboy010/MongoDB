import pymongo
from pymongo import MongoClient

#Соединение с базой данных
client = MongoClient('localhost', 27017)
db = client['project']
coll = db['first']