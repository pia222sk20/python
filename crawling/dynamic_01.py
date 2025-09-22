
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
import time
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')
time.sleep(3)
print('브라우져가 성공적으로 열렸습니다.')
# 검색창 요소 찾기 (id 가 'ipt_keyword_recruit' 인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME,'gLFyf')
#검색창에 파이썬  입력
search_input.send_keys('파이썬')
time.sleep(3)
# Enter키 누르기
search_input.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()