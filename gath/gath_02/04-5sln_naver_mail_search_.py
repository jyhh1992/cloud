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

chrome.get("https://www.naver.com/")
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.link_login"))) # 인터렉션을 할 수 있는 상태
print(login_button.text)
login_button.click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id"))) 
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw"))) 
#search.send_keys("아이폰 케이스\n")

#input_id.send_keys("id") # chapchar때문에 로그인이 안됨
#input_pw.send_keys("id") # chapchar때문에 로그인이 안됨

id ="자신의id"   
pw ="자신의pw" 
pyperclip.copy(id)
input_id.send_keys(Keys.CONTROL, "v")  # ctrl v 붙여넣기
pyperclip.copy(pw)
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

time.sleep(1)
# 페이지 내에 iframe이 있을 경우 
#chrome.switch_to.frame("iframe name")
chrome.switch_to.frame("minime")
mail = short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.user_info div.new_box a:nth-child(1)")))
#print(mail.text)
mail.click()
chrome.switch_to.default_content()

# selector의 속성 지정 방법
# a[class = "logout_button"]  
# a[class ^= "logout"]  # logout으로 시작
# a[class $= "button"]  # button으로 끝나는
# a[class *= "out_but"]  # out_but 문자열이 들어있는 

#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ol.mailList")))
titles = chrome.find_elements_by_css_selector("strong.mail_title")
print(titles)
for idx, title in enumerate(titles) :
    print("{} : {}".format(idx+1, title.text))
    time.sleep(1)

time.sleep(3)
chrome.close()