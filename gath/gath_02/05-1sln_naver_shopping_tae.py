# input box에 텍스트 입력하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time  

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox") 
# options.add_argument("headless")  # 크롬 창을 안뜨게함.
options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver_path = './driver/chromedriver'
# chrome = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(chrome, 10) 
short_wait = WebDriverWait(chrome, 3) 

chrome.get("http://shopping.naver.com")

# search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
# search.send_keys("아이폰 케이스")
# time.sleep(1)
# search.send_keys("\n")

interval = 2

# prev_height =chrome.execute_script("return document.body.scrollHeight")

def downScroll():
    prev_height =chrome.execute_script("return document.body.scrollHeight")
    while True:
        # 스크롤을 현재 페이지 가장 아래로 내림
        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 페이지 로딩 대기
        time.sleep(interval)
        # 현재 문서 높이를 가져와서 저장
        curr_height = chrome.execute_script("return document.body.scrollHeight")
        # 현재 높이와 이전 높이가 같으면 페이지의 마지막이라고 판단함. 반복문 탈출
        if curr_height == prev_height:
            break
        # 이전 높이 변경
        prev_height = curr_height

    print("스크롤 완료")

def scraping():
    items = chrome.find_elements_by_css_selector("div[class ^= basicList_info_area__")

    for item in items :
        # 광고 걸러내기
        try:
            item.find_element_by_css_selector("button[class ^= ad_")
            continue
        except:
            pass

        print(item.find_element_by_css_selector("a[class ^= basicList_link__]").text)


def crawling():
    search_word = input("검색할 단어를 입력해주세요 : ")
    page = int(input("스크래핑 할 페이지 수를 입력해주세요 : "))
    search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
    search.send_keys(search_word)
    time.sleep(1)
    search.send_keys("\n")

    i = 0
    while i < page:
        downScroll()
        time.sleep(1)
        print("-"*80)

        scraping()
        time.sleep(1)
        print(f"{i+1:>2d} 페이지 완료")
        print("-"*80)

        if (i+1) == page:
            break

        next_page = chrome.find_element_by_css_selector("a.pagination_next__1ITTf")
        next_page.click()
        i += 1

if __name__ == "__main__":
    crawling()