'''
Created on May 26, 2021

@author: hchang
'''

import os.path
from os import path
from selenium import webdriver
import sys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# selenium version 4
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
assignLinkList = []
allData = {}  

#login the zybook portal
driver.get("")

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



