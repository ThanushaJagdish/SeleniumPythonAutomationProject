import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
username = driver.find_element(By.ID,"userEmail")
password = driver.find_element(By.ID,"userPassword")
username.send_keys("Abc@gmail.com")
password.send_keys("Abc@123")
driver.find_element(By.ID,"login").click()
time.sleep(2)
print(driver.current_url)