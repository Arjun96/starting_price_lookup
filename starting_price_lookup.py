from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Setting Chrome to run Headless
chrome_options = Options()
chrome_options.headless = True

#Started chromedriver and navigated to Bell's smartphone paage
driver=webdriver.Chrome('/Users/luthraar/Downloads/chromedriver', options = chrome_options)
driver.get('https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices')