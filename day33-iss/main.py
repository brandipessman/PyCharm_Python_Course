import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.801565
MY_LONG = -96.707303
MY_EMAIL = "type email"
MY_PASSWORD = "need to make one"


def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])-5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])+19
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = "Subject:Look up👆\n\nThe ISS is above you in the sky."
        )
