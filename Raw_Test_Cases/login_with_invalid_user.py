from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLoginError:
    url = "http://demostore.supersqa.com/my-account/"
    invalid_email = "abc@gmail.com"
    invalid_user_expected_msg = (
        "Unknown email address. Check again or try your username."
    )

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, "username")
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, "password")
        field.send_keys("abcdefghij")

    def login(self):
        self.driver.find_element(By.NAME, "login").click()

    def verify_error_msg(self):
        error_text = self.driver.find_element(
            By.XPATH, "/html/body/div/div[2]/div/div[1]/ul"
        ).text
        # if error_text != self.invalid_user_expected_msg:
        #     raise Exception("Invalid user message not as expected.")
        # else:
        #     print("Pass!")
        assert (
            self.invalid_user_expected_msg == error_text
        ), "Invalid user message not as expected."
        print("Pass!")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.login()
        self.verify_error_msg()


if __name__ == "__main__":
    obj = InvalidUserLoginError()
    obj.main()
