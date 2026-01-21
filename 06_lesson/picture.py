from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
wait = WebDriverWait(driver, 40)

# Открытие страницы
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание появления изображения с id="award"
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))

# Получение значения атрибута 'src'
src_value = element.get_attribute('src')

# Вывод результата
print(src_value)