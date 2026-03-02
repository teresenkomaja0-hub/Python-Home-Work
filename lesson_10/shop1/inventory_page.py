from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    
    """
    Page Object для страницы инвентаря (списка товаров).
    Позволяет добавлять товары в корзину и переходить в корзину.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров.
        
        Args:
            driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.
        
        Args:
            product_name: str - название товара для добавления
            
        Returns:
            None
        """
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


    def go_to_cart(self) -> None:
        """
        Переходит в корзину покупок.
        
        Returns:
            None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()