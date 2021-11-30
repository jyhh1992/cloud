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

# 현재 document의 높이 반환


print("스크롤 완료")
time.sleep(1)
#chrome.close()
#chrome.quit()

# https://play.google.com/store/movies 할인정보 검색하기

from bs4 import BeautifulSoup as bs

# selenium chrome 드라이버로 받은 결과를 beautifulsoup에 전달하여 html 문서로 파싱
soup = bs(chrome.page_source, "html.parser")
# print(soup)
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

# for movie in movies:

# tds = soup.select("div.RZEgze")
# data_list= []
# for i in tds:
#     temp = []
#     if len(i.select('div.b8cIId.ReQCgd.Q9MA7b'))== 0:
#         continue
#     i1= i.select("div.b8cIId.ReQCgd.Q9MA7b")[0].get_text(strip=True)
#     i2= i.select('span.VfPpfd.ZdBevf.i5DZme')[0].get_text(strip=True)
#     # i3= i.select('span.SUZt4c.djCuy')[0].get_text(strip=True)
#     temp.append(i1)
#     temp.append(i2)
#     # temp.append(i3)
#     data_list.append(temp)

# print(data_list)

# print(f"제목 : {title}")
# print(f"할인 전 가격 : {title}")
# print(f"할인 후 가격 : {title}")
# print("링크: ","https://play.google.com/ "+link)
# print("*"*100)