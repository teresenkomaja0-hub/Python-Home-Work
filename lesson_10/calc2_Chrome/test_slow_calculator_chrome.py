import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# Если используете webdriver-manager
# from webdriver_manager.chrome import ChromeDriverManager

from .calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой в Chrome")
@allure.title("Тест калькулятора с задержкой 45 секунд в Chrome")
@allure.description("""
    Тест проверяет, что калькулятор с задержкой 45 секунд
    корректно складывает числа 7 и 8 в браузере Chrome.
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("slow-calculator", "chrome", "smoke")
def test_slow_calculator_chrome():
    """
    Тест проверяет работу калькулятора с установленной задержкой в Chrome.
    
    Тест выполняет следующие шаги:
    1. Открывает страницу калькулятора
    2. Устанавливает задержку 45 секунд
    3. Выполняет вычисление 7 + 8
    4. Ожидает появления результата
    5. Проверяет корректность результата и время выполнения
    """
    with allure.step("Инициализация Chrome драйвера"):
        
        chrome_options = Options()

        chrome_options.add_argument("--start-maximized")
        # Если используете webdriver-manager:
        # service = ChromeService(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Если ChromeDriver находится в PATH:
        driver = webdriver.Chrome(options=chrome_options)
    calculator_page = CalculatorPage(driver)

    try:
        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()
            allure.attach(
                driver.get_screenshot_as_png(),
                name="calculator_page_opened_chrome",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Установка задержки 45 секунд"):
            calculator_page.set_delay("45")

        # Засекаем время начала вычислений
        start_time = time.time()
        allure.attach(
            f"Время начала: {start_time}",
            name="start_time_chrome",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Выполнение вычисления 7 + 8"):
            with allure.step("Нажатие кнопки 7"):
                calculator_page.click_button("7")
            
            with allure.step("Нажатие кнопки +"):
                calculator_page.click_button("+")
            
            with allure.step("Нажатие кнопки 8"):
                calculator_page.click_button("8")
            
            with allure.step("Нажатие кнопки ="):
                calculator_page.click_button("=")

        with allure.step("Ожидание результата вычисления"):
            calculator_page.wait_for_result("15", timeout_seconds=50)

        # Засекаем время окончания
        end_time = time.time()
        elapsed_time = end_time - start_time
        allure.attach(
            f"Время выполнения: {elapsed_time:.2f} секунд",
            name="execution_time_chrome",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Проверка корректности результата"):
            actual_result = calculator_page.get_displayed_text()
            
            with allure.step("Проверка значения на экране"):
                assert actual_result == "15", \
                    f"Результат на экране '{actual_result}', ожидалось '15'"
                allure.attach(
                    f"Фактический результат: {actual_result}",
                    name="actual_result_chrome",
                    attachment_type=allure.attachment_type.TEXT
                )

        with allure.step("Проверка времени выполнения операции"):
            assert 42 <= elapsed_time <= 48, \
                f"Время выполнения {elapsed_time:.2f} секунд, ожидалось около 45 секунд"
            
            allure.attach(
                f"Время выполнения: {elapsed_time:.2f} сек. (ожидалось ~45 сек.)",
                name="time_check_result_chrome",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Тест успешно завершен"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="test_passed_screenshot_chrome",
                attachment_type=allure.attachment_type.PNG
            )
            print(f"✅ Тест пройден в Chrome! Результат: {actual_result}, время: {elapsed_time:.2f} сек.")

    except Exception as e:
        with allure.step("Ошибка выполнения теста"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="error_screenshot_chrome",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                name="error_message_chrome",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    finally:
        with allure.step("Закрытие браузера Chrome"):
            driver.quit()


if __name__ == "__main__":
    test_slow_calculator_chrome()