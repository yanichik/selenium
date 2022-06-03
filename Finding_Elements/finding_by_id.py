from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")

# cart = driver.find_element(By.ID, "site-header-cart")
# cart.click()

# driver.get("http://demostore.supersqa.com/my-account")
pdb.set_trace()
