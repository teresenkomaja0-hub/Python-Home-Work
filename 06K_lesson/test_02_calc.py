from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_calc_slow():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    wait = WebDriverWait(driver, 60)
    delay = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay.clear()
    delay.send_keys("45")
    for val in ["7", "+", "8", "="]:
        wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{val}']"))).click()
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert driver.find_element(By.CLASS_NAME, "screen").text == "15"
    driver.quit()