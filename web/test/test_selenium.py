import requests
import zipfile
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

# selenium version 4
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # type: ignore
assignLinkList = []
allData = {}  

#login the zybook portal
driver.get("http://127.0.0.1:8080/accounts/login")

username = driver.find_element(By.CSS_SELECTOR, "div.user-email input.zb-input")
username.send_keys("test")
password = driver.find_element(By.CSS_SELECTOR, "div.user-password input.zb-input")
password.send_keys("password")



driver.find_element(By.CSS_SELECTOR, "button.signin-button").click()

time.sleep(5)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")

time.sleep(10)
driver.implicitly_wait(20)

print ("execuation done")
driver.quit()