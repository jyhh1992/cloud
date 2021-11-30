# naver shopping 아이폰 케이스 검색
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time  
import os

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
chrome.get("http://shopping.naver.com")
wait = WebDriverWait(chrome, 10) 

def find(wait, css_selector):
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

# 사람이 하는 행동 로직을 그대로 재현해서 크롤이하는 방법
search = find(wait, "input[name=query]")
search.send_keys("아이폰 케이스\n")   # \n : new line

#time.sleep(3)
#chrome.close()