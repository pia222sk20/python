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
select
b.userID,
b.prodName,
c.code_name as group_name,
b.price,
b.amount
from buytbl b
left join code_master c
	on c.code_type='GRPN'
	and c.code_value = b.groupName
where c.use_yn = 'Y'
order by c.display_order 
;

-- usertbl  buytbl 연결 회원별 구매내역
-- 두 테이블을 회원정보 기준으로 회원정보가 누락없이 모드 출력
-- 각 회원별로 구매액 총합, 평균, 구매횟수

select
u.userid ,
u.name,
sum(b.price) total_price,
round(avg(b.price),2) avg_price,
count(*) cnt
from usertbl u
join buytbl b
	on u.userID = b.userID
group by u.userid    
order by total_price desc, avg_price desc, cnt desc
;

-- 공통코드에서 주소와 매핑
-- 공통코드에 있는 정보를 이용해서 출력
select
u.name,
c.code_name as addr_name,
b.prodName,
b.price,
b.amount
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'ADDR'
    and c.code_value = u.addr
order by c.display_order
;

-- 통신사 코드 추가
-- mobile1 을 code_master 의 MOB1에 해당하는 code_name 연결해서 통신사까지 출력
select
u.name,
c.code_name as addr_name,
b.prodName,
b.price,
b.amount,
cm.code_name
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'ADDR'
    and c.code_value = u.addr
left join code_master cm
	on cm.code_type = 'MOB1'
    and cm.code_value = u.mobile1
order by u.name
;

-- 상품분류 코드 추가
-- groupname을 code_master의 GRPN코드와 연결하고 총 구매금액 계산
select
u.userID,
u.name,
c.code_name as addr_name,
b.prodName,
b.price,
b.amount,
b.price * b.amount as total_price,
cm.code_name as code_name_mob1 ,
cmt.code_name as code_name_grpn
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'ADDR'
    and c.code_value = u.addr
left join code_master cm
	on cm.code_type = 'MOB1'
    and cm.code_value = u.mobile1
left join code_master cmt
	on cmt.code_type='GRPN'
	and cmt.code_value = b.groupname
where 
	c.use_yn='Y' or cm.use_yn='Y' or cmt.use_yn='Y'
order by u.name
;

-- 뷰 생성이후 사용
select * from user_buy_code_tbl;
-- GetUserList 프로시져 생성후
call GetUserList();
-- GetUserByAddr  프로시져 생성후
call GetUserByAddr('경남');
call GetUserByAddr('');
call GetUserByAddr(null);
-- call GetUserByAddr();  매개변수는 반드시 값을 줘야함

-- ManageCode 프로시져 생성후
call ManageCode('ADDR','대전','대전광역시',7,'Y','delete');
-- invalide action! update or insert
-- ADDR에 부산코드가 없음
select * from code_master where code_type = 'ADDR';
-- 부산, 부산광역시  공통코드에 추가
call ManageCode('ADDR','부산','부산광역시',6,'Y','insert');
select * from code_master where code_type = 'ADDR';
-- 수정
call ManageCode('ADDR','서울','서울특별시',0,'Y','update');
select * from code_master where code_type = 'ADDR';

-- 구매내역 집계 프로시져
-- 서울지역에서 구매건수
select 
count(*)
from usertbl u
join buytbl b
	on u.userID = b.userID
where u.addr = '경남'
;

-- GetPurchaseSummaryByAddr 프로시져 생성후
call GetPurchaseSummaryByAddr(Null);
-- 트랜잭션 에러처리
call AddCodeWithTransaction('ADDR','서울','서울특별시',0,'Y');




