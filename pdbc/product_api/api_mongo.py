import requests
from pymongo import MongoClient

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()

products = product_data['products']

groceries = []

for product in products:
    if product['category'] == 'groceries':
        groceries.append(product)

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("MongoDB Connection Successfully!")
    db=client['pymo1']
    col=db['product']
    col.insert_many(groceries)
    print("Data Inserted Successfully!")
except:
    print("Buddy Check -code one more time!")
finally:
    col=None
    db=None
    client=None