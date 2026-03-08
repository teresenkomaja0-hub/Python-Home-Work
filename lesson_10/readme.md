**Информация по работе с проектом**

1. Откройте терминал и подключите Allure: **pip install allure-pytest**

2. Запустите тесты и укажите путь к каталогу результатов тестирования:

**pytest --alluredir allure-result**

или

**python -m pytest --alluredir allure-result**

В директории с тестами появится папка allure-result. Там сохранятся отчеты о тестах.

3. Чтобы терминал распознал команду allure, установите Allure Report:

Пользователи Windows: запустите в терминале VS Code команду

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

Затем команду

**scoop install allure**

4. Команда **allure serve allure-result** запускает Allure и конвертирует результаты теста в отчет.

