import requests
from pymongo import MongoClient

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()

products = product_data['products']

def get_groceries(product):
    return product['category'] == 'groceries'


groceries = list(filter(get_groceries, products))

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("MongoDB Connection Successfully!")
    db=client['pymo1']
    col=db['product_1']
    col.insert_many(groceries)
    print("Data Inserted Successfully!")
except:
    print("Buddy Check -code one more time!")
finally:
    col=None
    db=None
    client=None