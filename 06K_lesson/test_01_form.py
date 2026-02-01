from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    for field, value in data.items():
        elem = wait.until(EC.presence_of_element_located((By.NAME, field)))
        elem.clear()
        elem.send_keys(value)

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-outline-primary"))).click()

    zip_elem = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_elem.get_attribute("class")

    for field in data:
        if field != "zip-code":
            el = driver.find_element(By.ID, field)
            assert "alert-success" in el.get_attribute("class")
    driver.quit()