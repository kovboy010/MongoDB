import pymongo
from pymongo import MongoClient


# Соединение с базой данных
def start_base():
    client = MongoClient('localhost', 27017)
    db = client['project']
    coll = db['first']
    #return print("Информация о клиенте, подключенному к БД: ", '\n', coll, '\n', '\n')
    return coll

