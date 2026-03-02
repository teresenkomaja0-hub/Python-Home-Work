import pytest
import allure
from selenium import webdriver
from shop1.login_page import LoginPage
from shop1.inventory_page import InventoryPage
from shop1.cart_page import CartPage
from shop1.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity("CRITICAL")
@allure.title("Тест полного цикла покупки")
@allure.description("Тест проверяет полный цикл покупки в интернет-магазине")
                    

def test_sauce_total() -> None:
    """
    Тест проверяет корректность итоговой суммы при покупке трех товаров.
    
    Ожидаемый результат: итоговая сумма равна $58.29.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открытие сайта и авторизация"):
         login_page.open()
         login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
         products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product in products:
            inventory_page.add_product_to_cart(product)

        with allure.step("Переход в корзину"):
         inventory_page.go_to_cart()

        with allure.step("Оформление заказа"):
         cart_page.checkout()
         checkout_page.fill_information("Мэри", "Петрова", "12345")
         checkout_page.continue_checkout()

        with allure.step("Проверка итоговой стоимости"):
         total_text = checkout_page.get_total_price()
        with allure.step(f"Проверка: ожидается {expected_sum}"):
         assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получена {total_text}"

    finally:
        with allure.step("Закрытие браузера"):

         driver.quit()