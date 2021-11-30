# https://play.google.com/store/movies 할인정보 검색
# selenium과 beautifulsoup 연동한 크롤링 실습

#### 동적 페이지 스크롤

from selenium import webdriver
import time  

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument("no-sandbox") 
#options.add_argument('headless')

driver_path = "/home/ubuntu/gath/chromedriver"
chrome = webdriver.Chrome(driver_path, options=options)

# 페이지 이동
url =  "https://play.google.com/store/movies/top"
chrome.get(url)

# 지정한 위치로 스크롤 내리기
# 1920 x 1080 (해당도 위치로  스크롤)
# chrome.execute_script("window.scrollTo(0, 1080)")   #1920* 1080(x, y)
# chrome.execute_script("window.scrollTo(0, 2080)")   #1920* 1080
# chrome.execute_script("window.scrollTo(0, 0)")   #1920* 1080

# 화면 가장 아래로 스크롤 내리기
interval = 2
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 현재 document의 높이 반환


print("스크롤 완료")
time.sleep(1)
#chrome.close()
#chrome.quit()

# https://play.google.com/store/movies 할인정보 검색하기

from bs4 import BeautifulSoup as bs

# selenium chrome 드라이버로 받은 결과를 beautifulsoup에 전달하여 html 문서로 파싱
soup = bs(chrome.page_source, "html.parser")
print(soup)
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))


