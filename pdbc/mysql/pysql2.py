import requests
import mysql.connector
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = response.json()

conn = mysql.connector.connect(
  host="localhost",
  user="abhay",
  password="6541",
  database="users"
)

mycursor = conn.cursor()

# Insert the data into the database
for user in data:
    address = user['address']['street'] if 'street' in user['address'] else ''
    query = """
        INSERT INTO users (id, name, username, email, address, website, company)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    mycursor.execute(query, (user['id'], user['name'], user['username'], user['email'], address, user['website'], user['company']['name'] if 'name' in user['company'] else ''))

# Commit the changes and close the connection
conn.commit()
mycursor.close()
conn.close()