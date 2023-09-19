import requests
from pprint import pprint

SHEETY_URL = "URL"
TOKEN = "TOKEN"

sheety_header = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL, headers=sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data,
                headers=sheety_header
            )
            print(response.text)
