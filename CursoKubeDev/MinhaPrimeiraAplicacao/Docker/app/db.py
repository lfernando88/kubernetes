from pymongo import MongoClient

try:
    cliente = MongoClient("mongodb://mongouser:mongopwd@service-mongo:27017")
    db = cliente.pessoas
    collection = db.dados
except:
    print('ERRO - Cannot conecct to db')
