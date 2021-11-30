from bs4 import BeautifulSoup as BS
import requests as req
url = "http://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser")

print(soup.title)
print(soup.title.text)
print(soup.title.string)
