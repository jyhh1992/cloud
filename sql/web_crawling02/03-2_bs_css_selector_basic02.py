html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <style>
    table{
      border-collapse: collapse;
      border:1px solid black;
    }
    table td, table th{
      border: 1px solid black;
    }
    table tr:first-child th{
      border-top: 0;
    }
    table tr:last-child td {
      border-bottom: 0;
    }
    table tr td:first-child,
    table tr th:first-child{
      border-left: 0;
    }
    table tr td:last-child,
    table tr th:last-child{
      border-right: 0;
    }
  </style>

</head>
<body>
  <div style="max-width: 960px; margin: auto; padding-top:20px;">
    <h1>호텔 예약 확인</h1>
    <input type="checkbox" />
    <span>이용 약관을 충분히 숙지하였으며 이에 동의합니다.</span>
    <br>
    <input type="checkbox" checked />
    <span> 14세 이상 보호자 동행에 동의합니다.</span>
    <br>
    <input type="checkbox" disabled />
    <span>5인 이상 단체 예약입니다.</span>
    <br>
    <div>
      <label for="tel">전화번호:</label>
      <input type="text" />
    </div>
    <br>
    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>이름</th>
          <th>가격</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>김철수</td>
          <td>
            <b>120,000</b>
          </td>
        </tr>
        <tr>
          <td>2</td>
          <td>이영희</td>
          <td>
            <b>200,000</b>
          </td>
        </tr>
        <tr>
          <td>3</td>
          <td>김서영</td>
          <td>
            <b>250,000</b>
          </td>
        </tr>
        <tr>
          <td>4</td>
          <td>서정희</td>
          <td>
            <b>300,000</b>
          </td>
        </tr>
      </tbody>
    </table>
    <h3>총 가격</h3>
    <div>
      <b>KRW : </b>
      <b>850,000</b>
    </div>
  </div>
</body>
</html>
'''
from bs4 import BeautifulSoup as BS
soup = BS(html, "html.parser")

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
arr = soup.select("b:not(:first-of-type)")
print(arr)

# nth-child()
arr = soup.select("tbody td:nth-child(3)")
print(arr)

# nth-of-type()
arr = soup.select("tbody td:nth-of-type(3)")
print(arr)