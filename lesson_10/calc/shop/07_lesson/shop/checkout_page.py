from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    
    """
    Страница оформления заказа.
    """
    def __init__(self, driver):
        
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
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
        Заполняет форму данными.

        :param first_name: Имя.
        :type first_name: str
        :param last_name: Фамилия.
        :type last_name: str
        :param postal_code: Почтовый индекс.
        :type postal_code: str
        :return: None
        """     
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)


    def continue_checkout(self) -> None:
        """
        Нажимает кнопку 'Continue'.

        :return: None
        """
        self.driver.find_element(*self.continue_button).click()


    def get_total_price(self) -> str:
        """
        Получает итоговую цену.

        :return: Текст с ценой.
        :rtype: str
        """
        total_text = self.wait.until(EC.presence_of_element_located(self.total_price)).text
        return total_text