import pytest
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
        # Открываем сайт и авторизация
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавляем товары
        products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product in products:
            inventory_page.add_product_to_cart(product)

        # Переход в корзину
        inventory_page.go_to_cart()

        # Оформление заказа
        cart_page.checkout()
        checkout_page.fill_information("Мэри", "Петрова", "12345")
        checkout_page.continue_checkout()

        # Получение итоговой стоимости
        total_text = checkout_page.get_total_price()
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получена {total_text}"

    finally:
        driver.quit()