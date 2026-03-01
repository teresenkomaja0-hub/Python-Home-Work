import pytest
import allure
from selenium import webdriver
from shop.login_page import LoginPage
from shop.inventory_page import InventoryPage
from shop.cart_page import CartPage
from shop.checkout_page import CheckoutPage

def test_sauce_total():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открыть сайт и выполнить авторизацию"):
         login_page.open()
         login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
         products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
         for product in products:
            inventory_page.add_product_to_cart(product)

        with allure.step("Перейти в корзину"):
         inventory_page.go_to_cart()

        with allure.step("Оформить заказ"):
         cart_page.checkout()
        with allure.step("Заполнить информацию о покупателе"):

         checkout_page.fill_information("Мэри", "Петрова", "12345")
         checkout_page.continue_checkout()

        with allure.step("Получить итоговую стоимость"):
         total_text = checkout_page.get_total_price()

        with allure.step("Проверить, что итоговая стоимость равна $58.29"):
         assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получена {total_text}"

    finally:
        driver.quit()