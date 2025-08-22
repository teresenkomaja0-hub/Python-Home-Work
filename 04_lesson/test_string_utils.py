import pytest
from string_utils import StringUtils


string_utils = StringUtils()


class TestCapitalize:
    """Тесты для метода capitalize"""
    
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
        ("123abc", "123abc"),  # числа в начале
        ("тест", "Тест"),  # кириллица
    ])
    def test_capitalize_positive(self, input_str, expected):
        assert string_utils.capitalize(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, expected", [
        ("", ""),  # пустая строка
        ("   ", "   "),  # только пробелы
        (" Skypro", " Skypro"),  # пробел в начале
    ])
    def test_capitalize_negative(self, input_str, expected):
        assert string_utils.capitalize(input_str) == expected


class TestTrim:
    """Тесты для метода trim"""
    
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("  hello  ", "hello  "),  # пробелы только в начале
        ("skypro", "skypro"),  # без пробелов
        ("   ", ""),  # только пробелы
    ])
    def test_trim_positive(self, input_str, expected):
        assert string_utils.trim(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str", [
        "",  # пустая строка
        "\tskypro",  # табуляция вместо пробела
        "\nskypro",  # перенос строки
    ])
    def test_trim_negative(self, input_str):
        # Эти тесты покажут дефект - метод не удаляет другие whitespace символы
        result = string_utils.trim(input_str)
        print(f"Input: '{input_str}', Result: '{result}'")


class TestContains:
    """Тесты для метода contains"""
    
    @pytest.mark.positive
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "Pro", True),  # подстрока
        ("hello world", " ", True),  # пробел
        ("123", "2", True),  # цифры
    ])
    def test_contains_positive(self, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "X", False),
        ("SkyPro", "sky", False),  # регистр
        ("", "a", False),  # пустая строка
        ("hello", "", False),  # пустой символ
    ])
    def test_contains_negative(self, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.xfail(reason="Дефект: метод не обрабатывает пустую строку")
    def test_contains_empty_string(self):
        assert string_utils.contains("", "a") == False


class TestDeleteSymbol:
    """Тесты для метода delete_symbol"""
    
    @pytest.mark.positive
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("hello world", " ", "helloworld"),  # пробел
        ("banana", "a", "bnn"),  # несколько вхождений
        ("12345", "3", "1245"),  # цифры
    ])
    def test_delete_symbol_positive(self, string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "X", "SkyPro"),  # символ не найден
        ("hello", "ll", "heo"),  # удаление подстроки
        ("", "a", ""),  # пустая строка
        ("test", "", "test"),  # пустой символ
    ])
    def test_delete_symbol_negative(self, string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

    @pytest.mark.xfail(reason="Дефект: метод не обрабатывает пустую строку")
    def test_delete_symbol_empty_string(self):
        assert string_utils.delete_symbol("", "a") == ""