from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_ENCODE_KEY')
print(f'P_KEY : {P_KEY[-10:]}')
# 데이터를 요청 할 주소
url = 'http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService'
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
from_data = {
    'serviceKey' : P_KEY,
    'registYy' : 2024,
    'registMt' : 12,
    'vhctyAsortCode' : 2,
    'registGrcCode':1,
    'useFuelCode':6
}
response = requests.get(url,data=from_data)
print(response.text[:500])



url = f"http://apis.data.go.kr/B553881/newRegistInfoService/newRegistInfoService?serviceKey={P_KEY}& registYy=2017&registMt=09&vhctyAsortCode=1&registGrcCode=10&useFuelCode=2&cnmCode=&prposSeNm=1&sexdstn=남자&agrde=2&dsplvlCode=4&hmmdImpSeNm=국산&prye=2016"
result = requests.get(url)
print(result.text)
