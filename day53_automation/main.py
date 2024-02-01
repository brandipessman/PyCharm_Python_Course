import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_FORM = "https://forms.gle/vNaLc2Z4JTy5t2AW6"
RESPONSES = "https://docs.google.com/forms/d/12aK-Z1BPV29cxpXXZ1YimyvcxOID0PssaWhugQ9xckU/edit#responses"

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_webpage = response.text

soup = BeautifulSoup(zillow_webpage, "html.parser")
listings = soup.select(selector="a.StyledPropertyCardDataArea-anchor")
addresses = []
links = []
for listing in listings:
    addresses.append(listing.getText().strip().replace("|", ""))
    links.append(listing.get("href"))

price_list = soup.select(selector="span.PropertyCardWrapper__StyledPriceLine")
prices = []
for price in price_list:
    price_dollar = price.getText()[0:6]
    prices.append(price_dollar)

full_listings = {
    "addresses":addresses,
    "prices":prices,
    "links":links
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(GOOGLE_FORM)
for num in range(0,len(full_listings["addresses"])):
    sleep(2)
    question1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question1.send_keys(full_listings["addresses"][num])
    question2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question2.send_keys(full_listings["prices"][num])
    question3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question3.send_keys(full_listings["links"][num])
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    new_form = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_form.click()

driver.quit()




