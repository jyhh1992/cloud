# webdriver_manager 를 활용하여 크롬 드라이버 연결하기
## [usage : ]
## pip install webdriver-manager 설치 하기
## from webdriver_manager.chrome import ChromeDriverManager
## chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
###############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time  
import os

options = webdriver.ChromeOptions()             # 옵션 설정 객체 생성
options.add_argument("window-size=1000,1000")   # 브라우저 크기 설정(가로 x 세로)
options.add_argument("no-sandbox")              # 샌드박스 사용 안하겠다. 텝별로 분리하겠다. 거리를 두겠다
# options.add_argument("headless")              # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
chrome.get("http://daum.net")

#### 다양한 엘리먼트 얻는 방법
#chrome.find_element_by_css_selector()
#chrome.find_elements_by_css_selector()
#chrome.find_elements_by_class_name()
#chrome.find_element_by_class_name()
#chrome.find_element_by_id()
#chrome.find_elements_by_id()
elem = chrome.find_element_by_class_name("link_login")

elem = chrome.find_element_by_name("q")
chrome.find_element_by_id("q").clear()
elem.send_keys("사과")
elem.send_keys(Keys.ENTER)
chrome.find_element_by_id("daumBtnSearch").click()
elem.click()

items = chrome.find_elements_by_class_name("thumb_img")
for item in items:
    print(item.get_attribute("src"))

wait = WebDriverWait(chrome, 10) 
ele = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
print(ele)

chrome.back()
time.sleep(2)
chrome.forward()
time.sleep(2)
chrome.close()
#chrome.quit() # tab 모두 종료