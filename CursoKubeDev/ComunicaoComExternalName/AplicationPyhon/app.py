from pymongo import MongoClient
import datetime

cliente = MongoClient("mongodb://mongouser:mongopwd@service-mongo:27017")

banco = cliente.test_database
album = banco.test_collection


if __name__ == '__main__':
    musicas = [
        {
            "_id": 1,
            "nome": "Radioactive",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()
        },
        {
            "_id": 2,
            "nome": "Hear Me",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()
        },
        {
            "_id": 3,
            "nome": "Demons",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()
        },
        {
            "_id": 4,
            "nome": "Nothing Left To Say",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()
        },
        {
            "_id": 5,
            "nome": "Amsterdam",
            "banda": "Imagine Dragons",
            "categorias": ["indie", "rock"],
            "lancamento": datetime.datetime.now()
        }
    ]


    album.insert_many(musicas)
