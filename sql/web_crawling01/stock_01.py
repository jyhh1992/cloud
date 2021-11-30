from bs4 import BeautifulSoup as BS
import requests as req
import pymysql

# DB 생성
conn = pymysql.connect(host='localhost', port=3306, user='rapa01',passwd='1234', db='stockdb', charset='utf8')
cur = conn.cursor()
cur.execute("""
                CREATE TABLE if not exists yahooDB(id INTEGER PRIMARY KEY AUTO_INCREMENT, 
                                                     Name TEXT not null,
                                                     Price float not null,
                                                     Change_c varchar(8) not null,
                                                     Change_rate  varchar(8) not null
                                                     )
            """
            )


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
    

    # temp.append(i1)
    # temp.append(i2)
    # temp.append(i3)
    # temp.append(i4)
    # temp.append(i3)
    # print(temp)
    cur.execute(
    "INSERT INTO yahooDB(Name, Price , Change_c , Change_rate ) VALUES (%s, %s, %s, %s)",
    (i1, i2, i3,i4))


conn.commit()
conn.close()

if __name__ == '__main__':
    pass

# f = open("nasdac.csv","w")

# for i in range(len(data_list)):
#     strl = " ".join(data_list[i])
    
#     f.write(strl+"\n")

