from bs4 import BeautifulSoup as BS
import requests as req

url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = req.get(url)
print(res.raise_for_status)
soup = BS(res.text,"html.parser")


# tds = soup.select("table td.title")
# print(tds)

tds = soup.select("table tr")
data_list= []
for i in tds:
    temp = []
    if len(i.select('td.title'))== 0:
        continue
    i1= i.select("td.title")[0].get_text(strip=True)
    i2= i.select('td>div.rating_type>strong')[0].get_text(strip=True)
    temp.append(i1)
    temp.append(i2)
    data_list.append(temp)

print(data_list)


#content > table > tbody > tr:nth-child(2) > td.title > a

#content > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > strong