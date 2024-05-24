import requests

response = requests.get('https://dummyjson.com/products')
data = response.json()  # This will parse the response as JSON and give you a dictionary

print(data)  # This will print the entire dictionary