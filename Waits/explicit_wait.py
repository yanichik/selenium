from cgitb import text
from socket import timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Waits/page_with_slow_image.html"
)

# my_img = driver.find_element(By.TAG_NAME, "img")
my_img = WebDriverWait(driver, 3).until(
    EC.visibility_of_all_elements_located((By.TAG_NAME, "img")),
    message=f"Image not found in 3 seconds",
)
print("found image")
