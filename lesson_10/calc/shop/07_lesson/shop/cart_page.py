from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    
    """
    Страница корзины.
    """
    def __init__(self, driver):
        
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.checkout_button = (By.ID, "checkout")


    def checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout'.

        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()