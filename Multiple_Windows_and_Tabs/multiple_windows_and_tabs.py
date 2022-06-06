from selenium import webdriver
import pdb

driver = webdriver.Chrome()

driver.get(
    "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Multiple_Windows_and_Tabs/windows-and_tabs_example.html"
)

driver.find_element("xpath", '//*[@id="windows"]/a[1]').click()
pdb.set_trace()
# my_heading = driver.find_element('xpath', '/html/body/h1').text
print("Before switching focus: " + driver.title)
# original_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles
original_window_handle = all_window_handles[0]
new_window = all_window_handles[1]
driver.switch_to.window(new_window)
print("After switching focus: " + driver.title)
print("Closing tab")
driver.close()
print("Switching back to original")
driver.switch_to.window(original_window_handle)
# import pdb

# pdb.set_trace()
