from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа (Checkout Page) сайта saucedemo.com
    Содержит методы для заполнения информации о покупателе, продолжения оформления заказа
    и получения итоговой стоимости
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа
        
        Args:
            driver: WebDriver - экземпляр драйвера браузера
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
        Заполняет форму с личной информацией покупателя
        
        Args:
            first_name: str - имя покупателя
            last_name: str - фамилия покупателя
            postal_code: str - почтовый индекс покупателя
            
        Returns:
            None
            
        Note:
            Метод заполняет все три поля формы: Имя, Фамилия и Почтовый индекс
        """
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def continue_checkout(self) -> None:
        """
        Нажимает кнопку "Continue" для перехода к следующему шагу оформления заказа
        
        Returns:
            None
            
        Note:
            После заполнения информации о покупателе этот метод подтверждает введенные данные
            и переходит на страницу с итоговой стоимостью заказа
        """
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа со страницы оформления
        
        Returns:
            str: Текстовое представление итоговой суммы заказа (например, "Total: $58.29")
            
        Note:
            Метод ожидает появления элемента с итоговой стоимостью и возвращает его текст
        """
        total_text = self.wait.until(EC.presence_of_element_located(self.total_price)).text
        return total_text