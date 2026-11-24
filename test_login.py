from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://saucedemo.com")
print("page Title is:",driver.title)
time.sleep(5)
driver.quit()
