from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
# WebDriverWait object on the driver for 5 seconds
wait = WebDriverWait(driver, 5)
# driver.implicitly_wait(5)
url = "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Present%20vs%20Displayed/present_vs_visible_with_cars.html"

driver.get(url)

# click on toyota radio button
# driver.find_element(By.CSS_SELECTOR, "#toyota").click()

# click on avalon checkbox BEFORE toyota radio clicked, so avalon not visible
# driver.find_element(
#     By.CSS_SELECTOR, "#toyota-models > input[type=checkbox]:nth-child(7)"
# ).click()

avalon = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#toyota-models > input[type=checkbox]:nth-child(7)")
    )
).click()
