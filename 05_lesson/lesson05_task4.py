from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

time.sleep(1)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

time.sleep(1)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(2)

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
message_text = success_message.text.strip()

print("\nТекст зеленой плашки:")
print("=" * 50)
print(message_text)
print("=" * 50)
        
print("Авторизация выполнена успешно!")