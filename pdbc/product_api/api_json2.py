import requests
from pymongo import MongoClient
import json

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()

products = product_data['products']

groceries = list(filter(lambda product:product['category'] == 'groceries', products))

fp = open('product.json', 'w')

json.dump(groceries, fp)

fp.close