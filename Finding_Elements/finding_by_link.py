from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com")

cart_el = driver.find_element(By.LINK_TEXT, "Cart")
print(cart_el.text)

accnt_el = driver.find_element(By.PARTIAL_LINK_TEXT, "acc")
print(accnt_el.text)
