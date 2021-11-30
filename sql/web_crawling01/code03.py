import requests as req
import re
url ='https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.get(url)
body = res.text
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