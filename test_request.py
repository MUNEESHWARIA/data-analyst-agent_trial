import requests

with open("question.txt", "rb") as f:
    files = {"file": f}
    response = requests.post("http://127.0.0.1:8000/api/", files=files)

print(response.json())
