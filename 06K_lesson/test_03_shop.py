from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())
driver = Firefox(service=service)

def test_saucedemo_purchase():
    driver.get("https://www.saucedemo.com/")
        
wait = WebDriverWait(driver, 10)

username_field = wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
username_field.send_keys("standard_user")
        
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")
        
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
        
wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

backpack_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
backpack_button.click()

tshirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
tshirt_button.click()
        
onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
onesie_button.click()

cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_button.click()

wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )
        
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
        
wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Maya")
        
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Tereschenko")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("6541997")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
        
wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text

total_amount = total_text.replace("Total: $", "").strip()
        
assert total_amount == "58.29", f"Ожидалась сумма $58.29, но получена ${total_amount}"
        
driver.quit()


