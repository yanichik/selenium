from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://demostore.supersqa.com/"
driver.get(url)
