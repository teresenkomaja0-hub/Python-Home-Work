from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

driver.get("http://uitestingplayground.com/textinput")

wait = WebDriverWait(driver, 10)

search_box = driver.find_element(By.ID, "newButtonName")
search_box.send_keys("SkyPro")

update_button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
update_button.click()
    
updated_button = wait.until(EC.presence_of_element_located((By.ID, "updatingButton")))
    
print("Текущий текст кнопки:", updated_button.text)