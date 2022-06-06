from selenium import webdriver
from selenium.webdriver.common.by import By
import random, string

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/my-account/")

reg_email_id = "reg_email"
reg_password_id = "reg_password"
btn_register_class = "woocommerce-form-register__submit"

reg_email_field = driver.find_element(By.ID, reg_email_id)
reg_password_field = driver.find_element(By.ID, reg_password_id)
reg_submit_btn = driver.find_element(By.CLASS_NAME, btn_register_class)

rand_email = "".join(random.choices(string.ascii_lowercase, k=7)) + "@gmails.com"
password = "Test1234567!"

reg_email_field.send_keys(rand_email)
reg_password_field.send_keys(password)
reg_submit_btn.click()

# verify registration success - find logout button
logout_btn = driver.find_element(
    By.CSS_SELECTOR,
    "#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a",
)

if logout_btn.is_displayed:
    print("Pass!")
else:
    print("Fail")
