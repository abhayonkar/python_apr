import requests
from pymongo import MongoClient

data = requests.get('https://jsonplaceholder.typicode.com/users')

user_list = data.json()

client = MongoClient("mongodb://localhost:27017")

db = client['pymo']

user_collection = db['user_pymo']

user_collection.insert_one({'name':'Abhay', 'lname':'onkar'})