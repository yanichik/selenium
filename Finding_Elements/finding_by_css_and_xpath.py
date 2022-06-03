from math import prod
from turtle import pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")

# product_search = driver.find_element(
#     By.CSS_SELECTOR, "#woocommerce-product-search-field-0"
# )
product_search = driver.find_element(
    By.XPATH, "/html/body/div[2]/header/div[1]/div[2]/div/form/input[1]"
)

product_search.send_keys("woo")
product_search.submit()
pdb.set_trace()
