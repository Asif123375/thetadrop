import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# Setting the chrome_options
global chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

# TODO: How much you want to buy
buying_price = 200

# TODO: You need to put your NFT link here
NFT_link = "https://thetatv.thetadrop.com/marketplace"

# TODO : fixed url path and test in Trven Device
driver = webdriver.Chrome(r"../thetadrop/chromedriver.exe", chrome_options=chrome_options)

driver.get(NFT_link)

print(input("Start Scripts.. :"))

# driver.implicitly_wait(10)
# clean_filter_xpath = "//div[@class='clear-filters']"
# clean_filter_elements = driver.find_element_by_xpath(clean_filter_xpath)
# clean_filter_elements.click()

# driver.implicitly_wait(10)
# filter_xpath = "//select[@name='sort']"
# filter_elements = driver.find_element_by_xpath(filter_xpath)
# filter_elements.click()


def nft_search(price_xpath, buy_xpath):
    for i in range(100):
        driver.get(NFT_link)
        driver.implicitly_wait(10)
        # price_value_xpath = "//strong[@class='price-value']"
        price_value_elements = driver.find_elements_by_xpath(price_xpath)
        # price_value_elements = elements
        for i in price_value_elements:
            nft_price = i.text
            print(nft_price)
            new_nft_price = nft_price.replace("$", "")
            if float(new_nft_price) < float(buying_price):
                i.click()

                buy_xpath = "//button[normalize-space()='Buy']"
                deposit_elements = driver.find_element_by_xpath(buy_xpath)
                deposit_elements.click()

                time.sleep(8)
                break
            else:
                print(f"price is biggest than {buying_price}")
            time.sleep(2)


price_value_xpath = "//strong[@class='price-value']"


nft_search(price_value_xpath)

print(input("Element End .. :"))
