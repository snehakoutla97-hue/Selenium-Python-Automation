from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://saucedemo.com")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
print("Login and Add to Cart Test Passed Sucessfully!")
time.sleep(4)
driver.quit()
