from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Класс для работы со страницей товаров (Inventory Page) сайта saucedemo.com
    Содержит методы для добавления товаров в корзину и перехода в корзину
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы товаров
        
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину
        
        Args:
            product_name: str - название товара для добавления в корзину
            
        Returns:
            None
            
        Note:
            Метод ищет товар по текстовому названию на странице и нажимает кнопку
            "Add to cart", связанную с этим товаром
        """
        xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def go_to_cart(self) -> None:
        """
        Выполняет переход в корзину покупок
        
        Returns:
            None
            
        Note:
            Метод нажимает на иконку корзины в правом верхнем углу страницы
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()