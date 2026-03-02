from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    
    """
    Page Object для страницы корзины.
    Позволяет перейти к оформлению заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.
        
        Args:
            driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.checkout_button = (By.ID, "checkout")


    def checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.
        
        Returns:
            None
        """
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()