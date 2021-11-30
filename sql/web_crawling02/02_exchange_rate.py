#  네이버 금융 페이지의 환율 공시 정보 기반 환율 계산기
import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')
html = res.text
#pos = html.find('미국 USD') # 데이터가 있는지 찾음.
#print(pos)

s = html.split('<span class="value">')[1].split('</span')[0]
print(s)