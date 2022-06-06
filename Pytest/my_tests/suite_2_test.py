import pytest


@pytest.mark.guest
class TestCheckout:
    def test_checkout_as_guest(self):
        print("")
        print("checkout guest")

    def test_checkout_existing_user(self):
        # print("")
        print("checkout existing user")
