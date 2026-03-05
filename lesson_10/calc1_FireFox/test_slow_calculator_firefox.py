import time
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# Если используете webdriver-manager для автоматического скачивания драйвера
# from webdriver_manager.firefox import GeckoDriverManager

from .calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой")
@allure.title("Тест калькулятора с задержкой 45 секунд")
@allure.description("""
    Тест проверяет, что калькулятор с задержкой 45 секунд
    корректно складывает числа 7 и 8, а также проверяет
    фактическое время выполнения операции.
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("slow-calculator", "smoke", "regression")
@allure.link("https://www.calculator.net/", name="Страница калькулятора")
def test_slow_calculator():
    """
    Тест проверяет работу калькулятора с установленной задержкой.
    
    Тест выполняет следующие шаги:
    1. Открывает страницу калькулятора
    2. Устанавливает задержку 45 секунд
    3. Выполняет вычисление 7 + 8
    4. Ожидает появления результата
    5. Проверяет корректность результата и время выполнения
    
    Ожидаемый результат: на экране отображается "15", время выполнения ~45 секунд
    """
    with allure.step("Инициализация веб-драйвера Firefox"):
        driver = webdriver.Firefox()
        driver.maximize_window()
    
    calculator_page = CalculatorPage(driver)

    try:
        with allure.step("Открытие страницы калькулятора"):
            calculator_page.open()
            allure.attach(
                driver.get_screenshot_as_png(),
                name="calculator_page_opened",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Установка задержки 45 секунд"):
            calculator_page.set_delay("45")

        # Засекаем время начала вычислений
        start_time = time.time()
        allure.attach(
            str(start_time),
            name="start_time",
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
            # Ждём, пока на экране не появится результат "15"
            # Максимальное время ожидания ставим с запасом (например, 50 секунд)
            calculator_page.wait_for_result("15", timeout_seconds=50)

        # Засекаем время окончания
        end_time = time.time()
        elapsed_time = end_time - start_time
        allure.attach(
            f"Время выполнения: {elapsed_time:.2f} секунд",
            name="execution_time",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Проверка корректности результата"):
            actual_result = calculator_page.get_displayed_text()
            
            with allure.step("Проверка значения на экране"):
                assert actual_result == "15", \
                    f"Результат на экране '{actual_result}', ожидалось '15'"
                allure.attach(
                    f"Фактический результат: {actual_result}",
                    name="actual_result",
                    attachment_type=allure.attachment_type.TEXT
                )

        with allure.step("Проверка времени выполнения операции"):
            # Дополнительная проверка: убедимся, что прошло примерно 45 секунд
            # Допустим погрешность в 3 секунды
            assert 42 <= elapsed_time <= 48, \
                f"Время выполнения {elapsed_time:.2f} секунд, ожидалось около 45 секунд"
            
            allure.attach(
                f"Время выполнения: {elapsed_time:.2f} сек. (ожидалось ~45 сек.)",
                name="time_check_result",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Тест успешно завершен"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="test_passed_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            print(f"✅ Тест пройден! Результат: {actual_result}, время: {elapsed_time:.2f} сек.")

    except Exception as e:
        with allure.step("Ошибка выполнения теста"):
            allure.attach(
                driver.get_screenshot_as_png(),
                name="error_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                str(e),
                name="error_message",
                attachment_type=allure.attachment_type.TEXT
            )
            raise

    finally:
        with allure.step("Закрытие браузера"):
            # Важно закрыть браузер даже в случае падения теста
            driver.quit()


# Для возможности запуска файла напрямую (не только через pytest)
if __name__ == "__main__":
    test_slow_calculator()
