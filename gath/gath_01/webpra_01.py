from selenium import webdriver
import time
driver_path = "/home/ubuntu/gath/chromedriver"
chrome =  webdriver.Chrome(driver_path)
print("aaa")
chrome.get("http://naver.com")
time.sleep(3)
chrome.close()