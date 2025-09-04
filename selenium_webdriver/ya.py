from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import os
options = Options()
options.add_argument('--log-level=3')
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Или через service аргументы
service = ChromeService(ChromeDriverManager().install())
service.creationflags = subprocess.CREATE_NO_WINDOW  # скрывает консоль
try:
    # Запуск браузера (ошибки будут подавлены)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    # Ваш код продолжается здесь...
    driver.get("http://uitestingplayground.com/classattr")
    print("✅ Страница загружена успешно!")
    
    
    
    time.sleep(2)
    
except Exception as e:
    print(f"❌ Произошла реальная ошибка: {e}")
    
finally:
    driver.quit()
    print("✅ Браузер закрыт")