from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

url = 'https://auto.danawa.com/auto/?Work=record'
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window() # 전체 화면으로 실행  옵션
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
try:
    # 페이지 초기 로딩 대기 (결과를 감싸는 recordSection 클래스를 기다림)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "recordSection"))
    )
    year_to_select = '2024'
    # 1. '년도' 선택 (Select 클래스 사용)
    print(f"1. '{year_to_select}년'을 선택합니다.")
    year_select_element = driver.find_element(By.ID, 'selMonth')
    select_year = Select(year_select_element)
    select_year.select_by_value(year_to_select)
    
    # 년도 선택 후, 데이터가 로드될 시간을 줌
    time.sleep(2)
    
    # 2. 1월부터 12월까지 순차적으로 조회
    for month in range(1, 13):
        try:
            # StaleElementReferenceException을 피하기 위해 매번 요소를 새로 찾습니다.
            month_value = f"{month:02d}" # 월을 '01', '02' 형태의 문자열로 변환
            print(f"==> '{month_value}월'을 선택합니다.")            
            month_select_element = driver.find_element(By.ID, 'selDay')
            select_month = Select(month_select_element)
            select_month.select_by_value(month_value)
            
            # 월 선택 후 데이터가 갱신될 때까지 대기합니다.
            # 예시: 판매실적 테이블의 첫 번째 행이 보일 때까지 기다림
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".recordTable.short tbody tr"))
            )
            print(f"'{month_value}월' 데이터 로딩 완료.")
            # 브라우져의 텍스트를 추출
            soup = BeautifulSoup(driver.page_source,'html.parser')
            tr_datas = soup.select('#autodanawa_gridC > div.gridMain > article > main > div > div:nth-child(3) > div.left > table > tbody > tr')
            for row in tr_datas:
                td_datas = row.select('td')
                print(td_datas[0].text, td_datas[1].text,td_datas[2].text,td_datas[3].text)
            # (여기에 각 월의 데이터를 수집하는 코드를 추가할 수 있습니다)
            
            time.sleep(1) # 시각적 확인을 위한 짧은 대기
            
        except Exception as e:
            print(f"'{month_value}월'을 처리하는 중 오류 발생: {e}")
            continue # 오류가 발생해도 다음 월로 넘어감

except Exception as e:
    print(f"자동화 중 오류가 발생했습니다: {e}")

finally:
    print("\n5초 후 브라우저를 종료합니다.")
    time.sleep(5)
    driver.quit()