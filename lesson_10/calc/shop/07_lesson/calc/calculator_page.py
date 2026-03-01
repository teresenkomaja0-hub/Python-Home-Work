from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    
    """
    Класс для взаимодействия со страницей калькулятора на сайте.
    """
    def __init__(self, driver):
        
        """
        Инициализация страницы.
        
        :param driver: selenium.webdriver. webdriver экземпляр, используемый для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_locator = (By.ID, "delay")
        self.screen_locator = (By.CLASS_NAME, "screen")
        self.button_locator = lambda text: (By.XPATH, f"//span[text()='{text}']")

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """


    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку на выполнение действия, вводя число секунд.

        :param seconds: Число секунд для задержки.
        :type seconds: int
        :return: None
        """
        delay_input = self.wait.until(EC.presence_of_element_located(self.delay_locator))
        delay_input.clear()
        delay_input.send_keys(str(seconds))


    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку с указанным текстом.

        :param text: Текст кнопки, которую нужно нажать.
        :type text: str
        :return: None
        """
        button = self.wait.until(EC.element_to_be_clickable(self.button_locator(text)))
        button.click()
        

    def get_result(self) -> str:
        """
        Получает текущий отображаемый результат на экране калькулятора.

        :return: Текст результата.
        :rtype: str
        """
        self.wait.until(EC.visibility_of_element_located(self.screen_locator))
        return self.driver.find_element(*self.screen_locator).text
