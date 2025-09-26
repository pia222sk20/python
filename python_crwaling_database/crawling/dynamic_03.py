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
# driver.maximize_window() # 전체 화면으로 실행  옵션
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
time.sleep(1)

# 더보기 클릭(국산모델 top10)
#   //*[@id="autodanawa_gridC"]/div[3]/article/main/div/div[3]/div[1]/a
more = driver.find_element(By.XPATH,'//*[@id="autodanawa_gridC"]/div[3]/article/main/div/div[3]/div[1]/a')
more.click()
time.sleep(2)
# 기간선택 레디오 버튼
radio =  driver.find_element(By.CSS_SELECTOR,"input[name='rdoMonthPeriod'][value='period']")
radio.click()
time.sleep(1)

select = Select(driver.find_element(By.ID,'selMonthFrom'))
select.select_by_value('2023')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayFrom'))
select.select_by_value('01')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selMonthTo'))
select.select_by_value('2023')
time.sleep(1)
select = Select(driver.find_element(By.ID,'selDayTo'))
select.select_by_value('12')

#조회 버튼 클릭  //*[@id="monthPeriodDiv"]/span[2]/input
# 속성중에 disalble = True 인 엘리먼트는 사용자 클릭을 막아놓음
btn = driver.find_element(By.XPATH,'//*[@id="monthPeriodDiv"]/span[2]/input')
driver.execute_script("arguments[0].click()", btn)  # 사용자 마우스 클릭 이벤트를 발생
# driver.execute_script("selectRecord('period');")  # 직접 실행

time.sleep(3)

# 셀리니움 문법을 이용해서 원하는 태그의 속한 텍스트를 추출
soup = BeautifulSoup(driver.page_source,'html.parser')  
tr_lists = soup.select('#autodanawa_gridC > div.gridMain > article > main > div > table > tbody > tr')
for tr in tr_lists:
    try:
        td_lists = tr.select('td')
        print(td_lists[3].select_one('td.title a').text.strip(), end='\t')
        print(td_lists[4].text.strip(), end='\t')
        print(td_lists[5].text.strip())
        
    except Exception as e:
        pass


time.sleep(10)
# 브라우져 종료
driver.quit()