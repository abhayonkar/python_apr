import requests
import mysql.connector
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = response.json()

print(type(data))

user_list = []

for user in data:
    user_list.append((user['id'], user['name']))

print(user_list)

# conn = mysql.connector.connect(
#   host="localhost",
#   user="abhay",
#   password="6541",
#   database="users"
# )

# mycursor = conn.cursor()