from selenium.webdriver.common.by import By
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select


class SizingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _sizing_link = "//a[contains(@href,'sizings')]"
    _add_new_sizing_button = "//a[contains(@href,'sizings/new')]"
    _new_sizing_name = "sizing_name"
    _category_selector = "sizing_category_id"
    _save_button = "commit"

    def enter_sizing_page(self):
        self.driver.find_element(By.XPATH, self._sizing_link).click()

    def click_add_new_sizing(self):
        self.driver.find_element(By.XPATH, self._add_new_sizing_button).click()

    def enter_name_of_sizing(self, name):
        self.driver.find_element(By.ID, self._new_sizing_name).send_keys(name)

    def select_category(self, category):
        select = Select(self.driver.find_element(By.ID, self._category_selector))
        select.select_by_visible_text(category)

    def go_to_next_step(self):
        self.driver.find_element(By.NAME, self._save_button).click()

    def add_new_sizing(self, name, category):
        self.enter_sizing_page()
        self.click_add_new_sizing()
        self.enter_name_of_sizing(name)
        self.select_category(category)
        self.go_to_next_step()

    def verify_if_sizing_is_created(self, name):
        element = self.driver.find_element(By.XPATH, f"//h3[text()='{name}']")
        if element is not None:
            return True
        return False
