import requests as req

res = req.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=삼성전자')
print(res.text)