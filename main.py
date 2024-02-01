from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)


# from pymongo.mongo_client import MongoClient

# uri = 'mongodb+srv://sanjaysingh19pmongodb:Atheist1234@cluster0.coj2xcn.mongodb.net/mern-estate?retryWrites=true&w=majority'

# client = MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)