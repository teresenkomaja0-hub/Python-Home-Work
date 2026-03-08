from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для работы со страницей корзины (Cart Page) сайта saucedemo.com
    Содержит методы для выполнения действий в корзине, в частности для перехода к оформлению заказа
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины
        
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """
        Нажимает кнопку "Checkout" для перехода к оформлению заказа
        
        Returns:
            None
            
        Note:
            Метод ожидает, пока кнопка "Checkout" станет кликабельной, затем нажимает её.
            После нажатия происходит переход на страницу оформления заказа (Checkout Page)
        """
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()