import unittest
from pages.home.login_page import LoginPage
from pages.sizings.sizing_page import SizingPage
from utilities.util import Util
import pytest


@pytest.mark.usefixtures("one_time_setup")
class SizingTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.sizing = SizingPage(self.driver)

    def test_create_sizing(self):
        _random_sizing_number = Util.generate_random_number()
        self.sizing.add_new_sizing(f"test by selenium {_random_sizing_number}", "Shirts")
        assert self.sizing.verify_if_sizing_is_created(f"test by selenium {_random_sizing_number}") == True
