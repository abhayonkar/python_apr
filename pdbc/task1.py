import requests
from pymongo import MongoClient

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("MongoDB Connection Successfully!")
    db=client['pymo1']
    col=db['users']
    col.insert_many(user_list)
    print("Data Inserted Successfully!")
except:
    print("Buddy Check -code one more time!")
finally:
    col=None
    db=None
    client=None