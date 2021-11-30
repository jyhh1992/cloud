# 타이핑 게임 제작 및 기본완성

import random
import time
# py sound for linux, pip install pyglet 설치
import pyglet 
import pymysql
import datetime


words = []                                   # 영어 단어 리스트(1000개 로드)
game_cnt = 1                                 # 게임 시도 횟수
corr_cnt = 0                                 # 정답 개수

# DB 생성
conn = pymysql.connect(host='localhost', port=3306, user='rapa01',passwd='1234', db='rec', charset='utf8')
cur = conn.cursor()
cur.execute("""
                CREATE TABLE if not exists wordgameDB(id INTEGER PRIMARY KEY AUTO_INCREMENT, 
                                                     corr_cnt TEXT not null,
                                                     exe_time TEXT not null,
                                                     regdate TEXT not null
                                                     )
            """
            )

with open('./data/word.txt', 'r') as f:  # 문제 txt 파일 로드
    for c in f:
        words.append(c.strip())
print(words)                                 # 단어 리스트 확인

input("Ready? Press Enter Key!")             # Enter Game Start!

start = time.time()                          # Start Time
while game_cnt <= 5:                         # 5회 반복
    random.shuffle(words)                    # List shuffle!
    que_word = random.choice(words)                 # List -> words random extract!

    print()
    print("*Question # {}".format(game_cnt))
    print(que_word)                                 # 문제 출력

    input_word = input()                              # 타이핑 입력
    print()
    
    if str(que_word).strip() == str(input_word).strip():     # 입력 확인(공백제거)
        good_sound = pyglet.resource.media(                  # 정답 소리 재생
            'assets/good.wav',
        )
        good_sound.play()        
        print("Pass!")
        corr_cnt += 1                         # 정답 개수 카운트
    else:
        bad_sound = pyglet.resource.media(              # 오답 소리 재생
            'assets/bad.wav',
        )
        bad_sound.play()        
        print("Wrong!")

    game_cnt += 1                                   # 다음 문제 전환

time.sleep(0.2)  # 단위 : sec, 마지막 문제 소리 재생을 위해 시간 지연
end = time.time()                            # End Time
exe_time = end - start                             # 총 게임 시간

exe_time = format(exe_time, ".3f")                       # 소수 셋째 자리 출력(시간)

# db 테이블 증가

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

# id 자동증가
# 정답수
# 걸린시간
# 저장한 시간

if corr_cnt >= 3:                             # 3개 이상 합격
    print("결과 : 합격")
else:
    print("불합격")
    
# 수행 시간 출력
print("게임 시간 :", exe_time, "초", "정답 개수 : {}".format(corr_cnt))

# sql = """INSERT INTO product VALUES('""" + str(product_code) + """',
# '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F'); """
cur.execute(
    "INSERT INTO wordgameDB(corr_cnt, exe_time, regdate) VALUES (%s, %s, %s)",
    (corr_cnt, exe_time, nowDatetime)
)
conn.commit()
conn.close()

# 시작지점
if __name__ == '__main__':
    pass
