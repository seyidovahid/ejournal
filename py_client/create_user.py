import requests

URL = "http://127.0.0.1:8000/create_user/"

data = {
    "username": "token_user",
    "password": "token123",
    "email": "token@gmail.com",
}

response = requests.post(URL, json=data)

print(response.json())
