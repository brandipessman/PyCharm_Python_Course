import requests
from datetime import *

USERNAME = "bjpessman"
TOKEN = "ljalsdfberjlkjlc"
GRAPHID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Crocheting Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/bjpessman/graphs/graph1.html

add_pixel_enpoint = f"{graph_endpoint}/{GRAPHID}"
year = datetime.today().year
month = datetime.today().month
if month < 10:
    month = f"0{month}"
day = datetime.today().day
if day < 10:
    day = f"0{day}"
date = f"{year}{month}{day}"
pixel_config = {
    "date": date,
    "quantity": input("How many minutes did you crochet today? "),
}

response = requests.post(url = add_pixel_enpoint, json = pixel_config, headers=headers)
print(response.text)

update = input("Would you like to update today's record? Type yes or no: ").lower()
if update == "yes":
    update_endpoint = f"{add_pixel_enpoint}/{date}"
    update_params = {
        "quantity": input("How many minutes did you crochet today? ")
    }

    response = requests.put(url = update_endpoint, json = update_params, headers=headers)
    print(response.text)