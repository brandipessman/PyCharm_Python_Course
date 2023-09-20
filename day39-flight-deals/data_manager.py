import requests
from decouple import config

SHEETY_URL = config('FLIGHT_SHEETY_URL')
TOKEN = config('FLIGHT_SHEETY_TOKEN')

sheety_header = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:


    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_URL}prices", headers=sheety_header)
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
                url=f"{SHEETY_URL}prices/{city['id']}",
                json=new_data,
                headers=sheety_header
            )
            #print(response.text)


    def add_user(self):
        print("Welcome to Brandi's Flight Club.\n We find the best flight deals and email you.")
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        created = False
        while created == False:
            email = input("What is your email? ")
            email_confirm = input("Type your email again: ")
            if email == email_confirm:
                print("You're in the club!")
                user_data = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email
                    }
                }
                headers = {
                    "Authorization": f"Bearer {TOKEN}",
                    "Content-Type": "application/json"
                }
                response = requests.post(
                    url=f"{SHEETY_URL}users",
                    json=user_data,
                    headers=headers
                )
                response.raise_for_status()
                print(response.text)
                created = True
            else:
                print("Emails do not match. Please try again.")