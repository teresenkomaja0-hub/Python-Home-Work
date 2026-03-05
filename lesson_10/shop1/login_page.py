from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей авторизации (Login Page) сайта saucedemo.com
    Содержит методы для открытия страницы и входа в систему
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации
        
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.url = "https://www.saucedemo.com/"

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """
        Открывает страницу авторизации в браузере
        
        Returns:
            None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными
        
        Args:
            username: str - имя пользователя
            password: str - пароль пользователя
            
        Returns:
            None
        """
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()