import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
MY_EMAIL = "@gmail.com"
MY_PASSWORD = "use an app password from gmail settings"

response = requests.get(URL, headers = header)
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, "lxml")
dollars = soup.find(name = "span", class_ = "a-price-whole").getText()
cents = soup.find(name = "span", class_ = "a-price-fraction").getText()
price = float(f"{dollars}{cents}")
price_unit = f"${price}"
product_title = soup.find(name = "span", id = "productTitle").getText().strip()
buy_price = 100
buy_price_unit = "$100"
message = f"The {product_title} is now {price_unit}, below your target price of {buy_price_unit}. Buy now!"

if price < buy_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Check Alert\n\n{message}\n{URL}".encode("utf-8")
    )