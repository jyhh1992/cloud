# selenium을 활용한 크롬 브라우저 제어하기
# http://naver.com 크롬 브라우저에 띄우기

from selenium import webdriver
import time
# selenium webdriver는 크롬 브라우저 버전 전용을 사용해야함.
# 실습path : /home/자신homeid/datagather/selenium/chromedriver

driver_path = "/home/rapa00/datagather/selenium/chromedriver"
chrome = webdriver.Chrome(driver_path)
chrome.get("http://naver.com")
time.sleep(3) # 단위 : sec
chrome.close()