import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://demostore.supersqa.com/"
driver.get(url)

# ex1: place holder
search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
placeholder = search_field.get_attribute("placeholder")
if placeholder != "Search products…":
    raise Exception("placeholder is wrong")
else:
    print("placeholder is accurate")

# ex2: see which tab is selected
nav_menu = driver.find_element(By.CLASS_NAME, "nav-menu")
selected_menu_options = nav_menu.find_elements(By.TAG_NAME, "li")
for menu in selected_menu_options:
    my_class = menu.get_attribute("class")
    if "current_page_item" in my_class:
        print(menu.text)

# ex3: get link url
product_link = driver.find_element("css selector", "li.product a")
product_url = product_link.get_attribute("href")
print(product_url)

pdb.set_trace()
