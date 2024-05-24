import mysql.connector
import requests

resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products = product_data['products']

beauty = list(filter(lambda product:product['category'] == 'beauty'), products )

data = []

for product in beauty:
    data.append()