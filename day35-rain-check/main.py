import requests
from twilio.rest import Client
import os

# use export OWM_API_KEY=key in the terminal to save the key to the environment
api_key = os.environ.get("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "IMadeThisUp"
auth_token = "IMadeThisUpToo"

parameters = {
    "lat": 40.813618,
    "lon": -96.702599,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url = OWM_endpoint, params = parameters)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

will_rain = False

for hour in data_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body = "It's going to rain today. Bring an umbrella.",
        from = "a phone number",
        to = "the phone number on the twilio account"
    )
    print(message.status)

