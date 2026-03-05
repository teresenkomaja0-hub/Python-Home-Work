from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen_locator = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "=": (By.XPATH, "//span[text()='=']"),
        }

    def open(self) -> None:
        """Открыть страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay: str) -> None:
        """Установить задержку"""
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        """Нажать на кнопку калькулятора"""
        self.driver.find_element(*self.buttons[button_text]).click()

    def get_displayed_text(self) -> str:
        """Получить текст с экрана калькулятора"""
        return self.driver.find_element(*self.screen_locator).text

    def wait_for_result(self, expected_value: str, timeout_seconds: int = 50) -> None:
        """Ожидать появления результата на экране"""
        WebDriverWait(self.driver, timeout_seconds).until(
            EC.text_to_be_present_in_element(self.screen_locator, expected_value)
        )