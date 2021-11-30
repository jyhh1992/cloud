#  네이버 금융 페이지의 환율 공시 정보 기반 환율 계산기
####1. find(), split() 테스트

# s = 'apple'
# print(s.find('e'))
# arr = s.split('p')
# print(arr)

# b = "여기는 한국전파통신협회 입니다."
# num = [1,2,3,4]
# print(b.find('여기'))
# print(num[1:3])
# pos = s.find('여기는 ')
# pos = pos+4
# print(b[pos:pos+2])

####2. split()
b = "지금은 9월 입니다."
arr = b.split('지금은 ')
print(arr)
print(arr[1].split('월')[0])

####3. split() 
print(b.split('지금은 ')[1].split('월')[0])