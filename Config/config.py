import os

from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "../Driver/chromedriver.exe"

    BASE_URL = "https://www.thetadrop.com/?m=login"
    HomePage_URL = "https://www.thetadrop.com/"
    email = os.environ.get('email')
    password = os.environ.get('thetapass')
    Login_page_title = "Home - THETA Drop"
    # Search_page_title = "NFT▵PRIDE's Collection | Binance NFT"
    Home_page_title = "Home - THETA Drop"
