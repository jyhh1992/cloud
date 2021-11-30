import re
s= 'hay'
print(re.match(r'..', s))
print(re.match(r'hay1*', s))

s= 'color'
print(re.match(r'colou?r', s))

s= 'how are you?'
print(re.match(r'how are you\?', s))

#A, B, C, D
s= '이 고기는 A등급 입니다.'
print(re.match(r'이 고기는 [ABCD]등급 입니다\.', s))

s= '이 고기는 A등급 입니다.'
print(s.split('이 고기는 ')[1].split('등급 입니다.')[0])
p = re.findall(r'이 (..)는 (.)등급 입니다\.', s)
print(p)
p = re.findall(r'이 (..)는 ([ABCD])등급 입니다\.', s)
print(p)