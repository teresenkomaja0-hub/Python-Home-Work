import allure
import pytest
from selenium import webdriver
from shop1 import LoginPage, InventoryPage, CartPage, CheckoutPage

@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест проверки итоговой суммы заказа")
@allure.description("Проверка корректности расчета итоговой стоимости трех товаров в корзине")
def test_sauce_total():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открытие сайта и авторизация пользователя"):
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

        with allure.step("Проверка итоговой стоимости заказа"):
            total_text = checkout_page.get_total_price()
            assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получена {total_text}"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()