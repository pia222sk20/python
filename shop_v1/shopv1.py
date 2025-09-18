# pip install pymysql # mysql을 접속할 수 있는 라이브러리
# pip install dotenv  # 환경변수 .env를 로드할수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
print('접속성공')

# 2. 각 테이블별 
    # C - insert
    # R - select
    # U - update
    # D - delete

# 고객 - customer
def create_customer(name):
    sql = 'insert into customer values(null,%s)'
    with conn.cursor() as cur:
        cur.execute(sql, name)
        conn.commit()
    print('고객추가 완료')

# [
#         {"회원아이디": "user01", "회원이름": "홍길동"},
#         {"회원아이디": "user02", "회원이름": "이몽룡"},
#         {"회원아이디": "user03", "회원이름": "성춘향"}
#     ]

def readAll_customers(isDict = False):
    sql = 'select * from customer'     
    result = []
    if isDict:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql)
            for c in cur.fetchall():             
                print(f"{c['customer_id']}  {c['name']}")
    else:
        with conn.cursor() as cur:
            cur.execute(sql)
            for c in cur.fetchall():            
                print(f'{c[0]}  {c[1]}')
                result.append(
                    {"회원아이디": c[0], "회원이름": c[1]}
                    )    
    print(f'조회완료')    
    return result

def update_customer(customer_id, name):
    sql = '''
        update customer 
            set name = %s
        where customer_id = %s
    '''

    with conn.cursor() as cur:
        cur.execute(sql, (name,customer_id)  )    
    conn.commit()
    print(f'업데이트 되었습니다.{customer_id} {name}')

def delete_customer(customer_id):
    sql = 'delete from customer where customer_id=%s'
    with conn.cursor() as cur:
        cur.execute(sql,customer_id)
    conn.commit()
    print(f'삭제되었습니다. {customer_id}') 

create_customer('abc')
readAll_customers()
update_customer(1,'abc')
delete_customer(1)


# 3.메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품별 구매회수, 평균구매액

# 4 기능구현과 테스트가 되면..  streamlit으로 UI 구성 - 템플릿화면을 보고 유사한 형태로 구현

# conn.close()  # 접속해제