# 구글 검색으로 이미지 검색하여 원하는 갯수만큼 이미지 자동으로 다운 받기
# 현재 위치의 절대경로 값 리터받아서 chromedriver path 설정
## 현대 디렉토리의 절대 경로값 리터받아서 chromedriver path 설정
# 키보드로 검색키워드와 갯수 입력 받음
# 검색 키워드로 폴더 생성, 지정한 갯수 만큼 이미지 파일 다운로드
## 외부 라이브러리 import 하기(파일 저장을 위한 디렉토리 만들리 파일)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
import os
import create_dir_
def search_selenium(search_name, search_path, search_limit) :
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    
    # webdriver option 설정
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1000,1000")
    options.add_argument("no-sandbox") 
    options.add_argument("headless")  # 크롬 창을 안뜨게함.
    
    browser = webdriver.Chrome(ChromeDriverManager().install())  # 시스템의 chrome browser에 맞는 driver 설정
    browser.get(search_url)
    browser.implicitly_wait(2)   # 응답을 위한 잠시 대기
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    print("로드된 이미지 개수 : ", image_count)

    create_dir_.search_selenium(search_name, search_path)

    for i in range( search_limit ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot(search_path + search_name + str(i) + ".png")

    browser.close()

if __name__ == "__main__" :
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    #search_path = os.path.realpath(__file__)  # 현재 파일의 실제 경로 리턴
    #search_path = os.path.dirname(os.path.realpath(__file__))  # 현재 파일의 절대경로 값 리턴
    search_path = os.path.dirname(os.path.realpath(__file__)) + "/" + search_name + "/"
    #print(search_path)    
    search_selenium(search_name, search_path, search_limit)