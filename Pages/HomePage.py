from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    LogIn_Button = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HomePage_URL)

    def get_homepage_title(self, title):
        return self.get_title(title)

    def do_click_Login_button(self):
        self.do_click(self.LogIn_Button)