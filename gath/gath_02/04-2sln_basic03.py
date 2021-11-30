# 브라우저 결과가 모두 로딩될 때까지 기다리는 다양한 방법 살펴보기

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

# chrome.get()은 페이이지의 화면이 로딩(html, css) 될때까지 기다림.(모든 데이터, js가 로딩될때까지 기다리지 않음.)
# body부분이 모두 loading 되는 시점, OnLoading 될 때까지 기다리기는 방법
#1. time.sleep(3) # 간단한 delay, 파이썬 라이브러리, 모든 경우를 커버하지 못함.
#2. chrome.implicitly_wait(3)  # 크롬드라이브와 통신하는 지점에서 delay, 모든 경우를 커버하지 못함.
#3. WebDriverWait, expected_conditions로 원하는 요소가 로딩될때까지 스마트하게 기다림(delay)
###(By.CSS_SELECTOR, "input[name=query]") 반드시 튜플로 들어가야함., WebDriverWait(chrome, 10) : 최대 10초 기다림
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]"))) 

chrome.close()