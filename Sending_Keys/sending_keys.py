import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "http://demostore.supersqa.com/my-account/"
driver.get(url)

# send text to fields
uname = driver.find_element(By.NAME, "username")
pw = driver.find_element(By.NAME, "password")
login = driver.find_element(By.NAME, "login")
uname.send_keys("myUserName")
pw.send_keys("myPassword")
login.click()
# time.sleep(3)
# driver.back()
# time.sleep(3)

# send non-text keys from keyboard
url = "http://demostore.supersqa.com/"
driver.get(url)
search_field = driver.find_element("name", "s")
search_field.send_keys(Keys.ADD)
search_field.send_keys(Keys.DECIMAL)
search_field.send_keys(Keys.EQUALS)
search_field.send_keys(Keys.SEMICOLON)
