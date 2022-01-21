from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    Email = (By.XPATH, "//input[@placeholder='email or username']")
    Password = (By.XPATH, "//input[@placeholder='password']")
    Captcha = (By.CSS_SELECTOR, "div[class='recaptcha-checkbox-checkmark']")
    LoginButton = (By.XPATH, "//div[@class='modal-actions row']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        # self.do_click(self.Captcha)
        # print("Fill the Captcha")
        self.do_click(self.LoginButton)



