from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    
    """
    Page Object для страницы медленного калькулятора.
    Предоставляет методы для взаимодействия с калькулятором.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        
        Args:
            driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        self.delay_locator = (By.ID, "delay")
        self.screen_locator = (By.CLASS_NAME, "screen")
        self.button_locator = lambda text: (By.XPATH, f"//span[text()='{text}']")


    def open(self) -> None:
        """
        Открывает страницу калькулятора в браузере.
        
        Returns:
            None
        """
        self.driver.get(self.url)


    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку вычислений.
        
        Args:
            seconds: int - количество секунд задержки
            
        Returns:
            None
        """
        delay_input = self.wait.until(EC.presence_of_element_located(self.delay_locator))
        delay_input.clear()
        delay_input.send_keys(str(seconds))


    def click_button(self, text: str) -> None:
        """
        Нажимает на кнопку с указанным текстом.
        
        Args:
            text: str - текст на кнопке
            
        Returns:
            None
        """
        button = self.wait.until(EC.element_to_be_clickable(self.button_locator(text)))
        button.click()
        

    def get_result(self) -> str:
        """
        Получает результат вычислений с экрана калькулятора.
        
        Returns:
            str - текст результата
        """
        self.wait.until(EC.visibility_of_element_located(self.screen_locator))
        return self.driver.find_element(*self.screen_locator).text
