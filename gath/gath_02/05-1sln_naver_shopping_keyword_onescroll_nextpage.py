# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.

driver_path = '/home/rapa00/datagather/seleniumv2/chromedriver'
chrome = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("http://shopping.naver.com")

# 사용자로부터 페이지 수를 입력받음
# 입력 받은 페이지 만큼 스크롤하여 아이템의 목록을 가져옴
# 페이지 구분 시켜서 콘솔에 출력하기
# 반복 되는 코드를 함수로 정의 하기


def search_keyword(key_word):
    search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
    #search.send_keys("아이폰 케이스")
    search.send_keys(key_word)
    time.sleep(1)
    search.send_keys("\n")
    # div 태그의 class의 속성 값이 basicList_link__로 시작하는 것 가져오기
    short_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class ^= basicList_info_area__")))

def page_load():
# 화면 가장 아래로 스크롤 내리기
    interval = 2
    chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 현재 document의 높이 반환
    prev_height = chrome.execute_script("return document.body.scrollHeight")

    while True:
        # 스크롤을 현재 페이지 가장 아래로 내림
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # 페이지 로딩 대기
        time.sleep(interval)
        # 현재 문서 높이를 가져와서 저장
        curr_height = chrome.execute_script("return document.body.scrollHeight")

        if curr_height == prev_height:
            break
        # 이전 높이 변경
        prev_height = curr_height
    print("스크롤 완료")

def gather_items():
    # 아이템들 모두 추출하기
    items = chrome.find_elements_by_css_selector("div[class ^= basicList_info_area__")

    for item in items :
        # 광고 걸러내기
        try:
            item.find_element_by_css_selector("button[class ^= ad_")
            continue
        except:
            pass
        # 광고 아닌것만 프린트
        print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)

    time.sleep(1)
    #next 페이지 이동 클래스 : pagination_next__1ITTf
    next_page = chrome.find_element_by_css_selector("a[class ^= pagination_next__")
    next_page.click()
    time.sleep(1)

if __name__ == "__main__" :
    key_word = input("검색할 키워드를 입력해 주세요. : ")
    order_page = int(input("몇개의 페이지를 스크래핑 할까요? :"))
    page_num = 1
    search_keyword(key_word)

    # 페이지 스크롤 1번 수행 해도 됨
    page_load()

    while page_num <= order_page:
        print("-"*30)
        gather_items()
        page_num += 1

#chrome.quit()