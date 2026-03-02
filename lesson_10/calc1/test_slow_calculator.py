import pytest
import allure
from selenium import webdriver
from calc1.calculator_page import CalculatorPage

@allure.feature("Калькулятор")
@allure.severity("CRITICAL")
@allure.title("Тест калькулятора")
@allure.description("Проверка результата")

def test_calc_slow() -> None:
    """
    Тест проверяет корректность работы калькулятора с задержкой.
    
    Ожидаемый результат: после вычислений на экране отображается "15".
    """
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        with allure.step("Открытие страницы калькулятора"):

         calculator.open()

        with allure.step("Установка задержки 45 секунд"):
         calculator.set_delay(45)

        with allure.step("Ввод выражения 7 + 8 ="):
         for val in ["7", "+", "8", "="]:
            calculator.click_button(val)

        with allure.step("Получение результата"):
         result_text = calculator.get_result()
        with allure.step("Проверка результата"):

         assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    finally:
        with allure.step("Закрытие браузера"):

         driver.quit()