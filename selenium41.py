from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Page Title:", driver.title)

time.sleep(5)

driver.quit()