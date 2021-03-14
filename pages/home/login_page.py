from selenium.webdriver.common.by import By
from base.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _dashboard_text = "//h2[text()='Dashboard']"
    _login_failed_info = "//div[contains(text(),'Invalid Email or password.')]"

    def get_email_field(self):
        return self.driver.find_element(By.ID, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self._password_field)

    def get_login_button(self):
        return self.driver.find_element(By.NAME, self._login_button)

    def enter_username(self, username):
        self.get_email_field().send_keys(username)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def clear_fields(self):
        self.get_email_field().clear()
        self.get_password_field().clear()

    def verify_if_logged_in(self):
        if self.driver.find_element(By.XPATH, self._dashboard_text) is not None:
            return True
        return False

    def verify_if_login_failed(self):
        if self.driver.find_element(By.XPATH, self._login_failed_info) is not None:
            return True
        return False

    def login(self, username="", password=""):
        self.clear_fields()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_title(self):
        return self.verify_page_title("SizingApp")
