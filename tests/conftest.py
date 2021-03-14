import pytest
from selenium import webdriver

from pages.home.login_page import LoginPage


@pytest.fixture(scope="class")
def one_time_setup(request):
    BASEURL = "https://app.sizeme.ai/"
    driver = webdriver.Chrome(executable_path=r"drivers\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(BASEURL)
    lp = LoginPage(driver)
    lp.login("uvc52155@cuoly.com", "uvc52155")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()