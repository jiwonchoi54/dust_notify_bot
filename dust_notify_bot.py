## 미세먼지 알림 봇을 만들어보자 ##
## 현재 미세먼지 상황을 네이버에서 크롤링해서 라인으로 알려줄게 ##
import requests
from bs4 import BeautifulSoup 
from datetime import datetime

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80%CC%BC&oquery=%CC%BC&tqi=UZIChlpVuE0ssv1L3T8ssssstHw-098837'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
now=datetime.now()

print('\n\n현재시각 : ', end='')
print(now)
print()

templist = soup.select('tbody > tr')
#print(templist)

list1 = []  
for temp in templist:
    list1.append(temp.text)

list2 = []
for num in range(1,19) :
    list2.append(list1[num])
    num += 1

for i in list2 :
    print(i)

#Api 및 Token 정보
url = 'https://notify-api.line.me/api/notify'
token = {'Authorization': 'Bearer oU3iH5XAhs0nu70ZQQiOWbqsgnMd1PLZYeW5cP02UWn'}

parameter = {"message" : list2}
response = requests.post(url, headers = token, data = parameter)

print(response.text)
