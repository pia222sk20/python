select * from code_master where use_yn = 'Y';
select * from usertbl;

-- 서울 대신에 코드에있는 값을 불러와서 서울특별시 .. 이런형태로 고객정보 조회
-- join 해야하고... 매칭되는 기준 컬럼  code_value & addr
-- 테이블 명은 별칭

select 
u.userid,
u.name,
u.addr,
c.code_name
from usertbl u
left join code_master c
	on u.addr = c.code_value
    and c.code_type = 'ADDR'
where c.use_yn ='Y'    
;    

-- 구매정보와 상품 분류를 연결
-- 전자대신에 전자제품처럼 보기좋게 코드마스터에서 조인해서 출력
-- buytbl , code_master
select * from buytbl;

