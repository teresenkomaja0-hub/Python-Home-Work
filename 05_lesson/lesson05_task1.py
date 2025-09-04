from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/classattr")

time.sleep(2)
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

blue_button.click()
print("Клик по синей кнопке выполнен успешно!")

