from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    
    """
    Страница каталога товаров.
    """
    def __init__(self, driver):
        
        """
        Инициализация страницы каталога.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию.

        :param product_name: Название продукта.
        :type product_name: str
        :return: None
        """
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()