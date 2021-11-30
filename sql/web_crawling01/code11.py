from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.yahoo.com/most-active?guccounter=1"
res = req.get(url)
soup = BS(res.text,"html.parser")

# tds = soup.select(" tbody tr td:nth-child(2)")
# name = []
# for i in tds:
#     name.append(i.get_text(strip=True))

# print(name)

print(res.raise_for_status)

data_list= []
tds = soup.select("tbody tr")
for i in tds:
    temp = []
    if len(i.select(" td:nth-child(2)")) == 0:
        continue
    i1= i.select(" td:nth-child(2)")[0].get_text(strip=True)
    i2= i.select(" td:nth-child(3)")[0].get_text()
    i3= i.select(" td:nth-child(4)")[0].get_text()
    i4= i.select(" td:nth-child(5)")[0].get_text()
    # i3= i.select(" td:nth-child(4)")[0].get_text()
    # b1 = i1.get_text()
    # b2 = i2.get_text()
    # b3 = i3.get_text()
    temp.append(i1)
    temp.append(i2)
    temp.append(i3)
    temp.append(i4)
    # temp.append(i3)
    # print(temp)
    data_list.append(temp)
print(data_list)

# f = open("nasdac.csv","w")

# for i in range(len(data_list)):
#     strl = " ".join(data_list[i])
    
#     f.write(strl+"\n")

#scr-res-table > div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\).W\(100\%\) > table > tbody > tr:nth-child(1) > td.Va\(m\).Ta\(start\).Px\(10px\).Fz\(s\)

#scr-res-table > div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\).W\(100\%\) > table > tbody > tr:nth-child(2) > td.Va\(m\).Ta\(start\).Px\(10px\).Fz\(s\)

#scr-res-table > div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\).W\(100\%\) > table > tbody > tr:nth-child(2) > td:nth-child(5) > fin-streamer > span