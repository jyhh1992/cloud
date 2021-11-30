import codecs
from bs4 import BeautifulSoup as BS
f = codecs.open("./test.html", 'r')
html = f.read()
soup = BS(html, "html.parser")
print(soup)

#enabled
#arr = soup.select("input:disabled")
#arr = soup.select("input:enabled")
#print(arr)

#disabled
#arr = soup.select("input:enabled")
#print(arr)

#checked
#arr = soup.select("input:checked")
#print(arr)

#empty
# arr1 = soup.select("input:empty")
# arr2 = soup.select("label + input:empty")
# print(arr1)
# print(arr2)

#first-child
# arr = soup.select("b:first-child")
# print(arr)

#last-child
# arr = soup.select("tbody tr:first-child")
# print(arr)

#first-of-type
# arr = soup.select("tbody td:first-of-type")
# print(arr)

#last-of-type
# arr = soup.select("tbody td:last-of-type")
# print(arr)

# not
# arr = soup.select("b:not(:first-of-type)")
# print(arr)

# nth-child()
# arr = soup.select("tbody td:nth-child(3)")
# print(arr)

# nth-of-type()
# arr = soup.select("tbody td:nth-of-type(3)")
# print(arr)