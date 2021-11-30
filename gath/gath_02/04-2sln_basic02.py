# chromdriver 절대경로 설정 : os.path.abspath() 활용해서 설정하기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  
import os
options = webdriver.ChromeOptions()             # 옵션 설정 객체 생성
options.add_argument("window-size=1000,1000")   # 브라우저 크기 설정(가로 x 세로)
options.add_argument("no-sandbox")              # 샌드박스 사용 안하겠다. 텝별로 분리하겠다. 거리를 두겠다
# options.add_argument("headless")              # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 

this_dir = os.path.dirname(os.path.abspath(__file__)) # 현재 위치의 절대 경로 값
chrome_path = this_dir + '/chromedriver'

chrome = webdriver.Chrome(chrome_path, options=options)
chrome.get("http://naver.com")

#OnLoading 될 때까지 기다리기는 방법
time.sleep(3) # 간단한 delay, 파이썬 라이브러리
chrome.close()