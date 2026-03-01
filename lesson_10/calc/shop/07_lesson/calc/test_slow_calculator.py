import pytest
import allure
from selenium import webdriver
from calc.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Тест калькулятора")
@allure.description("Проверка сложения 7+8=15 с задержкой 45 секунд")
@allure.severity("CRITICAL")

def test_calc_slow() -> None:
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        with allure.step("Открыть страницу калькулятора"):

         calculator.open()

        with allure.step(f"Установить задержку 45 секунд"):
         calculator.set_delay(45)

        with allure.step("Выполнить вычисление 7 + 8"):
         for val in ["7", "+", "8", "="]:
            calculator.click_button(val)

        with allure.step("Получить результат"):
         result_text = calculator.get_result()

        with allure.step("Проверить, что результат равен 15"):
         assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    finally:
        driver.quit()