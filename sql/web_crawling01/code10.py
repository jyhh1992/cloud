from bs4 import BeautifulSoup as BS
import requests as req
import csv

url = "https://finance.naver.com/sise/lastsearch2.nhn"
res = req.get(url)
soup = BS(res.text, "html.parser")

data_list= []
tds = soup.select("table.type_5 tr")
for i in tds:
    temp = []
    if len(i.select(" a.tltle")) == 0:
        continue
    i1= i.select(" a.tltle")[0].get_text(strip=True)
    i2= i.select(" td.number:nth-child(3)")[0].get_text()
    i3= i.select(" td.number:nth-child(4)")[0].get_text()
    # b1 = i1.get_text()
    # b2 = i2.get_text()
    # b3 = i3.get_text()
    temp.append(i1)
    temp.append(i2)
    temp.append(i3)
    # print(temp)
    data_list.append(temp)
print(data_list)

# for i in enumerate(temp) :
#     temp[i] = temp[i].replace(',','')

f = open("kospi1.csv","w")

for i in range(len(data_list)):
    strl = " ".join(data_list[i])
    
    f.write(strl+"\n")


f.close()


# import csv
# with open('kospi.csv', "w", encoding="utf-8", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(temp)





# csvFile = open('kospi.csv', "w+", encoding="utf-8", newline='')

# try:
#     writer = csv.writer(csvFile)
#     for i in range(len(temp)):
#         writer.writerow( (temp[i])

# finally:
#     csvFile.close()  

# tag = soup.select(" a.tltle")
# for td in tag:
#     a = td.get_text(strip=True)
#     print(a)

# tag2 =  soup.select(" td.number:nth-child(3)")
# for i in tag2:
#     b = i.get_text()
#     print(b)

# tag3 =  soup.select(" td.number:nth-child(8)")
# for i in tag3:
#     b = i.get_text()
#     print(b)


#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(8)

#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(3)

