from selenium import webdriver
import pdb

driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = "file:///Users/yanichik/Documents/0_Coding/Cameo/selenium/Present%20vs%20Displayed/present_vs_displayed.html"

driver.get(url)

btn1 = driver.find_element("id", "btn1")
btn1_text = btn1.text
print("first button text: {}".format(btn1_text))

btn2 = driver.find_element("id", "btn2")
btn2_text = btn2.text
print("second button text: {}".format(btn2_text))

btn3 = driver.find_element("id", "btn3")
btn3_text = btn3.text
print("third button text: {}".format(btn3_text))

btn4 = driver.find_element("id", "btn4")
btn4_text = btn4.text
print("fourth button text: {}".format(btn4_text))

pdb.set_trace()
