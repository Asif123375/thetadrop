from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import Basetest


class Test_HomePage(Basetest):
    def test_home_page_title(self):
        print("test_home_page_title")
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_homepage_title(TestData.Home_page_title)
        assert title == TestData.Home_page_title

    def test_loginButton(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click_Login_button()