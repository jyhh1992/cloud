import requests as req
import re
import datetime
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
import pymongo
# 몽고DB 서버 연결
username = 'rapa00' #username 넣으시오
password = '1234' #password 넣으시오
conn = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
print(conn)

mongodb = conn.cine21
actor_collection = mongodb.actor_collection #collection object creation
# actor 정보가 있는지 확인하기
actor_list = actor_collection.find()
for actor in actor_list:
    print(actor['actor'])

def lookupAndInsertDB(pastPeriod, pages=1):
    origin_url = 'http://www.cine21.com'
    # request url
    cine21_url = 'http://www.cine21.com/rank/person/content'
    month = pastPeriod #"2019-11"
    for page in range(pages+1):
        # post 방식으로 데이터를 가져오기 위한 request 시 필요 정보로서 브라우저 개발자 모드 network 탭의 form 정보.
        conditions = dict()
        conditions['section'] = 'actor'
        conditions['period_start'] = month
        conditions['gender'] = 'all'
        conditions['page'] = page


        # post 방식으로 request 요청
        response = req.post(cine21_url, data = conditions)
        print(response)
        soup=bs(response.content.decode('utf-8'), 'html.parser')
        # soup=bs(response.content, 'html.parser')
        print(type(soup))
        actorsInfoList =list()
        name_hitnum_movie_grade_infos = soup.select('li.people_li')
        print(type(name_hitnum_movie_grade_infos))
        # print(name_hitnum_movie_grade_infos)
        for info in name_hitnum_movie_grade_infos:
            # print(info)
            # print(info.select_one('div.name>a').text)
            name = re.sub("\(\w+\)", "", info.select_one('div.name>a').get_text(strip=True))
            print(name)#배우 이름
            appearanceNum = re.sub(".*?\(|\)", "", info.select_one('div.name>a').get_text(strip=True))
            print(appearanceNum)#기간내 출연건수
            hitIndex = info.select_one('ul.num_info strong').text
            print(hitIndex)#흥행지수
            hitMoviesAfter=info.select('ul.mov_list span')#기간내 대표적 출연영화들
            hitMovieAfterList = []
            for hitMovieAfter in hitMoviesAfter:
                # print(hitMovieAfter.text)
                hitMovieAfterList.append(hitMovieAfter.text)
            print(hitMovieAfterList)#기간내 대표적 출연영화들 리스트
            grade = info.select_one('span.grade').text
            print(grade)#기간내 순위
            # print(info.select_one('div.name>a')['href'])
            url_link = origin_url+info.select_one('div.name>a').attrs['href'] #배우의 상세정보 페이지 링크
            # print(url_link) #배우의 상세 정보 url
            res = req.get(url_link)
            soup_actor= bs(res.content, 'html.parser')
            print('*'*100)
            
            default_infos = soup_actor.select_one('ul.default_info')#리스르로서 내부에 원소 하나만 있음
            print('type(default_infos):',type(default_infos))
            # defaultInfosList =[]
            # print(default_infos)
            actor_dict = {} #배우 기본 정보
            for info in default_infos.select('li'):
                print('info:',info)
                detail_key = info.select_one('span.tit').get_text(strip=True)
                detail_value = re.sub('<span.*?>.*<\/span>','', str(info))
                detail_value = re.sub('<.*?>','',detail_value)
                print('key : ', detail_key, ',value : ', detail_value)
                actor_dict[detail_key]=detail_value
            ret =actor_collection.insert_one(
                {'actor':name,#이름
                'actor_detail':actor_dict,#기본정보 사전형태
                'actor_hit': hitIndex, #흥행지수
                'date':month,    #조회 설정 과거 기준
                'movie_list':hitMovieAfterList, #대표적 출연영화
                'appearance_number':appearanceNum,#기간내 출연건수
                'grade':grade#기간내 순위
                
                })
            print('insert 결과 :', ret)

if __name__ == '__main__':
    pastPeriod, pages = input('2019-11 형식으로 과거일 입력, 페이지 수 입력하시오.').split(',')
    #pastPeriod = "2019-11" #2년
    # lookupAndInsertDB(pastPeriod) #과거 기준 기간입력 조회
    #page =2
    lookupAndInsertDB(pastPeriod,int(pages)) #과거 기준 기간입력 및 페이지 조회

        


 


