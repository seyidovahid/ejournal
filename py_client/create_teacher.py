import requests

URL = "http://127.0.0.1:8000/create_profile/"

data = {
    "user": 6,
    "profile_type": "teacher",
    "faculty": 1,
    "qualifications": "a qualification",
    "teaching_experience": "this is experience of the teacher 'this-is-newly-created-user'",
}

response = requests.post(URL, json=data)

print(response.json())
