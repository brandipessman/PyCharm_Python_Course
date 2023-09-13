import requests
from datetime import *
import os

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_URL = os.environ["SHEETY_URL"]

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 57,
    "height_cm": 170,
    "age": 27
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url = URL, json=exercise_params, headers = header)
result = response.json()

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.today().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_header = {
    "Authorization": f"Bearer {TOKEN}"
}

sheety_response = requests.post(url = SHEETY_URL, json = sheety_params, headers = sheety_header)
print(sheety_response.text)