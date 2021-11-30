from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome(ChromeDriverManager().install())
elem = chrome.find_element_by_class_name("link_login")
elem.click()
chrome.find_element_by_class_name("1btn_g").click()
chrome.back()
time.sleep(2)
chrome.forward()
chrome.get("https://naver.com")

# selector의 속성 지정 다양한 방법
# a[class = "logout_button"]
# a[class ^= "logout"]  # logout으로 시작
# a[class $= "button"]  # button으로 끝나는
# a[class *= "out_but"]  # out_but 문자열이 들어있는

chrome.close()