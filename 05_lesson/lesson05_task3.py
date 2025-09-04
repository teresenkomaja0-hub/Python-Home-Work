from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")
time.sleep(1)

input_field.clear()
time.sleep(1)

input_field.send_keys("Pro")
time.sleep(1)

driver.quit()