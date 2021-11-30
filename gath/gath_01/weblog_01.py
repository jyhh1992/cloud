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
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3)

chrome.get("http://daum.net")
login_button = wait.untill(EC.visibility_of_element_located((By.CSS_SELECTOR,"a#gnb_login_button")))
login_button.click()
input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

input_id.send_keys("jyhh1992")
input_pw.send_keys("")

# selector의 속성 지정 다양한 방법
# a[class = "logout_button"]
# a[class ^= "logout"]  # logout으로 시작
# a[class $= "button"]  # button으로 끝나는
# a[class *= "out_but"]  # out_but 문자열이 들어있는

#time.sleep(3)
#chrome.close()