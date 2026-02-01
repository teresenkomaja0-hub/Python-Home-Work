from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    driver.get("https://www.saucedemo.com/")
    #авторизоваться как пользователь
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

#"Для каждого item в списке товаров:..."
    for item in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]:
#«Икс-Пас» xpath — переменная, в которую сохраняется XPath (выражение для поиска элемента).
#
# f"..." — форматированная строка (f-string). Внутри вставляется значение переменной item.
#"//div[text()='{item}']" — ищет <div>, содержащий точный текст, равный текущему товару.
#"/ancestor::div[@class='inventory_item']" — ищет ближайшего предка <div>, у которого есть класс "inventory_item".
#"//button" — внутри этого предка ищет кнопку <button>.
        xpath = f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"
#"Ждём, пока кнопка, соответствующая нашему XPath, станет кликабельной, и затем нажимаем на неё."
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

#Перейдите в корзину.       
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

#Нажмите Checkout.
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

#Заполните форму своими данными:
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Maya")
    driver.find_element(By.ID, "last-name").send_keys("Tereshchenko")
    driver.find_element(By.ID, "postal-code").send_keys("199178")

#Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()
#Прочитайте со страницы итоговую стоимость 
    total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    assert "58.29" in total, f"Total не равен $58.29, получили {total}"
    driver.quit()