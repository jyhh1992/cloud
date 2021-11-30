from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.nifc.gov/fire-information/statistics/wildfires"
res = req.get(url)
soup = BS(res.text,"html.parser")

# tds = soup.select(" tbody tr td:nth-child(2)")
# name = []
# for i in tds:
#     name.append(i.get_text(strip=True))

# print(name)

print(res.raise_for_status)

data_list= []
tds = soup.select("tbody")
for i in tds:
    temp = []
    if len(i.select(" td.tableCol1type")) == 0:
        continue
    i1= i.select(" td.tableCol1type")[0].get_text(strip=True)
    i2= i.select(" td:nth-child(2)")[0].get_text()
    i3= i.select(" td:nth-child(3)")[0].get_text()
    # i3= i.select(" td:nth-child(4)")[0].get_text()
    # b1 = i1.get_text()
    # b2 = i2.get_text()
    # b3 = i3.get_text()
    temp.append(i1)
    temp.append(i2)
    temp.append(i3)
    # temp.append(i3)
    # print(temp)
    data_list.append(temp)
print(data_list)

#block-nifc-content > div > article > div > div > div > div.block.block-layout-builder.block-inline-blockrich-text-editor > div > div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > table > tbody > tr:nth-child(3) > td:nth-child(1)

#block-nifc-content > div > article > div > div > div > div.block.block-layout-builder.block-inline-blockrich-text-editor > div > div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > table > tbody > tr:nth-child(4) > td.tableCol1type

#block-nifc-content > div > article > div > div > div > div.block.block-layout-builder.block-inline-blockrich-text-editor > div > div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > table > tbody > tr:nth-child(5) > td.tableCol1type

#block-nifc-content > div > article > div > div > div > div.block.block-layout-builder.block-inline-blockrich-text-editor > div > div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > table > tbody > tr:nth-child(4) > td:nth-child(2)

#block-nifc-content > div > article > div > div > div > div.block.block-layout-builder.block-inline-blockrich-text-editor > div > div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-hidden.field__item > table > tbody > tr:nth-child(5) > td:nth-child(3)



# f = open("nasdac.csv","w")

# for i in range(len(data_list)):
#     strl = " ".join(data_list[i])
    
#     f.write(strl+"\n")