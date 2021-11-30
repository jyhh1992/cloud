# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  

if __name__ == "__main__" :
    shop_search = input("원하는 검색 키워드 :")
    shop_page_num = int(input("페이지 수 :"))

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver_path = '/home/home/gath/chromedriver'
# chrome = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("http://shopping.naver.com")

search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys(shop_search)
time.sleep(1)
search.send_keys("\n")
short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class ^= basicList_info_area__")))

for i in range(shop_page_num):

    interval = 2

    # 현재 document의 높이 반환
    prey_height = chrome.execute_script("return document.body.scrollHeight ")

    while True:
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 스크롤을 현재 페이지 가장 아래로 내림
        time.sleep(interval)
        # 페이지 로딩 대기

        # 현재 문서 높이와 이전 높이가 같으면 페이지의 마지막이라고 판단함 반복문 탈출
        curr_height = chrome.execute_script("return document.body.scrollHeight")
        if curr_height == prey_height:
            break
        # 이전 높이 변경
        prey_height = curr_height
    print("스크롤 완료")

    next_page = chrome.find_element_by_css_selector("a[class ^= pagination_next__")
    next_page.click()

    time.sleep(5)

