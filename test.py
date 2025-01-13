import requests


url = "http://127.0.0.1:8000/predict/"
data = {
    "similarity": 0.85,
    "date_difference": 500
}

response = requests.post(url, json=data)
print(response.json())
