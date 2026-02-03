import pytest
from selenium import webdriver
from calc.calculator_page import CalculatorPage

def test_calc_slow():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    try:
        calculator.open()

        # Вводим задержку 45 секунд
        calculator.set_delay(45)

        # Выполняем нужные кнопки
        for val in ["7", "+", "8", "="]:
            calculator.click_button(val)

        # Проверяем результат
        result_text = calculator.get_result()
        assert result_text == "15", f"Ожидалось 15, получено {result_text}"

    finally:
        driver.quit()