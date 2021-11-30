from bs4 import BeautifulSoup as BS
import requests as req

# url = "http://naver.com"
# res = req.get(url)
# soup = BS(res.text, "html.parser")

# 네이버 홈페이지의 html 출력

# multiline string
html ="""
<html>
  <body>
    <div class="hi">&nbsp;&nbsp;&nbsp; 안녕하세요. </div>
  </body>
</html>
"""

soup = BS(html, "html.parser")
tag = soup.select("div")
print(tag.get_text(strip=True))



