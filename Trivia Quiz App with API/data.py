

import requests

url = "https://opentdb.com/api.php"
params = {
    "amount": "10",
    "type": "boolean"
}

response = requests.get(url, params=params)
response.raise_for_status()
if response.ok:
    question_data = response.json()["results"]
else:
    print("Request failed:", response.status_code)

