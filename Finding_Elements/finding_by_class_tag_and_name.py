from itertools import product
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com")

# finding by class name
product = driver.find_element(By.CLASS_NAME, "product")
products = driver.find_elements(By.CLASS_NAME, "product")

print(product)
print("__________________________")
print(products)

# finding by class tag
order_by = driver.find_element(By.NAME, "orderby")
