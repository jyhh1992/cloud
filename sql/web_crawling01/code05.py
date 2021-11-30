from bs4 import BeautifulSoup as Bs
import requests as req

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = Bs(res.text,"html.parser")


tds = soup.find_all("td")
# print (tds)

names=[]

for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    names.append(td.get_text(strip=True))

print(names)

#     print(td.string)
#     print(td.get_text(strip=True))

prices = []
for td in tds:
    if "class" in td.attrs:
        if "sale" in td.attrs["class"]:
            prices.append(td.get_text(strip=True))

print(prices)

f = open("finance.csv","w")

for i in range(len(names)):
    f.write(names[i]+","+prices[i] + "\n")

f.close()
# for s in td.stripped_strings:
#     names.append(td.get_text(strip=True))

# for td in tds:
#     print(td.strings)
#     for s in td.strings:
#         print(s)

# for s in td.stipped_strings:
#     print(s)



# body = res.text

# print(soup.title)

# #print(captuers)
# print("---------------")
# print("환율 계산기")
# print("---------------")
# print("")

# for c in captuers:
#     print(c[0] + " : " + c[1])
    
# print("")
# #usd =captuers[0][1].replace(",", "")
# usd = float(captuers[0][1].replace(",", ""))
# won = input("달러로 바꾸길 원하는 금액(원)을 입력해 주세요. : ")
# won = int(won)
# dollar = won / usd
# dollar = int(dollar)
# print(f"{dollar} 달러 환전되었습니다.")

