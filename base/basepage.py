class BasePage:

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        self.driver = driver

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title

        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.driver.title
            return actual_title == title_to_verify
        except:
            return False
