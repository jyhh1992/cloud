from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import os

def search_selenium(search_name_, base_path) :
    # os.makedirs(sub_dir) # Execution path
    try:
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            
    except OSError as e:
        print("exist directory " + search_name_ )
        if e.errno != e.EXIST:
            print("error : {} ".format(e))

search_name = input("검색하고싶은 키워드 : ")
search_limit = int(input("검색 갯수 입력 : "))
search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get(search_url)
chrome.implicitly_wait(2)

image_count = len(chrome.find_elements_by_tag_name("img"))
print("로드된 이미지 갯수 : ",image_count)

search_path = os.path.dirname(os.path.realpath(__file__)) + "/" +search_name + "/"
search_selenium(search_name, search_path)

for i in range(search_limit):
    image =chrome.find_elements_by_tag_name("img")[i]
    image.screenshot(search_path+search_name+str(i)+".png")

chrome.close()