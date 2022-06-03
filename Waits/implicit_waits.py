from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(
    "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Waits/page_with_slow_image.html"
)

my_img = driver.find_element(By.TAG_NAME, "img")
print(my_img)
