# 키보드로 검색 키워드를 입력받는다.
# 현재 디렉토리에 검색 키워드의 폴더를 생성한다.

import os

def search_selenium(search_name, base_path) :
    # os.makedirs(sub_dir) # Execution path
    try:
        if not os.path.exists(base_path):
            os.makedirs(base_path)

    except OSError as e:
        print("exist directory " + search_name )
        if e.errno != e.EXIST:
            print("error : {} ".format(e))

if __name__ == "__main__" :
    search_name = input("검색하고 싶은 키워드 : ")
    base_path = os.path.dirname(os.path.realpath(__file__)) + "/" + search_name + "/"
    print(base_path)    
    search_selenium(search_name, base_path)