import requests
# 데이터를 요청 할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugun' : '',
    'store' : ''
}
response = requests.post(url,data=from_data)

# 터미널에서 pip install beautifulsoup4 실행
from bs4 import BeautifulSoup
#  response 에 있는 문자열로 된 데이터를 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text,'html.parser')

# 원하는 정보를 추출
#  #contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
# soup.select('tbody > tr')  tbody가 한개 밖에 없어서 가능 만약 여러개면 가장 먼저 만나는 tbody
sotre_rows = soup.select(str_table_rows)
store_lists = []
for row in sotre_rows:        
    store_lists.append(
        (
            row.select('td')[0].text.strip(),
            row.select('td')[1].text.strip(),
            row.select('td')[2].text.strip(),
            row.select('td')[3].text.strip(),
            row.select('td')[5].text.strip()
        )
    )    
print(store_lists)    