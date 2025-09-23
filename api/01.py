# .env에 있는 값
# PUBLIC_ENCODE_KEY='U5i63xpIWM48raIRQBYpUXbA%2FwKd0iO6n%2Fn1%2BJISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w%3D%3D'
# PUBLIC_DECODE_KEY='U5i63xpIWM48raIRQBYpUXbA/wKd0iO6n/n1+JISyoEW1gWcEiz2No2fHPeid5TZoQN0HV85WyGv6LPwaQ8n4w=='


from dotenv import load_dotenv
import os
import requests
# .env 로드
load_dotenv()
P_KEY = os.getenv('PUBLIC_DECODE_KEY')
print(f'P_KEY : {P_KEY[-10:]}')
# 데이터를 요청 할 주소
base_url = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail'
# 서버에 보낼 데이터(1페이지를 보여달라는 의미로)
params_data = {
    'serviceKey': P_KEY,
    'page': 1,
    'perPage': 10
}
import json
response = requests.get(base_url, params=params_data)
data_dict = response.json()
json_print = json.dumps(data_dict,indent=4,ensure_ascii=False)
print(json_print)