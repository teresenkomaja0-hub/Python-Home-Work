from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    
    """
    Page Object для страницы оформления заказа.
    Позволяет заполнить информацию и получить итоговую сумму.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.
        
        Args:
            driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")


    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет информацию о покупателе.
        
        Args:
            first_name: str - имя
            last_name: str - фамилия
            postal_code: str - почтовый индекс
            
        Returns:
            None
        """
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)


    def continue_checkout(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.
        
        Returns:
            None
        """
        self.driver.find_element(*self.continue_button).click()


    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа.
        
        Returns:
            str - текст с итоговой стоимостью (например, "Total: $58.29")
        """
        total_text = self.wait.until(EC.presence_of_element_located(self.total_price)).text
        return total_text