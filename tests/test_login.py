import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
# Import the time module

from selenium.webdriver.support.wait import WebDriverWait


# Set up the WebDriver using the Service class
service = Service('D:/SQA_Project/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
# Open Google
driver.get("https://ems-test.amaderit.net/")

username_field = driver.find_element(By.ID,"username")
username_field.send_keys('adming3')

password_field = driver.find_element(By.ID,"password")
password_field.send_keys('12345678')

# Print the page title to the console
print("Page title is:", driver.title)
# Close the browser
driver.quit()