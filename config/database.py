from pymongo import MongoClient


client = MongoClient('mongodb+srv://${username}:${password}@cluster0.coj2xcn.mongodb.net/mern-estate?retryWrites=true&w=majority')

db = client.todo_db

collection_name = db["todo_collection"]