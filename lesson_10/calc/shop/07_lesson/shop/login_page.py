from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
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
        self.url = "https://www.saucedemo.com/"

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")


    def open(self) -> None:
        """
        Открывает страницу логина.

        :return: None
        """
        self.driver.get(self.url)


    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход по логину и паролю.

        :param username: Имя пользователя.
        :type username: str
        :param password: Пароль.
        :type password: str
        :return: None
        """
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()