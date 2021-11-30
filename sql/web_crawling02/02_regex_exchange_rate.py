import requests as req
import re

url ='https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.get(url)
body = res.text
# match()
# findall()
# 정규표현식 
#r = re.compile(r"미국 USD.*value\">(.*)</")
#DOT
# .은 \n을 포함하지 않는다. => re.DOTALL 설정
#r = re.compile(r"미국 USD.*value\">(.*)</", re.DOTALL)
#r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL) #? : 좁은 범위로 제한 
# 다른 국가의 환율도 같이 가져오도록 하기 위한것
#r = re.compile(r"blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL) 
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL) 
captuers = r.findall(body)
#print(captuers)

print("---------------")
print("환율 계산기")
print("---------------")
print("")
for c in captuers:
  print(c[0] + " : " + c[1])

print("")
#usd =captuers[0][1].replace(",", "")
usd = float(captuers[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해 주세요. : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")

