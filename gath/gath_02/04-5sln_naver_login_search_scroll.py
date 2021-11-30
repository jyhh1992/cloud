# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  
import os
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("http://shopping.naver.com")
#login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) # 인터렉션을 할 수 있는 상태
print(login_button.text)
login_button.click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id"))) 
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw"))) 
#search.send_keys("아이폰 케이스\n")

#input_id.send_keys("id") # chapchar때문에 로그인이 안됨
#input_pw.send_keys("pw") # chapchar때문에 로그인이 안됨

id="자신의id"
pw="자신의pw"

pyperclip.copy(id)
input_id.send_keys(Keys.CONTROL, "v")  # ctrl v 붙여넣기
pyperclip.copy(pw)
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

# 잘못입력해 에러난 상태 확인
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button"))) 

# def find(wait, css_selector):
#    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
# logout 버튼 숨어 있음.
search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("아이폰 케이스")
time.sleep(1)
search.send_keys("\n")

# selector의 속성 지정 방법
# a[class = "logout_button"]  
# a[class ^= "logout"]  # logout으로 시작
# a[class $= "button"]  # button으로 끝나는
# a[class *= "out_but"]  # out_but 문자열이 들어있는 

# div 태그의 class의 속성 값이 basicList_link__로 시작하는 것 가져오기
short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class ^= basicList_info_area__")))

## 무한 스크롤, js를 selenium이 실행
# console js :window.scrollBy(0, 1000)
# chrome.execute_script("window.scrollBy(0, 10000)")
# 문서의 최대 길이로 반환, 스크롤을 내렸을 때 스크롤 길이가 달라짐
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)") 
for i in range(8):
    chrome.execute_script("window.scrollBy(0, " + str((i+1) * 1000) + ")") 
    time.sleep(1) # laoding 할때까지 좀 기다려줌

items = chrome.find_elements_by_css_selector("div[class ^= basicList_info_area__")

for item in items :
    # 광고 걸러내기
    try:
        item.find_element_by_css_selector("button[class ^= ad_")
        continue
    except:
        pass
    print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)

time.sleep(3)
chrome.close()