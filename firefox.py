from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get(" https://ya.ru/ ")
driver.get("https://vk.com/")
# driver.back()
# driver.forward()
# for x in range(1, 10):
# 	driver.back()
# 	driver.forward()
# 	driver.set_window_size(640, 460)
driver.maximize_window ()#открыть окно по размеру экрана
driver.minimize_window() #свернуть окно браузера
driver.fullscreen_window() #развернуть окно на весь экран, аналог F11
driver.save_screenshot("./ya.png")
sleep(10)