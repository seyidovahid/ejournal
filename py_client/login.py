import requests

URL = "http://127.0.0.1:8000/login/"

data = {"username": "token_user", "password": "token123"}
headers = {"Content-Type": "application/json"}

response = requests.post(URL, json=data, headers=headers)

print(response.json())
