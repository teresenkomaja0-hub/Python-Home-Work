from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait = WebDriverWait(driver, 50)

delay_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
delay_input.clear()
delay_input.send_keys("45")

result_element = wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#result"), "15")
        )


driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

initial_text = driver.find_element(By.CLASS_NAME, "screen").text

result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), 
                "15"
            ))

final_result = driver.find_element(By.CLASS_NAME, "screen").text

assert final_result == "15", f"Ожидался результат '15', но получено '{final_result}'"


driver.quit()