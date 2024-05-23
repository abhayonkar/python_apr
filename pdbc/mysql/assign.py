import requests
import mysql.connector
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = response.json()

print(type(data))

user_list = []

for user in data:
    user_list.append((user['id'], user['name'], user['email'], user['address']['city']))

print(user_list)