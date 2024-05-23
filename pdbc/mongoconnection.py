from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client['pymo']

user_collection = db['users']

user_collection.insert_one()