import requests
import datetime as dt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()




nutritionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
    "Content-Type": "application/json"
}

user_input = input("What exercise did you do today? ")

params = {
    "query": (user_input),
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 180,
    "age": 25
}

response = requests.post(url=nutritionix_api_endpoint, json=params, headers=headers)
# response.raise_for_status()
data = response.json()

#sheety posting data from the nutritionix api
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
sheety_header = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}
body = {
    "workout": {
        "date": dt.datetime.now().strftime("%d/%m/%Y"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": data["exercises"][0]["name"].title(),
        "duration": round(data["exercises"][0]["duration_min"]),
        "calories": round(data["exercises"][0]["nf_calories"]),
        
    }
}

response_sheety = requests.post(sheety_endpoint, headers=sheety_header, json=body)
response_sheety.raise_for_status()
response_sheety.json()
