from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3801655990&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(URL)

driver.implicitly_wait(20)
signin = driver.find_element(By.LINK_TEXT, "Sign in")
signin.click()

driver.implicitly_wait(20)
signin2 = driver.find_element(By.LINK_TEXT, "Sign in")
signin2.click()

driver.implicitly_wait(20)
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.implicitly_wait(20)
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:
    job.click()
    try:
        driver.implicitly_wait(20)
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        easy_apply.click()

        driver.implicitly_wait(20)
        phonenumber = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--input")
        if phonenumber.text == "":
            phonenumber.send_keys(PHONE)

        next = driver.find_element(By.ID, "ember927")
        if next.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            next.click()

        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
driver.quit()