import unittest
from pages.home.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("one_time_setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)

    def test_invalid_login(self):
        # self.lp.logout()
        # self.lp.login()

        assert self.lp.verify_if_login_failed() is True
        assert self.lp.verify_title() is True

    def test_valid_login(self):
        # self.lp.login()

        assert self.lp.verify_if_logged_in() is True
