from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

driver_path = "/home/ubuntu/gath/chromedriver"
chrome = webdriver.Chrome(driver_path, options=options)
chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com")
chrome.back()
time.sleep(2)
chrome.forward()
time.sleep(2)
chrome.close()