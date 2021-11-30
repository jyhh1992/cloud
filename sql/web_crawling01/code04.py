from bs4 import BeautifulSoup as Bs
import requests as req

url = "https://www.naver.com/"
res = req.get(url)
soup = Bs(res.text,"html.parser")

print(soup.title)
print(soup.title.text)
print(soup.title.string)