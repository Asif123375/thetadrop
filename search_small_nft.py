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
buying_limits = 5
buying_speed = 4

# TODO: You need to put your NFT link here
NFT_link = "https://thetatv.thetadrop.com/marketplace"

# TODO : fixed url path and test in Trven Device
driver = webdriver.Chrome(r"../thetadrop/chromedriver.exe", chrome_options=chrome_options)


driver.get(NFT_link)

driver.implicitly_wait(10)
clean_filter_xpath = "//div[@class='clear-filters']"
clean_filter_elements = driver.find_element_by_xpath(clean_filter_xpath)
clean_filter_elements.click()

driver.implicitly_wait(10)
filter_xpath = "//select[@name='sort']"
filter_elements = driver.find_element_by_xpath(filter_xpath)
filter_elements.click()

print(input(".. :"))

driver.implicitly_wait(10)
price_value_xpath = "//strong[@class='price-value']"
price_value_elements = driver.find_elements_by_xpath(price_value_xpath)

for i in price_value_elements:
    print(i)
    print(i.text)
    print(i.text)
    print(input(".. :"))
# filter_elements[0].click()

print(input(".. :"))