from bs4 import BeautifulSoup as bs
import requests as req
import csv
# url = "http://naver.com"
# res = req.get(url)
# soup = bs(res.text, 'html.parser')
import re
url="https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = bs(res.text, 'html.parser')
# print('soup :', soup, type(soup))
tds = soup.find_all('td')
# print(tds)
names = []
price = []
namePrice = {}
for td in tds:
    if 'class' in td.attrs and 'sale' in td.attrs['class']:
        price.append(td.get_text(strip=True))
    if len(td.find_all('a'))==0:
        continue #no value  pass.
    else:
        names.append(td.get_text(strip=True))
for i in range(len(names)):
    namePrice[names[i]]=price[i]
# print('names : ', names)
# print('price :', price)
print(namePrice)
#file save
csvFile = open('nameprice.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    for i in range(len(names)):
        writer.writerow( (names[i], price[i]))
finally:
    csvFile.close()
# exchange from won to us dollar
won = 10000
usd = price[0].replace(",","")
dollar = won / float(usd)
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")