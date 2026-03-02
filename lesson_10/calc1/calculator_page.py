from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self.delay_locator = (By.ID, "delay")
        self.screen_locator = (By.CLASS_NAME, "screen")
        # Локатор для кнопок по тексту
        # Можно использовать XPath, ищущий span с нужным текстом
        self.button_locator = lambda text: (By.XPATH, f"//span[text()='{text}']")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        delay_input = self.wait.until(EC.presence_of_element_located(self.delay_locator))
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, text):
        button = self.wait.until(EC.element_to_be_clickable(self.button_locator(text)))
        button.click()
        
def get_result(self):
    # Ждем, пока результат не станет видимым (не обязательно именно "15")
    self.wait.until(EC.visibility_of_element_located(self.screen_locator))
    # Возвращаем текст
    return self.driver.find_element(*self.screen_locator).text
