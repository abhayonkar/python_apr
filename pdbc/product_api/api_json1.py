import requests
from pymongo import MongoClient
import json

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()

products = product_data['products']

def get_groceries(product):
    return product['category'] == 'groceries'


groceries = list(filter(get_groceries, products))

fp = open('product.json', 'w')

json.dump(groceries, fp)

fp.close