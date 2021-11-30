# 브라우저 드라이브 메니저로 크롬 드라이버 활용하기
# 사람이 하는 행동 로직을 그대로 재현해서 크롤이하는 방법
## input box에 키보드로 텍스트 입력하고 검색버튼 클릭, 또는 엔터 재현하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time  
import os

options = webdriver.ChromeOptions()             # 옵션 설정 객체 생성
options.add_argument("window-size=1000,1000")   # 브라우저 크기 설정(가로 x 세로)
options.add_argument("no-sandbox")              # 샌드박스 사용 안하겠다. 텝별로 분리하겠다. 거리를 두겠다
# options.add_argument("headless")              # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 
chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)

chrome.get("http://shopping.naver.com")
wait = WebDriverWait(chrome, 10) 

def find(wait, css_selector):
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# 사람이 하는 행동 로직을 그대로 재현해서 크롤이하는 방법
search = find(wait, "input[name=query]")

# 방법1: 버튼클릭
search.send_keys("아이폰 케이스")
button = find(wait, "a.co_srh_btn")
button.click()

# 방법2: 엔터(사용자 행위 생각해 보기)
search.send_keys("아이폰 케이스\n")

time.sleep(3)
chrome.close()