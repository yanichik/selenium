import pytest
import pdb
import time


@pytest.mark.usefixtures("init_driver")
class TestDummy:
    def test_dummy(self):
        print("I am dummy test line 1")
        print("I am dummy test line 2")
        self.driver.get("http://www.google.com")
        time.sleep(2)
        self.driver.quit()
