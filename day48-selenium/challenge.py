from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Brandi")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Pessman")
email = driver.find_element(By.NAME, "email")
email.send_keys("bjpessman@gmail.com")

signup = driver.find_element(By.CSS_SELECTOR, "form button")
signup.click()


