import requests
from datetime import *
from twilio.rest import Client
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

account_sid = "IMadeThisUp"
auth_token = "IMadeThisUpToo"

today = datetime.today()
yesterday = datetime.date(today - timedelta(days = 1))
twodays = datetime.date(today - timedelta(days = 2))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_url = "https://newsapi.org/v2/everything"
news_params = {
    "q": "apple",
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": "fc535d89705d4eb0969822ae8e00b96e"
}

news_response = requests.get(url = news_url, params=news_params)
news_data = news_response.json()
article1 = news_data["articles"][0]["title"]
article2 = news_data["articles"][1]["title"]
article3 = news_data["articles"][2]["title"]
news = f"{article1}\n{article2}\n{article3}"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "KVPRFVRUQVZTCW2V"
}
url = "https://www.alphavantage.co/query"
response = requests.get(url = url, params = stock_params)
data = response.json()
after_stock = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
before_stock = float(data["Time Series (Daily)"][f"{twodays}"]["4. close"])
change = after_stock - before_stock
if change < 0:
    symbol = "v"
else:
    symbol = "^"
percent_change = abs(change)/before_stock * 100

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if percent_change >= 5:
    text = (f"{COMPANY_NAME}: {symbol}{int(percent_change)}%\n"
            f"Headlines: \n{news}")
    print(text)
    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #     body=f"{text}",
    # from = "a phone number",
    # to = "the phone number on the twilio account"
    # )
    # print(message.status)
