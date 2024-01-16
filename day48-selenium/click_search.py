from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles.click()

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# Find the "Search <input> by name
search = driver.find_element(By.NAME, "search")

# Sending keyboard input to Selenium
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()