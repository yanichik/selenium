import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Dropdowns/drop_down_example.html"

driver.get(url)

select_dropdown = driver.find_element("id", "age-range-select")
dropdown_object = Select(select_dropdown)
pdb.set_trace()
